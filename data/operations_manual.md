# Banking Internal Operations and Compliance Manual

## 1) Purpose, scope, and governance

### 1.1 Manual purpose

**Purpose.**
This Internal Operations & Compliance Manual (“Manual”) defines the bank’s minimum required operational and compliance standards and the day-to-day procedures used to meet legal, regulatory, and internal control obligations. It provides a single reference for how work must be performed, documented, approved, escalated, and evidenced across the bank’s operations.

**What this Manual covers**

- Standard operating procedures (SOPs) for core operational processes (e.g., customer onboarding support, payments operations, reconciliations, exception handling).
- Compliance requirements and control steps embedded in operational workflows (e.g., KYC/AML checks, sanctions screening escalation, record retention requirements).
- Roles and responsibilities (including segregation-of-duties requirements) and escalation routes.
- Evidence and recordkeeping standards (what to capture, where to store it, retention period references).
- Issue, incident, and breach reporting requirements (what constitutes an incident, how to report, response timelines).
- Governance requirements for maintaining, updating, and approving policies/procedures.

**What this Manual does not cover**

- Legal interpretations or external legal advice (refer to Legal).
- Detailed system architecture, source code, or security exploitation techniques (refer to IT/Security technical standards).
- Product marketing materials or customer-facing terms and conditions (refer to Product & Legal documents).
- HR policies not directly tied to operational/compliance execution (refer to HR Handbook).
- One-off project plans or temporary operational playbooks unless formally incorporated through the change process.

**Audience.**
All employees and contractors performing or supervising operational tasks, and all control functions responsible for oversight (Compliance, Risk, Internal Audit). Where local law requires additional controls, local addenda apply.

**Authority.**
This Manual is mandatory. Non-compliance may result in corrective action, retraining, access restrictions, or disciplinary measures, consistent with HR policy and local law.

---

### 1.2 Scope

**In-scope**

- Business units and functions performing bank operations (Retail, SME, Corporate operations, contact centers, back office).
- Control functions supporting operations (Compliance, Operational Risk, Finance Controls, IT/Security where operationally relevant).
- All channels where operational activity occurs (branch, digital, call center, partner channels) to the extent the bank controls the process.

**Out-of-scope**

- Subsidiaries or affiliates not covered by this governance unless explicitly listed.
- Third-party operations not contractually under the bank’s operational control (covered under Third-Party Risk Management and vendor SOPs).

**Local variations.**
If regional regulation or business requirements conflict with this Manual, the stricter requirement applies. Conflicts must be escalated to Compliance and documented as a controlled exception or local addendum.

---

### 1.3 Definitions and glossary

Below is a baseline glossary. Functions may extend it in their sections, but must not redefine terms inconsistently.

**Key terms**

- **Policy:** A mandatory rule or principle approved by senior management that defines “what must be true.”
- **Standard:** A mandatory requirement that defines minimum acceptable criteria (often measurable).
- **Procedure / SOP:** Step-by-step instructions defining “how to do the work.”
- **Control:** A step designed to prevent, detect, or correct errors/non-compliance (e.g., approval, reconciliation, screening, sampling).
- **Evidence:** Records proving a control or process step was performed (e.g., logs, screenshots, tickets, signed forms).
- **Exception:** An approved deviation from a policy/standard/procedure for a defined period and scope.
- **Breach:** A confirmed violation of policy, law, or regulation requiring reporting and remediation.
- **Incident:** An event that disrupts operations or creates risk (may include breaches, fraud events, security incidents).
- **KYC:** Know Your Customer; identity verification and customer risk assessment process.
- **CDD / EDD:** Customer Due Diligence / Enhanced Due Diligence.
- **AML/CFT:** Anti–Money Laundering / Counter–Financing of Terrorism.
- **Sanctions screening:** Checks against relevant sanctions lists and internal watchlists.
- **SoD:** Segregation of Duties; separation of incompatible tasks to reduce fraud/error risk.
- **RACI:** Responsibility assignment model: Responsible, Accountable, Consulted, Informed.
- **SLAs:** Service level agreements for operational timelines and response times.
- **RTO/RPO:** Recovery Time Objective / Recovery Point Objective for continuity planning.

**Acronyms (common examples)**

- **BU:** Business Unit
- **Ops:** Operations
- **ORM:** Operational Risk Management
- **IA:** Internal Audit
- **QA:** Quality Assurance
- **TAT:** Turnaround Time

---

### 1.4 Ownership and responsibilities

**Manual owner (overall).**
The **Chief Operating Officer (COO)** (or equivalent Operations Head) is accountable for the overall Manual. Day-to-day administration is delegated to the **Operations Governance Lead**.

**Co-owners / control functions.**

- **Compliance:** Owns compliance requirements, regulatory mapping, AML/CFT/sanctions escalation rules, and compliance monitoring expectations.
- **Operational Risk:** Owns operational risk framework content (issue management, KRIs, incident taxonomy, control standards).
- **Finance Controls:** Owns reconciliations, GL controls, suspense handling standards.
- **IT/Security:** Owns operationally relevant security and access control procedures (joiner/mover/leaver workflows, logging/audit trail requirements).

**Section ownership model.**
Each section has an assigned **Section Owner** (Accountable) and **Procedure Owners** (Responsible). Ownership is recorded in the “Ownership Register” (Appendix) and must include:

- Section title and unique ID
- Accountable function/role
- Primary Responsible role(s)
- Review cadence
- Linked policies/standards
- Evidence repositories and system owners (where relevant)

**Three lines of defense alignment.**

- **1st line:** Business and Operations execute processes and controls.
- **2nd line:** Compliance and Risk set requirements and monitor.
- **3rd line:** Internal Audit provides independent assurance.

---

### 1.5 Approval workflow, versioning, and change log

**Document control**

- **Document ID:** OPS-COMP-MAN-001
- **Current version:** vX.Y
- **Effective date:** YYYY-MM-DD
- **Next review date:** YYYY-MM-DD
- **Classification:** Internal

**Change types**

- **Minor change:** Formatting, clarifications, non-control-impacting updates.
- **Material change:** Affects controls, approvals, customer outcomes, regulatory obligations, risk posture, or system processing.

**Approval workflow**

1. **Draft & impact assessment** (Procedure Owner)

   - Identify change type (minor/material)
   - Assess impacted processes, controls, systems, teams
   - Update evidence/recordkeeping requirements if needed

2. **Functional review** (Section Owner + impacted stakeholders)

   - Operations, Compliance, Risk, Finance Controls, IT/Security as applicable

3. **Control function sign-off** (mandatory for material changes)

   - Compliance sign-off if regulatory/compliance impact
   - Operational Risk sign-off if control/risk impact
   - IT/Security sign-off if access/logging/system workflows impacted

4. **Final approval authority**

   - Minor: Section Owner (and Manual admin)
   - Material: COO (or delegated governance committee) + required control function sign-offs

5. **Publication & effective date** (Operations Governance)

   - Publish to controlled repository
   - Notify impacted teams
   - Update training/attestations if required

**Emergency updates**

- Used when immediate risk/regulatory exposure exists.
- Temporary instruction may be issued as an **Operational Bulletin** with a defined expiry date.
- Must be incorporated into the Manual (or retired) within a fixed window (e.g., 30–60 days).

**Versioning rules**

- **Major version (X.0):** Significant restructuring or major policy shifts.
- **Minor version (X.Y):** Material procedure/control changes within same structure.
- **Patch (X.Y.Z):** Typos/clarifications with no control impact.

**Change log requirements**
Each release must include:

- Date, version, author, approver(s)
- Summary of changes
- Change type (minor/material)
- Impacted sections and procedures
- Required training/communication actions
- Links to tickets/approvals

---

### 1.6 Policy hierarchy

This Manual sits within a structured hierarchy to ensure consistency and auditability:

1. **External obligations (highest authority)**

   - Laws, regulations, regulator guidance, supervisory expectations

2. **Internal policies**

   - Bank-wide mandatory principles approved by senior management/Board where required
   - Examples: AML Policy, Sanctions Policy, Data Privacy Policy, Operational Risk Policy

3. **Standards**

   - Minimum required controls and thresholds that implement policies
   - Examples: KYC Standard, Record Retention Standard, Access Control Standard

4. **Procedures / SOPs**

   - Step-by-step execution instructions (this Manual contains many of these)

5. **Job aids**

   - Checklists, scripts, templates, FAQs, decision trees (must align to the procedure)

**Conflict rule.**
Where requirements differ, the stricter requirement applies. Conflicts must be escalated and documented via the exception or addendum process.

**Traceability expectation.**
Every procedure must reference:

- The governing policy/standard
- Required controls
- Evidence and retention requirements
- Owner and review cadence

## 2) Organization, roles, and accountability

### 2.1 Organization structure (business lines + control functions)

The bank operates under a “three lines of defense” model to ensure clear accountability for execution, oversight, and independent assurance.

**Business lines (First Line – executes operations)**

- **Retail Banking** (branches, digital channels, contact center)
- **SME Banking**
- **Corporate/Commercial Banking**
- **Operations (Back Office / Middle Office)**
  Typical sub-functions:

  - Customer Operations (onboarding support, account maintenance)
  - Payments & Settlements
  - Lending Operations (documentation, disbursement support, servicing)
  - Cards Operations (issuance, disputes, chargebacks)
  - Reconciliations & Controls
  - Customer Service Operations

**Control functions (Second Line – sets requirements & monitors)**

- **Compliance** (AML/CFT, sanctions, conduct, regulatory obligations)
- **Operational Risk Management (ORM)** (risk framework, KRIs, issue management)
- **Information Security / IT Risk** (security controls, access, cyber governance)
- **Legal** (contract/legal interpretation; supports policy drafting where needed)
- **Finance Controls** (GL controls, reconciliations, financial reporting controls)

