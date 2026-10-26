"""EPI Python — Exercise 6.4: Replace and Remove

Chapter 6: Strings
Textbook: pages 71–72 (printed page numbers; problem, solution and the
start of the program on 71; rest of the program, complexity and variants
on 72).

PROBLEM (from the textbook)
---------------------------
Consider the following two rules that are to be applied to an array of
characters.
    * Replace each 'a' by two 'd's.
    * Delete each entry containing a 'b'.
For example, applying these rules to the array <a, c, d, b, b, c, a>
results in the array <d, d, c, d, c, d, d>.

Write a program which takes as input an array of characters, and removes
each 'b' and replaces each 'a' by two 'd's. Specifically, along with the
array, you are provided an integer-valued size. Size denotes the number of
entries of the array that the operation is to be applied to. You do not
have to worry about preserving subsequent entries. For example, if the
array is <a, b, a, c, _> and the size is 4, then you can return
<d, d, d, d, c>. You can assume there is enough space in the array to hold
the final result.

HINT (from the textbook)
------------------------
Consider performing multiples passes on s.

(The wording "multiples passes" is the book's own.)

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Using library insert/delete methods: array libraries often let you insert
at a position (later entries shift right, the array grows) and delete at a
position (later entries shift left, the array shrinks). Applying those
directly would cost O(n) per insertion or deletion, so O(n^2) overall for
an array of length n.

Using a new array: writing the result into a fresh array is easy and O(n)
time — skip 'b's, write two 'd's for each 'a', copy everything else — but
it costs O(n) extra space.

Two special cases suggest an in-place method:
* If there are no 'a's, one forward pass suffices with no extra space:
  skip 'b's and copy the other characters toward the front.
* If there are no 'b's, first compute the final length (array length plus
  the number of 'a's), then write the result character by character from
  the last character backwards, so nothing is overwritten before it is
  read.

The book's example for the backward pass: the array is
<a, c, a, a, _, _, _> with size 4. Successive states (bold in the book
marks characters already part of the final result; here they are the
trailing entries):
    <a, c, a, a, _, d, d>
    <a, c, a, d, d, d, d>
    <a, c, c, d, d, d, d>
    <d, d, c, d, d, d, d>

Combined algorithm:
1. Forward iteration: delete the 'b's (compacting toward the front) and
   count the 'a's; this gives the final number of valid characters.
2. Backward iteration: starting from the end of the resulting string,
   replace each 'a' by two 'd's and move other characters to their final
   positions.
If there are more 'b's than 'a's the number of valid entries decreases;
if there are more 'a's than 'b's it increases. The book's program returns
the number of valid entries in the final result.

In this file:
* replace_and_remove_in_place follows the book's replace_and_remove(size,
  s): it modifies the given list and returns the final valid size.
* replace_and_remove is an extra wrapper-style version (not in the book)
  that grows the list if needed and returns the valid prefix as a list.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    replace_and_remove(4, list("abac") + ["", ""])   -> ['d','d','d','d','c']
    replace_and_remove_in_place(4, list("abac") + [""] * 4)  -> 5, with the
        first five entries 'd','d','d','d','c'
(These use the book's <a, b, a, c> example with extra spare entries.)
"""


# `size: int`, `letters: list[str]` and `-> list[str]` are type hints.
# `list[str]` means "a list whose items are strings" (this subscripted
# built-in form needs Python 3.9 or later). Python does not check or
# enforce annotations at run time; tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
# Generic alias types: https://docs.python.org/3/library/stdtypes.html#types-genericalias
def replace_and_remove(size: int, letters: list[str]) -> list[str]:
    """In-place: erase b and replace each a with two d entries.

    Helper added in this file (not printed in the book). Uses the
    textbook's forward-then-backward algorithm, but extends the list when
    it is too short and returns the resulting valid prefix as a new list.
    """
    # `0 <= size <= len(letters)` is a chained comparison, equivalent to
    # `0 <= size and size <= len(letters)`. `raise ValueError(...)`
    # signals an argument with an unacceptable value.
    # Comparisons: https://docs.python.org/3/reference/expressions.html#comparisons
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if not 0 <= size <= len(letters):
        raise ValueError("size outside list")
    write = 0
    count_a = 0

    # Forward pass: copy every non-'b' toward the front (deleting 'b's)
    # and count the 'a's. `write` never gets ahead of `read`, so no
    # unread entry is overwritten.
    for read in range(size):
        if letters[read] != 'b':
            letters[write] = letters[read]
            write += 1
        if letters[read] == 'a':
            count_a += 1

    # Each 'a' grows by one character (one 'a' becomes two 'd's).
    new_size = write + count_a
    if len(letters) < new_size:

        # [''] * k builds a list of k empty strings (list repetition);
        # list.extend(iterable) appends all of its items to the end of
        # the list in place. This grows the list so the backward pass has
        # room; the book instead assumes enough space already exists.
        # Sequence operations: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
        # list.extend: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
        letters.extend([''] * (new_size - len(letters)))

    # Backward pass: `cursor` reads the compacted characters from the
    # last one, `final` writes from the end of the final result.
    cursor = write - 1
    final = new_size - 1
    while cursor >= 0:
        if letters[cursor] == 'a':

            # Slice assignment: letters[i:j] = [...] replaces the entries
            # at positions i..j-1 of the same list with the new items.
            # Here it writes 'd' at positions final-1 and final.
            # Docs: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
            letters[final - 1:final + 1] = ['d', 'd']
            final -= 2
        else:
            letters[final] = letters[cursor]
            final -= 1
        cursor -= 1

    # letters[:new_size] is a slice: a new list holding the first
    # new_size entries (the valid result); spare entries are left out.
    return letters[:new_size]


