"""EPI Python — Exercise 19.8: Implement a Timer Class

Chapter 19: Parallel Computing
Textbook: page 298 (printed page number; problem, hint and solution are all
on 298).

PROBLEM (from the textbook)
---------------------------
Consider a web-based calendar in which the server hosting the calendar has
to perform a task when the next calendar event takes place. (The task could
be sending an email or a Short Message Service (SMS).) Your job is to design
a facility that manages the execution of such tasks.

Develop a timer class that manages the execution of deferred tasks. The
timer constructor takes as its argument an object which includes a run
method and a string-valued name field. The class must support—(1.) starting
a thread, identified by name, at a given time in the future; and (2.)
canceling a thread, identified by name (the cancel request is to be ignored
if the thread has already started).

HINT (from the textbook)
------------------------
There are two aspects—data structure design and concurrency.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The design has two parts: the data structures and the locking mechanism.

Data structure 1 — a min-heap of key-value pairs: the key is a run time and
the value is the thread to run at that time. A dispatch thread runs these
threads:
  - It sleeps from one call to the next, and may be woken up when a thread
    is added to or deleted from the pool. When woken, it lengthens or
    shortens its remaining sleep according to the top of the min-heap.
  - On waking, it looks at the thread at the top of the heap; if its launch
    time is now, it removes it from the heap and runs it. It then sleeps
    until the launch time of the next thread in the heap.
  - Because of deletions, the dispatch thread may wake up and find nothing
    to do.

Data structure 2 — a hash table mapping thread ids to their entries in the
min-heap. To cancel a thread, look it up and delete it from the min-heap.
Each time a thread is added, it is inserted into the min-heap; if it lands
at the top of the heap, the dispatch thread is interrupted so it can adjust
its wake-up time.

Locking: the min-heap is shared by the update methods and the dispatch
thread, so it must be locked. The simplest solution is a single lock used
for all reads and writes of the min-heap and the hash table.

The book describes this design in prose only and prints no program. This
file's Timer class is an implementation of that design added for the
repository: a heapq min-heap, a dict keyed by task name, one
threading.Condition serving as the single lock (and as the way to wake the
dispatcher), and a dispatch thread. See TEXTBOOK CODE COMPARISON below.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
Scheduling a task named 'say-hello' with zero delay runs its callback
almost immediately on a new thread; timer.close() then stops the
dispatcher.
"""

# Python standard library: heap queue (priority queue) algorithm.
# Module documentation: https://docs.python.org/3/library/heapq.html
# heappush: https://docs.python.org/3/library/heapq.html#heapq.heappush
# heappop:  https://docs.python.org/3/library/heapq.html#heapq.heappop
import heapq

# Python standard library: thread-based parallelism.
# Module documentation: https://docs.python.org/3/library/threading.html
# Condition: https://docs.python.org/3/library/threading.html#condition-objects
# Thread:    https://docs.python.org/3/library/threading.html#thread-objects
# Event (used in __main__): https://docs.python.org/3/library/threading.html#event-objects
import threading

# Python standard library: time access and conversions.
# Module documentation: https://docs.python.org/3/library/time.html
# monotonic: https://docs.python.org/3/library/time.html#time.monotonic
import time


