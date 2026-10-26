# Exercise 6.7: Compute all mnemonics for a phone number

**Printed textbook page:** 74. **Reference transcription pages:** 74–74.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 74 (PDF page 88)

```text
# Reverses each word in the string
revexse-range(s, start, end - 1)
start=end+1
# Reverses the Tast word.
reverse-range (s , start , len(s) - 1)
Since we spend O(1) per characte{, the time complexiry is O(n), where n is the length of s. The
computation in place, i.e., the additional sPace comPlexity is O(1).
6.7 Coupurr ALL MNEMoNICS FoR A pHoNE NUMBER
Each digit, apart from 0 and 1, in a phone keypad corresponds to one of three or four letters of the
alphabet, as shown in Figure 5.1. Since words are easier to remember than numbers, it is natural
to ask if a 7 or 10-digit phone number can be represented by a word. For example, "2276696"
corresponds to "ACRONYM" as well as "ABPOMZN".
FIgure 6.1: Phone keypad
Write a program which takes as input a phone number, specified as a string of digits, and returns
all possible character sequences that correspond to the phone number. The cell phone keypad is
specified by a mapping that takes a digit and returns the corresponding set of characters. The
character sequences do not have to be legal words or phrases.
Hint: Use recursion.
Solution: For a7 digit phone number, the brute-force approach is to formT ranges of characters,
one for each digit. For example, if the number is "2276696" then the ranges ate'N-'C','N-
'C', 'P'-'S', 'M'-'O', 'ly't'-'O', 'W'-'Z', and 'M'-'O'. We use 7 nested for-loops where the iteration
variables correspond to the T ranges to enumerate all possible mnemonics. The drawbacks of such
an approach are its repetitiveness in code and its inflexibility.
As a general rule, any such enumeration is best computed using recursion. The execution path
is very similar to that of the brute-force approach, but the compiler handles the looping.
# The napping fron digit to corresponding characters.
I1APPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'lKL', 'llNO', 'PQRS', 'TUV', 'IJXYZ')
def phone-mnemonic (phone-number) :
def phone-mnemonic-helper (digit) 
:
if digit == len(phone-number)
74
```
