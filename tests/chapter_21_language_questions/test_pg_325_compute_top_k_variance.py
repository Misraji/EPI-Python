"""Tests for the two complete variants of EPI exercise 21.8."""

# Parameterization repeats a test for each independently named algorithm.
# Documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_21_language_questions.pg_325_compute_top_k_variance import (
    compute_top_k_variance,
    compute_top_k_variance_original,
)


@pytest.mark.parametrize('algorithm', [compute_top_k_variance_original, compute_top_k_variance])
def test_top_k_score_variance(algorithm):
    assert algorithm(['A', 'B', 'A', 'A', 'B', 'C'], [1, 4, 2, 5, 8, 10], 2) == {
        'A': 4.5, 'B': 8.0,
    }
    assert algorithm(['A', 'A', 'A'], [4, 4, 7], 1) == {'A': 0.0}
    assert algorithm(['A', 'A'], [1, 5], 3) == {}
    with pytest.raises(ValueError):
        algorithm(['A'], [], 2)
    with pytest.raises(ValueError):
        algorithm(['A'], [1], 0)


def test_randomized_equivalence_to_reference():
    from random import Random
    rng = Random(2108)
    for _ in range(400):
        students = [rng.choice('abcd') for _ in range(rng.randrange(1, 35))]
        scores = [rng.randint(-30, 30) for _ in students]
        k = rng.randrange(1, 12)
        expected = {}
        for name in set(students):
            top = sorted((score for student, score in zip(students, scores)
                          if student == name), reverse=True)[:k]
            if len(top) == k:
                mean = sum(top) / k
                expected[name] = sum((x - mean)**2 for x in top)
        for algorithm in (compute_top_k_variance_original, compute_top_k_variance):
            output = algorithm(students, scores, k)
            assert output.keys() == expected.keys()
            for key in output:
                assert output[key] == pytest.approx(expected[key])
