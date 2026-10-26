# Exercise 22.7: Libraries and design patterns

**Printed textbook page:** 338. **Reference transcription pages:** 338–338.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 338 (PDF page 352)

```text
class l,lagi cllazeGame (l{azeGame ) :
def make-room(seIf):
return l'lagi cRoom o
class llagicRoon(Room) :
def connect(self, room2) :
print("connecting magic room")
Here's how you use the factory to create regular and magic games.
ordinary-maze-game = ordinary-maze-game. 0rdinaryHazeGame o
magic-maze-game = magic-maze-game. I'lagicl{azeGame o
A drawback of the factory method pattern is that it makes subclassing challenging.
An abstract factory provides an interface for creating families of related objects without sPecify-
ing their concrete classes. For example, a class DocumentCreator could provide interfaces to create
anumberof products,suchascreateletterO andcreateResumeO. Concreteimplementationsof
this class could choose to irnplement these products in different ways, e.9., with modern or classic
fonts, right-flush or right-ragged layout, etc. Client code gets a DocumentCreator object and calls
its factory methods. Use of this pattem makes it possible to interchange concrete implementations
without changing the code that uses them, even at runtime. The price for this flexibility is more
planning and upfront coding, as well as and code that may be harder to understand, because of the
added indirections.
22.7 Lrsranlrs AND DEsIGN pATTERNS
Why is there no library of design pattems so a developers do not have to write code every time
they want to use them?
Solution: There are several reasons that design pattems carurot be delivered as a set of libraries.
The key idea is that pattems cannot be cleanly abstracted from the objects and the Processes they are
applicable to. More specifically, libraries provide the implementations of algorithms. In contrast,
design pattems provide a higher level understanding of how to structure classes and objects to
solve specific types of problems. Another difference is that it's often necessary to use combinations
of different pattems to solve a problem, e.g., Model-View-Controller (MVC), which is commonly
used in UI design, incorporates the Observer,strategy, and Composite pattems. It's not reasonable
to come up with libraries for every possible case.
Of course, many libraries take advantage of design pattems in their implementations: sorting
and searching algorithms use the template method pattem, custom comparison functions illustrate
the strategy pattem, string interning is an example of the flyweight pattem, typed-I/O shows off
the decorator pattern, etc.
Variant: Give examples of commonly used library code that use the following pattems: template,
strategy, observer, singleton, flyweight, static factory, decorator, abstract factory.
Varianh Compare and contrast the iterator and composite patterns.
338
```
