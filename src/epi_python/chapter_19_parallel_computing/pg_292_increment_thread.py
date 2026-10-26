"""EPI Python 19.2, textbook printed page 292: Analyze two unsynchronized interleaved threads.

QUESTION: Analyze unsynchronized shared counter increments, which can lose updates because increments are read-modify-write.

TEXTBOOK ALGORITHM: The PDF launches two threading.Thread objects and joins them; outcomes depend on interpreter/scheduler.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_19_parallel_computing.pg_292_increment_thread
Test: python -m pytest tests/chapter_19_parallel_computing/test_pg_292_increment_thread.py -v
"""

# threading.Thread documentation: https://docs.python.org/3/library/threading.html#threading.Thread
import threading


def run_unsynchronized_increments(n: int) -> int:
    counter = 0

    def increment_thread():
        nonlocal counter
        for _ in range(n):
            counter = counter + 1

    t1=threading.Thread(target=increment_thread)
    t2=threading.Thread(target=increment_thread)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return counter


if __name__=='__main__':
    result=run_unsynchronized_increments(10000)
    print('Unprotected counter after two threads:',result)
    assert 0<=result<=20000
