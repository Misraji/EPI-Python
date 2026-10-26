# Exercise 20.13: Implement Mileage Run

**Printed textbook page:** 312. **Reference transcription pages:** 312–313.

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

#### Printed page 313 (PDF page 327)

```text
a round trip flight simply to maintain their stahrs. The destination is immaterial-the goal is to
minimize the cost-per-mile (cpm), i.e., the ratio of dollars spent to miles flown.
Design a system that will help its users find mileage runs.
Hint: Partition the implied features into independent tasks.
Solution: There are two distinct aspects to the design. The first is the user-facing portion of the
system. The second is the server backend that gets flight-price-distance information and combines
it with user input to generate the alerts.
We begin with the user-facing portion. For simplicity, we illustrate it with a web-app, with the
realization that the web-app could also be written as a desktop or mobile app. The web-app has
the following components: a login page, a manage alerts page, a create an alert page, and a results
page. For such a system we would like defer to a single-sign-on login service such as that provided
by Google or Facebook. The management page would present login information, a list of alerts,
and the ability to create an alert.
One reasonable formulation of an alert is that it is an origin city, a target cpm, and optionally,
a date or range of travel dates. The results page would show flights satisfying the constraints.
Note that other formulations are also possible, such as how frequently to check for flights, a set of
destinations, a set of origins, etc.
The classical approach to implement the web-app front end is through dynamically generated
HTML on the server, e.9., through ]ava Server Pages. It can be made more visually appealing
and intuitive by making appropriate use of cascaded style sheets, which are used for fonts, colors,
and placements. The UI can be made more efficient through the use of ]avascript to autocomplete
corunon fields, and make attractive date pickers.
Modem practice is to eschew server-side HTML generation, and instead have a single-page
application, in which |avascript reads and writes favaScript Object Notation (ISON) objects to the
server/ and incrementally updates the single-page based. The AngularJS framework supports this
approach.
The web-app backend server has four components: gathering flight data, matching user-
generated alerts to this data, persisting data and alerts, and generating the responses to browser
initiated requests.
Flight data can be gathered via "scraping" orby subscribing to a flight data service. ftraping
refers to extraction of data from a website. It can be quite involved-some of the issues are parsing
the results from the website, filling in form data, and running the Javascript that often populates
the actual results on a page. Selenium is a ]ava tibrary that can programmatically interface to
the Firefox browser, and is appropriate for scraping sites that are rich in ]avascript. Most flight
data services are paid. IIA software provides a very widely used paid aggregated flight data feed
service. The popular Kayak site provides an Extensible Markup Language (XML) feed of recently
discovered fares, which can be a good free alternative. Flight data does not include the distance
between airports, but there are websites which return the distance between airport codes which can
be used to generate the cpm for a flight.
There are a number of common web application frameworks--essentially libraries that handle
many common tasks-that can be used to generate the server. ]ava and Python are very commonly
used for writing the backend for web applications.
313
```
