import yaml
import subprocess

with open("evals/cases.yaml") as f:
    cases = yaml.safe_load(f)["cases"]

for case in cases:
    print("\nRunning:", case["question"])

    result = subprocess.getoutput(
        f'python -m portfolio_ask "{case["question"]}"'
    )

    passed = all(k.lower() in result.lower() for k in case["expected_keywords"])

    print("PASS" if passed else "FAIL")