# Exercise 15.10: Compute a Gray code

**Printed textbook page:** 232. **Reference transcription pages:** 232–233.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 232 (PDF page 246)

```text
if solve-partial-sudoku(i + 1, j):
return True
partial-assignnenttilijl = EUPTY-ENTRY # Undo assignnent
return False
ETIPTY-ENTRY = 0
return solve-partial-sudoku(0, 0)
Because the program is specialized to 9 x 9 grids, it does not make sense to speak of its time
complexity, since there is no notion of scaling with a size parameter. Howevel since the problem
of solving Sudoku generalized to nxn grids is NP-complete, it should notbe difficult to prove that
the generalization of this algorithm to n x n grids has exponential time complexity.
15.10 CoNrpurs a Gnev copu
An n-bit Gray code is a permutation of 10,1,2,...,2n - 1) such that the binary representations
of successive integers in the sequence differ in only one place. (This is with wraparound,
i.e., the last and first elements must also differ in only one place.) For example, both
((000)2, (100)2, (101)2, (111)2,(110)2, (010)2, (011)2, (001)2) - <0,4,5,7,6,2,3,1) and <0,7,3,2,6,7,5,4>
are Gray codes for n = 3.
Write a program which takes n as input and retums an n-bit Gray code.
Hint: lNrile out Gray codes for n = 2,3,4.
Solution: A brute-force approach would be to enumerate sequences of length 2n whose entries
are n bit integers. We would test if the sequence is a Gray code, and stop as soon as we find
one. The complexity is astronomical-there are 2nx2' sequences. We can improve complexity by
enumerating permutations of 0,7,2, . . . ,2n - 1, since we want distinct entries, but this is still a very
high complexity.
We can do much better by directing the enumeration. Specifically, we build the sequence
incrementally, adding a value only if it is distinct from all values currently in the sequence, and
differs in exactly one place with the previous value. (For the last value, we have to check that
it differs in one place from the first value.) This is the approach shown below. For n = 4, we
begin with (0000)2. Next we try changing bits in (0000)2, one-at-a-time to get a value not currently
present in the sequence, which yields (0001)2, which we append to the sequence. Changing bits
in (0001)2, one-at-a-time, we get (0000)z (which is already present), and then (0011)2, which is not,
so we append it to the sequence, which is now ((0000)2, (0001)2, (0011)2). The next few values are
(0010)2, (0011)2, (0111)2.
def gray-code (num-bits) :
def directed-gray-code (history) :
def differs-by-one-bit (x, y) :
bit_difference=x^y
return bit-difference 
and not (bit-difference 
&
(bit-difference 
- 1))
if len(result) == 1 << num-bits:
# Check if the .first and Last codes differ by one bit
return differs-by-one-bit(result[0], 
result[-1])
232
```

#### Printed page 233 (PDF page 247)

```text
for i in range(num-bits):
previous_code = result[-1]
candidate_next_code = previous_code ^ (1 << i)
if candidate-next*code not in history:
hi story. add (candidate_next_code)
result . append (candidate_next_code)
if directed-gray-code (history) :
return True
hi story. remove (candidate_next_code)
del result [ -1]
return FaIse
result = [0]
directed-gray-code (set ( t0l ) )
return result
Now we present a more analytical solution. The inspiration comes from small case analysis.
The sequence ((00)2, (01)2, (11)2, (10)2) is az-blt Gray code. To get to n = 3, we cannot just prepend
0 to each elements of ((00)2, (01)2,(11)2,(10)z), 1 to ((00)2, (01)2,(11)2,(10)z) and concatenate the two
sequences-that leads to the Gray code property being violated from (010)2 to (100)2. However, it
is preserved everywhere else.
Since Gray codes differ in one place on wrapping around, prepending 1 to the reverse of
((00)2, (01)2,(11)2,(10)2) solves the problem when transitioning from a leading 0 to a leading 1.
For n = 3 this leads to the sequence ((@0)2,(001)2,(011)2,(010)2, (1to)2,(11.1)2,(to1)2,(100)z). The
general solution uses recursion in conjunction with this reversing, and is presented below.
def gray-code (num-bits) :
if num-bits == 0:
return [0]
# These inpTicitTy begin with 0 at bjt-jndex (num_bits - 1).
gray-code_num_bits_minus_l = gray_code(num_bits - 1)
# Now, add a 1 at bjt-jndex (nun_bits - 1) to all entrjes in
# gray_code_nurn_bi ts_nrinus_L
leading-bit-one = 1 << (nunr_bits - 1)
# Process in reverse order to achieve refTection of
# gray-code_nura_bi ts_tuinus_I .
return gray_code_num_bits_minus_1 + [
Ieading-bit-one I i for i in reversed(gray_code_num_bits_minus_l)
l
# Pythonic so-lution uses list conprehension.
def gray-code_pythonic (num_bits) :
result = [0]
for i in range(num_bits):
result 1= [x + 2**i for x in reversed(result)]
return result
Assuming we operate on integers that fit within the size of the integer word, the time complexity
T(r) satisfies T(n) = T(n - 1) + O(2"-r). The time complexity is O(2n).
233
```
