"""EPI Python — Exercise 17.6: The Gasup Problem

Chapter 17: Greedy Algorithms and Invariants
Textbook: pages 267–269 (printed page numbers; problem on 267, solution and
Figure 17.3 on 268, end of the program, complexity and variant on 269).

PROBLEM (from the textbook)
---------------------------
In the gasup problem, a number of cities are arranged on a circular road.
You need to visit all the cities and come back to the starting city. A
certain amount of gas is available at each city. The amount of gas summed
up over all cities is equal to the amount of gas required to go around the
road once. Your gas tank has unlimited capacity. Call a city ample if you
can begin at that city with an empty tank, refill at it, then travel
through all the remaining cities, refilling at each, and return to the
ample city, without running out of gas at any point. See Figure 17.2 for an
example.

Given an instance of the gasup problem, how would you efficiently compute
an ample city? You can assume that there exists an ample city.

Figure 17.2 (book): the circular road is 3000 miles long and the vehicle
gets 20 miles per gallon. Going around the circle the cities, their gas
and their distance to the next city are: A 50G, 900M; B 20G, 600M;
C 5G, 200M; D 30G, 400M; E 25G, 600M; F 10G, 200M; G 10G, 100M (back to
A). Starting with no gas at city D completes the circuit, so D is an ample
city.

HINT (from the textbook)
------------------------
Think about starting with more than enough gas to complete the circuit
without gassing up. Track the amount of gas as you perform the circuit,
gassing up at each city.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: simulate the trip starting from every city. That is O(n^2)
time for n cities.

Simple greedy rules do not work: picking the city with the most gas, the
city closest to its next city, or the city with the best distance-to-gas
ratio. In the example, A has the most gas, but starting at A you cannot
reach C. City G is closest to its next city (A) and has the lowest
distance-to-gas ratio (100/10), yet starting at G you cannot reach D.

Insight: plot the amount of gas in the tank against distance travelled
(book Figure 17.3: (a) starting at A, (b) starting at D). Allow the amount
to go negative for the sake of the picture. The graphs for different
starting cities are identical up to a vertical translation and a cyclic
shift along the distance axis.

So look at the city where the tank level on ARRIVAL (before refuelling) is
minimum. Because the graphs differ only by translation and shifting, a city
that is minimum on one graph is minimum on every graph — it does not
depend on where we started. Call it z. Start at z: we never have less gas
than we had on arrival at z, i.e. never below 0, and on returning to z we
have exactly 0 gas (total gas exactly suffices). So the trip succeeds.
This argument also shows that an ample city always exists.

Finding z needs a single pass over the cities, simulating the change in gas
as we advance and remembering where the running total is smallest. The
book's implementation is find_ample_city(gallons, distances), with
MPG = 20.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    gallons=[2, 0, 3], distances=[20, 40, 40]  (MPG = 20)
    Legs need 1, 2, 2 gallons. Running surplus on arriving at city 1 is
    2 - 1 = 1, at city 2 it is 1 + (0 - 2) = -1 (the minimum), so city 2
    is ample: 3 - 2 = 1, 1 + 2 - 1 = 2, 2 + 0 - 2 = 0.
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
import collections


# Miles per gallon used to convert each distance into gallons needed, as in
# the book's figure (20 miles per gallon).
MPG = 20

# collections.namedtuple creates a small immutable tuple class with named
# fields. A CityAndRemainingGas(city, remaining_gallons) records the city
# at which the running gas total was lowest so far, and that lowest total.
# Fields can be read as .city and .remaining_gallons. (The book defines this
# class inside the function; here it is module level.)
CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas', ('city','remaining_gallons'))


# Type hints document two lists of ints and an int result (the index of an
# ample city). Python does not enforce annotations at run time.
def find_ample_city(gallons: list[int], distances: list[int]) -> int:
    """The book assumes total available gallons suffice for the circular tour.

    The textbook's implementation: gallons[i] is the amount of gas in city
    i, and distances[i] is the distance from city i to the next city. The
    input validation (ValueError) is an addition not in the book.
    """

    # Added safety check (not in the book). `raise ValueError(...)` stops
    # the function with an exception if the lists differ in length or are
    # empty (`not gallons` is True for an empty list).
    if len(gallons) != len(distances) or not gallons:
        raise ValueError('Each city must have a gas amount and outbound distance')

    # Running tank level relative to starting at city 0 with an empty tank.
    remaining_gallons = 0

    # Best (lowest) arrival level seen so far: arriving at city 0 at the
    # very start, the level is 0.
    city_remaining_gallons_pair = CityAndRemainingGas(0,0)

    # range(1, n) visits arrivals at cities 1 .. n-1. On each step we add
    # the gas picked up at the previous city and subtract the gas burned on
    # the leg to this city. `//` is floor (integer) division, converting
    # miles to whole gallons.
    for i in range(1,len(gallons)):
        remaining_gallons += gallons[i-1] - distances[i-1] // MPG

        # A new minimum arrival level: remember this city. Namedtuples are
        # immutable, so a new one is created rather than updated.
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(i,remaining_gallons)
    return city_remaining_gallons_pair.city


# TEXTBOOK POST-SOLUTION DISCUSSION (page 269)
# --------------------------------------------
# One pass over the cities: time complexity O(n), space complexity O(1).
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Solve the same problem
# when you cannot assume that there exists an ample city.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - MPG = 20: same as the book.
# - Book: `def find_ample_city(gallons, distances):` with the comment
#   "gallons[i] is the amount of gas in city i, and distances[i] is the
#   distance city i to the next city" above it. File: same name and
#   parameters, type hints added; the comment's content is in the
#   docstring.
# - Book defines CityAndRemainingGas INSIDE the function; the file defines
#   it at module level.
# - Book stores `num_cities = len(gallons)` and loops over
#   `range(1, num_cities)`; the file calls len(gallons) directly.
# - The file adds an input check that raises ValueError for empty input or
#   mismatched list lengths; the book has no validation.
# - Core arithmetic and minimum tracking are identical.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added three-city example (see ADDITIONAL EXAMPLES in the module
    # docstring): city 2 is where the running gas total is lowest, so it is
    # the ample city.
    gallons=[2,0,3]
    distances=[20,40,40]
    city=find_ample_city(gallons,distances)
    print('Ample city:',city)

    # `assert` raises AssertionError if the condition is False; a quick
    # smoke check, while pytest does the thorough testing.
    assert city==2
