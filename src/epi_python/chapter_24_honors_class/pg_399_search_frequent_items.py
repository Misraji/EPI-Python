"""EPI Python 24.33, textbook printed page 399: The heavy hitter problem.

QUESTION: Find every string occurring strictly more than n/k times using two passes and O(k) candidate space.

TEXTBOOK ALGORITHM: Maintain at most k-1 weighted candidates via Counter and verify candidate frequencies in a second pass.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_399_search_frequent_items
Test: python -m pytest tests/chapter_24_honors_class/test_pg_399_search_frequent_items.py -v
"""

# collections.Counter documentation: https://docs.python.org/3/library/collections.html#collections.Counter
import collections


def search_frequent_items(k: int, stream) -> list[str]:
    """stream must support *two independent iterations* (e.g. a list)."""
    if k <= 1:
        return []
    table = collections.Counter()
    n = 0
    for word in stream:
        table[word] += 1
        n += 1
        if len(table) == k:
            for candidate in list(table):
                table[candidate] -= 1

            # Unary plus creates a Counter without zero/negative count entries.
            table = +table
    for candidate in table:
        table[candidate] = 0
    for word in stream:
        if word in table:
            table[word] += 1
    return [word for word, count in table.items() if count > n / k]


if __name__ == '__main__':
    words = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
    print('Frequent words:', search_frequent_items(3, words))
    assert search_frequent_items(3, words) == ['a']
