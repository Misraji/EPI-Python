# Exercise 8.1: Implement a stack with max API

**Printed textbook page:** 98. **Reference transcription pages:** 98–100.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 98 (PDF page 112)

```text
def print-Iinked-list-in-reverse 
(head)
nodes = []
rhile head:
nodes . append (head. data)
head = head.next
rhile nodes:
print (nodes.pop O )
The time and space complexity are O(n), where n is the number of nodes in the list.
As an altemative, we could form the reverse of the list using Solution 7.2 on Page 85, iterate
through the list printing entries, then perform another reverse to recover the list-this would have
O(rz) time complexity and O(1) space complexity.
to recognrze
LIFO property is applicable. For
benefits from a stack.
Consider augmenting the basic stack or queue data structure to support additional operations,
such as finding the maximum element.
Table 8.1 : Top Tips for Stacks
Kttow your stflck libraries
Some of the problems require you to implement your own stack class; for others, use the built-in
Iist-type.
o s. append(e) pushes an element onto the stack. Not much can go wrong with a call to push.
o s [-1] will retrieve, but does not remove, the element at the top of the stack.
o s.popO will remove and retum the element at the top of the stack.
o len(s) == 0 tests if the stack is empty.
\A/hen called on an empty list s, both s [- 1] and s .pop O raise an IndexError exception.
8.1 hrrpr.rNrsNr A srAcK wrrH uex API
Design a stack that includes a max operation, in addition to push and pop. The max method should
return the maximum value stored in the stack.
Hint: Llse additional storage to track the maximum value.
Solution: The simplest way to implement a max operation is to consider each element in the stack,
e.g., by iterating through the underlying array for an array-based stack. The time complexity is
O(n) and the space complexity is O(1), where n is the number of elements currently in the stack.
The time complexity can be reduced to O(logn) using auxiliary data structures, specifically, a
heap or a BST, and a hash table. The space complexity increases to O(n) and the code is quite
complex.
Suppose we use a single auxiliary variable, M, to record the element that is maximum in the
stack. Updating M on pushes is easy: M = max(Me), where e is the element being pushed.
However, updating M on pop is very time consuming. If M is the element being popped, we have
98
```

#### Printed page 99 (PDF page 113)

```text
no way of knowing what the maximum remaining element is, and are forced to consider all the
remaining elements.
We can dramatically improve on the time complexity of poppi.g by caching, in essence, trading
time for space. Specifically, for each entry in the stack, we cache the maximum stored at or below
that entry. Now when we pop, we evict the corresponding cached value.
class Stack:
ElementwithCachedl{ax = collections. namedtuple ('Elementl{ithCachedl.lax' ,
('element', 'max'))
def --init--(se1f):
self . _element_with_cached_max = []
def empty(self):
return len(self.-element-with-cached_max) == 0
def max(self):
if seIf. emptyO:
raise IndexError('maxO: empty stack')
return self . -element_with-cached-max [-1] . max
def pop(seIf):
if self. emptyO :
raise IndexError ('pop O : empty stack')
return self. -element-with_cached-max .pop O . element
def push (self , x) :
self . -element-with-cached-max. append (
self.ElementWithcachedllax(x, x if self.emptyO else max(
x, self.maxO)))
Each of the specified methods has time complexity O(1). The additional space complexity is O(n),
regardless of the stored keys.
We can improve on the best-case space needed by observing that if an element e being pushed
is smaller than the maximum element already in the stack, then e can never be the maximum, so
we do not need to record it. We cannot store the sequence of maximum values in a separate stack
because of the possibility of duplicates. We resolve this by additionally recording the number of
occurrences of each maximum value. See Figure 8.2 on the following page for an example.
class Stack:
class llaxlf i thcount :
def --init-- 
(seIf, 
max , count) :
self.max, self.count = max, count
def --init--(self);
self,_element = []
seIf._cached_max_with_count = []
def empty(self):
return len(seIf.-element) =- 0
def max(self):
if self. emptyo
99
```

#### Printed page 100 (PDF page 114)

```text
raise IndexError('maxO : empty stack')
return self . -cached-max-with-count [-1] . max
def pop(self):
if self. empty O :
raise IndexError('pop(): empty stack')
pop-element = se1f. -element . pop o
current-max = self ,-cached-max-with-count[-1].max
if pop-element == current-max:
se1f. -cached-max-with-count [ - 1] . count -= 1
if seIf. -cached-max-with-count [ - 1] . count == 0
seIf. -cached-max-with-count . pop ()
return pop-element
def push ( self , x) :
se1f. -element . append (x)
if len(self .-cached-max-with-count) == 0:
self . -cached-max-with-count. append(se1f . llaxwithcount (x, 1) )
else:
current-max = seIf.-cached-max-with-count[-1].max
if x == current-max:
self. -cached-max-with-count [-l] . count += 1
elif x > current-max:
self . -cached-max-with-count. append(seIf . uaxl{ithcount (x, 1))
The worst-case additional space complexity is O(n), which occurs when each key pushed is greater
than all keys in the primary stack. However, when the number of distinct keys is small, or the
maximum changes infrequently, the additional space completty is less, O(1) in the best-case. The
time complexity for each specified method is still O(1).
q
5
;
1
?
a t#
FA
5
4
t-'
1f-
2t:
H
[j] ,
Lrl
lrl
LA bd
[,] *
E]
E]
E]
u,, Lil , [,] *
t_t t-t
aux
3
5
5
4
1
2
2
I =l l-ztl
4
aux.
aux
aux
aux
5
4
0
2
2
2
2
2
2
Figure 8.2: The primary and auxiliary stacks for the following operations: push 2, push 2, push 1, push 4, push 5,
push 5, push 3, pop, pop, pop, pop, push 0, push 3. Both stacks are initially empty, and their progression is shown from
leftto-right, then top-to-bottom. The top of the auxiliary stack holds the maximum element in the stack, and the number
of times that element occurs in the stack. The auxiliary stack is denoted by aux.
100
```
