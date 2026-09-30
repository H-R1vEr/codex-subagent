#!/usr/bin/env python3
"""Synthetic arithmetic fixture, not scientific GMM validation."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def compute(source: Path) -> dict[str, float]:
    values = {}
    with source.open(encoding='utf-8', newline='') as stream:
        for row in csv.DictReader(stream):
            key = row['record_id']
            if not key or key in values:
                raise ValueError('Missing or duplicate record ID')
            observed, predicted = float(row['observed_g']), float(row['predicted_g'])
            if not all(math.isfinite(x) and x > 0 for x in (observed, predicted)):
                raise ValueError(f'Nonpositive/nonfinite ground motion: {key}')
            values[key] = math.log(observed) - math.log(predicted)
    if not values:
        raise ValueError('No records')
    return values

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    source = ROOT / 'examples/synthetic-residuals/records.csv'
    expected = json.loads((source.parent / 'expected.json').read_text())['residuals']
    result = compute(source)
    if result.keys() != expected.keys() or not all(
            math.isclose(result[k], expected[k], rel_tol=0, abs_tol=1e-12) for k in expected):
        raise ValueError('Fixture comparison failed')
    payload = {'kind': 'synthetic_fixture', 'status': 'PASS_ARITHMETIC_ONLY',
               'log_base': 'natural', 'unit': 'g', 'record_count': len(result),
               'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
               'absolute_tolerance': 1e-12, 'residuals': result}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8') as stream:
        json.dump(payload, stream, indent=2)
        stream.write('\n')
    print(f'Synthetic arithmetic passed; wrote {args.output}')

if __name__ == '__main__':
    main()
