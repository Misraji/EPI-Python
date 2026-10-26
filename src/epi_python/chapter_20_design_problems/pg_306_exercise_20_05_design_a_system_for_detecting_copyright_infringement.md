# Exercise 20.5: Design a system for detecting copyright infringement

**Printed textbook page:** 306. **Reference transcription pages:** 306–306.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 306 (PDF page 320)

```text
of matching user IDs for every attribute. To do it use reverse indexes, with a string hash for quick
lookup in storage. Assuming arrays are retumed sorted there is an easy way to merge arrays for
multiple attributes and make a decision about matching to a group / starting new grouP.
Now suppose the network is too large to fit on a single machine. Because of number of users
it makes sense to process problem on multiple machines----each will store subset of attributes and
may retum results as user IDs. We will need to make two merge operations:
o Identical searches-when a single attribute lookup was performed on many machines. We
will need to merge retumed sorted IDs into big sorted list of IDs.
o Searches by different attributes-we will need to merge those attributes if they all are present
in all lists (or if the match criteria is above X/o, e.g. 314 are matching).
Since in all likelihood we do not need to perform real-time matching we could use the Consumer-
Producer pattem: pick up users from a queue and perform a search, thereby limit the number of
simultaneous requests.
20.5 Dssrchr A sysrEM FoR DETEcTING copyRIGHT INFRINGEMENT
YouTV.com is a successful online video sharing site. Hollywood studios complain that much of the
material uploaded to the site violates copyright.
Design a feature that allows a studio to enter a set y of videos that belong to it, and to determine
which videos in the YouTV.com database match videos in V.
Hln f: Normalize the video format and create signatures.
Solution: If we replaced videos everywhere with documents, we could use the techniques in
Solution 20.3 on Page 304, where we looked for near duplicate documents by computing hash
codes for each length-k substring.
Videos differ from documents in that the same content may be encoded in many different
formats, with different resolufions, and levels of compression.
One way to reduce the duplicate video problem to the duplicate document problem is to re-
encode all videos to a common format, resolution, and compression level. This in itself does not
mean that two videos of the same content get reduced to identical files-the initial settings affuct
the resulting videos. However, we can now "signature" the normalized video.
A trivial signature would be to assign a 0 or a 1 to each frame based on whether it has more or
less brightness than average. A more sophisticated signature would be a 3 bit measure of the red,
green/ and blue intensities for each frame. Even more sophisticated signatures can be developed,
e.g.,by taking into account the regions on individual frames. The motivation for better signatures
is to reduce the number of false matches returned by the system, and thereby reduce the amount of
time needed to review the matches.
The solution proposed above is algorithmic. However, there are alternative approaches that
could be effective: letting users flag videos that infringe copyright (and possibly rewarding them
for their effort), checking for videos that are identical to videos that have previously been identified
as infringing, looking at meta-information in the video header, etc.
Variant Design an online music identification service.
306
```
