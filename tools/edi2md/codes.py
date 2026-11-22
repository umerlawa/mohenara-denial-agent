"""Decode tables for the code systems present in corpus v2-chain-corpus-v1.1.
Every lookup keeps the raw code; unknown codes fall back to the raw code alone."""

CARC = {
    "1": "deductible amount",
    "2": "coinsurance amount",
    "3": "copayment amount",
    "4": "procedure code is inconsistent with the modifier used",
    "5": "procedure code/type of bill is inconsistent with the place of service",
    "16": "claim/service lacks information or has submission/billing error",
    "18": "exact duplicate claim/service",
    "22": "care may be covered by another payer per coordination of benefits",
    "23": "impact of prior payer(s) adjudication",
    "24": "charges covered under a capitation agreement/managed care plan",
    "27": "expenses incurred after coverage terminated",
    "29": "the time limit for filing has expired",
    "45": "charge exceeds fee schedule/maximum allowable, contractual",
    "50": "non-covered: not deemed a medical necessity by the payer",
    "97": "payment included in the allowance for another service, bundled",
    "119": "benefit maximum for this time period has been reached",
    "151": "information does not support this many/frequency of services",
    "236": "procedure/modifier combination not compatible per coding guidelines, bundled",
}

CAS_GROUP = {
    "CO": "Contractual Obligation",
    "PR": "Patient Responsibility",
    "OA": "Other Adjustment",
    "PI": "Payer Initiated",
}

RARC = {
    "N362": "the number of days or units exceeds the acceptable maximum",
    "N20": "service not payable with other service rendered on the same date",
    "N822": "missing procedure modifier(s)",
    "M80": "not covered when performed with same-day service",
    "N286": "missing/incomplete/invalid referring provider primary identifier",
    "N30": "patient ineligible for this service",
    "N211": "you may not appeal this decision",
    "M77": "missing/incomplete/invalid place of service",
    "MA04": "secondary payment cannot be considered without primary payer identity",
    "N435": "exceeds number/frequency approved or allowed within time period",
    "N111": "no appeal right except duplicate claim/service issue",
}

CLP_STATUS = {
    "1": "processed as primary, paid",
    "2": "processed as secondary, paid",
    "3": "processed as tertiary, paid",
    "4": "denied",
    "22": "reversal of previous payment",
}

FILING = {
    "MB": "Medicare Part B",
    "CI": "commercial insurance",
    "HM": "HMO",
}

EB01 = {
    "1": "active coverage",
    "6": "inactive",
    "R": "other or additional payer",
}

EB03 = {"30": "health benefit plan coverage"}

DATE_QUAL = {
    "405": "production date",
    "232": "claim statement period start",
    "233": "claim statement period end",
    "472": "service date",
    "050": "received date",
    "291": "plan date",
    "356": "eligibility begin",
    "357": "eligibility end",
    "434": "statement period",
}

NM1_ENTITY = {
    "41": "submitter",
    "40": "receiver",
    "85": "billing provider",
    "87": "pay-to provider",
    "IL": "insured/subscriber",
    "QC": "patient",
    "PR": "payer",
    "PE": "payee",
    "DN": "referring provider",
    "82": "rendering provider",
    "77": "service facility",
    "AY": "clearinghouse",
    "1P": "provider",
}

ID_QUAL = {
    "MI": "member ID",
    "XX": "NPI",
    "PI": "payer ID",
    "46": "ETIN",
    "SY": "SSN",
    "FI": "federal tax ID",
    "EI": "employer ID/EIN",
    "TJ": "federal tax ID",
    "6R": "line item control number",
    "D9": "clearinghouse claim number",
    "F8": "original reference number",
}

POS = {
    "02": "telehealth (other than home)",
    "10": "telehealth (patient home)",
    "11": "office",
    "12": "home",
    "19": "off-campus outpatient hospital",
    "22": "on-campus outpatient hospital",
    "49": "independent clinic",
    "81": "independent laboratory",
}

FREQ = {"1": "original claim", "7": "replacement of prior claim", "8": "void of prior claim"}

MODIFIER = {
    "GP": "under PT plan of care",
    "GO": "under OT plan of care",
    "GW": "not related to hospice terminal condition",
    "GA": "ABN on file",
    "59": "distinct procedural service",
    "25": "significant separate E/M same day",
    "76": "repeat procedure same provider",
    "77": "repeat procedure other provider",
    "XE": "separate encounter",
    "XP": "separate practitioner",
    "XS": "separate structure",
    "XU": "unusual non-overlapping service",
    "95": "synchronous telemedicine",
}

STC_STATUS = {"A1": "acknowledged/received", "A2": "accepted for adjudication", "A7": "rejected"}
CLAIM_STATUS_CODE = {"19": "entity acknowledges receipt of claim", "20": "accepted for processing"}

BPR_METHOD = {"CHK": "check", "ACH": "ACH", "NON": "no payment"}
TRN_TYPE = {"1": "current transaction trace", "2": "referenced transaction trace"}


def date(v):
    """CCYYMMDD -> YYYY-MM-DD, otherwise raw."""
    if len(v) == 8 and v.isdigit():
        return f"{v[0:4]}-{v[4:6]}-{v[6:8]}"
    return v


def carc(group, code):
    g = CAS_GROUP.get(group, group)
    meaning = CARC.get(code)
    if meaning:
        return f"{group}-{code} ({g}: {meaning})"
    return f"{group}-{code} ({g}: meaning not in local table)"


def rarc(code):
    m = RARC.get(code)
    return f"{code} ({m})" if m else f"{code} (remark code, meaning not in local table)"


def look(table, code, label=""):
    m = table.get(code)
    if m:
        return f"{code} ({m})"
    return f"{code}{' (' + label + ')' if label else ''}"


def idq(q):
    """REF/ID qualifier with raw code kept."""
    m = ID_QUAL.get(q)
    return f"{q} ({m})" if m else q


def dq(q):
    """Date qualifier with raw code kept."""
    m = DATE_QUAL.get(q)
    return f"{m} ({q})" if m else f"date qualifier {q}"


def mods_str(mods):
    out = []
    for m in mods:
        meaning = MODIFIER.get(m)
        out.append(f"{m} ({meaning})" if meaning else m)
    return ", ".join(out)
