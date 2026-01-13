\
from __future__ import annotations
import json
import argparse
from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass(frozen=True)
class Thresholds:
    green_lt: float = 0.35
    red_gte: float = 0.70
    quality_min_green: float = 0.35
    quality_min_any: float = 0.20
    red_override_if_low_quality: float = 0.85

def map_traffic_light(risk_score: Optional[float], quality_score: Optional[float], t: Thresholds = Thresholds()) -> str:
    # Unknown risk -> Yellow (insufficient artifacts)
    if risk_score is None:
        return "yellow"

    q = 0.0 if quality_score is None else float(quality_score)

    # Very low quality: avoid confident Green; allow Red only if overwhelming
    if q < t.quality_min_any and risk_score < t.red_override_if_low_quality:
        return "yellow"

    # Red condition
    if risk_score >= t.red_gte:
        return "red"

    # Green condition
    if (risk_score < t.green_lt) and (q >= t.quality_min_green):
        return "green"

    # Otherwise Yellow
    return "yellow"

def main():
    ap = argparse.ArgumentParser(description="DSIT deterministic traffic-light mapper (reference).")
    ap.add_argument("--input", required=True, help="Path to a DSIT signal-bus JSON file.")
    args = ap.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        obj: Dict[str, Any] = json.load(f)

    risk = obj.get("aggregation", {}).get("risk_score")
    q = obj.get("quality", {}).get("quality_score")

    light = map_traffic_light(risk, q)
    print(json.dumps({"risk_score": risk, "quality_score": q, "traffic_light": light, "version": "trafficlight-v0.1"}, indent=2))

if __name__ == "__main__":
    main()