**Independent assurance (Third Line)**

- **Internal Audit (IA)** (independent assessment of control design and effectiveness)

**Governance bodies (examples)**

- Operations Risk & Control Committee (ORCC)
- Financial Crime Committee (FCC)
- Change Advisory Board (CAB) (for system/process changes)
- Incident/Crisis Management Team (for severe events)

---

### 2.2 Roles & responsibilities (RACI for key processes)

The table below defines baseline responsibilities. Each department must maintain a detailed RACI per procedure, but must not weaken these minimum accountabilities.

**RACI definitions**

- **R (Responsible):** Performs the work
- **A (Accountable):** Ultimately answerable; approves outcomes
- **C (Consulted):** Provides input before decisions
- **I (Informed):** Notified after actions/decisions

#### Baseline RACI (core operational processes)

| Key process                               | Operations | Business Line Owner | Compliance | Operational Risk | Finance Controls | IT/Security | Internal Audit |
| ----------------------------------------- | ---------- | ------------------- | ---------- | ---------------- | ---------------- | ----------- | -------------- |
| Customer onboarding (ops processing)      | R          | A                   | C          | C                | I                | C           | I              |
| KYC/CDD review & EDD decision             | R          | A                   | A/C\*      | C                | I                | I           | I              |
| Sanctions screening hit escalation        | R          | I                   | A          | C                | I                | I           | I              |
| Payments processing (STP + exceptions)    | R          | A                   | C          | C                | C                | C           | I              |
| Reconciliations & break resolution        | R          | I                   | I          | C                | A                | I           | I              |
| Operational incident reporting            | R          | A                   | C          | A/C\*            | I                | C           | I              |
| Policy/procedure change (material)        | R          | A                   | A/C\*      | A/C\*            | C                | C           | I              |
| Access provisioning (joiner/mover/leaver) | C          | A                   | I          | C                | I                | R/A         | I              |

- Depending on topic: Compliance is **Accountable** for AML/sanctions decisions; Operational Risk is **Accountable** for operational risk taxonomy/issue governance.

**Minimum expectations**

- Every procedure must name: **Procedure Owner (R)** and **Section Owner (A)**.
- Any process involving regulatory obligations must include **Compliance as C or A**.
- Any process impacting financial reporting or balances must include **Finance Controls as A or C**.

---

### 2.3 Segregation of duties (SoD) rules

**Principle.**
No individual may control a transaction end-to-end across initiation, approval, execution, and reconciliation where this creates unacceptable fraud/error risk.

**Core SoD requirements (minimum)**

1. **Initiation ≠ Approval**

   - The requestor must not be the approver for the same request (e.g., fee waiver, limit override, account closure exception).

2. **Execution ≠ Reconciliation**

   - Staff who execute postings or payment releases must not perform the reconciliation for the same ledger/process.

3. **Maker–Checker for high-risk actions**

   - All high-risk activities require two-person control (maker enters, checker reviews/approves).

4. **Access administration SoD**

   - No single person should both request and grant privileged access.
   - Privileged changes require approvals and audit logs.

5. **Exception handling SoD**

   - Exceptions (policy deviations) must be approved by an independent authority (typically Compliance/Risk/Operations governance), not the requestor’s direct chain alone.

**SoD enforcement**

- Embedded into system entitlements (role-based access control).
- Monitored via periodic access reviews and audit logs.
- Violations must be reported as a control issue and remediated (access removal, process redesign, retraining).

**Temporary SoD breaks**

- Only allowed under documented emergency conditions (e.g., staffing shortage).
- Must be time-bound, approved, and logged as an exception with compensating controls (e.g., enhanced post-review sampling).

---

### 2.4 Delegation of authority / approval limits (signing matrix)

**Purpose.**
The Delegation of Authority (DoA) defines who can approve what, at which thresholds, and under which conditions. It ensures consistent decision-making and prevents unauthorized commitments.

**Approval categories (examples)**

- Customer account exceptions (KYC doc gaps, onboarding overrides)
- Fee waivers and interest adjustments
- Payment release and limit overrides
- Write-offs, settlements, collections actions
- Vendor onboarding, contract approvals (in coordination with Procurement/Legal)
- User access approvals (standard vs privileged)
- Policy/procedure exceptions

**Signing matrix rules**

- Each category must define:

  - **Approval level(s)** (Team Lead / Manager / Head / Committee)
  - **Thresholds** (amount, risk rating, customer tier)
  - **Conditions** (required documentation, independent review)
  - **Validity period** (one-time vs ongoing)
  - **Required consultations** (e.g., Compliance sign-off for AML/sanctions)

- Approvals must be recorded in a controlled system (ticketing/workflow tool), not informal chat.

**Examples of mandatory controls**

- **High-risk customer decisions (EDD acceptance)** → Compliance (Accountable) + Business (Accountable) approval.
- **Privileged access** → IT/Security approval + manager approval + logging requirement.
- **Material operational exceptions** → Operations governance + Compliance/ORM consultation as relevant.

_(The detailed numeric thresholds are maintained in the DoA Appendix and may vary by country/entity.)_

---

### 2.5 Escalation paths (who to call, when)

**Escalation objectives**

- Protect customers and the bank
- Meet regulatory reporting timelines
- Contain incidents quickly
- Ensure decisions are made at the right authority level

**General escalation triggers (minimum)**
Escalate **immediately** (same day, within defined SLA) when:

- Suspected financial crime (AML red flags, sanctions hit, suspicious transactions)
- Confirmed or likely policy breach or regulatory non-compliance
- Material customer harm or complaint with legal/regulatory risk
- Payment issues that may cause loss, mis-posting, or settlement failure
- Data/privacy incidents (mis-sent documents, unauthorized access)
- System outages impacting critical services
- Fraud suspicion (internal or external)
- Control failure (e.g., reconciliation not performed, maker-checker bypassed)

**Standard escalation routes**

1. **Operational issues (process failure, backlog, errors)**

   - Frontline/Processor → Team Lead → Operations Manager → Operations Head
   - Notify Operational Risk if control failure or material impact is possible.

2. **Compliance / financial crime**

   - Processor/Frontline → Team Lead → **Compliance (AML/Sanctions desk)** immediately
   - If confirmed/suspected: Compliance escalates to MLRO/Head of Compliance per local rules.

3. **Security / privacy**

   - Any staff → Team Lead → **InfoSec / IT Risk** immediately
   - Preserve evidence; do not attempt “self-fix” outside procedure.

4. **Financial control breaks**

   - Ops/Finance Ops → Finance Controls → CFO delegate as required.

5. **Severe incidents (customer impact, major outage, significant loss)**

   - Trigger Incident Management process
   - Activate Crisis Management Team if severity threshold is met.

**Escalation SLAs (example structure)**

- **Critical:** immediate notification (≤1 hour), continuous updates until contained
- **High:** same business day (≤4 hours)
- **Medium:** within 1 business day
- **Low:** within 3 business days or scheduled review

**Contact directory**

- The Manual must include an **Escalation Contact List** (role-based, not personal numbers), maintained by Operations Governance:

  - Operations Duty Manager (primary/backup)
  - Compliance AML/Sanctions desk (primary/backup)
  - InfoSec incident hotline / ticket queue
  - Operational Risk on-call
  - Finance Controls contact
  - Internal Audit mailbox (for reporting concerns)
  - Country/entity-specific regulator liaison (Compliance-owned)

## 3) Customer lifecycle operations

### 3.1 Onboarding procedures (Retail, SME, Corporate)

**Objective.**
Ensure customers are onboarded consistently, lawfully, and with appropriate risk controls before any account is activated or transactions are processed.

**Common onboarding stages (all segments)**

1. **Intake & eligibility**

   - Confirm product eligibility, residency/jurisdiction constraints, and required documents.

2. **Identity & entity verification**

   - Retail: verify individual identity and authenticity of documents.
   - SME/Corporate: verify legal existence, registration status, and authorized signatories.

3. **KYC data capture**

   - Collect mandatory customer profile fields (see 3.3).

4. **Risk assessment**

   - Assign initial risk rating based on customer type, geography, product, and intended activity.

5. **Screening**

   - Sanctions/PEP/adverse media screening per policy; escalate potential matches.

6. **Approval & account setup**

   - Maker–checker for account creation and high-risk overrides.

7. **Welcome & disclosures**

   - Provide required customer notices and obtain required consents/acknowledgements.

8. **Activation controls**

   - Restrict account until all minimum controls pass; define what “activation” means per product.

**Segment-specific requirements**

- **Retail**

  - Identity verification method(s) permitted (in-branch, remote, third-party verification) and evidencing requirements.
  - Address verification rules and acceptable substitutes.

- **SME**

  - Business registration, tax ID, ownership structure, authorized signatory verification.
  - Purpose of account and expected transaction profile.

- **Corporate**

  - Full corporate documentation pack, board resolutions (where required), delegated authority, and complex ownership mapping.
  - Relationship manager involvement and heightened controls for cross-border activities.

**Quality checks**

- Sampling-based QA of onboarding files.
- “No account activation without minimum KYC + screening completion,” unless a controlled exception is approved.

---

### 3.2 Customer due diligence (CDD) and enhanced due diligence (EDD)

**CDD (baseline for all customers)**

- Verify identity (person) or legal existence (entity).
- Understand ownership/control and verify beneficial owners as required.
- Understand purpose of relationship and expected activity.
- Screen against sanctions and other required watchlists.
- Assign a risk rating and set monitoring intensity.

**EDD (required for higher-risk relationships)**
EDD is triggered by risk factors such as:

- High-risk geographies, complex ownership, high cash volumes, unusual transaction expectations
- Politically exposed persons (PEPs) or close associates
- Negative/adverse information requiring review
- Certain high-risk products, channels, or industries

