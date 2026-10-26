"""EPI Python — Exercise 19.2: Analyze Two Unsynchronized Interleaved Threads

Chapter 19: Parallel Computing
Textbook: pages 292–293 (printed page numbers; problem, program, hint and
start of the solution on 292; the rest of the argument, the worst-case
schedule and Figure 19.1 on 293).

PROBLEM (from the textbook)
---------------------------
Threads t1 and t2 each increment an integer variable N times, as shown in
the code below. This program yields nondeterministic results. Usually, it
prints 2N but sometimes it prints a smaller value. The problem is more
pronounced for large N. As a concrete example, on one run the program
output 1320209 when N = 1000000 was specified at the command line.

(The book's program: module-level N = 1000000 and counter = 0; a function
increment_thread() that declares `global counter` and runs
`counter = counter + 1` N times; two threading.Thread objects t1 and t2
with target=increment_thread, both started, both joined, then
print(counter).)

What are the maximum and minimum values that could be printed by the
program as a function of N?

HINT (from the textbook)
------------------------
Be as perverse as you can when scheduling the threads.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The increment is unguarded, so the final value depends on the order in
which the thread scheduler runs the threads' reads and writes.
(`counter = counter + 1` is a read, an add and a write; another thread can
run between the read and the write, and its updates are then overwritten.)

Maximum: 2N, when the scheduler runs one thread to completion and then the
other.

Minimum:
  - N = 1: the minimum is 1. t1 reads 0, t2 reads 0, t1 increments and
    writes 1, then t2 increments and writes 1.
  - N > 1: the final value is at least 2. Two cases:
      * Some thread T does read-increment-write-read-increment-write with no
        write by the other thread between its two reads; then the value it
        writes is at least 2. If the other thread later writes 1, that
        thread has not finished, so it increments at least once more.
      * Otherwise T's second read returns 1 or more (the other thread has
        written at least once), so T's final write is at least 2.

The lower bound 2 is achieved by this schedule (book Figure 19.1,
"Worst-case schedule for two unsynchronized threads"):
  1. t1 loads the counter value, 0.
  2. t2 runs its loop N - 1 times.
  3. t1, unaware of the change, writes 1.
  4. t2 loads the counter value, 1.
  5. t1 runs its remaining N - 1 iterations.
  6. t2, unaware of the change, writes 2 to the counter.

So the program can print any value from 2 (for N > 1) up to 2N, depending
on scheduling. This file wraps the book's program in a function,
run_unsynchronized_increments(n), so it can be called and tested.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
run_unsynchronized_increments(10000) returns some value no larger than
20000. On CPython, the global interpreter lock and thread switch interval
often make it exactly 20000 for small n, but that is NOT guaranteed — the
analysis above still applies.
"""

# Python standard library: thread-based parallelism.
# Module documentation: https://docs.python.org/3/library/threading.html
# Thread API: https://docs.python.org/3/library/threading.html#threading.Thread
#             https://docs.python.org/3/library/threading.html#thread-objects
import threading


# Type hints: `n: int` and `-> int`. Python does not enforce annotations.
def run_unsynchronized_increments(n: int) -> int:
    """Run the textbook's two unsynchronized incrementing threads.

    Returns the final counter value, which can be anywhere from 2 (for
    n > 1) up to 2n depending on how the threads interleave.
    """

    # The shared variable both threads update (the book's global counter).
    counter = 0

    def increment_thread():

        # `nonlocal counter` makes the assignment below rebind the
        # enclosing function's `counter` instead of creating a new local
        # variable. (The book uses `global counter` for a module-level
        # variable; nonlocal is the equivalent for a nested function.)
        nonlocal counter

        # `_` is a conventional name for a loop variable that is not used.
        for _ in range(n):

            # NOT atomic: read counter, add 1, write counter. If the other
            # thread writes in between, one of the updates is lost. This
            # line is deliberately left unsynchronized; a threading.Lock
            # around it would make the result always 2n.
            counter = counter + 1

    # threading.Thread(target=f) creates a thread object that will run f()
    # in a separate thread. Creating it does not start it.
    t1=threading.Thread(target=increment_thread)
    t2=threading.Thread(target=increment_thread)

    # start() begins running the thread's target concurrently with the
    # current thread; each Thread may be started only once.
    t1.start()
    t2.start()

    # join() blocks until that thread finishes, so both loops are complete
    # before the counter is read.
    t1.join()
    t2.join()
    return counter


# TEXTBOOK POST-SOLUTION DISCUSSION (page 293)
# --------------------------------------------
# The whole solution is the max/min analysis in the module docstring:
# maximum 2N; minimum 1 when N = 1 and 2 when N > 1, achieved by the
# schedule of Figure 19.1.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: a top-level script with module globals `N = 1000000` and
#   `counter = 0`, `def increment_thread():` using `global counter`, two
#   module-level threads, and `print(counter)` at the end.
# - File: everything is wrapped in
#   `def run_unsynchronized_increments(n: int) -> int:`; `counter` is a
#   local of that function, `increment_thread` is nested and uses
#   `nonlocal counter`, N becomes the parameter `n`, and the value is
#   RETURNED instead of printed (the __main__ block prints it).
# - The increment statement and the Thread start/join sequence match the
#   book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Run the two racing threads with n = 10000 (much smaller than the
    # book's 1000000, to keep the demo quick).
    result=run_unsynchronized_increments(10000)
    print('Unprotected counter after two threads:',result)

    # Chained comparison: 0 <= result <= 20000. The result is
    # nondeterministic, so only a range can be checked. `assert` raises
    # AssertionError if the condition is False.
    assert 0<=result<=20000
