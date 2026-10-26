"""Independent, randomized cross-checks of the new checkpoint implementations.

Tests compare results with simple Python reference models, not copies of the
optimized algorithms. Every pseudorandom experiment uses a fixed seed.
"""

# random.Random gives reproducible tests without altering global random state.
# Documentation: https://docs.python.org/3/library/random.html#random.Random
import random

# itertools.permutations enumerates all orderings for small-input references.
# Documentation: https://docs.python.org/3/library/itertools.html#itertools.permutations
import itertools

from epi_python.chapter_04_primitive_types.pg_029_multiply_without_arithmetic import multiply
from epi_python.chapter_04_primitive_types.pg_031_divide_without_arithmetic import divide
from epi_python.chapter_05_arrays.pg_043_multiply_digits import multiply_digits
from epi_python.chapter_05_arrays.pg_050_apply_permutation import apply_permutation
from epi_python.chapter_05_arrays.pg_061_spiral_ordering import matrix_in_spiral_order
from epi_python.chapter_05_arrays.pg_064_rotate_matrix import rotate_matrix
from epi_python.chapter_06_strings.pg_069_convert_base import convert_base
from epi_python.chapter_07_linked_lists.pg_095_list_pivot import list_pivot_values
from epi_python.chapter_09_binary_trees.pg_125_reconstruct_from_traversals import reconstruct_tree
from epi_python.chapter_11_searching.pg_153_kth_largest_element import find_kth_largest
from epi_python.chapter_12_hash_tables.pg_168_smallest_subarray_covering_set import smallest_subarray_covering_set
from epi_python.chapter_12_hash_tables.pg_171_smallest_subarray_sequential_cover import find_smallest_sequentially_covering_subset
from epi_python.chapter_12_hash_tables.pg_175_string_decompositions import find_all_substrings


def test_bitwise_arithmetic_against_python():
    rng = random.Random(15)
    for _ in range(350):
        x, y = rng.randrange(0, 1 << 20), rng.randrange(1, 1 << 15)
        assert multiply(x, y) == x * y
        assert divide(x, y) == x // y


def test_digit_multiplication_against_python_big_integers():
    rng = random.Random(28)
    for _ in range(250):
        a, b = rng.randrange(-(10**20), 10**20), rng.randrange(-(10**20), 10**20)
        def digits(x):
            if x == 0:
                return [0]
            return [-int(str(abs(x))[0])] + [int(c) for c in str(abs(x))[1:]] if x < 0 else [int(c) for c in str(x)]
        output = multiply_digits(digits(a), digits(b))
        sign = -1 if output[0] < 0 else 1
        actual = sign * int(''.join(str(abs(digit)) for digit in output))
        assert actual == a * b


def test_apply_permutation_against_direct_scatter():
    rng = random.Random(45)
    for n in range(0, 25):
        for _ in range(8):
            p = list(range(n))
            rng.shuffle(p)
            values = list(range(n))
            rng.shuffle(values)
            expected = [None] * n
            for source, destination in enumerate(p):
                expected[destination] = values[source]
            assert apply_permutation(p, values) == expected


def test_matrix_rotation_four_turns_and_spiral_contents():
    for n in range(1, 14):
        matrix = [[row * n + col for col in range(n)] for row in range(n)]
        original = [row[:] for row in matrix]
        spiral = matrix_in_spiral_order(matrix)
        assert sorted(spiral) == list(range(n * n))
        assert len(spiral) == n * n
        for _ in range(4):
            rotate_matrix(matrix)
        assert matrix == original


def test_base_conversion_reference_roundtrip():
    rng = random.Random(139)
    for _ in range(300):
        value = rng.randrange(-10**9, 10**9)
        target_base = rng.randrange(2, 17)
        text = convert_base(str(value), 10, target_base)
        assert convert_base(text, target_base, 10) == str(value)


def test_linked_list_stable_pivot():
    rng = random.Random(85)
    for _ in range(300):
        values = [rng.randrange(0, 12) for _ in range(rng.randrange(0, 30))]
        pivot = rng.randrange(0, 12)
        expected = [x for x in values if x < pivot] + [x for x in values if x == pivot] + [x for x in values if x > pivot]
        assert list_pivot_values(values, pivot) == expected


def test_tree_reconstruction_from_preorder_and_inorder():
    def make(values):
        if not values:
            return None
        center = len(values) // 2
        return values[center], make(values[:center]), make(values[center + 1:])

    def preorder(tree):
        return [] if tree is None else [tree[0]] + preorder(tree[1]) + preorder(tree[2])

    def inorder(tree):
        return [] if tree is None else inorder(tree[1]) + [tree[0]] + inorder(tree[2])

    for n in range(0, 60):
        tree = make(list(range(n)))
        assert reconstruct_tree(preorder(tree), inorder(tree)) == tree


def test_quickselect_independent_sort():
    rng = random.Random(22)
    for n in range(1, 60):
        values = [rng.randrange(-30, 30) for _ in range(n)]
        expected = sorted(values, reverse=True)
        for k in range(1, n + 1):
            assert find_kth_largest(k, values) == expected[k-1]


def test_cover_set_against_brute_force():
    rng = random.Random(51)
    vocabulary = 'abcd'
    for _ in range(200):
        values = [rng.choice(vocabulary) for _ in range(rng.randrange(1, 14))]
        required = set(rng.sample(list(vocabulary), rng.randrange(1, 5)))
        candidates = [(i, j) for i in range(len(values)) for j in range(i, len(values)) if required <= set(values[i:j+1])]
        answer = smallest_subarray_covering_set(values, required)
        if not candidates:
            assert answer is None
        else:
            assert answer in candidates
            assert answer[1] - answer[0] == min(j-i for i,j in candidates)


def test_sequential_cover_against_brute_force():
    rng = random.Random(77)
    vocabulary = 'abcd'
    for _ in range(150):
        values = [rng.choice(vocabulary) for _ in range(rng.randrange(1, 14))]
        query = rng.sample(list(vocabulary), rng.randrange(1, 5))
        candidates = []
        for i in range(len(values)):
            for j in range(i, len(values)):
                it = iter(values[i:j+1])
                if all(any(candidate == q for candidate in it) for q in query):
                    candidates.append((i,j))
        answer = find_smallest_sequentially_covering_subset(values, query)
        if not candidates:
            assert answer is None
        else:
            assert answer in candidates
            assert answer[1]-answer[0] == min(j-i for i,j in candidates)


def test_word_decomposition_against_brute_force():
    rng = random.Random(57)
    for _ in range(140):
        text = ''.join(rng.choice('abc') for _ in range(15))
        words = [''.join(rng.choice('abc') for _ in range(2)) for _ in range(3)]
        permutations = {''.join(parts) for parts in itertools.permutations(words)}
        expected = [i for i in range(len(text)-6+1) if text[i:i+6] in permutations]
        assert find_all_substrings(text, words) == expected