EDD minimum steps (in addition to CDD)

- Obtain additional information on source of funds/wealth (as applicable)
- Increased verification of beneficial owners/controllers
- Senior approval (as defined in Delegation of Authority)
- Enhanced ongoing monitoring rules (more frequent review, stricter alert handling)
- Document rationale for accept/decline decision and retain evidence

**Outcomes**

- **Approve:** proceed with conditions (e.g., limits, monitoring).
- **Approve with restrictions:** reduced limits, product constraints, additional documents due.
- **Decline/exit:** follow account closure and offboarding procedures with Compliance guidance.

---

### 3.3 KYC data standards, document requirements, refresh frequency

**KYC data standards (minimum)**
All customer records must be:

- **Complete:** mandatory fields populated; required documents attached
- **Accurate:** verified against source documents or authoritative sources
- **Consistent:** aligned across systems (CRM, core banking, screening tools)
- **Traceable:** any change must have audit trail (who/when/why)
- **Timely:** refreshed per review schedule or trigger events

**Mandatory KYC fields (examples)**

**Retail**

- Full legal name, date of birth, nationality, ID type/number/expiry
- Address, contact info, occupation/employer (as required)
- Purpose of account and expected activity
- Tax residency and declarations (as required by local rules)
- Risk rating, screening results, and approval record

**SME/Corporate**

- Legal entity name, registration number, tax ID
- Registered address, operating address, nature of business/industry
- Ownership structure (including beneficial owners as required)
- Authorized signatories and delegated authority
- Expected transaction profile (volume, counterparties, geographies)
- Risk rating, screening results, and approval record

**Document requirements**

- Defined lists of acceptable documents by segment and jurisdiction, including:

  - Primary identity documents
  - Proof of address / business address
  - Incorporation/registration documents for entities
  - Authority documents (board resolution, power of attorney) where applicable

- Document handling rules:

  - Validity checks (expiry, tampering signs)
  - Copy certification rules (who can certify, required stamps/signatures)
  - Storage standards (system of record, file naming, retention mapping)

**Refresh frequency (periodic reviews)**

- Review frequency is risk-based (e.g., higher-risk reviewed more often).
- **Trigger-based refresh** required when:

  - Name/address/signatory changes
  - Ownership/control changes
  - Material change in expected activity or unusual behavior
  - Adverse information or sanctions/PEP status change
  - Product upgrades or new high-risk products added

---

### 3.4 Account opening / modification / closure

**Account opening (controls)**

- Maker–checker for account creation and parameter setup (limits, products enabled).
- Confirm completion of minimum KYC + screening before activation.
- Apply appropriate account restrictions until full due diligence is complete (if policy permits staged onboarding).

**Account modification**

- All changes must be ticketed/workflow-controlled with:

  - Requestor identity
  - Justification
  - Required approvals (DoA)
  - Evidence (supporting documents)
  - Audit trail in system of record

- High-risk modifications requiring additional controls:

  - Beneficial owner changes, signatory changes, address changes
  - Limit increases or cross-border enablement
  - Changes to product permissions

**Account closure / exit**

- Verify closure eligibility (no holds, unresolved disputes, compliance restrictions).
- Compliance review required if:

  - Suspicious activity is involved
  - Sanctions/financial crime concerns exist
  - Regulatory reporting is pending

- Ensure balances are settled, fees applied correctly, and statements generated as required.
- Retain closure documentation and rationale, including who approved and why.

---

### 3.5 Handling vulnerable customers and special cases

**Principle.**
Customers requiring extra care must receive fair, safe, and compliant treatment, with additional controls to prevent harm or exploitation.

**Common vulnerable/special cases (examples)**

- Elderly customers, customers with disabilities, limited language proficiency
- Customers under guardianship or with power of attorney
- Victims of fraud/scams or suspected coercion
- Deceased customer estates
- Minors or youth accounts (where applicable)
- Non-residents, refugees, or customers with alternative documentation (subject to law)

**Operational requirements**

- Provide accessible communication options (language support, alternative formats where feasible).
- Verify authority carefully (guardian/PoA documents); apply maker–checker on sensitive changes.
- Apply heightened scam/fraud checks when coercion is suspected; pause transactions and escalate.
- Ensure privacy and dignity: limit disclosure, avoid unnecessary information requests.
- Document actions and rationale; escalate to Compliance/Risk when uncertainty exists.

**Escalation triggers**

- Suspicion of exploitation or coercion
- Unusual third-party control over account activity
- Conflicting documentation or unclear authority
- Repeat scam indicators

---

---

## 4) Product and transaction operations

### 4.1 Deposits, payments, transfers, and cash operations

**Deposits (account servicing)**

- Posting rules (cut-off times, value dating, reversals)
- Exception handling (mis-postings, duplicate postings)
- Interest accrual and statement generation controls
- Dormant/inactive account handling (where applicable)

**Payments & transfers**

- Payment initiation channels (branch, digital, file upload) and validation rules
- Screening steps (sanctions/AML) before release when required
- Maker–checker requirements for:

  - High-value payments
  - New beneficiaries
  - Limit overrides
  - Manual repairs

- Returns, rejects, recalls, and investigations process
- Cut-off times, queue management, and backlog controls

**Cash operations (if applicable)**

- Cash acceptance/dispensing controls, dual control for vault/cash movements
- Cash limits, counterfeit checks, and exception logs
- Daily balancing, discrepancies handling, and escalation timelines

**Reconciliations**

- Required reconciliation types (nostro, suspense, payment gateways)
- Break classification, aging rules, and remediation SLAs
- Independent review and sign-off requirements

---

### 4.2 Cards (issuance, disputes/chargebacks, fraud handling)

**Card issuance**

- Eligibility checks and identity verification
- Card production and delivery controls (secure handling, activation)
- PIN issuance/management controls (secure channels, auditability)
- Replacement/reissue workflows and approvals

**Disputes and chargebacks**

- Intake requirements (customer statement, timelines, evidence)
- Provisional credit rules (if applicable) and conditions
- Chargeback lifecycle management (representment, arbitration if applicable)
- Customer communications templates and required disclosures
- Documentation standards and retention

**Fraud handling**

- Fraud alert triage and case creation
- Temporary blocks, transaction holds, and customer verification steps
- Replacement and account remediation actions
- Escalation to fraud specialists and Compliance when required
- Metrics and monitoring (fraud rates, false positives, time-to-contain)

---

### 4.3 Lending operations (origination support, disbursement, repayment, collections)

**Origination support**

- Document checklist control (income, collateral, legal docs where applicable)
- Underwriting decision capture and approval evidence (per DoA)
- Conditions precedent tracking (what must be satisfied before disbursement)
- Conflict-of-interest and SoD checks (sales vs approval vs operations)

**Disbursement**

- Pre-disbursement validation (signed contracts, approvals, insurance, collateral perfection where required)
- Maker–checker for disbursement setup and release
- Disbursement posting controls, fees/charges correctness
- Exception handling (partial disbursement, rework, cancellation)

**Repayment and servicing**

- Payment allocation rules (principal/interest/fees)
- Early repayment / restructuring workflows and approvals
- Delinquency management steps (notices, repayment plans)
- Customer communication and documentation standards

**Collections**

- Controlled contact rules (frequency, permitted language, prohibited practices)
- Escalation and handoff to external agencies (if allowed)
- Write-off / settlement approvals per DoA
- Litigation support process (with Legal)

---

### 4.4 Trade finance / remittances (if applicable)

**Trade finance**

- Document checking standards (LCs, collections) and discrepancy handling
- Sanctions screening for parties, goods, vessels (as applicable)
- Approval and issuance/amendment controls
- Exposure and limit checks, collateral/margin handling
- Recordkeeping and audit trails for all decisions

**Remittances**

- Validation rules for beneficiary and purpose codes (if required)
- Cross-border screening and monitoring requirements
- Return/repair workflows and customer communications
- Cut-off times and settlement controls

---

### 4.5 Fees, interest calculation, waivers, and adjustments

**Fee governance**

- Standard fee schedules (where stored, who can change them)
- System parameter change controls (CAB approvals, testing evidence)
- Customer notifications where required

**Interest calculation**

- Interest rate setup controls and independent review
- Accrual and posting schedules, rounding rules
- Negative interest handling (if applicable)
- Period-end processing controls and reconciliation

**Waivers and adjustments**

- Eligibility criteria for waivers (service recovery, pricing programs)
- Approval limits per DoA; maker–checker required for manual adjustments
- Documentation requirements:

  - Reason code
  - Customer communication record (if required)
  - Approval evidence

- Monitoring:

  - Exception reporting for high waiver volumes or unusual patterns
  - Periodic review by Finance Controls/Operational Risk

## 5) Compliance framework (core)

### 5.1 Overview and principles

The bank maintains a compliance framework designed to:

- Meet applicable legal and regulatory obligations.
- Prevent, detect, and report financial crime and misconduct.
- Ensure customers are treated fairly and consistently.
- Maintain auditable evidence of decisions and controls.

**Minimum expectations**

- Compliance obligations must be embedded into day-to-day procedures (not “optional guidance”).
- Regulatory-impacting decisions require documented rationale, approvals, and evidence retention.
- Exceptions must be controlled, time-bound, and approved per Delegation of Authority (DoA).

---

### 5.2 AML/CFT program (monitoring, alerts, SAR/STR process)

**Objective.**
Detect and deter money laundering and terrorism financing through risk-based controls across onboarding, transaction monitoring, and reporting.

**Core components**

1. **Customer risk assessment**

   - Risk rating assigned at onboarding and refreshed periodically or on trigger events.

