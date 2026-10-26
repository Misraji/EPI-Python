"""EPI 14.11: Add credits (printed page 215).

Problem: Add credits. The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: O(1) global credit increment; other operations use dict and a lazily invalidated heap.

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 14.11, printed page 215):
# Maintain client credits supporting insert, remove, lookup, add-to-all, and maximum.
# HINT: Use a global offset so add-to-all does not update individual clients.

# heapq maintains a min-heap; negating credits makes highest-credit entries win.
# https://docs.python.org/3/library/heapq.html
import heapq


class ClientsCreditsInfo:
    """Credit map with O(1) add-to-all and lazy max-heap cleanup.

    EPI uses bintrees.RBTree. A lazy heap plus dict uses only standard Python.
    """
    def __init__(self):
        self._offset=0
        self._client_to_credit:dict[str,int]={}
        self._credit_heap:list[tuple[int,str]]=[]

    def insert(self, client_id: str, credits: int) -> None:
        adjusted=credits-self._offset
        self._client_to_credit[client_id]=adjusted
        heapq.heappush(self._credit_heap,(-adjusted,client_id))

    def remove(self, client_id: str) -> bool:
        return self._client_to_credit.pop(client_id,None) is not None

    def lookup(self, client_id: str) -> int:
        credit=self._client_to_credit.get(client_id)
        return -1 if credit is None else credit+self._offset

    def add_all(self, credits: int) -> None:
        self._offset+=credits

    def max(self) -> str:
        while self._credit_heap:
            negative,client=self._credit_heap[0]
            if self._client_to_credit.get(client)==-negative:
                return client
            heapq.heappop(self._credit_heap)
        return ''


if __name__ == '__main__':
    info=ClientsCreditsInfo()
    info.insert('A',4); info.insert('B',8)
    info.add_all(3)
    print('Top client and adjusted credits:',info.max(),info.lookup(info.max()))
    assert info.max()=='B' and info.lookup('A')==7
