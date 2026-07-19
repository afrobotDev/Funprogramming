from main import *

run_cases = [
    ("add 3", lambda x: x + 3, 4, 10),
    ("double", lambda x: x * 2, 5, 20),
]

submit_cases = run_cases + [
    ("subtract 1", lambda x: x - 1, 10, 8),
    ("times 3", lambda x: x * 3, 2, 18),
    ("add 10", lambda x: x + 10, 0, 20),
]


def test(label, operation, value, expected_output):
    print("---------------------------------")
    print(f"Operation: {label}")
    print(f"Start value: {value}")
    print("")
    result = run_twice(operation, value)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

