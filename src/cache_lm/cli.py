from __future__ import annotations

import argparse
import json

from langchain_core.messages import HumanMessage

from cache_lm.checkpointing import sqlite_checkpointer
from cache_lm.env import get_env
from cache_lm.graph import compiled_graph
from cache_lm.graph import create_graph
from cache_lm.manual import get_manual
from cache_lm.prompts import system_prefix_hash


def manual_stats() -> dict[str, object]:
    manual = get_manual()
    return {
        "path": str(manual.path),
        "bytes": len(manual.bytes),
        "manual_sha256": manual.sha256,
        "system_prefix_hash": system_prefix_hash(manual_text=manual.text),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cache-lm")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "manual-stats",
        help="Print basic information about the operations manual.",
    )

    run_parser = subparsers.add_parser(
        "run",
        help="Run one graph turn (stubbed or LLM, depending on CACHE_LM_MODE).",
    )
    run_parser.add_argument(
        "--input",
        required=True,
        help="User input for a single turn.",
    )
    run_parser.add_argument(
        "--thread-id",
        default=None,
        help="Thread identifier for persistence (requires --checkpoint-db).",
    )
    run_parser.add_argument(
        "--checkpoint-db",
        default=None,
        help=("SQLite DB path for persistence. If set, state is persisted per "
              "--thread-id across runs."),
    )
    run_parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full final state as JSON.",
    )
    run_parser.add_argument(
        "--show-metrics",
        action="store_true",
        help="Print per-expert TTFT/latency metrics (if available).",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "manual-stats":
        stats = manual_stats()
        print(f"path: {stats['path']}")
        print(f"bytes: {stats['bytes']}")
        print(f"manual_sha256: {stats['manual_sha256']}")
        print(f"system_prefix_hash: {stats['system_prefix_hash']}")
        return 0

    if args.command == "run":
        thread_id = args.thread_id or get_env("CACHE_LM_THREAD_ID")
        checkpoint_db = args.checkpoint_db or get_env("CACHE_LM_CHECKPOINT_DB")

        if thread_id and not checkpoint_db:
            raise SystemExit(
                "--checkpoint-db is required when --thread-id is set")

        config = None
        if thread_id:
            config = {"configurable": {"thread_id": thread_id}}

        if checkpoint_db:
            if not thread_id:
                raise SystemExit(
                    "--thread-id is required when --checkpoint-db is set")
            with sqlite_checkpointer(checkpoint_db) as checkpointer:
                graph = create_graph().compile(checkpointer=checkpointer)
                result = graph.invoke(
                    {"messages": [HumanMessage(content=args.input)]},
                    config=config,
                )
        else:
            graph = compiled_graph()
            result = graph.invoke(
                {"messages": [HumanMessage(content=args.input)]},
                config=config,
            )

        if args.json:
            print(json.dumps(result, indent=2, default=str))
            return 0

        print(result.get("response", ""))
        if args.show_metrics:
            ttft = result.get("ttft_ms_by_expert") or {}
            latency = result.get("latency_ms_by_expert") or {}
            if ttft:
                print("\nmetrics:")
                ordered_experts = [
                    "compliance_auditor",
                    "technical_specialist",
                    "support_concierge",
                ]
                for expert in ordered_experts:
                    if expert not in ttft:
                        continue
                    ms = ttft[expert]
                    lat_ms = latency.get(expert)
                    if lat_ms is None:
                        print(f"- {expert}: ttft_ms={ms:.1f}")
                    else:
                        print(
                            f"- {expert}: ttft_ms={ms:.1f} latency_ms={lat_ms:.1f}"
                        )
        return 0

    raise ValueError(f"Unhandled command: {args.command}")
