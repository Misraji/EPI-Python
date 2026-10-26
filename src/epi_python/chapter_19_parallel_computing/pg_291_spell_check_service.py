"""EPI Python — Exercise 19.1: Implement Caching for a Multithreaded Dictionary

Chapter 19: Parallel Computing
Textbook: pages 291–292 (printed page numbers; problem, the flawed program,
hint, solution and most of the corrected program on 291; its last lines and
the variant on 292).

PROBLEM (from the textbook)
---------------------------
The program below is part of an online spell correction service. Clients
send as input a string, and the service returns an array of strings in its
dictionary that are closest to the input string (this array could be
computed, for example, using Solution 16.2 on Page 239). The service caches
results to improve performance. Critique the implementation and provide a
solution that overcomes its limitations.

(The book then prints the program to critique: a class SpellCheckService
with class attributes w_last and closest_to_last_word, both None, and a
static method service(req, resp). It extracts the word w from the request;
if w differs from w_last it sets w_last = w and recomputes
closest_to_last_word = closest_in_dictionary(w); finally it encodes
closest_to_last_word into the response. There is no locking.)

HINT (from the textbook)
------------------------
Look for races, and lock as little as possible to avoid reducing
throughput.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
1. The original program has a race condition. Example: clients A and B send
   requests at the same time and the service starts one thread per request.
   A's thread finds its input string in the cache; right after that check,
   B's thread runs, misses the cache, computes its result and stores it. If
   the cache is full, some entry is evicted — possibly the one for A's
   string. When A's thread resumes and reads the value it "knows" is
   there, the cache returns null.

2. One thread-safe fix: synchronize every call to the service. Then only
   one thread runs the method at a time and cache reads and writes cannot
   race. But performance is poor: only one service call can execute at a
   time.

3. The book's fix: lock only the code that touches the cached values —
   the check of the cached value, and the updates to it. Several threads
   can then compute closest strings concurrently, which is good because
   that computation is slow (the very reason results are cached). The lock
   makes the read on a hit and the write on completion atomic. On a hit
   the cached array is COPIED inside the lock, so the caller gets its own
   list that a later update cannot disturb.

This file implements the corrected program only (as an instance-based
class with an injected lookup function); the original, racy program is
described above but not included (see TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
With a stand-in lookup `lambda w: [w.upper()]`, service('hello') returns
['HELLO']; a second call with 'hello' is answered from the cache with a
copy of the stored list.
"""

# Python standard library: thread-based parallelism.
# Module documentation: https://docs.python.org/3/library/threading.html
# Lock API: https://docs.python.org/3/library/threading.html#lock-objects
#           https://docs.python.org/3/library/threading.html#threading.Lock
import threading


class SpellCheckService:
    """PDF algorithm; inject callable lookup in place of the book's undefined HTTP service.

    This is the textbook's CORRECTED SpellCheckService (lock only around
    cache access). closest_in_dictionary must be a function taking a word
    and returning a list (anything with a .copy() method).
    """

    def __init__(self, closest_in_dictionary):

        # The expensive function that computes the closest dictionary words.
        # A leading underscore marks an attribute as internal by convention
        # (Python does not enforce privacy).
        self._lookup = closest_in_dictionary

        # The one-entry cache: the last word looked up and its result.
        self._last_word = None
        self._closest_to_last_word = None

        # threading.Lock() creates a mutual-exclusion lock. Only one thread
        # can hold it at a time; others trying to acquire it wait. It is
        # NOT reentrant: the same thread acquiring it twice would deadlock.
        self._lock = threading.Lock()

    def service(self, word):
        """Return the closest words for `word`, using the one-entry cache."""
        result = None

        # `with lock:` acquires the lock at the start of the block and
        # releases it automatically at the end, even if an exception occurs
        # (the lock is a context manager). Only the cache CHECK is locked.
        with self._lock:
            if word == self._last_word:

                # list.copy() makes a shallow copy, so the caller receives
                # its own list, unaffected by later cache updates.
                result = self._closest_to_last_word.copy()

        # Cache miss: do the slow computation WITHOUT holding the lock, so
        # other threads can serve requests (or compute) concurrently.
        if result is None:
            result = self._lookup(word)

            # Lock again only to update the two cache fields together, so no
            # other thread can see the new word paired with the old result.
            with self._lock:
                self._last_word = word
                self._closest_to_last_word = result.copy()
        return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 292)
# --------------------------------------------
# The book gives no complexity analysis for this exercise; its discussion is
# the critique and fix described in the module docstring.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Threads 1 to n execute a
# method called critical(). Before this, they execute a method called
# rendezvous(). The synchronization constraint is that only one thread can
# execute critical() at a time, and all threads must have completed
# executing rendezvous() before critical() can be called. You can assume n
# is stored in a variable n that is accessible from all threads. Design a
# synchronization mechanism for the threads. All threads must execute the
# same code. Threads may call critical() multiple times, and you should
# ensure that a thread cannot call critical() a (k + 1)th time until all
# other threads have completed their kth calls to critical().


# TEXTBOOK CODE COMPARISON
# ------------------------
# - The book's first (racy) SpellCheckService is not in this file; only the
#   corrected version is implemented.
# - Book: class attributes `w_last = closest_to_last_word = None` and
#   `lock = threading.Lock()` shared by all callers, with
#   `@staticmethod def service(req, resp)`. File: per-instance attributes
#   `_last_word`, `_closest_to_last_word`, `_lock`, set in a new
#   `__init__(self, closest_in_dictionary)`; `service(self, word)` is an
#   ordinary method.
# - I/O: the book reads the word with
#   `req.extract_word_to_check_from_request()` and writes the answer with
#   `resp.encode_into_response(result)`; the file takes `word` directly and
#   RETURNS the result.
# - Lookup: the book calls a global `closest_in_dictionary(w)`; the file
#   calls the injected `self._lookup(word)`.
# - Cache write: the book stores `closest_to_last_word = result`; the file
#   stores `result.copy()`.
# - The locking structure (copy under lock on a hit; compute outside the
#   lock; update both fields under the lock) matches the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # A lambda is a small anonymous function: `lambda w: [w.upper()]` takes
    # a word and returns a one-element list. It stands in for the real
    # (slow) dictionary search. This demo is single-threaded; it shows the
    # API and the cache, not concurrency.
    checker=SpellCheckService(lambda w: [w.upper()])
    print('Corrections:',checker.service('hello'))

    # The second call is a cache hit. `assert` raises AssertionError if the
    # condition is False; pytest does the thorough testing.
    assert checker.service('hello')==['HELLO']
