# Exercise 20.4: Pair users by attributes

**Printed textbook page:** 305. **Reference transcription pages:** 305–305.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 305 (PDF page 319)

```text
moved around.) By normalizing ids, we can cast the problem back into one of finding corunon
substrings.
The approach we have just described is especially effective when the number of files is very
large and the files are spread over mtlny servers. In particular, the map-reduce framework can be
used to achieve the effect of a single G spread over many servers.
20.4 PerR usrns By ATTRTBUTES
You are building a social network where each user specifies a set of attributes. You would like to
pair each user with another unpaired user that specified the same set of attributes.
You are given a sequence of users where each user has a unique 32-bit integer key and a set of
attributes specified as strings. Uy'hen you read a user, you should pair that user with another
previously read user with identical attributes who is currently unpaired, if such a user exists. If the
user cannot be paired, you should add him to the unpaired set.
Hint: Map sets of atlributes to strings.
Solution: First, we examine the algorithmic core of this problem. Later we will consider imple-
mentation details, particularly those related to scale.
A brute-force algorithm is to compare each new user's attributes with the attributes of users in
the unpaired set. This leads to O(nz) time complexity, where n is the number of users.
To improve the time complexity, we need a way to find users who have the same attributes as
the new user. A hash table whose keys are subsets of attributes and values are users is the perfect
choice. This leaves us with the problem of designing a hash function which is suitable for subsets
of attributes.
If the total number of possible attributes is small, we can represent a subset of attributes with
abit anay, where each index represents a specific attribute. Specifically, we store a 1 at an index
if that attribute is present. We can then use any hash function for bit arrays. The time complexity
to process the n users is a hash lookup per uset i.e., O(nm), where tz is the number of distinct
attributes. The space complexity is also O(nm)-n entries, each of size m.
If the set of possible attributes is large, and most users have a small subset of those attributes, the
bit vector representation for subsets is inefficient from both a time and space perspective. A better
approach to represent sparse subsets is directly record the elements. To ensure equal subsets have
equal hash codes, we need to represent the subsets in a unique way. One approach is to sort the
elements. We can view the sorted sequence of attributes as a single string, namely the concatenation
the individual elements. We then use a hash function for strings. For example, if the possible
attributes are {USA, Senior, Income, Prime Customer}, and a user has attributes {USA, Income}, we
represent his set of attributes as the string "Income,USA".
The time complexity of this approach is O(M), where M is the sum of the sizes of the attribute
sets for all users.
Now we consider implementation issues. Suppose the network is small enough that a single
machine can store it. For such a system, you can use database with Users table, Attributes table,
and a join table between them. Then for every attribute you will find matches (or no match) and
based on criteria you can decide if user could join a group or start a new one. If you do not like
to use a database and want to reinvent the wheel, you still can use similar approach and get a list
305
```
