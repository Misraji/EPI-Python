# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_357_rotate_array import rotate_array_cycles,rotate_array,rotate_array_naive


@pytest.mark.parametrize('a', [[],[1],[1,2],[1,2,3,4,5],[1,2,3,4,5,6]])
@pytest.mark.parametrize('steps',[-11,-2,0,1,2,7,10])
def test_rotate_variants(a,steps):
    expected=a[-steps%len(a):]+a[:-steps%len(a)] if a and steps%len(a) else a[:]
    for fn in (rotate_array_cycles,rotate_array,rotate_array_naive):
        actual=a[:]
        fn(steps,actual)
        assert actual==expected
