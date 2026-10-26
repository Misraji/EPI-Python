# Exercise 17.3: The interval covering problem

**Printed textbook page:** 262. **Reference transcription pages:** 262–263.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 262 (PDF page 276)

```text
def minimum-tota1-waiting-time (service-times) :
# Sort the service tifies in increasing order,
service-times. sort o
total-waiting-time = 0
for i, service-time in enunerate(service-times) :
num-remaining-queries = len(service-times) - (i + 1)
total-waiting-time 
+= service-time * nun-remaining-queries
return total-waiting-time
The time complexity is dominated by the time to sort/ i.e./ O(nlogn)
17.3 Tnr rNrrnvel covERING pRoBLEM
Consider a foreman responsible for a number of tasks on the factory floor. Each task starts at a fixed
time and ends at a fixed time. The foreman wants to visit the floor to check on the tasks. Your job
is to help him minimize the number of visits he makes. In each visit, he can check on all the tasks
taking place at the time of the visit. A visit takes place at a fixed time, and he can only check on
tasks taking place at exactly that time. For example, if there are tasks at times 10,3f,12,61,13,41,16,9),
then visit times 0,2,3,6 cover all tasks. A smaller set of visit times that also cover all tasks is 3,6. In
the abstract, you are to solve the following problem.
You are given a set of closed intervals. Design an efficient algorithm for finding a minimum sized
set of numbers that covers all the intervals.
Hint: Think about extremal points.
Solution: Note that we c€u:r restrict our attention to numbers which are endpoints without losing
optimality. A brute-force approach might be to enumerate every possible subset of endpoints,
checking for each one if it covers all intervals, and if so, determining if it has a smaller size than any
previous such subset. Since a set of size k has 2k subsets, the time complexity is very high.
We could simply retum the left end point of each interval, which is fast to compute but, as
the example in the problem statement showed, may not be the minimum number of visit times.
Similarly, always greedily picking an endpoint which covers the most intervals may also lead to
suboptimum results, e.g., consider the six intervals 11.,27,12,3),13,4),12,37,13,41,14,5]. The point 3
appears in four intervals, more than any other point. However, if we choose 3, we do not cover
[1,2] and [4,5], so we need two additional points to cover all six intervals. If we pick 2 and 4, each
individually covers just three intervals, but cornbined they cover all six.
It is a good idea to focus on extreme cases. [n particulal, consider the interval that ends first, i.e.,
the interval whose right endpoint is minimum. To cover it, we must pick a number that appears in
it. Furthermore, we should pick its right endpoint, since any other intervals covered by a number
in the interval will continue to be covered if we pick the right endpoint. (Otherwise the interval we
began with carurot be the interval that ends first,) Once we choose that endpoint, we can remove
all other covered intervals, and continue with the remaining set.
The above observation leads to the following algorithm. Sort all the intervals, comparing on
right endpoints. Select the first interval's right endpoint. Iterate through the intervals, looking for
the first one not covered by this right endpoint. As soon as such an interval is found, select its right
endpoint and continue the iteration.
For the given example,11.,21,12,3),13,4],12,31,13,47,[4,5], after sorting on right endpoints we
get11,,2l,12,3),12,31,13,4\,13,41,[4,5]. The leftmost right endpoint is 2, which covers the first three
intervals. Therefore, we select 2, and as we iterate, we see it covers 11,,2),12,3), [2,3]. U/hen we get
262
```

#### Printed page 263 (PDF page 277)

```text
to f3,4f, we select its right endpoint, i.e., 4. This covers f3,41,13,47,[4,5]. There are no remaining
intervals, so 12,41is a minimum set of points covering all intervals.
Interval = collections.namedtuple('Interval', 
('1eft,,'right,))
def find-nininum-visits (intervals) 
:
# Sort intervais based on the right endpoints.
intervals . sort (key=operator . attrgetter (' ri ght' ) )
last-visit_time, 
num_visits = float('-inf'), 
0
:for interval in intervals:
if interval.Ieft 
> last_visit_time:
# The current right endpoint, Iast_vjsit*time, 
will not cover any
# nore interyal.s.
last_visit_time = interval.right
num-visits += 1
return num_visits
Since we sPend O(1) time per index, the time complexity after the initial sort isO(n),where n is the
number of intervals. Therefore, the time taken is dominated by the initial sort, i.e., O(nlogn).
Figure 17.1 : An instance of the minimum ray covering problem, with 12 partially overlapping arcs. Arcs have been
drawn at different distances for illustration. For this instance, six cameras are sufficient, corresponding to the six rays.
Varianh You are responsible for the security of a castle. The castle has a circular perimeter. A total
of z robots Patrol the perimeter---€ach robot is responsible for a closed connected subset of the
perimeter, i.e., an arc. (The arcs for different robots may overlap.) You want to monitor the robots
by installing cameras at the center of the castle that look out to the perimeter. Each camera can look
along a ray. To save cost, you would like to minimize the number of cameras. See Figure 17.'J, for
an example.
Variant There are a number of points in the plane that you want to observe. You are located at the
point (0,0). You can rotate about this point, and your field-of-view is a fixed angle. Which direction
should you face to maximize the number of visible points?
Inaaiants
A common aPProach to designing an efficient algorithm is to use invariants. Briefly, an invariant is
a condition that is true during execution of a program. This condition may be on the values of the
263
```
