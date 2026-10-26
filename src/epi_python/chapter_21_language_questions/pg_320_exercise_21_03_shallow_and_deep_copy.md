# Exercise 21.3: Shallow and deep copy

**Printed textbook page:** 320. **Reference transcription pages:** 320–320.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 320 (PDF page 334)

```text
Solution: The program prints 13 (=9 + 4) rather than the 7 (=3 + 4) than might be expected. This
is because the the functions created in the loop have the same scope. They use the same variable
name, and consequently, all refer to the same variable, l, which is 10 at the end of the loop, hence
the 13 (=9 + 4).
There are many ways to get the desired behavior. A reasonable approach is to return the lambda
from a function, thereby avoiding the naming conflict.
def create-increment-function (x)
return lanbda y: y + x
increment-by-i = [create-increment-function(i) for i in range(10)J
print (increment-by-i t 3l (4) )
27.3 SHarrow AND DEEP coPY
Describe the differences between a shallow copy and a deep copy. When is each appropriate, and
when is neither appropriate? How is deep copy implemented?
Solution: First, we note that assignment in Python does not copy-it simply a variable to a target.
For objects that are mutable, or contain mutable items, a copy is needed if we want to change the
copywithoutchangingtheoriginal. Forexample,tf A = U, 2, 4, 8l andweassignAtoB,i'e.,B
= A, then if we changeB, e.g., B. append(16), then A will also change.
There are two ways to make a copy: shallow and deep. These are implemented in the copy
module, specifically as copy.copy(x) and copy.deepcopy(x). A shallow copy constructs a new
compound object and then (to the extent possible) inserts references into it to the objects found in
the original. A deep copy constructs a new compound object and then, recursively, inserts copies
into it of the objects found in the original.
Asaconcreteexample,suPPoseA = [lL, 2, 3],[4, 5, 6]l andB = copy.copy(A).Thenif
weupdateBasB[0][0] = 0,AtOltOl alsochangesto0. However,if B = coPy.deepcopy(A),then
the same update will leave A unchanged.
The difference between shallow and deep copying is only relevant for compound objects, that
is objects that contain other objects, such as lists or class instances. If A = lL, 2, 3l and B =
copy. copy(A), then if we update B as B [0] = 0, A is unchanged.
Diving under the hood, deep copy is more challenging to implement since recursive objects
(compound objects that, directly or indirectly, contain a reference to themselves) result in infinite
recursion in a naive implementation of deep copy. Furthermore, since a deep copy copies every-
thing, it may copy too much, e.g., book-keeping data struchrres that should be shared even between
copies. The copy. deepcopyO function avoids these problems by caching objects already copied,
and letting user-defined classes override the copying operation. In particular, a class can override
one orboth of--copy--O and --deepcopy--O.
Copying is defensive-it may avoided if it's known that the client will not mutate the object.
Similarly, if the object is itself immutable, e.g., a tuple, then there's no need to copy it.
320
```
