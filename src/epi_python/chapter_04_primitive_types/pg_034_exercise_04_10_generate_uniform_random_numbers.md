# Exercise 4.10: Generate uniform random numbers

**Printed textbook page:** 34. **Reference transcription pages:** 34–34.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 34 (PDF page 48)

```text
return x == 0
num-digits = math. floor(nath. Iogl0(x)) + 1
msd-mask = l0**(num-digits - 1)
for i in range(num-digits // 2):
if x // msd-mask != x X 10:
return FaIse
x %= msd-mask # Renove the nost significant digit of x
x //= L0 # Renove the least significant digix of x.
msd-mask //= 100
return True
The time complexity is O(n), and the space complexity is O(1). Alternatively, we could use Solu-
tion 4.8 on Page 32 to reverse the digits in the number and see if it is unchanged.
4.10 GnNEnrrs uNrFoRM RANDoM NUMBERS
This problem is motivated by the following scenario. Six friends have to select a designated driver
using a single unbiased coin. The process should be fair to everyone.
How would you implement a random number generator that generates a random integer I between a
and b, inclusive, given a random number generator that produces zero or one with equal probability?
All values nla,b) should be equally likely.
Hint: How would you mimic a three-sided coin with a two-sided coin?
Solution: Note that it is easy to produce a random integerbetween 0 and 2i-1, inclusive: concatenate
I bits produced by the random number generator. For example, two calls to the random number
generator will produce one of (00)2, (01)2, (10)2, (11)2. These four possible outcomes encode the four
integers 0,7,2,3, and all of them are equally likely.
For the general case, first note that it is equivalent to produce a random integer between 0 and
b - a, inclusive, since we can simply add a to the result. lf b - a is equal to 2i - 1, for some l, then we
can use the approach in the previous paragraph.
lf b - a is not of the form 2i - 7, we find the smallest number of the form 2' - 1 that is greater
than b - a. We generate an i-bit number as before. This l-bit number may or may not lie between 0
and b - a, inclusive. If it is within the range, we return it-all such numbers are equally likely. If it
is not within the range, we try again with I new random bits. We keep trying until we get a number
within the range.
For example, to generate a random number corresponding to a dice roll, i.e., a number between 1
and6,webeginbymakingthreecallstotherandomnumbergenerator(since22-1 
< (6-1) <23-1).
If this yields one of (000)2, (001)2, (010)2, (011)2, (100)2, (101)2, we retum 1 plus the corresponding
value. Observe that all six values between 1 and 6, inclusive, are equally likely to be retumed. If the
three calls yields one of (110)2, (1.1.7)2, we make three more calls. Note that the probability of having
to try again is 218, which is less than half. Since successive calls are independent, the probability
that we require many attempts diminishes very rapidly, e.g., the probability of not getting a result
in 10 attempts is (2/8)10 which is less than one-in-a-million.
def uniforrn-random(lower-bound, upper-bound)
34
```
