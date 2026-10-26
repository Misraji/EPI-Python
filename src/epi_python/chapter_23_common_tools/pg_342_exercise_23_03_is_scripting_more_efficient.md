# Exercise 23.3: Is scripting more efficient?

**Printed textbook page:** 342. **Reference transcription pages:** 342–342.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 342 (PDF page 356)

```text
Solution: Version control systems such as git and SVN allow users to define actions to take around
events such as commits, locking and unlocking files, and altering revision properties. These actions
are specified as executable programs known as hook scripts. When the version control system gets
to these events, it will check for the existence of a corresponding hook script, and execute it if it
exists.
Hook scripts have access to the action as it is taking place, and are passed corresponding
command-line arguments. For example, the pre-commit hook is passed the repository path and the
transaction ID for the currently executing commit. If a hook script refurns a nonzero exit code, the
version control system aborts the action, refurning the script's standard error output to the user.
The following hook scripts are used most often:
o pre-commif: Executed before a change is committed to the repository. Often used to check log
messages, to format files, run a test suite, and to perform custom security or policy checking.
o post-commlf: Executed once the commit has completed. Often used to inform users about a
completed commit, for example by sending an email to the team, or update the bug tracking
system.
As a rule, hooks should never alter the content of the transaction. At the very least, it can surprise
a new developer; in the worst-case, the change can result in buggy code.
Scripting languages
Scripting languages, such as AWK, Perl, and Python were originally developed as tools for quick
hacks, rapid prototyping, and gluing together other programs. They have evolved into mainstream
programming languages. Some of their characteristics are as follows.
r Text strings are the basic (sometimes only) data type.
o Associative affays are a basic aggregate type.
o Regexps are usually built in.
o Programs are interpreted rather than compiled.
o Declarations are often not required.
They are easy to get started with, and can often do a great deal with very little code.
23,3 Is scnrruNc lronn nrrrcrrNr?
Your manager read a study in which a Python program was found to have taken one-tenth the
development time then a program written in C++ for the same application, and now demands that
you immediately program exclusively in Python. Tell him about five dangers of doing this.
Solution: First, any case study is entirely anecdotal. It's affected by the proficiency of the developers,
the nature of the program being written, etc. So no case study alone is sufficient as the basis for a
language choice.
Second, switching development environments for any team is an immediate slowdown, since
the developers must learn all the new hicks and unlearn all the old ones. If a team wants to make
this kind of switch, it needs to have a very long runway.
Third, scripting languages are simply not good for some tasks. For example, many high-
performance computing or systems tasks should not be done in Python. The lack of a type system
means some serious bugs can go undetected.
Fourth, choosing to program entirely in any language is a risky endeavor. Any decent engineer-
ing department should be willing to adopt the best tool for the job at hand.
Finally, Python itself may be a risky choice at this point in time, since there is an ongoing shift
from the 2.x branch to 3.x. If you choose to work in2.x, you likely have a massive refactor into 3.x
342
```
