# Exercise 22.5: Adapters

**Printed textbook page:** 336. **Reference transcription pages:** 336–336.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 336 (PDF page 350)

```text
22.5 Apeprrns
\,Vhat is the difference between a class adapter and an object adapter?
Solution: The adapter pattern allows the interface of an existing class to be used from another
interface. It is often used to make existing classes work with others without modifying their source
code.
There are two ways to build an adapter: via subclassing (the class adapter pattern) and com-
position (the object adapter pattern). In the class adapter pattem, the adapter inherits both the
interface that is expected and the interface that is pre-existing. In the object adapter pattern, the
adapter contains an instance of the class it wraps and the adapter makes calls to the instance of the
wrapped object.
Here are some remarks on the class adapter pattem.
o The class adapter pattern allows re-use of implementation code in both the target and adaptee.
This is an advantage in that the adapter doesn't have to contain boilerplate pass-throughs or
cut-and-paste reimplementation of code in either the target or the adaptee.
o The class adapter pattem has the disadvantages of inheritance (changes in base class may
cause unforeseen misbehaviors in derived classes, etc.). The disadvantages of inheritance are
made worse by the use of two base classes, which also precludes its use in languages like Java
(prior to |ava 1.8) that do not support multiple inheritance.
o The class adapter can be used in place of either the target or the adaptee. This can be advantage
if there is a need for a two-way adapter. The ability to substitute the adapter for adaptee can
be a disadvantage otherwise as it dilutes the purpose of the adapter and may lead to incorrect
behavior if the adapter is used in an unexpected manner.
o The class adapter allows details of the behavior of the adaptee to be changed by overriding
the adaptee's methods. Class adapters, as members of the class hierarchy, are tied to specific
adaptee and target concrete classes.
As a concrete example of an object adapter, suppose we have legacy code that returns objects of
type stack. Newer code expects inputs of type deque, which is more general than stack (but does not
subclass stack). We could create a new type, stack-adapter, which implements the deque methods,
and can be used anywhere deque is required. The stack-adapter class has a field of type stack-this
is referred to as object composition. It implements the deque methods with code that uses methods
on the composed stack object. Deque methods that are not supported by the underlying stack throw
unsupported operation exceptions. Lr this scenario, the stack-adapter is an example of an object
adapter.
Here are some conunents on the object adapter pattem.
o The object adapter pattern is "purer" in its approach to the purpose of making the adaptee
behave like the target. By implementing the interface of the target only, the object adapter is
only useful as a target.
o Use of an interface for the target allows the adaptee to be used in place of any prospective
target that is referenced by clients using that interface.
o Use of composition for the adaptee similarly allows flexibility in the choice of the concrete
classes. If adaptee is a concrete class, any subclass of adaptee will work equally well within
the object adapter pattem, If adaptee is an interface, any concrete class implementing that
interface will work.
336
```
