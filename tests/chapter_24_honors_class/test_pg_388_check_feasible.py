# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_388_check_feasible import Jug,check_feasible


def test_jugs():
    j=[Jug(200,210),Jug(500,510)]
    assert check_feasible(j,400,430)
    assert not check_feasible(j,100,110)
    assert check_feasible(j,1000,1050)


def test_unusable():
    assert not check_feasible([],100,200)
