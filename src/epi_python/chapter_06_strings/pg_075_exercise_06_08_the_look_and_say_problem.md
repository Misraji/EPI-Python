# Exercise 6.8: The look-and-say problem

**Printed textbook page:** 75. **Reference transcription pages:** 75–75.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 75 (PDF page 89)

```text
# A77 digits are processed, so add partiaT_nnenonic to nnerlonics.
# (We add a copy sjnce subsequent calls nodify partiaT_mnenonic.)
mnemoni c s . append ( " . j oin (parti al_mnemoni c ) )
else
# Try a77 possible characters for this digit
for c in UAPPINclint(phone-numberldigitl)l 
:
partial-mnemonicldigitl = c
phone-mnenonic-helper(digit + f)
mnemonics, partial-mnemonic = [] , [0] * Ien(phone_number)
phone-mnemonic-helper (0)
return mnemonics
Since there are no more than 4 possible characters for each digit, the number of recursive calls,T(n),
satisfies T(n) < 4T(n - 1), where z is the number of digits in the number. This solves to T(n) = O(4').
For the function calls that entail recursion, the time spent within the function, not including the
recursive calls, is O(1). Each base case entails making a copy of a string and adding it to the result.
Since each such string has length n, eachbase case takes time O(n). Therefore, the time complexity
is O(4"n).
Varianft Solve the same problem without using recursion.
6.8 Tnr r,oox-aND-sAy pRoBLEM
The look-and-say sequence starts with 1. Subsequent numbers are derived by describing the
previous number in terms of consecutive digits. Specifically, to generate an entry of the sequence
from the previous entry, read off the digits of the previous entry, counting the number of digits in
grouPs of the same digit. For example, 1; one 1; two 1s; one 2 then one 1; one 1, then one 2, then
two 1s; three 1s, then two 2s, then one 1. The first eight numbers in the look-and-say sequence are
<'t, 1.1., 21, 1211, 111221, 31221.1., 13112227, 1113213211> .
Write a Program that takes as input an integer r and retums the nth integer in the look-and-say
sequence. Retum the result as a string.
Hint:\ou need to retum the result as a string.
Solution: We compute the nth number by iteratively applying this rule n - 1 times. Since we are
counting digits, it is natural to use strings to represent the integers in the sequence. Specifically,
going from the ith number to the (i + 1)th number entails scanning the digits from most significant
to least significant, counting the number of consecutive equal digits, and writing these counts.
def look-and-say(n):
def next-number (s) :
result, i = tl, 
0
rhile i < len(s):
count = 1
rhile i + 1 < Ien(s) and stil == sli + 1l
i+=1
count += 1
result.append(str(count) + sIi])
i+=1
return " . join(result)
75
```
