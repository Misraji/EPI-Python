# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_17_greedy_algorithms_and_invariants.pg_260_optimum_task_assignment import optimum_task_assignment


@pytest.mark.parametrize(('durations','optimum'), [([5,2,1,6,4,4],8),([1,2],3),([1,1,1,1],2),([1,2,3,4],5)])
def test_task_pairs(durations,optimum):
    result=optimum_task_assignment(durations[:])
    assert max(p.task_1+p.task_2 for p in result)==optimum
    assert sorted(x for p in result for x in p)==sorted(durations)
