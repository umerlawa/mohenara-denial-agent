"""Template v1: denial-resolution-ordered, token-lean markdown.
Rule: every decoded code keeps its raw form next to the meaning."""

import codes as C


def money(v):
    return f"${v}" if v else ""


def line_proc(cpt, mods):
    label = cpt
    if mods:
        label += "-" + "-".join(mods)
    return label


def party_line(p):
    role = C.NM1_ENTITY.get(p["entity"], "entity")
    bits_name = " ".join(x for x in [p.get("first"), p.get("middle"), p.get("last")] if x)
    if not bits_name:
        bits_name = p.get("last", "")
    bits = [f"{role} [{p['entity']}]: {bits_name}"]
    if p.get("id"):
        bits.append(f"{C.idq(p['id_qual'])} {p['id']}")
    for a in p.get("addr", []):
        bits.append(a.replace("*", ", "))
    if p.get("contact"):
        con = [x for x in p["contact"] if x]
        bits.append("contact " + " ".join(con))
    for q, v in p.get("refs", []):
        bits.append(f"{C.idq(q)} {v}")
    return "; ".join(bits)


def bht_line(bht, label):
    if not bht:
        return None
    extra = f", type {bht['type']}" if bht.get("type") else ""
    return (f"{label} reference {bht['ref']}, dated {C.date(bht['date'])} {bht['time']}, "
            f"purpose code {bht['purpose']}, structure {bht['structure']}{extra}.")


