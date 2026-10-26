# pytest documentation: https://docs.pytest.org/en/stable/
from collections import Counter

from epi_python.chapter_24_honors_class.pg_399_search_frequent_items import search_frequent_items


def test_frequent_items():
    for words in [[], ['a'], ['a','b','a','c','a','b','a'], list('aabbccddeeeaa')]:
        for k in range(2, 8):
            counts=Counter(words)
            expected={w for w,c in counts.items() if c>len(words)/k}
            assert set(search_frequent_items(k, words))==expected
