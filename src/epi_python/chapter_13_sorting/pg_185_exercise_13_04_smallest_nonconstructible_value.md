# Exercise 13.4: Smallest nonconstructible value

**Printed textbook page:** 185. **Reference transcription pages:** 185–185.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 185 (PDF page 199)

```text
def --init-_(self , first-name, last_name) :
self. first_name, self. last_name = first*name, Iast_name
def --eq--(self, 
other):
return self.first*name == other.first_name
def --1t--(self, other):
return (self. first_name < other. first_name
if self.first-name != other.first_name else
se1f. Iast-name < other. last_name)
def eliminate-duplicate (A) :
A.sortO 
# Ilakes identical elernents becone neighbors
write-idx = 1
for cand in A[1:]:
if cand != Alwrite_idx - 1]:
AIwrite-idx] = cand
write-idx += 1
del AIwrite-idx: ]
The time complexity is O(nlogn) and the space complexity is O(1).
13.4 Slaarrssr NoNcoNSTRUcTTBLE vALUE
Given a set of coins, there are some arnounts of change that you may not be able to make with them,
e.9., you cannot create a change amount greater than the sum of the your coins. For example, if
your coins are 1,1.,1,1.,1.,5,10,25, then the smallest value of change which cannot be made is 21.
Write a program which takes an array of positive integers and retums the smallest number which
is not to the sum of a subset of elements of the array.
Hlnf: Manually solve for a few short arrays.
Solution: A brute-force approach would be to enumerate all possible values, starting from 1, testing
each value to see if it is the sum of array elements. Howeveq, there is no simple efficient algorithm
for checking if a given number is the sum of a subset of entries in the array. Heuristics may be
employed, but the program will be unwieldy.
We can get a great deal of insight from some small concrete examples. Observe that (1,2)
ProducesL,2,3,Nrd(1,3)producesL,3,4. Atrivialobservationisthatthesmallestelementinthe
array sets a lower bound on the change amount that can be constructed from that array, so if the
array does not contain a L, it cannot produce 1. However, it may be possible to produce 2 without
a 2 being present, since there can be 2 or more 1s present.
Continuing with a larger example, <L,2,4) produces 7,2,3,4,5,6,7, and <1,2,5) produces
7,2,3,5,6,7,8. Generalizing/ suppose a collection of numbers can produce every value up to
and including V, but not V + 1. Now consider the effect of adding a new element u to the collection.
lfuSV+1,wecanstillproduceeveryvalueuptoandincludingV+uandwecannotproduce
V+u+ 1. Ontheotherhand, If u>V+l,thenevenbyaddingutothecollectionwecannotproduce
V +7.
185
```
