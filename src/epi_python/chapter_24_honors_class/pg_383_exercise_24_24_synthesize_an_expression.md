# Exercise 24.24: Synthesize an expression

**Printed textbook page:** 383. **Reference transcription pages:** 383–384.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 383 (PDF page 397)

```text
# See '* ' ratches zero chatacter in s[;-len(s)J
return is_match_here (regex [2: ] , s)
# Case (4.): regex begins with single character match
return bool(s and regex[0] in ('.', 
stOl)
and is-match_here(regexIl:], s[1:]))
# Case (2.): regex starts with'^'.
if regex [0] == 'r' '
return is_match_here (regex [1: ] , s)
return any(is_match_here(regex, s[i:]) 
for i in range(Ien(s) + l))
Let C(x,k) be k copies of the string.r concatenated together. For the regular expression C(a.*,k) and
string C(ab,k- 1) the algorithm presented above takes time exponential in k. We cannot give a more
precise bound on the time complexity.
Variant Solve the same problem for regular expressions without the ^ and g operators.
24.24 SyurnBsrzr AN ExpRESsroN e
Consideranexpressionoftheform(3o1o4o1o5),whereeachoisanoperato\e.g.r+,-,x,+.
The expression takes different values based on what the operators are. Some examples are 14 (if all
operators are +)/ 60 (if all operators are x), arrd22(3 - 1 + 4 x 1 x 5).
Determining an operator assignment such that the resulting expression takes a specified value
is, in general, a difficult computational problem. For example, suppose the operators are + and -,
and we want to know whether we can select each o such that the resulting expression evaluates to
0. The problem of partitioning a set of integers into two subsets which sum up to the same value,
which is a famous NP-complete problem, directly reduces to our problem.
Write a Program that takes an array of digits and a target value, and retums true if it is possible to
intersperse multiplies (x) and adds (+) with the digits of the array such that the resulting expression
evaluatestothetargetvalue. Forexample,if thearrayis <1,2,9,2,5,9,2,8,s,9)andthetargetvalue
is99S,thenthetargetvaluecanberealizedbytheexpressionl23+2+5x3x7+85x9,soyour
program should retum true.
Hint: Build the assignment incrementally.
Solution: Let A be the array of digits and k the target value. We want to intersperse x and +
operations among these digits in such a way that the resulting expression equals k.
For each pair of characters, (Alil,Ali + 1]), we can choose to insert a x, a +, or no operator.
If the length of A is n, the number of such locations is n - 1,, implying we can encode the choice
with an array of length n - 1,. Each entry is one of three values-X, *, and - (which indicates no
operator is added at that location). There are exactly 3'-1 such arrays, so a brute-force solution
is to systematically enumerate all arrays. For each enumerated auay, we compute the resulting
exPression, and refurn as soon as we evaluate to k. The time complexity is O(n x 3u), since each
expression takes time O(n) to evaluate.
To improve runtime, we use a more focused enumeration. Specifically, the first operator can
aPPear after the first, second, third, etc. digit, and it can be a + or x. For + to be a possibility, it must
383
```

#### Printed page 384 (PDF page 398)

```text
be that the sum of the value given by the initial operator assignment plus the value encoded by the
remaining digits is greater than or equal to the target value. This is because the maximum value is
achieved when there are no operators. For example, for \L,2,3,4,5>, we can never achieve a target
value of 11,07 if the first operator is a + placed after the 3 (since 1,23 + 45 < 11.07). This gives us a
heuristic for pruning the search.
def expression-synthesis (digits , target) :
def directed-expression-synthesis(digits, 
current-term) :
def evaluate O :
interrnediate-operands = []
operand-it = iter(operands)
intermediate-operands . append (next (operand-it) )
# EvaTuates '*' first,
for oper in operators:
if oPer == '*' :
product = interrnediate-operands[-1] n nert(operand-it)
intermediate-operandst-fl = product
else: # oPer == '+'.
intermediate-operands . append (next (operand-it) )
# EvaTuates '+' second.
return sun(intermediate-operands)
current-term = current-term * 10 + digits[0]
if len(digits) 
== 1;
operands . append ( current-term)
if evaluateo == target: 
# Found a natch
return True
del operands [-1]
return FaIse
# No operator.
if directed-expression-synthesis (digits [1: ] , current-term) :
return True
# Tries nrultiplication operator '*'.
operands . append ( current-terrn)
operators . append ('* ')
if directed-expression-synthesis (digits [1: ] , 0) :
return True
de1 operands [ -1]
del operators [-1]
# Tries addition operator '+',
operands . append ( current-tern)
# First check feasibility of plus operator.
if target - evaluateO <= functools.reduce(lanbda val, d: val * 10 + d,
digits [1: ] , 0) :
operators. append(' +' )
if directed-expression-synthesis(digits[1:], 0) :
return True
del operators[-1]
del operands [ -1]
return FaIse
operands, operators = [], tl
return directed-expression-synthesis(digits, 0)
384
```
