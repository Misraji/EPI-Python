# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_398_calculate_trapping_water import calculate_trapping_water

@pytest.mark.parametrize('heights', [[], [1], [1,2,3], [3,2,1], [3,0,2,0,4], [0,1,0,2,1,0,1,3,2,1,2,1]])
def test_volume(heights):
    expected = sum(max(0, min(max(heights[:i+1]), max(heights[i:])) - h)
                   for i,h in enumerate(heights))
    assert calculate_trapping_water(heights) == expected
