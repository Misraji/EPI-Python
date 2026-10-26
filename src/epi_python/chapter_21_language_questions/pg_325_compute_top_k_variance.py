"""EPI Python — Exercise 21.8: Python Code

Chapter 21: Language Questions
Textbook: pages 325–326 (printed page numbers; the problem and its long
program start on 325, the rest of that program and the solution are on 326).

PROBLEM (from the textbook)
---------------------------
Rewrite the following program using a Pythonic style.

The program to rewrite is `compute_top_k_variance(students, scores, k)`,
whose docstring reads:

    students and scores are equal length lists of strings and floats,
    respectively. The function computes for each string that appears at
    least k times in the list the variance of the top k scores that
    correspond to it. Strings that appear fewer than k times are not
    considered.

(The full long program is reproduced as executable code below, as
`compute_top_k_variance_original`.)

HINT (from the textbook)
------------------------
The book gives no hint for this exercise.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The long program works in four stages, each written with explicit loops and
explicit initialization:
1. Count how many times each student name occurs, using a plain dict and
   an "if not present, set to 1, else add 1" test.
2. Create an empty score list for every student with at least k
   occurrences, then loop over the input by index to append each of those
   students' scores.
3. For each such student, sort the scores and copy the last k of them
   (the k largest, from largest down) into a new list.
4. For each student, total the k scores in a loop, divide by k for the
   mean, then sum (score - mean) * (score - mean) in another loop.

Note: the value computed is the SUM of squared deviations from the mean;
neither program divides it by k (or k - 1), even though both call it a
variance. Both implementations in this file keep that behaviour.

The book's answer: the built-ins and library functions zip(),
functools.reduce(), heapq.nlargest() and sum() directly replace the
boilerplate loops, and collections.defaultdict together with a dictionary
comprehension removes the need for explicit initialization. Concretely:
- zip pairs each student with their score, so no index variable is needed;
- defaultdict(list) groups scores by student without first creating keys;
- a dict comprehension with an `if` filter keeps only students with at
  least k scores, and heapq.nlargest(k, ...) picks their top k;
- sum(...) / k gives the mean, and functools.reduce with a lambda
  accumulates the squared deviations.

Both programs are present below: `compute_top_k_variance_original` (the
long program from the problem) and `compute_top_k_variance` (the book's
Pythonic solution).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    students = ["A", "B", "A", "A", "B", "C"]
    scores   = [1.0, 4.0, 2.0, 5.0, 8.0, 10.0],  k = 2
    A's scores [1, 2, 5]: top 2 are [5, 2], mean 3.5,
        (5 - 3.5)**2 + (2 - 3.5)**2 = 4.5
    B's scores [4, 8]: mean 6.0, (8 - 6)**2 + (4 - 6)**2 = 8.0
    C appears only once (< k), so C is omitted.
    Result: {"A": 4.5, "B": 8.0}
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# defaultdict: https://docs.python.org/3/library/collections.html#collections.defaultdict
import collections

# Python standard library: higher-order functions and operations on callables.
# Module documentation: https://docs.python.org/3/library/functools.html
# reduce: https://docs.python.org/3/library/functools.html#functools.reduce
import functools

# Python standard library: heap queue (priority queue) algorithms.
# Module documentation: https://docs.python.org/3/library/heapq.html
# nlargest: https://docs.python.org/3/library/heapq.html#heapq.nlargest
import heapq


def _check_inputs(students, scores, k):
    """Validate inputs (helper added in this repository; not in the book)."""

    # len() returns the number of items in a sequence.
    if len(students) != len(scores):

        # ValueError is the built-in exception for an unacceptable value.
        # https://docs.python.org/3/library/exceptions.html#ValueError
        raise ValueError("students and scores must have equal lengths")
    if k <= 0:
        raise ValueError("k must be positive")


# Type hints: `list[str]` means "a list of str", `list[float]` "a list of
# float", and `dict[str, float]` "a dict mapping str keys to float values".
# (Built-in types written with [...] in hints need Python 3.9+.) Python does
# not check or enforce these hints at runtime.
def compute_top_k_variance_original(
    students: list[str], scores: list[float], k: int
) -> dict[str, float]:
    """The verbose program the textbook asks the reader to rewrite."""
    _check_inputs(students, scores, k)

    # `counts: dict[str, int] = {}` is a variable annotation: a type hint on
    # an assignment. It only documents the intended type; `{}` is an
    # ordinary empty dict.
    counts: dict[str, int] = {}

    # Stage 1: count occurrences, looping by index with range(len(...)).
    for i in range(len(students)):
        if students[i] not in counts:
            counts[students[i]] = 1
        else:
            counts[students[i]] += 1

    # Stage 2: an empty list for each student with at least k occurrences,
    # then append that student's scores (again looping by index).
    all_scores: dict[str, list[float]] = {}
    for student in counts:
        if counts[student] >= k:
            all_scores[student] = []
    for i in range(len(students)):
        if students[i] in all_scores:
            all_scores[students[i]].append(scores[i])

    top_k_scores: dict[str, list[float]] = {}
    for student in all_scores:

        # Stage 3: sorted(iterable) returns a NEW list in ascending order
        # (the original list is unchanged). The k largest scores are at the
        # end; index len - 1 - i walks backward from the largest.
        # https://docs.python.org/3/library/functions.html#sorted
        sorted_scores = sorted(all_scores[student])
        top_k_scores[student] = []
        for i in range(k):
            top_k_scores[student].append(sorted_scores[len(sorted_scores) - 1 - i])

    # Stage 4: mean by explicit summation, then the sum of squared
    # deviations. `/` is true division and always returns a float.
    result: dict[str, float] = {}
    for student in top_k_scores:
        total = 0
        for score in top_k_scores[student]:
            total += score
        mean = total / k
        variance = 0
        for score in top_k_scores[student]:
            variance += (score - mean) * (score - mean)
        result[student] = variance
    return result


def compute_top_k_variance(
    students: list[str], scores: list[float], k: int
) -> dict[str, float]:
    """The textbook's Pythonic solution using standard-library idioms."""
    _check_inputs(students, scores, k)

    # collections.defaultdict(factory) is a dict that, when a MISSING key is
    # looked up, first calls `factory()` and stores the result under that
    # key. With `list` as the factory, a new student automatically gets an
    # empty list, so `.append` works without the long program's explicit
    # initialization. Note that `list` is passed itself (the callable), not
    # `list()` or `[]`. Only lookups with [] create keys; `in` does not.
    all_scores = collections.defaultdict(list)

    # zip(a, b) yields pairs (a[0], b[0]), (a[1], b[1]), ... and stops at
    # the shorter input. Unpacking each pair into `student, score` replaces
    # the long program's index variable i.
    # https://docs.python.org/3/library/functions.html#zip
    for student, score in zip(students, scores):
        all_scores[student].append(score)

    # A dictionary comprehension `{key: value for ... in ... if condition}`
    # builds a dict in one expression. The `if` clause skips students with
    # fewer than k scores. dict.items() yields (key, value) pairs.
    #
    # heapq.nlargest(n, iterable) returns a list of the n largest items,
    # largest first. It does not modify its input and, for small n, avoids
    # fully sorting the data. This replaces the long program's
    # sort-then-copy-backward loop.
    top_k_scores = {
        student: heapq.nlargest(k, student_scores)
        for student, student_scores in all_scores.items()
        if len(student_scores) >= k
    }

    # functools.reduce(function, iterable, initial) folds an iterable into a
    # single value: starting from `initial` (0 here), it repeatedly sets
    # accumulator = function(accumulator, next_item). The lambda (a small
    # anonymous function) adds one squared deviation per score, giving the
    # sum of (score - mean)**2.
    #
    # The inner generator expression produces (student, selected_scores,
    # mean) triples, where sum(selected_scores) / k is the mean; sum() adds
    # all items of an iterable. The outer dict comprehension unpacks each
    # triple, so `mean` is available inside the lambda while reduce runs.
    # https://docs.python.org/3/library/functions.html#sum
    return {
        student: functools.reduce(
            lambda variance, score: variance + (score - mean) ** 2,
            selected_scores,
            0,
        )
        for student, selected_scores, mean in (
            (student, selected_scores, sum(selected_scores) / k)
            for student, selected_scores in top_k_scores.items()
        )
    }