class Timer:
    """Finite, closable implementation of the book's named-task timer design.

    Not printed in the book: an added implementation of the textbook's
    min-heap + hash-table + single-lock + dispatch-thread design. Tasks are
    given as (name, callback, delay_seconds) rather than an object with run
    and name.
    """

    def __init__(self):

        # threading.Condition() is a lock plus wait()/notify(). It is the
        # book's "single lock" guarding the heap and the table, and it also
        # lets other methods wake the sleeping dispatcher (the book's
        # "interrupt the dispatch thread").
        self._condition=threading.Condition()

        # The min-heap: a plain list kept in heap order by heapq functions.
        # Entries are tuples (deadline, sequence, name, callback). Tuples
        # compare element by element, so the earliest deadline is at
        # _heap[0]; the unique sequence number breaks ties so the names and
        # callbacks are never compared.
        self._heap=[]

        # The hash table: task name -> its heap entry (the same tuple
        # object). A heap entry whose name no longer maps to it is stale
        # (cancelled) and is skipped lazily by the dispatcher instead of
        # being removed from the middle of the heap.
        self._scheduled={}
        self._sequence=0
        self._closed=False

        # Threads started for tasks, remembered so close() can join them.
        self._launched=[]

        # threading.Thread(target=f, daemon=True) prepares a thread running
        # f. daemon=True means the thread will not keep the program alive
        # at exit. start() begins running it.
        self._dispatcher=threading.Thread(target=self._dispatch,daemon=True)
        self._dispatcher.start()

    def schedule(self,name,callback,delay_seconds):
        """Run callback() on a new thread after delay_seconds (book op 1)."""

        # `with condition:` holds the single lock for the whole update.
        with self._condition:

            # `raise` stops with an exception: no scheduling after close(),
            # and names must be unique because tasks are identified by name.
            if self._closed:
                raise RuntimeError('timer already closed')
            if name in self._scheduled:
                raise ValueError('task name already scheduled')
            self._sequence+=1

            # time.monotonic() returns seconds from a clock that never goes
            # backwards (unaffected by system clock changes), so it is the
            # right clock for deadlines. Only differences between its values
            # are meaningful.
            item=(time.monotonic()+delay_seconds,self._sequence,name,callback)
            self._scheduled[name]=item

            # heapq.heappush(heap, item) inserts item and restores the heap
            # property in O(log n) time.
            heapq.heappush(self._heap,item)

            # notify() wakes the dispatcher (if waiting) so it can recompute
            # its sleep time in case this task is now the earliest.
            self._condition.notify()

    def cancel(self,name):
        """Cancel a not-yet-started task by name (book op 2).

        Returns True if a pending task was cancelled, False if the name was
        unknown or the task had already started (the request is ignored).
        """
        with self._condition:

            # dict.pop(key, default) removes and returns the value, or
            # returns default (None) if the key is absent — no KeyError.
            # `is not None` turns the outcome into a bool. The heap entry is
            # left in place and discarded later by the dispatcher.
            found=self._scheduled.pop(name,None) is not None
            self._condition.notify()
            return found

    def _dispatch(self):
        """The dispatch thread's loop (book: the dispatch thread)."""
        while True:
            with self._condition:
                while True:
                    if self._closed:
                        return

                    # Discard stale (cancelled) entries at the top of the
                    # heap. dict.get(key) returns None for a missing key;
                    # `is not` compares object identity, so an entry counts
                    # as live only if the table still maps its name to THIS
                    # exact tuple.
                    while self._heap and self._scheduled.get(self._heap[0][2]) is not self._heap[0]:

                        # heapq.heappop(heap) removes and returns the
                        # smallest entry in O(log n) time.
                        heapq.heappop(self._heap)

                    # Nothing scheduled: sleep until schedule/cancel/close
                    # calls notify(). wait() releases the lock while
                    # sleeping and re-acquires it on waking; `continue`
                    # re-checks everything from the top.
                    if not self._heap:
                        self._condition.wait()
                        continue

                    # Time left until the earliest deadline.
                    remaining=self._heap[0][0]-time.monotonic()

                    # Too early: sleep at most `remaining` seconds.
                    # wait(timeout=...) returns on notify() OR when the
                    # timeout expires; either way the loop re-checks, which
                    # handles insertions of earlier tasks and cancellations.
                    if remaining>0:
                        self._condition.wait(timeout=remaining)
                        continue

                    # The earliest task is due: remove it from both data
                    # structures. Tuple unpacking splits the entry into its
                    # four fields.
                    deadline,seq,name,callback=heapq.heappop(self._heap)
                    self._scheduled.pop(name,None)

                    # Start the task on its own thread, as the problem asks
                    # ("starting a thread"), so a slow task never delays
                    # the dispatcher.
                    worker=threading.Thread(target=callback)
                    self._launched.append(worker)
                    worker.start()
                    break

    def close(self):
        """Stop the dispatcher and wait briefly for started tasks (added)."""
        with self._condition:
            self._closed=True

            # dict.clear() removes all pending tasks.
            self._scheduled.clear()

            # notify_all() wakes every waiting thread (here, the dispatcher)
            # so it sees _closed and returns.
            self._condition.notify_all()

        # join(timeout=2) waits up to 2 seconds for each thread to finish;
        # it returns either way, so close() cannot hang forever.
        self._dispatcher.join(timeout=2)
        for thread in self._launched:
            thread.join(timeout=2)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 298)
# --------------------------------------------
# The book's solution ends with the single-lock remark; there is no
# complexity analysis or further discussion.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - The book prints NO code for this exercise; the whole Timer class is an
#   addition in this file, following the book's described design (min-heap
#   keyed by run time, hash table keyed by thread id/name, a single lock,
#   a dispatch thread that sleeps until the next launch time and is woken
#   when the heap changes).
# - Interface differences from the problem statement: the problem's
#   constructor takes an object with a run method and a name field; this
#   Timer's constructor takes no arguments and tasks are passed to
#   `schedule(name, callback, delay_seconds)` as a name, a callable and a
#   relative delay (not an absolute time).
# - Design details not in the book: cancelled entries are removed lazily
#   (left in the heap and skipped), a sequence number breaks deadline ties,
#   duplicate names raise ValueError, and `close()` shuts the timer down.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # threading.Event() is a thread-safe flag: set() turns it on, and
    # wait(timeout) blocks until it is on or the timeout passes, returning
    # True if the flag was set. Passing the bound method seen.set as the
    # callback lets us observe that the task ran.
    seen=threading.Event()
    timer=Timer()
    timer.schedule('say-hello',seen.set,0)

    # `assert` raises AssertionError if the task did not run within 1 s.
    assert seen.wait(1)
    timer.close()
    print('Named task executed successfully')
