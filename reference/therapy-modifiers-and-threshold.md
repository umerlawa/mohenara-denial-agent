# Outpatient Therapy: Discipline Modifiers (GP/GO/GN), the KX Threshold, and Their Denials

> Retrieved 2026-08-12. Every rule below carries a primary-source citation.
>
> **Retrieval note:** direct HTTP fetching (`WebFetch`) of `cms.gov`, `x12.org`, `hhs.gov` and every
> MAC domain was blocked by this environment's egress proxy (gateway answered 403 to CONNECT;
> `EGRESS_BLOCKED` returned for each host). Rule text below was retrieved via **domain-restricted
> search over those same primary domains**, so the cited URL is the authoritative source but the
> wording is a retrieved excerpt, **not a verbatim full-text read**. Where a figure or a pairing
> could not be confirmed against the primary document itself, it is flagged inline and repeated in
> **Open questions** rather than asserted. Before quoting a passage back to a payer in an appeal
> letter, open the cited PDF and confirm the wording.
>
> **Two different denials warning.** CO-4/N822 and CO-119/N435 look adjacent — both are "a modifier
> is missing on a therapy line" — but they are **not the same problem and not the same fix**.
> CO-4 is a *claim-completeness* failure that Medicare does not even adjudicate; CO-119 is a
> *coverage* denial that Medicare does adjudicate and that carries appeal rights. Routing one down
> the other's path wastes the timely-filing clock. See §8.

---

## 0. Decision summary — read this first

| | **Missing discipline modifier** | **Missing KX above threshold** |
|---|---|---|
| Remit codes | **CO-4 + N822** | **CO-119 + N435** |
| What actually failed | The line carries an "always therapy" code with no GP/GO/GN | Cumulative allowed charges passed the CY threshold and the line has no KX |
| Adjudicated? | **No** — returned as unprocessable (RUC) | **Yes** — a denial |
| Appeal rights? | **None** | **Yes** — reopening / redetermination |
| Group code | **CO** | **CO** (unless a valid ABN + GA is on the line, then PR) |
| Balance is | **Provider write-off.** Not billable to the beneficiary. | **Provider write-off.** Not billable to the beneficiary. |
| Correct route | **Submit a new claim** with the modifier appended | **Reopening** (clerical) or **redetermination** to add KX |
| Never do | Never file an appeal — there is no determination to appeal | Never transfer the balance to the patient absent GA |

