"""EPI Python — Exercise 19.5: Deadlock

Chapter 19: Parallel Computing
Textbook: pages 295–296 (printed page numbers; problem and the start of the
Account program on 295; the rest of the program, the solution and the
corrected lines on 296).

PROBLEM (from the textbook)
---------------------------
When threads need to acquire multiple locks to enter a critical section,
deadlock can result. As an example, suppose both T1 and T2 need to acquire
locks L and M. If T1 first acquires L, and then T2 then acquires M, they
end up waiting on each other forever.

Identify a concurrency bug in the program below, and modify the code to
resolve the issue.

(The book's program: class Account with a class counter _global_id = 0;
__init__(self, balance) stores _balance, takes the next _id from
_global_id and increments it, and creates self._lock = threading.RLock();
get_balance(self) returns _balance; a @staticmethod
transfer(acc_from, acc_to, amount) starts a threading.Thread whose target
is acc_from._move with args (acc_to, amount); and _move(self, acc_to,
amount), inside `with self._lock:`, returns False if amount exceeds the
balance, otherwise adds amount to acc_to._balance, subtracts it from
self._balance, prints 'returning True' and returns True.)

(The book prints no hint for this exercise.)

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
1. The bug: suppose U1 starts a transfer to U2 and, immediately afterwards,
   U2 starts a transfer to U1. Each transfer runs in its own thread, so the
   first thread can lock U1 and then the second thread can be scheduled
   and lock U2. Now each thread waits for the lock the other holds:
   deadlock.

2. One fix: a single global lock taken by the transfer method. Drawback:
   it blocks unrelated transfers — e.g. U3 cannot transfer to U4 while a
   transfer from U5 to U6 is pending.

3. The canonical fix: impose a global ordering on locks and always acquire
   them in that order. Accounts already have unique integer ids, so _move
   acquires the lock of the account with the smaller id first (lock1) and
   the other second (lock2), then does `with lock1, lock2:`. The book's
   comment notes that it does not matter if lock1 equals lock2 (a transfer
   from an account to itself): the locks are reentrant (RLock), so the
   same thread may re-acquire lock2.

   With a fixed order, two threads can never each hold one lock while
   waiting for the other, so the circular wait that causes deadlock is
   impossible.

This file's Account implements the corrected program, with a few
additions listed in TEXTBOOK CODE COMPARISON.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
a = Account(100), b = Account(0); Account.transfer(a, b, 40) starts a
thread; after joining it, a has 60 and b has 40.
"""

# Python standard library: thread-based parallelism.
# Module documentation: https://docs.python.org/3/library/threading.html
# Lock API: https://docs.python.org/3/library/threading.html#lock-objects
# RLock API: https://docs.python.org/3/library/threading.html#rlock-objects
# Thread API: https://docs.python.org/3/library/threading.html#thread-objects
import threading


class Account:
    """A bank account whose transfers lock accounts in id order.

    The textbook's Account class with the deadlock fix applied.
    """

    # Class attribute shared by all accounts: the next id to hand out.
    # The leading underscore marks it internal by convention.
    _global_id=0

    # Added in this file (not in the book): a plain, non-reentrant
    # threading.Lock guarding _global_id, so two accounts created in
    # different threads at the same time cannot receive the same id.
    _id_lock=threading.Lock()

    def __init__(self,balance):
        self._balance=balance

        # `with lock:` acquires the lock and releases it automatically at
        # the end of the block. `+=` on a shared counter is read-modify-write
        # and not atomic, hence the lock.
        with Account._id_lock:
            self._id=Account._global_id
            Account._global_id+=1

        # threading.RLock() is a REENTRANT lock: the thread holding it may
        # acquire it again without blocking (it must release it the same
        # number of times). This matters when lock1 and lock2 below are the
        # same lock (a transfer from an account to itself).
        self._lock=threading.RLock()

    def get_balance(self):

        # The file reads the balance under the lock so it never observes a
        # transfer half-way (the book reads it without locking).
        with self._lock:
            return self._balance

    def _move(self,other,amount):
        """Move `amount` from self to other; the book's corrected _move."""

        # Conditional expressions (`A if cond else B`) pick the lock of the
        # account with the SMALLER id as lock1 and the other as lock2. Every
        # thread therefore acquires any two account locks in the same global
        # order, which rules out deadlock.
        lock1=self._lock if self._id<other._id else other._lock
        lock2=other._lock if self._id<other._id else self._lock

        # `with lock1, lock2:` acquires lock1 then lock2, and releases them
        # in reverse order at the end of the block (also on exceptions).
        with lock1,lock2:

            # Reject overdrafts (book) and negative amounts (added here).
            if amount>self._balance or amount<0:
                return False
            other._balance+=amount
            self._balance-=amount
            return True

    # @staticmethod: a function stored in the class that receives no
    # automatic self/cls argument; call it as Account.transfer(a, b, x).
    @staticmethod
    def transfer(acc_from,acc_to,amount):

        # threading.Thread(target=f, args=(x, y)) prepares a thread that
        # will call f(x, y). Here f is the BOUND method acc_from._move, so
        # the call is acc_from._move(acc_to, amount). `args` must be a
        # tuple. start() begins running it concurrently.
        thread=threading.Thread(target=acc_from._move,args=(acc_to,amount))
        thread.start()

        # Returning the Thread (added; the book returns nothing) lets the
        # caller join() it to wait for the transfer to finish.
        return thread


# TEXTBOOK POST-SOLUTION DISCUSSION (page 296)
# --------------------------------------------
# The book's discussion is the deadlock scenario, the global-lock
# alternative and its drawback, and the lock-ordering fix described in the
# module docstring; it gives no complexity analysis.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - The book prints the original Account in full and then only the
#   replacement lines for _move (lock1/lock2 selection and
#   `with lock1, lock2:`). The file contains the corrected version only.
# - Added in the file: class attribute `_id_lock` and `with
#   Account._id_lock:` around id assignment; `with self._lock:` in
#   get_balance; the `amount<0` check; `return thread` from transfer.
# - _move: parameter `acc_to` renamed `other`; the book's
#   `print('returning True')` is omitted.
# - transfer: book thread variable `th`; file `thread`.
# - Method order differs (the file defines _move before transfer).
# - The book's comment "Does not matter if lock1 equals lock2: since
#   recursive_mutex locks are reentrant, we will re-acquire lock2." is
#   reflected in the new comments.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Tuple unpacking creates two accounts (ids assigned in order).
    a,b=Account(100),Account(0)

    # transfer() starts a background thread; join() waits until it is done
    # so the balances can be checked reliably.
    transfer=Account.transfer(a,b,40)
    transfer.join()
    print('Balances:',a.get_balance(),b.get_balance())

    # `assert` raises AssertionError if the balances are not (60, 40).
    assert (a.get_balance(),b.get_balance())==(60,40)
