# pytest documentation: https://docs.pytest.org/en/stable/
import threading

from epi_python.chapter_19_parallel_computing.pg_297_writers_preference_lock import WritersPreferenceLock


def test_writer_not_starved_by_new_readers():
    rw=WritersPreferenceLock()
    rw.acquire_read()
    sequence=[]
    entered=threading.Event()
    def writer():
        rw.acquire_write();sequence.append('writer');entered.set();rw.release_write()
    t=threading.Thread(target=writer)
    t.start()
    # Allow the writer to enter the condition wait queue.
    with rw._condition:
        assert rw._waiting_writers==1
    def reader():
        rw.acquire_read();sequence.append('reader');rw.release_read()
    r=threading.Thread(target=reader);r.start()
    rw.release_read()
    t.join(1);r.join(1)
    assert sequence==['writer','reader']
    assert entered.is_set()
