# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_18_graphs.pg_278_flip_color import flip_color,flip_color_recursive


@pytest.mark.parametrize('fn',[flip_color,flip_color_recursive])
def test_connected_component(fn):
    a=[[1,1,0],[1,0,0],[0,0,1]]
    fn(0,0,a)
    assert a==[[0,0,0],[0,0,0],[0,0,1]]


@pytest.mark.parametrize('fn',[flip_color,flip_color_recursive])
def test_single(fn):
    a=[[1]]
    fn(0,0,a)
    assert a==[[0]]
