# Exercise 13.11: Compute a salary threshold

**Printed textbook page:** 195. **Reference transcription pages:** 195–196.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 195 (PDF page 209)

```text
# Find the nidpoint of L using a sTow and a fast pointer.
pre-sIow, slow, fast = None, L, L
while fast and fast. next:
pre-slow = slolr
fast , slow = fast . next. next , slow. next
pre-slow.next = None # SpJits the list 
into two equaT-sized ljsts.
return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(s1ow))
The timecomplexity is the same as that of mergesort,i.e.,O(nlogn). Thoughno memory is explicitly
allocated, the space complexity is O(logr). This is the maximum function call stack depth, since
each recursive call is with an argument that is half as long.
1,3.17 CoMpurs A sALARY THREsHoLD
You are working in the finance office for ABC corporation. ABC needs to cut payroll expenses to a
specified target. The chief executive officer wants to do this by putting a cap on last year's salaries.
Every employee who eamed more than the cap last year will be paid the cap this year; employees
who eamed no more than the cap will see no change in their salary.
For example, if there were five employees with salaries last year were $90, $30, $100, $40, and g20,
and the target payroll this year is $210, then 60 is a suitable salary cap, since 60+30 +60+40+20 = 210.
Design an algorithm for computing the salary cap, given existing salaries and the target payroll.
Hint: How does the pay,roll vary with the cap?
Solution: Brute-force is not much use-there are an infinite number of possibilities for the cap.
The cap lies between 0 and the maximum current salary. The payroll increases with the cap,
which suggests usingbinary search in this range-if a cap is too high, no higher cap will work; the
same is true if the cap is too low.
Suppose there are n employees. Let the array holding salary data be A. The payroll, P(c), implied
by a cap of c is f,[j min(atl], c). Each step of the binary search evaluating P(c) which takes time
O(n). As in Solution 11.5 on Page 149, the number of binary search steps depends on the largest
salary and the desired accuracy.
We can use a slightly more analytical method to avoid the need for a specified tolerance. The
intuition is that as we increase the cap, as long as it does not exceed someone's salary, the payroll
increases linearly. This suggests iterating through the salaries in hcreasing order. Assume the
salaries are given by an array A, which is sorted. Suppose the cap for a total payroll of T is known
to lie between the kth and (k + 1)th salaries. We want Z!=i Atil + @ - k)c to equal = T, which solves
toc = (r -fltratillt(/ *k).
For the given example, A = (20,30,40,90,100), and r = 2Lo. The payrolls for caps equal to
the salaries in A are (100, 140, 170,270,280). Since T = 270lies between 170 and 270, the cap lies
between the 40 and 90. For any cap c between 40 and 90, the implied payroll is 20 + 30 + 40 + 2c.
We want this to be 210,so we solve 20 + 30 + 40 + 2c = 210 for c, yieldin g c = 60.
def find-salary-cap(target_payrol1, current_salaries) :
current_salaries . sort o
unadjusted-salary-sum = 0.0
for i, current_salary in enunerate(current_salaries)
adjusted-people = Ien(current_salaries) - i
195
```

#### Printed page 196 (PDF page 210)

```text
adjusted-salary-sum = current-salary * adjusted-people
if unadjusted-salary-sum + adjusted-salary-sum >= target-payroll:
return (target-payroll - unadjusted-salary-sum),/ adjusted-people
unadjusted-salary-sun += current-salary
# ivo solution, since targex-payro-ll > existing payroL7.
return -1.0
The most expensive operation for this entirc solution is sorting A, hence the run time is O(nlogn).
Once wehaveA sorted, we simply iteratethroughits entries lookingforthe firstentrywhichimplies
a payroll that exceeds the target, and then solve for the cap using an arithmetical expression.
If we are given the salary array sorted in advance as well as its prefix sums, then for a given
value of T, we can use binary search to get the cap in O(logn) time.
Varianfi Solve the same problem using only O(1) space.
196
```