**The single most decision-relevant fact, resolved:** for both denials the balance is a
**provider write-off, not beneficiary liability**. See §7 for the full chain of authority. The only
circumstance that converts a threshold balance to patient responsibility is a valid ABN
(CMS-R-131) issued *before* the service and reported with modifier **GA** — and in that case the
remit shows group code **PR**, not CO. A CO-prefixed line is definitionally not billable to the
patient ([CMS, Health Care Payment and Remittance Advice](https://www.cms.gov/medicare/coding-billing/electronic-billing/health-care-payment-remittance-advice)).

---

## 1. Scope: which payers actually run these rules

| Payer type | Do GP/GO/GN and KX apply? | Source |
|---|---|---|
| **Medicare FFS Part B** (therapist in private practice, physician/NPP office, CORF/ORF, SNF Part B, HHA Part B, hospital outpatient) | **Yes.** Therapy modifiers and the KX threshold are Medicare constructs applied by MACs at adjudication. | [CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services); [Medicare Claims Processing Manual Ch. 5](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c05.pdf) |
| **Medicare Advantage** | **Not established.** MA plans are not bound to the FFS threshold mechanic and commonly substitute prior authorization / UM-vendor visit limits. See Open questions. | — |
| **Medicaid** | **Not established federally.** No federal analogue to the KX threshold; limits are set state by state. See Open questions. | — |
| **Commercial / ERISA** | **Not established.** Visit-count caps under the plan document are the common construct, not KX. See Open questions. | — |

> **Do not present these as universal rules.** Everything below is sourced to Medicare FFS
> guidance. A CO-119 from a commercial payer is a **benefit-limit** denial under the plan document
> and its remedy is a benefit-limit appeal with the plan's own accumulator, not a KX modifier.

---

## 2. The four codes, keyed

### 2.1 CARC (Claim Adjustment Reason Codes)

| CARC | Wording | Confidence | Source |
|---|---|---|---|
| **4** | "The procedure code is inconsistent with the modifier used **or a required modifier is missing**." | Wording confirmed; consistent across MAC and X12-derived listings. | [X12, Claim Adjustment Reason Codes](https://x12.org/codes/claim-adjustment-reason-codes); [Noridian, Reason Code 4](https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/m114-n565-4) |
| **119** | "Benefit maximum for this time period or occurrence has been reached." | Wording confirmed; CMS names this code explicitly as the therapy-threshold denial. | [X12, Claim Adjustment Reason Codes](https://x12.org/codes/claim-adjustment-reason-codes); [Medicare Claims Processing Manual Ch. 5](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c05.pdf) |

The operative half of CARC 4 for therapy claims is the **second** clause. The modifier is not
*wrong*; it is *absent*. This matters when reading the remit: a CO-4 on a 97110 line billed by a
therapist in private practice is almost always "no GP/GO/GN," not "GP conflicts with the code."

### 2.2 RARC (Remittance Advice Remark Codes)

| RARC | Wording | Confidence | Source |
|---|---|---|---|
| **N822** | "Missing procedure modifier(s)." | Wording confirmed. MAC guidance describes it as "submitting a CPT/HCPCS code without a required modifier." | [X12, Remittance Advice Remark Codes](https://x12.org/codes/remittance-advice-remark-codes); [Noridian, Denial Code Resolution — JE Part B](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/denial-resolution) |
| **N435** | "Exceeds number/frequency approved/allowed within time period without support documentation." | Wording confirmed across multiple independent government code listings. | [X12, Remittance Advice Remark Codes](https://x12.org/codes/remittance-advice-remark-codes); [Nevada Medicaid, Web Announcement 3479](https://www.medicaid.nv.gov/Downloads/provider/web_announcement_3479_20241113.pdf) |

**Read N435 literally — it is the tell.** N435 says the *documentation* did not support exceeding
the allowed amount. On a therapy claim that means one of two very different things, and the
distinction drives the remedy:

- **KX was never appended** → nothing was attested, so nothing was supported. Clerical. Fixable.
- **KX was appended but the record does not justify continued therapy** → the attestation was
  made and rejected on review. Not clerical. This is a medical-necessity fight requiring records,
  and it is an active RAC audit topic ([CMS, Approved RAC Topic 0228 — Therapy Claims Billed with KX Modifier](https://www.cms.gov/data-research/monitoring-programs/medicare-fee-service-compliance-programs/medicare-fee-service-recovery-audit-program/approved-rac-topics/0228-therapy-claims-billed-kx-modifier-medical-necessity-documentation-requirements)).

Check the submitted line for KX before choosing a route. Do not assume it was omitted.

---

## 3. Discipline modifiers GP / GO / GN

| Modifier | Discipline | Verbatim meaning |
|---|---|---|
| **GP** | Physical therapy | "Services delivered under an outpatient **physical therapy** plan of care" |
| **GO** | Occupational therapy | "Services delivered under an outpatient **occupational therapy** plan of care" |
| **GN** | Speech-language pathology | "Services delivered under an outpatient **speech-language pathology** plan of care" |

Source: [CMS Transmittal R4440CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2019downloads/R4440cp.pdf);
[CMS Transmittal R3814CP — Always Therapy](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2017Downloads/R3814CP.pdf);
[Noridian, Modifier GN](https://med.noridianmedicare.com/web/jeb/topics/modifiers/GN);
[Noridian, Modifier GP](https://med.noridianmedicare.com/web/jfb/topics/modifiers/GP).

**The modifier follows the plan of care, not the licence of the person in the room.** The
descriptors say "delivered under an outpatient ___ plan of care." CMS states the modifiers "refer
only to services provided under plans of care for physical therapy, occupational therapy and
speech-language pathology services," and that GN/GO/GP identify "when each outpatient therapy
service is furnished under a speech-language pathology, occupational therapy, or physical therapy
plan of care" ([R4440CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2019downloads/R4440cp.pdf)).
A service delivered by a PTA under a PT plan of care therefore still carries **GP**; the assistant
fact is carried separately by **CQ** (PTA) or **CO** (OTA), which must be paired with GP or GO
respectively — claims with modifiers not so paired are "rejected/returned as unprocessable"
([CMS, Billing Examples Using CQ/CO Modifiers](https://www.cms.gov/medicare/coding-billing/therapy-services/billing-examples-using-cq-co-modifiers-services-furnished-whole-or-part-ptas-otas)).

> **Modifier CO (OTA) and group code CO are different objects that share two letters.** On an 835,
> `CO` in the CAS segment is the group code; `CO` in the service-line modifier field is the OTA
> modifier. Never let a parser conflate them.

**Exactly one discipline modifier per line.** They are mutually exclusive — the line was furnished
under one plan of care. On institutional claims the pairing is enforced against the revenue code:
revenue code 43x (OT) lines may only carry GO, and 44x (SLP) lines may only carry GN
([R4440CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2019downloads/R4440cp.pdf)).
"Wrong discipline modifier for the revenue code" and "no modifier at all" both land as a
completeness failure, not a coverage denial.

**They may never be used off-list.** CMS: the modifiers "should never be used with codes that are
not on the list of applicable therapy services"
([R4440CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2019downloads/R4440cp.pdf)).
Appending GP to a non-therapy code to clear an edit is a compliance exposure, not a fix.

---

## 4. "Always therapy" codes — including the four in this corpus

CMS maintains an annual **Therapy Code List** dividing codes into those that **always** describe a
therapy service and those that **sometimes** do
([CMS Transmittal R13431CP — 2026 Annual Update to the Therapy Code List](https://www.cms.gov/files/document/r13431cp.pdf);
[MLN MM14250 — Therapy Code List: 2026 Annual Update](https://www.cms.gov/files/document/mm14250-therapy-code-list-2026-annual-update.pdf)).

| CPT | Descriptor (short) | Status | Discipline modifier |
|---|---|---|---|
| **97110** | Therapeutic exercises | **Always therapy** | Required — GP/GO/GN |
| **97112** | Neuromuscular re-education | **Always therapy** | Required — GP/GO/GN |
| **97140** | Manual therapy techniques | **Always therapy** | Required — GP/GO/GN |
| **97530** | Therapeutic activities | **Always therapy** | Required — GP/GO/GN |

Sources: [CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services);
[R3814CP — Always Therapy](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2017Downloads/R3814CP.pdf);
[MLN MM10176 — Updated Editing of Always Therapy Services](https://www.cms.gov/sites/default/files/repo-new/50/mm101762.pdf);
[MCD Article A56566 — Billing and Coding: Outpatient Physical and Occupational Therapy Services](https://www.cms.gov/medicare-coverage-database/view/article.aspx?articleid=56566).

Two rules that decide most CO-4 cases:

1. **Always-therapy codes always need a discipline modifier**, whoever furnishes them. CMS
   instructs contractors to "return claims for 'always therapy' codes when they do not contain
   appropriate therapy modifiers"
   ([MM10176](https://www.cms.gov/sites/default/files/repo-new/50/mm101762.pdf);
   [R3814CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2017Downloads/R3814CP.pdf)).
2. **Everything a therapist in private practice furnishes is a therapy service**, regardless of
   whether the code is classified always- or sometimes-therapy, and the appropriate therapy
   modifier must be on the claim
   ([R3814CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2017Downloads/R3814CP.pdf)).
   Noridian implements this by provider specialty: with specialty codes 65 (PT) or 67 (OT) on the
   claim, an applicable HCPCS code without GN/GO/GP is **returned as unprocessable**
   ([Noridian, Modifiers — JE Part B](https://med.noridianmedicare.com/web/jeb/topics/modifiers)).

So a CO-4/N822 on 97110 from a PT private practice is unambiguous: the discipline modifier was
omitted. There is no "but the code was sometimes-therapy" defence available.

---

## 5. The KX modifier and the therapy threshold

### 5.1 What KX attests

KX is an **attestation by the clinician**, not a billing flag. CMS: "use of modifier KX indicates
that the clinician attests that services at, and above, the therapy threshold are medically
necessary and reasonable, with justification for continued therapy documented in the patient's
medical record"
([CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services);
[CMS RAC Topic 0228](https://www.cms.gov/data-research/monitoring-programs/medicare-fee-service-compliance-programs/medicare-fee-service-recovery-audit-program/approved-rac-topics/0228-therapy-claims-billed-kx-modifier-medical-necessity-documentation-requirements)).

Two consequences a denial system must encode:

- **The justification lives in the medical record, not on the claim.** Nothing is attached at
  submission. KX asserts that the record already contains it.
- **KX is not self-proving.** Appending it does not make the service payable; it makes it
  *adjudicable*, and exposes it to targeted and RAC review. Adding KX to a claim whose record
  does not support continued therapy converts a write-off into a false-attestation exposure.
  Only append KX when the documentation actually exists.

The generic HCPCS descriptor for KX is "Requirements specified in the medical policy have been
met" ([Palmetto GBA, JM Part B — HCPCS Modifier KX](https://www.palmettogba.com/palmetto/jmb.nsf/DID/9WQ50UO6SS)).
For therapy, the medical policy whose requirements are being attested is the threshold exception.

### 5.2 The thresholds

| Item | CY 2026 amount | Source |
|---|---|---|
| KX modifier threshold — **PT and SLP combined** | **$2,480** | [CMS Transmittal R13437CP — 2026 Annual Update of Per-Beneficiary Threshold Amounts](https://www.cms.gov/files/document/r13437cp.pdf) ([landing page](https://www.cms.gov/medicare/regulations-guidance/transmittals/2025-transmittals/r13437cp)) |
| KX modifier threshold — **OT, separately** | **$2,480** | Same. *(See Open questions — the OT figure was returned by search over R13437CP but not read from the PDF itself.)* |
| Targeted medical review (MR) threshold — PT/SLP combined | **$3,000** | [R13437CP](https://www.cms.gov/files/document/r13437cp.pdf); [CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services) |
| Targeted medical review (MR) threshold — OT | **$3,000** | Same |

Mechanics:

- **Two separate accumulators.** One for PT and SLP **combined**, one for OT **alone**. A
  beneficiary can be over threshold for PT/SLP and under for OT on the same date. Never accumulate
  all three together.
- **Per beneficiary, per calendar year.** "Financial limitations or thresholds are applied to
  therapy services for each beneficiary," and Medicare "applies these thresholds in order,
  according to the dates when the claims were **received**"
  ([Noridian, Per-Beneficiary KX Modifier Thresholds — JF Part B](https://med.noridianmedicare.com/web/jfb/specialties/outpatient-therapy/per-beneficiary_kx_modifier_thresholds)).
  Received-date ordering means the accumulator is **not** under the billing provider's control —
  another provider's later-submitted claim for an earlier date can consume threshold first.
- **The accumulator is national, not per-provider.** It follows the beneficiary across every
  provider billing therapy that year. A first-ever claim from your clinic can still be over
  threshold.
- **KX goes on the line.** It is appended to each line item of service at and above the threshold
  ([CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services)).
- **Indexed annually by the MEI.** The dollar figure changes every January
  ([CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services)). **Use the
  threshold in effect for the date of service's calendar year, never the current year's figure.**
- **KX does not replace the discipline modifier.** An above-threshold 97110 line carries **both**
  GP and KX. Supplying KX while omitting GP still produces CO-4.
- **Statutory basis.** Section 50202 of the Bipartisan Budget Act of 2018 added §1833(g)(7)(A) of
  the Social Security Act, preserving the former therapy cap amounts as thresholds above which
  claims must include KX. The hard cap is gone; the threshold is not
  ([CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services);
  [CMS Transmittal R12702OTN](https://www.cms.gov/files/document/r12702otn.pdf)).

### 5.3 What happens above threshold with no KX

Plainly stated by CMS: "Claims for services over the KX modifier threshold amounts **without the KX
modifier are denied**" ([CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services);
[R13437CP](https://www.cms.gov/files/document/r13437cp.pdf)). The denial carries **CARC 119**
([Medicare Claims Processing Manual Ch. 5](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c05.pdf)).

Note the shape of this denial: it is a **coverage** denial, adjudicated, with appeal rights and
with limitation-of-liability protection attached (§7). That is why it behaves nothing like CO-4.

### 5.4 The targeted medical review threshold ($3,000)

- **It is targeted, not automatic.** Crossing $3,000 does not itself trigger review. CMS retained
  "the targeted medical review (MR) process at a lower threshold amount of $3,000"
  ([CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services);
  [R13437CP](https://www.cms.gov/files/document/r13437cp.pdf)). Selection criteria are applied on
  top of the dollar figure.
- **It does not change payment.** Passing $3,000 does not add a claim requirement beyond KX. It
  changes **audit exposure**, not adjudication.
- **$3,000 is frozen, then indexed.** It stays at $3,000 for the statutory period and is indexed by
  the MEI thereafter. *(Sources retrieved disagree on whether the freeze runs through CY 2027 with
  indexing beginning CY 2028, or through CY 2028 — see Open questions. The $3,000 figure itself is
  not in doubt for the current year.)*

---

## 6. Recognition table — mapping a remit line to a diagnosis

| Remit | Line facts | Diagnosis | Route |
|---|---|---|---|
| CO-4 + N822 | 97110/97112/97140/97530, no GP/GO/GN | Discipline modifier omitted | **New claim** (§8.1) |
| CO-4 + N822 | GO on a 43x-revenue line, or GP with CO (OTA) unpaired | Wrong/unpaired discipline modifier | **New claim** (§8.1) |
| CO-119 + N435 | Above CY threshold, **no KX** on line | KX omitted; nothing attested | **Reopening** (§8.2) |
| CO-119 + N435 | Above CY threshold, **KX present** | Attestation rejected on documentation | **Redetermination with records** (§8.2) |
| CO-119 + N435 | Accumulator disputed (another provider's claims) | Threshold arithmetic, not a modifier problem | Verify accumulator before any resubmission |
| **PR**-119 | GA on the line, valid ABN on file | Liability validly transferred | Bill the patient (§7.3) |

---

## 7. THE GROUP CODE — resolved: provider write-off, not patient liability

This is the question the previous version of this file left open. The sources do resolve it.

### 7.1 What the group code means

> "Group Codes assign financial responsibility for the unpaid portion of the claim balance — e.g.,
> **CO (Contractual Obligation) assigns responsibility to the provider** and **PR (Patient
> Responsibility) assigns responsibility to the patient**."
> — [CMS, Health Care Payment and Remittance Advice](https://www.cms.gov/medicare/coding-billing/electronic-billing/health-care-payment-remittance-advice);
> [Medicare Claims Processing Manual Ch. 22 — Remittance Advice](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf)

CO is used "when a contractual agreement between the payer and payee, **or a regulatory
requirement**, resulted in an adjustment." And the operative billing rule: **Medicare
beneficiaries may be billed only when group code PR is used with an adjustment**
([CMS, Health Care Payment and Remittance Advice](https://www.cms.gov/medicare/coding-billing/electronic-billing/health-care-payment-remittance-advice)).

**Therefore: a CO-prefixed balance is a write-off. Transferring a CO balance to patient
responsibility is improper billing, not an aggressive collections posture.**

### 7.2 Why CO-119 is CO — the chain of authority

The threshold denial is not merely conventionally CO; it is CO because a statute puts it there.

1. **Limitation of liability applies to therapy threshold denials.** §1833(g) of the Social
   Security Act extends the §1879 limitation-of-liability (LOL) protections to beneficiaries
   receiving outpatient therapy services when services are denied for certain reasons —
   **including failure to include a necessary KX modifier**
   ([CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services);
   [CMS, Outpatient Therapy Services and ABN FAQ (Aug 2018)](https://www.cms.gov/medicare/billing/therapyservices/downloads/2018-08-abn-faq.pdf)).
   Section 50202 of the BBA of 2018 did not disturb the liability procedures effective since
   January 1, 2013 ([CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services)).
2. **Under LOL the provider eats it.** "The therapist and therapy providers (outpatient
   facility/clinics) are **financially responsible** when Medicare denies payment for therapy
   services above the threshold amount **for failure to use the KX modifier**"
   ([Noridian, Per-Beneficiary KX Modifier Thresholds — JF Part B](https://med.noridianmedicare.com/web/jfb/specialties/outpatient-therapy/per-beneficiary_kx_modifier_thresholds);
   [Noridian, Outpatient Therapy Services and ABN Use](https://med.noridianmedicare.com/web/jfb/topics/abn/outpatient-therapy-services-and-advance-beneficiary-notice-of-noncoverage-abn-use)).
3. **Provider responsibility is expressed on the remit as CO** (§7.1).

**Conclusion: CO-119 is a provider write-off. The remedy is a corrected submission, never a
patient transfer.**

### 7.3 The one exception — ABN and modifier GA

Liability transfers to the beneficiary only if the provider issued a **valid** ABN
(Form CMS-R-131) **before** furnishing the service and reports it with **GA**. CMS states the
mapping directly:

- **Group Code PR** assigns financial liability to the beneficiary if the claim carries a **GA**
  modifier indicating a signed ABN is on file.
- **Group Code CO** assigns financial liability to the provider if the claim carries a **GZ**
  modifier indicating **no** signed ABN is on file.

Sources: [CMS Transmittal R12763CP](https://www.cms.gov/files/document/r12763cp.pdf);
[CMS, Outpatient Therapy Services and ABN FAQ (Aug 2018)](https://www.cms.gov/medicare/billing/therapyservices/downloads/2018-08-abn-faq.pdf);
[CMS, ABN and Therapy Caps FAQ](https://www.cms.gov/Medicare/Billing/TherapyServices/Downloads/ABN-Noncoverage-FAQ.pdf).

Hard constraints on that exception:

- **The ABN must predate the service.** "If the ABN isn't issued when it is required and Medicare
  doesn't pay the claim, the provider/supplier will be liable for the charges"
  ([CMS Aug-2018 ABN FAQ](https://www.cms.gov/medicare/billing/therapyservices/downloads/2018-08-abn-faq.pdf)).
  An ABN cannot be obtained retroactively to rescue a denied claim. **If the remit shows CO-119
  and no GA was on the submitted line, the write-off is already fixed** — no signature collected
  today changes it.
- **Do not use GA and KX together** ([CMS, Therapy Services](https://www.cms.gov/medicare/coding-billing/therapy-services)).
  They assert opposite things: KX says "this is medically necessary and documented"; GA says "I
  expect Medicare to find this not medically necessary and I warned the patient." Reporting both
  on one line is internally contradictory.
- GZ (no ABN on file) explicitly produces **CO** — provider liability
  ([R12763CP](https://www.cms.gov/files/document/r12763cp.pdf)).

### 7.4 Why CO-4 is CO

CO-4 needs no liability analysis, because **no coverage determination was ever made**. A claim
returned as unprocessable "does not meet the criteria to be considered as a claim, **is not
denied**, and, as such, is not afforded appeal rights"
([Medicare Claims Processing Manual Ch. 1, §80.3.1](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf)).
There is no determination that the service was non-covered, so there is no basis on which the
beneficiary could be made liable. The defect is the **provider's own incomplete submission**.
Beneficiaries may be billed only under PR (§7.1). **A CO-4 balance is a provider write-off until
the claim is submitted correctly** — and once it is submitted correctly it should simply pay,
leaving only ordinary deductible/coinsurance as PR.

---

## 8. The correction mechanism — the two routes are different

Medicare Part B does **not** accept the institutional frequency-code-7 replacement-claim mechanic.
See `resubmission-and-frequency-codes.md`. The actual routes are below.

### 8.1 Missing discipline modifier (CO-4 + N822) → **submit a new claim**

Not a corrected claim. Not a reopening. Not an appeal. A **new claim**.

- CMS instructs contractors to **return** professional claims reporting always-therapy HCPCS codes
  whenever the appropriate GN/GO/GP is missing
  ([R3814CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2017Downloads/R3814CP.pdf);
  [MM10176](https://www.cms.gov/sites/default/files/repo-new/50/mm101762.pdf)).
- A returned/unprocessable claim is not a determination and has **no appeal rights**; contractors
  "shall not deny claims and afford appeal rights for incomplete or invalid information." The
  claim is returned "explaining the error(s) and how to correct the errors **prior to
  resubmission**"
  ([Medicare Claims Processing Manual Ch. 1, §80.3.1](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf)).
- MAC guidance for N822 states the resolution directly: research the proper modifier to report
  with the CPT/HCPCS code and **submit a new claim**
  ([Noridian, Denial Code Resolution — JE Part B](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/denial-resolution);
  [Noridian, Denial Code Resolution — JF Part B](https://med.noridianmedicare.com/web/jfb/topics/claim-submission/denial-resolution)).

> **Timely filing consequence — the trap in this denial.** Because the returned claim was never a
> claim, it **did not stop the timely-filing clock**. The one-year filing limit continues to run
> from the date of service. A CO-4/N822 sitting in a work queue is losing time that no appeal can
> recover. Work these first. Cross-reference `timely-filing.md`.
>
> **Do not file an appeal on a CO-4.** There is no determination to appeal; a redetermination
> request will be dismissed and the filing clock will keep running while it is pending.

### 8.2 Missing KX above threshold (CO-119 + N435) → **reopening**, or redetermination

Here a determination **was** made, so appeal machinery exists and the reopening route is available.

- Omitting KX from a line where the documentation already supported it is a **minor error or
  omission**. The law "provides that reopenings may be done to correct minor errors or omissions,
  that is, clerical errors," and MACs "**do not** process claim corrections involving minor errors
  and omissions through the appeals process"
  ([Medicare Claims Processing Manual Ch. 34 — Reopening and Revision of Claim Determinations](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf)).
- If a provider files an appeal but the issue is a minor error or omission, contractors "shall
  treat the request as a request for reopening" regardless
  ([MCPM Ch. 34](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf)).
- **Reopening window: one year from the initial determination**
  ([Noridian, Reopening — JF Part B](https://med.noridianmedicare.com/web/jfb/topics/appeals/reopening)).
- **But KX is not always reopening-eligible.** At least one MAC treats KX as a *complex* modifier
  routed through appeal: "a redetermination request may be submitted to add, change or remove the
  KX modifier or other specific complex modifiers"
  ([Noridian, Per-Beneficiary KX Modifier Thresholds — JF Part B](https://med.noridianmedicare.com/web/jfb/specialties/outpatient-therapy/per-beneficiary_kx_modifier_thresholds)).
  Reopening is discretionary — "all decisions on granting reopenings are at the contractor's
  discretion" ([MCPM Ch. 34](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf)).
  **Check the servicing MAC's own modifier-reopening list before choosing.** Redetermination is the
  safe fallback: it is always available, and a request that should have been a reopening is
  converted rather than dismissed.
- **Redetermination window: 120 days from receipt of the initial determination.** See
  `appeal-levels.md`.
- Where KX **was** present and the denial reflects a documentation judgment, reopening is wrong on
  the merits. That is a **redetermination with the medical record attached** — the treatment notes,
  progress notes, and re-evaluation that justify therapy continuing past the threshold
  ([CMS RAC Topic 0228](https://www.cms.gov/data-research/monitoring-programs/medicare-fee-service-compliance-programs/medicare-fee-service-recovery-audit-program/approved-rac-topics/0228-therapy-claims-billed-kx-modifier-medical-necessity-documentation-requirements)).

### 8.3 Precondition before adding KX to anything

Do not add KX reflexively to clear a CO-119. KX is an attestation (§5.1). Before submitting:

1. Confirm the beneficiary genuinely crossed the CY threshold for **that discipline's**
   accumulator (PT/SLP combined vs OT) — if not, the denial is an accumulator error and adding KX
   concedes a fact that is not true.
2. Confirm the medical record **already contains** the justification for therapy beyond the
   threshold, dated on or before the date of service.
3. Only then append KX to the affected lines, keeping GP/GO/GN in place.

---

## Open questions

Unresolved items. Each names the source that should settle it. None of these are guessed at above.

**Figures needing a verbatim read of the primary PDF**

- The **CY 2026 OT threshold** is reported as **$2,480**, matching PT/SLP. This was returned by
  domain-restricted search over [R13437CP](https://www.cms.gov/files/document/r13437cp.pdf) but the
  PDF itself could not be opened (egress blocked). The equality is consistent with prior years
  (2025: $2,410 for both), but **read the transmittal before relying on the OT figure**.
- The **MR threshold freeze end year** is reported inconsistently across retrieved excerpts — some
  say $3,000 holds until CY 2028, others until CY 2027 with MEI indexing beginning CY 2028. These
  may be the same rule stated two ways, but the exact statutory sunset was not confirmed. Read
  [R13437CP](https://www.cms.gov/files/document/r13437cp.pdf) and BBA 2018 §50202.
- Whether the threshold accumulates against **allowed** charges or **billed** charges, and whether
  beneficiary deductible/coinsurance counts toward it, was not confirmed from a primary source.
  Source: [Medicare Claims Processing Manual Ch. 5](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c05.pdf), financial-limitation section.

**Code pairing**

- The corpus pairs **CARC 4 with N822**. Both wordings are confirmed independently, and MAC
  guidance confirms missing therapy modifiers are returned as unprocessable with N822. However,
  one retrieved excerpt associates N822 with **CARC 16** ("Claim/service lacks information or has
  submission billing error(s)") rather than CARC 4. Both pairings appear in the field and MACs
  differ. **The routing in §8.1 is unaffected** — CARC 16 and CARC 4 both indicate an unprocessable
  return here — but a system that keys strictly on `4` should also match `16` + `N822`. Confirm
  against the servicing MAC's denial-code-resolution page.
- Whether a **wrong-discipline** modifier (GP on an OT plan of care) yields CO-4/N822 or is instead
  caught by a revenue-code edit with different codes was not confirmed.

**Mechanism**

- Whether **KX is reopening-eligible** varies by MAC (§8.2). No CMS-level list of
  reopening-eligible modifiers was retrieved. Confirm per MAC before routing.
- Whether the **one-year timely-filing limit** is ever tolled for a claim returned as unprocessable
  was not confirmed; §80.3.1 implies it is not. Verify against
  [MCPM Ch. 1](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf).

**Payer-type divergence — must not be collapsed into the Medicare rules above**

- Whether **Medicare Advantage** plans apply the KX threshold construct at all, or substitute prior
  authorization and UM-vendor visit limits. If MA substitutes its own limits, a CO-119 from an MA
  plan is a plan-benefit denial and §7's LOL analysis **does not transfer**.
- Whether **Medicaid** programs require GP/GO/GN and what visit or dollar limits apply. These are
  set state by state; there is no federal analogue to the KX threshold to cite.
- Whether **commercial** plans use KX at all, or cap by visit count under the plan document — in
  which case the remedy is a benefit-limit appeal with the plan's accumulator, not a modifier
  correction, and the liability question is contractual rather than governed by §1879.

**Adjacent, deliberately out of scope here**

- **8-minute rule / timed-vs-untimed** unit counting for 97110, 97112, 97140, 97530. This drives
  unit-count denials, not modifier denials. Source:
  [MCPM Ch. 5](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c05.pdf).
- **NCCI PTP edits** among these four codes (notably 97140 paired against the others) and the
  59 / X{EPSU} rules. See `ncci-ptp-and-mue.md`.
- **MPPR** reduction on the practice-expense component of always-therapy codes on the same date.
  This is an underpayment dispute, not a denial, and must not be worked as one.