2. **Transaction monitoring**

   - Rules/scenarios and thresholds aligned to customer risk and products.
   - Coverage includes unusual patterns, rapid movement of funds, high-risk corridors, structuring indicators, and anomaly detection (where available).

3. **Alert management**

   - Alerts are triaged, investigated, dispositioned, and evidenced within defined SLAs.
   - “Close with rationale” is mandatory; unsupported closures are prohibited.

4. **Case management**

   - Investigation steps and required documentation are standardized (case notes, supporting data, communications log).

5. **Reporting obligations (SAR/STR)**

   - Where required by local law, suspicious activity reports/transaction reports must be filed via the designated channel within regulatory timelines.
   - Reporting decisions are owned by the bank’s designated AML authority (e.g., MLRO or equivalent), with documented rationale.

**Alert workflow (minimum)**

- **Triage:** validate alert quality, de-duplicate, confirm entity linkage.
- **Investigation:** review transactions, customer profile, expected activity, and supporting documents.
- **Decision:** clear, continue monitoring, restrict activity, or escalate for reporting consideration.
- **Escalation:** suspected suspicious activity must be escalated immediately to the AML function.
- **Closure:** record outcome, rationale, and evidence; apply follow-up actions (KYC refresh, restrictions, EDD).

**Evidence requirements**

- Alert metadata, investigation notes, data extracts/screens, decision rationale, approver identity, timestamps, and follow-up actions.

---

### 5.3 Sanctions screening (lists, name matching rules, escalation)

**Objective.**
Prevent the bank from providing services to sanctioned parties and comply with sanctions regimes applicable to the bank’s jurisdiction(s) and operations.

**List sources (as applicable)**

- **UN** sanctions lists
- **EU** consolidated list
- **OFAC** (US)
- **Local/national** sanctions lists and regulator-provided watchlists
- Bank internal watchlists (e.g., prior fraud/exit lists), where permitted

**Screening coverage**

- Customers (retail/entity), beneficial owners, directors, authorized signatories
- Beneficiaries and counterparties for payments and trade-related activity (where applicable)
- Names and key identifiers captured at onboarding and during lifecycle events

**Name matching rules (high level)**

- Use a documented matching policy defining:

  - Minimum data fields used (name, DOB, nationality, ID number where available)
  - Handling of aliases, transliterations, partial matches
  - Risk-based match thresholds and tuning governance

- Changes to matching thresholds or rule tuning require approval and testing evidence.

**Escalation and decisioning**

- Potential matches must be escalated to the sanctions compliance desk for disposition.
- Until disposition is complete:

  - New relationship onboarding may be paused.
  - Transactions may be held per procedure and legal requirements.

- Dispositions must be recorded as:

  - **False match** (with rationale and supporting evidence), or
  - **True match / probable match** (triggering required actions and reporting/escalation).

---

### 5.4 Anti-bribery / anti-corruption (ABAC), gifts & entertainment

**Objective.**
Prevent bribery and corruption risk and ensure ethical conduct in interactions with customers, vendors, and public officials.

**Core controls**

- **Prohibited conduct:** offering or accepting anything of value to improperly influence a decision.
- **Gifts & entertainment rules:**

  - Thresholds and approval requirements (per DoA).
  - Restrictions on cash or cash-equivalent gifts.
  - Enhanced rules involving government/public officials and high-risk third parties.

- **Recording and transparency**

  - Gifts/entertainment must be recorded in the designated register when above the reporting threshold.

- **Third-party risk**

  - Intermediaries, agents, and vendors must undergo due diligence appropriate to risk.

**Escalation triggers**

- Any suspected bribery/corruption attempt, unusual requests, or pressure to bypass controls.

---

### 5.5 Market conduct, fair treatment, suitability (if relevant)

**Objective.**
Ensure customers are treated fairly across product sales, servicing, complaints, and remediation.

**Minimum expectations**

- Clear, non-misleading communications and disclosures.
- Controls to prevent mis-selling and inappropriate product placement.
- Suitability/appropriateness checks where required (e.g., investments/insurance).
- Transparent complaint handling with defined SLAs and root-cause tracking.
- Remediation and fee adjustments governed by policy and DoA.

**Evidence requirements**

- Records of customer disclosures/acknowledgements (where required).
- Records of advice/suitability assessment outcomes (where applicable).
- Complaint logs, decisions, and communication templates used.

---

### 5.6 Conflicts of interest

**Objective.**
Identify, disclose, and manage conflicts that could compromise impartial decision-making.

**Examples of conflicts**

- Personal relationships with customers/vendors.
- Outside employment or financial interests affecting decisions.
- Gifts/benefits that create undue influence.
- Staff handling accounts related to themselves or close associates.

**Controls**

- Mandatory disclosure process and periodic attestations.
- Restrictions on self-approval and handling of related-party activity.
- Recusal and reassignment procedures where conflicts exist.
- Monitoring and disciplinary consequences for non-disclosure.

---

### 5.7 Whistleblowing & non-retaliation policy

**Objective.**
Enable safe reporting of suspected wrongdoing and protect reporters from retaliation.

**Reporting channels**

- Anonymous hotline/portal (where legally permitted)
- Compliance mailbox or designated intake
- Internal Audit channel for control concerns
- Manager escalation (not recommended if conflict exists)

**Protections**

- Non-retaliation is mandatory; retaliation is a disciplinary offense.
- Confidentiality is maintained to the extent legally possible.
- Reports are triaged, investigated, and tracked with documented outcomes.

**Minimum process**

- Intake → triage/severity assignment → investigation → remediation → closure → lessons learned.

---

---

## 6) Data, privacy, and record management

### 6.1 Data classification (public / internal / confidential / restricted)

**Objective.**
Classify data so it is handled with appropriate safeguards, limiting access and reducing leakage risk.

**Classification levels (baseline)**

- **Public:** Approved for external release (e.g., published rates, marketing).
- **Internal:** Non-public business information with limited impact if disclosed.
- **Confidential:** Sensitive business/customer data; disclosure could cause harm or regulatory impact.
- **Restricted:** Highly sensitive data requiring strict controls (e.g., credentials, certain customer identifiers, security keys, SAR/STR-related materials where applicable, sensitive investigations).

**Handling rules (minimum)**

- Labeling requirements (documents, emails, storage folders where applicable).
- Approved storage locations by classification.
- Prohibited channels for higher classifications (e.g., personal email, unapproved messaging).

---

### 6.2 Access control rules (least privilege, MFA expectations)

**Principles**

- **Least privilege:** access only what is needed for the role.
- **Need-to-know:** sensitive investigations and restricted data access is limited further.
- **Segregation of duties:** entitlements must enforce maker–checker and prevent end-to-end control.

**Minimum controls**

- Role-based access control (RBAC) with approved role catalog.
- **MFA required** for:

  - Remote access
  - Privileged/admin functions
  - Access to restricted systems/data (where technically feasible)

- Joiner/mover/leaver workflow:

  - Manager approval + system owner approval
  - Time-bound access for temporary needs
  - Immediate deprovisioning on exit

- Periodic access reviews and attestation by managers/system owners.

---

### 6.3 Privacy requirements (consent, data sharing, retention)

**Objective.**
Ensure customer and employee personal data is collected, used, shared, and retained lawfully and transparently.

**Minimum requirements**

- **Collection limitation:** collect only what is necessary for legal/operational purposes.
- **Purpose limitation:** use data only for stated, legitimate purposes.
- **Consent management:** where consent is required, record consent status and provide withdrawal handling.
- **Data sharing controls:**

  - External sharing requires approved legal basis, contract clauses, and security controls.
  - Cross-border transfers require additional checks per local rules.

- **Data subject rights (where applicable):**

  - Requests for access/correction/deletion handled via defined process with identity verification.

- **Retention alignment:** retain personal data only as long as required for legal/business needs, then dispose securely.

---

### 6.4 Records retention schedule (what to keep, how long, where)

**Objective.**
Retain records to satisfy regulatory and business needs while minimizing over-retention risk.

**Retention schedule requirements**
For each record category define:

- **Record type** (e.g., onboarding file, transaction record, complaint record)
- **System of record** (where it must be stored)
- **Minimum retention period** (and any legal holds)
- **Disposition method** (secure deletion/destruction)
- **Owner** (function accountable)

**Typical record categories (examples)**

- Customer onboarding/KYC and updates
- Screening outcomes and investigations (including rationale)
- Transaction records and payment messages
- Account opening/modification/closure approvals
- Complaints and remediation
- Operational incidents and issue management artifacts
- Access logs and entitlement change approvals
- Policy/procedure approvals and change logs

**Storage rules**

- Records must reside in approved repositories with access control and auditability.
- “Local copies” on personal devices are prohibited for confidential/restricted records unless explicitly approved and encrypted.

---

### 6.5 eDiscovery / legal hold process

**Objective.**
Preserve relevant records when litigation, investigations, audits, or regulatory actions require it, preventing alteration or deletion.

**Trigger events**

- Notice of litigation or dispute
- Regulatory investigation/exam requiring preservation
- Internal investigation with potential legal exposure
- Audit request requiring complete historical records

**Minimum process**

1. **Legal hold issuance** (Legal is owner)

   - Define scope: custodians, systems, date ranges, record types.

2. **Preservation actions**

   - Suspend retention-based deletion for in-scope records.
   - Lock down access and prevent modification where feasible.

3. **Collection and review**

   - Use approved tools/processes; maintain chain-of-custody logs.

4. **Release of hold**

   - Legal formally releases the hold; normal retention resumes.

**Employee obligations**

- Do not delete, modify, or move records under hold.
- Follow instructions precisely; escalate questions to Legal/Compliance.

## 7) Operational risk and internal controls

### 7.1 Overview and principles

**Objective.**
Maintain a consistent control environment that prevents, detects, and corrects operational failures, customer harm, financial loss, and regulatory breaches.

