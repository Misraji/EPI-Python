# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_359_rook_attack import rook_attack


@pytest.mark.parametrize('a',[[],[[0]],[[1,1],[1,1]],[[1,0],[1,1]],[[0,1],[1,1]],[[1,1,1],[1,0,1],[1,1,1]]])
def test_rook(a):
    original=[row[:] for row in a]
    if not a:
        assert rook_attack(a) is None
        return
    m,n=len(a),len(a[0])
    expected=[[0 if any(original[i][col]==0 for col in range(n)) or any(original[row][j]==0 for row in range(m)) else original[i][j]
               for j in range(n)] for i in range(m)]
    rook_attack(a)
    assert a==expected
