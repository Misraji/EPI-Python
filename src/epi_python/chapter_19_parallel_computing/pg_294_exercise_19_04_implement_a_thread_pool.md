# Exercise 19.4: Implement a thread pool

**Printed textbook page:** 294. **Reference transcription pages:** 294–294.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 294 (PDF page 308)

```text
def --init--(self):
super O . --init-- o
self.turn = self.0DD-TURN
def wait-turn(self , old-turn) :
with self:
$hile self.turn != old-turn
self. wait ()
def toggle-turn(se1f) :
with self:
self.turn ^= True
self, notify o
class oddThread(threading. Thread)
def --init--(self , monitor) :
superO.--init--o
self.monitor = nonitor
class EvenThread(threading. Thread) :
def --init--(seIf , nonitor):
super O . --init-- o
self.monitor = monitor
def run
for
( self) :
i ln range(l, 1O1, 2):
self, monitor , wait-turn (oddEvenl{onitor . oDD-TURN)
print ( i )
self. rnonitor . toggle-turn o
def run(self):
for i in range(z, 101, 2):
se1f. nonitor , wait-turn (OddEvenllonitor . EVEN-TURN)
print (i)
seIf. monitor . toggle-turn o
19.4 Inpr-slruNr A THREAD PooL
The following program, implements Part of a simple HTIP server:
SERVERPORT = 8080
def mainO:
serversock = socket . socket (socket . AF-IilET , socket . S0CK-STREAII)
serversock.bind(( ", 
SERVERP0RT))
serversock. listen(5)
rhile True:
sock, addr = serversock,accepto
process-req(sock)
294
```