**Principles**

- Controls must be **built into the process**, not added “after the fact.”
- Controls must be **evidenced** (audit trail or documented proof).
- Risk and control ownership must be **clear** (RACI + control owner).
- Material control failures must be **reported, remediated, and monitored** to closure.

---

### 7.2 Control objectives per process

Each operational process must document its control objectives and link them to specific control steps.

**Minimum control objectives (apply as relevant)**

- **Accuracy:** transactions and records are correct and complete.
- **Authorization:** actions occur only with proper approvals/DoA.
- **Timeliness:** processing meets cut-offs and SLAs.
- **Compliance:** legal/regulatory and policy requirements are met.
- **Asset protection:** prevents fraud, theft, and unauthorized use.
- **Data integrity & confidentiality:** information is protected and consistent across systems.
- **Reconciliation & completeness:** records reconcile to trusted sources; breaks are investigated and resolved.
- **Customer fairness:** customers are treated fairly and outcomes are consistent.

**Control mapping requirement**
For every process/SOP, include:

- Control ID and description
- Control type (preventive/detective/corrective)
- Frequency (real-time/daily/weekly/monthly)
- Owner (role), performer (role), reviewer (role)
- Evidence location (system/report/ticket)
- Exceptions and escalation rules

---

### 7.3 Key risk indicators (KRIs) and monitoring cadence

**Objective.**
Use KRIs to identify risk build-up early and trigger preventive actions.

**KRI governance**

- KRIs must have: definition, calculation method, data source, owner, thresholds, and actions.
- Thresholds typically include: **Green / Amber / Red**.
- KRIs are reviewed with a fixed cadence, and exceptions are escalated.

**Example KRIs (typical for bank operations)**

- **Operational timeliness**

  - Payment processing backlog volume; % items beyond SLA
  - Reconciliation breaks aging; # breaks > X days

- **Quality and errors**

  - Error/rework rate; manual repair volume
  - Posting/reversal count; duplicate transactions rate

- **Control effectiveness**

  - Maker–checker override rate
  - % missed control sign-offs (e.g., missed daily balancing)

- **Customer impact**

  - Complaint rate; repeat complaints
  - % cases requiring remediation/fee refunds

- **Fraud and financial loss**

  - Fraud attempts detected; confirmed fraud loss
  - Chargeback ratios (cards)

- **Compliance risk (ops-driven)**

  - KYC refresh overdue rate
  - Sanctions screening holds aging

**Monitoring cadence (minimum guidance)**

- **Daily:** backlogs, cut-off breaches, critical reconciliations, high-risk queues
- **Weekly:** error rates, break aging, override trends, training gaps
- **Monthly:** KRI dashboard review with Operations + ORM + Compliance (as relevant)
- **Quarterly:** threshold recalibration and control design review for high-change areas

**Action expectations**

- Amber: action plan with owner and due date.
- Red: immediate escalation to operations management and ORM; consider incident declaration.

---

### 7.4 Issue management (logging, severity, owners, remediation timelines)

**Objective.**
Ensure all control gaps, process weaknesses, audit findings, and recurring errors are tracked to closure with accountability.

**What qualifies as an “issue”**

- Control failure (missed reconciliation, unauthorized override, missing approvals)
- Process design gap (no clear owner, unclear steps, systemic rework)
- Audit finding or regulatory observation
- Repeated operational errors indicating a root cause
- System defect that impacts controls or customer outcomes

**How to log issues (minimum)**
All issues must be logged in an approved tracking system (ticketing/GRC tool) with:

- Issue title, description, and impact summary
- Date identified, source (audit, ops, monitoring, incident)
- Scope (process, product, system, teams)
- Root cause category (people/process/system/vendor)
- Severity rating and rationale
- Owner (Accountable role) and action owners (Responsible roles)
- Remediation plan and milestones
- Evidence of completion and validation approach

**Severity model (example)**

- **Critical:** significant customer harm, regulatory breach likely, material loss, or major control breakdown
  → immediate escalation; urgent remediation plan
- **High:** meaningful risk exposure or repeated failures; potential external impact
  → remediation within defined short timeline
- **Medium:** localized impact; manageable but needs fix
  → remediation within standard timeline
- **Low:** minor improvement; no meaningful risk exposure
  → fix via normal change cycle

**Remediation timelines**

- Each severity level must map to a maximum target closure time (tracked and reported).
- Extensions require justification and management approval; compensating controls must be documented.

**Validation and closure**

- Closure requires evidence that actions were implemented and controls are effective (QA sampling, control testing, post-fix metrics).

---

### 7.5 Incident reporting (ops incidents, compliance breaches)

**Objective.**
Contain harm quickly and meet reporting obligations when incidents occur.

**What is an incident**

- Service outage or severe degradation impacting critical operations
- Processing failure that affects customer transactions or balances
- Data/privacy events (handled with InfoSec/Privacy process)
- Compliance breaches or near-misses with regulatory significance
- Fraud events with confirmed or likely loss
- Any event requiring emergency change or crisis escalation

**Incident lifecycle (minimum)**

1. **Detect & declare**

   - Identify severity and immediate risk; assign incident commander (role-based).

2. **Contain**

   - Stop the bleed: pause processing, apply blocks/holds, isolate impacted systems as instructed.

3. **Communicate**

   - Notify stakeholders (Ops, ORM, Compliance, IT/Security, Customer Service) based on severity.

4. **Investigate**

   - Identify impact, root cause, and affected customers/transactions.

5. **Remediate**

   - Fix cause; correct impacted records; customer remediation where required.

6. **Post-incident review**

   - Lessons learned, control improvements, and KRI updates.

**Evidence requirements**

- Timeline of events, decisions, communications, data extracts, approvals, and remediation proof.

---

### 7.6 Fraud risk management and red flags

**Objective.**
Reduce fraud losses through prevention, detection, escalation, and staff awareness.

**Controls (baseline)**

- Maker–checker for high-risk actions (limit changes, beneficiary updates, manual postings)
- Velocity limits and anomaly detection where available
- Strong identity verification and authority checks for sensitive changes
- Case management for fraud reports and investigations
- Post-event remediation: credential resets, account restrictions, customer notification standards

**Common operational red flags (examples)**

- Sudden changes to contact details followed by high-value transfers
- Unusual third-party involvement or pressure to bypass standard checks
- Repeated failed authentication/verification attempts
- High frequency of manual overrides or exception processing by one user/team
- Multiple accounts linked to same device/contact detail (where detectable)
- Customer reports coercion or unusual urgency

**Escalation**

- Suspected fraud must be escalated immediately to the fraud team and, where relevant, Compliance (AML) and InfoSec.

---

---

## 8) IT, security, and technology operations (for bank users)

### 8.1 Overview

**Objective.**
Ensure employees use bank technology safely, protect customer information, and maintain reliable audit trails for regulated operations.

**Scope.**
Applies to all bank users of systems, devices, networks, and approved third-party tools used for bank work.

---

### 8.2 Acceptable use of systems and devices

**General rules**

- Bank systems and devices are for authorized business use only.
- Only approved software and services may be used to store or process bank data.
- Do not bypass security controls or share accounts.
- Do not use personal email or unapproved messaging for confidential/restricted information.

**Remote work expectations (if applicable)**

- Use approved VPN/secure access methods.
- Do not work in public spaces in a way that exposes customer information (screen privacy, secure conversations).
- Lock screens when unattended; secure printed materials.

---

### 8.3 Security controls (passwords, phishing, removable media, secure printing)

**Passwords and authentication**

- Use strong, unique passwords; do not reuse across services.
- MFA is required where enforced; do not approve MFA prompts you did not initiate.
- Never share passwords, OTPs, or authentication tokens.

**Phishing and social engineering**

- Treat unexpected links/attachments as suspicious.
- Verify unusual requests through official channels, especially requests to:

  - change customer details
  - expedite payments
  - approve exceptions
  - provide access or credentials

- Report suspected phishing immediately via the designated channel.

**Removable media**

- Use of removable media is restricted and must follow bank policy.
- Only approved, encrypted media may be used where explicitly permitted.
- Never plug unknown devices into bank computers.

**Secure printing**

- Avoid printing confidential information unless necessary.
- Use secure print release where available.
- Collect printed documents immediately; store or dispose securely (shred bins).

---

### 8.4 Change management (who can request/approve changes)

**Objective.**
Ensure changes to systems, configurations, or operational processes are reviewed, tested, approved, and traceable.

**What counts as a “change”**

- System configuration updates impacting processing or controls
- Access role changes or entitlement model changes
- Workflow/process changes affecting approvals, evidence, or SLAs
- Rule/threshold tuning for monitoring/screening systems

**Change roles**

- **Requester:** proposes change with business justification.
- **Approver(s):** authority per change type (Ops owner, IT owner, Compliance/ORM/Finance Controls where impacted).
- **Implementer:** executes change (often IT).
- **Verifier:** validates change outcomes (QA/control testing role).

**Minimum change requirements**

- Document scope, impact assessment, rollback plan, and testing evidence.
- Obtain approvals before implementation.
- Emergency changes require post-implementation review and formalization.

---

### 8.5 Access provisioning & deprovisioning (joiner/mover/leaver)

**Objective.**
Ensure users have correct access for their role and that access is removed promptly when no longer needed.

**Joiner**

- Access request must be tied to role-based access templates.
- Requires manager approval + system owner approval.
- Privileged access requires additional approvals and justification.

**Mover**

- Role changes require:

  - Removal of old access first (where appropriate)
  - Grant of new access based on new role
  - Review for SoD conflicts

**Leaver**

- Access must be revoked promptly on termination/role exit.
- Disable credentials, remote access, and shared mailbox access as required.
- Recover physical assets (tokens, laptops) per IT policy.

