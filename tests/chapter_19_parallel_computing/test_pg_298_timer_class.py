# pytest documentation: https://docs.pytest.org/en/stable/
import threading

from epi_python.chapter_19_parallel_computing.pg_298_timer_class import Timer


def test_immediate_and_cancelled_tasks():
    timer=Timer()
    called=threading.Event()
    cancelled=threading.Event()
    try:
        timer.schedule('execute',called.set,0)
        timer.schedule('cancel',cancelled.set,3600)
        assert timer.cancel('cancel')
        assert called.wait(1)
        assert not cancelled.is_set()
        assert not timer.cancel('cancel')
    finally:
        timer.close()
