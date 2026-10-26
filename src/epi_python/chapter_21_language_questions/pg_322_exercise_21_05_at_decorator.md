# Exercise 21.5: @decorator

**Printed textbook page:** 322. **Reference transcription pages:** 322–322.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 322 (PDF page 336)

```text
Solution: First, recall that functions are first class objects in Python, that is, they can be passed as
arguments to other functions, and retumed by functions. Additionally, functions can be defined
within other functions. In certain contexts, these facts can greatly simplify writing code. For
example, here is code that prints the time take to run a function.
def time-function(f)
Print how Tong a function takes to compute
begin = time. tine o
result = fo
end = time.timeo
print("Function call took " + str(end - begin) + " seconds to execute.")
return result
def fooO:
print("I am fooO")
def ackermann(m, n):
ifm==0:
return n + 1
elif n == 0:
return ackermann(m - 1, 1)
else:
return ackermann(m - 1, ackermann(m, n - 1))
t ime-func t i on ( foo )
# functooTs.partialO take a functjon and positional argunents to it and
# creates a new function with those arguments preassigned to the specified
# vaTues.
time-function(functools.partial(ackermann, 3, 4))
Python provides syntactic sugaring to simplify this process in the form of the @decorator construct.
The annotation @tirne-firnction amounts to the following: foo = @time-function(foo).
def time-function(f):
def wrapper(*args, o*kwargs) :
begin = time. time o
result = f(*args, **kwargs)
end = time. time ()
print("Function caIl with arguments {all-args} took ".fornat(
atl-args="\t".join((str(args), 
str(kwargs)))) + str(end - begin) +
" seconds to execute.")
return result
return wrapper
@time-functi on
def fooO:
print("I am fooO")
322
```
