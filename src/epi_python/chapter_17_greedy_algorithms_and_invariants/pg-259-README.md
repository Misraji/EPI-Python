# Chapter 17: Greedy Algorithms And Invariants

**Starts at printed page 259.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 259

```text
Cnaprsn
Greedy Algorithms and Invariants
The intended function of a program, or part of a program, wn be spec-
ifed by making general assertions about the oalues which the releuant
oarinbles will take after execution of the program.
- 
" An Axiomatic Basis for Computer Programming,"
C. A. R. Hoenr, L969
Greeily algorithms
A greedy algorithm is an algorithm that computes a solution in steps; at each step the algorithm
makes a decision that is locally optimum, and it never changes that decision.
A greedy algorithm does not necessarily produce the optimum solution. As example, consider
making change for 48 pence in the old British currency where the coins came in30,24,12,6,3, arrd 1
pence denominations. Suppose our goal is to make change using the smallest number of coins.
The natural greedy algorithm iteratively chooses the largest denomination coin that is less than or
equal to the amount of change that remains to be made. If we try this for 48 pence, we get three
coins-3O + 12 + 6. However, the optimum answer would be two cotns-14 + 24.
L:r its most general form, the coin changing problem is NP-hard, but for some coinages, the
greedy algorithm is optimum----e.g., if the denominations are of the form {1, r,i,f\. (An ad hoc
argument can be applied to show that the greedy algorithm is also optimum for US coinage.)
The general problem can be solved in pseudo-polynomial time using DP in a manner similar to
Problem 16.6 on Page246.
Sometimes, there are multiple greedy algorithms for a given problem, and only some of them
are optimum. For example, consider 2n cittes on a line, half of which are white, and the other half
are black. Suppose we need to pair white with black cities in a one-to-one fashion so that the total
length of the road sections required to connect paired cities is minimized. Multiple pairs of cities
may share a single section of road, e.g., if we have the pairing (0,4) and (1,2) then the section of
road between Cities 0 and 4 can be used by Cities 1 and 2.
The most straightforward greedy algorithm for this problem is to scan through the white cities,
and, for each white city, pair it with the closest unpaired black city. This algorithm leads to
suboptimum results. Consider the case where white cities are at 0 and at 3 and black cities are at 2
and at 5. If the white city at 3 is processed first, it will be paired with the black city at 2, forcing the
cities at 0 and 5 to pair up, leading to a road length of 5. In contrast, the pairing of cities at 0 and 2,
and 3 and 5 leads to a road length of 4.
A slightly more sophisticated greedy algorithm does lead to optimum results: iterate through
all the cities in left-to-right order, pairing each city with the nearest unpaired city of opposite color.
Note that the pairing for the first city must be optimum, since if it were to be paired with any other
city, we could always change its pairing to be with the nearest black city without adding any road.
This observation can be used in an inductive proof of overall optimality.
259
```
