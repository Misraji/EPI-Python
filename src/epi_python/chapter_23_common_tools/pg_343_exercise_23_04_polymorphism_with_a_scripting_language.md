# Exercise 23.4: Polymorphism with a scripting language

**Printed textbook page:** 343. **Reference transcription pages:** 343–343.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 343 (PDF page 357)

```text
coming in the next few years; and if you choose to work in 3.x, you likely will run into libraries you
simply cannot use because they don't yet support the latest versions of Python.
23.4 PoryuonpnrsM wrrH A scRrprrNc LANGUAGE
Briefly, a fava interface is a kind of type specification. To be precise, it specifies a group of related
methods with empty bodies. (All methods ate nonstatic and public.) Interfaces have many benefits
oveq, for example, abstract classes-in particulaq, they are a good way to implement polymorphic
functions in ]ava.
Describe the advantages and disadvantages of Python and java for polymorphism. In particulal,
how would you implement a polymorphic function in Python?
Solution: )ava's polymorphism is first-class. The compiler is aware at compile-tirne of whatever
interfaces (in the general sense) an object exposes-regardless of whether they derive from actual
interfaces or from superclasses. As a result, a polymorphic function in Java has a guarantee that
any argument to it implements the methods it will call during its execution.
In Python, however, no such safety exists. So there are two tricks to use when implementing
a polymorphic function in Python. First, you can specify your classes using multiple inheritance.
In this case, mEuly of the superclasses are simply interface specifications. These classes, mix-ins,
may implement the desired methods or leave them for the subclass to implement. In effect, they
provide a poor-man's interface. (However, they're not as robust as Java's solution since the method
resolution order gets tricky in multiple-inheritance scenarios.)
But there is a trickier problem here, which is that even if a class is implemented with a particular
method, it's trivial at runtime to overvrrrite that method, e.g., with None, before passing it as an
argument. So you still don't have any guarantees. This motivates the second trick, which is the
use of "duck typing"-that is, rather than trying to get some safety guarantee that cannot exist in
Python, just inspect the object at runtime to see if it exposes the right interface. (The phrase comes
from this adage: "If it looks like a duck, quacks like a duck, and acts like a duck, then it's probably
a duck".) So, where in |ava a developer might write a function that only accepts arguments that
implement a Drawable interface, in Python you would simply call that object's draw method and
hope for the best. Type checking still exists here; it's just deferred to runtime, which implies it may
throw exceptions. The function is still quite polymorphic-more so, in some sense, since it can
accept literally any object that has a draw method.
Build systeffis
A program typically cannot be executed immediately after change: intermediate steps are required
to build the program and test it before deploying it. Other components can also be affected by
changes, such as documentation generated from program text. Build systems automate these steps.
23.5 DspsNnrNcyANALysrs
Argue that a build system such as Make which looks purely at the time stamps of source code and
derived products when determining when a product needs to be rebuilt can end up spending more
time building the product that is needed. How can the you avoid this? Are there any pitfalls to
your approach?
Solution: Suppose a source file is changed without its semantics being affected, e.g., a comment is
added or it's reformatted. Abuild system like Make will propagate this change through dependen-
cies, even though subsequent products are unchanged.
343
```
