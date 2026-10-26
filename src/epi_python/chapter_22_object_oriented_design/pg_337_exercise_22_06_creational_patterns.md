# Exercise 22.6: Creational Patterns

**Printed textbook page:** 337. **Reference transcription pages:** 337–337.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 337 (PDF page 351)

```text
o A disadvantage is that if target is not based on an interface, target and all its clients may need
to change to allow the object adapter to be substituted.
Variant The UML diagrams for decorator, adapter, and proxy look identical, so why is each
considered a separate pattem?
22.6 CnranoNarParrEnNs
Explain what each of these creational pattems is: builder, static factory, factory method, and abstract
factory.
Solution: The idea behind the builder pattem is to build a complex object in phases. It avoids
mutability and inconsistent state by using an mutable inner class that has a build method that
retums the desired object, Its key benefits are that it breaks down the construction process/ and can
give names to steps. Compared to a constructor, it deals far better with optional parameters and
when the parameter list is very long.
A static factory is a function for construction of objects. Its key benefits are as follow: the
function's niune c€u:r make what it's doing much clearer compared to a call to a constructor. The
function is not obliged to create a new object-in particulaq, it can retum a flyweight. It can also
return a subtype that's more optimized, e.g., it can choose to construct an object that uses an integer
in place of a Boolean array if the array size is not more than the integer word size.
A factory method defines interface for creating an object, but lets subclasses decide which class
to instantiate. The classic example is a maze game with two modes-one with regular rooms, and
one with magic rooms. The program below uses a template method, as described in Problem 22.1
on Page 333, to combine the logic common to the two versions of the game.
fron abc import ABC, abstractmethod
class Roon(ABC):
@ab stractmethod
def connect(self, room2)
pass
class l.IazeGame (ABC) :
@abstractnethod
def make-room(seIf):
print ("abstract make-room")
pass
def addRoom(self, room):
print ("adding room")
def --init--(self):
rooml = self.make_roomo
room2 = self.rnake_roono
roomL . connect (room2)
self. addRoom(roon1)
self. addRoom(room2)
This snippet implements the regular rooms. This snippet implements the magic rooms.
JJ/
```