**Periodic access reviews**

- Managers/system owners must attest that access remains appropriate, with documented results.

---

### 8.6 Logging, audit trails, and monitoring expectations

**Objective.**
Maintain sufficient audit trails to reconstruct events, support investigations, and meet regulatory expectations.

**Minimum logging expectations**

- Systems must capture:

  - user identity
  - timestamps
  - actions performed (create/approve/modify/override)
  - before/after values for sensitive changes where feasible
  - authorization/approval references (ticket IDs, workflow IDs)

**User responsibilities**

- Do not perform work outside approved systems where it breaks auditability (e.g., approvals in chat).
- Use official workflows for approvals and exceptions.
- Do not attempt to disable or circumvent logging.

**Monitoring**

- High-risk actions and privileged activities are monitored and reviewed.
- Alerts from security tooling must be handled within defined SLAs.
- Log access is restricted to authorized roles; log retention follows the retention schedule.

## 9) Financial controls and treasury-adjacent ops (as applicable)

### 9.1 Overview and principles

**Objective.**
Ensure financial records are accurate, complete, timely, and auditable; protect the bank’s liquidity and assets; and maintain strong controls over postings, reconciliations, and treasury-adjacent operational activities.

**Principles**

- **Books and records integrity:** every posting is supported, traceable, and approved.
- **Independence:** execution and reconciliation/review are segregated where feasible.
- **Timeliness:** breaks and exceptions are resolved within defined SLAs.
- **Auditability:** evidence is retained in approved systems with clear ownership.

---

### 9.2 Reconciliations (daily/monthly) and break handling

**Minimum reconciliation coverage (as applicable)**

- **Bank accounts / Nostro / settlement accounts**
- **Payment gateways / clearing networks**
- **Cash and ATM/branch cash positions**
- **Suspense and clearing accounts**
- **Fee and interest income accounts (where relevant)**
- **Key operational sub-ledgers to GL** (cards, loans, deposits)

**Cadence**

- **Daily:** high-volume or high-risk accounts (payments, settlement, cash)
- **Monthly:** lower-risk accounts and financial close reconciliations
- **Ad-hoc:** after incidents, major system changes, or cut-over events

**Reconciliation standards**

- Define trusted sources (“system of record” vs external statements).
- Use standardized templates and naming conventions.
- Require **preparer** and **independent reviewer** sign-off (maker–checker).
- Evidence must include inputs, matching logic, and outputs (reports, statements, extracts).

**Break handling**

- **Break classification:** timing, data mismatch, missing entry, duplicate, unauthorized, unknown.
- **Ownership:** assign a break owner and target resolution date at creation.
- **Aging and escalation:**

  - Breaks are tracked by age buckets (e.g., 0–2 days, 3–7, 8–30, >30).
  - Escalate breaks beyond threshold to Finance Controls/Operations leadership.

- **Corrective actions:**

  - Adjusting entries must be approved and evidenced.
  - Root cause analysis required for recurring breaks and significant items.

- **Close-out rules:** breaks cannot be closed without documented resolution and evidence.

---

### 9.3 GL posting rules and suspense accounts

**Objective.**
Ensure postings are accurate, authorized, and consistently coded, and that suspense accounts are tightly controlled.

**GL posting rules**

- Standardized chart of accounts mapping for each product/process.
- Required posting attributes:

  - transaction reference ID
  - value date vs posting date
  - currency and FX rate source (if applicable)
  - maker–checker approvals for manual entries

- Manual journals:

  - Only permitted for approved roles.
  - Must include justification, supporting evidence, and approval per DoA.
  - Must be traceable back to source transaction or correction request.

**Suspense accounts (strict controls)**

- Suspense accounts are temporary holding accounts and must not be used as long-term storage.
- All suspense entries must include:

  - reason code
  - owner
  - expected resolution date
  - linkage to a case/ticket

- **Daily monitoring** of suspense aging and balances.
- Escalation required for aged items beyond policy thresholds.
- Periodic independent review by Finance Controls.

**Prohibited practices**

- “Parking” entries in suspense to meet close deadlines without a remediation plan.
- Unapproved backdating or undocumented manual adjustments.

---

### 9.4 Cash management procedures

**Objective.**
Maintain sufficient liquidity for operational needs, protect physical cash, and ensure accurate reporting of cash positions.

**Scope (as applicable)**

- Branch cash operations, vault handling, CIT (cash-in-transit) coordination
- ATM cash management and balancing
- Treasury operational cash positioning and movements

**Minimum controls**

- Dual control for vault access and material cash movements.
- Defined cash limits by location and role; exceptions require approval.
- Daily cash balancing and independent review.
- Counterfeit detection controls and escalation workflow.
- Incident reporting for discrepancies, suspected theft, or counterfeit events.

**Cash movement governance**

- All cash movements must be recorded (who/when/why/how much).
- Use secure channels for instruction and confirmation (no informal messaging).
- Maintain chain-of-custody records for CIT movements.

---

### 9.5 Limits management (exposure, liquidity, operational limits)

**Objective.**
Prevent excessive risk by managing exposures and ensuring the bank operates within approved limits.

**Limit types (as applicable)**

- **Exposure limits:** counterparty, customer, sector, country, product limits
- **Liquidity limits:** intraday liquidity thresholds, buffer requirements
- **Operational limits:** payment release thresholds, teller cash limits, user/system transaction caps

**Limit governance**

- Limits must have:

  - owner (Accountable role)
  - rationale and methodology
  - monitoring frequency
  - breach thresholds and escalation actions

- Breach handling:

  - immediate containment actions (e.g., restrict processing, require approvals)
  - escalation to Treasury/Risk/Operations leadership based on severity
  - post-breach review and corrective actions

**Change controls**

- Limit changes require approvals per DoA and must be logged with evidence.
- Temporary limits must have an expiry date and compensating controls.

---

### 9.6 Pricing/valuation controls (if relevant to the bank)

**Objective.**
Ensure rates, prices, and valuations used in customer transactions and financial reporting are accurate, approved, and auditable.

**Coverage (as applicable)**

- Interest rate tables and product pricing parameters
- FX rates and spreads
- Fees and commissions schedules
- Valuation models or inputs for products that require valuation

**Minimum controls**

- Rate/pricing changes require:

  - documented rationale and approvals (Product + Finance/Treasury + Compliance where relevant)
  - testing evidence in lower environments (where applicable)
  - effective date controls and rollback plan

- Independent validation:

  - spot checks or periodic reviews by Finance Controls/Treasury

- Monitoring:

  - exception reports for manual rate overrides or unusual pricing outcomes

- Evidence:

  - change tickets, approvals, before/after parameters, and communication logs

---

---

## 10) Third-party and outsourcing management

### 10.1 Overview and principles

**Objective.**
Ensure third-party services (vendors, partners, outsourced operations) are selected, contracted, and managed to meet the bank’s security, compliance, operational resilience, and service quality requirements.

**Principles**

- Risk-based due diligence before onboarding.
- Contracts must contain minimum protections and enforceable controls.
- Ongoing monitoring and periodic reviews are mandatory.
- The bank remains accountable for outsourced activities.

---

### 10.2 Vendor due diligence and onboarding

**Vendor onboarding stages (minimum)**

1. **Business need and risk assessment**

   - Define service scope, data access, criticality, and substitutability.

2. **Due diligence**

   - Corporate profile, financial health (as applicable)
   - Security posture (controls, certifications, incident history)
   - Compliance and regulatory alignment (data handling, subcontractors)
   - Operational capability and resiliency (BCP/DR capabilities)

3. **Approval**

   - Approvals per DoA, including security/compliance sign-off for high-risk vendors.

4. **Contracting and implementation**

   - Ensure minimum clauses (see 10.3).
   - Implementation plan includes access controls, testing, and acceptance criteria.

5. **Go-live controls**

   - Confirm security requirements, monitoring, and operational handoffs are in place.

**Risk tiering**

- Vendors should be categorized (e.g., Critical/High/Medium/Low) based on:

  - access to customer data
  - impact of outage
  - regulatory sensitivity
  - concentration risk and replaceability

- Tier determines review cadence and control intensity.

---

### 10.3 Contract minimum clauses (security, audit rights, SLAs)

All third-party contracts must include minimum clauses appropriate to risk tier, including:

**Security and privacy**

- Data protection requirements aligned to the bank’s data classification rules
- Encryption expectations (in transit/at rest where applicable)
- Access control and least privilege obligations
- Incident notification timelines and cooperation requirements
- Subcontractor restrictions and approval requirements

**Audit and oversight rights**

- Bank right to audit (or obtain independent audit reports)
- Right to request evidence of controls (SOC reports or equivalent where applicable)
- Regulator access rights where required by local regulation

**Service levels and performance**

- SLAs for availability, response times, and support
- Escalation requirements and penalties/remedies for chronic SLA breaches
- Change control expectations (advance notice for material changes)

**Resilience**

- BCP/DR requirements (RTO/RPO expectations where applicable)
- Testing cadence for DR and incident exercises

**Termination and transition**

- Exit assistance obligations (data return, migration support)
- Data deletion and certification on termination
- Ownership of bank data and restrictions on use

---

### 10.4 Ongoing monitoring and periodic reviews

**Monitoring expectations**

- SLA tracking, incident tracking, and service quality reviews.
- Security monitoring for high-risk vendors (e.g., periodic questionnaires, audit reports).
- Financial/operational health checks for critical vendors.
- Tracking of subcontractors and material changes.

**Periodic review cadence (example)**

- **Critical vendors:** quarterly service reviews; annual full risk review
- **High risk:** semi-annual service reviews; annual risk review
- **Medium/low:** annual or biennial review as appropriate

**Issue management**

- Vendor issues are logged in the bank’s issue management system with:

  - severity, owner, remediation plan, and deadlines

