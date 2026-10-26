# Exercise 12.3: Implement an ISBN cache

**Printed textbook page:** 165. **Reference transcription pages:** 165–165.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 165 (PDF page 179)

```text
collections, Counter (magazine_text ) )
In the worst-case, the letter is not constructible or the last character of the magazine is essentially
required. Therefore, the time complexity is O(m + n) where m and n are the number of characters in
the letter and magazine, respectively. The space complexity is the size of the hash table constructed
in the pass over the lefter, i.e., O(L), where L is the number of distinct characters appearing in the
letter.
If the characters are coded in ASCII, we could do away with the hash table and use a 256 entry
integer array A, with.4[] being set to the number of times the character I appears in the letter.
12.3 INrpr.ulrsNr aN ISBN cACHE
The Intemational Standard Book Number (ISBN) is a unique commercial book identifier. It is a
string of length 10. The first 9 characters are digits; the last character is a check character. The check
character is the sum of the first 9 digits, mod 11, with 10 represented by 'X'.(Modem ISBNs use
13 digits, and the check digit is taken mod 10; this problem is concerned with 10-digit ISBNs.)
Create a cache for looking up prices of books identified by their ISBN. You implement lookup,
insert, and remove methods. Use the Least Recently Used (LRU) policy for cache eviction. If an
ISBN is already present, insert should not change the price, but it should update that entry tobe the
most recently used entry. Lookup should also update that entry to be the most recently used entry.
Hint: Amofilze the cost of deletion. Altematively, use an auxiliary data structure.
Solution: Hash tables are ideally suited for fast lookups. We can use a hash table to quickly lookup
price by using ISBNs as keys. Along with each key, we store a value, which is the price and the
most recent time a lookup was done on that key.
This yields O(1) lookup times on cache hits. Inserts into the cache are also O(1) time, until the
cache is full. Once the cache fills up, to add a new entry we have to find the LRU entry, which will
be evicted to make place for the new entry. Finding this entry takes O(n) time, where n is the cache
size.
One way to improve performance is to use lazy garbage collection. Specifically, let's say we
want the cache to be of size n. We do not delete any entries from the hash table until it grows to
2n entries. At this point we iterate through the entire hash table, and find the median age of items.
Subsequently we discard everything below the median. The worst-case time to delete becomes
O(n)but it will happen at most once every n operations. Therefore, the amortized time to delete is
O(1). The drawback of this approach is the O(n) time needed for some lookups that miss on a full
cache, and the O(n) increase in memory,
An altemative is to maintain a separate queue of keys. In the hash table we store for each key
a reference to its location in the queue. Each time an ISBN is looked up and is found in the hash
table, it is moved to the front of the queue. (This requires us to use a linked list implementation of
the queue, so that items in the middle of the queue can be moved to the head.) V/hen the length of
the queue exceeds n,whena new element is added to the cache, the item at the tail of the queue is
deleted from the cache, i.e., from the queue and the hash table.
class LRUCache:
def --init--(self 
, capacity)
165
```
