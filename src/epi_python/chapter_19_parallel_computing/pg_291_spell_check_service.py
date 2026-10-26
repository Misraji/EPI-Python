"""EPI Python 19.1, textbook printed page 291: Implement caching for a multithreaded dictionary.

QUESTION: Cache spell-check requests without holding a lock during the expensive dictionary lookup.

TEXTBOOK ALGORITHM: The book keeps the most recent word/result pair, copies cached results under a lock, and computes misses outside the lock.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_19_parallel_computing.pg_291_spell_check_service
Test: python -m pytest tests/chapter_19_parallel_computing/test_pg_291_spell_check_service.py -v
"""

# threading.Lock documentation: https://docs.python.org/3/library/threading.html#lock-objects
import threading


class SpellCheckService:
    """PDF algorithm; inject callable lookup in place of the book's undefined HTTP service."""
    def __init__(self, closest_in_dictionary):
        self._lookup = closest_in_dictionary
        self._last_word = None
        self._closest_to_last_word = None
        self._lock = threading.Lock()

    def service(self, word):
        result = None
        with self._lock:
            if word == self._last_word:
                result = self._closest_to_last_word.copy()
        if result is None:
            result = self._lookup(word)
            with self._lock:
                self._last_word = word
                self._closest_to_last_word = result.copy()
        return result


if __name__=='__main__':
    checker=SpellCheckService(lambda w: [w.upper()])
    print('Corrections:',checker.service('hello'))
    assert checker.service('hello')==['HELLO']