- Repeated issues may trigger:

  - enhanced monitoring
  - contractual remedies
  - vendor re-tendering or exit planning

---

### 10.5 Concentration risk and exit plans

**Objective.**
Reduce dependence on any single vendor and ensure continuity if a vendor fails.

**Concentration risk controls**

- Identify vendors supporting critical services and map dependencies.
- Assess single points of failure (region, cloud provider, subcontractor).
- Maintain visibility on overlapping dependencies across vendors.

**Exit planning (mandatory for critical/high-risk vendors)**

- Documented exit plan including:

  - trigger conditions (financial distress, repeated SLA failures, security incidents, regulatory issues)
  - transition timeline and responsibilities
  - data migration approach and data deletion verification
  - alternate provider options or internal fallback processes

- Periodic testing or tabletop exercises for critical vendor exits where feasible.

## 11) Business continuity and crisis management

### 11.1 Overview and objectives

**Objective.**
Ensure the bank can continue critical services and recover operations within acceptable timeframes during disruptions (technology outages, facility issues, vendor failures, cyber events, natural disasters), while protecting customers, meeting regulatory obligations, and maintaining clear command-and-control.

**Scope.**
Applies to all business lines, operations, control functions, and critical third parties that support in-scope processes and systems.

**Principles**

- Safety and customer protection first.
- Prioritize continuity of **critical processes** before non-critical work.
- Clear roles, escalation paths, and communications.
- Decisions and actions must be recorded for auditability and regulatory review.

---

### 11.2 BCP/DR roles, triggers, and comms templates

#### Roles and responsibilities

- **Crisis Management Lead (CML):** Overall accountable during declared crises; chairs crisis calls and approves major decisions.
- **Business Continuity Manager (BCM):** Maintains BCP documentation, coordinates testing, and supports activation.
- **Incident Commander (IC):** Leads operational/technology incident response for a specific event (may be IT or Operations depending on cause).
- **Operations Lead:** Owns continuity of operational processes, backlog triage, and manual workarounds.
- **IT/DR Lead:** Owns system recovery, failover, and technical restoration updates.
- **Compliance/Regulatory Liaison:** Advises on regulatory obligations, notifications, and reporting.
- **Communications Lead:** Controls internal/external messaging (employees, customers, partners).
- **Vendor Manager:** Coordinates third-party support and escalation for outsourced services.

#### Triggers (activation criteria)

BCP/DR or crisis procedures may be triggered by:

- Prolonged outage or degradation of a critical system/service.
- Loss of facility access or unsafe working conditions.
- Loss of critical staff capacity (e.g., widespread illness, travel disruption).
- Material cybersecurity incident.
- Third-party outage impacting critical processes.
- Any event likely to breach RTO/RPO targets or cause material customer harm.

**Severity-based escalation**

- **Operational Incident:** managed under incident process; BCP not activated unless thresholds met.
- **BCP Activation:** when disruption exceeds “normal operations” capability and requires workarounds or alternate modes.
- **Crisis Declaration:** when the event is severe, cross-functional, and requires executive decision-making and structured communications.

#### Communication templates (minimum set)

The bank maintains approved templates (role-based contact lists; no personal data) for:

- **Internal staff update:** what happened, impact, what to do, next update time.
- **Executive update:** impact summary, risks, customer impact, actions, decisions needed.
- **Customer advisory (if required):** service status, expected timelines, safety guidance, support channels.
- **Regulator notification (if required):** event description, scope, mitigations, next steps.
- **Third-party escalation:** incident summary, required response time, requested actions.

Templates must specify: owner, approval authority, distribution list, and update cadence.

---

### 11.3 Alternate sites and remote work rules

**Alternate site strategy (as applicable)**

- Designated alternate site(s) with capacity planning for critical roles.
- Access requirements: badges, secure connectivity, workstation readiness.
- Seating plan priorities based on critical process tiering.

**Remote work continuity rules**

- Remote work is permitted during disruptions if security and privacy requirements can be met.
- Minimum controls:

  - Approved secure access methods (VPN/secure gateway where applicable).
  - MFA enabled for remote access and privileged actions.
  - Prohibition on handling confidential/restricted data in insecure environments (public printing, unsecured Wi-Fi without bank controls).
  - Screen privacy expectations (lock screen; avoid exposing customer data).

- Manual workarounds must preserve auditability (use approved ticketing/workflow, not informal channels).

---

### 11.4 Critical process prioritization (RTO/RPO expectations)

**Objective.**
Focus limited resources on restoring or sustaining the most important processes first.

**Criticality tiers (example model)**

- **Tier 0 (Life-safety / systemic):** crisis communications, fraud containment, security controls.
- **Tier 1 (Critical):** customer funds movement, core banking availability, payment processing, reconciliation of settlement accounts.
- **Tier 2 (Important):** onboarding/servicing backlogs, card disputes intake, loan servicing processes.
- **Tier 3 (Routine):** lower-impact support tasks, non-urgent reporting.

**RTO/RPO definitions**

- **RTO (Recovery Time Objective):** maximum acceptable downtime for a process/system.
- **RPO (Recovery Point Objective):** maximum acceptable data loss measured in time.

**Expectations**

- Each critical process must document:

  - tier classification
  - RTO/RPO targets
  - dependencies (systems, vendors, people)
  - manual workaround options and limits
  - backlog recovery plan and reconciliation requirements

- RTO/RPO targets must be reviewed periodically and aligned with regulatory expectations and business risk appetite.

---

### 11.5 Cyber incident playbook (high-level)

**Objective.**
Respond quickly to cybersecurity incidents to contain damage, protect data, and restore services, while meeting reporting obligations.

**High-level phases (no technical exploitation detail)**

1. **Detect and triage**

   - Identify incident type (phishing, malware, account compromise, data exposure, service disruption).
   - Assign severity and incident owner.

2. **Contain**

   - Restrict access, disable impacted accounts, isolate affected services as directed by InfoSec/IT.
   - Preserve logs and evidence.

3. **Eradicate and recover**

   - Remove threat presence (as executed by IT/InfoSec).
   - Restore systems and validate integrity.

4. **Communicate**

   - Internal updates to impacted teams.
   - External communications only via approved channels and owners.
   - Regulatory notification via Compliance/Legal as required.

5. **Post-incident review**

   - Root cause, lessons learned, control improvements, monitoring enhancements.

**User responsibilities**

- Report suspected phishing or suspicious activity immediately.
- Do not attempt self-remediation outside procedure (to avoid destroying evidence).
- Follow directions on password resets, device checks, and access changes.

---

### 11.6 Crisis decision-making structure

**Crisis governance**

- **Crisis Management Team (CMT):** cross-functional group empowered to make time-sensitive decisions.
- **Decision rights**

  - Service suspension decisions (e.g., temporarily disabling a channel) require defined approval authority.
  - Customer communications require Communications Lead + Compliance/Legal approval where relevant.
  - Regulatory notifications owned by Compliance/Legal.

- **Decision logging**

  - All major decisions must be recorded: decision, rationale, time, approver, and follow-up actions.

**Meeting cadence**

- Initial rapid cadence during stabilization; move to scheduled updates once contained.
- Every update includes: impact, actions taken, decisions needed, next milestones, next update time.

---

---

## 12) Training, attestations, and competency

### 12.1 Overview and objectives

**Objective.**
Ensure employees and contractors understand policies and procedures required for their roles, can execute controls correctly, and periodically attest to compliance.

**Principles**

- Training is **role-based** and **risk-based**.
- High-risk roles require **competency validation**, not just course completion.
- Attestations are recorded and auditable.

---

### 12.2 Mandatory training list by role

The bank maintains a training matrix mapping courses to roles. Minimum topics include:

**All staff (baseline mandatory)**

- Code of conduct and ethics
- Data privacy and confidentiality
- Information security awareness (phishing, secure handling)
- Whistleblowing and non-retaliation
- Recordkeeping and acceptable use

**Operations staff**

- Operational controls (maker–checker, evidence standards)
- Incident reporting and escalation
- Customer fairness and complaint handling basics
- Fraud awareness and red flags

**Customer-facing staff (branches, contact center, relationship teams)**

- Customer communications standards and fair treatment
- KYC/KYB intake requirements and document handling
- Scam awareness and vulnerable customer handling
- Complaint intake and escalation

**Compliance / AML / sanctions roles**

- AML/CFT investigations and case management
- Sanctions screening disposition standards
- Regulatory reporting obligations and timelines
- Quality assurance and control testing expectations

**Finance Controls / reconciliation roles**

- Reconciliation standards and break handling
- GL posting controls and suspense governance
- Close processes and evidence requirements

**IT/Security privileged users (as applicable)**

- Privileged access responsibilities
- Security incident reporting and escalation
- Logging, audit trails, and change management controls

---

### 12.3 Certification / attestation cadence

**Cadence (example governance)**

- **At hire (pre-access):** core security + privacy + conduct modules
- **Annual:** refreshers for AML, privacy, security, conduct
- **Semi-annual or quarterly:** for high-risk teams (AML investigations, payments exceptions, fraud)
- **Event-driven:** after policy updates, major incidents, or audit findings

**Attestations (minimum)**

- Annual code of conduct attestation
- Annual conflicts of interest disclosure/attestation
- Annual privacy and acceptable use acknowledgement
- Role-based attestations (e.g., AML responsibilities for relevant staff)

**Tracking and enforcement**

- Completion and attestation records must be tracked centrally.
- Access to certain systems may be contingent on completion for high-risk roles.

---

### 12.4 Competency checks for high-risk roles

**Objective.**
Confirm capability to perform tasks correctly, not only that training was completed.

**High-risk roles (examples)**

