"""EPI Python — Exercise 19.9: Test the Collatz Conjecture in Parallel

Chapter 19: Parallel Computing
Textbook: pages 298–299 (printed page numbers; the problem starts at the
bottom of 298; the rest of the problem, hint, solution and program are on
299).

PROBLEM (from the textbook)
---------------------------
In Problem 12.11 on Page 176 and its solution we introduced the Collatz
conjecture and heuristics for checking it. In this problem, you are to
build a parallel checker for the Collatz conjecture. Specifically, assume
your program will run on a multicore machine, and threads in your program
will be distributed across the cores. Your program should check the Collatz
conjecture for every integer in [1, U] where U is an input to your program.

Design a multi-threaded program for checking the Collatz conjecture. Make
full use of the cores available to you. To keep your program from
overloading the system, you should not have more than n threads running at
a time.

(Reminder, not quoted: the Collatz conjecture says that repeatedly
replacing x by 3x + 1 if x is odd, or by x / 2 if x is even, always reaches
1.)

HINT (from the textbook)
------------------------
Use multithreading for performance—take care to minimize threading
overhead.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Heuristics for pruning the check of an individual integer are in Solution
12.11 (page 176). The point here is the multi-threaded structure.

1. One thread per number: a master thread launches n threads for the
   numbers 1, 2, ..., n, tracks which number is next, and gives it to
   whichever thread finishes. Problem: checking one number takes very
   little time compared with the overhead of communicating with a thread.

2. Fixed subranges: divide [1, U] into n equal subranges and let thread i
   handle the i-th one. Problem: some integers take much longer to check
   than others, so one thread may take far longer than the rest, leaving
   most cores idle.

3. Compromise (the book's choice): give threads smaller intervals that are
   still large enough to outweigh the thread overhead. Keep a work queue
   of unprocessed intervals and hand them to threads as they return. The
   book does this with the library pool, concurrent.futures
   .ProcessPoolExecutor(max_workers=NTHREADS), which performs the task
   assignment and load balancing; each submitted task is
   worker(lower, upper) for one interval of size RANGESIZE.

The book's program has worker(lower, upper), collatz_check(x, visited),
and a top-level loop submitting the intervals. This file has the same two
functions (worker changed to return a bool) plus a driver
parallel_collatz(limit, max_workers, range_size).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
parallel_collatz(100, 2, 25) checks 1..100 in four intervals
([1, 25], [26, 50], [51, 75], [76, 100]) on 2 worker processes and returns
True.
"""

# Python standard library: high-level interface for running callables
# asynchronously on pools of threads or processes.
# Module documentation: https://docs.python.org/3/library/concurrent.futures.html
# ProcessPoolExecutor API: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor
# Executor.submit / Future.result: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.submit
#                                  https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.result
from concurrent.futures import ProcessPoolExecutor


def collatz_check(x,visited):
    """Check one number (textbook collatz_check).

    Returns True if the sequence from x reaches 1, False if it revisits a
    number (a cycle that would disprove the conjecture). `visited` is the
    set of numbers already seen on this sequence.
    """
    if x==1:
        return True

    # `in` on a set is an average O(1) membership test.
    if x in visited:
        return False
    visited.add(x)

    # `x & 1` is bitwise AND with 1: it is 1 (truthy) exactly when the
    # lowest bit is set, i.e. x is odd (book comment: "odd number").
    if x & 1:
        return collatz_check(3*x+1,visited)

    # Even number: `x >> 1` shifts the bits right by one place, which for a
    # non-negative int equals x // 2 (book comment: "divide by 2"). Python
    # ints are unbounded, so 3x + 1 never overflows.
    #
    # Note: this is recursive, one call per step; Python's default
    # recursion limit (about 1000) is far above the Collatz sequence lengths
    # for small inputs.
    return collatz_check(x>>1,visited)


def worker(lower,upper):
    """Check every integer in [lower, upper] (textbook worker, as a bool).

    Book comment: "Performs basic unit of work". This is the function run
    in each pool process; it must be defined at module top level so it can
    be pickled and sent to the worker processes.
    """

    # range(lower, upper + 1) includes upper. A fresh set() is used for each
    # starting number.
    for i in range(lower,upper+1):
        if not collatz_check(i,set()):
            return False
    return True


# Type hints (`limit: int`, `max_workers: int=2`, `range_size: int=20`,
# `-> bool`) document the parameters; Python does not enforce them.
def parallel_collatz(limit: int, max_workers: int=2, range_size: int=20) -> bool:
    """Check [1, limit] using a bounded process pool (driver added here).

    Plays the role of the book's top-level submission loop, with
    max_workers ~ NTHREADS and range_size ~ RANGESIZE.
    """

    # Nothing to check for an empty range.
    if limit<1:
        return True

    # ProcessPoolExecutor(max_workers=k) runs tasks in at most k separate
    # PROCESSES (not threads). Separate processes each have their own
    # Python interpreter, so CPU-bound work like this really runs in
    # parallel on multiple cores; threads in CPython are limited by the
    # global interpreter lock. Arguments and results are pickled between
    # processes.
    #
    # The `with` block shuts the pool down at the end, waiting for all
    # submitted tasks to finish (book comment: "Uses the library thread pool
    # for task assignment and load balancing").
    with ProcessPoolExecutor(max_workers=max_workers) as executor:

        # One task per interval: range(1, limit+1, range_size) yields the
        # interval starts 1, 1+range_size, ...; min(...) clips the last
        # interval at limit. executor.submit returns a Future for each.
        # Idle processes pick up waiting intervals, which is the load
        # balancing the book wants.
        futures=[executor.submit(worker,start,min(limit,start+range_size-1))
                 for start in range(1,limit+1,range_size)]

        # future.result() waits for that task and returns its bool (or
        # re-raises its exception). all() returns True only if every
        # interval passed, stopping at the first False.
        return all(future.result() for future in futures)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 299)
# --------------------------------------------
# The book's discussion is the comparison of the three work-distribution
# strategies in the module docstring; it gives no complexity analysis.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - collatz_check: matches the book (same name, parameters and logic); the
#   book's comments "Checks an individual number", "odd number", "even
#   number" and "divide by 2" are reflected in the new comments.
# - worker: book body `assert collatz_check(i, set())` for each i, then
#   `print('(%d,%d)' % (lower, upper))`; file returns False on the first
#   failure and True otherwise, with no assert and no print.
# - Submission: the book uses a top-level snippet with
#   `executor = concurrent.futures.ProcessPoolExecutor(max_workers=NTHREADS)`,
#   `with executor:` and
#   `for i in range(N // RANGESIZE): executor.submit(worker,
#   i * RANGESIZE + 1, (i + 1) * RANGESIZE)` (N, NTHREADS, RANGESIZE not
#   defined in the listing). The file adds
#   `parallel_collatz(limit, max_workers=2, range_size=20)`, which builds
#   the executor in the `with` statement, clips the last interval with
#   min(limit, ...) (the book's loop drops a final partial interval when
#   N is not a multiple of RANGESIZE), and returns the combined result.
# - Import: book `concurrent.futures.ProcessPoolExecutor`; file
#   `from concurrent.futures import ProcessPoolExecutor`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# For ProcessPoolExecutor this guard is also REQUIRED on platforms that
# start worker processes by re-importing this module (e.g. Windows, macOS):
# without it each worker would try to start its own pool.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Check 1..100 with 2 worker processes and intervals of 25 numbers.
    success=parallel_collatz(100,2,25)
    print('Collatz checks through 100:',success)

    # `assert` raises AssertionError if the check failed.
    assert success
