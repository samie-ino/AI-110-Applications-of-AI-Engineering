from agent import diagnose
from evaluator import verify

test_cases = [
    {"input": "op-amp output stuck high", "expected": "saturation"},
    {"input": "no current in circuit", "expected": "open"},
    {"input": "noisy signal", "expected": "noise"}
]

def run_tests():
    results = []
    passed = 0

    for case in test_cases:
        diagnosis = diagnose(case["input"])
        evaluation, confidence = verify(case["input"], diagnosis)

        success = case["expected"] in diagnosis.lower()

        if success:
            passed += 1

        results.append({
            "input": case["input"],
            "passed": success,
            "confidence": confidence
        })

    return results, passed, len(test_cases)
