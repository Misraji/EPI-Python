"""EPI Python — Exercise 16.1: Count the Number of Score Combinations

Chapter 16: Dynamic Programming
Textbook: pages 236–239 (printed page numbers; problem and solution start on 236).

PROBLEM (from the textbook)
---------------------------
"In an American football game, a play can lead to 2 points (safety), 3
points (field goal), or 7 points (touchdown, assuming the extra point).
Many different combinations of 2, 3, and 7 point plays can make up a final
score. For example, four combinations of plays yield a score of 12:
  * 6 safeties (2 x 6 = 12),
  * 3 safeties and 2 field goals (2 x 3 + 3 x 2 = 12),
  * 1 safety, 1 field goal and 1 touchdown (2 x 1 + 3 x 1 + 7 x 1 = 12), and
  * 4 field goals (3 x 4 = 12)."

"Write a program that takes a final score and scores for individual plays,
and returns the number of combinations of plays that result in the final
score."

HINT (from the textbook)
------------------------
"Count the number of combinations in which there are 0 w0 plays, then 1 w0
plays, etc."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Intuition from small scores: a 9 point score can be reached by scoring 7
then a 2 point play, scoring 6 then a 3 point play, or scoring 2 then a 7
point play. In general an s point score comes from an s-2, s-3 or s-7
point score followed by one play. That recursively enumerates every
scoring SEQUENCE, but different sequences can be the same combination
(e.g. 2 then 7, and 7 then 2, both give 9). Brute force would enumerate the
sequences and count distinct combinations (e.g. sort each sequence and put
it in a hash table) — far too slow, since there can be very many sequences.

Since only combinations matter, count combinations by how many plays of
each single type are used. Example, final score 12:
* Only 2 point plays: exactly one way.
* 2 and 3 point plays: put all 2 point plays first. Zero 2 point plays ->
  one combination of 3 point plays; one 2 point play -> none (3 does not
  divide 12 - 2); two -> none (3 does not divide 12 - 2x2); three -> one
  (3 divides 12 - 2x3); and so on.
* Adding 7 point plays: add the number of combinations of 2 and 3 that
  reach 12 and that reach 5 — the only scores from which 7 point plays can
  lead to 12.

With play scores W[0], ..., W[n-1] and final score s, a naive version of
this is exponential because it re-solves the same subproblems. DP fixes
that: let A[i][j] be the number of combinations totalling j using plays
W[0], ..., W[i]. (E.g. A[1][12] counts the ways to reach 12 with 2 and/or 3
point plays.) Then A[i+1][j] = A[i][j] (no W[i+1] plays) + A[i][j - W[i+1]]
(one) + A[i][j - 2W[i+1]] (two) + ...

Directly coded this needs three nested loops: over scores, over play
types, and a third over at most j/W[i] + 1 values (e.g. for j = 10, i = 1,
W[i] = 3 it looks at A[0][10], A[0][7], A[0][4], A[0][1]). The third loop
is bounded by s, so the time is O(sns) = O(s^2 n).

Improvement: the sums repeat work. With 2 and 3 point plays, the count for
12 is A[0][0] + A[0][3] + A[0][6] + A[0][9] + A[0][12] and the count for 15
is A[0][0] + A[0][3] + A[0][6] + A[0][9] + A[0][12] + A[0][15], which
repeats the first sum. So A[1][15] = A[0][15] + A[1][12], and in general
A[1][j] = A[0][j] + A[1][j - 3]: A[1][0] = A[0][0], A[1][1] = A[0][1],
A[1][2] = A[0][2], A[1][3] = A[0][3] + A[1][0], A[1][4] = A[0][4] + A[1][1],
A[1][5] = A[0][5] + A[1][2], ... Each entry now takes O(1) time.

Figure 16.3 (DP table for 2,3,7 point plays, final scores 0..12):

    score:  0  1  2  3  4  5  6  7  8  9 10 11 12
    2       1  0  1  0  1  0  1  0  1  0  1  0  1
    2,3     1  0  1  1  1  1  2  1  2  2  2  2  3
    2,3,7   1  0  1  1  1  1  2  2  2  3  3  3  4

E.g. for 2,3,7 and total 9: the entry for 2,3 at 9 (no 7 point play) plus
the entry for 2,3,7 at 2 (one more 7 point play) = 2 + 1 = 3.

The book's program num_combinations_for_final_score(final_score,
individual_play_scores) implements this 2D table
-> `num_combinations_for_final_score_table` below. The file's
`num_combinations_for_final_score` is a one-dimensional version that is NOT
printed in the book (it corresponds to the first variant, "solve using O(s)
space", for which the book gives no solution).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    score=0, plays=[2, 3]    -> 1   (the empty combination)
    score=4, plays=[2, 3]    -> 1   (2 + 2)
    score=7, plays=[2, 3, 7] -> 2   (7; 2 + 2 + 3)
    score=1, plays=[2, 3]    -> 0
"""


def num_combinations_for_final_score(score: int, scores: list[int]) -> int:
    """Count combinations of plays summing to `score`, with an O(score) table.

    NOT a printed textbook implementation: a one-row version of the book's
    2D table (the book's first variant asks for O(s) space but gives no
    solution).
    """

    # ways[t] = number of combinations, using the play types processed so
    # far, that total t. `[0]*(score+1)` builds a list of score+1 zeros.
    # Type hints such as `score: int` are not enforced by Python.
    ways=[0]*(score+1)

    # One way to reach 0: use no plays.
    ways[0]=1

    # Play types in the OUTER loop: each type is considered once, so
    # combinations are counted, not ordered sequences. Totals ascend, so
    # ways[total-play] already includes uses of the current play type; that
    # is what allows any number of plays of this type (the 1D form of
    # A[i][j] = A[i-1][j] + A[i][j - W[i]]).
    for play in scores:
        for total in range(play,score+1):
            ways[total] += ways[total-play]
    return ways[score]



