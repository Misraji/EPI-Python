"""EPI Python 24.35, textbook printed page 402: Road network.

QUESTION: Choose one proposed bidirectional highway minimizing the total all-pairs driving distance.

TEXTBOOK ALGORITHM: Use Floyd–Warshall on original highways, then evaluate each proposed road against all ordered pairs.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_402_find_best_proposals
Test: python -m pytest tests/chapter_24_honors_class/test_pg_402_find_best_proposals.py -v
"""

# collections.namedtuple documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


HighwaySection = namedtuple('HighwaySection',('x','y','distance'))


def find_best_proposals(highways: list[HighwaySection], proposals: list[HighwaySection], n: int):
    g=[[float('inf')]*n for _ in range(n)]
    for i in range(n):
        g[i][i]=0
    for road in highways:
        g[road.x][road.y]=g[road.y][road.x]=min(g[road.x][road.y],road.distance)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j]=min(g[i][j],g[i][k]+g[k][j])
    best = None
    best_saving = 0
    for proposed in proposals:
        total_saving=0
        for a in range(n):
            for b in range(n):
                proposed_distance = min(g[a][proposed.x] + proposed.distance + g[proposed.y][b],
                                        g[a][proposed.y] + proposed.distance + g[proposed.x][b])
                total_saving += max(g[a][b]-proposed_distance,0)
        if total_saving>best_saving:
            best_saving,best=total_saving,proposed
    return best


if __name__=='__main__':
    roads=[HighwaySection(0,1,5),HighwaySection(1,2,5)]
    choices=[HighwaySection(0,2,2),HighwaySection(0,2,11)]
    print('Best highway:',find_best_proposals(roads,choices,3))
    assert find_best_proposals(roads,choices,3)==choices[0]
