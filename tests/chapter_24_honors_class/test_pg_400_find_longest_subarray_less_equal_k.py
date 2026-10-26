# pytest documentation: https://docs.pytest.org/en/stable/
import random

from epi_python.chapter_24_honors_class.pg_400_find_longest_subarray_less_equal_k import find_longest_subarray_less_equal_k


def oracle(data,k):
    return max([j-i for i in range(len(data)) for j in range(i+1,len(data)+1)
                if sum(data[i:j])<=k] or [0])


def test_examples():
    assert find_longest_subarray_less_equal_k([],10)==0
    rng=random.Random(123)
    for n in range(9):
        for _ in range(40):
            data=[rng.randrange(-7,8) for _ in range(n)]
            k=rng.randrange(-10,11)
            assert find_longest_subarray_less_equal_k(data,k)==oracle(data,k)
