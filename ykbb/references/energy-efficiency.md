# Energy Efficiency — Workflow (§64 + Schedules C & D)

Use this guide for any Yellowknife energy-compliance question. The
by-law routes energy compliance by **occupancy × Part** — each route
has its own prescriptive values and performance targets.

---

## Routing

| Building | Section | Route | Details |
|---|---|---|---|
| Part 9 residential | §64(1)–(5) | Prescriptive or Performance | Schedule C airtightness |
| Part 9 residential — factory-built **temporary worker accommodation** | §64(3) | Exempt under conditions | CSA-cert + meets minimum at date of construction |
| Part 9 non-residential | §64(6) | Comply with **NBC** | |
| Part 3 residential | §64(7) | **Schedule D** | |
| Part 3 non-residential | §64(8) | Comply with **NECB** | see `canec` skill |

---

## Part 9 Residential (§64(1)–(5), Table 1, Table 2 + Schedule C)

### §64(1) — compliance path

All NBC Part 9 residential buildings shall:

- comply with **Prescriptive Path** or **Performance Path**; and
- provide a **Residential-Building-Energy-Efficiency-Form**.

### §64(4) — Prescriptive Path (Table 1, p. 25)

Effective thermal resistance / transmittance values must be **not
less than** the values in Table 1:

| Assembly | Effective RSI [m²·K/W] | Effective R-value [ft²·°F/BTU] |
|---|---:|---:|
| Walls (above grade) | **5.28** | 30 |
| Walls (below grade) | 4.96 | 28 |
| Attic ceilings/roof | **10.6** | 60 |
| Cathedral ceilings/roof | 7.0 | 40 |
| Slab on ground | 5.64 | 32 |
| Exposed floor | 7.0 | 40 |
| Floors above unheated space | 6.28 | 36 |
| Insulation skirt extending out | 5.64 | 32 |

| Assembly | Effective USI [W/m²·K] | Effective U-value [BTU/ft²·°F] |
|---|---:|---:|
| Doors excluding glazing | 0.91 | 0.16 |
| Windows and glazed doors | 1.00 | 0.18 |

**FDWR (Fenestration and door-to-wall ratio) maximum — 15%.**

### §64(5) — Performance Path (Table 2, p. 25)

Buildings conforming to the performance path will be designed and
constructed to conform to Table 2:

| Metric | Target |
|---|---|
| **TEDI** | 105 kWh/(m²·a) |
| %<Ref (no 9.36.5 or ERS base loads) | **-25%** |

Performance Path implementation:

- Energy modelling **by the energy advisor**, as defined by Natural
  Resources Canada.
- Technical airtightness specifications in **Schedule C**.

### Schedule C — Energy NBC Part 9 Residential (p. 33)

Technical specifications for energy modelling and airtightness in a
Part 9 residential building.

- **(1)** Energy modelling via a computer program tested per
  **ANSI/ASHRAE 140**, "Evaluation of Building Energy Analysis
  Computer Programs". Modelling shall conform to NBC **Subsection
  9.36.5** or the **E.R.S.**
- **(2)** Airtightness tested **twice** — meeting targets:

  | Phase | Target | Smaller buildings (<1,200 ft²) |
  |---|---|---|
  | Mid-Construction | **3.0 ACH50** | 1.5 cm²/m² NLA |
  | Final post-construction | **1.5 ACH50** | 1.0 cm²/m² NLA |

  Testing per CAN/CGSB 149.10, ASTM E 779, or U.S.A.C.E. Version 3;
  and the applicable standards of the E.R.S.

- **(3)** All housing types (per E.R.S.) must have an **EnerGuide
  rating label** affixed visibly at time of final inspection.
- **(4)** **House performance compliance calculation report** — per
  Article **2.2.8.3 Division C of the NBC**, in a form prescribed by
  the Senior Administrative Officer.

---

## Part 9 non-residential (§64(6))

> Part 9 Non-Residential Buildings as defined in the N.B.C. shall
> comply with the N.B.C.

No Yellowknife overlay — defer to NBC 9.36 as applicable (or NBC Part
3 where the building falls under Part 3 by choice/exceedance).

---

## Part 3 Residential (§64(7) + Schedule D, pp. 34–36)

> Part 3 Residential Buildings as defined in the N.B.C. shall be
> designed to comply with **Schedule D** of this By-law.

### Schedule D opening (p. 34)

- **(1)** Ventilation per **ASHRAE 62.1-2001** (except addendum n),
  and constructed to conform to:
  - (a) The current version of the **NECB**, except that where NECB
    refers to the NBC, this By-law's provisions apply.
- **(2)** Comply with Prescriptive Path or Performance Path, and all
  other requirements.

### §D(3) — Prescriptive Path (Table 3, p. 34)

| Assembly | Effective RSI [m²·K/W] | Effective R-value [ft²·°F/BTU] |
|---|---:|---:|
| Walls (above grade) | **6.82** | 38 |
| Walls (below grade) | 5.95 | 34 |
| Ceilings/roof | **9.09** | 52 |
| Slab on ground | 3.30 | 18 |
| Exposed floor | 8.75 | 50 |
| Floors above unheated space | 8.55 | 49 |
| Perimeter insulation (1.0 m out) | 3.30 | 18 |

