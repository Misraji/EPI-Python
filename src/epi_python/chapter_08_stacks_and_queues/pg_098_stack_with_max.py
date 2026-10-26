"""EPI Python — Exercise 8.1: Implement a Stack with Max API

Chapter 8: Stacks and Queues
Textbook: pages 98–100 (printed page numbers; the problem and solution start
on page 98, the second program and Figure 8.2 are on page 100).

PROBLEM (from the textbook)
---------------------------
"Design a stack that includes a max operation, in addition to push and pop.
The max method should return the maximum value stored in the stack."

HINT (from the textbook)
------------------------
"Use additional storage to track the maximum value."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Simplest approach: compute max by looking at every element currently on the
stack (for an array-based stack, iterate over the underlying array). This
costs O(n) time per max call and O(1) extra space, where n is the number of
elements on the stack.

Auxiliary structures: a heap or a BST together with a hash table bring max
down to O(log n) time, but the extra space grows to O(n) and the code becomes
considerably more complicated.

A single variable M holding the current maximum: pushing e is easy to handle
(M = max(M, e)), but popping is the problem. If the popped element is M,
nothing tells us what the largest of the remaining elements is, so all of
them would have to be re-examined.

Caching (trading space for time): store, alongside every stack entry, the
maximum of that entry and everything below it. A pop simply discards the
entry together with its cached maximum, so the new top's cached value is
immediately the correct maximum. This is the textbook's first program,
implemented below as the class `Stack`.

Reducing the best-case space: an element e pushed while a larger element is
already on the stack can never become the maximum (the larger element stays
below it until e is popped), so there is no need to record a maximum for it.
One might keep just the sequence of maxima on a separate stack, but that
breaks down when the maximum value is pushed more than once (duplicates).
The fix is to store each maximum together with a count of how many times it
occurs. The auxiliary stack therefore holds (max, count) pairs; Figure 8.2
illustrates this. This is the textbook's second program, implemented below
as the class `StackWithCount` (the book also calls this class `Stack`).

Figure 8.2 (textbook example; primary stack and aux stack, both initially
empty, shown after each operation): push 2, push 2, push 1, push 4, push 5,
push 5, push 3, pop, pop, pop, pop, push 0, push 3. Reading the figure, the
top of aux evolves as follows:
    push 2 -> aux top (2,1)        push 2 -> (2,2)
    push 1 -> (2,2) unchanged      push 4 -> (4,1) above (2,2)
    push 5 -> (5,1)                push 5 -> (5,2)
    push 3 -> (5,2) unchanged      pop 3  -> (5,2)
    pop 5  -> (5,1)                pop 5  -> (5,1) removed; top (4,1)
    pop 4  -> (4,1) removed; top (2,2)
    push 0 -> (2,2) unchanged      push 3 -> (3,1) above (2,2)
The top of aux always holds the current maximum and how many times it
occurs on the primary stack.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    stack_max_history([3, 1, 4, 1, 5]) -> [3, 3, 4, 4, 5]
    Calling max() or pop() on an empty stack raises IndexError.
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
import collections


class Stack:
    """Stack with O(1) max, caching the maximum in every entry.

    This is the textbook's first implementation (pages 98–99).
    """

    # Each record holds the element and the maximum at or below that entry.
    #
    # collections.namedtuple(typename, field_names) creates a new class: a
    # tuple subclass whose positions can also be read by name. Here
    # ElementWithCachedMax(7, 9) behaves like the tuple (7, 9), but the
    # values can be read as `.element` and `.max`, which makes the code
    # self-describing. Like any tuple it is immutable, which is fine here
    # because a stack record never changes after it is pushed.
    #
    # Because this assignment appears inside the class body, the new class
    # becomes a class attribute: it is reached as Stack.ElementWithCachedMax
    # or, inside methods, as self.ElementWithCachedMax.
    ElementWithCachedMax = collections.namedtuple(
        "ElementWithCachedMax", ("element", "max")
    )

    def __init__(self):

        # The underlying Python list acts as the stack: its end is the top.
        # The leading underscore is a naming convention meaning "internal;
        # not part of the public interface" (Python does not enforce it).
        self._element_with_cached_max = []

    # `-> bool` is a return-type annotation (a type hint). It documents that
    # the method returns a bool; Python records it but does not enforce it.
    def empty(self) -> bool:
        return len(self._element_with_cached_max) == 0

    def max(self) -> int:
        if self.empty():

            # Raising IndexError matches what Python lists do on an empty
            # `s[-1]` or `s.pop()`, so callers get a familiar error type.
            raise IndexError("max(): empty stack")

        # Index -1 refers to the last list element, i.e. the stack top.
        # Its cached `.max` field is the maximum of the whole stack.
        return self._element_with_cached_max[-1].max

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop(): empty stack")

        # list.pop() with no argument removes AND returns the last element
        # (the top) in O(1) time. The removed record's cached maximum
        # disappears with it, so the new top already holds the correct
        # maximum of the remaining elements. `.element` extracts the value.
        # Documentation: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
        return self._element_with_cached_max.pop().element

    # `value: int` and `-> None` are type hints: the parameter is expected to
    # be an int and the method returns nothing. Python does not check them.
    def push(self, value: int) -> None:

        # A conditional expression `A if condition else B` evaluates to A
        # when the condition is true, otherwise B. For the first element
        # the maximum is the element itself; otherwise the built-in max()
        # compares the new value with the current maximum below it.
        # max(): https://docs.python.org/3/library/functions.html#max
        maximum = value if self.empty() else max(value, self.max())

        # list.append() adds the new record at the end (the top) in
        # amortized O(1) time.
        # Documentation: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(value, maximum)
        )


class StackWithCount:
    """Stack with O(1) max that records only maxima with their counts.

    This is the textbook's second implementation (pages 99–100), which the
    book also names `Stack`; it is renamed here so both versions can coexist.
    """

    # A small nested class used as a mutable record. Unlike a namedtuple,
    # its `count` attribute can be changed in place (count += 1), which is
    # exactly what duplicate maxima require.
    class MaxWithCount:
        def __init__(self, maximum: int, count: int):
            self.max = maximum
            self.count = count

    def __init__(self):

        # `list[int]` is a type hint for "a list whose items are ints"
        # (built-in generic syntax, Python 3.9+). The second hint names the
        # nested class by its full path. Hints are not enforced at runtime.
        # _element is the primary stack; _cached_max_with_count is the
        # auxiliary stack ("aux" in Figure 8.2).
        self._element: list[int] = []
        self._cached_max_with_count: list[StackWithCount.MaxWithCount] = []

    def empty(self) -> bool:

        # An empty list is falsy in Python, so `not self._element` is True
        # exactly when the primary stack has no elements.
        return not self._element

    def max(self) -> int:
        if self.empty():
            raise IndexError("max(): empty stack")

        # The top of the auxiliary stack always holds the current maximum.
        return self._cached_max_with_count[-1].max

    def push(self, value: int) -> None:
        self._element.append(value)

        # An empty auxiliary list (falsy) means this is the first element:
        # it is the maximum, seen once.
        if not self._cached_max_with_count:
            self._cached_max_with_count.append(self.MaxWithCount(value, 1))
        else:
            current_maximum = self._cached_max_with_count[-1].max

            # Equal to the current maximum: one more copy of it.
            if value == current_maximum:
                self._cached_max_with_count[-1].count += 1

            # Larger: a new maximum is recorded on top of aux.
            # Smaller values are not recorded at all; they can never be the
            # maximum while the larger element remains below them.
            elif value > current_maximum:
                self._cached_max_with_count.append(self.MaxWithCount(value, 1))

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop(): empty stack")
        value = self._element.pop()
        maximum = self._cached_max_with_count[-1]

        # Only popping a copy of the current maximum affects aux. When its
        # count reaches zero, that maximum no longer occurs on the stack and
        # its record is removed, exposing the previous maximum beneath it.
        if value == maximum.max:
            maximum.count -= 1
            if maximum.count == 0:
                self._cached_max_with_count.pop()
        return value


def stack_max_history(values: list[int]) -> list[int]:
    """Push each value onto a `Stack` and record max() after every push.

    Repository helper added for testing/learning; not in the textbook.
    """
    stack = Stack()
    result: list[int] = []
    for value in values:
        stack.push(value)
        result.append(stack.max())
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 99–100)
# ------------------------------------------------
# First program (cache a maximum in every entry): push, pop, max and empty
# all run in O(1) time. The extra space is O(n) no matter what keys are
# stored, since every entry carries its cached maximum.
#
# Second program (maxima with counts): the worst-case extra space is still
# O(n); this happens when every pushed key is larger than all keys already
# on the primary stack, so each push adds an aux record. When there are few
# distinct keys, or the maximum changes rarely, aux is much smaller, down to
# O(1) in the best case. Every operation still takes O(1) time.
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book program 1, `class Stack` (page 99): file class `Stack` has the same
# namedtuple `ElementWithCachedMax` and the same method names. Differences:
# `push(self, x)` is renamed `push(self, value: int) -> None`; the book
# computes the cached maximum inline inside the append call
# (`x if self.empty() else max(x, self.max())`), while the file first stores
# it in a separate local variable `maximum`; return-type hints (`-> bool`,
# `-> int`) are added to empty/max/pop.
#
# Book program 2, also named `class Stack` (pages 99–100): file renames it
# `StackWithCount`. `MaxWithCount.__init__(self, max, count)` becomes
# `__init__(self, maximum: int, count: int)` with two separate assignments
# instead of the book's tuple assignment `self.max, self.count = max, count`.
# `empty` uses `not self._element` instead of `len(self._element) == 0`.
# `push(self, x)` becomes `push(self, value: int)`; the book tests
# `len(self._cached_max_with_count) == 0`, the file `not
# self._cached_max_with_count`; the local `current_max` is renamed
# `current_maximum`. In `pop`, the book uses `pop_element` and
# `current_max = ...[-1].max` and indexes `[-1]` again to update the count;
# the file uses `value` and keeps a reference `maximum = ...[-1]` (the record
# object), comparing `value == maximum.max` and updating `maximum.count`.
# The file puts `push` before `pop` (book order: empty, max, pop, push).
# Type hints `list[int]` / `list[StackWithCount.MaxWithCount]` are added to
# the attributes.
#
# Helper not in the book: `stack_max_history`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Run the same scenario on both textbook designs. A class is an ordinary
    # object in Python, so it can be placed in a tuple and called later.
    # The pushes 2, 2, 1, 4, 5, 5, 3 followed by four pops are the
    # operations of the book's Figure 8.2.
    for stack_type in (Stack, StackWithCount):
        stack = stack_type()
        for value in (2, 2, 1, 4, 5, 5, 3):
            stack.push(value)

            # An f-string (f"...") evaluates the expressions inside {} and
            # inserts their values. `stack_type.__name__` is the class's
            # name as a string, e.g. "Stack".
            print(f"{stack_type.__name__}: pushed {value}, max={stack.max()}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. After popping 3, 5, 5, 4 (as in Figure 8.2) the
        # remaining elements are 2, 2, 1, so the maximum is 2.
        for expected in (3, 5, 5, 4):
            assert stack.pop() == expected
        assert stack.max() == 2
        print(f"{stack_type.__name__}: final max={stack.max()}")
    print("Both textbook stack designs passed.")
