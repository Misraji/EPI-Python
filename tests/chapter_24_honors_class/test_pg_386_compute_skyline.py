# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_386_compute_skyline import Rectangle,compute_skyline


def test_skyline():
    buildings=[Rectangle(0,2,2),Rectangle(1,3,4),Rectangle(4,4,1)]
    rectangles=compute_skyline(buildings)
    skyline={x:r.height for r in rectangles for x in range(r.left,r.right+1)}
    for x in range(5):
        assert skyline[x]==max([b.height for b in buildings if b.left<=x<=b.right] or [0])


def test_empty():
    assert compute_skyline([])==[]
