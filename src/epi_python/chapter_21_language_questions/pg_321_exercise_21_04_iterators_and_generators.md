# Exercise 21.4: Iterators and Generators

**Printed textbook page:** 321. **Reference transcription pages:** 321–321.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 321 (PDF page 335)

```text
21,4 Irrnerons aNo GsNsRArons
\A/hat is the difference between an iterator and a generator?
Solution: First, recall what an iterator is-it's any object that has --iter--O and --next-o
methods. The first returns the iterator object itself, and is used is used in for and in statements.
The second method retums the next value in the iteration-if there is no more items it raises the
Stoplteration exception. Here is an iterator that returns numbers that increment by a random
amount between 0 and 1, stopping at a limit specified in the constructor.
# IterabTe object, impTements __iter__(), __next__11
class Randomlncrement O :
def __init__(se1f, limit) 
:
self.-offset 
= 0.0
self._limit 
= limit
def --iter--(self)
return self
def --next__(self):
seIf. _offset += random. random o
if (seIf.-offset > seIf.-lirnit)
raise Stoplterationo
return self. _offset
# Call thjs to change the stop condjtjon. ft's safe to interTeave tljs,rjth
# usage of the iterator.
def increment-1imit(self , increment_amount) :
self.-1imit 
+= increment-amount
A generator is an easy way to create iterators. As a concrete example, here is the same iterator
expressed as a generator. Note the use of the keyword yield.
def random-it€rator (Iimit) :
offset = 0
nhile True:
offset += random.randomo
if (offset > limit):
raise Stoplterationo
yield offset
A generator uses the function call stack to implicitly store the state of the iterator-this can simplify
the writing of an iterator compared to writing the same iterator as an explicit class; it also helps
readability,
Every generator is an iterator, but the converse is not true. In particulaq, an iterator can be a full-
blown class, and can therefore offer additional functionality. For example, it's easy to add a method
to the iterator class above to change the iteration limit-this is impossible with the generator.
21,.5 @orcoRlron
Explain what a decorator is, with an example that shows why its useful.
321.
```
