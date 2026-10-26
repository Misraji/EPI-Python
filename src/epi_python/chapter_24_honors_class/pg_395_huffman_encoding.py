"""EPI Python — Exercise 24.31: Implement Huffman Coding

Chapter 24: Honors Class
Textbook: pages 395–398 (printed page numbers; problem on 395, solution
starts on 396).

PROBLEM (from the textbook)
---------------------------
Context: text can be compressed with a code book mapping each character to a
bit string (its code word); the compressed text is the concatenation of the
code words, and the code book is stored separately (e.g. in a preamble). To
decompress, read bits until they form a code word, and repeat. For the
compression to be reversible it suffices that no code word is a prefix of
another ("011 is a prefix of 0110 but not a prefix of 1100"). Shorter bit
strings should go to more common characters. The book restricts attention to
individual characters (examining common sequences of characters may compress
better but costs more time). Commonness is measured by a character's
frequency, a number between zero and one; all frequencies sum to 1. The
average code length is the sum, over characters, of code word length times
frequency. Table 24.1 gives English letter frequencies, in percent, in
everyday documents:

    a 8.17   b 1.49   c 2.78   d 4.25   e 12.70  f 2.23   g 2.02
    h 6.09   i 6.97   j 0.15   k 0.77   l 4.03   m 2.41   n 6.75
    o 7.51   p 1.93   q 0.10   r 5.99   s 6.33   t 9.06   u 2.76
    v 0.98   w 2.36   x 0.15   y 1.97   z 0.07

"Given a set of characters with corresponding frequencies, find a code book
that has the smallest average code length."

HINT (from the textbook)
------------------------
"Reduce the problem from n characters to one on n - 1 characters."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Trivial solution: fixed-length codes of ceil(log n) bits for n distinct
characters. Optimal when all characters are equally likely, but much worse
when frequencies vary widely.

Heuristic 1: split the characters into two subsets of about equal total
frequency, solve each, and prefix 0 to the first subset's codes and 1 to the
second's. Not always optimal: for A, B, C, D with frequencies
{0.4, 0.35, 0.2, 0.05} it yields 00, 10, 11, 01, whereas the optimum is
0, 10, 110, 111. It also needs a near-balanced partition, which is
computationally hard.

Heuristic 2: give 0 to the most frequent character, solve the rest, and
prefix their codes with 1. Very poor with equal frequencies: if A, B, C, D
all have 0.25 it yields 0, 10, 100, 111 whereas 00, 01, 10, 11 is optimal.
It ignores relative frequencies.

Huffman coding is optimal (other optimal codes may exist). It focuses on the
least frequent characters: merge the two rarest characters into a new
character, solve the n - 1 character problem recursively, then derive the
two merged characters' codes from their combined character's code by
appending 0 for one and 1 for the other. Concretely:

(1) Sort the characters by increasing frequency and create a binary tree
    node for each; call this set S.
(2) Make a new node u whose children are the two nodes of smallest
    frequency; u's frequency is the sum of theirs.
(3) Remove those children from S and add u. Repeat from (2) until S holds a
    single node, the root.

Label left edges 0 and right edges 1; the root-to-leaf path spells the
leaf character's code. For Table 24.1 this gives the Huffman tree of
Figure 24.9 and the codes of Table 24.2 (page 397):

    a 1110      b 110000    c 01001     d 11111     e 100
    f 00101     g 110011    h 0110      i 1011      j 001001011
    k 0010011   l 11110     m 00111     n 1010      o 1101
    p 110001    q 001001001 r 0101      s 0111      t 000
    u 01000     v 001000    w 00110     x 001001010 y 110010
    z 001001000

For example t, e and z get 000, 100 and 001001000. The average code length
is 4.205, versus ceil(log 26) = 5 bits per character for the trivial code.
The book's implementation keeps S as a min-heap of candidate nodes.

The single function in this file, huffman_encoding, follows that heap-based
algorithm and, like the book's program, returns the average code length.
It computes code lengths from tree depths rather than building the code
strings (see the code comparison).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    a 50%, b 25%, c 25%  ->  codes of lengths 1, 2, 2;
                             average length 0.5*1 + 0.25*2 + 0.25*2 = 1.5
"""

# Python standard library: heap queue (priority queue) algorithms on lists.
# Module documentation: https://docs.python.org/3/library/heapq.html
# APIs used: https://docs.python.org/3/library/heapq.html#heapq.heapify
#            https://docs.python.org/3/library/heapq.html#heapq.heappop
#            https://docs.python.org/3/library/heapq.html#heapq.heappush
import heapq

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple

# Python standard library: iterator building blocks.
# Module documentation: https://docs.python.org/3/library/itertools.html
# count API: https://docs.python.org/3/library/itertools.html#itertools.count
from itertools import count


# collections.namedtuple creates a tuple subclass with named fields: a
# CharWithFrequency has .c (the character) and .freq (its frequency, given
# as a percentage as in Table 24.1). Same definition as the book.
CharWithFrequency=namedtuple('CharWithFrequency',('c','freq'))


