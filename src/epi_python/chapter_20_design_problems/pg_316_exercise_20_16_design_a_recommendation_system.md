# Exercise 20.16: Design a recommendation system

**Printed textbook page:** 316. **Reference transcription pages:** 316–316.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 316 (PDF page 330)

```text
20.1,6 Dnsrcn A RECoMMENDATIoN SYSTEM
]ingle wants to generate more page views on its news site. A product manager has the idea to add
to each article a sidebar of clickable snippets from articles that are likely to be of interest to someone
reading the current article.
Design a system that automatically generates a sidebar of related articles'
Hint: This problem can be solved with various degrees of algorithmic sophistication: none at all, simple
frequency analysis, or machine leaming.
Solution: The key technical challenge in this problem is to come up with the list of articles-the
code for adding these to a sidebar is trivial.
One suggestion might be to add articles that have proved to be popular recently. Another is to
have links to recent news articles. A human reader at ]ingle could tag articles which he believes to
be significant. He could also add tags such as finance, sports, and politics, to the articles. These
tags could also come from the HTML meta-tags or the page title,
We could also provide randomly selected articles to a random subset of readers and see how
popular these articles prove to be. The popular articles could then be shown more frequently.
On a more sophisticated level, Jingle could use automatic textual analysis, where a similarity is
defined between pairs of articles-this similarity is a real number and measures how many words
are common to the two. Several issues come up, such as the fact that frequently occurring words
such as "for" arrd "the" should be ignored and that having rare words such as "arbltrage" at:td
"diesel" in common is more significant than having say, "sale" and "international"'
Textual analysis has problems, such as the fact that two words may have the same spelling
but completely different meanings (anti-virus means diffurent things in the context of articles on
acquired immune deficiency symdrome (AIDS) and computer security). One way to augment
textual analysis is to use collaborative filtering-using information gleaned from many users. For
example, by examining cookies and timestamps in the web server's log files, we cEIn tell what
articles individual users have read. If we see many users have read both A and B in a single session/
we might want to recommend B to anyone reading A. For collaborative filtering to work, we need
to have many users.
20.17 Drsrclt AN opTIMIZED wAy oF DISTRIBUTING LARGE FILEs
Jingle is developing a search feature for breaking news. New articles are collected from a variety
of online news sources such as newspapers, bulletin boards, and blogs, by a single lab machine at
|ingle. Every minute, roughly one thousand articles are posted and each article is 100 kilobytes.
Jingle would like to serve these articles from a data center consisting of a 1000 servers. For
performance reasons, each server should have its own copy of articles that were recently added.
The data center is far away from the lab machine.
Design an efficient way of copying one thousand files each 1@ kilobytes in size from a single lab
server to each of 1000 servers in a distant data center.
Hint: Explolt the data center.
31.6
```
