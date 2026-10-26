# Exercise 21.6: List vs tuple

**Printed textbook page:** 323. **Reference transcription pages:** 323–323.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 323 (PDF page 337)

```text
@time-functi on
def ackermann (m, n) :
ifn==0:
return n + 1
elif n == 0:
return ackernann(m - 1, 1)
else:
ret,urn ackermann(m - 1, ackermann(m, n - 1))
@time-function
def bar(*args, "*kwargs):
print(su[(args) 
t sun(kwargs. values O))
Other corunon uses of decorators are checking access control on function backing up REST end-
points/ and adding a delay to the end of a function to rate-limit it.
21,.6 Lrsr vs ruprr
In what ways are lists and tuples similar, and in what ways are they different?
Solution: Lists,e.g., [6, 28, 496, 8128] andtuples, e.g., (3. 14, "pi',, [True, False, True])
are similar in that both represent sequences. Both use the same syntax to access, the l-th element of
the sequence, and both support the in operator for membership checking.
The key difference between a tuple and a list is that a tuple is immutable-you cannot change
the element at index l, or add/delete from a tuple, all of which are possible with a list.
There are numerous benefits of immutability, the most important of which immutable objects
are more container-friendly and thread-safe. Elaborating on container-friendliness, if a mutable
object is inserted in a set, changed, and then the changed objected is looked up, the lookup will fail
(because the hashcode has changed from when it was added to the set). For this reason, tuples are
can be put in sets, and used as map keys, but lists cannot.
For the sake of completeness, it's worth pointing out that it's possible to have a mutable object
in a tuple, and as a result such a tup1e is not longer immutable, as illustrated below:
class AO:
def -_init__(self, x)
self.x = x
def --eq--(seIf , other) :
return isinstance(other, A) and self.x == other.x
def --hash--(self):
return self.x * 113 + 119
u = A(42)
v = A(42)
U = (u, )
V = (v, )
323
```
