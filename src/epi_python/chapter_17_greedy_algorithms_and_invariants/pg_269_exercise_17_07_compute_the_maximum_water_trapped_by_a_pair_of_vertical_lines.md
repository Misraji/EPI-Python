# Exercise 17.7: Compute the maximum water trapped by a pair of vertical lines

**Printed textbook page:** 269. **Reference transcription pages:** 269–269.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 269 (PDF page 283)

```text
CityAndRenainingGas = collections. namedtuple ( 'CityAndRemainingGas , 
,
( 'city ' , 'remaining_gallons ') )
city-remaining-gaIIons-pair = CityAndRemainingGas(0, O)
num-cities = !6n(93IIons)
for i in range(1, num-cities):
remaining-gallons +- gallonsti - 1l - distancesti - 1l // l,lpc
if remaining-gallons < city_remaining_9al1ons_pair. remaining_gaIlons :
city_remaining_gaIlons_pair = CityAndRemainingGas (
i, remaining_gaIIons)
return city_renaining_gallons_pair. city
The time complexity is O(n), and the space complexity is O(1).
Varianh Solve the same problem when you cannot assume that there exists an ample city.
17.7 CoupurE THE MAXIMUM wATER TRAppED By A pArR oF vERTICAL LrNES
An array of integers naturally defines a set of lines parallel to the Y-axis, starting from x = 0 as
illustrated in Figure U.a@). The goal of this problem is to find the pair of lines that together with
the X-axis "ttap" the most water. See Figure 17.4b) for an example.
0 
i 
2 
3 
4 
5 
6 
7 
I 
9 
lO 
tL 
t2 
13 
14 
15 
L6 
17
(a) A graphical depiction of the array (1,2,1,,3,4,4,5,6,2,1,3,1,3,2,1.,2,4,I>
2 
3 
4 
5 
6 
7 
8 
9 
10 
11 
t2 
13 
14 
15 
t6 
1?
(b) The shaded area between 4 and 16 is the maximum water that can be trapped by the anay in (a).
Figute 17.4: Example of maximum water trapped by a pair of vertical lines.
Write a Program which takes as input an integer array and retums the pair of entries that trap the
maximum amount of water.
Hint: Slart with 0 and z - 1 and work your way in.
0l
269
```
