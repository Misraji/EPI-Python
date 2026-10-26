"""EPI Python — Exercise 19.6: The Readers-Writers Problem

Chapter 19: Parallel Computing
Textbook: pages 296–297 (printed page numbers; problem and hint on 296,
solution and the Reader/Writer program on 297).

PROBLEM (from the textbook)
---------------------------
Consider an object s which is read from and written to by many threads.
(For example, s could be the cache from Problem 19.1 on Page 291.) You need
to ensure that no thread may access s for reading or writing while another
thread is writing to s. (Two or more readers may access s at the same
time.)

One way to achieve this is by protecting s with a mutex that ensures that
two threads cannot access s at the same time. However, this solution is
suboptimal because it is possible that a reader R1 has locked s and
another reader R2 wants to access s. Reader R2 does not have to wait until
R1 is done reading; instead, R2 should start reading right away.

This motivates the first readers-writers problem: protect s with the added
constraint that no reader is to be kept waiting if s is currently opened
for reading.

Implement a synchronization mechanism for the first readers-writers
problem.

HINT (from the textbook)
------------------------
Track the number of readers.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
We must know whether the shared object (the book calls it "the string") is
being read or written, and, while it is being read, how many readers are
active. The book uses two locks — a read lock and a write lock — plus a
read counter protected by the read lock.

Reader:
  1. Lock the read lock, increment the counter, release the read lock.
  2. Perform the reads.
  3. Lock the read lock, decrement the counter, release the read lock.

Writer:
  1. Lock the write lock (so writers exclude each other).
  2. Repeatedly: lock the read lock and check whether the read counter is
     0; if so, perform the write, release the read lock and leave the loop.
  3. Release the write lock.

As in Solution 19.3 (page 293), wait/notify primitives are used so that a
writer sleeps instead of busy waiting: a reader that decrements the counter
notifies, and a writer that sees a nonzero count waits on the read lock
until the count drops to 0.

The book's program consists of two threading.Thread subclasses, Reader and
Writer, using class attributes LR (read lock), LW (write lock), read_count
and data of a class RW (not shown). This file instead provides a reusable
lock object, ReadersWritersLock, built on a different but standard
reader-preference scheme: the FIRST reader acquires the write lock on
behalf of all readers and the LAST reader releases it. See TEXTBOOK CODE
COMPARISON below.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
Two readers can hold the lock at once (acquire_read twice, then
release_read twice); afterwards a writer can acquire_write and
release_write.
"""

# Python standard library: thread-based parallelism.
# Module documentation: https://docs.python.org/3/library/threading.html
# Lock API: https://docs.python.org/3/library/threading.html#lock-objects
#           https://docs.python.org/3/library/threading.html#threading.Lock
import threading


class ReadersWritersLock:
    """Reader-preference solution from the book's first readers-writers problem.

    Not the book's Reader/Writer thread classes: a lock object with
    acquire_read/release_read for readers and acquire_write/release_write
    for writers. Readers never wait while other readers hold the lock.
    """

    def __init__(self):

        # Number of readers currently reading.
        self._read_count=0

        # threading.Lock() creates a mutual-exclusion lock that one thread
        # holds at a time. _count_lock protects _read_count (it plays the
        # role of the book's read lock LR).
        self._count_lock=threading.Lock()

        # _write_lock is held by a writer while writing, OR by the group of
        # active readers as a whole. Note: a plain Lock may be released by a
        # different thread than the one that acquired it, which this scheme
        # relies on (the last reader to leave may not be the first to come).
        self._write_lock=threading.Lock()

    def acquire_read(self):

        # `with lock:` acquires the lock and releases it at the end of the
        # block, even if an exception occurs.
        with self._count_lock:

            # The first reader in blocks writers by taking the write lock
            # (waiting here if a writer is active). Later readers just bump
            # the count and proceed immediately — no reader waits for
            # another reader.
            if self._read_count==0:

                # acquire() blocks until the lock is free, then takes it.
                self._write_lock.acquire()
            self._read_count+=1

    def release_read(self):
        with self._count_lock:
            self._read_count-=1

            # The last reader out lets writers in. release() frees the
            # lock; releasing an unlocked Lock raises RuntimeError.
            if self._read_count==0:
                self._write_lock.release()

    def acquire_write(self):

        # A writer needs the object exclusively: it waits until no writer
        # and no reader group holds the write lock.
        self._write_lock.acquire()

    def release_write(self):
        self._write_lock.release()


# TEXTBOOK POST-SOLUTION DISCUSSION (page 297)
# --------------------------------------------
# The book gives no further discussion or complexity analysis after the
# program. (Exercise 19.7, which follows, points out that in this solution a
# waiting writer can be overtaken by newly arriving readers and may starve.)
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Structure differs completely. Book: comment "LR and LW are class
#   attributes in the RW class. They serve as read and write locks. The
#   integer variable read_count in RW tracks the number of readers.", then
#   `class Reader(threading.Thread)` and `class Writer(threading.Thread)`,
#   each with an infinite `while True:` run() loop that reads/prints or
#   increments `RW.data` and calls `do_something_else()`. The RW class
#   itself is not shown in the book.
# - File: no Reader/Writer/RW classes; a single `ReadersWritersLock` class
#   with `_read_count`, `_count_lock`, `_write_lock` and methods
#   acquire_read, release_read, acquire_write, release_write.
# - Algorithm differs: in the book the writer holds LW and loops, under LR,
#   until read_count == 0, using `RW.LR.wait()` (and readers call
#   `RW.LR.notify()` after decrementing), so LR is used as a condition
#   variable. In the file the first reader acquires the write lock and the
#   last reader releases it; no wait/notify is used.
# - Both give reader preference (the first readers-writers problem).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # A single-threaded walk-through of the API (added). Two reads can be
    # held at the same time; after both are released a writer gets
    # exclusive access. `;` puts two statements on one line (legal,
    # uncommon style). No assert is used: the demo would block (hang)
    # rather than fail if the locking were wrong.
    rw=ReadersWritersLock()
    rw.acquire_read();rw.acquire_read()
    print('Two readers acquired shared access')
    rw.release_read();rw.release_read()
    rw.acquire_write();rw.release_write()
    print('Writer acquired exclusive access')
