# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_402_find_best_proposals import HighwaySection,find_best_proposals


def test_highways():
    h=[HighwaySection(0,1,5), HighwaySection(1,2,5)]
    a=HighwaySection(0,2,2)
    b=HighwaySection(0,2,20)
    assert find_best_proposals(h,[a,b],3)==a
    assert find_best_proposals(h,[b],3) is None
    assert find_best_proposals(h,[],3) is None
