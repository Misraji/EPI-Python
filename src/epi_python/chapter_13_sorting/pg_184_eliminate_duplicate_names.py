"""EPI 13.3, printed page 184: Remove first-name duplicates.

Problem: Remove first-name duplicates. See pg_184_exercise_13_03_remove_first_name_duplicates.md for the full
original problem, hint, development, and variants from the PDF text layer.

Approach and complexity: O(n log n) time for sorting, then O(n) compaction; sorting in-place.

EDUCATIONAL RECONSTRUCTION: source and comments are not claimed verbatim.
Run directly: python -m epi_python.chapter_13_sorting.pg_184_eliminate_duplicate_names
Test: python -m pytest tests/chapter_13_sorting/test_pg_184_eliminate_duplicate_names.py -v
"""

# TEXTBOOK PROBLEM (exercise 13.3, printed page 184):
# Remove duplicate first names from records consisting of first and last names.
# HINT: Bring equal items close together.

# dataclass supplies a constructor and printable field representation.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class Name:
    first_name: str
    last_name: str


def eliminate_duplicate(names: list[Name]) -> None:
    """Retain one name per first name, sorted, updating the original list."""
    # list.sort sorts in place and key selects which fields determine order.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#list.sort
    names.sort(key=lambda name: (name.first_name, name.last_name))
    if not names:
        return
    write = 1
    for candidate in names[1:]:
        if candidate.first_name != names[write - 1].first_name:
            names[write] = candidate
            write += 1
    del names[write:]


if __name__ == "__main__":
    people = [Name("Ian", "Botham"), Name("David", "Gower"), Name("Ian", "Bell")]
    eliminate_duplicate(people)
    print("Distinct first names:", people)
    assert [p.first_name for p in people] == ["David", "Ian"]
