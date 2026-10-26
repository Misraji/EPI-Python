# Exercise 22.1: Template Method vs Strategy

**Printed textbook page:** 333. **Reference transcription pages:** 333–333.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 333 (PDF page 347)

```text
Csaprsn
Obi ect-Oriented Design
One thing expert designers know not to do is soloe euery problem from first
principles.
- "Design Patterns: Elements of Reusablc Object-Oiented Software,"
E. Garuua, R. Hur'.r, R. E. ]onNsoN, eNo |. M. Vrrssrors, 1994
A class is an encapsulation of data and methods that operate on that data. Classes match the way
we think about computation. They provide encapsulation, which reduces the conceptual burden of
writing code, and enable code reuse, through the use of inheritance and polymorphism. Howevel,
naive use of object-oriented constructs can result in code that is hard to maintain.
A design pattem is a general repeatable solution to a commonly occurring problem. It is not a
complete design that can be coded up directly-rather, it is a description of how to solve a problem
that arises in many different situations. In the context of object-oriented programming, design
patterns address both reuse and maintainability. In essence, design pattems make some parts of a
system vary independently from the other parts.
Adnan's Design Pattern course material, available freely online, contains lecture notes, home-
works, and labs that may serve as a good resource on the material in this chapter.
22.1, Trlaprars Mrrson vs, Srn,rrrcy
Explain the difference between the template method pattern and the strategy pattern with a concrete
example.
Solution: Both the template method and strategy pattems are similar in that both are behavioral
pattems, both are used to make algorithms reusable, and both are general and very widely used.
However, they differ in the following key way:
o In the template method, a skeleton algorithm is provided in a superclass. Subclasses can
override methods to specialize the algorithm.
o The strategy pattern is typically applied when a family of algorithms implements a common
interface. These algorithms can then be selected by clients.
As a concrete example, consider a sorting algorithm like quicksort. TWo of the key steps in
quicksort are pivot selection and partitioning. Quicksort is a good example of a template method-
subclasses can implement their own pivot selection algorithm, e.g., using randomized median
finding or selecting an element at random, and their own partitioning method, e.g., using the DNF
partitioning algorithms in Solution 5.1 on Page 40.
Since there may be multiple ways in which to sort elements, e.g., student objects may be
compared by GPA, majo1, name, and combinations thereof, it's natural to make the comparison
operation used by the sorting algorithm an €rgument to quicksort. One way to do this is to pass
JJJ
```
