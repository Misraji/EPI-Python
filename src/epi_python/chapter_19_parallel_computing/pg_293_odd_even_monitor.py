"""EPI Python — Exercise 19.3: Implement Synchronization for Two Interleaving
Threads

Chapter 19: Parallel Computing
Textbook: pages 293–294 (printed page numbers; problem, hint, solution and
the start of OddEvenMonitor on 293; the rest of the program on 294).

PROBLEM (from the textbook)
---------------------------
Thread t1 prints odd numbers from 1 to 100; Thread t2 prints even numbers
from 1 to 100.

Write code in which the two threads, running concurrently, print the
numbers from 1 to 100 in order.

HINT (from the textbook)
------------------------
The two threads need to notify each other when they are done.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: a lock that the two threads repeatedly acquire, guarding a
single variable recording which thread went last. Its drawback is the busy
waiting antipattern: a thread keeps grabbing the lock just to discover it
is not its turn, wasting processor time that could run some other task.

The book's solution keeps the same idea (a shared "whose turn" variable)
but avoids busy locking by using a condition variable: the book's class
OddEvenMonitor subclasses threading.Condition. A thread waits (sleeping,
not spinning) until it is its turn, prints, flips the turn and notifies the
other thread. (The book's sentence introducing the program runs straight
into the code listing: it avoids busy locking "by using" the class shown.)

The book's program has three classes: OddEvenMonitor (ODD_TURN = True,
EVEN_TURN = False, turn, wait_turn, toggle_turn), OddThread and EvenThread
(threading.Thread subclasses whose run() loops over the odd / even numbers
1..100). This file keeps those classes, generalised with an output callback
and a limit, plus a driver function print_in_order.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
print_in_order(20) collects the numbers emitted by the two threads and
returns [1, 2, 3, ..., 20], in order, every time.
"""

# Python standard library: thread-based parallelism.
# Module documentation: https://docs.python.org/3/library/threading.html
# Condition API: https://docs.python.org/3/library/threading.html#condition-objects
# Thread API: https://docs.python.org/3/library/threading.html#thread-objects
import threading


class OddEvenMonitor(threading.Condition):
    """The textbook's monitor: a Condition plus a shared 'whose turn' flag.

    threading.Condition combines a lock with wait/notify. A thread holding
    the lock can call wait(), which RELEASES the lock and sleeps until
    another thread calls notify(); on waking it re-acquires the lock before
    wait() returns. Subclassing it lets the monitor itself be used in
    `with self:` and to call self.wait() / self.notify().
    """

    # Class attributes naming the two turns (True for odd, False for even).
    ODD_TURN=True
    EVEN_TURN=False

    def __init__(self):

        # super().__init__() runs threading.Condition's own constructor,
        # which creates the underlying lock. Without it the object would not
        # work as a Condition.
        super().__init__()

        # Odd goes first (1 is printed first).
        self.turn=self.ODD_TURN

    def wait_turn(self,old_turn):
        """Block until it is `old_turn`'s turn (book method name)."""

        # `with self:` acquires the condition's lock and releases it at the
        # end of the block, even on an exception.
        with self:

            # Re-check the predicate in a LOOP: wait() may return even
            # though the turn has not changed (e.g. a spurious wakeup), so
            # a thread must test again before proceeding.
            while self.turn!=old_turn:
                self.wait()

    def toggle_turn(self):
        """Hand the turn to the other thread and wake it (book method)."""
        with self:

            # `^=` is in-place XOR. For bools, True ^ True is False and
            # False ^ True is True, so this flips the turn.
            self.turn ^= True

            # notify() wakes one thread waiting on this condition (it must
            # be called while holding the lock). The woken thread runs once
            # this `with` block releases the lock.
            self.notify()


class OddThread(threading.Thread):
    """Emits odd numbers when it is the odd turn (textbook OddThread)."""

    # Subclassing threading.Thread: the code to run goes in run(), which is
    # invoked in the new thread when start() is called.
    def __init__(self,monitor,emit,limit):

        # The Thread base class must be initialised before use.
        super().__init__()

        # Tuple unpacking assigns three attributes in one statement. emit is
        # the output callback (the book prints directly); limit replaces the
        # book's fixed 100.
        self.monitor,self.emit,self.limit=monitor,emit,limit

    def run(self):

        # range(start, stop, step): 1, 3, 5, ... up to limit (stop is
        # exclusive, hence limit + 1).
        for i in range(1,self.limit+1,2):
            self.monitor.wait_turn(OddEvenMonitor.ODD_TURN)
            self.emit(i)
            self.monitor.toggle_turn()


class EvenThread(threading.Thread):
    """Emits even numbers when it is the even turn (textbook EvenThread)."""

    def __init__(self,monitor,emit,limit):
        super().__init__()
        self.monitor,self.emit,self.limit=monitor,emit,limit

    def run(self):

        # 2, 4, 6, ... up to limit.
        for i in range(2,self.limit+1,2):
            self.monitor.wait_turn(OddEvenMonitor.EVEN_TURN)
            self.emit(i)
            self.monitor.toggle_turn()


def print_in_order(limit=100):
    """Run both threads and return the numbers in the order emitted.

    Driver added in this file (the book shows only the classes). The
    default limit=100 matches the book's 1..100.
    """
    monitor=OddEvenMonitor()
    result=[]

    # `result.append` is a BOUND METHOD: passing it as `emit` means
    # emit(i) appends i to this result list. Only one thread emits at a
    # time (they alternate turns), so the appends happen in order.
    odd=OddThread(monitor,result.append,limit)
    even=EvenThread(monitor,result.append,limit)

    # start() launches each thread's run(); join() waits for each to
    # finish. `;` puts two statements on one line (legal, uncommon style).
    odd.start();even.start()
    odd.join();even.join()
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 294)
# --------------------------------------------
# The book gives no further discussion or complexity analysis after the
# program.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - OddEvenMonitor: matches the book (ODD_TURN/EVEN_TURN, __init__,
#   wait_turn with a while/wait loop, toggle_turn with `^= True` and
#   notify()).
# - OddThread / EvenThread: book constructors take only `monitor`; file
#   takes `monitor, emit, limit`. Book run() loops `range(1, 101, 2)` /
#   `range(2, 101, 2)` and calls `print(i)`; file loops up to `limit` and
#   calls `self.emit(i)`.
# - The file adds `print_in_order(limit=100)`, which creates and runs the
#   threads and returns the collected list; the book shows no driver code.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Run the two threads for 1..20 (smaller than the book's 100 to keep
    # the output short).
    output=print_in_order(20)
    print('Ordered output:',output)

    # list(range(1, 21)) is [1, 2, ..., 20]. `assert` raises
    # AssertionError if the threads ever produced a different order.
    assert output==list(range(1,21))
