import json
from pathlib import Path

import jsonschema


def test_example_signal_bus_conforms_to_schema():
    root = Path(__file__).resolve().parents[1]
    schema_path = root / "schemas" / "signal-schema-v1.0.schema.json"
    example_path = root / "examples" / "sample_signal_bus.json"

    assert schema_path.exists(), f"Missing schema: {schema_path}"
    assert example_path.exists(), f"Missing example: {example_path}"

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    instance = json.loads(example_path.read_text(encoding="utf-8"))

    # Draft 2020-12 compatible validator selection
    jsonschema.validate(instance=instance, schema=schema)
