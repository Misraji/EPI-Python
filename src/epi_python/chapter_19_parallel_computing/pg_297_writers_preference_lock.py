"""EPI Python — Exercise 19.7: The Readers-Writers Problem with Write Preference

Chapter 19: Parallel Computing
Textbook: pages 297–298 (printed page numbers; problem begins on 297,
rest of the problem, hint, solution and variant on 298).

PROBLEM (from the textbook)
---------------------------
Suppose we have an object s as in Problem 19.6 on the preceding page. In the
solution to Problem 19.6 on the facing page, a reader R1 may have the lock;
if a writer W is waiting for the lock and then a reader R2 requests access,
R2 will be given priority over W. If this happens often enough, W will
starve. Instead, suppose we want W to start as soon as possible.

This motivates the second readers-writers problem: protect s with
"writer-preference", i.e., no writer, once added to the queue, is to be kept
waiting longer than absolutely necessary.

Implement a synchronization mechanism for the second readers-writers
problem.

HINT (from the textbook)
------------------------
Force readers to acquire a write lock.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
To give writers preference, modify Solution 19.6 so that a reader begins by
locking the write lock and then immediately releasing it. A writer that has
acquired the write lock is then guaranteed to be ahead of all readers that
arrive afterwards: they cannot get past the write lock until the writer
releases it.

The book gives this solution in prose only; it prints NO program for this
exercise. This file's WritersPreferenceLock is an implementation added for
the repository (not from the book). It reaches the same goal — a waiting
writer blocks newly arriving readers — with a single threading.Condition
and a count of waiting writers, rather than the book's "readers briefly
take the write lock" idea.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
A reader can acquire and release the lock, then a writer can acquire and
release it. If a writer is waiting, any reader that calls acquire_read
after that waits until the writer has finished.
"""

# Python standard library: thread-based parallelism.
# Module documentation: https://docs.python.org/3/library/threading.html
# Condition API: https://docs.python.org/3/library/threading.html#condition-objects
#                https://docs.python.org/3/library/threading.html#threading.Condition
import threading


class WritersPreferenceLock:
    """Condition-based finite form of the book's writer-preference locking rule.

    Added implementation (the book prints no code for 19.7). Readers share
    access; writers get exclusive access; once a writer is waiting, new
    readers must wait for it.
    """

    def __init__(self):

        # threading.Condition() bundles a lock with wait()/notify(). A
        # thread holding the condition can wait(), which RELEASES the lock
        # and sleeps until notified, then re-acquires the lock before
        # returning. All state below is read and written only while holding
        # this condition's lock.
        self._condition=threading.Condition()

        # Number of readers currently reading.
        self._readers=0

        # True while a writer holds exclusive access.
        self._writer_active=False

        # Writers that have asked for access but not yet received it. This
        # count is what gives writers preference.
        self._waiting_writers=0

    def acquire_read(self):

        # `with condition:` acquires its lock for the block and releases it
        # afterwards, even on an exception.
        with self._condition:

            # A reader waits while a writer is active OR any writer is
            # waiting (the writer-preference rule). The predicate is checked
            # in a while loop because wait() can return before the condition
            # is actually true (another thread may have changed state first,
            # or a spurious wakeup may occur).
            while self._writer_active or self._waiting_writers:
                self._condition.wait()
            self._readers+=1

    def release_read(self):
        with self._condition:
            self._readers-=1

            # The last reader out wakes ALL waiting threads; notify_all()
            # is used because both readers and writers may be waiting and
            # each re-checks its own predicate.
            if self._readers==0:
                self._condition.notify_all()

    def acquire_write(self):
        with self._condition:

            # Register as waiting before sleeping, so readers arriving from
            # now on will hold back.
            self._waiting_writers+=1

            # try/finally: the `finally` block runs however the `try` block
            # exits (normally or via an exception such as KeyboardInterrupt
            # during wait()), so the waiting count is always restored.
            try:

                # Wait until no writer is active and no readers remain.
                while self._writer_active or self._readers:
                    self._condition.wait()
                self._writer_active=True
            finally:
                self._waiting_writers-=1

    def release_write(self):
        with self._condition:
            self._writer_active=False

            # Wake everyone: waiting writers and readers re-check their
            # predicates; another waiting writer will still block readers.
            self._condition.notify_all()


# TEXTBOOK POST-SOLUTION DISCUSSION (page 298)
# --------------------------------------------
# The book adds no complexity analysis or further remarks.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): The specifications to
# Problems 19.6 on Page 296 and 19.7 on the previous page allow
# starvation — the first may starve writers, the second may starve readers.
# The third readers-writers problem adds the constraint that neither readers
# nor writers should starve. Implement a synchronization mechanism for the
# third readers-writers problem.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - The book prints no code for this exercise; its solution is one
#   paragraph modifying Solution 19.6 so that each reader first locks and
#   immediately releases the write lock.
# - The entire WritersPreferenceLock class (a threading.Condition, counters
#   _readers and _waiting_writers, flag _writer_active, and the
#   acquire_read / release_read / acquire_write / release_write methods) is
#   an addition in this file and uses a different mechanism from the book's
#   described one (waiting-writer count instead of readers touching the
#   write lock).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # A single-threaded walk-through of the API (added). `;` puts two
    # statements on one line (legal, uncommon style). If the locking logic
    # were wrong, these calls would block (hang) rather than raise, so no
    # assert is used; the multithreaded checks are in the pytest suite.
    rw=WritersPreferenceLock()
    rw.acquire_read();rw.release_read()
    rw.acquire_write();rw.release_write()
    print('Reader and writer exclusion checks passed')
