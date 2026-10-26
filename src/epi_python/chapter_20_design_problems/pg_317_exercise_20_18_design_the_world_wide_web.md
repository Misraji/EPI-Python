# Exercise 20.18: Design the World Wide Web

**Printed textbook page:** 317. **Reference transcription pages:** 317–317.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 317 (PDF page 331)

```text
Solution: Assume that the bandwidth from the lab machine is a limiting factor. It is reasonable to
first do trivial optimizations, such as combining the articles into a single file and compressing this
file.
Opening 1000 connections from the lab server to the 1000 machines in the data center and trans-
ferring the latest news articles is not feasible since the total data transferred will be approximately
100 gigabytes (without compression).
Since the bandwidth between machines in a data center is very high, we can copy the file from
the lab machine to a single machine in the data center and have the machines in the data center
complete the copy. Instead of having just one machine serve the file to the remainngggg machines,
we can have each machine that has received the file initiate copies to the machines that have not yet
received the file. In theory, this leads to an exponential reduction in the time taken to do the copy.
Several additional issues have to be dealt with. Should a machine initiate further copies before
it has received the entire file? (This is tricky because of link or server failures.) How should the
knowledge of machines which do not yet have copies of the file be shared? (There can be a central
repository or servers can simply check others by random selection.) If the bandwidth between
machines in a data center is not a constant, how should the selections be made? (Servers close to
each other, e.9., in the same rack, should prefer communicating with each other.)
Finally, it should be mentioned that there are open source solutions to this problem, e.g., Unison
and BitTorrent, which would be a good place to start.
20.18 DssrcN tnr Wonrn Wrnr Wnn
Design the World Wide Web. Specifically, describe what happens when you enter a URL in a
browser address bar, and press retum.
Hint: Follow the flow of information.
Solution: At the network level, the browser extracts the domain n.une component of the URL, and
determines the IP address of the serve\ e.g.t through a call to a Domain Name Server (DNS), or a
cache lookup. It then communicates using the HTTP protocol with the server. HTIP itself is built
on top of TCPAR which is responsible for routing, reassembling, and resending packets, as well as
controlling the transmission rate.
The server determines what the client is asking for by looking at the portion of the URL that
comes after the domain name, and possibly also the body of the HTTP request. The request may
be for something as simple a file, which is returned by the webserver; HTTP spells out a format by
which the type of the returned file is specified. For example, the URL http://go,com/imgs/abc.png may
encode a request for the file whose hierarchical name is imgs/abc.png relative to a base directory
specified at configuration to the web server.
The URL may also encode a request to a service provided by the web server. For example,
http://go.com/lookup/flight?num=UA37,city=AUS is a request to the lookup/flight service, with an argu-
ment consisting of two attribute-value pair. The service could be implemented in many ways, e.g.t
Java code within the servel, or a Common Gateway Interface (CGI) script written in Perl. The
service generates a HTTP response, typically HTML, which is then retumed to the browser. This
response could encode data which is used by scripts running in the browser. Common data formats
include |SON and XML.
317
```
