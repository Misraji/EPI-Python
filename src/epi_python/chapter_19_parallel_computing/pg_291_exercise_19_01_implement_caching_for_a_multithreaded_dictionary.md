# Exercise 19.1: Implement caching for a multithreaded dictionary

**Printed textbook page:** 291. **Reference transcription pages:** 291–291.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 291 (PDF page 305)

```text
79,1 IlrprrNlsNr cACHTNG FoR A MULTTTHREADED DrcrroNARy
The program below is part of an online spell correction service. Clients send as input a string,
and the service returns an array of strings in its dictionary that are closest to the input string (this
array could be computed, for example, using Solution 1.6.2 onPage 239). The service caches results
to improve performance. Critique the implementation and provide a solution that overcomes its
limitations.
class SpellCheckService :
w-last = closest_to_last_word = None
@staticmethod
def service (req , resp) :
w = req. extract_word_to_check_from_request ()
if w != SpeIlCheckService.w_last:
SpellCheckService.w_last = w
SpellCheckService, closest_to_1ast_word = closest_in*dictionary(w)
resp. encode_into_response (SpellCheckService, closest_to_1ast_word)
Hint: Look for races, and lock as little as possible to avoid reducing throughput.
Solution: The solution has a race condition. Suppose clients A and B make concurrent requests,
and the service launches a thread per request. Suppose the thread for requestA finds that the input
string is present in the cache, and then, immediately #ter that check, the thread for request B is
scheduled. Suppose this thread's lookup fails, so it computes the result, and adds it to the cache.
If the cache is full, an entry will be evicted, and this may be the result for the string passed in
request A. Now when request A is scheduled back, it does a lookup for the value corresponding
to its input string, expecting it to be present (since it checked that that string is a key in the cache).
Howeve4 the cache will return null.
A thread-safe solution would be to slmchronize every call to the service. In this case, only
one thread could be executing the method and there are no races befween cache reads and writes.
However, it also leads to poor performance--only one thread can execute the service call at a time.
The solution is to lock just the part of the code that operates on the cached values-specifically,
the check on the cached value and the updates to the cached values:
In the Program below, multiple threads can be concurrently computing closest strings. This is
good because the calls take a long time (this is why they are cached). Locking ensures that the read
assignment on a hit and write assignment on completion are atomic.
class SpellCheckService :
w-last = closest_to_last_word = None
lock = threading.Locko
@staticmethod
def service (req , resp) :
w = req. extract_word_to_check_from_requesto
result = None
with SpellCheckService . lock:
if w == SpellCheckService.w_last:
result = SpellCheckService . closest_to_Iast_word. copy o
if result is None:
result = closest_in_dictionary(w)
with SpellCheckService. lock:
SpellCheckService.w-Iast = w
291,
```
