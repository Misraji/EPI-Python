# Exercise 17.1: Compute an optimum assignment of tasks

**Printed textbook page:** 260. **Reference transcription pages:** 260–260.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 260 (PDF page 274)

```text
Greedy algorithms b o o t camp
For US currency, wherein coins take values L,5, 10,25,50,100 cents, the greedy algorithm for making
change results in the minimum number of coins. Here is an implementation of this algorithm. Note
that once it selects the number of coins of a particular value, it never changes that selection; this is
the hallmark of a greedy algorithm.
def change-making (cents) :
COINS = [100, 50, 25, 10, 5, 1]
num-coins = 0
for coin in C0INS:
num-coins += cents // coin
cents %= coin
return num-coins
We perform 6 iterations, and each iteration does a constant amount of computation, so the time
complexity is O(1).
often the right choice
an optimization pro
SA
set of choices to select from.
It's often easier to conceptualize a greedy algorithm recursively, and then implement it using
iteration for higher performance.
Even if the greedy approach does not yield an optimum solution, it can give insights into the
optimum algorithm, or serve as a heuristic,
Sometimes the correct greedy
is not obvious.
Table 17.1 : Top Tips for Greedy Algorithms
17.1 Colrpurr AN oprrMUM ASSIGNMENT oF TASKS
We consider the problem of assigning tasks to workers. Each worker must be assigned exactly two
tasks. Each task takes a fixed amount of time. Tasks are independent, i.e., there are no constraints of
the form "Task 4 cannot start before Task 3 is completed ." Any task can be assigned to any worker.
We want to assign tasks to workers so as to minimize how long it takes before all tasks are
completed. For example, if there are 6 tasks whose durations ate 5,2,1,6,4,4 hours, then an
optimum assignment is to give the first two tasks (i.e., the tasks with duration 5 and 2) to one
worker, the next two (1 and 6) to another worke1 and the last two tasks (4 and 4) to the last worker.
For this assignment, all tasks will finish after max(5 + 2,1 + 6,4 + 4) = 8 hours.
Design an algorithm that takes as input a set of tasks and retums an optimum assignment.
Hint: What additional task should be assigned to the worker who is assigned the longest task?
Solution: Simply enumerating all possible sets of pairs of tasks is not feasible-there are too many
of them. (The precise number assignments is (;)(";')(";^l . . .ti>til = nllZnlz, where n is the number
of tasks.)
Instead we should look more carefully at the structure of the problem. Extremal values are
important-the task that takes the longest needs the most help. In particular, it makes sense to pair
the task with longest duration with the task of shortest duration. This intuitive observation can be
understood by looking at any assignment in which a longest task is not paired with a shortest task.
260
```
