"""EPI Python 24.14, textbook printed page 368: Compute fair bonuses.

QUESTION: Assign at least one ticket per developer, rewarding greater productivity than either immediate neighbor.

TEXTBOOK ALGORITHM: The printed textbook includes a heap strategy and a two-pass left/right dynamic strategy.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_368_calculate_bonus
Test: python -m pytest tests/chapter_24_honors_class/test_pg_368_calculate_bonus.py -v
"""

# heapq documentation: https://docs.python.org/3/library/heapq.html
import heapq


def calculate_bonus(productivity: list[int]) -> int:
    tickets=[1]*len(productivity)
    for i in range(1,len(productivity)):
        if productivity[i]>productivity[i-1]:
            tickets[i]=tickets[i-1]+1
    for i in reversed(range(len(productivity)-1)):
        if productivity[i]>productivity[i+1]:
            tickets[i]=max(tickets[i],tickets[i+1]+1)
    return sum(tickets)


def calculate_bonus_heap(productivity: list[int]) -> int:
    """Alternative min-heap solution also given in the book."""
    tickets=[1]*len(productivity)

    # heappop returns the next minimum (productivity, index) pair.
    heap=[(p,i) for i,p in enumerate(productivity)]
    heapq.heapify(heap)
    while heap:
        _,i=heapq.heappop(heap)
        if i>0 and productivity[i]>productivity[i-1]:
            tickets[i]=max(tickets[i],tickets[i-1]+1)
        if i+1<len(productivity) and productivity[i]>productivity[i+1]:
            tickets[i]=max(tickets[i],tickets[i+1]+1)
    return sum(tickets)


if __name__=='__main__':
    for fn in (calculate_bonus,calculate_bonus_heap):
        print(fn.__name__,fn([1,2,2,1]))
        assert fn([1,2,2,1])==6