def replace_and_remove_in_place(size: int, letters: list[str]) -> int:
    """Textbook's replace_and_remove: modify the list, return valid length.

    The caller supplies enough spare entries in `letters` to contain all
    expansions. The function does not grow the input or return a new list.
    Adds input checks that the book's program does not have.
    """
    # Reject a size that is negative or larger than the list.
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if size < 0 or size > len(letters):
        raise ValueError('Invalid logical input length')

    # Forward iteration: remove 'b's and count the number of 'a's.
    write_index = 0
    count_a = 0
    for i in range(size):
        if letters[i] != 'b':
            letters[write_index] = letters[i]
            write_index += 1
        if letters[i] == 'a':
            count_a += 1

    # Valid characters after the backward pass: survivors plus one extra
    # per 'a'. The book assumes the array is large enough; this file
    # checks it.
    final_size = write_index + count_a
    if final_size > len(letters):
        raise ValueError('Textbook algorithm requires preallocated capacity')

    # Backward iteration: replace 'a's with 'dd's starting from the end.
    # read_index walks the compacted characters right to left;
    # write_index now points at the last slot of the final result.
    read_index = write_index-1
    write_index = final_size-1
    while read_index >= 0:
        if letters[read_index] == 'a':

            # Slice assignment modifies consecutive entries of the same
            # list (positions write_index-1 and write_index) instead of
            # creating a new list; the list's length is unchanged because
            # two items replace two items.
            # Documentation: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
            letters[write_index - 1:write_index + 1] = ['d','d']
            write_index -= 2
        else:
            letters[write_index] = letters[read_index]
            write_index -= 1
        read_index -= 1
    return final_size


# TEXTBOOK POST-SOLUTION DISCUSSION (page 72)
# -------------------------------------------
# The forward and the backward iterations are each O(n) time, so the total
# time complexity is O(n). No additional space is allocated.
#
# VARIANTS
# --------
# Variant 1: You have an array C of characters, which may be letters,
#            digits, blanks and punctuation. The telex-encoding of C is an
#            array T in which letters, digits and blanks appear unchanged
#            but punctuation marks are spelled out: "." becomes "DOT", ","
#            becomes "COMMA", "?" becomes "QUESTION MARK", and "!" becomes
#            "EXCLAMATION MARK". Design an algorithm to perform
#            telex-encoding with O(1) space.
#            (stated in the book; no solution given)
# Variant 2: Write a program which merges two sorted arrays of integers, A
#            and B, so that the final result is a sorted array of length
#            m + n, where n and m are the lengths of A and B respectively.
#            Use O(1) additional storage: assume the result is stored in
#            A, which has sufficient space. The arrays are C-style arrays,
#            i.e. contiguous preallocated blocks of memory.
#            (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# replace_and_remove_in_place (file) vs replace_and_remove (book):
#   book: `def replace_and_remove(size, s)`; forward loop with
#   `write_idx, a_count = 0, 0`; backward part sets
#   `cur_idx = write_idx - 1`, `write_idx += a_count - 1`,
#   `final_size = write_idx + 1`, and writes an 'a' as
#   `s[write_idx - 1:write_idx + 1] = 'dd'` (assigning a string, which
#   Python splits into its characters); returns `final_size`.
#   file: renamed `replace_and_remove_in_place(size: int, letters:
#   list[str]) -> int` (type hints added); adds a ValueError check on
#   `size` and a ValueError when the list lacks capacity (the book just
#   assumes it); variables renamed (`count_a`, `read_index`); the final
#   size is computed first as `write_index + count_a` and `write_index`
#   is then reset to `final_size - 1` (equivalent arithmetic); the
#   slice assignment uses the list `['d','d']` instead of the string
#   'dd' (same effect on a list).
# replace_and_remove (file): not in the book. Same two-pass algorithm,
#   but it extends the list with '' entries when it is too short and
#   returns the slice `letters[:new_size]` (a list) instead of the size.
#   Note the file's name `replace_and_remove` refers to this helper, not
#   to the book's program of that name.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The book's <a, b, a, c, ...> example with size 4. list("abac")
    # splits a string into a list of its characters, and `+` concatenates
    # two lists into a new list (here adding two spare '' entries).
    # The comprehensive test suite remains in the separate tests/ folder.
    letters = list("abac") + ["", ""]
    result = replace_and_remove(4, letters)

    # print() with several arguments writes them separated by a space.
    print("replace_and_remove:", result)

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    assert result == list("ddddc")

    # The textbook version needs enough preallocated spare entries; it
    # returns the valid length, and buffer[:count] shows the valid part.
    buffer = list("abac") + ["", "", "", ""]
    count = replace_and_remove_in_place(4, buffer)
    print("textbook in-place replacement:", buffer[:count], "valid length:", count)
    assert buffer[:count] == list("ddddc") and count == 5