| Assembly | Effective USI [W/m²·K] | Effective U-value [BTU/ft²·°F] |
|---|---:|---:|
| Doors excluding glazing | 1.4 | 0.25 |
| Windows and glazed doors | 1.4 | 0.25 |

**FDWR maximum — 17%**.

### §D(4) — Performance Path (pp. 35–36)

Compliance path:

- (a) **Part 8 of the NECB** requirements;
- (b) **Operating air leakage rate** calculated from the assumed /
  measured rate using:

  `I_AGW = C × Q/S × S/A_AGW`

  where:
  - I_AGW = infiltration rate [L/s·m²] to be used for energy
    modelling, applied to the modelled above-ground wall area;
  - C = (5 Pa / 75 Pa)^n;
  - n = 0.60 (default flow exponent, if no whole-building test
    result);
  - Q = volume of air [L/s] flowing through the envelope at 75 Pa;
  - S = total surface area [m²] of the envelope (pressure boundary);
  - A_AGW = modelled above-ground wall area [m²] including windows;

- (c) Good energy modelling practice per ASHRAE Handbooks and
  Standards;
- (d) Until airtightness test results are available, use **1.50
  L/(s·m²) at 75 Pa**, converted to operating pressure via the
  formula above.

**Table 4 targets (p. 36):**

| Metric | Target |
|---|---:|
| **TEDI** | **120** kWh/(m²·a) |
| **TEUI** | **225** kWh/(m²·a) |

### §D(5) — Airtightness testing (p. 36)

- **(a)** Air barrier system shall have a normalized air leakage rate
  **≤ 1.50 L/(s·m²)** tested per:
  - ASTM E 3158 "Standard Test Method for Measuring the Air Leakage
    Rate of a Large or Multizone Building"; **or**
  - U.S.A.C.E. Version 3 "Air Leakage Test Protocol for Building
    Envelopes".

  At a pressure differential of 75 Pa, with building prepared per
  the envelope test protocol, tested for both pressurized and
  depressurized conditions, results averaged.

- **(b)** Where intentional openings for mechanical equipment are
  left unsealed, airtightness rate is adjusted in the energy model
  to account for air leakage through mechanical equipment.
- **(c)** Part 3 residential buildings shall be tested **twice** to
  meet the airtightness target; the first test occurs at
  **Mid-Construction**.

### §D(6) — Heat recovery

Buildings shall use **heat recovery systems** per NECB **Article
5.2.10 Division B**.

### §D(7) — Mechanical equipment efficiency

Mechanical systems per NECB **Article 5.2.12**. Components of
mechanical ventilation systems not specifically described in 5.2.12
per good engineering practice — ASHRAE Handbooks and Standards,
HRAI Digest, TECA Ventilation Guideline, Hydronics Institute
Manuals, or SMACNA manuals.

---

## Part 3 non-residential (§64(8))

> Part 3 Non-Residential Buildings as defined in the N.B.C. shall
> comply with the **N.E.C.B.**

No Yellowknife overlay — defer to NECB 2020 as adopted by §5 and
applied. See the `canec` skill for the authoritative NECB text.

---

## Temporary worker accommodation — §64(3)

Part 9 residential **factory-constructed** prefabricated buildings,
modules, and panels may be **exempt** from the Part 9 residential
energy rules if:

- (a) used as **temporary worker's accommodation**, as defined by the
  Zoning By-law; **and**
- (b) attached **legible CSA certification** or equivalent Canadian
  certification standard, illustrating the factory-constructed
  building / modules / panels were constructed to **meet the minimum
  standard at the date and jurisdiction of construction**.

This standard applies to prefabricated buildings of any occupancy
used as temporary worker accommodation.

---

## Drafting guidance

### For a new single-family home (Part 9 residential)

1. Confirm with owner — **Prescriptive or Performance** path.
2. If Prescriptive — design envelope to meet Table 1 effective RSI
   values; FDWR ≤ 15%.
3. If Performance — retain an NRCan-registered Energy Advisor, model
   to TEDI ≤ 105 kWh/(m²·a) and -25% vs reference, and plan for
   **two airtightness tests** (3.0 / 1.5 ACH50 mid/final — or
   1.5 / 1.0 NLA for <1,200 ft² buildings).
4. Affix EnerGuide label at final inspection.

### For a small apartment / Part 3 residential

1. Default to **Schedule D Prescriptive Path** (Table 3) unless
   fenestration or design drives Performance Path.
2. Ventilation to **ASHRAE 62.1-2001** (note: 2001 vintage, not
   current edition — Yellowknife intentionally anchors to this
   version).
3. If Performance — design to TEDI ≤ 120 / TEUI ≤ 225 kWh/(m²·a);
   plan for airtightness testing at Mid-Construction and final
   (1.50 L/(s·m²) at 75 Pa target).
4. **Heat recovery** is mandatory (per NECB 5.2.10).

### Common mistake

Using NBC 9.36 defaults without checking Table 1 — Yellowknife
Part 9 walls need RSI 5.28 (R-30) above grade; NBC 9.36 Zone 8
default is lower. §15 paramountcy says Yellowknife wins — so
always apply the tighter Yellowknife value.
