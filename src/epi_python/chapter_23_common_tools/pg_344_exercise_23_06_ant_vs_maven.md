# Exercise 23.6: ANT vs Maven

**Printed textbook page:** 344. **Reference transcription pages:** 344–344.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 344 (PDF page 358)

```text
One solution to this is as follows. During the reconstruction of a component A, a component
called Anew is created and compared with the existing A. If Ansv/ and A are different, AngM/ is
copied to A. Otherwise, A remains unchanged, include the date that it was changed.
This may not always be the reasonable thing to do. For example, even if the source files
remain unchanged, environmental differences or changes to the compilation process may lead to
the creation of different intermediate targets, which would necessitate a full rebuild. Therefore each
intermediate target must be rebuilt in order to compare against the existing components, but it's
indeterminate before construction whether the new objects will be used or not.
23.6 ANT vs. MevtN
Contrast ANT and Maven
Solution: Historically, ANT was developed in the early days of Java to overcome the limitations
of Make. It has tasks as a "primitive"-in Make these must be emulated using pseudo-targets,
variables, etc. ANT is cross-platform-since Make largely scripts what you would do at the
command-line, a Makefile written for Unix-like platforms will not work out-of-the-box on, say/
Windows.
ANT itself has a number of shortcomings. These are overcome in Maven, as described below
o Maven is declarative whereas Ant is imperative in nature. You tell Maven what are the
dependencies of your project-Maven will fetch those dependencies and build the artifact for
you, e.g., a war file. In Ant, you have to provide all the dependencies of your project and tell
Ant where to copy those dependencies.
o With Maven, you can use "archetypes" to set up your project very quickly. For example you
can quickly set up a Java Enterprise Edition project and get to coding in a matter of minutes.
Maven knows what should be the project structure for this type of project and it will set it up
for you.
o Maven is excellent at dependency management. Maven automatically retrieves dependencies
for your project. It will also retrieve any dependencies of dependencies. You never have to
worry about providing the dependent libraries. ]ust declare what library and version you
want and Maven will get it for you.
o Maven has the concept of snapshot builds and release builds. During active development
your project is built as a snapshot build. When you are ready to deploy the project, Maven will
build a release version for you which can be put into a company wide Nexus repository. This
way, all your release builds are in one repository that are accessible throughout the company.
o Maven favors convention over configuration. In Ant, you have to declare a bunch of properties
before you can get to work. Maven uses sensible defaults and if you follow the Maven
recommended project layout, your build file is very small and everything works out of the
box.
r Maven has very good support for running automated tests. ln fact, Maven will run your tests
as part of the build process by default. You do not have to do anything special.
o Maven provides hooks at different phases of the build and you can perform additional tasks
as per your needs
Database
Most software systems today interact with databases, and it's important for developers to have
basic knowledge of databases.
3M
```