def num_combinations_for_final_score_table(score: int, scores: list[int]) -> int:
    """Textbook implementation: the 2D DP table over play types and scores.

    Book name num_combinations_for_final_score(final_score,
    individual_play_scores). Returns 1 for score 0 and 0 otherwise when no
    play types are given (not in the book).
    """

    # With no play types the table would have no rows; handle it directly.
    # `x if cond else y` is a conditional expression: it evaluates to x
    # when cond is true, otherwise to y.
    if not scores:
        return 1 if score == 0 else 0

    # dp[i][total] counts unordered ways using scoring values scores[:i+1].
    # The list comprehension creates a SEPARATE row list for each play type
    # (`[[0]*(score+1)]*len(scores)` would instead repeat one shared row).
    # `_` is the conventional name for a loop variable that is not used.
    dp = [[0] * (score + 1) for _ in scores]

    # enumerate(scores) yields (index, value) pairs: row number and play.
    for row, play in enumerate(scores):

        # One way to reach 0 (the book puts this 1 into the initial rows).
        dp[row][0] = 1
        for total in range(1, score + 1):

            # Combinations that use no play of this type: the previous row.
            # A nonzero row number is truthy, so `if row` means row >= 1.
            without_play = dp[row - 1][total] if row else 0

            # Reuse the same row for unbounded repetitions of this play:
            # dp[row][total - play] already counts all combinations that
            # may include this play type, so adding one more play reaches
            # `total`.
            with_play = dp[row][total - play] if total >= play else 0
            dp[row][total] = without_play + with_play

    # `dp[-1]` is the last row (all play types); its entry for `score`.
    return dp[-1][score]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 239)
# --------------------------------------------
# Time: O(sn) — two loops, one over the s scores and one over the n play
# types, each entry O(1). Space: O(sn), the size of the 2D array.
#
# VARIANTS (each stated in the book; no solution given)
# ----------------------------------------------------
# 1. Solve the same problem using O(s) space.
# 2. Write a program that takes a final score and scores for individual
#    plays, and returns the number of SEQUENCES of plays that result in the
#    final score. For example, 18 sequences of plays yield a score of 12;
#    some are <2,2,2,3,3>, <2,3,2,2,3>, <2,3,7>, <7,3,2>.
# 3. The final score is given as (s, s'): Team 1 scored s points and Team 2
#    scored s'. Compute the number of distinct scoring sequences that lead
#    to this score. For example, for (6, 3), "Team 1 scores 3, Team 2 scores
#    3, Team 1 scores 3" is one such sequence.
# 4. The final score is (s, s'). Compute the maximum number of times the
#    team that led could have changed. For example, for s = 10 and s' = 6
#    the lead could have changed 4 times: Team 1 scores 2, then Team 2
#    scores 3 (lead change), then Team 1 scores 2 (lead change), then Team
#    2 scores 3 (lead change), then Team 1 scores 3 (lead change), followed
#    by 3.
# 5. You are climbing stairs and can advance 1 to k steps at a time. Your
#    destination is exactly n steps up. Write a program which takes n and k
#    and returns the number of ways to reach the destination. For example,
#    for n = 4 and k = 2 there are five ways: four single steps; two single
#    steps then a double step; a single, a double, then a single; a double
#    then two singles; and two double steps.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * `num_combinations_for_final_score` (1D list `ways`) is NOT the book's
#   program, although it has the book's function name; it is an added
#   O(s)-space version (the book's first variant). Parameters renamed
#   `score`, `scores`.
# * The book's 2D program is `num_combinations_for_final_score_table`
#   here. Book names: `final_score`, `individual_play_scores`,
#   `num_combinations_for_score`, loop indices `i`, `j`,
#   `without_this_play`, `with_this_play`; file: `score`, `scores`, `dp`,
#   `row`/`play` (via enumerate), `total`, `without_play`, `with_play`.
# * Book initializes rows as `[[1] + [0] * final_score for _ in
#   individual_play_scores]`; file creates zero rows and sets
#   `dp[row][0] = 1` inside the loop.
# * Book condition `if i >= 1 else 0`; file `if row else 0` (same meaning).
#   Book returns `num_combinations_for_score[-1][-1]`; file
#   `dp[-1][score]` (same entry).
# * File adds the empty-`scores` guard (book would fail with IndexError on
#   an empty list) and type hints.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples for the 1D version: score 0 (one empty combination),
    # a single combination, the 2,3,7 case for 7 (7 alone, or 2+2+3), and
    # an unreachable score. Then the textbook 2D version on 7 with 2,3,7.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, the pytest suite is thorough.
    observed = num_combinations_for_final_score(0, [2, 3])
    print("num_combinations_for_final_score:", observed)
    assert observed == 1
    observed = num_combinations_for_final_score(4, [2, 3])
    print("num_combinations_for_final_score:", observed)
    assert observed == 1
    observed = num_combinations_for_final_score(7, [2, 3, 7])
    print("num_combinations_for_final_score:", observed)
    assert observed == 2
    observed = num_combinations_for_final_score(1, [2, 3])
    print("num_combinations_for_final_score:", observed)
    assert observed == 0
    assert num_combinations_for_final_score_table(7, [2, 3, 7]) == 2
    print("Two-dimensional and space-optimized scoring DP: passed")
