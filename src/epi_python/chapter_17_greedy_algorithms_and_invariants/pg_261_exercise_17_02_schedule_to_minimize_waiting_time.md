# Exercise 17.2: Schedule to minimize waiting time

**Printed textbook page:** 261. **Reference transcription pages:** 261–261.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 261 (PDF page 275)

```text
By swapping the task that the longest task is currently paired with with the shortest task, we get an
assignment which is at least as good.
Note that we are not claiming that the time taken for the optimum assignment is the sum of
the maximum and minimum task durations. Indeed this may not even be the cos€, €.g.r if the two
longest duration tasks are close to each other in duration and the shortest duration task takes much
less time than the second shortest task. As a concrete example, if the task durations are L,8,9,10,
the optimum delay is 8 + 9 = 17, notl + 10.
[r summary, we sort the set of task durations, and pair the shortest, second shortest, third
shortest, etc. tasks with the longest, second longest, third longest, etc. tasks. For example, if the
durations are 5,2,1.,6,4,4, then on sorting we get 1,2,4,4,5,6, and the pairings are (1.,6), (2,5), and
(4,4).
PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))
def optimum-task-a ssi gnment ( task-durations ) :
task-durations . sort o
return I
PairedTasks(task*durationslil, task_durations [-i])
for i in range(Ien(task_durations) // Z)
l
The time complexity is dominated by the time to sort, i.e., O(nlogn).
17.2 Scnnours ro MrNrMrzE wArrrNG TrME
A database has to respond to a set of client SQL queries. The service time required for each query
is known in advance. For this application, the queries must be processed by the database one at a
time, but can be done in any order. The time a query waits before its tum comes is called its waiting
time.
Given service times for a setof queries, compute a schedule forprocessingthe queries thatminimizes
the total waiting time. Retum the minimum waiting time. For example, if the service times are
<2,5,1.,3),if wescheduleinthegivenordeq,thetotalwaitingtimeis0+(2)+(2+5)+(2+5 
+1) =17.
If however, we schedule queries in order of decreasing service times, the total waiting time is
0+(5)+(5+3)+(5+3+2)=23.Aswewillsee,forthisexample,theminimumwaitingtimeisl0.
Hint:Focus on extreme values.
Solution: We can solve this problem by enumerating all schedules and picking the best one. The
complexity is very high-O(nl) to be precise, where n is the number of queries.
Intuitively, it makes sense to serve the short queries first. The justification is as follows. Since
the service time of each query adds to the waiting time of all queries remaining to be processed, if
we put a slow query before a fast one, by swapping the two we improve the waiting time for all
queries between the slow and fast query, and do not change the waiting time for the other queries.
We do increase the waiting time of the slow query, but this cancels out with the decrease in the
waiting time of the fast query. Hence, we should sort the queries by their service time and then
process them in the order of nondecreasing service time.
For the given example, the best schedule processes queries in increasing order of service times.
Ithasatotalwaitingtimeof0+(1)+(1+2)+(1+2+3)=l0.Notethatschedulingquerieswith
longer service times, which we gave as an earlier example, is the worst approach.
261
```
