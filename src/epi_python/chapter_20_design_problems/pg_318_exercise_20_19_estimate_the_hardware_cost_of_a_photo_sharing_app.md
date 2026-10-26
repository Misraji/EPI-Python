# Exercise 20.19: Estimate the hardware cost of a photo sharing app

**Printed textbook page:** 318. **Reference transcription pages:** 318–318.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 318 (PDF page 332)

```text
The browser is responsible for taking the retumed FilML and displaying it on the client. The
rendering is done in two parts. First, a parse tree (the DOM) is generated from the HTML, and
then a rendering library "paints" the screen. The retumed HTML may include scripts written in
javaScript. These are executed by the browser, and they can perform actions like making requests
and updating the DOM based on the responses-this is how a live stock ticker is implemented.
Styling attributes (CSS) are commonly used to customize the look of a page.
Many more issues exist on both the client and server side: security, cookies, HTML form
elements, HTML styling, and handlers for multi-media content, to name a few.
20.19 Esur'rern rHE HARDwARE cosr oF A pHoro sHARING App
Estimate the hardware cost of the server hardware needed to build a photo sharing app used by
every person on the earth.
Hint: tJse variables to denote quantities and costs, and relate them with equations. Then fill in reasonable
values.
Solution: The cost is a function of server CPU and RAM resources, storage, and bandwidth, as well
as the number and size of the images that are uploaded each day. We will create an estimate based
on unit costs for each of these. We assume a distributed architecture in which images are spread
("sharded") across servers.
Assume each user uploads i images each day with an average size of s bytes, and that each
image is viewed u times. After d days, the storage requirement is lsdN, where N is the number of
users. Assuming o >> 1, i.e., most images are seen many times, the server cost is dominated by the
time to serve the images. The servers are required to serve up Nlu images and Nlas bytes each day.
Assuming a server can handle /x HTTP requests per second and has an outgoing bandwidth of b
bytes per second, the number of required servers is max(Nlo/Th,NioslTb), where T is the number
of seconds in a day.
Reasonable values for N, i, s, alrrd o are 1010, 10, 10s, and 100. Reasonable values for h and b
are 10a and 108. There are approximately 1d seconds in a day. Therefore the number of servers
requiredismax((1010x10x100)/(10sx104),(1010x10x100x10s)/(10sx108))=L05.Eachserver
would cost $1000, so the total cost would be of the order of 100 million dollars.
Storage costs are approximately $0.1 per gigabyte, and we add Nls - 1010 x 10 x 1d bytes each
day, so each day we need to add a million dollars worth of storage.
The above calculation leaves out many costs, such as electricity, cooling, and network. It also
neglects computations such as computing trending data and spam analysis. Furthermore, there is
no measure of the cost of redundancy, such as replicated storage, or the ability to handle nonuniform
loads. Nevertheless, it is a decent starting point. \A/hat is remarkable is the fact that the entire world
can be connected through images at a very low cost-pennies Per Person.
318
```
