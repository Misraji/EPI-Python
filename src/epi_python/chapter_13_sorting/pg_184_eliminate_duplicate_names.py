"""EPI Python — Exercise 13.3: Remove First-Name Duplicates

Chapter 13: Sorting
Textbook: pages 184–185 (printed page numbers; problem and solution start on 184).

PROBLEM (from the textbook)
---------------------------
"Design an efficient algorithm for removing all first-name duplicates from
an array. For example, if the input is <(Ian,Botham),(David,Gower),
(Ian,Bell),(Ian,Chappell)>, one result could be <(Ian,Bell),(David,Gower)>;
<(David,Gower),(Ian,Botham)> would also be acceptable."

HINT (from the textbook)
------------------------
"Bring equal items close together."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: use a hash table. For names this needs a hash function and an
equality function that look only at the first name. Build the hash table,
then iterate over it, writing its entries to the result array. Time O(n),
where n is the number of items; the hash table needs O(n) space in the worst
case.

Avoiding the extra space: reuse the input array to hold the result. First
sort the array, which places equal elements next to each other; sorting
takes O(n log n) time. Then remove duplicates in one O(n) pass, copying each
element that differs from the last kept element into the next "write"
position and finally truncating the array. Sorting requires that the
elements be comparable; the book's Name class therefore defines equality
(first name only) and a less-than order (first name, then last name).

The function below follows the book's single implementation (sort, then
compact in place).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [(Ian,Botham), (David,Gower), (Ian,Bell)]
        -> [(David,Gower), (Ian,Bell)]   (sorted; Bell precedes Botham)
"""

# Python standard library: automatic generation of special methods for
# simple record-like classes.
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` is a class decorator. From the annotated class attributes
# (`first_name: str`, `last_name: str`) it generates `__init__` (so
# `Name("Ian", "Bell")` works), a readable `__repr__` (used by print), and
# `__eq__`, which compares ALL fields. It does NOT generate ordering methods
# such as `__lt__` here, so Name objects themselves cannot be sorted
# directly; the function below sorts with a `key` instead.
# The `: str` annotations declare the field types; Python does not enforce them.
@dataclass
class Name:
    first_name: str
    last_name: str


# Type hints: `names: list[Name]` documents a list of Name objects;
# `-> None` says the function returns nothing (it mutates `names`).
# Annotations are not enforced at run time.
def eliminate_duplicate(names: list[Name]) -> None:
    """Retain one name per first name, sorted, updating the original list.

    This is the textbook's implementation: sort, then compact in place.
    """

    # list.sort() sorts the list IN PLACE and returns None. It is stable
    # and runs in O(n log n) time.
    # `key=` takes a function applied to each element; elements are ordered
    # by the values it returns. `lambda name: (...)` is a small anonymous
    # function returning a tuple. Tuples compare element by element, so this
    # orders by first name and breaks ties by last name, exactly the order
    # the book's `Name.__lt__` defines. Sorting brings all records with the
    # same first name next to each other.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#list.sort
    # Sorting HOW TO: https://docs.python.org/3/howto/sorting.html
    names.sort(key=lambda name: (name.first_name, name.last_name))

    # An empty list is falsy; with no names there is nothing to compact.
    if not names:
        return

    # names[0] is always kept, so writing starts at index 1.
    write = 1

    # `names[1:]` is a slice: a NEW list holding every element after the
    # first. Iterating over the copy means the assignments to names[write]
    # below cannot disturb the iteration.
    for candidate in names[1:]:

        # Compare only first names: keep `candidate` when its first name
        # differs from the most recently kept record's first name.
        if candidate.first_name != names[write - 1].first_name:
            names[write] = candidate
            write += 1

    # `del names[write:]` deletes the slice from index `write` to the end,
    # truncating the list in place so only the kept records remain.
    # Documentation: https://docs.python.org/3/tutorial/datastructures.html#the-del-statement
    del names[write:]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 185)
# --------------------------------------------
# Time: O(n log n) (dominated by sorting). Space: O(1) beyond the input.
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book's `class Name` is a hand-written class with `__init__`, an `__eq__`
#   that compares ONLY `first_name`, and an `__lt__` ordering by first name,
#   then last name. File: `@dataclass class Name` with typed fields; its
#   generated `__eq__` compares BOTH fields and it has no `__lt__`.
# - Book: `def eliminate_duplicate(A)` calls `A.sort()` (relying on
#   `Name.__lt__`; book comment "# Makes identical elements become
#   neighbors."), uses `write_idx`/`cand`, and tests `cand != A[write_idx - 1]`
#   (relying on the first-name-only `__eq__`). File: parameter `names:
#   list[Name]` with `-> None`, sorts with an explicit
#   `key=lambda name: (name.first_name, name.last_name)`, compares
#   `.first_name` attributes explicitly, uses `write`/`candidate`, and adds an
#   early `return` for an empty list (the book's `del A[1:]` would also handle
#   an empty list). The book's final `del A[write_idx:]` is kept as
#   `del names[write:]`. Resulting behaviour is the same.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Three of the book's example records (Ian Chappell omitted). After
    # sorting, David Gower comes first, then Ian Bell (Bell < Botham), and
    # Ian Botham is removed as a first-name duplicate.
    people = [Name("Ian", "Botham"), Name("David", "Gower"), Name("Ian", "Bell")]
    eliminate_duplicate(people)
    print("Distinct first names:", people)

    # `[p.first_name for p in people]` is a list comprehension extracting
    # the first names. `assert` stops the program with an AssertionError if
    # the condition is false; a quick smoke check, with the full tests in
    # the separate tests/ folder.
    assert [p.first_name for p in people] == ["David", "Ian"]
