"""EPI exercise 8.1, printed page 98: Implement a stack with max API.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Implement a stack with max API.
Method/complexity: Store per-entry maximum in second stack field; O(1) push/pop/max, O(n) storage.
For the book's original explanation and variants, see:
    pg_098_exercise_08_01_implement_a_stack_with_max_api.md

Run: python -m epi_python.chapter_08_stacks_and_queues.pg_098_stack_with_max
Test: python -m pytest tests/chapter_08_stacks_and_queues/test_pg_098_stack_with_max.py -v
"""

class Stack:
    """LIFO stack supporting O(1) push/pop/max, including duplicate maxima."""
    def __init__(self):
        self._items: list[tuple[int, int]] = []

    def push(self, value: int) -> None:
        maximum = value if not self._items else max(value, self._items[-1][1])
        self._items.append((value, maximum))

    def pop(self) -> int:
        return self._items.pop()[0]

    def max(self) -> int:
        if not self._items:
            raise IndexError("max from empty stack")
        return self._items[-1][1]


def stack_max_history(values: list[int]) -> list[int]:
    """Push each input and record the maximum after that operation."""
    stack = Stack()
    result = []
    for value in values:
        stack.push(value)
        result.append(stack.max())
    return result


if __name__ == "__main__":
    stack = Stack()
    for value in [2, 7, 3]:
        stack.push(value)
        print("push:", value, "max:", stack.max())
    assert stack.pop() == 3 and stack.max() == 7