# TEXTBOOK POST-SOLUTION DISCUSSION (page 326)
# --------------------------------------------
# The book gives no further discussion or complexity analysis after the
# Pythonic program; its point is that zip(), functools.reduce(),
# heapq.nlargest() and sum() replace boilerplate loops, while
# collections.defaultdict and a dictionary comprehension remove explicit
# initialization.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Long program (`compute_top_k_variance_original`):
# - Book names it `compute_top_k_variance(students, scores, k)` with a
#   triple-quoted docstring; file renames it with an `_original` suffix and
#   adds type hints and variable annotations (`counts: dict[str, int]`, ...).
# - Book loops `for key in counts` / `for key in all_scores` /
#   `for key in top_k_scores`; file uses the name `student` instead of `key`.
# - Book: `variance = variance + (score - mean) * (score - mean)`; file:
#   `variance += (score - mean) * (score - mean)`.
# Pythonic program (`compute_top_k_variance`):
# - Same name as the book; type hints added.
# - Book reuses the name `scores` inside both comprehensions (shadowing the
#   parameter); file uses `student_scores` and `selected_scores`.
# - Book writes `(score - mean)**2`; file `(score - mean) ** 2` (same).
# Both: call the added helper `_check_inputs`, which raises ValueError for
# unequal lengths or k <= 0; the book has no such checks.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added example (see the module docstring): A has three scores, B two,
    # C one; with k = 2, C is left out.
    student_names = ["A", "B", "A", "A", "B", "C"]
    marks = [1.0, 4.0, 2.0, 5.0, 8.0, 10.0]

    # Functions are objects, so both versions can be looped over and called.
    for function in (compute_top_k_variance_original, compute_top_k_variance):
        observed = function(student_names, marks, 2)

        # f-string: each expression in {} is evaluated and inserted;
        # `function.__name__` is the function's name as a string.
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"{function.__name__}: {observed}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. Dicts are equal when they have the same keys and values.
        # These are quick smoke checks; pytest does the thorough testing.
        assert observed == {"A": 4.5, "B": 8.0}
    print("Both textbook implementations passed.")
