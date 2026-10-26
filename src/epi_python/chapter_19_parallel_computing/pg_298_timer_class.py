"""EPI Python 19.8, textbook printed page 298: Implement a Timer class.

QUESTION: Schedule named tasks for execution in the future and allow cancellation before they start.

TEXTBOOK ALGORITHM: Implement the PDF min-heap plus name-indexed dictionary, protected by a condition and driven by a dispatch thread.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_19_parallel_computing.pg_298_timer_class
Test: python -m pytest tests/chapter_19_parallel_computing/test_pg_298_timer_class.py -v
"""

# heapq documentation: https://docs.python.org/3/library/heapq.html
import heapq

# threading.Condition and Thread: https://docs.python.org/3/library/threading.html
import threading

# time.monotonic documentation: https://docs.python.org/3/library/time.html#time.monotonic
import time


class Timer:
    """Finite, closable implementation of the book's named-task timer design."""
    def __init__(self):
        self._condition=threading.Condition()
        self._heap=[]
        self._scheduled={}
        self._sequence=0
        self._closed=False
        self._launched=[]
        self._dispatcher=threading.Thread(target=self._dispatch,daemon=True)
        self._dispatcher.start()

    def schedule(self,name,callback,delay_seconds):
        with self._condition:
            if self._closed:
                raise RuntimeError('timer already closed')
            if name in self._scheduled:
                raise ValueError('task name already scheduled')
            self._sequence+=1
            item=(time.monotonic()+delay_seconds,self._sequence,name,callback)
            self._scheduled[name]=item
            heapq.heappush(self._heap,item)
            self._condition.notify()

    def cancel(self,name):
        with self._condition:
            found=self._scheduled.pop(name,None) is not None
            self._condition.notify()
            return found

    def _dispatch(self):
        while True:
            with self._condition:
                while True:
                    if self._closed:
                        return
                    while self._heap and self._scheduled.get(self._heap[0][2]) is not self._heap[0]:
                        heapq.heappop(self._heap)
                    if not self._heap:
                        self._condition.wait()
                        continue
                    remaining=self._heap[0][0]-time.monotonic()
                    if remaining>0:
                        self._condition.wait(timeout=remaining)
                        continue
                    deadline,seq,name,callback=heapq.heappop(self._heap)
                    self._scheduled.pop(name,None)
                    worker=threading.Thread(target=callback)
                    self._launched.append(worker)
                    worker.start()
                    break

    def close(self):
        with self._condition:
            self._closed=True
            self._scheduled.clear()
            self._condition.notify_all()
        self._dispatcher.join(timeout=2)
        for thread in self._launched:
            thread.join(timeout=2)


if __name__=='__main__':
    seen=threading.Event()
    timer=Timer()
    timer.schedule('say-hello',seen.set,0)
    assert seen.wait(1)
    timer.close()
    print('Named task executed successfully')