# Type hints: input is a list of CharWithFrequency, output a float (average
# code length). Annotations are documentation only; not enforced.
def huffman_encoding(symbols: list[CharWithFrequency]) -> float:
    """Return average codeword length for frequency percentages (as in the book).

    This follows the textbook's single implementation (min-heap of
    candidate nodes; repeatedly merge the two least frequent), but
    represents tree nodes as plain tuples and computes code lengths from
    leaf depths instead of building code strings.
    """

    # Added guard (not in the book): no symbols, average length 0.
    if not symbols:return 0.0

    # itertools.count() returns an endless iterator 0, 1, 2, ...; each
    # next(serial) gives the following integer. Heap entries are tuples
    # (frequency, serial, node) and tuples compare item by item, so when two
    # frequencies are equal the unique serial number decides, and Python
    # never has to compare two nodes (a leaf namedtuple against an internal
    # (left, right) tuple could raise TypeError or behave arbitrarily).
    serial=count()

    # List comprehension: one heap entry per symbol (step (1) of the book).
    heap=[(s.freq,next(serial),s) for s in symbols]

    # heapq.heapify(list) rearranges the list in place, in linear time, into
    # a min-heap: heap[0] is always the smallest entry. This replaces sorting
    # by frequency.
    heapq.heapify(heap)

    # Keeps combining two nodes until there is one node left (book's
    # comment); this is steps (2) and (3).
    while len(heap)>1:

        # heapq.heappop(heap) removes and returns the smallest entry in
        # O(log n), keeping the heap property. Two pops give the two least
        # frequent nodes. Tuple unpacking discards the serial with `_`.
        lf,_,left=heapq.heappop(heap)
        rf,_,right=heapq.heappop(heap)

        # heapq.heappush(heap, item) inserts in O(log n). The merged node is
        # the tuple (left, right); its frequency is the sum of its children's.
        heapq.heappush(heap,(lf+rf,next(serial),(left,right)))

    # Maps each character to the length of its code word.
    code_lengths={}

    # Traverses the binary tree, assigning code lengths to leaves (depth =
    # number of 0/1 edges from the root = code length).
    def assign(node,depth):

        # isinstance(obj, cls) tests whether obj is an instance of cls (or a
        # subclass). Leaves are CharWithFrequency; internal nodes are plain
        # (left, right) tuples, which are not CharWithFrequency instances.
        # Docs: https://docs.python.org/3/library/functions.html#isinstance
        if isinstance(node,CharWithFrequency):

            # max(1, depth): with a single symbol the root is a leaf at
            # depth 0; this gives it a 1-bit code instead (the book would
            # assign the empty code '').
            code_lengths[node.c]=max(1,depth)
        else:
            assign(node[0],depth+1)
            assign(node[1],depth+1)

    # heap[0] is the only remaining entry; [2] selects its node (the root).
    assign(heap[0][2],0)

    # Average code length: sum() over a generator expression of
    # length * frequency, dividing by 100 because frequencies are
    # percentages. `/` is true division and yields a float.
    return sum(code_lengths[s.c]*s.freq/100 for s in symbols)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 398)
# --------------------------------------------
# Each execution of steps (2) and (3) needs two extract-min operations and
# one insert, so building the Huffman tree takes O(n log n) time for n
# characters. The tree may be very skewed; then the code words have lengths
# 1, 2, 3, ..., n and generating the code book costs
# O(1 + 2 + ... + n) = O(n^2).
#
# A rigorous optimality proof is very unlikely to be asked in an interview.
# The proof that Huffman's algorithm gives the minimum average code length
# is by induction on the number of characters; the induction step uses
# proof by contradiction, with the two leaves of the rarest characters
# playing the central role.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * CharWithFrequency: book `collections.namedtuple(...)`; file imports
#   `namedtuple` directly. Same fields.
# * Tree nodes: the book defines a nested class `BinaryTree` with
#   `aggregate_freq`, `s`, `left`, `right` and `__lt__` comparing
#   `aggregate_freq` with `<=`, and keeps `BinaryTree` objects in the heap.
#   The file uses heap tuples `(freq, serial, node)` with an
#   `itertools.count()` tie-breaker (an extra import not in the book), leaf
#   nodes being CharWithFrequency and internal nodes `(left, right)` tuples.
# * Code assignment: the book's `assign_huffman_code(tree, code)` builds the
#   actual code strings in a dict named `huffman_encoding` (appending '0',
#   switching to '1', `''.join(code)`), then returns
#   `sum(len(huffman_encoding[s.c]) * s.freq / 100 for s in symbols)`.
#   The file's `assign(node, depth)` records only code lengths in
#   `code_lengths`, using `max(1, depth)`, and returns the same sum.
# * Added: type hints, `if not symbols: return 0.0` guard. Behaviour
#   differs for a single symbol (book: length 0; file: length 1).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example: frequencies 50%, 25%, 25% give lengths 1, 2, 2.
    result=huffman_encoding([CharWithFrequency('a',50),CharWithFrequency('b',25),CharWithFrequency('c',25)])
    print('Average Huffman code length:',result)

    # `assert` stops with an AssertionError if the condition is false.
    # (Exact float equality works here because 0.5 + 0.5 + 0.5 is exactly
    # representable.) pytest provides the more thorough verification.
    assert result==1.5
