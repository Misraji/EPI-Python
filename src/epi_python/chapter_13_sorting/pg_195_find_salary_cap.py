"""EPI Python — Exercise 13.11: Compute a Salary Threshold

Chapter 13: Sorting
Textbook: pages 195–196 (printed page numbers; problem and solution start on 195).

PROBLEM (from the textbook)
---------------------------
"You are working in the finance office for ABC corporation. ABC needs to cut
payroll expenses to a specified target. The chief executive officer wants to
do this by putting a cap on last year's salaries. Every employee who earned
more than the cap last year will be paid the cap this year; employees who
earned no more than the cap will see no change in their salary."

"For example, if there were five employees with salaries last year were
$90, $30, $100, $40, and $20, and the target payroll this year is $210, then
60 is a suitable salary cap, since 60+30+60+40+20 = 210."

"Design an algorithm for computing the salary cap, given existing salaries
and the target payroll."

HINT (from the textbook)
------------------------
"How does the payroll vary with the cap?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force is of little use: the cap has infinitely many possible values.

Binary search: the cap lies between 0 and the maximum current salary, and
the payroll increases with the cap, so binary search over that range works
(if a cap is too high, every higher cap is also too high; likewise for too
low). With n employees and salaries in array A, the payroll for cap c is
P(c) = sum over i = 0..n-1 of min(A[i], c). Each binary-search step evaluates
P(c) in O(n) time. As in Solution 11.5 (page 149), the number of steps
depends on the largest salary and the desired accuracy.

A more analytical method avoids needing a tolerance. As the cap rises, as
long as it stays at or below a given person's salary, the payroll grows
linearly. So iterate through the salaries in increasing order. With A
sorted, suppose the cap for total payroll T lies between the k-th and
(k+1)-th salaries. Then we need
    sum_{i=0}^{k-1} A[i] + (n - k) * c = T,
which gives
    c = (T - sum_{i=0}^{k-1} A[i]) / (n - k).

Worked example from the book: A = <20,30,40,90,100>, T = 210. The payrolls
for caps equal to each salary in A are <100,140,170,270,280>. Since 210 lies
between 170 and 270, the cap lies between 40 and 90. For any cap c in that
range the payroll is 20 + 30 + 40 + 2c; setting this to 210 gives c = 60.

The function below follows the book's single implementation (sort, then scan
for the first salary whose implied payroll reaches the target).
"""


# Type hints: a float target and a list of float salaries in, a float cap
# out. Python does not enforce annotations at run time.
def find_salary_cap(target_payroll: float, current_salaries: list[float]) -> float:
    """Find a common cap so sum(min(salary, cap)) equals the target.

    This is the textbook's sort-and-scan implementation. Returns -1.0 when
    no cap can reach the target (target exceeds the current payroll).
    """

    # Added input check (not in the book). any(iterable) returns True as
    # soon as one item is true; the generator expression `value < 0 for
    # value in current_salaries` yields one boolean per salary.
    # Documentation: https://docs.python.org/3/library/functions.html#any
    if any(value < 0 for value in current_salaries) or target_payroll < 0:
        raise ValueError('Salaries and payroll must be nonnegative')

    # Added edge case (not in the book): with no employees, only a zero
    # target is achievable. Conditional expression `X if cond else Y`.
    if not current_salaries:
        return 0.0 if target_payroll == 0 else -1.0

    # Added early exit: the built-in sum() adds all salaries. If the target
    # exceeds the current payroll no cap can reach it (the book reaches the
    # same -1.0 at the end of its loop).
    # Documentation: https://docs.python.org/3/library/functions.html#sum
    if target_payroll > sum(current_salaries):
        return -1.0

    # sorted() returns a NEW ascending list, leaving the caller's list
    # unchanged (the book sorts the input in place with list.sort()).
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    sorted_salaries = sorted(current_salaries)

    # `unchanged` is the book's unadjusted_salary_sum: the total of salaries
    # below the cap, which are paid in full. 0.0 makes the arithmetic float.
    unchanged = 0.0

    # enumerate(iterable) yields (index, item) pairs, unpacked into
    # `i, salary`. Index i tells how many salaries lie before this one.
    # Documentation: https://docs.python.org/3/library/functions.html#enumerate
    for i, salary in enumerate(sorted_salaries):

        # If the cap equalled `salary`, the people from i onward (n - i of
        # them) would each be paid `salary`; `possible` is that payroll.
        remaining = len(sorted_salaries) - i
        possible = unchanged + remaining * salary

        # The first time that payroll reaches the target, the cap lies
        # between the previous salary and this one: solve
        # unchanged + remaining * c = target for c.
        # `/` is true division and always produces a float.
        if target_payroll <= possible:
            return (target_payroll - unchanged) / remaining
        unchanged += salary

    # Added fallback (not in the book). Because of the early exit above,
    # the loop always returns before reaching this line. The built-in max()
    # returns the largest item.
    return max(sorted_salaries)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 196)
# --------------------------------------------
# Sorting A is the most expensive step, so the run time is O(n log n). With A
# sorted, a single pass finds the first entry whose implied payroll exceeds
# the target, and an arithmetic expression then gives the cap.
#
# If the salary array is given already sorted together with its prefix sums,
# then for a given T the cap can be found by binary search in O(log n) time.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Solve the same problem
# using only O(1) space.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def find_salary_cap(target_payroll, current_salaries):` sorts the
# input in place (`current_salaries.sort()`), uses
# `unadjusted_salary_sum = 0.0`, loops with
# `for i, current_salary in enumerate(current_salaries):`, computes
# `adjusted_people = len(current_salaries) - i` and
# `adjusted_salary_sum = current_salary * adjusted_people`, returns
# `(target_payroll - unadjusted_salary_sum) / adjusted_people` when
# `unadjusted_salary_sum + adjusted_salary_sum >= target_payroll`, and after
# the loop returns -1.0 (comment "No solution, since target_payroll >
# existing payroll.").
# File: type hints added; extra ValueError check for negative values; extra
# empty-list case; explicit early `return -1.0` when the target exceeds
# `sum(current_salaries)`; sorts a copy with `sorted()`; variables renamed
# `unchanged`, `salary`, `remaining`, `possible`; the comparison is written
# `target_payroll <= possible`; final line `return max(sorted_salaries)`
# instead of `return -1.0` (unreachable in practice). Same results for valid
# inputs.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # The book's example: salaries 90, 30, 100, 40, 20 and target 210; the
    # expected cap is 60.
    cap = find_salary_cap(210.0, [90.0,30.0,100.0,40.0,20.0])
    print('Payroll cap:', cap)

    # `assert` stops the program with an AssertionError if the condition is
    # false. Rather than compare floats exactly, it recomputes the capped
    # payroll (sum of min(salary, cap)) and checks with abs() that it is
    # within 1e-9 (scientific notation for 0.000000001) of the target.
    # Full tests live in the tests/ folder.
    assert abs(sum(min(s,cap) for s in [90,30,100,40,20]) - 210) < 1e-9
