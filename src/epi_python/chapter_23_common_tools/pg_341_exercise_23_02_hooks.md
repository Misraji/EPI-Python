# Exercise 23.2: Hooks

**Printed textbook page:** 341. **Reference transcription pages:** 341–341.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 341 (PDF page 355)

```text
merging rePorts no conflicts: the merged program compiles without any trouble. However the
behavior is not what was expected.
Both slmtactic merging and semantic merging greatly increase runtimes, and are very limiting
since they are tightly coupled to specific programming languages. In practice, line-based merging
is used in conjunction with a small set of unit tests (a "smoke suite") invoked with a pre-commit
hook script. Compilation finds syntax and static semantics errors, and the tests (hopefully) identify
deeper semantic issues.
Flgure 23.1 : An example of a 3-way line based merge.
23.2 Hoors
What are hooks in a version control system? Describe their applications.
341.
int sm(int n) {
int total = 0;
for (int i = 0; i < n; i++) {
total = total + i;
l
return total;
l;
Version 1
void sun(int n, int* result) {
int total = 0;
for (int i = 0; i < n; i++) {
total = total + i;
)*result = total;
);
Version l-a
int sun(int n) {
if(n<0){
returr 0;
lint total = 0;
for (int i = 0; i < n; i++) t
total += i;
)
retunr total;
);
Version Lb
int r = sm(10);
void sun(int n, int* resuLt) {
if(n<0)t
return 0;
)int total = 0;
for (int i = 0; i < n; i++) {
total=total+i;
)*result = totali
);
Merge of Versions l-a and 1b
int r = sm(10);
```
