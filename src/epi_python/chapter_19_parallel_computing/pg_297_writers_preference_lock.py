"""EPI Python 19.7, textbook printed page 297: The readers-writers problem with write preference.

QUESTION: Prevent writers from starving when new readers continuously arrive.

TEXTBOOK ALGORITHM: Follow the PDF: readers must pass a writer-preference gate, so queued writers can stop later readers entering.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_19_parallel_computing.pg_297_writers_preference_lock
Test: python -m pytest tests/chapter_19_parallel_computing/test_pg_297_writers_preference_lock.py -v
"""

# threading.Condition documentation: https://docs.python.org/3/library/threading.html#condition-objects
import threading


class WritersPreferenceLock:
    """Condition-based finite form of the book's writer-preference locking rule."""
    def __init__(self):
        self._condition=threading.Condition()
        self._readers=0
        self._writer_active=False
        self._waiting_writers=0

    def acquire_read(self):
        with self._condition:
            while self._writer_active or self._waiting_writers:
                self._condition.wait()
            self._readers+=1

    def release_read(self):
        with self._condition:
            self._readers-=1
            if self._readers==0:
                self._condition.notify_all()

    def acquire_write(self):
        with self._condition:
            self._waiting_writers+=1
            try:
                while self._writer_active or self._readers:
                    self._condition.wait()
                self._writer_active=True
            finally:
                self._waiting_writers-=1

    def release_write(self):
        with self._condition:
            self._writer_active=False
            self._condition.notify_all()


if __name__=='__main__':
    rw=WritersPreferenceLock()
    rw.acquire_read();rw.release_read()
    rw.acquire_write();rw.release_write()
    print('Reader and writer exclusion checks passed')
