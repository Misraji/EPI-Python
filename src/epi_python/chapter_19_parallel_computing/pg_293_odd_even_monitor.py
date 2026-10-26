"""EPI Python 19.3, textbook printed page 293: Implement synchronization for two interleaving threads.

QUESTION: Two threads print numbers in ascending order, one odd and the other even.

TEXTBOOK ALGORITHM: Use the PDF OddEvenMonitor subclass of threading.Condition to wait and toggle turns.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_19_parallel_computing.pg_293_odd_even_monitor
Test: python -m pytest tests/chapter_19_parallel_computing/test_pg_293_odd_even_monitor.py -v
"""

# threading.Condition documentation: https://docs.python.org/3/library/threading.html#condition-objects
import threading


class OddEvenMonitor(threading.Condition):
    ODD_TURN=True
    EVEN_TURN=False

    def __init__(self):
        super().__init__()
        self.turn=self.ODD_TURN

    def wait_turn(self,old_turn):
        with self:
            while self.turn!=old_turn:
                self.wait()

    def toggle_turn(self):
        with self:
            self.turn ^= True
            self.notify()


class OddThread(threading.Thread):
    def __init__(self,monitor,emit,limit):
        super().__init__()
        self.monitor,self.emit,self.limit=monitor,emit,limit

    def run(self):
        for i in range(1,self.limit+1,2):
            self.monitor.wait_turn(OddEvenMonitor.ODD_TURN)
            self.emit(i)
            self.monitor.toggle_turn()


class EvenThread(threading.Thread):
    def __init__(self,monitor,emit,limit):
        super().__init__()
        self.monitor,self.emit,self.limit=monitor,emit,limit

    def run(self):
        for i in range(2,self.limit+1,2):
            self.monitor.wait_turn(OddEvenMonitor.EVEN_TURN)
            self.emit(i)
            self.monitor.toggle_turn()


def print_in_order(limit=100):
    monitor=OddEvenMonitor()
    result=[]
    odd=OddThread(monitor,result.append,limit)
    even=EvenThread(monitor,result.append,limit)
    odd.start();even.start()
    odd.join();even.join()
    return result


if __name__=='__main__':
    output=print_in_order(20)
    print('Ordered output:',output)
    assert output==list(range(1,21))
