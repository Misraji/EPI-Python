# Exercise 23.1: Merging in a version control system

**Printed textbook page:** 339. **Reference transcription pages:** 339–340.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 339 (PDF page 353)

```text
CHapten
Common Tools
UNIX is a gmeral-purpwe, multi-user, interactioe operating sys-
tem for the Digital Equipmmt Corporation PDP-11/40 and 11/45
computers. lt ffirs a number of features seldom found eam in
larger operating systefls, including: (1) a hierarchical file system
incorporating demountable aolumes; Q) compatible file, deuice,
and inter-process AO; G) the ability to initiate asynchronous pro-
cesses; (4) system command lnnguage selectable on a per-user
basis; and (5) ooer 100 subsystems including a dozen languages.
- 
"The UNIX TimeSharing System,"
D. Rncslr aNo K. Tnoupsor.t,1974
The problems in this chapter are concerned with tools: version control systems, scripting lan-
Suages, build systems, databases, and the networking stack. Such problems are not commonly
asked----expect them only if you are interviewing for a specialized role, or if you claim specialized
knowledge, e.9., network security or databases. We emphasize these are vast subjects, e.g., net-
working is taught as a sequence of courses in a university curriculum. Our goal here is to give
you a flavor of what you might encounter. Adnan's Advanced Programming Tools course mate-
rial, available freely online, contains lecture notes, homeworks, and labs that may serve as a good
resource on the material in this chapter.
Version control
Version control systems are a cornerstone of software development--every developer should un-
derstand how to use them in an optimal way.
23.1, Mrncrxc rN A vERSroN coNTRoL sysrEM
What is merging in a version control system? Specifically, describe the limitations of line-based
merging and ways in which they can be overcome.
Solution:
Modem version control systems allow developers to work concurrently on a personal copy of
the enfue codebase. This allows software developers to work independently. The price for this
merging: periodically, the personal copies need to be integrated to create a new shared version.
There is the possibility that parallel changes are conflicting, and these must be resolved during the
merge.
By far, the most common approach to merging is text-based. Text-based merge tools view
software as text. Line-based merging is a kind of text-based merging, specifically one in which each
line is treated as an indivisible unit. The merging is "three-way": the lowest corunon ancestor in
the revision history is used in conjurction with the two versions. With line-based merging of text
files, common text lines can be detected in parallel modifications, as well as text lines that have been
339
```

#### Printed page 340 (PDF page 354)

```text
inserted, deleted, modified, or moved. Figure 23.1 on the facing page shows an example of such a
line-based merge.
One issue with line-based merging is that it cannot handle two parallel modifications to the
same line: the two modifications cannot be combined, only one of the two modifications must
be selected. A bigger issue is that a line-based merge may succeed, but the resulting program is
broken because of syntactic or semantic conflicts. In the scenario in Figure 23.1 on the next page
the changes made by the two developers are made to independent lines, so the line-based merge
shows no conflicts. However, the program will not compile because a function is called incorrectly.
In spite of this, line-based merging is widely used because of its efficiency, scalability,and
accuracy. A three-way, line-based merge tool in practice will merge 90"/" of the changed files
without any issues. The challenge is to automate the remainingl0% of the situations that cannot
be merged automatically.
Text-based merging fails because it does not consider any syntactic or semantic information.
Syntactic merging takes the syntax of the programming language into account. Text-based merge
often yields unimportant conflicts such as a code comment that has been changed by different
developers or conflicts caused by code reformatting. A syntactic merge can ignore all these: it
displays a merge conflict when the merged result is not syntactically correct'
We illustrate syntactic merging with a small example:
if (n%2 == 0) then m = n/2;
TWo developers change this code in a diffurent ways, but with the same overall effect. The first
updatesit to
if (n%2 == 0) then n = n/2 else m = (n-L) /2;
and the second developer's update is
m = n/2;
Both changes to the same thing. However, a textual-merge will likely result in
which is slmtactically incorrect. Syntactic merge identifies the conflicU it is the integtator's resPon-
sibility to manually resolve rt, e.9., by removing the else portion.
Syntactic merge tools are unable to detect some frequently occurring conflicts. For example, in
the merge of Versions 'l-a and lb in Figure 23.1 on the facing page will not compile, since the call to
sum(10) has the wrong signature. Syntactic merge will not detect this conflict since the program is
still syntactically correct. The conflict is a semantic conflict, specifically, a static semantic conflict,
since it is detectable at compile-time. (The compile will retum something like "function argument
mismatch error".)
Technically, syntactic merge algorithms operate on the parse trees of the programs to be merged.
More powerful static semantic merge algorithms have been proposed that operate on a graph
representation of the progrEuns, wherein definitions and usage are linked, making it easier to
identify mismatched usage.
Static semantic merging also has shortcomings. For example, suppose Point is a class rep-
resenting 2D-points using Cartesian coordinates, and that this class has a distance function that
returns $i7 
Suppose Alice checks out the project, and subclasses Point to create a class that
supports polar coordinates, and uses Points's distance function to retum the radius. Concurrently,
Bob checks out the project and changes Point's distance function to retum lrl + lyl. Static semantic
340
```
