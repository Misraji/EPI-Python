# Exercise 11.9: Find the missing IP address

**Printed textbook page:** 155. **Reference transcription pages:** 155–156.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 155 (PDF page 169)

```text
the smallest or largest element in the current subarray. The probability of the worst-case reduces
exponentially with the length of the input array, and the worst-case is a nonissue in practice. For
this reason, the randomize selection algorithm is sometimes said to have almost certain O(n) time
complexity.
Variant: Design an algorithm for finding the median of an array,
Varianh Design an algorithm for finding the kth largest element of .4 in the presence of duplicates.
The kth largest element is defined to be A[k * 1] after A has been sorted in a stable manner, i.e., if
A[il = Alj] and I < 7 then AUI must appear before Alj) after stable sorting.
Varianfi A number of apartment buildings are coming up on a new street. The postal service
wants to place a single mailbox on the street. Their objective is to minimize the total distance
that residents have to walk to collect their mail each day. (Different buildings may have different
nurnbers of residents.)
Devise an algorithm that computes where to place the mailbox so as to minimize the total
distance, that residents travel to get to the mailbox. Assume the input is specified as an array of
building objects, where each building object has a field indicating the number of residents in that
building, and a field indicating the building's distance from the start of the street.
1'1,.9 FrNp rur MrssrNG IP.lnpREss
The storage capacity of hard drives dwarfs that of RAM. This can lead to interesting space-time
trade-ofb.
Suppose you were given a file containing roughly one billion IP addresses, each of which is a 32-bit
quantity. How would you programmatically find an IP address that is not in the file? Assume you
have unlimited drive space but only a few megabytes of RAM at your disposal.
Hint: Can you be sure there is an address which is not in the file?
Solution: Since the file can be treated as consisting of 32-bit integers, we can sort the input file
and then iterate through it, searching for a gap between values. The time complexity is O(nlogn),
where n is number of entries. Furthermore, to keep the RAM usage low, the sort will have to use
disk as storage, which in practice is very slow
Note that we cannot just compute the largest entry and add one to it, since if the largest entry
is 255.255.255.255 (the highest possible IP address), adding one to it leads to overflow The same
holds for the smallest entry. (In practice this would be a good heuristic.)
We could add all the IP addresses in the file to a hash table, and then enumerate IP addresses,
starting with 0.0.0.0, until we find one not in the hash table. This requires a minimum of 4 gigabytes
of RAM to store the data.l
We can reduce the storage requirement by an order of magnitude by using a bit array represen-
tation for the set of all possible IP addresses. Specifically, we allocate an array of 232 bits, initialized
to 0, and write a 1 at each index that corresponds to an IP address in the file. Then we iterate
through the bit array, looking for an entry set to 0. There are232 : 4 x 10e possible IP addresses, so
1A hash table has additional memory overhead, e.g., the table itself, as well as the next-fields in the collision chains,
which amounts to roughly 5 gigabytes on a 32-bit machine.
155
```

#### Printed page 156 (PDF page 170)

```text
not all IP addresses appear in the file. The storage is 232 18bytes, is half a gigabyte. This is still well
in excess of the storage limit.
Since the input is in a file, we can make multiple passes through it. We c;u:l use this to narow
the search down to subsets of the space of all IP addresses as follows. We make a pass through
the file to count the number of IP addresses present whose leading bit is a 1, and the number of IP
addresses whose leading bit is a 0. At least one IP address must exist which is not present in the
file, so at least one of these two counts is below 231. For example, suppose we have determined
using counting that there must be an IP address which begins with 0 and is absent from the file.
We can focus our attention on IP addresses in the file thatbegin with 0, and continue the process of
elimination based on the second bit. This entails 32 passes, and uses only two integer-valued count
variables as storage.
Since we have more storage, we can count on groups of bits. Specifically, we can count the
number of IP addresses in the file that begin with 0,L,2, . . . ,216 - 1 using an array of 216 integers that
can be represented with 32 bits. For every IP address in the file, we take its 16 MSBs to index into
this array and increment the count of that number. Since the file contains fewer than 232 numbers,
there must be one entry in the array that is less than 216, This tells us that there is at least one IP
address which has those upper bits and is not in the file. In the second pass, we can focus only on
the addresses whose leading 16 bits match the one we have found, and use a bit array of size 216 to
identify a missing address.
def find-missing-element (stream) :
NUII-BUCKET=1<<16
counter = [0] * NU]I-BUCKET
stream, stream-copy = itertools, tee(strean)
for x in stream:
uPper-Part-x=x>>16
counterIupper-part-x] += 1
# Look for a bucket that contains less than (1 << 16) elements
BUCKET-CAPACITY = 1 << 16
candidate-bucket = next(i for i, c in enunerate(counter)
if c < BUCKET-CAPACITY)
# Finds a77 IP addresses in the st.ream rrrhose first 
16 bits are equal to
# candidate-bucket.
candidates = [0] o BUCKET-CAPACITY
stream = stream_copy
for x in stream-copy:
upper-Part-x=x>>16
if candidate-bucket == upper-part-x:
# Records the presence of 16 ISB of x.
lower_part_x = ((1 << 16) - 1) & x
candidatesIlower-part-x] = 1
# At Teast one of the LSB conbinations is absent , find it
for i, v in enunerate(candidates):
if v == 0:
return (candidate-bucket << 16) I i
The storage requirement is dominated by the count array, i.e.,276 integer entries.
156
```
