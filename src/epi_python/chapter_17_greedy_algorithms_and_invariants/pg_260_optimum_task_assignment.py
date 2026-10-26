"""EPI Python 17.1, textbook printed page 260: Compute an optimum assignment of tasks.

QUESTION: Assign two tasks per worker to minimize the maximum per-worker combined duration.

TEXTBOOK ALGORITHM: Sort task durations and pair the shortest with the longest; return namedtuple pairs.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_17_greedy_algorithms_and_invariants.pg_260_optimum_task_assignment
Test: python -m pytest tests/chapter_17_greedy_algorithms_and_invariants/test_pg_260_optimum_task_assignment.py -v
"""

# collections.namedtuple documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
import collections


PairedTasks = collections.namedtuple('PairedTasks', ('task_1','task_2'))


def optimum_task_assignment(task_durations: list[int]) -> list[PairedTasks]:
    """Return pairings; as in the textbook, input order is changed by sort()."""
    task_durations.sort()
    return [PairedTasks(task_durations[i], task_durations[~i])
            for i in range(len(task_durations)//2)]


if __name__ == '__main__':
    assignments=optimum_task_assignment([5,2,1,6,4,4])
    print('Optimal pairing:',assignments)
    assert max(a.task_1+a.task_2 for a in assignments)==8
