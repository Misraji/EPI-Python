"""EPI Python — Exercise 14.1: Test if a Binary Tree Satisfies the BST Property

Chapter 14: Binary Search Trees
Textbook: pages 199–201 (printed page numbers; problem on 199, solution
starts on 200).

PROBLEM (from the textbook)
---------------------------
"Write a program that takes as input a binary tree and checks if the tree
satisfies the BST property."

HINT (from the textbook)
------------------------
"Is it correct to check for each node that its key is greater than or equal
to the key at its left child and less than or equal to the key at its right
child?"

Reference figure used below — Figure 14.1 (page 198), "An example of a BST"
(node label = key):
    A=19 with left child B=7 and right child I=43
    B=7:  left C=3 (children D=2, E=5), right F=11
    F=11: right G=17, whose left child is H=13
    I=43: left J=23, right O=47
    J=23: right K=37 (children L=29, N=41); L=29 has right child M=31
    O=47: right P=53

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Direct approach from the definition: compute the maximum key in the root's
left subtree and the minimum key in its right subtree; check that the root's
key is >= that maximum and <= that minimum; if so, recursively check both
subtrees, otherwise return false. The minimum of a general binary tree is the
smallest of the root's key, the left subtree's minimum and the right
subtree's minimum (it can be in either subtree, since a general binary tree
need not be a BST); the maximum is analogous. The trouble is that subtrees
are traversed repeatedly: in the worst case (the tree is a BST and every
node's left child is empty) this is O(n^2) for n nodes. Caching each node's
largest and smallest keys brings it to O(n), at the cost of O(n) cache
storage.

Two O(n) approaches follow.

1. Propagate range constraints downward. The root imposes the first
   constraint: every key in its left subtree must be <= its key, every key in
   its right subtree >= it. In general, if all keys in a tree must lie in
   [l, u] and the root's key is w (which itself must be in [l, u], or the
   requirement already fails at the root), then the left subtree's keys must
   lie in [l, w] and the right subtree's in [w, u].
   Example on Figure 14.1: the initial range is [-inf, inf]; the call on the
   subtree rooted at B gets [-inf, 19] (19 being A's bound for its left
   subtree); at F the constraint is [7, 19]; at K it is [23, 43]. The binary
   tree of Figure 9.1 (page 112) is rejected when the recursion reaches C:
   the constraint there is [-inf, 6], but the key at F is 271.

2. Inorder traversal (described in the book without a listing): an inorder
   walk of a BST visits keys in sorted order, and conversely a binary tree
   whose inorder walk is sorted must be a BST (directly from the definitions
   of a BST and an inorder walk). So walk inorder, remembering the key of the
   previously visited node; if it is ever greater than the current node's
   key, the BST property is violated.

All of these explore the left subtree first, so even when the property fails
near the root (e.g. the root's right child holds a key smaller than the
root's), they still take O(n) time.

3. Breadth-first search reduces the time when the violation is at a node of
   small depth. Each queue entry holds a node plus a lower and an upper bound
   on the keys of the subtree rooted there. Start with the root and bounds
   (-inf, inf). Repeatedly pop an entry and check its node against its
   bounds: on a violation, stop (the property fails); otherwise enqueue its
   children with their corresponding bounds.
   Example on Figure 14.1: start with (A, [-inf, inf]); pop it and add
   (B, [-inf, 19]) and (I, [19, inf]); pop B and add (C, [-inf, 7]) and
   (D, [7, 19]) [as printed: B's right child in the figure is F]; continuing,
   every node satisfies its constraint, so the tree is a BST.
   If the property is violated in a subtree whose nodes lie within some
   depth, the violation is found without visiting any node at a greater
   depth, because each enqueued entry carries the tightest possible bounds
   for that node's key.

In this file: `is_bst_nodes` is the book's recursive range-constraint
implementation (approach 1); `is_bst_nodes_bfs` is the book's BFS
implementation (approach 3); `is_binary_tree_bst` is an adapter added in
this file that accepts a nested-tuple tree. The inorder approach has no
listing in the book.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    empty tree                               -> True
    2 with children 1 (left), 3 (right)       -> True
    2 with children 3 (left), 1 (right)       -> False
    10 with left 5 whose RIGHT child is 12,
       and right child 15                     -> False
       (each parent/child pair looks fine, but 12 > 10 sits in 10's left
       subtree: this is why the hint's local check is not enough)
"""

# Python standard library: automatic generation of special methods for
# simple record-like classes.
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# deque API: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


# `@dataclass` generates `__init__` from the annotated fields, so
# `TreeNode(2, TreeNode(1), TreeNode(3))` works (children default to None),
# plus a readable `__repr__`. The child annotations are strings because
# `TreeNode` is not yet defined while its own body runs; `"TreeNode | None"`
# means "a TreeNode or None". Annotations are not enforced at run time.
@dataclass
class TreeNode:
    data: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


