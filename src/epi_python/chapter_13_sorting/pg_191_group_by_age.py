"""EPI 13.8, printed page 191: Partitioning and sorting an array with many repeated entries.

Problem: Partitioning and sorting an array with many repeated entries. See pg_191_exercise_13_08_partitioning_and_sorting_an_array_with_many_repeated_entries.md for the full
original problem, hint, development, and variants from the PDF text layer.

Approach and complexity: O(n) expected time and O(d) dictionary space for d distinct ages.

EDUCATIONAL RECONSTRUCTION: source and comments are not claimed verbatim.
Run directly: python -m epi_python.chapter_13_sorting.pg_191_group_by_age
Test: python -m pytest tests/chapter_13_sorting/test_pg_191_group_by_age.py -v
"""

# TEXTBOOK PROBLEM (exercise 13.8, printed page 191):
# Reorder records so entries with the same key occupy contiguous positions.
# HINT: Track key ranges as items are swapped into groups.

# dataclass generates a lightweight record with named attributes.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class Person:
    age: int
    name: str


def group_by_age(people: list[Person]) -> None:
    """Rearrange people in place so members of the same age are contiguous."""
    age_to_count = {}
    for person in people:
        age_to_count[person.age] = age_to_count.get(person.age, 0) + 1
    age_to_offset = {}
    offset = 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count
    while age_to_offset:
        from_age = next(iter(age_to_offset))
        from_index = age_to_offset[from_age]
        person_age = people[from_index].age
        destination = age_to_offset[person_age]
        people[from_index], people[destination] = people[destination], people[from_index]
        age_to_count[person_age] -= 1
        if age_to_count[person_age] == 0:
            del age_to_offset[person_age]
        else:
            age_to_offset[person_age] += 1


if __name__ == '__main__':
    people = [Person(13,'A'),Person(14,'B'),Person(13,'C'),Person(12,'D')]
    group_by_age(people)
    print('Grouped ages:', [p.age for p in people])
    assert {p.name for p in people} == {'A','B','C','D'}
    assert [p.age for p in people] == [13, 13, 14, 12] or [p.age for p in people] == [13, 13, 12, 14] or [p.age for p in people] == [12, 13, 13, 14] or [p.age for p in people] == [12, 14, 13, 13] or [p.age for p in people] == [14, 13, 13, 12] or [p.age for p in people] == [14, 12, 13, 13]
