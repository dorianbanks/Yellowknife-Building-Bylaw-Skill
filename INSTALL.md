# Install

Detailed install instructions for the Yellowknife Building By-law Claude
Skill. For a quick overview, see [README.md](README.md#install).

---

## Prerequisites

- **Claude Code** or **Claude.ai** with skills enabled.
- **Python 3.8+** on your `PATH` (only needed if you plan to run
  `scripts/lookup.py` directly — Claude runs it for you inside the
  skill).

---

## Option 1 — Personal install (Claude Code)

```bash
git clone https://github.com/dorianbanks/Yellowknife-Building-Bylaw-Skill.git
cd Yellowknife-Building-Bylaw-Skill
mkdir -p ~/.claude/skills
cp -R ykbb ~/.claude/skills/ykbb
```

Restart Claude Code. Ask a Yellowknife permit question — the skill
should auto-trigger. Run `/plugin list` and look for `ykbb`.

### Updating

```bash
cd Yellowknife-Building-Bylaw-Skill
git pull
cp -R ykbb ~/.claude/skills/ykbb
```

---

## Option 2 — Project-scoped install

From your project root:

```bash
mkdir -p .claude/skills
git clone https://github.com/dorianbanks/Yellowknife-Building-Bylaw-Skill.git /tmp/ykbb-src
cp -R /tmp/ykbb-src/ykbb .claude/skills/ykbb
rm -rf /tmp/ykbb-src
```

Commit `.claude/skills/ykbb` (or add to `.gitignore` if you prefer
everyone install it themselves). Claude Code picks it up automatically
when started in that directory.

---

## Option 3 — Organization-wide upload (Claude Team / Enterprise)

If your Claude plan has **Organization Settings → Add Skill** on
[claude.ai](https://claude.ai):

```bash
git clone https://github.com/dorianbanks/Yellowknife-Building-Bylaw-Skill.git
cd Yellowknife-Building-Bylaw-Skill/ykbb
zip -r ../ykbb.zip .
cd ..
```

Then upload `ykbb.zip` via **Settings → Organization → Skills → Add
Skill**.

> **Size note:** the bundled by-law PDF is only ~1.5 MB, so the zip
> stays well under 2 MB — comfortable for any upload UI.

---

## Verifying the install

Open Claude Code (or claude.ai) and ask:

```
Quote §29 of Yellowknife Building By-law 5058.
```

You should see Claude:

1. Acknowledge the `ykbb` skill.
2. Resolve the section with `lookup.py` (→ PDF p. 14).
3. Read the PDF at the resolved page.
4. Quote the applicant-responsibilities provision with a *(PDF p. N)*
   citation.
5. Close with a City of Yellowknife Building Services Division
   disclaimer.

If you get a generic answer with no PDF reference, the skill did not
load — confirm `~/.claude/skills/ykbb/SKILL.md` exists and restart
Claude Code.

---

## Uninstall

```bash
rm -rf ~/.claude/skills/ykbb        # personal install
rm -rf .claude/skills/ykbb          # project install
```

For org-uploaded skills, remove via the same claude.ai admin UI used
to install.

---

## If you had the old `nwtbc` skill installed

This repository replaces the prior
`Northwest-Territories-Building-Code-Skill` / `nwtbc` skill, which was
anchored on the GNWT *Good Building Practice for Northern Facilities*
(a design guide, not enforceable code). The new skill (`ykbb`) is
anchored on the City of Yellowknife Building By-law No. 5058 —
enforceable municipal law for Yellowknife projects.

To swap:

```bash
rm -rf ~/.claude/skills/nwtbc
cp -R ykbb ~/.claude/skills/ykbb
```

Restart Claude Code.