def render(case):
    out = []
    w = out.append
    cid = case["id"]
    e837 = case["files"].get("837")
    e835 = case["files"].get("835")
    e270 = case["files"].get("270")
    e271 = case["files"].get("271")
    e277 = case["files"].get("277")

    payer = e835["payer"]["name"] if e835 and e835.get("payer") else ""
    patient = ""
    subscriber_id = ""
    dob = ""
    gender = ""
    if e837:
        for p in e837["parties"]:
            if p["entity"] == "IL":
                patient = f"{p['first']} {p['last']}".strip()
                subscriber_id = p["id"]
        if e837.get("dmg"):
            dob = C.date(e837["dmg"]["dob"])
            gender = e837["dmg"]["gender"]
    dos = ""
    if e837 and e837["lines"]:
        d = e837["lines"][0].get("dos")
        if d:
            dos = C.date(d["value"])
    w(f"# Case {cid}")
    w("")
    w(f"Patient {patient}, DOB {dob}, sex {gender}, member ID {subscriber_id}. "
      f"Payer: {payer}. Service date {dos}.")

    if e835:
        clp = e835["clp"]
        st = C.look(C.CLP_STATUS, clp["status"])
        filing = C.look(C.FILING, clp["filing"])
        w("")
        w("## Adjudication outcome (835)")
        w(f"Claim {clp['claim_id']}: status {st}. Billed {money(clp['charge'])}, "
          f"paid {money(clp['paid'])}, patient responsibility {money(clp['patient_resp'])}. "
          f"Filing indicator {filing}. Payer claim control {clp['payer_control']}, "
          f"POS {C.look(C.POS, clp['pos'])}, frequency {C.look(C.FREQ, clp['frequency'])}.")
        bpr = e835["bpr"]
        w(f"Payment: {money(bpr['amount'])} by {C.look(C.BPR_METHOD, bpr['method'])}, "
          f"handling {bpr['handling']}.")
        for d in e835["dates"]:
            w(f"{C.dq(d['qual'])}: {C.date(d['value'])}.")
        for n1, label in ((e835.get("payer"), "Payer"), (e835.get("payee"), "Payee")):
            if not n1:
                continue
            bits = [f"{label} [{n1['entity']}]: {n1['name']}"]
            if n1.get("id"):
                bits.append(f"{C.idq(n1['id_qual'])} {n1['id']}")
            for a in n1.get("addr", []):
                bits.append(a.replace("*", ", "))
            if n1.get("contact"):
                bits.append("contact " + " ".join(x for x in n1["contact"] if x))
            w("; ".join(bits) + ".")
        for t in e835["trn"]:
            w(f"Trace ({C.look(C.TRN_TYPE, t['type'])}): {t['ref']}"
              + (f", originator {t['origin']}" if t.get("origin") else "") + ".")
        for d in e835["claim_dates"]:
            w(f"{C.dq(d['qual'])}: {C.date(d['value'])}.")
        if e835["moa"]:
            for m in e835["moa"]:
                w("Outpatient adjudication remarks (MOA): " + ", ".join(C.rarc(x) for x in m) + ".")
        for q, v in e835["refs"]:
            w(f"Payee {C.idq(q)}: {v}.")
        w("")
        w("Service lines:")
        w("")
        w("| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |")
        w("|---|---|---|---|---|---|---|")
        for i, ln in enumerate(e835["lines"], 1):
            adj = "; ".join(
                f"{C.carc(c['group'], c['code'])} {money(c['amount'])}"
                for c in ln["cas"]) or "none"
            rem = "; ".join(f"HE {C.rarc(r)}" for r in ln["rarcs"]) or ""
            allowed = "; ".join(f"allowed (B6) {money(v)}" for q, v in ln["amts"] if q == "B6")
            other_amts = "; ".join(f"amount {q} {money(v)}" for q, v in ln["amts"] if q != "B6")
            extra = " " + " ".join(x for x in [allowed, other_amts] if x) if (allowed or other_amts) else ""
            w(f"| {i} | {line_proc(ln['cpt'], ln['mods'])} | {ln['units']} | "
              f"{money(ln['charge'])} | {money(ln['paid'])}{extra} | {adj} | {rem} |")
        line_refs = []
        for ln in e835["lines"]:
            for q, v in ln.get("refs", []):
                line_refs.append(f"{v}" if q == "6R" else f"{C.idq(q)} {v}")
            for d in ln["dates"]:
                if d["qual"] != "472":
                    line_refs.append(f"{C.dq(d['qual'])} {C.date(d['value'])}")
        if line_refs:
            w("")
            w("Line item control numbers (REF 6R): " + ", ".join(line_refs) + ".")
        if any(ln["mods"] for ln in e835["lines"]):
            mods = sorted({m for ln in e835["lines"] for m in ln["mods"]})
            w("Modifiers on remit lines: " + C.mods_str(mods) + ".")
        if e835["claim_cas"]:
            adj = "; ".join(f"{C.carc(c['group'], c['code'])} {money(c['amount'])}" for c in e835["claim_cas"])
            w(f"Claim-level adjustments: {adj}.")
        if e835["claim_parties"]:
            w("Remit claim parties: " + "; ".join(party_line(p) for p in e835["claim_parties"]) + ".")

    if e837:
        w("")
        w("## Claim as billed (837P)")
        clm = e837["clm"]
        sbr = e837["sbr"] or {}
        dx = ", ".join(f"{d['code']} ({'principal, ' + d['qual'] if d['qual'] == 'ABK' else 'additional, ' + d['qual']})"
                       for d in e837["dx"])
        w(f"Claim {clm['id']}, total charge {money(clm['charge'])}, "
          f"POS {C.look(C.POS, clm['pos'])} (facility qualifier {clm['facility_qual']}), "
          f"frequency {C.look(C.FREQ, clm['frequency'])}. Diagnosis: {dx}.")
        w(f"Subscriber relationship code {sbr.get('relation', '')} (18 = self), "
          f"payer responsibility {sbr.get('payer_resp', '')} (P = primary), "
          f"claim filing {C.look(C.FILING, sbr.get('filing', ''))}.")
        w(f"Provider signature {clm['provider_sig']}, assignment {clm['assignment']}, "
          f"benefits assigned {clm['benefits_assign']}, release of info {clm['release']}.")
        w("")
        w("| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |")
        w("|---|---|---|---|---|---|---|")
        for ln in e837["lines"]:
            ref6r = "; ".join(v if q == "6R" else f"{C.idq(q)} {v}" for q, v in ln.get("refs", []))
            d = ln.get("dos", {})
            w(f"| {ln['lx']} | {line_proc(ln.get('cpt', ''), ln.get('mods', []))} | "
              f"{ln.get('units', '')} {ln.get('unit_type', '')} | {money(ln.get('charge', ''))} | "
              f"{C.date(d.get('value', ''))} | {ln.get('dx_pointer', '')} | {ref6r} |")
        mods = sorted({m for ln in e837["lines"] for m in ln.get("mods", [])})
        if mods:
            w("")
            w("Modifiers on claim: " + C.mods_str(mods) + ".")
        w("")
        w("Parties on claim:")
        for p in e837["parties"]:
            w(f"- {party_line(p)}")
        b = bht_line(e837["bht"], "Submission")
        if b:
            w(f"- {b}")

    if e271 or e270:
        w("")
        w("## Eligibility (270 inquiry / 271 response)")
    if e270:
        inq_date = ""
        for d in e270["dates"]:
            if d["qual"] == "291":
                inq_date = C.date(d["value"])
        svc = C.look(C.EB03, e270.get("eq") or "")
        traces = "; ".join(f"trace {t['ref']}" + (f" origin {t['origin']}" if t.get("origin") else "")
                           for t in e270["trn"])
        w(f"Inquiry for service type {svc}, {C.dq('291')} {inq_date}."
          + (f" {traces}." if traces else ""))
        who = "; ".join(party_line(p) for p in e270["parties"])
        w(f"Inquiry parties: {who}.")
        if e270.get("dmg"):
            w(f"Subject DOB {C.date(e270['dmg']['dob'])}, sex {e270['dmg']['gender']}.")
    if e271:
        w("")
        w("Response:")
        for eb in e271["eb"]:
            desc = C.look(C.EB01, eb["info"])
            svc = C.look(C.EB03, eb["service"]) if eb["service"] else ""
            plan = f", plan: {eb['plan_desc']}" if eb.get("plan_desc") else ""
            covq = f", coverage level {eb['coverage']}" if eb.get("coverage") else ""
            ins = f", insurance type {eb['plan']}" if eb.get("plan") else ""
            w(f"- benefit: {desc}{covq}" + (f", service type {svc}" if svc else "") + ins + plan)
        for d in e271["dates"]:
            w(f"- {C.dq(d['qual'])}: {C.date(d['value'])}")
        for m in e271["msgs"]:
            w(f"- payer message: {m}")
        others = [p for p in e271["parties"]]
        if others:
            w("Response parties: " + "; ".join(party_line(p) for p in others) + ".")
        if e271.get("dmg"):
            w(f"Subject DOB {C.date(e271['dmg']['dob'])}, sex {e271['dmg']['gender']}.")
        b = bht_line(e271["bht"], "Eligibility exchange")
        if b:
            w(b)

    w("")
    w("## Clearinghouse acknowledgment (277CA)")
    if e277:
        for st in e277["stc"]:
            cat = C.look(C.STC_STATUS, st["category"])
            code = C.look(C.CLAIM_STATUS_CODE, st["status"])
            w(f"Status {cat}, claim status code {code}, date {C.date(st['date'])}, "
              f"action code {st['action']}, amount {money(st['amount'])}.")
        for q, v in e277["refs"]:
            w(f"{C.idq(q)}: {v}.")
        for t in e277["trn"]:
            w(f"Trace ({C.look(C.TRN_TYPE, t['type'])}): {t['ref']}.")
        for d in e277["dates"]:
            w(f"{C.dq(d['qual'])}: {C.date(d['value'])}.")
        for q, v in e277["amt"]:
            w(f"Amount {q}: {money(v)}.")
        for q, v in e277["qty"]:
            w(f"Quantity {q}: {v}.")
        who = "; ".join(party_line(p) for p in e277["parties"])
        w(f"Parties: {who}.")
        b = bht_line(e277["bht"], "Acknowledgment")
        if b:
            w(b)
    else:
        w("No 277CA acknowledgment is present for this case.")

    w("")
    w("## Chart note (verbatim)")
    w("")
    w(case["chart_note"] or "No chart note present.")

    w("")
    w("## Transmission envelopes (control data)")
    order = [("270", "eligibility_270"), ("271", "eligibility_271"), ("837", "claim_837p"),
             ("277", "ack_277ca"), ("835", "remit_835")]
    for key, label in order:
        blob = case["files"].get(key)
        if not blob:
            continue
        env = blob["env"]
        isa = env.get("isa", {})
        gs = env.get("gs", {})
        st = env.get("st", {})
        se = env.get("se", {})
        w(f"- {label}: sender [{isa.get('sender_qual', '')}] {isa.get('sender', '')} to "
          f"receiver [{isa.get('receiver_qual', '')}] {isa.get('receiver', '')}, "
          f"interchange {isa.get('control', '')} date {isa.get('date', '')} time {isa.get('time', '')} "
          f"version {isa.get('version', '')} usage {isa.get('usage', '')}; "
          f"group {gs.get('func', '')} control {gs.get('control', '')} date {gs.get('date', '')} "
          f"time {gs.get('time', '')} spec {gs.get('version', '')}; "
          f"transaction {st.get('type', '')} control {st.get('control', '')}"
          + (f" impl {st.get('impl', '')}" if st.get("impl") else "")
          + f"; segments {se.get('count', '')}")

    if case["unmapped"]:
        w("")
        w("## Unmapped segments (raw)")
        for src, raw in case["unmapped"]:
            w(f"- {src}: `{raw}`")

    return "\n".join(out) + "\n"
