"""EPI 15.4: Generate the power set — printed page 224.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Generate the power set
Algorithm: Double the existing family with subsets that additionally include the next item.
Read the corresponding `pg_224_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_15_recursion.pg_224_generate_power_set
Test: python -m pytest tests/chapter_15_recursion/test_pg_224_generate_power_set.py -v
"""

def generate_power_set(values: list[int]) -> list[list[int]]:
    """Enumerate every subset; input indices select independent membership."""
    subsets=[[]]
    for value in values:
        subsets += [subset + [value] for subset in subsets]
    return subsets


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = generate_power_set([])
    print("generate_power_set:", observed)
    assert observed == [[]]
    observed = generate_power_set([1])
    print("generate_power_set:", observed)
    assert observed == [[], [1]]
    observed = generate_power_set([1, 2])
    print("generate_power_set:", observed)
    assert observed == [[], [1], [2], [1, 2]]
