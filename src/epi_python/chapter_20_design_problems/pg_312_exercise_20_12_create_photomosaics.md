# Exercise 20.12: Create photomosaics

**Printed textbook page:** 312. **Reference transcription pages:** 312–312.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 312 (PDF page 326)

```text
may nm into a situation where most clients will find that the min event they are trying to extract
has already been deleted. If the throughput of this service can be handled by a single machine, we
can make one server solely responsible for responding to all the requests. This server can prefetch
the top hundred or so events from each of the machines and keep them in a heap.
In many applications, we do not need strong consistency guarantees. We want to spend most of
our resources taking care of the highest priority jobs. In this setting, a client could pick one of the
machines at random, and request the highest priority job. This would work well for the distributed
crawler application. It is not suited to event-driven simulation because of dependencies.
Another other issue to consider is resilience: if a node fails, all list of work on that node fails
as well. It is better to have nodes to contain overlapped lists and the dispatching node in this case
will handle duplicates. The lost of a node shouldn't result in full re-hashing-the replacement node
should handle only new jobs. Consistent hashing can be used to achieve this.
A front-end caching server can become a bottleneck. This can be avoided by using replication,
i.e., multiple servers which duplicate each other. There could be possible several ways to coordinate
them: use non-overlapping lists, keep a blocked job list, return a random job from the jobs with
highest priority.
20.12 Cnrnrr PHoroMosArcs
A photomosaic is built from a collection of images called "tiles" and a target image. The photomosaic
is another image which approximates the target image and is built by juxtaposing the tiles. Quality
is defined by human perception.
Design a program that produces high quality mosaics with minimal compute time'
Hint:How would you define the distance between two images?
Solution: A good way to begin is to partition the image into s x s-sized squares, compute the
average color of each such image square, and then find the tile that is closest to it in the color sPace.
Distance in the color space can be the L2-distance over the Red-Green-Blue (RGB) intensities for
the color. As you look more carefully at the problem, you might conclude that it would be better
to match each tile with an image square that has a similar structure. One way could be to perform
a coarse pixelization (2x2 or 3 x 3) of each image square and finding the tile that is "closest" to
the image square under a distance function defined over all pixel colors. In essence, the problem
reduces to finding the closest point from a set of points in a k-dimensional sPace.
Given m tiles and an image partitioned into n squares, then a brute-force approach would have
O(mn) time complexity. You could improve on this by first indexing the tiles using an appropriate
search tree. You can also run the matching in parallel by partitioning the original irnage into
subimages and searching for matches on the subimages independently.
20.13 Ilrprnlrcur MrI,sacr RUN
Airlines often give customers who fly frequently with them a "status". This status allows them
early boarding, more baggage, upgrades to executive class, etc. Typically, status is a function of
miles flown in the past twelve months. People who travel frequently by air sometimes want to take
312
```
