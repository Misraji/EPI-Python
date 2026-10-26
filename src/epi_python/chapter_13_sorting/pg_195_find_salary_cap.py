"""EPI 13.11, printed page 195: Compute a salary threshold.

Problem: Compute a salary threshold. See pg_195_exercise_13_11_compute_a_salary_threshold.md for the full
original problem, hint, development, and variants from the PDF text layer.

Approach and complexity: O(n log n) due to sorting and O(n) scan; progressively assign salaries below cap.

EDUCATIONAL RECONSTRUCTION: source and comments are not claimed verbatim.
Run directly: python -m epi_python.chapter_13_sorting.pg_195_find_salary_cap
Test: python -m pytest tests/chapter_13_sorting/test_pg_195_find_salary_cap.py -v
"""

# TEXTBOOK PROBLEM (exercise 13.11, printed page 195):
# Compute the common salary cap that reduces total payroll to a specified target.
# HINT: Sort salaries and determine which salaries will remain unchanged.

def find_salary_cap(target_payroll: float, current_salaries: list[float]) -> float:
    """Find a common cap so sum(min(salary, cap)) equals the target."""
    if any(value < 0 for value in current_salaries) or target_payroll < 0:
        raise ValueError('Salaries and payroll must be nonnegative')
    if not current_salaries:
        return 0.0 if target_payroll == 0 else -1.0
    if target_payroll > sum(current_salaries):
        return -1.0
    sorted_salaries = sorted(current_salaries)
    unchanged = 0.0
    for i, salary in enumerate(sorted_salaries):
        remaining = len(sorted_salaries) - i
        possible = unchanged + remaining * salary
        if target_payroll <= possible:
            return (target_payroll - unchanged) / remaining
        unchanged += salary
    return max(sorted_salaries)


if __name__ == '__main__':
    cap = find_salary_cap(210.0, [90.0,30.0,100.0,40.0,20.0])
    print('Payroll cap:', cap)
    assert abs(sum(min(s,cap) for s in [90,30,100,40,20]) - 210) < 1e-9
