"""EPI Python 19.5, textbook printed page 295: Deadlock.

QUESTION: Avoid deadlock when transferring money between accounts concurrently.

TEXTBOOK ALGORITHM: Acquire both account RLocks consistently by increasing unique account id, as in the PDF.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_19_parallel_computing.pg_295_account_transfer
Test: python -m pytest tests/chapter_19_parallel_computing/test_pg_295_account_transfer.py -v
"""

# threading.RLock documentation: https://docs.python.org/3/library/threading.html#rlock-objects
import threading


class Account:
    _global_id=0
    _id_lock=threading.Lock()

    def __init__(self,balance):
        self._balance=balance
        with Account._id_lock:
            self._id=Account._global_id
            Account._global_id+=1
        self._lock=threading.RLock()

    def get_balance(self):
        with self._lock:
            return self._balance

    def _move(self,other,amount):
        lock1=self._lock if self._id<other._id else other._lock
        lock2=other._lock if self._id<other._id else self._lock
        with lock1,lock2:
            if amount>self._balance or amount<0:
                return False
            other._balance+=amount
            self._balance-=amount
            return True

    @staticmethod
    def transfer(acc_from,acc_to,amount):
        thread=threading.Thread(target=acc_from._move,args=(acc_to,amount))
        thread.start()
        return thread


if __name__=='__main__':
    a,b=Account(100),Account(0)
    transfer=Account.transfer(a,b,40)
    transfer.join()
    print('Balances:',a.get_balance(),b.get_balance())
    assert (a.get_balance(),b.get_balance())==(60,40)
