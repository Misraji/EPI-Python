"""EPI Python — Exercise 13.8: Partitioning and Sorting an Array with Many Repeated Entries

Chapter 13: Sorting
Textbook: pages 191–192 (printed page numbers; problem and solution start on 191).

PROBLEM (from the textbook)
---------------------------
"Suppose you need to reorder the elements of a very large array so that
equal elements appear together. For example, if the array is
<b,a,c,b,d,a,b,d> then <a,a,b,b,b,c,d,d> is an acceptable reordering, as is
<d,d,c,a,a,b,b,b>."

"If the entries are integers, this reordering can be achieved by sorting the
array. If the number of distinct integers is very small relative to the size
of the array, an efficient approach to sorting the array is to count the
number of occurrences of each distinct integer and write the appropriate
number of each integer, in sorted order, to the array. When array entries
are objects, with multiple fields, only one of which is to be used as a key,
the problem is harder to solve."

"You are given an array of student objects. Each student has an
integer-valued age field that is to be treated as a key. Rearrange the
elements of the array so that students of equal age appear together. The
order in which different ages appear is not important. How would your
solution change if ages have to appear in sorted order?"

HINT (from the textbook)
------------------------
"Count the number of students for each age."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: sort the array, comparing on age. For length n that is
O(n log n) time and O(1) space. It does more than required: the
specification only asks that students of equal age be adjacent.

Use the counting idea from the problem introduction. It cannot be applied
literally, because whole objects must be written, not integers: two
students may share an age yet be different students.

Worked example from the book: <(Greg,14),(John,12),(Andy,11),(Jim,13),
(Phil,12),(Bob,13),(Chip,13),(Tim,14)>.
- One pass records the count of each age in a hash table:
  (14,2), (12,2), (11,1), (13,3). So two students of age 14, two of 12, one
  of 11 and three of 13 must be written, in any order, with equal ages
  adjacent.
- With a NEW output array, the groups would start at these offsets: age 14
  at index 0, age 12 at 0 + 2 = 2, age 11 at 2 + 2 = 4, age 13 at 4 + 1 = 5.
  Iterating over the input and writing each entry at its age's next offset,
  after the first four iterations the new array would be
  <(Greg,14),_,(John,12),_,(Andy,11),(Jim,13),_,_>.
- That is O(n) time but needs O(n) additional space for the result array.

In-place version: keep, for each distinct age, a subarray marking the
entries not yet filled with elements of that age, and swap elements across
these subarrays to move each one to its correct position. The program uses
two hash tables to track the subarrays: one holds each subarray's starting
offset, the other its size. A subarray is removed as soon as it becomes
empty.

The function below follows the book's single (in-place) implementation.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    ages [13, 14, 13, 12] -> any arrangement with the two 13s adjacent,
    e.g. [13, 13, 14, 12].
"""

