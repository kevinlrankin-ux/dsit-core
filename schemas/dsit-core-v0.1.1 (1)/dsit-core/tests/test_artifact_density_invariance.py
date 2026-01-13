from src.traffic_light_mapper import map_traffic_light, Thresholds

def test_artifact_density_does_not_force_outcome():
    """Governance invariant: artifact density may change uncertainty/quality, not outcome authority."""
    t = Thresholds()
    risk = 0.42  # mid-range, should remain Yellow regardless of artifact density

    low_q = 0.38   # sparse artifacts -> lower quality
    high_q = 0.72  # richer artifacts -> higher quality

    light_low = map_traffic_light(risk, low_q, t)
    light_high = map_traffic_light(risk, high_q, t)

    assert low_q != high_q
    assert light_low == light_high, (
        "Artifact density improperly altered traffic-light outcome (threshold coupling detected)."
    )
