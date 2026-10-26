# Exercise 21.8: Python code

**Printed textbook page:** 325. **Reference transcription pages:** 325–325.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 325 (PDF page 339)

```text
def foo (u, v , *args , **kwargs) :
print('u,v ='+ 
str((u, v)))
for i in range(1en(ar9s)):
print('args {0} = {1}'.fornat(str(i), 
str(argslil)))
for (keyword , value) in kwargs, items O :
print('keyword,value = ' + str((keyword, value)))
foo(1, 'eu1er' , 2.7L, t6, 281, name='cfg', rank=1)
# Alternate ca77
args = (2.7L, [6, 28])
kwargs = {'name': 'cfg', 'rank': 1}
foo(1, 'euler' , *args , **kwargs)
Some points:
o It's not important that the parameter referenced in the function be called args-it could iust
as well be called D or argdict;
o it is important is the ** be specified;
o the ** argument must appear after all the regular named parameters and the * argument (if
any);
o ** can be used at the call site too; and
o keyword arguments are quite different from named arguments, wherein the names of the
arguments are specified in the function itself.
21.8 Pyrnox coon
Rewrite the following prcgram using a Pythonic style.
def compute-top-k_variance(students, scores, k)
students and scores are equaT length lists of strjngs and fToats,
respectiveTy. The function computes for each string that appears at least
k tines in the Jist the variance of the top k scores that correspond to it
Strings that appear fewer than k tirnes are not considered.
counts = {}
for i in range(1en(students)):
if students[i] not in counts
countsIstudentsti]l = i
else:
countsIstudentsti]l += f
all_scores = {}
for key in counts:
if counts[key] >= k:
all-scoresIkey] = 11
for i in range(Ien(students)):
if studentstil in all_scores:
all_scores I students Ii ] I, append ( scores Ii ] )
325
```
