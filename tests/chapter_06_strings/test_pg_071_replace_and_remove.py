"""Independent tests for EPI 6.4.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_06_strings.pg_071_replace_and_remove import replace_and_remove

@pytest.mark.parametrize(("args", "expected"), [
    ((4, ["a", "b", "a", "c", "", ""]), ["d","d","d","d","c"]),
    ((4, list("bbcc")), ["c","c"]),
    ((0, []), []),
    ((3, list("aba")), ["d","d","d","d"]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert replace_and_remove(*copy.deepcopy(args)) == expected



def test_textbook_replace_and_remove_contract_and_random_cases():
    from epi_python.chapter_06_strings.pg_071_replace_and_remove import replace_and_remove_in_place
    import random
    rng=random.Random(6104)
    for size in range(24):
        for _ in range(15):
            original=[rng.choice('aabcd') for _ in range(size)]
            want=list(''.join('dd' if c=='a' else '' if c=='b' else c for c in original))
            buffer=original+['']*size
            identity=id(buffer)
            result=replace_and_remove_in_place(size,buffer)
            assert result==len(want) and id(buffer)==identity
            assert buffer[:result]==want
