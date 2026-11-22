# Where the corpus and the guardrail disagree, and which one wins

The brief says two things that, on a specific set of cases, cannot both hold:

> Never guess facts it does not have.

> CARC/RARC meanings come from `reference/runtime/*.md`, cited by filename,
> never recalled from memory.

and

> Scorer accuracy >= 85% on the full labeled dev slice.

On the `ncci_ptp_no59` family the labels want an answer the reference material
says cannot be given. This note records the conflict, the evidence on each
side, and the choice — because silently resolving it in favour of the score is
exactly the failure the guardrails exist to prevent.

## What the reference says

`reference/runtime/07-ncci-and-mue.md`, quoting the primary sources it cites
(`ncci-ptp-carc-236.md` §5 and §8 rows 3–4, itself from CMS Transmittal 4188 /
CR 10852 and Pub 100-04 ch.23 §20.9):

> **Read the line:** the 236 line is the **Column Two** code, definitionally;
> Column One is payable. […] The 835 carries **neither the partner code nor
> the CCMI**; look the pair up in the PTP edit file for the **DOS quarter**,
> else `awaiting_human` — **do not guess**.

And the disposition rule:

> **Disposition:** `correct_and_resubmit` only when **CCMI = 1** *and* the
> record documents a separate encounter, anatomic site, or specimen.

CCMI — the Column One/Column Two Modifier Indicator — is the value that decides
whether a bypass modifier is even permitted. `0` means no modifier can ever
bypass the edit (`do_not_resubmit`). `1` means one can, if the documentation
supports it (`correct_and_resubmit`). `9` means the edit does not apply
(`appeal`). **All three dispositions are live, and the indicator that selects
between them is not in any artifact the system is given.** It lives in the
quarterly CMS PTP edit file, which is not part of the case.

## What the labels want

Every `ncci_ptp_no59` case in the corpus is labeled `correct_and_resubmit` —
i.e. CCMI = 1 in every instance.

## What the system did

It parked, with questions of this shape:

> What is the NCCI PTP Column One/Column Two Modifier Indicator for this code
> pair in the DOS quarter's edit file, and does the record document a separate
> encounter or anatomic site?

That is the correct question, asked of the right source, for the right reason.
It is the behaviour the reference card prescribes in the sentence quoted above.

## The choice

**The guardrail wins.** The prompt now names CCMI explicitly as the standing
example of a park that must not be talked out of.

The alternative was to teach the system that a `CO-236` denial means
`correct_and_resubmit`. That would score better on this corpus and be wrong in
the field: it would confidently instruct a biller to append a bypass modifier
to a pair whose CCMI is `0`, where no modifier is permitted and the resubmission
draws a second denial — or, on a CCMI `9` pair, it would resubmit where the
correct move is to appeal the edit's applicability. The corpus happens to
contain only CCMI-1 pairs. A system tuned to that fact has learned the corpus,
not the domain.

## What it costs

Measured on the 71-case pre-fix baseline: 7 `ncci_ptp_no59` cases, 2 correct,
5 lost — 4 to parking and 1 to a wrong path. On the full 140-case slice the
family is 14 cases, so the ceiling this imposes is **about 10 percentage
points** of joint accuracy.

That is a large price and it is worth being explicit that it is being paid
deliberately. It is also the single biggest known gap between the reported
accuracy and what the system could score if it were allowed to guess.

## What would actually fix it

Not a prompt change. The PTP edit file for the DOS quarter is a published CMS
artifact; loading the relevant quarters and letting the system look the pair up
would turn every one of these parks into a determinate answer, correctly
derived rather than assumed. That is a data-ingestion task, out of scope here,
and it is the right fix.

Until then the honest reading of the `ncci_ptp_no59` column is not "the system
got these wrong" but "the system was not given what these require, and said
so."
