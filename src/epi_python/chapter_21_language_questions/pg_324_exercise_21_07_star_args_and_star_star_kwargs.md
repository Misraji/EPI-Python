# Exercise 21.7: *args and **kwargs

**Printed textbook page:** 324. **Reference transcription pages:** 324–324.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 324 (PDF page 338)

```text
S = set([U])
print (U in S)
print(V in S)
u.x = 28
print(u in s)
# Prints True.
# Also prints lrue, since we impTemented equals and hash
# Prints Fa.lse, since u has changed.
Some less important differences include the following:
o Conventionally, tuples are used to represent heterogeneous groups of values, where lists are
used for homogeneous values, as in the example above.
r Tuples are slightly faster to build and access, and have a smaller memory footprint.
2L.7 *encs ANn *rwlncs
What are *args and *kwargs? Where are they appropriate?
Solution: Both are used to pass a variable number of arguments to a function. The first, *args, is
used to pass a variable length argument list, e.9.,
def foo(u, v, *args):
print('u,v 
= ' + str((u, v)))
for i in range(Ien(args)):
print('args 
{0} = {1}'.fornat(str(i), 
str(argstil)))
foo (1 , 'euler ' , 2.71, t6, 281 )
Alternative caI.1 .
I{ith the o, foo gets 4 arguments, not 3. Prints
u,v = (1, 'eu7er')
args 0 = 2,77
args 1 = [6, 28]
arss = (2.7L, 16, 281)
foo (1 , 'eu1er' , *args)
Without the *, foo gets 3 atgunents, not 4. Prints
u,v = (7, 'euler')
args 0 = (2.71, t6, 281)
foo(1, 'euler', 
args)
Some points:
o It's not important that the parameter referenced in the function be called args-it could just
as well be called A or varargs (though args is idiomatic);
o it is important that the o be specifiedi
o the * argument must appear after all the regular arguments (if any); and
o * can be used at the call site too.
The second, **kwargs, is used when passing a variable number of keyword arguments to a
function.
324
```
