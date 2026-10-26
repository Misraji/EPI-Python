# Exercise 21.9: Exception Handling

**Printed textbook page:** 326. **Reference transcription pages:** 326–327.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 326 (PDF page 340)

```text
top-k-scores = {}
for key in all-scores:
sorted-scores = sorted(all-scoresIkey])
top-k-scoresIkey] = []
for i in range(k):
top-k-scores Ikey] . append(sorted-scores [Ien(sorted-scores) - 1 - i] )
result = {}
for key in top-k-score's:
total = 0
for score in top-k-scores[key]:
total += score
mean=total/k
variance = 0
for score in top-k-scores[key]:
variance = variance + (score
resultIkey] = variance
mean) * (score - mean)
return result
Solution: The functions zipO, fturctools.reduceO, heapq.nlargest.O, and sumO, directly re-
place boilerplate loops. The coltections . defaultdict container and dictionary comPrehension
remove the need for explicit initialization.
def compute-top-k-variance(students, scores, k)
aIl-scores = collections. defaultdict (1ist)
for student, score in zip(students, scores)
a1I-scores Istudent] . append(score)
top-k-scores = {
student: heapq.nlargest(k, scores)
for student, scores in aIl-scores.itemsO if len(scores) >= k
)
return {
student : functools, reduce(
lanbda variance, score: variance + (score - mean)*o2,
for student, scores, mean in (
(student, scores, sun(scores) / k)
for student, scores in top-k-scores.itemsO)
I
scores, 0)
21,.9 Excrp,rIox HeuoltNc
Briefly describe exception handling in Python, paying special attention to the roles played by try,
except, eIse, finally, and raise. Rewrite the following program using excePtions to make it
more robust.
def get-col-surn(filename, col) :
# l{ay raise loError.
csv-file = open(filename)
csv-reader = csv, reader(csv-file)
326
```

#### Printed page 327 (PDF page 341)

```text
running-sum = 0
for row in csv-reader:
value = rowIcol]
running-sum += int(value)
csv-file . close o
print("Sum - " + str(running-sum))
Solution: A statement or expression it may result in an error when an attempt is made to execute
it. Such errors are called exceptions. They do not always entail exiting the program. For example,
if a user enters a filename, and no corresponding file is found, or the user does not have read
permissions, the user can be prompted again. Such checks can be made using a try block.
The try block can be followed by an except block, a finally block, or an except block followed
by a finally block or an except block followed by an else block followed by a finatty block.
If a finally block exists, it is always executed, regardless of whether an exception was raised
and/or caught. Here is an example. Note that there is no except block-any exception raised in the
try block is propagated up.
def get-value (filename , key) :
handle = open(filename)
try:
file_contents = handle . read o
js-text = json. loads(fiIe_contents)
return js_textIkey]
finally:
# Ptevent resource Teak if there js an errot parsing.file_contents,
handle . close o
The code below shows basic trylexcept usage. Note the duplicated code used to avoid the
resource leak.
def get_value (filename , key) :
handl,e = open(filename)
try:
file_contents = handle.reado
js-text = json. loads (file_contents)
handle. close o
return (True , j s_text tkeyl )
ercept ValueError:
handle . close o
return (Fa1se, )
The duplicated code can be avoided by using trylexcept/finatly
def get-value (filename , key) :
handle = open(filename)
try:
file_contents = handle . read o
js_text = json. loads (file_contents)
return (True , j s_text tkeyl )
ercept ValueError:
return (False, )
finally:
handle. close o
327
```
