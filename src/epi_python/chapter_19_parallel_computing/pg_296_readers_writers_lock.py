"""EPI Python 19.6, textbook printed page 296: The readers-writers problem.

QUESTION: Allow multiple readers concurrently, but writers require exclusive access.

TEXTBOOK ALGORITHM: The PDF tracks read_count under a lock and lets the first reader acquire and last reader release a writer exclusion lock.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_19_parallel_computing.pg_296_readers_writers_lock
Test: python -m pytest tests/chapter_19_parallel_computing/test_pg_296_readers_writers_lock.py -v
"""

# threading.Lock documentation: https://docs.python.org/3/library/threading.html#lock-objects
import threading


class ReadersWritersLock:
    """Reader-preference solution from the book's first readers-writers problem."""
    def __init__(self):
        self._read_count=0
        self._count_lock=threading.Lock()
        self._write_lock=threading.Lock()

    def acquire_read(self):
        with self._count_lock:
            if self._read_count==0:
                self._write_lock.acquire()
            self._read_count+=1

    def release_read(self):
        with self._count_lock:
            self._read_count-=1
            if self._read_count==0:
                self._write_lock.release()

    def acquire_write(self):
        self._write_lock.acquire()

    def release_write(self):
        self._write_lock.release()


if __name__=='__main__':
    rw=ReadersWritersLock()
    rw.acquire_read();rw.acquire_read()
    print('Two readers acquired shared access')
    rw.release_read();rw.release_read()
    rw.acquire_write();rw.release_write()
    print('Writer acquired exclusive access')