- AML/sanctions investigators and disposition approvers
- Payments exception repair and manual release roles
- Reconciliation owners for critical accounts
- Privileged access administrators
- Fraud case handlers and dispute decision roles

**Competency validation methods**

- Scenario-based assessments (case studies with required decisions and evidence)
- Supervised work review during probation period
- Periodic quality sampling with threshold pass rates
- Certification requirements for certain roles where applicable

**Remediation**

- Targeted retraining, supervised work, and restricted access until competency is demonstrated.

---

### 12.5 New joiner onboarding checklist

**Objective.**
Ensure new joiners are ready and safe to operate before they receive full access and responsibility.

**Checklist (minimum)**

- **Administrative**

  - Role assignment confirmed; reporting line and RACI understood
  - Confidentiality agreements completed (as applicable)

- **Mandatory training (pre-access)**

  - Security awareness + phishing basics
  - Data privacy/confidentiality
  - Code of conduct and whistleblowing channel awareness

- **Access provisioning**

  - Role-based access requested and approved (joiner workflow)
  - SoD conflicts checked before granting access
  - MFA enabled and tested

- **Process onboarding**

  - SOP walkthrough for key tasks
  - Evidence standards and where to store records
  - Escalation contacts and incident reporting steps

- **Shadowing and validation**

  - Shadow period with buddy/mentor
  - Initial quality check of work outputs
  - Sign-off by team lead before independent processing

## 13) Audit and regulatory interaction

### 13.1 Overview and principles

**Objective.**
Support audits and regulatory engagements efficiently, transparently, and consistently, while protecting confidentiality and ensuring responses are accurate, complete, and evidence-based.

**Principles**

- Provide **facts and evidence**, not opinions or speculation.
- Use **approved channels** and designated liaisons.
- Maintain **document integrity** (version control, traceability, and confidentiality).
- Track all findings to closure with accountable owners and verified remediation.

---

### 13.2 How to respond to audit requests (evidence standards)

**Audit request intake**

- All requests must be routed through the bank’s defined intake path (e.g., Audit Liaison / Operations Governance / Compliance liaison).
- Requests are logged with:

  - request scope, due date, and audit owner
  - requested period and sample size
  - systems/processes involved
  - internal owner for response

**Evidence standards (minimum)**
Evidence provided to audit must be:

- **Relevant:** directly addresses the request.
- **Complete:** includes required context (dates, approvals, references).
- **Accurate:** matches system of record; no manual edits that change meaning.
- **Traceable:** links back to source system/ticket/case ID.
- **Readable and organized:** labeled files, consistent naming, and clear indexing.
- **Tamper-evident:** wherever possible, export from system of record (PDF/report export) rather than re-creating in spreadsheets.

**Preparation checklist**

- Confirm scope and time period.
- Pull evidence from approved sources (system of record).
- Ensure maker–checker approvals are visible where required.
- Redact only where permitted and necessary, and record redaction rationale.
- Validate evidence before submission (peer review for high-risk items).

**Submission rules**

- Use the approved repository/secure channel for sharing.
- Include an index (“evidence pack cover sheet”) listing:

  - item number, description, source, date, and owner

- Maintain a copy of what was submitted and when (audit trail).

**Do / Don’t**

- **Do:** answer exactly what’s asked; ask liaison to clarify ambiguous requests.
- **Don’t:** create new “evidence” after the fact; don’t provide unreviewed extracts; don’t share via informal chat or personal email.

---

### 13.3 Regulatory exams: communication rules and document handling

**Regulatory engagement governance**

- Regulators are engaged only through designated roles (e.g., Head of Compliance/Legal and assigned regulatory liaison).
- Employees must not contact regulators directly unless explicitly authorized.

**Communication rules**

- Be factual, concise, and consistent.
- If you don’t know, say so and escalate to the liaison—do not guess.
- Do not commit to timelines or actions without approval.
- Any material statements must be backed by evidence or documented policy.

**Document handling**

- Use controlled repositories and approved secure transfer methods.
- Maintain a regulator request log including:

  - request text, date received, due date
  - owner, status, and submission date
  - evidence pack index and references

- Ensure documents are current versions; include version numbers and effective dates.
- Where permitted, minimize disclosure (principle of least disclosure) while still meeting the request.

**Confidentiality**

- Treat exam requests and responses as confidential.
- Follow data classification and privacy rules for customer/employee information.

---

### 13.4 Management action plans (MAPs) and tracking

**Objective.**
Ensure findings from audit, regulators, or internal reviews are remediated on time with sustainable fixes.

**What is a MAP**
A Management Action Plan is a formal remediation commitment that includes:

- finding statement and risk description
- root cause
- corrective actions (what will change)
- preventive actions (how recurrence will be prevented)
- owners and accountable executive
- milestones and deadlines
- validation method (how effectiveness will be proven)

**MAP lifecycle**

1. **Register**

   - Log the finding with severity, due date, and impacted areas.

2. **Design**

   - Define actions, timeline, resources, and dependencies.

3. **Approve**

   - Obtain approvals per governance (Ops/Compliance/ORM/IT as applicable).

4. **Execute**

   - Implement actions; store implementation evidence.

5. **Validate**

   - Independent validation (QA, control testing, ORM review, or Internal Audit re-test).

6. **Close**

   - Close only after validation evidence is accepted and residual risk is addressed.

**Tracking requirements**

- Central tracker with status, milestones, blockers, and escalation triggers.
- Overdue MAPs require escalation to the relevant governance committee.

---

### 13.5 Model of “3 lines of defense” in practice

**1st line (Business & Operations)**

- Owns process execution and day-to-day controls.
- Identifies and logs issues/incidents.
- Produces evidence that controls were performed.

**2nd line (Compliance, Operational Risk, Finance Controls, IT Risk)**

- Defines requirements, sets standards, and provides oversight.
- Monitors KRIs, performs reviews, and challenges control design/effectiveness.
- Advises on regulatory obligations and risk acceptance/exceptions.

**3rd line (Internal Audit)**

- Independently evaluates governance, control design, and operating effectiveness.
- Performs audits and follow-up testing on MAP closures.

**Key practice expectations**

- Clear RACI per process/control.
- No “self-assurance” for 3rd line—Internal Audit remains independent.
- Issues are not considered resolved until independently validated where required.

---

---

## 14) Appendices: templates, checklists, and job aids

### 14.1 SOP templates (step-by-step)

**SOP Template (minimum fields)**

- SOP Title, SOP ID, Version, Effective Date
- Purpose and scope
- Definitions (if needed)
- Roles & responsibilities (RACI)
- Inputs / prerequisites
- Step-by-step procedure (numbered steps)
- Controls embedded per step (control ID, maker–checker, approvals)
- Evidence to retain (what/where/how long)
- Exceptions and escalation rules
- SLAs/cut-off times (if applicable)
- Related policies/standards
- Change log

---

### 14.2 Forms

**A) Onboarding checklist (Retail/SME/Corporate variants)**

- Customer type and risk tier
- Required documents list with verification ticks
- Screening completed (sanctions/PEP) with disposition reference
- Risk rating assigned and approved
- Account setup approvals (maker–checker)
- Evidence pack location and reviewer sign-off

**B) Exception request form**

- Exception type (policy/procedure/control)
- Business rationale and scope (who/what/where)
- Risk assessment (impact, likelihood, compensating controls)
- Requested duration and expiry date
- Required approvers (per DoA) and consultations (Compliance/ORM/IT)
- Evidence requirements and monitoring plan
- Approval decision and conditions

**C) Incident report form**

- Incident summary (what/when/how detected)
- Impact assessment (customers, funds, systems, compliance)
- Severity classification and rationale
- Immediate containment actions taken
- Stakeholders notified and timestamps
- Root cause hypothesis (initial) and investigation plan
- Remediation actions, owners, and due dates
- Post-incident review and lessons learned

**D) SAR/STR pack (where applicable)**

- Case ID and reporting decision owner
- Customer identifiers and profile summary
- Transaction summary and timeline
- Suspicion rationale and supporting evidence list
- Internal investigation notes and disposition
- Approvals and submission record (date/time/channel)
- Confidential handling label and access restrictions

---

### 14.3 Sample customer communications

Provide approved templates for common scenarios, such as:

- Request for additional KYC documents
- Account status update or hold notification (where permitted)
- Dispute/chargeback receipt confirmation and status updates
- Complaint acknowledgement and resolution notice
- Fraud/scam safety guidance and next steps
- Service outage advisory (status + support channels)

Each template should include:

- required disclaimers and escalation language
- prohibited language list (avoid admissions where inappropriate)
- approval owner (Legal/Compliance/Customer Service governance)

---

### 14.4 Control testing checklists

**Control testing template**

- Control ID and description
- Control owner and frequency
- Population and sampling method
- Test steps and acceptance criteria
- Evidence reviewed and references
- Results (pass/fail) with findings
- Root cause and remediation actions
- Re-test plan and closure criteria

**Common control checklists**

- Maker–checker approvals present and valid
- Reconciliations completed and independently reviewed
- KYC refresh completed within required timeframes
- Sanctions dispositions documented with evidence
- Access changes approved and logged
- Incident records complete (timeline, actions, approvals)

---

### 14.5 Reference matrices

**A) Approval limits / DoA matrix**

- Category (fees, limits, exceptions, write-offs, privileged access)
- Approval level required by threshold/risk tier
- Required consultations and evidence
- Validity period for approvals

**B) Records retention schedule**

- Record type, owner, repository
- Minimum retention period
- Disposition method
- Legal hold override rule

**C) Escalation contacts matrix**

- Scenario (AML/sanctions, fraud, outage, data/privacy, reconciliation breaks)
- Primary contact role + backup role
- Channel (ticket queue/hotline), SLA for response
- Escalation chain (Level 1/2/3)
