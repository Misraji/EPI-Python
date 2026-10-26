# Exercise 20.14: Implement Cormexus

**Printed textbook page:** 314. **Reference transcription pages:** 314–314.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 314 (PDF page 328)

```text
Persistence of data can be implemented through a database. Most web application frameworks
provide support for automating the process of reading and writing objects from and to a database.
Finally, web application frameworks can route incoming HTTP requests to appropriate code-this
is through a configuration file matching URLs to methods. The framework provides convenience
methods for accessing HTTP fields and writing results. Frameworks also provide HTTP templating
mechanisms, wherein developers intersperse HTML with snippets of code that dynamically add
content to the HTML.
Web application frameworks typically implement cron functionaliry wherein specified functions
are executed at a regular interval. This can be used to periodically scrape data and check if the
condition of an alert is matched by the data.
Finally, the web app can be deployed via a platform-as-a-seryice such as Amazon Web Services
and Google App Engine.
20.14 IMprsl,rcNr CoNNrxus
How would you design Connexus, a system by which users can share pictures? Address issues
around access control (public, private), picture upload, organizing pictures, summarizing sets of
pictures, allowing feedback, and displaying geographical and temporal information for pictures.
Hlnf: Think about the UI, in particular UI widgets that make for an engaging product.
Solution: There are three aspects to Connexus. The first is the serverbackend, used to store images,
and meta-data, such as author, comments, hashtags, GPS coordinates, etc., as well as run cron jobs
to identify trending streams. The technology for this is similar to Mileage Run (Solution 20.13 on
the previous page), with the caveat that a database is not suitable for storing large binary objects
such as images, which should be stored on a local or remote file system. (The database will hold
references to the file.)
The web UI is also similar to Mileage Run, with a login page, a management page, and pages
for displaying images. Images can be grouped based on a concept of a stream, with comment
boxes annotating streams. Facebook integration would make it easier to share links to streams, and
post new images as status updates. Search capability and discussion boards also enhance the user
experience.
Some UI features that are especially appealing are displaying images by location on a zoomable
map, slider UI controls to show subsets of images in a stream based on the selected time intervals,
a file upload dialog with progress measures, support for multiple simultaneous uploads, and drag-
and-drop upload. A11 these UI widgets are provided by, for example, the jQuery-Ul ]avascript
library. fihis library also makes the process of creating autocompletion on text entry fields trivial.)
Connexus is an application that begs for a mobile client. A smartphone provides a camera/
location information, and push notifications. These can be used to make it easier to create and im-
mediately upload geotagged images, find nearby images, and be immediately notified on updates
and comments. The two most popular mobile platforms, iOS and Android, have APIs rich in UI
widgets and media access. Both can use serialization formats such as ]SON or protocol buffers to
communicate with the server via remote procedure calls layered over HTTP'
31.4
```
