# Exercise 22.2: Observer pattern

**Printed textbook page:** 334. **Reference transcription pages:** 334–334.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 334 (PDF page 348)

```text
quicksort an object that implements a compare method. These objects constitute an example of the
strategy pattem, as do the objects implementing pivot selection and partitioning.
There are some other smaller differences between the two pattems. For example, in the template
method pattern, the superclass algorithm may have "hooks"---talls to placeholder methods that
can be overridden by subclasses to provide additional functionality. Sometimes a hook is not
implemented, thereby forcing the subclasses to implement that functionality; some times it offers a
"no-operation" or some baseline functionality. There is no analog to a hook in a strategy pattern.
Note that there's no relationship between the template method pattem and template meta-
programming (a form of generic programming favored in C++).
22.2 Onsrnvrn PATTERN
Explain the observer pattem with an example.
Solution: The observer pattem defines a one-to-many dependency between objects so that when
one object changes state all its dependents are notified and updated automatically.
The observed object must implement the following methods.
r Register an observer.
o Remove an observer.
o Notify all currently registered observers.
The observer object must implement the following method.
o Update the observer. (Update is sometimes refeffed to as notify.)
As a concrete example, consider a service that logs user requests, and keeps track of the 10
most visited pages. There may be multiple client applications that use this information, e.g., a
leaderboard display, ad placement algorithms, recorunendation system, etc. Instead of having
the clients poll the service, the service, which is the observed object, provides clients with register
and remove capabilities. As soon as its state changes, the service enumerates through registered
observers, calling each observer's update method.
Though most readily understood in the context of a single program, where the observed and
observer are objects, the observer pattern is also applicable to distributed computing.
22.3 Pusu vs. PULL oBsERvER PATTERN
In the observer pattem, subjects push information to their observers. There is another way to
update data-the observers rr.ay "ptrll" the information they need from the subject. Compare and
contrast these two approaches.
Solution: Both push and pull observer designs are valid and have tradeoffr depending on the
needs of the project. With the push design, the subject notifies the observer that its data is ready and
includes the relevant information that the observer is subscribing to, whereas with the pull design,
it is the observer's job to retrieve that information from the subject.
The pull design places a heavier load on the observers, but it also allows the observer to query
the subject only as often as is needed. One important consideration is that by the time the observer
retrieves the information from the subject, the data could have changed. This could be a positive
or negative result depending on the application. The pull design places less responsibility on the
subject for tracking exactly which information the observer needs, as long as the subject knows
334
```
