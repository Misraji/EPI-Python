# Chapter 15: Recursion

**Starts at printed page 217.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 217

```text
Cuaprun
Recursion
The power of recursion eoidmtly lies in the possibility of defining an infinite
set of objects by a fnite statemmt. ln the same mannel, an infinite number
of cornputations can be ilescribed by a finite recursiae program, ezten if this
program contains no explicit repetitions.
- 
" Algorithms + Data Structures = Programs,"
N. E. WInrs, 1976
Recursion is an approach to problem solving where the solution depends partially on solutions to
smaller instances of related problems. It is often appropriate when the input is expressed using
recursive rules, such as a computer grammar. More generally, searching, enumeration, divide-
and-conquer, and decomposing a complex problem into a set of similar smaller instances are all
scenarios where recursion may be suitable.
A recursive function consists of base cases and calls to the same function with different argu-
ments. TWo key ingredients to a successful use of recursion are identifying the base cases, which
are to be solved directly, and ensuring progress, that is the recursion converges to the solution.
A divide-and-conquer algorithm works by repeatedly decomposing a problem into two or more
smaller independent subproblems of the same kind, until it gets to instances that are simple enough
to be solved directly. The solutions to the subproblems are then combined to give a solution to the
original problem. Merge sort and quicksort are classical examples of divide-and-conquer.
Divide-and-conquer is not synonymous with recursion. In divide-and-conquet the problem is
divided into two or more independent smaller problems that are of the same type as the original
problem. Recursion is more general-there may be a single subproblem, e.g.,binary search, the
subproblemsmaynotbe independent, e.9., dynamic programming, and they maynotbeof the same
type as the original, e.9., regular expression matching. In addition, sometimes to improve runtime,
and occasionally to reduce space complexity, a divide-and-conquer algorithm is implemented using
iteration instead of recursion.
Recursion boot camp
The Euclidean algorithm for calculating the greatest common divisor (GCD) of two numbers is a
classic example of recursion. The central idea is that if U ) x, the GCD of r and y is the GCD of r
ffird y - r. For example, GCD(156,36) = GCD((156 - 36) = 120,36). By extension, this implies that
the GCD of r and y is the GCD of r and y mod x, i.e., GCD(156,36) = GCD((156 mod 36) = 1.2,36) =
GCD(12,36 mod 12 = 0) = 12.
def gcd(x, y):
return x if Y == 0 else Scd(y, x % y)
217
```

### Printed page 218

```text
Since with each recursive step one of the arguments is at least halved, it means that the time
complexity is O(logmax(x,y)).Put another way, the time complexity is O(n),where r is the number
of bits needed to represent the inputs. The space complexity is also O(n), which is the maximum
depth of the function call stack. (The program is easily converted to one which loops, thereby
reducing the space complexity to O(1).)
Now we describe a problem that can be elegantly solved using a recursive divide-and-conquer
algorithm. A triomino is formed by joining three unit-sized squares in an L-shape. A mutilated
chessboard (henceforth 8 x 8 Mboard) is made up of 64 unit-sized squares arranged in an 8 x 8
square, minus the top-left square, as depicted in Figure 15.1(a). Suppose you are asked to design
an algorithm that computes a placement of 21 triominoes that covers the 8 x 8 Mboard. Since
the 8 x 8 Mboard contains 63 squares, and we have 21 triominoes, a valid placement cannot have
overlapping triominoes or triominoes which extend out of the 8 x 8 Mboard.
(a) An8xSMboard. 
(b) Four4x4Mboards.
Figure 15.1 : Mutilated chessboards.
Divide-and-conquer is a good strategy for this problem. Lrstead of the 8 x 8 Mboard, let's
consider an n x n Mboard. A 2 x 2 Mboard can be covered with one triomino since it is of the same
exact shape. You may hypothesize that a triomino placement for an n x n lvlboard with the top-left
square missing can be used to compute a placement for an (n + 1\ x (/, + 1) Mboard. Howeveq, you
will quickly see that this line of reasoning does not lead you anywhere.
Another hypothesis is that if a placement exists for an nxnlvfboard, then one also exists for a
2n x 2n Mboard. Now we can apply divide-and-conquer. Take four n x n lvlboards and arrange
them to form a 2nx2n square in such a way that three of the Mboards have their missing square set
towards the center and one Mboard has its missing square outward to coincide with the missing
corner of a2n x 2n Mboard, as shown in Figure 15.1(b). The gap in the center can be covered with a
triomino and, by hypothesis, we cal:r cover the four n x n Mboards with triominoes as well. Hence,
a placement exists for any n that is a power of 2. In particular, a placement exists for the 23 x 23
Mboard; the recursion used in the proof directly yields the placement.
218
```
