# Exercise 23.12: DNS

**Printed textbook page:** 348. **Reference transcription pages:** 348–349.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 348 (PDF page 362)

```text
as a generalization of the secret byte;256 bits is the common size) to the server. This secret key is
used to scramble the data to be transmitted in a recoverable way. The secret key is generated via
hashing a random number. Public key cryptography is based on the fact that it's possible to create
a one-way function, i.e., a function that can be made public and is easy to compute in one direction,
but hard to invert with the public information about it. Rivest, Shamir, and Adleman introduced
a prototypical such function which is based on several number theoretic facts, such as the relative
ease with which primes can be created, that computing ab mod c is fast, and that factorization is
(likely) hard.
Private key cryptography involves a single key which is a shared secret between the sender
and recipient. Private key cryptography offers many orders of magnitude higher bandwidth than
public key cryptography. For this reason, once the secret key has been exchanged via public key
cryptography, HTTPS turns to private key cryptography, specifically AES. AES operates on 128 bit
blocks of data. (If the data to be transmitted is less than 128 bits, it's padded up; if it's greater than
128bits, it's broken down into 128bit chunks.) The l28bitblock is represented as 16bytes na4x4
matrix. The secret key is used to select an ordering in which to permute the bytes; it is also used to
XOR the bits. This operation is reversible using the secret key.
A small shortcoming of the scheme described above is that it is susceptible to replay attacks-an
adversary may not know the exact contents of a transmission, but may know that it represents an
action ("add 10 gold coins to my World-Of-Warcraft account"). This can be handled by having the
seryer send a random number which must accompany client requests.
HTTPS adds another layer of security-SSl certificates. The third party issuing the SSL certificate
verifies that the HTTPS server is on the domain that it claims to be on, which precludes someone
who has hijacked the network from pretending to be the server being requested by the client. This
check is orthogonal to the essence of SSL (private key exchange and AES), and it can be disabled,
e.g., for testing a server locally.
23.12 DNS
Describe DNS, including both operational as well as implementation aspects.
Solution: DNS is the system which translates domain narnes-www. google. com-to numerical IP
addresses-216. 58 . 218 . 110. It is essential to the functioning of the Intemet. DNS is what makes it
possible for a browser to access a website-the routers in the Internet network rely on IP addresses
to lookup next-hops for packets.
There are many challenges to implementing DNS. Here are some of the most important ones.
o There are hundreds of millions of domains.
o There are hundreds of billions of DNS lookups a day.
o Domains and IP addresses are added and updated continuously.
To solve these problems, DNS is implemented as a distributed directory service. A DNS lookup
is addressed to a DNS server. Each DNS server stores a database of domain names to IP addresses;
if it cannot find a domain name being queried in this database it forwards the request to other
DNS servers. These requests can get forwarded all the way up to the root name servers, which are
responsible for top-level domains.
At the time of writing there are L3 root name servers. This does not mean there are exactly 13
physical servers. Each operator uses redundancy to provide reliable service. Additionally, these
servers are replicated across multiple locations. Key to performance is the heavy use of caching, in
the client itself, as well as in the DNS servers.
348
```

#### Printed page 349 (PDF page 363)

```text
Part lV
The Honors Class
```
