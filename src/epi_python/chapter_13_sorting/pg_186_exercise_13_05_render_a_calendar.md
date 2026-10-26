# Exercise 13.5: Render a calendar

**Printed textbook page:** 186. **Reference transcription pages:** 186–187.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 186 (PDF page 200)

```text
Another observation is that the order of the elements within the array makes no difference to
the amounts that are constructible. However, by sorting the array allows us to stop when we reach
a value that is too large to help, since all subsequent values are at least as large as that value.
Specifically, let M[i - 1] be the maximum constructible amount from the first I elements of the sorted
array. If the next array element r is greater than Mli-1)+1., M[i- 1] is still the maximum constructible
amount,sowestop andretum Mli-1'l+ l astheresult. Otherwise,wesetM[l] =Mli- 1] +rand
continue with element (l + 1).
To illustrate, suppose we are given <L2,2,L,15,2,4>. This sorts to (1,2,2,4,12,15>. The maximum
constructible amount we can make with the first element is L. The second element, 2, is less than
or equal to 1 + 1, so we can produce all values up to and including 3 now. The third element, 2,
allows us to produce a1l values up to and including 5. The fourth element,4, allows us to produce
all values up to 9. The fifth element, 12 is greater than 9 + 1, so we cannot produce 10. We stop-10
is the smallest number that cannot be constructed.
The code implementing this approach is shown below.
def smallest-nonconstructible-vaIue (A) :
max-constructible-value = 0
for a in sorted(A):
if a > max-constructible-value + 1
breaL
max-constructible-value += a
return max-constructible-value + 1
The time complexity as a function of n, the length of the arcay, is O(n log n) to sort and O(n) to iterate,
i.e., O(nlogn).
13.5 RrNpnn A cALENDAR
Consider the problem of designing an online calendaring application. One component of the design
is to render the calendar, i.e., display it visually.
Suppose each day consists of a number of events, where an event is specified as a start time and
a finish time. Individual events for a day are to be rendered as nonoverlapping rectangular regions
whose sides are parallel to the X- and Y-axes. Let the X-axis correspond to time. If an event starts
at time b and ends at time e, the upper and lower sides of its corresponding rectangle must be at b
and e, respectively. Figure 13.L on the facing page represents a set of events.
Suppose the Y-coordinates for each day's events must lie between 0 and L (a pre-specified
constant), and each event's rectangle must have the same "height" (distance between the sides
parallel to the X-axis). Your task is to compute the maximum height an event rectangle can have.
hr essence, this is equivalent to the following problem.
Write a program that takes a set of events, and determines the maximum number of events that
take place concurrently.
Hint: Focus on endpoints.
Solution: The number of events scheduled for a given time changes only at times that are start or
end times of an event. This leads the following brute-force algorithm. For each endpoint, compute
the number of events that contain it. The maximum number of concurrent events is the maximum
of this quantity over all endpoints. If there are n intervals, the total number of endpoints is 2n.
186
```

#### Printed page 187 (PDF page 201)

```text
rE8 l
-
E9
I
E5
FII
1
L
L
E3
l
tt-
J
0 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 11 12 13 1,4 15 L6 17
E1
E2
rE4 1
-
Figure 13.1 : A set of nine events. The earliest starting event begins at time 1; the latest ending event ends at time 17
The maximum number of concurrent events is 3, e.g., {E1, E5, E8} as well as others.
Computing the number of events containing an endpoint takes O(n) time, since checking whether an
interval contains a point takes O(1) time. Therefore, the overall time complexity isO(Znxn) = O(n2).
The inefficiency in the brute-force algorithm lies in the fact that it does not take advantage of
localiry i.e., as we move from one endpoint to another. trfuitively, we can improve the run time by
sorting the set of all the endpoints in ascending order. (If two endpoints have equal times, and one
is a start time and the other is an end time, the one corresponding to a start time comes first. If both
are start or finish times, we break ties arbitrarily.)
Now as we proceed through endpoints we can incrementally track the number of events taking
place at that endpoint using a counter. For each endpoint that is the start of an interval, we increment
the counter by 1, and for each endpoint that is the end of an interval, we decrement the counter by
1. The maximum value attained by the counter is maximum number of overlapping intervals.
For the example in Figure 13.L, the first seven endpoints are 1(start), 2(start), 4(start), S(end),
S(end), 6(start), 7(end). The counter values are updated to 1,2,3,2, L,2,1..
# Event is a tuple (start_tifle , end_tine)
Event = collections . namedtuple ('Event ' , (' start ' , 'finish') 
)
# Endpoint is a tuple (start_tine , 0) or (end_tire , t) so that jf tjnes
# are equa7, start-tine 
cones first
Endpoint = collections.nanedtuple('Endpoint', 
('time','is-start'))
def find-rnax-simultaneous-events (A) :
# Builds an array of al7 endpoints.
E = ([Endpoint (event. start , True)
for event in el + [Endpoint(event.finish, Fa1se) for event in A])
# Sorts the endpoint array according to the tine, breaking ties by putting
# statt times before end tines.
E.sort(key=Ianbda e: (e.time, not e.is-start))
# Track the nunber of sirau.Itaneous eyents, record the maximum nunber of
# simultaneous eyents.
nax-num-simultaneous_events, num_simultaneous_events = 0, 0
for e in E:
if e. is-start:
num-simultaneous_events += 1
max_nun_simultaneous_events = nat(num_simultaneous_events,
max-num-simultaneous_events )
else:
num-simultaneous_events -= 1
return max-num_simultaneous_events
1,87
```
