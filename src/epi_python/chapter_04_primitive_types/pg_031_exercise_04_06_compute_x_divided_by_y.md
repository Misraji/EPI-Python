# Exercise 4.6: Compute x divided by y

**Printed textbook page:** 31. **Reference transcription pages:** 31–31.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 31 (PDF page 45)

```text
The time complexity of addition is O(n), where rz is the number of bits needed to represent the
operands. Since we do r additions to perform a single multiplication, the total time complexity is
o(n2).
4.6 Colaeurn x/y
Given two positive integers, compute their quotient, using only the addition, subtraction, and
shifting operators.
Hint:Relate xly to (x - y)ly.
Solution: A brute-force approach is to iteratively subtract y from r until what remains is less than
y. The number of such subtractions is exactly the quotient, xf y, and the remainder is the term that's
less than y. The complexity of the brute-force approach is very hi gh, e.g.,when y = L and r = 231 -1,
it will take 231 - 1 iterations.
A better approach is to try and get more work done in each iteration. For example, we can
compute the largest k such that 2!'y < x, subtract 2l'y frorn x, and add 2ft to the quotient. For
example,i6s=(1011)zandA=(l})z,thenk=2,since2x22< 
11 and2x23> 11. Wesubtract
(1000)2 from (1011)2 to get (11)2, add2l' = 22 = (100)2 to the quotient, and continue by updating r to
(11h.
The advantage of using 2ky is that it can be computed very efficiently using shifting, and r is
at least halved in each iteration. If it takes rz bits to represent xly, there are O(n) iterations. If the
largest k such that 2ky < r is computed by iterating through k, each iteration has time complexity
O(rz). This leads to anO(nz) algorithm.
A better way to find the largest k in each iteration is to recognize that it keeps decreasing.
Therefore, instead of testing in each iteration whether 20y,21y,22y,. . . is less than or equal to r, after
we initially find the largest k suchthat2ky 1 x, hsubsequent iterations we test2k-ty,2k-2y,2k-3y, . . .
with x.
For the example given earlier, after setting the quotient to (100)2 we continue with (11)2. Now
the largest k such that2ky < (11)z is 0, so we add 20 = (1)z to the quotient, which is now (101)2.
We continue with (11)2 - (10)2 = (1)2. Since (1)2 < !,we are done-the quotient is (101)2 and the
remainder is (1)2.
def divide (x , y) :
result, power = 0, 32
y_power=y<<power
rhile x >= y:
while y-power > x:
Y-Power >>= 1
Power -= 1
result += 1 << power
x _= y_power
return result
In essence, the program applies the grade-school division algorithm to binary numbers. With each
iteration, we process an additional bit. Therefore, assuming individual shift and add operations
take O(1) time, the time complexity isO(n).
31
```
