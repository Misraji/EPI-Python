"""EPI Python 19.9, textbook printed page 298: Test the Collatz conjecture in parallel.

QUESTION: Check the Collatz conjecture for all integers in [1,U] with bounded parallel workers.

TEXTBOOK ALGORITHM: Partition the input into ranges; submit each range to a ProcessPoolExecutor, like the PDF.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_19_parallel_computing.pg_298_parallel_collatz
Test: python -m pytest tests/chapter_19_parallel_computing/test_pg_298_parallel_collatz.py -v
"""

# concurrent.futures.ProcessPoolExecutor: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def collatz_check(x,visited):
    if x==1:
        return True
    if x in visited:
        return False
    visited.add(x)
    if x & 1:
        return collatz_check(3*x+1,visited)
    return collatz_check(x>>1,visited)


def worker(lower,upper):
    for i in range(lower,upper+1):
        if not collatz_check(i,set()):
            return False
    return True


def parallel_collatz(limit: int, max_workers: int=2, range_size: int=20) -> bool:
    if limit<1:
        return True
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures=[executor.submit(worker,start,min(limit,start+range_size-1))
                 for start in range(1,limit+1,range_size)]
        return all(future.result() for future in futures)


if __name__=='__main__':
    success=parallel_collatz(100,2,25)
    print('Collatz checks through 100:',success)
    assert success
