# Exercise 8.2: Evaluate RPN expressions

**Printed textbook page:** 101. **Reference transcription pages:** 101–101.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 101 (PDF page 115)

```text
8.2 Evar.uanr RPN rxpnrssroNs
A string is said to be an arithmetical expression in Reverse Polish notation (RPN) if:
(1.) It is a single digit or a sequence of digits, prefixed with an option -, c.g.,"6" , "129" ,'-42".
(2.) It is of the form "A,B,o" where A and B are RPN expressions and o is one of +, -,x, / .
For example, the following strings satisfy these rules: "1729", "3,4,+,2,x,L,+", "1.,1.,+,-2,x,',
"-641,,6, 1,28, 1".
An RPN expression can be evaluated uniquely to an integer, which is determined recursively.
The base case corresponds to Rule (1.), which is an integer expressed in base-lO positional system.
Rule (2.)corresponds to the recursive case, and the RPNs are evaluated in the natur alway, e.g., it A
evaluates to 2 and B evaluates to 3, then "A,B,x" evaluates to 6.
Write a program that takes an arithmetical expression in RPN and retums the number that the
expression evaluates to.
Hlnf: Process subexpressions, keeping values in a stack. How should operators be handled?
Solution: Let's begin with the RPN example "3,4,+,2,x,1,+". The ordinary form for this is
(3 + 4) x2+ 1,. To evaluate this by hand, we would scan from left to right. We record 3, then 4, then
applying the + to 3 and 4, and record the result, 7. Note that we never need to examine the 3 and 4
again. Next we multiply by 2, and record the result, L4. Finally, we add 1 to obtain the final result,
15.
Observe that we need to record partial results, and as we encounter operators, we apply them
to the partial results. The partial results are added and removed in last-in, first-out order, which
makes a stack the natural data structure for evaluating RPN expressions.
def evaluate (RPN-expression) :
intermediate_results = []
DELIilITER = ,,,
oPERAT0RS = {
'+': lanbda y, x: x + y,
lanbda y, x: x " y, '/':
I
'-' : Iambda y, x: x - y,
lanbda y, x: int(x / y)
for token in RPil_expression. split (DELIHITER) :
if token in 0PERAT0RS:
intermediate-resuIts. append(0PERATORS Itoken] (
intermediate_results.popO, intermediate_results.popO))
else: # token is a nunber,
intermediate_results . append (int (token) )
return intermediate_results [ - 1]
Since we perform O(1) computation per character of the string, the time complexity is O(n), where
n is the length of the string.
Varianfi Solve the same problem for expressions in Polish notation, i.e., when A,B, o is replaced by
o,A,B in Rule (2.).
101
```
