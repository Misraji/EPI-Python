# Exercise 12.11: Test the Collatz conjecture

**Printed textbook page:** 176. **Reference transcription pages:** 176–176.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 176 (PDF page 190)

```text
return FaIse
return True
word-to-freq = collections. Counter (words)
unit-size = Ien(words[0])
return I
i for i in range(Ien(s) - unit-size * Ien(words) + r)
if match-alI-words-in-dict (i)
l
We analyze the time complexity as follows. Let m be the number of words ar.d n the length of
each word. Let N be the length of the sentence. For any fixed i, to check if the string of length nm
starting at an offtet of i in the sentence is the concatenation of all words has time complexity O(nm),
assuming a hash table is used to store the set of words, This implies the overall time complexity is
O(Nnm). hr practice, the individual checks are likely to be much faster because we cil:I stop as soon
as a mismatch is detected.
The problem is made easier, complexity-wise and implementation-wise, by the fact that the
words are all the same length-it makes testing if a substring equals the concatenation of words
straightforward.
12.77 Trsr rns Correrz coNIECTURE
The Collatz conjecture is the following: Take any natural number. If it is odd, triple it and add one;
if it is even, halve it. Repeat the process indefinitely. No matter what number you begin with, you
will eventually arrive at 1.
As an example, if we startwith 11we get the sequence 11,34,17,52,26,L3,40,20,10,5,16,8,4,2,1.
Despite intense efforts, the Collatz conjecture has not been proved or disproved.
Suppose you were given the task of checking the Collatz conjecture for the first billion integers.
A direct approach would be to compute the convergence sequence for each number in this set.
Test the Collatz conjecture for the first n positive integers.
Hint: How would you efficiently check the conjecture for zr assuming it holds for allm < n?
Solution: Often interview questions are open-ended with no definite good solution-all you can
do is provide a good heuristic and code it well.
The Collatz hypothesis can fail in two ways-a sequence retums to a previous number in the
sequence, which implies it will loop forever, or a sequence goes to infinity. The latter cannot be
tested with a fixed integer word length, so we simply flag overflows.
The general idea is to iterate through all numbers and for each number repeatedly apply the
rules till you reach 1. Here are some of the ideas that you can try to accelerate the check:
o Reuse computation by storing all the numbers you have already proved to converge to 1; that
way, as soon as you reach such a number, you can assume it would reach 1.
r To save time, skip even numbers (since they are immediately halved, and the resulting number
must have already been checked).
o If you have tested every number up to k,youcan stop the chain as soon as you reach a number
that is less than or equal to k. You do not need to store the numbers below k in the hash table.
176
```
