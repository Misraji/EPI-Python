# Exercise 22.4: Singletons and Flyweights

**Printed textbook page:** 335. **Reference transcription pages:** 335–335.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 335 (PDF page 349)

```text
when to notify the observer. This design also requires that the subject make its data publicly
accessible by the observers. This design would likely work better when the observers are running
with varied frequency and it suits them best to get the data they need on demand.
The push design leaves all of the information transfer in the subject's control. The subject calls
update for each observer and passes the relevant information along with this call. This design
seems more object-oriented, because the subject is pushing its own data out, rather than making its
data accessible for the observers to pull. It is also somewhat simpler and safer in that the subject
always knows when the data is being pushed out to observers, so you don't have to worry about an
observer pulling data in the middle of an update to the data, which would require synchronization.
22.4 SlncrnroNs aNo Frywrrcrrrs
Explain the differences between the singleton pattem and the flyweight pattem. Use concrete
examples.
Solution: The singleton pattern ensures a class has only one instance, and provides a global point
of access to it. The flyweight pattern minimizes memory use by sharing as much data as possible
with other similar objects. It is a way to use objects in large numbers when a simple repeated
representation would use an unacceptable amount of memory.
A common example of a singleton is a logger. There may be many clients who want to listen to
the logged data (console, hle, messaging service, etc.), so all code should log to a single place.
A common example of a flyweight is string inteming-a method of storing only one copy of
each distinct string value. Inteming strings makes some string processing tasks more time- or
space-efficient at the cost of requiring more time when the string is created or intemed. The distinct
values are usually stored in a hash table. Since multiple clients may refer to the same flyweight
object for safety flyweights should be immutable.
There is a superficial similarity between singleton and flyweight both keep a single copy of an
object. There are several key differences between the two:
o Flyweights are used to save memory. Singletons are used to ensure all clients see the same
object.
o A singleton is used where there is a single shared object, e.g., a database corurection, server
configurations, a logger, etc. A flyweight is used where there is a family of shared objects,
e.g., objects describing character fonts, or nodes shared across multiple binary search trees.
o Flyweight objects are invariable immutable. Singleton objects are usually not immutablll e.g,
requests can be added to the database connection object.
o The singleton pattem is a creational pattern, whereas the flyweight is a structural pattem.
In summary a singleton is like a global variable, whereas a flyweight is like a pointer to a canonical
representation.
Sometimes, but not always, a singleton object is used to meate flyweights---dients ask the
singleton for an object with specified fields, and the singleton checks its intemal pool of flyweights
to see if one exists. If such an object already exists, it returns that, otherwise it creates a new
flyweight, add it to its pool, and then retums it. (L:r essence the singleton serves as a gateway to a
static factory.)
335
```
