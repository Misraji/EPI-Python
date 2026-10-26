# Chapter 4: Primitive Types

**Starts at printed page 23.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 23

```text
CHaprrn
Primitive Tpes
Representation is the essence ofprogramming
- 
" The Mythiul Man Month,"
F. P. Bnooxs, 1975
A program updates variables in memory according to its instructions. Variables come in types-a
type is a classification of data that spells out possible values for that type and the operations that
can be performed on it. A type can be provided by the language or defined by the programmer. In
Python everything is an object-this includes Booleans, integers, characters, etc.
Prtmiilae types boot camp
Writing a program to count the number of bits that are set to 1 in a positive integer is a good way to
get up to speed with primitive types. The following program tests bits one-at-a-time starting with
the least-significant bit. It illustrates shifting and masking; it also shows how to avoid hard-coding
the size of the integer word.
def count-bits (x) :
num-bits = 0
rhile x:
num-bits+=x&1
x>>=1
return num-bits
Since we perform O(1) computation per bit, the time complexity is O(n),whercn is the number of
bits needed to represent the integer, e.g., 4 bits are needed to represent 12, which is (1100)z in binary.
The techniques in Solution 4.L on the next page, which is concemed with cotrnting the number of
bits mod 2, i.e., the paity, can be used to improve the performance of the program given above.
Know your primitioe types
Python has a number of built-in types: numerics (e.g., integer), sequences (e.g., list), mappings (e.g.,
dict), as well as classes, instances and exceptions. All instances of these types are objects.
Integers in Python3 are unbounded-the maximum integer representable is a fr:nction of the
available memory. The constant sys.maxsize can be used to find the word-size; specifically, it's
the maximum value integer that can be stored in the word, e.g., 2**63 - L on a 64-bit machine.
Bounds on floats are specified in sys. float-info.
o Be very familiar with the bit-wise operators such as 6&4,11 Z, B>>L, -L6>>2, 1<<10, -0, 15^x.
Negative numbers are treated as their 2's complement value. (There is no concept of an
unsigned shift in Python, since integers have infinite precision.)
23
```
