# Exercise 8.5: Compute buildings with a sunset view

**Printed textbook page:** 103. **Reference transcription pages:** 103–105.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 103 (PDF page 117)

```text
Write a program which takes a pathname, and retums the shortest equivalent pathname. Assume
individual directories and files have names that use only alphanumeric characters. Subdirectory
names may be combined using forward slashes (/), the current directory (.) and parent directory
(. .).
Hint: Trace the cases. How should . and . . be handled? Watch for invalid paths.
Solution: It is natural to process the string from left-to-right, splitting on forward slashes (/s). We
record directory and file names. Each time we encounter a . ., we delete the most recent narne,
which corresponds to going up directory hierarchy. Since names are processed in a last-in, first-out
order, it is natural to store them in a stack. hrdividual periods (. s) are skipped.
If the string begins with /, then we cannot go up from it. We record this in the stack. If the stack
does not begin with /, we may encounter an empty stack when processing . ., which indicates a
path that begins with an ancestor of the current working path. We need to record this in order to
give the shortest equivalent path. The final state of the stack directly corresponds to the shortest
equivalent directory path.
Forexample,if thestring issc//./../tc/awk/././, thestackprogressionisasfollows: (sc),0,
(tc), (tc, awk). Note that we skip three . s and the / after sc/.
def shortest-equivalent-path(path) :
if not path:
raise ValueError('Empty string is not a valid path.')
path-names = [] 
# Uses list 
as a stack.
# Special case.' starts rcith '/' , which is an absol.ute path
if path tOl == '/' 
:
path-names . append ('/')
for token in (token for token in path.split('/') if token not in
if token == ' .. ':
if not path-names or path-names[-1] == '..':
path_name s . append (token)
else:
if path-names[-1] ==' /' :
raise ValueError('Path error')
path-names.popo
else: # Ilust be a name.
path_names . append (token)
t'
,,])
result =' /' .join(path_names)
return result[result.startswith(' //'):) 
# Avoid starting'//'
The time complexity is O(n), where n is the length of the pathname.
8.5 Coupurn BUrLDrNcs wrrH A suNSET vrEw
You are given a series of buildings that have windows facing west. The buildings are in a straight
line, and any building which is to the east of a building of equal or greater height cannot view the
sunset.
103
```

#### Printed page 104 (PDF page 118)

```text
Design an algorithm that processes buildings in east-to-west order and returns the set of buildings
which view the sunset. Each building is specified by its height.
Hint: rNhen does a building not have a sunset view?
Solution: A brute-force approach is to store all buildings in an array. We then do a reverse scan of
this array, tracking the running maximum. Any building whose height is less than or equal to the
running maximum does not have a sunset view.
The time and space complexity are both O(n),where n is the number of buildings.
Note that if a building is to the east of a taller building, it cannot view the sunset. This suggests a
way to reduce the space complexity. We record buildings which potentially have a view. Each new
building may block views from the existing set. We determine which such buildings are blocked
by comparing the new building's height to that of the buildings in the existing set. We can store the
existing set as a hash set-this requires us to iterate over all buildings each time a new building is
processed.
If a new building is shorter than a building in the current set, then all buildings in the current
set which are further to the east cannot be blocked by the new building. This suggests keeping the
buildings in a last-in, first-out mElnner/ so that we can terminate earlier.
Specifically, we use a stack to record buildings that have a view. Each time a building b is
processed, if it is taller than the building at the top of the stack, we pop the stack until the top of the
stack is taller than b-all the buildings thus removed lie to the east of a taller building.
Although some individual steps may require many pops, each building is pushed and popped
at most once. Therefore, the run time to process n buildings is O(n), and the stack always holds
precisely the buildings which currently have a view
The memory used is O(n), and the bound is tight, even when only one building has a view-
consider the input where the west-most building is the tallest, and the remaining n - 1 buildings
decrease in height from east to west. Howevet in the best-case, e.g., when buildings appear in
increasing height, we use 0(L) space. In contrast, the brute-force approach always uses O(n) space.
def examine-buildings-with-sunset (sequence) :
BuildingWithHeight = collections. namedtuple (' Buildingl{ithHeight',
('id' , 'heisht ') )
candidates = []
for buiLding-idx, building-height in enunerate(sequence) :
while candidates and building_height >= candidates[-1].height:
candidates .pop o
candidates. append(BuildingWithHeight (building-idx, 
building-height))
return Icandidate.id for candidate in reversed(candidates)]
Variant: Solve the problem subject to the same constraints when buildings are presented in west-
to-east order.
Queues
A queue supports two basic operations----enqueue and dequeue. (If the queue is empty, dequeue
typically retums null or throws an exception.) Elements are added (enqueued) and removed
(dequeued) in first-in, first-out order. The most recently inserted element is referred to as the tail
104
```

#### Printed page 105 (PDF page 119)

```text
or back element, and the item that was inserted least recently is referred to as the head or front
element.
A queue can be implemented using a linked list, in which case these operations have O(1) time
complexity. The queue API often includes other operations, e.g., a method that retums the item at
the head of the queue without removing it, a method that returns the item at the tail of the queue
without removing it, etc. A queue can also be implemented using an array; see Problem 8.7 on
Page 1.07 for details.
dequeud 
- 
)
:2i0' 
ZiOiliy'enqueue4
------r-----i-
Jr!rIr
-J-J-t-- 
-J_I_ 
_J__---L---_J_
(a) lnitial configuration. (b) Queue (a) after dequeue. (c) Queue (b) a,ter enqu€uing 4
Figure 8.3: Examples of enqueuing and dequeuing.
A deque, also sometimes called a double-ended queue, is a doubly linked list in which all
insertions and deletions are from one of the two ends of the list, i.e., at the head or the tail. An
insertion to the front is commonly called a push, and an insertion to the back is commonly called
an inject. A deletion from the front is commonly called a pop, and a deletion from the back is
commonly called an eject. (Different languages and libraries may have different nomenclature.)
Queuesboot camp
In the following program, we implement the basic queue APl---enqueue and dequeue-as well
as a max-method, which refums the maximum element stored in the queue. The basic idea is to
use composition: add a private field that references a library queue object, and forward existing
methods (enqueue and dequeue in this case) to that object.
class Queue:
def --init--(self):
self ._data = collections.dequeo
def enqueue (self, x) :
seIf.-data.append(x)
def dequeue(self):
return self ._data.popleft()
def max(self):
return max (se1f . -data)
The time complexity of enqueue and dequeue are the same as that of the library queue, namely,
O(1). The time complexity of finding the maximurnis O(n), where n is the number of entries. In
Solution 8.9 on Page 109 we show how to improve the time complexity of maximum to O(1) with a
more customized approach.
Learn to recogmze w
queue
property is
Table 8.2: Top Tips for Queues
when order needs to be preserved.
105
For example, queues are
```
