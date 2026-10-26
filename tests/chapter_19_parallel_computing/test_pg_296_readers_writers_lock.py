# pytest documentation: https://docs.pytest.org/en/stable/
import threading

from epi_python.chapter_19_parallel_computing.pg_296_readers_writers_lock import ReadersWritersLock


def test_readers_then_writer():
    rw=ReadersWritersLock()
    rw.acquire_read();rw.acquire_read()
    acquired=threading.Event()
    def write():
        rw.acquire_write()
        acquired.set()
        rw.release_write()
    thread=threading.Thread(target=write)
    thread.start()
    assert not acquired.wait(0.02)
    rw.release_read();rw.release_read()
    assert acquired.wait(1)
    thread.join(1)
    assert not thread.is_alive()
