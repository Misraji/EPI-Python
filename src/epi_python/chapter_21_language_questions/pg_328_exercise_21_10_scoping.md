# Exercise 21.10: Scoping

**Printed textbook page:** 328. **Reference transcription pages:** 328–329.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 328 (PDF page 342)

```text
Here's the original program rewritten using trylexcept/else/finalIy blocks to make it more
robust. In particular, the else shows what code is executed in the absence of exceptions. Note how
we use raise to create/propagate exceptions upwards.
class ColSumCsvParseException (Exception)
def --init--(self 
, *args) :
Exception. --init--(seIf 
, *args)
self. line-number = args [ 1]
def get-col-sum(filename, co1) :
# nay raise loErtor, wi77 propagate to ca77er
csv-file = open(filename)
csv-reader = csv. reader(csv-file)
running-sum = Iine-number = 0
try:
for row in csv-reader:
if col >= len(row):
raise IndexError("Not enough entries in row " + str(row))
value = rowIcol]
# We wi77 sirip rows for which the corresponding co.lumns cannot be
# parsed to an int , logging the fact.
try:
running-sum += int(value)
ercept valueError:
print("cannot convert " + value + " to int, ignoring")
Iine-number += 1
ercept csv. Error:
# Programs should raise exceptions appropriate to their 7eve7 of
# abstraction, so we propagate the csv,Ellor upwatds as a
# Col SunC svP ar s eExcept i on .
print("In csv. Error handler")
raise ColsumcsvParseException("Error processing csv", line-number)
else:
print("Sum = " + str(running-sum))
finally:
# Ensure there is no resource l.eak,
csv-fi1e . close o
return running-sum
There are anumberof built-inexceptionfypesinPython, e.g., IndexError, FloatingPointError,
EnvironmentError, ValueError, etc., and these should be used whenever possible.
21.10 ScopINc
Explain the rules for variable scope.
Solution: There are two (nonexclusive) possibilities: the variable appears in an expression, and the
variable is being assigned to.
When the variable appears in an expression, Python searches for it in the following order:
(1.) The current function.
(2.) Enclosing scopes, e.g., containing functions.
328
```

#### Printed page 329 (PDF page 343)

```text
(3.) The module containing the code (also referred to as the global scope)
(a.) The built-in scope, e.9., open
(A NameError is raised if none of these contain a defined variable with the given name.)
In the simplest case, the variable is defined already in the current scope, in which case the
assignment happens to it. Otherr,rrise, if the assignment happens outside a function, it defines a
new global variable; if it happens within a function, it defines a new variable whose scope is the
function that contains the assignment.
To make an assignment to a variable not defined in the current scope within a function happen
to a global variable, define a new variable in the current scope, that variable should be declared as
global in the function. In Python3, to have an assignment to a variable in nested function use an
enclosing function's scope, use nonlocal: this will make the program search outwards through the
enclosing scopes (but not to the module level) for that variable.
The scoping rules seek to prevent variables local to a function from polluting the containing
functions and module. They can lead to scoping bugs though, so as a rule names should be kept
distinct.
Here is a program that illustrates these rules
x, y, z ='gIobal-\','global-y','global-z'
def basic-scoping O :
print(x) 
# 97oba7-x
y = 'local -y'
global z
z = 'Local-z'
basic_scoping ()
print(x, y, z) # gLoba7-x globaT-y 7oca7-z
def inner-outer-scoping O :
def innerl O :
print(x) # outet-x
def inner2 O :
x = 'inner2 -x'
print(x) # inner2-x
def inner3O:
nonlocal x
x = 'inner3 -x'
print(x) # inner3-x
x = "outer-x"
innerlO, inner2O, inner3o
print (x) # inneri -x
inner-outer_scoping o
print (x , y , z) # gTobal -x g7oba7 -y 7oca7 -z
329
```
