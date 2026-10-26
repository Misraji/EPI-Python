# Exercise 20.6: Design TeX

**Printed textbook page:** 307. **Reference transcription pages:** 307–307.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 307 (PDF page 321)

```text
20.6 Dusrcr.r TBI
The Tp[ system for typesetting beautiful documents was designed by Don Knuth. Unlike GUI
based document editing programs, Tp[ relies on a markup language, which is compiled into a
device independent intermediate representation. Tp[ formats text, lists, tables, and embedded
figures; supports avery rich set of fonts and mathematical symbols; automates section numbering,
cross-referencing, index generation; exports an API; and much more.
How would you implement Tp[?
Hint: There are two aspects--$uilding blocks (e.g., fonts, symbols) and hierarchical layout.
Solution: Note that the problem does not ask for the design of Tg[, which itself is a complex
problem involving feature selection, and language design. There are a number of issues corunon
to implementing any such program: programming language selection, lexing and parsing input,
error handling, macros, and scripting.
Two key implementation issues specific to Tp[ are a specifying fonts and symbols (e.g., A,b, f,
L, f ,r),and assembling a document out of components.
Focusing on the second aspect, a reasonable abstraction is to use a rectangular bounding box to
describe components. The description is hierarchical: each individual symbol is a rectangle, lines
and paragraphs are made out of these rectangles and are themselves rectangles, as are section titles,
tables and table entries, and included images. A key algorithmic problem is to assemble these
rectangles, while preserving hard constraints on layout, and soft constraints on aesthetics. See also
Problem 16.11 on Page 254 for an example of the latter.
Tuming our attention to symbol specification, the obvious approach is to use a 2D arcay of
bits to represent each symbol. This is referred to as a bit-mapped representation. The problem
with bit-mapped fonts is that the resolution required to achieve acceptable quality is very high,
which leads to huge documents and font-libraries. Different sizes of the same symbol need to be
individually mapped, as do italicized and bold-face versions.
A better approach is to define symbols using mathematical functions. A reasonable approach is
to use a language that supports quadratic and cubic functions, and elementary graphics transforma-
tions (rotation, interpolation, and scaling). This approach overcomes the limitations of bit-mapped
fonts-parameters such as aspect ratio, font slant, stroke width, serif size, etc. can be programmed.
Other implementation issues include enabling cross-referencing, automatically creating indices,
supporting colors, and outputting standard page description formats (e.g., pDF)).
Donald Knuth's book"DigitalTypography" describes in great detail the design and implementa-
tion of Tp{.
20,7 DrsrcN A sEARcH ENGTNE
Keyword-based search engines maintain a collection of several billion documents. One of the
key computations performed by a search engine is to retrieve all the documents that contain the
keywords contained in a query. This is a nontrivial task in part because it must be performed in a
few tens of milliseconds.
Here we consider a smaller version of the problem where the collection of documents can fit
within the RAM of a single computer.
307
```
