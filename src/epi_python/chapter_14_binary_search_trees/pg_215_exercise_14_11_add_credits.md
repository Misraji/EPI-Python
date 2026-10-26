# Exercise 14.11: Add credits

**Printed textbook page:** 215. **Reference transcription pages:** 215–216.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 215 (PDF page 229)

```text
14.11, Aon cnsorrs
Consider a server that a large number of clients connect to. Each client is identified by a string.
Each client has a "credit", which is a nonnegative integer value. The server needs to maintain a
data structure to which clients can be added, removed, queried, or updated. Lr addition, the server
needs to be able to add a specified number of credits to all clients simultaneously.
Design a data structure that implements the following methods:
o Insert: add a client with specified credit, replacing any existing entry for the client.
o Remove: delete the specified client.
o Lookup: return the number of credits associated with the specified client.
o Add-to-all: increment the credit count for all current clients by the specified amount.
o Max: retum a client with the highest number of credits.
Hint:Use additional global state.
Solution: A hash table is a natural data structure for this application. Howevel, it does not support
efficient max operations, nor is there an obvious way to perform the simultaneous increment, short
traversing all entries. A BST does have efficient max operation, but it too does not natively support
the global increment.
A general principle when addingbehaviors to an object is to wrap the object, and add functions
in the wraPPet which add behaviors before or after delegating to the object. In our contex! this
suggests storing the clients in a BST, and having the wrapper track the total increment amount.
For example, if we have clients A,B, C, with credits 1.,2,3, respectively, and want to add 5 credits
to each, the wrapper sets the total increment amount to 5. A lookup on B then is performed by
looking up in the BST, which retums 2, and then adding 5 before returning. If we want to add 4
more credits to each, we simply update the total increment amount to 9.
One issue to watch out for is what happens to clients inserted after a call to the add-to-all
function. Continuing with the given example, if we were to now add D with a credit of 6, the
lookup would retum 6 + 9, which is an error.
The solution is simple-subtract the increment from the credit, i.e., add D with a credit of
6 - 9 = -3 to the BST. Now a lookup for D will retum -3 + 9, which is the correct amount.
More specifically, the BST keys are credits, and the corresponding values are the clients with
that credit. This makes for fast max-queries. Howevet to perform lookups and removes by client
quickly, the BST by itself is not enough (since it is ordered by credit, not client id). We can solve this
by maintaini.g an additional hash table in which keys are clients, and values are credits. Lookup
is trivial. Removes entails a lookup in the hash to get the credit, and then a search into the BST to
get the set of clients with that credit, and finally a delete on that set.
class Clientscreditslnfo 
:
def __init__(self):
se1f._offset = 0
self._client_to_credit 
= {}
self ._credit_to_clients = bintrees.RBTreeo
def insert (se1f, client_id , c) :
self . remove (client_id)
seIf.-client-to-creditIclient_id] 
= c - se1f._offset
self._credit_to_clients. setdefault(c - self ._offset,
setO). add(client_id)
21.5
```

#### Printed page 216 (PDF page 230)

```text
def remove(se1f , client-id) 
:
credit = self.-client-to-credit. 
get(client-id)
if credit is not None:
seIf. -credit-to-clients 
Icredit] . renove (client-id)
if not seIf. -credit-to-clients 
Icredit] :
del self . -credit-to-clients 
Icredit]
del self . -client-to-credit 
Iclient-id]
return True
return False
def lookup(self, client-id) 
:
credit = self.-client-to-credit. 
get(client-id)
return -1 if credit is None else credit + self.-offset
def add-all (self, C) :
se1f.-offset *= C
def rnax(seIf):
if not self, -credit-to-clients:
return "
clients = self.-credit-to-clients,max-itemO 
[1]
return " if not clients else nett(iter(clients))
The time complexity to insert and remove is dominated by the BST, i.e., O(logn), where n is the
number of clients in the data structure. Lookup and add-to-all operate only on the hash table, and
have O(1) time complexity. Library BST implementations uses caching to perform max in O(1) time.
2t6
```
