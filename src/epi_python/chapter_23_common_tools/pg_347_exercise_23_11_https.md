# Exercise 23.11: HTTPS

**Printed textbook page:** 347. **Reference transcription pages:** 347–347.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 347 (PDF page 361)

```text
individual packets from one host to another, Each IP packet has a header that includes the source
and destination IP address, the length of the packet, the type of the protocol it's layering (TCP and
UDP are common), and an error checking code.
IP moves packets through a network consisting of links and routers. A router has multiple
input and output ports. It forwards packets through the network using routing tables that tell the
router which output port to forward in incoming packet to. Specifically, a routing table maps IP
prefixes to output ports. For example, an entry in the routing table may indicate that all packets
with destination IP address matching 171.23. *. * are to be forwarded out the interface port with
id 17. IP routers exchange "link state information" to compute the routing tables; this computation
is a kind of shortest path algorithm.
TCP, the Transmission Control Protocol, is an end-to-end protocol built on top of IP. It creates a
a continuous reliable bidirectional connection. It does this by maintaining state at the two hosts-
this state includes IP packets that have been received, as well as sending acknowledgements. It
responds to dropped packets by requesting retransmits----each TCP packet has a sequence number.
The receiver signals the transmitter to reduce its transmission rate if the drop rate becomes high-it
does this by reducing the received window size. TCP also "demultiplexes" incoming data using
the concept of port number-this allows multiple applications on a host with a single IP address to
work simultaneously.
HTTR the Hyper Text Transfer Protocol, is built on top of TCP. An HTTP request or response
can be viewed as a text string consisting of a header and a body. The HTTP request and responses
header specify the type of the data through the Content-Type field. The response header includes
a code, which could indicate success ("2@"), a variety of failures ("4}4"-resource not found), or
more specialized scenarios ("302"-use cached version). A few other protocol fields are cookies,
request size, compression used.
HTTP was designed to enable the world-wide web, and focused on delivering web pages in a
single logical transaction. Its generality means that it has grown to provide much more, e.g., it's
commonly used to access remote procedures ("services"). An object-which could be a web page,
a file, or a service-is addressed using a URL, Uniform Resource Locator, which is a domain n€une,
a path, and optional arguments. When used to implement services, a corunon paradigm is for the
client to send a request using URL arguments, a JSON object, and files to be uploaded, and the
server responds with ]SON.
23,11, HTTPS
Describe HTTPS operationally, as well as the ideas underlying it.
Solution: In a nutshell, HTTPS is HTTP with SSL encryption. Because of the commercial impor-
tance of the Intemet, and the prevalence of wireless networks, it's imperative to protect data from
eavesdroppers-this is not done automatically by IP/ICP/HTTP.
Conceptually, one way to encrypt a channel is for the communicating parties to XOR each
transmitted byte with a secret byte-the receiver then XORs the received bytes with the secret.
This scheme is staggeringly weak-an eavesdropper can look at statisfics of the transmitted data to
easily figure out which of the 255 bytes is the secret. It leaves open the question of how to get the
secrete byte to the receiver. Furthermore, a client who initiates a transaction has no way of knowing
if someone has hijacked the network and directed traffic from the client to a malicious server.
SSL resolves these issues. First of all, it uses public key cryptography for key exchange-the idea
is that the public key is used by the client to encrypt and send a secret key (which can be viewed
347
```