# Python standard library: automatic generation of special methods for
# simple record-like classes.
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` is a class decorator: from the annotated fields it generates
# `__init__` (so `Person(13, 'A')` works), a readable `__repr__`, and an
# all-field `__eq__`. The annotations `age: int`, `name: str` declare the
# field types but are not enforced.
@dataclass
class Person:
    age: int
    name: str


# Type hints: `people: list[Person]`, `-> None` (works by mutating the list).
def group_by_age(people: list[Person]) -> None:
    """Rearrange people in place so members of the same age are contiguous.

    This is the textbook's in-place implementation (two hash tables:
    age -> remaining count, age -> next free offset).
    """

    # First pass: count people of each age. dict.get(key, default) returns
    # the stored value, or `default` (0 here) when the key is absent, so the
    # first occurrence of an age starts its count at 1.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#dict.get
    age_to_count = {}
    for person in people:
        age_to_count[person.age] = age_to_count.get(person.age, 0) + 1

    # Assign each age a contiguous block: block start offsets are running
    # sums of the counts. dict.items() yields (key, value) pairs, unpacked
    # here into `age, count`. Dictionaries iterate in insertion order
    # (guaranteed since Python 3.7), i.e. order of first appearance.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#dict.items
    age_to_offset = {}
    offset = 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    # Loop until every age's block is completely filled (an empty dict is
    # falsy, so the loop stops when age_to_offset becomes empty).
    while age_to_offset:

        # iter(d) creates an iterator over the dict's keys, and next(...)
        # returns its first item: i.e. "any one age whose block is still
        # unfinished". This takes O(1) time.
        # Documentation: https://docs.python.org/3/library/functions.html#next
        from_age = next(iter(age_to_offset))

        # The first unfilled slot of that age's block, and the age of the
        # person currently sitting there.
        from_index = age_to_offset[from_age]
        person_age = people[from_index].age

        # That person belongs at the first unfilled slot of THEIR age's
        # block. Swap them there using simultaneous (tuple) assignment: the
        # right-hand side is evaluated fully before either assignment.
        destination = age_to_offset[person_age]
        people[from_index], people[destination] = people[destination], people[from_index]

        # One more person of `person_age` is now in place. When none remain,
        # `del` removes that age's entry, shrinking the dictionary; otherwise
        # advance its next free offset.
        age_to_count[person_age] -= 1
        if age_to_count[person_age] == 0:
            del age_to_offset[person_age]
        else:
            age_to_offset[person_age] += 1


# TEXTBOOK POST-SOLUTION DISCUSSION (page 192)
# --------------------------------------------
# Time O(n): the first pass does n hash-table inserts, and each step of the
# second pass spends O(1) time moving one element to its proper location.
# Additional space is dictated by the hash tables: O(m), where m is the
# number of distinct ages.
#
# If the ages must additionally appear in sorted order, use a BST-based map
# (Chapter 14) from ages to counts, since it keeps ages sorted. In the
# example the age-count pairs would then come out as (11,1), (12,2), (13,3),
# (14,2). The time becomes O(n + m log m), since each BST insertion is
# O(log m). Such a sort is often called a counting sort.
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `Person = collections.namedtuple('Person', ('age', 'name'))`.
#   File: `@dataclass class Person` with the same field order.
# - Book counts with `collections.Counter([person.age for person in
#   people])`; file uses a plain dict and `dict.get(..., 0) + 1`.
# - Book initialises `age_to_offset, offset = {}, 0` in one statement; file
#   uses two statements.
# - Book loop variables `from_idx`, `to_age`, `to_idx`; file uses
#   `from_index`, `person_age`, `destination`. Book updates the offset as
#   `age_to_offset[to_age] = to_idx + 1` when the count is still nonzero
#   (`if age_to_count[to_age]:`), else deletes; file tests `== 0` first and
#   uses `+= 1` otherwise. Book comment "Use age_to_count to see when we are
#   finished with a particular age." Type hints added. Same behaviour.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example (not from the book): two people aged 13 must end up
    # next to each other; group order is not fixed by the problem.
    people = [Person(13,'A'),Person(14,'B'),Person(13,'C'),Person(12,'D')]
    group_by_age(people)

    # `[p.age for p in people]` is a list comprehension listing the ages.
    print('Grouped ages:', [p.age for p in people])

    # `assert` stops the program with an AssertionError if the condition is
    # false. First: `{p.name for p in people}` is a SET comprehension; the
    # check confirms nobody was lost or duplicated. Second: the ages form one
    # of the six arrangements with the 13s adjacent. Full tests are in tests/.
    assert {p.name for p in people} == {'A','B','C','D'}
    assert [p.age for p in people] == [13, 13, 14, 12] or [p.age for p in people] == [13, 13, 12, 14] or [p.age for p in people] == [12, 13, 13, 14] or [p.age for p in people] == [12, 14, 13, 13] or [p.age for p in people] == [14, 13, 13, 12] or [p.age for p in people] == [14, 12, 13, 13]
