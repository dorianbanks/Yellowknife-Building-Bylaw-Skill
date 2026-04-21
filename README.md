# City of Yellowknife Building By-law (No. 5058) — Claude Skill

A [Claude Skill](https://code.claude.com/docs/en/skills) that turns Claude
into a practitioner-grade reference for the **City of Yellowknife Building
By-law No. 5058** — the enforceable municipal building law inside City of
Yellowknife limits, Northwest Territories, adopted by Council on
**May 30, 2022**. It bundles the full 39-page by-law PDF, a page-numbered
citation index, and workflow guides for the decisions that actually come
up on Yellowknife permit work.

**Scope note — Yellowknife only.** This by-law applies *only inside City
of Yellowknife municipal limits*. It is enacted by Yellowknife's Council
under the NWT *Cities, Towns and Villages Act* (S.N.W.T. 2003, c.22,
ss. 70–75). Other NWT communities have their own bylaws (or none — with
MACA or the NWT Office of the Fire Marshal as AHJ on Commissioner's Land).
This skill does not cover those.

---

## What it does

Ask Claude a Yellowknife building-permit question in plain English or by
citation, and the skill will:

1. **Route** the question to the right workflow guide — permits /
   responsibilities / orders / fees / Part 2 construction / energy /
   foundations & retaining walls.
2. **Resolve** any section or schedule you name (e.g. `§29`, `§64(4)`,
   `Schedule B`) to a PDF page via the bundled `lookup.py` script.
3. **Read the authoritative text** from the bundled by-law PDF.
4. **Quote and cite** in the standard form: *City of Yellowknife
   Building By-law No. 5058, §29(1)(b) (PDF p. 14)*.
5. **Flag the NBC/NECB layer** — By-law §4 adopts **NBC 2020 in
   entirety** and §5 adopts **NECB 2020 in entirety**. Technical
   national-code questions are redirected to the `canbc` and `canec`
   companion skills.
6. **Close with the AHJ disclaimer.** Always. Binding determinations
   belong to the **City of Yellowknife Building Services Division**,
   not to Claude.

### Triggers on things like

- *"Is a sprinkler required in a three-unit rowhouse in Yellowknife?"*
- *"Can I build a Part 9 house foundation pinned to bedrock without an
  engineer?"*
- *"What R-value do I need for above-grade walls on a Part 9 house?"*
- *"What's the permit expiry period?"*
- *"Received a Stop-Work order — how do I request Council review?"*
- *"Does the 600 mm retaining wall need a permit?"*
- *"Quote §29."*

---

## Why this exists

Yellowknife is the only NWT municipality with a full modern building
by-law that goes beyond the National Building Code — with specific
Yellowknife deltas on foundations (pinned-to-bedrock paths,
Schedule B piers), sprinklers (MFD ≥ 3 units to NFPA 13), hydrants,
energy efficiency (exceeds NBC 9.36 defaults), and retaining walls
(Schedule E). Architects working on Yellowknife projects need these
at their fingertips; the standard BCBC / NBC references don't cover
any of it.

---

## Install

### Personal use (single machine)

1. Clone this repository.
2. Copy the `ykbb/` folder into your Claude skills directory:

   ```bash
   cp -R ykbb ~/.claude/skills/ykbb
   ```

3. Restart Claude Code. Run `/plugin list` and look for `ykbb`.

### Team / studio use

Every team member clones the repo and copies the `ykbb/` folder into
`~/.claude/skills/ykbb`. Pull to update. For Claude Team/Enterprise
plans with **Organization Settings → Add Skill**, zip the `ykbb/`
folder and upload:

```bash
cd ykbb && zip -r ../ykbb.zip . && cd ..
```

See [INSTALL.md](INSTALL.md) for project-scoped installs and other
details. The bundled PDF is only ~1.5 MB, so the zip is well under
any typical upload cap.

---

## How to use it

Once installed, just ask — the skill auto-triggers on Yellowknife /
Northwest Territories building-permit questions.

```
> Stop-Work order just arrived for a Yellowknife site — what's my
  review window?

> Is a sprinkler required in a four-unit walk-up in Yellowknife?

> Can I build a Part 9 house foundation pinned to bedrock without an
  engineer?

> Prescriptive R-value for above-grade walls, Part 9 residential.

> Quote §64(4).

> Summarize Schedule D (Part 3 residential energy).
```

---

## What's in the skill

```
ykbb/
├── SKILL.md                         # skill definition + operating instructions
├── assets/
│   └── yk_bylaw_5058_2022.pdf       # 39-page by-law PDF
├── references/
│   ├── index.md                     # section/schedule outline with PDF pages
│   ├── index.json                   # machine-readable outline
│   ├── citations.json               # citation → page lookup (§N, Schedule X)
│   ├── map.md                       # structural map + quick-pick decision tree
│   ├── definitions.md               # §3 defined-term index
│   ├── permits-and-occupancy.md     # workflow: §§17–24 permits, exemptions, OC
│   ├── responsibilities.md          # workflow: §§29–35 applicant / RDP / inspector
│   ├── orders-and-enforcement.md    # workflow: §§36–46 orders / offences
│   ├── fees-and-penalties.md        # workflow: §§45–51 + Schedule A fines
│   ├── part2-local-construction.md  # workflow: §§53–70 Yellowknife construction deltas
│   ├── energy-efficiency.md         # workflow: §64 + Schedules C (P9 res) & D (P3 res)
│   └── foundations-retaining.md     # workflow: §§54–58 + Schedule B + Schedule E
├── scripts/
│   └── lookup.py                    # citation → page resolver + keyword search
└── evals/
    └── evals.json                   # evaluation test suite
```

---

## Relationship to the National Codes

By-law §4 adopts **NBC 2020 in entirety**. §5 adopts **NECB 2020 in
entirety**. §15 establishes **paramountcy** — the by-law prevails over
the NBC only *to the extent it exceeds the NBC*. Practical meaning:

| Question type | Source of truth |
|---|---|
| Permit process / inspections / orders / fees | **This skill** |
| Yellowknife-specific deltas (Part 2 of the by-law) | **This skill** |
| NBC technical content (occupancy, exits, fire separations, etc.) | **NBC 2020** — see the [National-Building-Code-of-Canada-Skill](https://github.com/dorianbanks/National-Building-Code-of-Canada-Skill) |
| NECB technical content (Part 3 non-residential energy) | **NECB 2020** — see the [National-Energy-Code-of-Canada-Skill](https://github.com/dorianbanks/National-Energy-Code-of-Canada-Skill) |

---

## Key Yellowknife deltas (what architects miss most often)

- **MFD sprinkler threshold is 3 units** (§61) — tighter than the
  generic NBC threshold. NFPA 13 required, not 13R/13D.
- **Part 9 residential prescriptive RSI values exceed NBC 9.36**
  (§64(4), Table 1). Above-grade walls **RSI 5.28 (R-30)**; FDWR 15%.
- **Pinned-to-bedrock foundations have a no-RDP prescriptive path**
  (§§54, 56 + Schedule B) — for Part 9 only, within spec.
- **Retaining walls 600–1200 mm** require drawings per Schedule E;
  anything above 1200 mm OR supporting a structure needs an
  RDP-stamped design.
- **RDP means NAPEG engineer or NWTAA architect in good standing** —
  not a BC/Alberta professional. Out-of-territory firms need NWTAA
  temporary/occasional licensure before stamping.
- **Permit expires at 2 years** (§22(6)); abandoned after 180 idle
  days (§23(7)).
- **Summary Conviction maxes**: $2,000 individual / $10,000
  corporation / 6 months imprisonment (§45). Continuing offences are
  per-day (§46(4)).

---

## Scope & limits

- **Yellowknife municipal limits only.** Don't extrapolate to Inuvik,
  Hay River, Fort Smith, or unincorporated Commissioner's Land.
- **NBC technical content not reproduced.** §4 adopts it in entirety;
  this skill surfaces the administrative + local-delta layer only.
- **Not a code consultant.** Binding determinations belong to the
  City of Yellowknife Building Services Division.
- **Authoritative text wins.** Always verify by reading the cited
  PDF page before relying on an answer for a permit submission.

---

## Sister skills

Companion Claude Skills for related Canadian building-code jurisdictions:

- [National-Building-Code-of-Canada-Skill](https://github.com/dorianbanks/National-Building-Code-of-Canada-Skill) — NBC 2020, adopted in entirety by Yellowknife By-law §4. Use for technical NBC questions.
- [National-Energy-Code-of-Canada-Skill](https://github.com/dorianbanks/National-Energy-Code-of-Canada-Skill) — NECB 2020, adopted in entirety by Yellowknife By-law §5. Use for Part 3 non-residential energy framework.
- [Vancouver-Building-By-law-Skill](https://github.com/dorianbanks/Vancouver-Building-By-law-Skill) — parallel Canadian municipal by-law example (City of Vancouver, VBBL 2025).
- [British-Columbia-Building-Code-Skill](https://github.com/dorianbanks/British-Columbia-Building-Code-Skill) — BCBC 2024 for BC projects (different jurisdiction; closely tracks NBC like Yellowknife does).

---

## Credits

Built by **Dorian Banks**. Released under the MIT License — see
[LICENSE](LICENSE).

By-law No. 5058 is published by the **City of Yellowknife**. This
repository redistributes the 2022 by-law PDF for reference use inside
the skill; consult the official source at
[yellowknife.ca](https://www.yellowknife.ca/) for authoritative and
current versions, including any subsequent amendments.

---

## Disclaimer

This skill is a reference aid for licensed practitioners. It is not
legal advice, not a substitute for a code consultant, and not a
substitute for review by the City of Yellowknife Building Services
Division. Always verify against the official published by-law and
confirm with the City before relying on any output for a permit
submission or construction.