# Type hints: `root: TreeNode | None` (an empty tree is None), `-> bool`.
def is_bst_nodes(root: TreeNode | None) -> bool:
    """Check every node against the full valid ancestor key range.

    This is the textbook's first O(n) implementation: recursive propagation
    of [lower, upper] bounds (book name `is_binary_tree_bst`).
    """

    # A nested function: `valid` is defined inside `is_bst_nodes` and is only
    # visible there. It replaces the book's default arguments for the range.
    def valid(node,lower,upper):

        # An empty subtree satisfies any constraint.
        if node is None:
            return True

        # Chained comparison: `lower <= x <= upper` means
        # `lower <= x and x <= upper`, evaluating x once.
        if not lower <= node.data <= upper:
            return False

        # Left keys must lie in [lower, node.data], right keys in
        # [node.data, upper]. `and` short-circuits: the right subtree is
        # checked only if the left one is valid.
        return valid(node.left,lower,node.data) and valid(node.right,node.data,upper)

    # float('-inf') and float('inf') are negative and positive infinity:
    # they compare below / above every number, so the root is unconstrained.
    # Documentation: https://docs.python.org/3/library/functions.html#float
    return valid(root,float('-inf'),float('inf'))


# Type hints: a nested tuple (data, left, right) or None; `-> bool`.
def is_binary_tree_bst(tree: tuple | None) -> bool:
    """Adapter added in this file (not in the textbook).

    Converts a nested tuple `(data, left_subtree, right_subtree)` into
    TreeNode objects and runs the recursive range check `is_bst_nodes`.
    """

    # Recursive builder using a conditional expression `X if cond else Y`.
    def build(t):
        return None if t is None else TreeNode(t[0],build(t[1]),build(t[2]))
    return is_bst_nodes(build(tree))


def is_bst_nodes_bfs(root: TreeNode | None) -> bool:
    """PDF's second complete solution: propagate BST bounds breadth-first.

    This is the textbook's BFS implementation (book name also
    `is_binary_tree_bst`).
    In a wide tree, the queue can use O(n) space. A violation near the
    root is detected without traversing descendants at greater depth.
    """

    # collections.deque is a double-ended queue. deque(iterable) creates it
    # with the given items. Here the single starting entry is a tuple
    # (node, lower bound, upper bound) for the root with infinite bounds.
    # Unlike list.pop(0), which shifts every remaining element (O(n)),
    # deque.popleft() removes the oldest entry in O(1) time: exactly what a
    # first-in, first-out BFS queue needs.
    # Documentation: https://docs.python.org/3/library/collections.html#collections.deque
    # popleft: https://docs.python.org/3/library/collections.html#collections.deque.popleft
    pending = deque([(root, float("-inf"), float("inf"))])

    # A non-empty deque is truthy; the loop runs until the queue is empty.
    while pending:

        # Remove the oldest entry and unpack the tuple into three names.
        node, lower, upper = pending.popleft()

        # Empty children are enqueued too; skip them here.
        if node is None:
            continue
        if not lower <= node.data <= upper:
            return False

        # Carry every ancestor's constraints to both descendants.
        # deque.append adds an entry at the right end (the back of the queue).
        pending.append((node.left, lower, node.data))
        pending.append((node.right, node.data, upper))

    return True


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 200–201)
# -------------------------------------------------
# - Recursive range-constraint version: O(n) time, O(h) additional space,
#   where h is the height of the tree (the recursion depth).
# - Inorder-walk version and the range version both explore the left
#   subtree first, so a violation close to the root still costs O(n).
# - BFS version: O(n) time and O(n) additional space (the queue).
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book listing 1: `def is_binary_tree_bst(tree, low_range=float('-inf'),
#   high_range=float('inf')):` recursing on itself with the range passed
#   through default parameters and `if not tree:` for the empty case.
#   File: `is_bst_nodes(root: TreeNode | None) -> bool` with a nested helper
#   `valid(node, lower, upper)` and `is None` tests; same logic.
# - Book listing 2 (BFS), also named `is_binary_tree_bst(tree)`: defines a
#   local `QueueEntry = collections.namedtuple('QueueEntry', ('node',
#   'lower', 'upper'))`, seeds `bfs_queue = collections.deque([...])`, and
#   checks only `if front.node:` before enqueuing both children with
#   `bfs_queue += [...]`. File: `is_bst_nodes_bfs`, plain tuples instead of
#   QueueEntry, `from collections import deque`, `continue` on None, two
#   `append` calls. Same logic.
# - The file's `is_binary_tree_bst(tree: tuple | None)` is an added adapter
#   taking nested tuples, NOT the book's function of the same name.
# - The file defines its own `TreeNode` dataclass (the book uses a BST node
#   class with `data`, `left`, `right`).
# - The book's inorder-traversal approach has no listing in either place.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases (added for learning; pytest has the
    # full set): an empty tree, a valid three-node BST, the same shape with
    # the children swapped, and the "hidden grandchild" counterexample.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks.
    result=is_binary_tree_bst(None)
    print('is_binary_tree_bst', result)
    assert result == True
    result=is_binary_tree_bst((2, (1, None, None), (3, None, None)))
    print('is_binary_tree_bst', result)
    assert result == True
    result=is_binary_tree_bst((2, (3, None, None), (1, None, None)))
    print('is_binary_tree_bst', result)
    assert result == False
    result=is_binary_tree_bst((10, (5, None, (12, None, None)), (15, None, None)))
    print('is_binary_tree_bst', result)
    assert result == False

    # Check the independent breadth-first textbook implementation too.
    # `right=TreeNode(12)` is a keyword argument, skipping the `left` field.
    valid_root = TreeNode(2, TreeNode(1), TreeNode(3))
    invalid_root = TreeNode(10, TreeNode(5, right=TreeNode(12)), TreeNode(15))
    assert is_bst_nodes_bfs(valid_root)
    assert not is_bst_nodes_bfs(invalid_root)
    print("Breadth-first BST check: passed")
