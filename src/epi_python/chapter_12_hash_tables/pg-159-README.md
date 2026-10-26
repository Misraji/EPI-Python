# Chapter 12: Hash Tables

**Starts at printed page 159.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 159

```text
Cnaprrn
Hash Tables
The new methods are intended to reduce the amount of space required to
contain the hash-coded infurmatian from thnt associated with conoentional
methods. The reduction in space is accomplisheil by exploiting the possibil-
ity that a small fraction of urors of commission may be toluable in some
applications.
- 
" Space/time trade-offs in hash coding with allowable errors,"
B. H. Br.oorvr, 1970
A hash table is a data structure used to store keys, optionally, with corresponding values. Inserts,
deletes and lookups run in O(1) time on average.
The underlying idea is to store keys in an array. A key is stored in the array locations ("slots")
based on its "hash code". The hash code is an integer computed from the key by a hash function.
If the hash function is chosen well, the objects are distributed uniformly across the array locations.
If two keys map to the same location, a "collision" is said to occur. The standard mechanism to
deal with collisions is to maintain a linked list of objects at each array location. If the hash ftmction
does a good job of spreading objects across the underlying array and take O(1) time to compute, on
average, lookups, insertions, and deletions have O(1 + n lm) time complexity, where n is the number
of objects arrd m is the length of the array. If the "load" n f m grows large, rehashing can be applied
to the hash table. A new array with a larger number of locations is allocated, and the objects are
moved to the new array. Rehashing is expensive (O(n + ru) time) but if it is done infrequently (for
example, whenever the number of entries doubles), its amortized cost is low.
A hash table is qualitatively different from a sorted array-keys do not have to appear in order,
and randomization (specifically, the hash function) plays a central role. Compared to binary search
trees (discussed in Chapter 14), inserting and deleting in a hash table is more efficient (assuming
rehashing is infrequent). One disadvantage of hash tables is the need for a good hash ft:nction but
this is rarely an issue in practice. Similarly, rehashing is not a problem outside of realtirne systems
and even for such systems, a separate thread can do the rehashing.
A hash function has one hard requirement-equal keys should have equal hash codes. This may
seem obvious, but is easy to get wrong, e.9., by writing a hash function that is based on address
rather than contents, or by including profiling data.
A softer requirement is that the hash ftrnction should "spread" keys, i.e., the hash codes for a
subset of objects should be uniformly distributed across the underlying array. In addition, a hash
fimction should be efficient to compute.
A common mistake with hash tables is that a key that's present in a hash table will be updated.
The consequence is that a lookup for that key will now fail, even though it's still in the hash table.
If you have to update a key, first remove it, then update it, and finally, add it back-this ensures it's
moved to the correct array location. As a rule, you should avoid using mutable objects as keys.
159
```

### Printed page 160

```text
Now we illustrate the steps for designing a hash function suitable for strings. First, the hash
function should examine all the characters in the string. It should give a large range of values, and
should not let one character dominate (e.g., if we simply cast characters to integers and multiplied
them, a single 0 would result in a hash code of 0). We would also like a rolling hash function, one in
which if a character is deleted from the front of the string, and another added to the end, the new
hash code can be computed in O(1) time (see Solution 6.13 on Page 80). The following function has
these properties:
def string-hash(s, modulus) :
I'IULT = 997
A hash table is a good data structure to represent a dictionary, i.e., a set of strings. In some
applications, a trie, which is a tree data strucfure that is used to store a dynamic set of strings, has
computational advantages. Unlike a BSI nodes in the tree do not store a key. Instead, the node's
position in the tree defines the key which it is associated with.
Hash tables boot camp
We introduce hash tables with two examples-one is an application that benefits from the algorith-
mic advantages of hash tables, and the other illustrates the design of a class that can be used in a
hash table.
An application of hash tables
Anagrams are popular word play ptzzles, whereby rearranging letters of one set of words, you
get another set of words. For example, "eleven plus two" is an anagram for "twelve plus one".
Crossword puzzle enthusiasts and Scrabble players benefit from the ability to view all possible
iuragrams of a given set of letters.
Suppose you were asked to write a program that takes as input a set of words and retums groups
of anagrams for those words. Each group must contain at least two words,
For example, if the input is "debitcard", "elyis", "silent", "badcredit", "lives", "fteedom",
"listen", "levis", "money" then there are three groups of anagrams: (1.) "debitcatd", "badcredit";
(2.) " elvis" , "lives" , "levis"; (3.) "silent", "listen". (Note that "money" does not appear in any group,
since it has no anagrams in the set.)
Let's begin by considering the problem of testing whether one word is an anagram of another.
Since anagrams do not depend on the ordering of characters in the strings, we can perform the
test by sorting the characters in the string. TWo words are ,magrams if and only if they result
in equal strings after sorting. For example, sort("logarithmic") and sort("algorithmic") are both
"acghiilmort", sa "logarithmic" and "algorithmic" are anagrams.
We can form the described grouping of strings by iterating through all strings, and comparing
each string with all other remaining strings. If two strings are anagrams, we do not consider the
second string again. This leads to anO(n2mlogm) algorithm, where n is the number of strings and
m is the maximum string length.
Looking more carefully at the above computation, note that the key idea is to map strings to
a representative. Given any string, its sorted version can be used as a unique identifier for the
anagram group it belongs to. What we want is a map from a sorted string to the anagrams it
760
```

