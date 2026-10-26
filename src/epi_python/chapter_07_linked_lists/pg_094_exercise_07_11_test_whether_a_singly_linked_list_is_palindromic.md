# Exercise 7.11: Test whether a singly linked list is palindromic

**Printed textbook page:** 94. **Reference transcription pages:** 94–94.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 94 (PDF page 108)

```text
def even-odd-merge (L)
if not L:
return L
even-dummy-head, odd-dummy-head = ListNode(0), ListNode(0)
tails, 
turn = [even-dummy-head, odd-dummy-head], 0
while L:
tails Iturn] . next = L
L = L. next
tails Iturn] = tails Iturn] . next
turn ^= L # Alternate betreen even and odd.
tails [1] . next = ilone
tails [0] . next = odd-dummy-head. next
return even-dummy-head. next
The time complexity is O(n) and the space complexity is O(1)
7.11 Trsr wnrrHsR A srNGLy LINKED LIST IS pALINDRoMIC
It is straightforward to check whether the sequence stored in an array is a palindrome. Floweve4
if this sequence is stored as a singly linked list, the problem of detecting palindromicity becomes
more challenging. See Figure 7.1. on Page 82 for an example of a palindromic singly linked list.
Write a program that tests whether a singly linked list is palindromic.
Hint: lt's easy if you can traverse the list forwards and backwards simultaneously.
Solution: A brute-force algorithm is to compare the first and last nodes, then the second and
second-to-last nodes, etc. The time complexity is O(n2), where n is the number of nodes in the list.
The space complexity is O(1).
The O(nz) complexity comes from having to repeatedly traverse the list to identify the last,
second-to-last, etc. Getting the first node in a singly linked list is an O(1) time operation. This
suggests paying a one-time cost of O(n) tirne complexity to get the reverse of the second half of the
original list, after which testing paLindromicity of the original list reduces to testing if the first half
and the reversed second half are equal. This approach changes the list passed in, but the reversed
sublist can be reversed again to restore the original list.
def is-linked-li 
st-a-palindrone (L) :
# Finds the second half of L.
slow=fast=L
rhile fast and fast.next:
fast , slow = fast, next. next , slow. next
# Conpares the first 
haTf and the reversed second half -lists.
first-half-iter, 
second-half-iter = L, reverse-linked-list(slow)
rhile second-half-iter and first-half-iter:
if second-half-iter.data != first-ha1f-iter.data:
return False
second_half-iter , first_half-iter 
= (second-half-iter. next ,
first-half-iter 
. next)
return True
The time complexity is O(n). The space complexity is O(1).
94
```
