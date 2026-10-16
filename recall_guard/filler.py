"""Deterministic, licence-free filler text. Combinatorial sentences about neutral office logistics; no digits,
so a planted numeric value can never collide with the filler."""

import random

SUBJECTS = (
    "The maintenance team", "The regional office", "A visiting auditor", "The night supervisor",
    "The procurement group", "Our logistics partner", "The facilities manager", "The planning committee",
    "A junior analyst", "The records clerk", "The warehouse crew", "The training coordinator",
    "The security desk", "The front office", "The catering vendor", "The fleet dispatcher",
    "The quality inspector", "The payroll office", "The site engineer", "The communications lead",
    "The archive staff", "The reception team", "The safety officer", "The building owner",
    "The cleaning contractor", "The transport desk", "The harbour office", "The regional council",
    "The events team", "The legal department", "The print room", "The mail room",
)
PREDICATES = (
    "reviewed the quarterly schedule", "postponed the inventory count", "approved the revised floor plan",
    "requested additional shelving", "circulated the updated parking rules", "archived the older correspondence",
    "rescheduled the fire drill", "confirmed the delivery window", "audited the cleaning rota",
    "replaced the corridor lighting", "drafted a note on visitor badges", "reserved the larger meeting room",
    "catalogued the returned equipment", "reported a leak in the stairwell", "renewed the coffee contract",
    "adjusted the heating timetable", "collected the signed attendance sheets", "inspected the loading bay",
    "summarised the supplier feedback", "relabelled the storage crates", "tested the backup generator",
    "updated the evacuation map", "ordered replacement chairs", "logged the courier arrivals",
    "closed the east entrance for repairs", "briefed the new volunteers", "compared two shelving quotes",
    "filed the insurance paperwork", "measured the mezzanine clearance", "repainted the loading ramp",
    "verified the badge reader", "moved the recycling bins",
)
TAILS = (
    "before the regional meeting.", "without further comment.", "ahead of the winter break.",
    "as the handbook recommends.", "after a short discussion.", "despite the earlier delay.",
    "once the paperwork cleared.", "to the satisfaction of the board.", "while the lifts were serviced.",
    "pending a final signature.", "in line with last year's practice.", "at the request of the tenants.",
    "with help from the contractor.", "following the usual checklist.", "for the second time this season.",
    "under the new procedure.", "because the forecast changed.", "so the ramp could be cleared.",
    "though nobody objected.", "and noted it in the log.", "during the morning shift.",
    "after the budget review.", "to free up the side corridor.", "on the advice of the engineer.",
    "as agreed in the spring.", "with minor adjustments.", "in time for the open day.",
    "before the auditors arrived.", "given the recent complaints.", "until the parts arrive.",
    "across both buildings.", "with the usual exceptions.",
)


def filler_sentence(rng: random.Random) -> str:
    """One sentence drawn from the combinatorial bank (32^3 = 32768 distinct sentences)."""
    return f"{rng.choice(SUBJECTS)} {rng.choice(PREDICATES)} {rng.choice(TAILS)}"


def filler_sentences(n: int, seed: int) -> tuple[str, ...]:
    """`n` filler sentences, byte-identical for the same `(n, seed)`."""
    rng = random.Random(seed)
    return tuple(filler_sentence(rng) for _ in range(n))