### Printed page 161

```text
corresPonds to. Anytime you need to store a set of strings, a hash table is an excellent choice. Our
final algorithm proceeds by adding sort(s) for each string s in the dictionary to a hash table. The
sorted strings are keys, and the values are arrays of the corresponding strings from the original
input.
def find-anagrams (dictionary) :
sorted_string_to_anagrams = collections. defaultdict(list)
for s in dictionary:
# Sorts the string, uses it as a key, and then appends tle original
# string as another value into hash table.
sorted_string_to_anagrams [ " . join(sorted(s)) ] . append(s)
return I
group for group in sorted_string_to_anagrams.values() if len(group) >= 2
l
The computation consists of n calls to sort and n insertions into the hash table. Sorting all the
keys has time complexity O(nmlogm). The insertions add a tirne complexity of O(nm), yielding
O(nmlogm) time complexity in total.
Variant: Design anO(nm) algorithm for the same problem, assuming strings are made up of lower
case English characters.
Design of a hashable class
Consider a class that represents contacts. For simplicity, assume each contact is a string. Suppose
it is a hard requirement that the individual contacts are to be stored in a list and it's possible that
the list contains duplicates. Two contacts should be equal if they contain the same set of strings,
regardless of the ordering of the strings within the underlying list. Multiplicity is not important,
i.e., three repetitions of the same contact is the same as a single instance of that contact. In order to
be able to store contacts in a hash table, we first need to explicitly define equaliry which we can do
by forming sets from the lists and comparing the sets.
In our context, this implies that the hash function should depend on the strings present, but not
their ordering; it should also consider only one copy if a string appears in duplicate form. It should
be pointed out that the hash function and equals methods below are very inefficient. In practice,
it would be advisable to cache the underlying set and the hash code, remembering to void these
values on updates.
class Contactlist:
def __init__(self , names) :
names is a -Iist of strings
self.names = names
def --hash--(seIf):
# ConceptuaTTy we want to hash the set o.f nafies, Since the set type is
# nutabTe, it cannot be hashed. Therefore ,rre use frozenset.
return hash (frozenset ( self . names) )
def --eq--(self, 
other):
return set(self.names) == set(other.names)
161
```

### Printed page 162

```text
def merge-contact-lists (contacts) :
contacts is a list of contactList
return list (set (contacts) )
The time complexity of computing the hash is O(n), where n is the number of strings in the
contact list. Hash codes are often cached for performance, with the caveat that the cache must be
cleared if object fields that are referenced by the hash function are uPdated.
the best theoretical and
Each of these operations has O(1) time complexity. The O(1) time complexity for insertion is for
the average case-a single insert can take O(n) if the hash table has to be resized.
Consider using a hash code as a signature to enhance performance,, e.g.t to filter out candidates.
Consider using a precomputed lookup table instead of boilerplate iJ-then code for mappings,
e.g., from character to value, or character to character.
When defining your own type that will be put in a hash table, be sure you understand the
relationship between logical equality and the fields the hash function must inspect. Specifi-
cally, anytime equality is implemented, it is imperative that the correct hash function is also
implemented, otherwise when objects are placed in hash tables, logically equivalent objects may
appear in different buckets, leading to lookups returning false, even when the searched item is
present.
Sometimes you'll need a multimap, i.e., a map that contains multiple values for a single key, or
a bi-directional map. If the language's standard libraries do not provide the functionality you
need, leam how to implement a multimap using lists as values, or find a third party library
that has a multimap.
Table 12.1 : Top Tips for Hash Tables
Know your hash table libraries
There are multiple hash table-based data structures commonly used in Python-set, dict,
collections. defaultdict, and collections. Counter. The difference between set and the other
three is that is set simply stores keys, whereas the others store key-value pairs. All have the
property that they do not allow for duplicate keys, unlike, for example, list.
In a dict, accessing value associated with a key that is not present leads to a KeyError exception.
However, a collections. defaultdict retums the defaultvalue of the type thatwas specifiedwhen
thecollectionwasinstantiated,e.g.,ifd = collections.defaultdict(list),thenif k not in d
then d [k] is tl. A collections . Counter is used for counting the number of occurrences of keys,
with a number of setlike operations, as illustrated below.
c = collections.Counter(a=3, b=1)
d = collections . Counter (a=1 , b=2)
# add two counters together: ctxl + d[x], coTTections.Counter(f'a': 4,
c+d
162
b': 3])
```
