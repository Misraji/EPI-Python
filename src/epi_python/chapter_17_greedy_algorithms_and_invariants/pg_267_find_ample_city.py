"""EPI Python 17.6, textbook printed page 267: The gasup problem.

QUESTION: Given gas at each city and distances between successive cities, return a city where a full tour succeeds.

TEXTBOOK ALGORITHM: Find the city with minimum running surplus of gallons when arriving, using the textbook 20-miles-per-gallon assumption.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_17_greedy_algorithms_and_invariants.pg_267_find_ample_city
Test: python -m pytest tests/chapter_17_greedy_algorithms_and_invariants/test_pg_267_find_ample_city.py -v
"""

# collections.namedtuple documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
import collections


MPG = 20
CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas', ('city','remaining_gallons'))


def find_ample_city(gallons: list[int], distances: list[int]) -> int:
    """The book assumes total available gallons suffice for the circular tour."""
    if len(gallons) != len(distances) or not gallons:
        raise ValueError('Each city must have a gas amount and outbound distance')
    remaining_gallons = 0
    city_remaining_gallons_pair = CityAndRemainingGas(0,0)
    for i in range(1,len(gallons)):
        remaining_gallons += gallons[i-1] - distances[i-1] // MPG
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(i,remaining_gallons)
    return city_remaining_gallons_pair.city


if __name__ == '__main__':
    gallons=[2,0,3]
    distances=[20,40,40]
    city=find_ample_city(gallons,distances)
    print('Ample city:',city)
    assert city==2
