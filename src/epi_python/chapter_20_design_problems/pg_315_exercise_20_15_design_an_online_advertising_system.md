# Exercise 20.15: Design an online advertising system

**Printed textbook page:** 315. **Reference transcription pages:** 315–315.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 315 (PDF page 329)

```text
20.15 Drsrcu AN oNLTNE ADvERTTsTNG sysrEM
fingle, a search engine startup, has been very successful at providing a high-quality Internet search
service. A large number of customers have approached Jingle and asked it to display paid adver-
tisements for their products and services alongside search results.
Design an advertising system for ]ingle.
Hizf: Consider the stakeholders separately.
Solution: Reasonable goals for such a system include
o providing users with the most relevant ads,
o providing advertisers the best possible retum on their investment, and
o minimizing the cost and maximizing the revenue to Jingle.
TWo key components for such a system are:
o The front-facing component, which advertisers use to create advertisements, organize ciun-
PaiSns, limit when and where ads are shown, set budgets, and create performance reports.
o The ad-serving system, which selects which ads to show on the searches.
The front-facing system can be a fairly conventional web application, i.e., a set of web pages,
middleware that responds to user requests, and a database. Key features include:
o LJser authentication-a way for users to create accounts and authenticate themselves. Alter-
natively, use an existing single sign-on login service, e.g., Facebook or Google.
o User input-a set of form elements to let advertisers specify ads, advertising budget, and
search keywords to bid on.
o Performance reports-a way to generate reports on how the advertiser's money is being spent.
o Customer s€rvicmven the best of automated systems require occasional human interaction,
e.g'l ways to override limits on keywords. This requires an interface for advertisers to contact
customer service representatives, and an interface for those representatives to interact with
the system.
The whole front-end system can be built using, for example, HyperText Markup Language
(HTML) and |avaScript. A commonly used approach is to use a LAMP stack on the server-side:
Linux as the OS, Apache as the HTTP seryer, MySQf as the database software, and PHP for the
application logic.
The ad-serving system is less conventional. The ad-serving system would build a specialized
data structure, such as a decision tree, from the ads database. It chooses ads from the database
of ads based on their "relevance" to the search. Lr addition to keywords, the ad-serving systems
can use knowledge of the user's search history, how much the advertiser is willing to pay, the time
of day, user locale, and type of browser. Ma.y strategies can be envisioned here for estimating
relevance, such as, using information retrieval or machine leaming techniques that learn from past
user interactions.
The ads could be added to the search results by embedding lavaScript in the results page. This
Javaftript pulls in the ads from the ad-serving system directly. This helps isolate the latency of
serving search results from the latency of serving ad results.
There are many more issues in such a system: making sure there are no inappropriate images
using an image recognition API; using a link verification to check if keywords really corresponds to
a real site; serving up images from a content-delivery network; and having a fallback advertisement
to show if an advertisement cannot be found.
315
```
