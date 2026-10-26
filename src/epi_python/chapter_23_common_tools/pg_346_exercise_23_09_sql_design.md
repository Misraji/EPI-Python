# Exercise 23.9: SQL design

**Printed textbook page:** 346. **Reference transcription pages:** 346–346.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 346 (PDF page 360)

```text
23.9 SQL prsrcN
Write SQL commands to create a table appropriate for representing students as well as SQL com-
mands that illustrate how to add, delete, and update students, as well as search for students by
GPA with results sorted by GPA.
Then add a table of faculty advisors, and describe how to model adding an advisor to each
student. Write a SQL query that retums the students who have an advisor with a specific n€une.
Solution: Natural fields for a student are name, birthday, GPA, and graduating year. In addition,
we would like a unique key to serve as an identifier. A SQL statement to create a student table would
looklikethefollowing:CREATE TABLE students (id INT AUTO-INCREMENT, name VARCHAR(30),
birthday DATE, gpa FLOAT, graduate-year INT, PRII{ARY KEY(id));. Here are examples of
SQL statements for updating the students table.
o Add a student
- INSERT INTO students(name, birthday, gpa, graduate-year) VALUES ('Cantor',
'1997-10-22" 3.9, 2009);
o Delete students who graduated before 1985.
- DELETE FRoM students WIIERE graduate-year < 1985;
o Update the GPA and graduating year of the student with id 28 to 3.14 and 2015, respectively.
- UPDATE students SET gpa = 3.14, graduate-year - 2015 WHERE id = 28;
The following query retums sflrdents with a GPA greater than 3.5, sorted by GPA. It includes each
student'sname,GPA,andgraduatingyear. 
SELECT gpa, name, graduate*year FR0lt students
WHERE gpa > 3.5 ORDER BY gpa DESC;
Now we tum to the second part of the problem. Here is a sample table for faculty advisers.
id name
1 Church
2 Thrski
title
Dean
Professor
We add a new column advisor-id to the students table. This is the foreign key on the
previous page. As an example, here's how to retum students with GPA whose advisor is
Church: SELECT s.name, s.gp? FROI{ students s, advisors p WHERE s.advisor-i6 = p.id
AND p.name = 'Church';.
Variant: \,l/hat is a SQL join? Suppose you have a table of courses and a table of students. How
might a SQL join arise naturally in such a database?
Networking
Most software systems today interact with the network, and it's important for developers even
higher up the stack to have basic knowledge of networking. Here are networking questions you
may encounter in an interview setting.
23.10 IP, TCP, aNo HTTP
Explain what IR TCP, and HTTP are. Emphasize the differences between them.
Solution: IP, TCR and HTTP are networking protocols-they help move informationbetween two
hosts on a network.
IR the Internet Protocol, is the lowest-level protocol of the three. It is independent of the
physical channel (unlike for example, WiFi or wired Ethemet). Its primary focus is on getting
u6
```
