# One-Click GitHub Release Bundle — Step-by-Step

This folder is already a publishable repo. Use it to create a GitHub release quickly.

## A) Create a GitHub repo (web UI)
1. In GitHub, click **New repository**
2. Name: `dsit-core` (or your preferred name)
3. Choose **Public** (or Private if desired)
4. Click **Create repository**

## B) Upload this bundle (fastest path)
Option 1: GitHub web upload
1. Open the new repo in your browser
2. Click **Add file → Upload files**
3. Drag/drop the *contents* of this folder (not the zip) into the upload area
4. Commit message: `Initial DSIT core bundle (v0.1.0)`
5. Click **Commit changes**

Option 2: Git CLI (preferred for repeatability)
```bash
git init
git add .
git commit -m "Initial DSIT core bundle (v0.1.0)"
git branch -M main
git remote add origin <YOUR_REPO_URL>
git push -u origin main
```

## C) Create the release tag (GitHub UI “one-click”)
1. Go to your repo → **Releases**
2. Click **Draft a new release**
3. Tag: `v0.1.0`
4. Target: `main`
5. Release title: `DSIT Core v0.1.0`
6. Description (paste):
   - Signal Schema v1.0
   - Deterministic traffic-light mapping reference
   - CCBP runtime prompt + explanation templates
   - Example signal-bus input
7. Click **Publish release**

## D) Attach the zip (optional)
1. On the release page, click **Edit**
2. Drag/drop the `dsit-core-v0.1.0.zip` asset (if you created one locally)
3. Save

## E) Quick sanity check
```bash
python -m src.traffic_light_mapper --input examples/sample_signal_bus.json
```
Expected: `traffic_light` should map consistently with the thresholds.
