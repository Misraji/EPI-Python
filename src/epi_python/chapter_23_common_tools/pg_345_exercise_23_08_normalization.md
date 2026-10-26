# Exercise 23.8: Normalization

**Printed textbook page:** 345. **Reference transcription pages:** 345–345.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 345 (PDF page 359)

```text
23.7 SQL vs. NoSQL
Contrast SQL and NoSQL databases.
Solution: A relational database is a set of tables (also known as relations). Each table consists of
rows. A row is a set of columns (also known as fields or attributes), which could be of various types
(integer, float, date, fixed-size string, variable-size string, etc.). SQL is the language used to create
and manipulate such databases. MySQL is a popular relational database.
A NoSQL database provides a mechanism for storage and retrieval of data which is modeled
by means other than the tabular relations used in relational databases. MongoDB is a popular
NoSQL database. The analog of a table in MongoDB is a collection, which consists of documents.
Collections do not enforce a schema. Documents can be viewed as hash maps from fields to values.
Documents within a collection can have different fields.
A key benefit of NoSQL databases is simplicity of design: a field can trivially be added to new
documents in a collection without this affecting documents already in the database. This makes
NoSQL a popular choice for startups which have an agile development environment.
The data structures used by NoSQL databases, e.g., key-value pairs in MongoDB, are different
from those used by default in relational databases, making some operations faster in NoSQL.
NoSQL databases are typically much simpler to scale horizontally, i.e., to spread documents from
a collection across a cluster of machines.
A key benefit of relational databases include support for ACID transactions. ACID (Atomicity,
Consistency, Isolatiory Durability) is a set of properties that guarantee that database transactions
are Processed reliably. For example, there is no way in MongoDB to remove an item from inventory
and add it to a customer's order as an atomic operation.
Another benefit of relational database is that their query language, SQL, is declarative, and
relatively simple. In contrast, complex queries in a NoSQL database have to be implemented pro-
grammatically. (It's often the case that the NoSQL database will have some support for translating
SQL into the equivalent NoSQL program.)
23.8 Nonuer,rzerroN
What is database normalization? \A/hat are its advantages and disadvantages?
Solution: Database normalization is the process of organizing the columns and tables of a relational
database to minimize data redundancy. Specifically, normalization involves decomposing a table
into less redundant tables without losing information, thereby enforcing integrity and saving space.
The central idea is the use of "foreign keys". A foreign key is a field (or collection of fields)
in one table that uniquely identifies a row of another table. Lr simpler words, the foreign key is
defined in a second table, but it refers to the unique key in the first table. For example, a table called
Employee may use a unique key called employee-id. Another table called Employee Details has
a foreign key which references employee-id in order to uniquely identify the relationship between
both the tables. The objective is to isolate data so that additions, deletions, and modifications of an
attribute can be made in just one table and then propagated through the rest of the database using
the defined foreign keys.
The primary drawback of normalization is performance-often, a large number of joins are
required to recover the records the application needs to function.
345
```
