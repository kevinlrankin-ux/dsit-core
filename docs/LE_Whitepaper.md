# Deepfake Signal Integrity Toolkit (DSIT) — Law Enforcement Brief (Public)

## Executive Summary
DSIT is a signal-first media integrity assessment toolkit for images, audio, and video. It produces probabilistic
indicators (Green/Yellow/Red) and a structured evidence bundle. DSIT is not a ground-truth authenticity oracle.

## Core Design
1) Acquisition & extraction (lawful retrieval; hashing; metadata capture)
2) Local detectors (measurement only)
3) Signal normalization (schema-stable outputs)
4) CCBP runtime mapping/explanation (bounded, non-directive)

## Output
- Traffic light indicator
- Risk score (0..1) + Quality score (0..1)
- Top signals (with false-positive caveats)
- Provenance status
- Limits statement

## Limitations
- No guarantee of authenticity or falsity
- Compression/noise can reduce detection power
- Novel generators may evade some detectors

## Auditability
- Input hashing
- Version-pinned detectors
- Deterministic mapping rules
