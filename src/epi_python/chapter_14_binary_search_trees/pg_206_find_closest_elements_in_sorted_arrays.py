"""EPI 14.6: Find the closest entries in three sorted arrays (printed page 206).

Problem: Find the closest entries in three sorted arrays. The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: O(N log k) with standard-library heap, rather than bintrees.RBTree; k arrays and N total entries.

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 14.6, printed page 206):
# Choose one item from each sorted array so that max-min is minimized.
# HINT: Advance the smallest current item; track the largest.

# heapq implements a minimum-priority queue using a Python list.
# https://docs.python.org/3/library/heapq.html
import heapq


def find_closest_elements_in_sorted_arrays(sorted_arrays: list[list[int]]) -> int:
    """Return minimum (maximum - minimum) across one value per sorted array.

    The textbook uses an ordered BST from the third-party bintrees package.
    This self-contained adaptation uses the standard-library heapq instead.
    """
    if not sorted_arrays or any(not row for row in sorted_arrays):
        raise ValueError('Every input sorted array must contain at least one item')
    heap = [(row[0], i, 0) for i,row in enumerate(sorted_arrays)]

    # heapify converts a list into a min-heap in linear time.
    # https://docs.python.org/3/library/heapq.html#heapq.heapify
    heapq.heapify(heap)
    current_max = max(value for value,_,_ in heap)
    min_distance = float('inf')
    while True:

        # heappop retrieves/removes the smallest (value, array, position) entry.
        # https://docs.python.org/3/library/heapq.html#heapq.heappop
        minimum, source, index = heapq.heappop(heap)
        min_distance = min(min_distance, current_max - minimum)
        if index+1 == len(sorted_arrays[source]):
            return int(min_distance)
        next_value = sorted_arrays[source][index+1]
        current_max = max(current_max, next_value)

        # heappush preserves the heap invariant after appending a new entry.
        # https://docs.python.org/3/library/heapq.html#heapq.heappush
        heapq.heappush(heap,(next_value,source,index+1))


if __name__ == '__main__':
    example=[[5,10,15],[3,6,9,12,15],[8,16,24]]
    result=find_closest_elements_in_sorted_arrays(example)
    print('Shortest covering interval width:',result)
    assert result==1
