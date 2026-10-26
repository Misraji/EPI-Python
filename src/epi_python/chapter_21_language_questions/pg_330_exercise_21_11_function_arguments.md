# Exercise 21.11: Function arguments

**Printed textbook page:** 330. **Reference transcription pages:** 330–332.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 330 (PDF page 344)

```text
def outer-scope-error O :
def innerO:
try:
x = x + 321
ercept NameError:
print('Error: x is local, and so x + 1 is not defined yet')
x = 123
inner o
outer-scope-errorO # prints'Error
def outer-scope-array-no-error O :
def innerO:
x[0] = -x[0] # x[0] isn't a variable, it's resoJ,ved fron outer x
x = [31a]
inner ()
print (x [0] )
# -314
outer-scope-array-no-error o
21,.lL FuNcrrouARcuMENrs
What are positional, keyword, and default arguments to a function. What does the following
proglam ouQut, and why?
def foo(x=[]):
x.append(1)
return x
res = foo()
print (res)
res = fooo
print (res)
Solution: On the calling side, some function arguments canbe specified by name. These arguments
have come after all of the ururamed arguments (also known as positional arguments). Consider the
following function.
def foo(x , y, z)':
returnx*x+y*y+z*z
It can be called using positional arguments, or keyword arguments as follows.
foo(1, 2, 3)
330
```

#### Printed page 331 (PDF page 345)

```text
foo(x=l , y=2, z=3)
foo (1 , y=2 , z=3)
foo(1, z=3, y=3)
foo (z=3 , y=3 , x=1)
# This is a syntax error I
foo(x=1, 2, z=3)
# This is a syntax error,
foo (1 , x=2 , z=3 , y=4)
keyword argunents nust fo77ow positional argufients
a variabTe cannot be assigned twice.
Keywords arguments have the following benefits.
o The function call is much clearer-it's harder to mistakenly exchange two values.
. They make it easier to refactor a function into having more arguments. Specifically, the
combination of keyword arguments and default values means that old code does not have to
be touched even when new arguments are added.
\Alhen a function is defined, its arguments can be specified to have default values; if the function
is called without the argument, the argument gets its default value. There must be default values
for all arguments which are not specified in calls to the function.
One subtlety with default arguments is that they are evaluated once, specifically when the
module is loaded, and are shared across all callers. For this reason, the program given in the
example prints [1 , 1] after the second call-the first call updates the default argument to [1]. As
a rule, mutable arguments should have None as their default values. Then the function can test the
argument in its body-if it is None, the function can assign it to the desired default value. See the
program below for an example.
def read-file_as-array_buggy(filename, default=tl)
try:
filehandle = open(filename)
return filename.readO. splito
elcept Exception:
return default
def read-file-as-array-works (filename, default=None)
if default is None:
default = []
try:
filehandle = open(filename)
return filename. readO. splito
elcept Exception:
return default
A = read-file-as-array-buggy("does_not_exist
A.append("first")
B = read-file-as_array-buggy("does_not_exist
B. append("second")
print (B) # ['fixst' 
, 'second']
A = read-file_as_array_works ("does_not_exist
A. append("first")
B = read_fiIe_as_array_works ("does_not_exist
B. append("second")
txt")
txt")
txt")
txt")
331
```

#### Printed page 332 (PDF page 346)

```text
print (B) # [' second' ]
,t-)1
```
