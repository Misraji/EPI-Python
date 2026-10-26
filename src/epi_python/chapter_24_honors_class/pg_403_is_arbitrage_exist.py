"""EPI Python 24.36, textbook printed page 403: Test if arbitrage is possible.

QUESTION: Determine whether directed currency exchange rates admit a profitable conversion cycle.

TEXTBOOK ALGORITHM: Transform rates by negative logarithm and run Bellman–Ford to detect a negative-weight cycle.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_403_is_arbitrage_exist
Test: python -m pytest tests/chapter_24_honors_class/test_pg_403_is_arbitrage_exist.py -v
"""

# math.log documentation: https://docs.python.org/3/library/math.html#math.log
import math


def is_arbitrage_exist(rates: list[list[float]]) -> bool:
    if not rates:
        return False
    n=len(rates)
    graph=[[-math.log(rate) for rate in row] for row in rates]
    distance=[float('inf')]*n
    distance[0]=0.0
    for _ in range(1,n):
        updated=False
        for i in range(n):
            for j in range(n):
                new_distance=distance[i]+graph[i][j]
                if new_distance<distance[j]-1e-12:
                    distance[j]=new_distance
                    updated=True
        if not updated:
            return False
    return any(distance[i]+graph[i][j]<distance[j]-1e-12
               for i in range(n) for j in range(n))


if __name__ == '__main__':
    rates=[[1,2,1],[0.5,1,2],[0.3,0.5,1]]
    print('Arbitrage detected:',is_arbitrage_exist(rates))
    assert is_arbitrage_exist(rates)
