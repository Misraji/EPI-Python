# Exercise 17.6: The gasup problem

**Printed textbook page:** 267. **Reference transcription pages:** 267–268.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 267 (PDF page 281)

```text
for it in input-stream:
if candidate-count == 0:
candidate , candidate_count = it, 
candidate_count +
elif candidate == it:
candi.date-count += 1
else:
candidate_count -= I
return candidate
Since we sPend O(1) time per entry, the time complexity is O(n). The additional space complexity
is O(1).
The code above assumes a majority word exists in the sequence. If no word has a strict majority/
it still refums a word from the stream, albeit without any meaningful guarantees on how common
that word is. We could check with a second pass whether the retumed word was a majority. Similar
ideas can be used to identify words that appear more than nlk ttrnes in the sequence, as discussed
in Problem 24.33 on Page 399.
17.6 THr cesup pRoBLEM
In the gasup problem, a number of cities are arranged on a circular road. You need to visit all the
cities and come back to the starting city. A certain amount of gas is available at each city. The
amount of gas summed up over all cities is equal to the amount of gas required to go around the
road once. Your gas tank has unlimiled capacity. Call a city arnple if you can begin at that city with
an empty tank, refill at it, then travel through all the remaining cities, refilling at each, and retum
to the ample city, without running out of gas at any point. See Figure 77.2 for an example.
200 M
30c
600 M
5C
$
c
$
D
400 M
25G *p E
600 M
20G
$
B
900 M
F
A
$
$
10c
50c
200 M
100 M
Figure 17.2: The length of the circular road is 3000 miles, and your vehicle gets 20 miles per gallon. The distance noted
at each city is how far it is from the next city. For this configuration, we can begin with no gas at City D, and complete
the circuit successfully, so D is an ample city.
Given an instance of the gasup problem, how would you efficiently compute an ample city? You
can assume that there exists an ample city.
Hlzf; Think about starting with more than enough gas to complete the circuit without gassing up. Track the
amount of gas as you perform the circuit, gassing up at each city.
Solution: The brute-force approach is to simulate the traversal from each city. This approach has
trrneO(nz) time complexity, where n is the number of cities.
--,
G
$
10c
267
```

#### Printed page 268 (PDF page 282)

```text
Greedy approaches, e.g., finding the city with the most gas, the city closest to the next city, or
the city with best distance-to-gas ratio, do not work. For the given example, A has the most gas,
but you cannot get to C starthg from A. The city G is closest to the next city (A), and has the lowest
distance-to-gas ratio (100/10) but it cannot get to D.
We can gain insight by looking at the graph of the amount of gas as we perform the traversal.
See Figure 17.3 for an example. The amount of gas in the tank could become negative, but we ignore
the physical impossibility of that for now These graphs are the sarne up to a translation about the
Y-axis and a cyclic shift about the X-axis.
[:r particular, consider a city where the amount of gas in the tank is minimum when we enter
that city. Observe that it does not depend where we begin from-because graphs are the same up to
translation and shifting, a city that is minimum for one graph will be a minimum city for all graphs.
Let zbe a city where the amount of gas in the tank before we refuel at that city is minimum. Now
suppose we pick z as the starting point, with the gas present at z. Since we never have less gas than
we started with at z, Nrdwhen we retum to z we have 0 gas (since it's given that the total amount of
gas is just enough to complete the traversal) it means we can complete the joumey without running
out of gas. Note that the reasoning given above demonstrates that there always exists an ample
city.
9
0
5
4
o:
a2
r. 
I
0
-1
D
77
F
,27 
,29 30
c
cl
21
Dstance (x100M
(a) Gas vs. distance, starting at A.
A
D
30
c
28
B
F
D
0
5
4
3
2
1
0
g
(,
G
10 
t2 13
22
Distmce (x 100M)
(b) Gas vs. distance, starting at D.
Flgure 17.3r Gas as a function of distance for ditferent starting cities for the configuration in Figure '17.2 on the
preceding page.
The computation to determine z can be easily performed with a single pass over all the cities
simulating the changes to amount of gas as we advance.
IIPG = 20
# galTonsli] is the anount of gas in city i, and distancesfiJ is the
# distance city i to the next city.
def find-amp1e-city(gaIlons, distances) :
remaining-galIons = 0
268
```
