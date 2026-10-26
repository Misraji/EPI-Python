"""EPI Python — Exercise 6.6: Reverse All the Words in a Sentence

Chapter 6: Strings
Textbook: pages 73–74 (printed page numbers; problem, solution and most of
the program on 73; end of the program and complexity on 74).

PROBLEM (from the textbook)
---------------------------
Given a string containing a set of words separated by whitespace, we would
like to transform it to a string in which the words appear in the reverse
order. For example, "Alice likes Bob" transforms to "Bob likes Alice". We
do not need to keep the original string.

Implement a function for reversing the words in a string s.

HINT (from the textbook)
------------------------
It's difficult to solve this with one pass.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Computing, in a single pass, where every character belongs in the final
result is intricate.

Special case: if every word is a single character, the answer is simply the
reverse of s.

General case: reversing the whole of s already puts the words in their
correct relative order, but every word longer than one character now has
its letters backwards. Fix this by reversing each individual word.

Worked example from the book: "ram is costly" reversed is
"yltsoc si mar"; reversing each word then gives "costly is ram".

The book's program assumes s is encoded as a bytearray (a mutable sequence
of bytes), so both reversals happen in place. In this file:
* reverse_words_bytearray follows the book's reverse_words(s) on a
  bytearray.
* reverse_words is an extra str-based helper (not in the book) using
  str.split and str.join, which allocates new lists and strings.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    reverse_words('a')        -> 'a'
    reverse_words('')         -> ''
    reverse_words('one two')  -> 'two one'
"""


# `sentence: str` and `-> str` are type hints: they document the expected
# argument and return types. Python does not check or enforce them at run
# time; tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
def reverse_words(sentence: str) -> str:
    """Reverse the order of words separated by single ASCII spaces.

    Helper added in this file (not printed in the book): a simple
    split/reverse/join version that builds a new string.
    """

    # str.split(sep) divides a string into a list of pieces at each
    # occurrence of sep. With an explicit ' ' separator, consecutive
    # spaces produce empty strings in the list, so the exact spacing is
    # preserved (reversed) in the output; ''.split(' ') gives [''].
    # Documentation: https://docs.python.org/3/library/stdtypes.html#str.split
    words = sentence.split(' ')

    # reversed(sequence) returns a lazy iterator over the items from last
    # to first (it does not sort and does not copy the list).
    # ' '.join(iterable) concatenates the strings, putting one space
    # between neighbours.
    # reversed: https://docs.python.org/3/library/functions.html#reversed
    # str.join: https://docs.python.org/3/library/stdtypes.html#str.join
    return ' '.join(reversed(words))


# `-> None` documents that the function returns nothing useful: it works
# by mutating its argument.
def reverse_words_bytearray(buffer: bytearray) -> None:
    """Textbook's reverse_words: mutate ASCII/UTF-8 bytes in place.

    The textbook assumes each word is separated by an ASCII space and the
    caller passes a mutable `bytearray`, not an immutable Python `str`.
    """

    # A bytearray is a mutable sequence of integers 0..255 (bytes); unlike
    # str, its items can be reassigned, which is what makes an in-place,
    # O(1)-extra-space solution possible.
    # bytearray: https://docs.python.org/3/library/stdtypes.html#bytearray-objects
    #
    # First, reverse the whole string (book comment).
    # bytearray.reverse() reverses the items in place and returns None.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
    buffer.reverse()

    # Nested helper: reverse buffer[start..finish] (inclusive) in place by
    # swapping the two ends and moving inward. It reads `buffer` from the
    # enclosing function (a closure); start and finish are its own local
    # copies, so changing them does not affect the caller.
    def reverse_range(start: int, finish: int) -> None:
        while start < finish:

            # Tuple assignment: the right side is evaluated first, so the
            # two entries are swapped without a temporary variable.
            buffer[start], buffer[finish] = buffer[finish], buffer[start]
            start += 1
            finish -= 1

    start = 0
    while True:

        # bytearray.find(sub, start) returns the lowest index >= start
        # where sub occurs, or -1 if it is absent. b' ' is a bytes literal
        # holding one ASCII space byte; a bytearray is searched with
        # bytes, not with the str ' '.
        # Documentation: https://docs.python.org/3/library/stdtypes.html#bytes.find
        # Bytes literals: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
        end = buffer.find(b' ', start)
        if end < 0:
            break

        # Reverses each word in the string (book comment): the word
        # occupies positions start..end-1, just before the space.
        reverse_range(start, end-1)
        start = end+1

    # Reverses the last word (book comment): it has no space after it.
    reverse_range(start, len(buffer)-1)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 74)
# -------------------------------------------
# O(1) work is spent per character, so the time complexity is O(n), where
# n is the length of s. The computation is done in place, so the
# additional space complexity is O(1). (This applies to the bytearray
# version; the str helper reverse_words allocates a list and a new
# string.)
#
# VARIANTS
# --------
# The book lists no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# reverse_words_bytearray (file) vs reverse_words (book):
#   book: comment "Assume s is a string encoded as bytearray.";
#   `def reverse_words(s)`; `s.reverse()`; nested
#   `def reverse_range(s, start, end)` taking the array as a parameter and
#   swapping with `start, end = start + 1, end - 1`; main loop identical
#   in structure (`end = s.find(b' ', start)`, break if negative,
#   `reverse_range(s, start, end - 1)`, `start = end + 1`), then
#   `reverse_range(s, start, len(s) - 1)`.
#   file: renamed `reverse_words_bytearray(buffer: bytearray) -> None`
#   (type hints added); the nested helper is
#   `reverse_range(start: int, finish: int) -> None`, which drops the
#   array parameter and uses `buffer` from the enclosing scope; its second
#   index is named `finish` and is updated with two separate statements.
#   Same algorithm and results.
# reverse_words (file): a str-based split/reversed/join helper that is not
#   in the book. Note the file's name `reverse_words` refers to this
#   helper, not to the book's bytearray program of that name.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The first example is the book's "Alice likes Bob"; the rest are
    # added: one word, the empty string, and two words. The comprehensive
    # test suite remains in the separate tests/ folder.
    observed = reverse_words('Alice likes Bob')

    # print() with several arguments writes them separated by a space.
    print("reverse_words:", observed)

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    assert observed == 'Bob likes Alice'
    observed = reverse_words('a')
    print("reverse_words:", observed)
    assert observed == 'a'
    observed = reverse_words('')
    print("reverse_words:", observed)
    assert observed == ''
    observed = reverse_words('one two')
    print("reverse_words:", observed)
    assert observed == 'two one'

    # bytearray(b"...") makes a mutable copy of a bytes literal, as the
    # book's program requires. After the in-place call,
    # bytearray.decode('ascii') converts the bytes back to a str for
    # printing; a bytearray compares equal to a bytes object with the
    # same contents.
    # bytearray: https://docs.python.org/3/library/stdtypes.html#bytearray
    # decode: https://docs.python.org/3/library/stdtypes.html#bytearray.decode
    raw = bytearray(b"Alice likes Bob")
    reverse_words_bytearray(raw)
    print("PDF in-place bytearray method:", raw.decode('ascii'))
    assert raw == b"Bob likes Alice"
