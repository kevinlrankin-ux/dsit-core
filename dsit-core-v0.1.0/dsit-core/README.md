# DSIT Core (Deepfake Signal Integrity Toolkit)

DSIT is a **signal-first** media integrity assessment toolkit for **images, audio, and video**.  
It produces **probabilistic indicators** (e.g., *Green / Yellow / Red*) and a structured **evidence bundle**.

## What this repo contains (core)
- **Signal Schema v1.0** (machine-readable contract)
- **Traffic-light mapping reference** (deterministic rules)
- **Explanation templates** (human-readable, non-judgmental)
- **CCBP-governed ChatGPT runtime prompt** (explanation + governance layer)

## What DSIT is (and is not)
- ✅ A **triage indicator** + **signal space** for investigative review  
- ❌ Not a ground-truth authenticity oracle  
- ❌ Not a “verdict engine”

## Quick start (local)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
python -m src.traffic_light_mapper --input examples/sample_signal_bus.json
```

## Repo layout
- `schemas/` — JSON contracts (Signal Schema v1.0)
- `src/` — reference implementations (deterministic mapping)
- `runtime/` — CCBP runtime prompt + explanation templates
- `docs/` — whitepaper + governance notes
- `examples/` — sample inputs/outputs

## License
See `LICENSE` and `docs/IP_PARTICIPATION_ADDENDUM.md`.
