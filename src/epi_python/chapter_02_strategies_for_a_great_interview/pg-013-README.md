# Chapter 2: Strategies For A Great Interview

**Starts at printed page 13.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 13

```text
CHeprrn
Strategies For A Great Interview
The essence of strategy is choosing whnt not to do.
- M. E. Ponrrn
The technical component of an onsite interview usually consists of three to five one-on-one in-
terviews with engineers. A typical one hour interview with a single interviewer consists of five
minutes of introductions and questions about the candidate's r6sum6. This is followed by five to
fifteen minutes of questioning on basic programming concepts. The core of the interview is one
or two problems where the candidate is expected to present a detailed solution on a whiteboard,
Paper/ or integrated development environments (IDEs). Depending on the interviewer and the
question, the solution may be required to include syntactically correct code and tests. Junior candi-
dates should expect more emphasis on coding, and less on system design and architecture. Senior
candidates should expect more emphasis on system design and architecture, though at least one
interviewer will ask a problem that entails writing detailed code.
Appro aching the problem
No matter how clever and well prepared you are, the solution to an interview problem may not
occur to you immediately. Here are some things to keep in mind when this happens.
Clarify the question: This may seem obvious but it is amazing how many interviews go badly
because the candidate spends most of his time trying to solve the wrong problem. If a question
seems exceptionally hard, you may have misunderstood it.
A good way of clarifying the question is to state a concrete instance of the problem. For example,
if the question is "find the first occurrence of a number greater than k in a sorted dttdf", you could
ask "if the input array is <2,20,30) and k is 3, then are you supposed to retum 1, the index of 20?"
These questions can be formalized as unit tests.
Feel free to ask the interviewer what time and space complexity he would like in your solution. If
you are told to implement an O(n) algorithm or use O(1) space, it can simplify your life considerably.
It is possible that he will refuse to specify these, or be vague about complexity requirements, but
there is no harm in asking. Even if they are evasive, you may get some clues.
Work on concrete examples: Consider the problem of determining the smallest amount of
change that you cannot make with a given set of coins, as described on Page 186. This problem
may seem difficult at first. Howeve{, if you try out the smallest amount that cannot be made with
some small examples, e.9.,11,21,11,,31, {L,2,4l,l'1,2,51, you will get the key insights: examine coins
in sorted order, and look for a large "jtJmp"-acoin which is larger than the sum of the preceding
coins.
13
```

### Printed page 14

```text
Spell out the brute-force solution: Problems that are put to you in an interview tend to have
an obvious brute-force solution that has a high time complexity compared to more sophisticated
solutions. For example, instead of trying to work out a DP solution for a problem (e.g., for
Problem 167 onPage249), try a1l the possible configurations. Advantages to this approach include:
(1.) it helps you explore opportunities for optimization and hence reach a better solution, (2.) it gives
you an opportunity to demonstrate some problem solving and coding skills, and (3.) it establishes
that both you and the interviewer are thinking about the same problem. Be wamed that this strategy
can sometimes be detrimental if it takes a long time to describe the brute-force approach.
Think out loud: One of the worst things you can do in an interview is to freeze up when solving
the problem. It is always a good idea to think out loud and stay engaged. On the one hand, this
increases your chances of finding the right solution because it forces you to put your thoughts in
a coherent manner. On the other hand, this helps the interviewer guide your thought process in
the right direction. Even if you are not able to reach the solution, the interviewer will form some
impression of your intellectual ability.
Apply patterns: Pattems-general reusable solutions to commonly occurring problems-can
be a good way to approach a baffling problem. Examples include finding a good data structure,
seeing if your problem is a good fit for a general algorithmic technique, e.g., divide-and-conqueq,
recursion, or dlmamic programming, and mapping the problem to a graph.
Presenting the solution
Once you have an algorithm, it is important to present it in a clear manner. Your solution will
be much simpler if you take advantage of libraries such as ]ava Collections, C++ STL, or Python
collections. However, it is far more important that you use the language you are most comfortable
with. Here are some things to keep in mind when presenting a solution.
Libraries: Do not reinvent the wheel (unless asked to invent it). In particular, master the
libraries, especially the data structures. For example, do not waste time and lose credibility trying
to remember how to pass an explicit comparator to a BST constructor. Remember that a hash
function should use exactly those fields which are used in the equality check. A comparison
function should be transitive.
Focus on the top-level algorithm: It's OK to use functions that you will implement later. This
will let you focus on the main part of the algorithm, will penalize you less if you don't complete the
algorithm. (Hash, equals, and compare functions are good candidates for deferred implementation.)
Specify that you will handle main algorithm first, then comer cases. Add TODO comments for
portions that you want to come back to.
Manage the whiteboard: You will likely use more of the board than you expect so start at the
top-left comer. Make use of functions-skip implementing anything that's trivial (e.g., finding the
maximum of an array) or standard (e.g., a thread pool). Best practices for coding on a whiteboard
are very different from best practices for coding on a production project. For example, don't worry
about skipping documentation, or using the right indentation. Writing on a whiteboard is much
slower than on a keyboard, so keeping your identifiers short (our recommendation is no more than
7 characters) but recognizable is a best practice. Have a convention for identifiers, €.9.r i, j,k for
array indices, A, B, C for arrays, s for string, d for dict., etc.
1.4
```

### Printed page 15

```text
Assume valid inputs: ln a production environmen! it is good practice to check if inputs are
valid, e.g., that a string purporting to represent a normegative integer actually consists solely of
numeric characters, no flight in a timetable arrives before it departs, etc. Unless they are pa* of the
problem statement, in an interview setting, such checks are inappropriate: they take time to code,
and distract from the core problem. (You should clarify this assumption with the interviewer.)
Test for corner cases: For many problems/ your general idea may work for most valid inputs
but there may be pathological valid inputs where your algorithm (or your implementation of it)
fails. For example, your binary search code may crash if the input is an empty affay; or you may
do arithmetic without considering the possibility of overflow. It is important to systematically
consider these possibilities. If there is time, write unit tests. Small, extreme, or random inputs
make for good stimuli. Don't forget to add code for checking the result. Occasionally, the code to
handle obscure corner cases may be too complicated to implement in an interview setting. If so,
you should mention to the interviewer that you are aware of these problems, and could address
them if required.
Syntax: Interviewers rarely penalize you for small syntax elrors since modem IDE excel at
handling these details. However, lots of bad syntax may result in the impression that you have
limited coding experience. Once you are done writing your program, make a pass through it to fix
any obvious syrtax errors before claiming you are done.
Candidates often tend to get ftrnction signatures wrong and it reflects poorly on them. For
example, it would be an error to write a function in C that refums an arraybut not its size,
Memory m:rnagement: Generally speaking, it is best to avoid memory mEu:ragement operations
altogether. See if you can reuse space. For example, some linked list problems can be solved with
O(1) additional space by reusing existing nodes.
Your Interviewer Is Not Alan Turing: Interviewers are not capable of analyznglong programs,
particularly on a whiteboard or paper. Therefore, they ask questions whose solutions use short
Programs. A good tip is that if your solution takes more than 50 lines to code in Python, it's a sign
that you are on the wrong track, and you should reconsider your approach.
Know yourintentiewers B the company
It can help you a great deal if the company can share with you the background of your interviewers
in advance. You should use search and social networks to leam more about the people interviewing
you. Letting your interviewers know that you have researched them helps break the ice and forms
the impression that you are enthusiastic and will go the extra mile. For fresh graduates, it is also
important to think from the perspective of the interviewers as described in Chapter 3.
Once you ace your interviews and have an offur, you have an important decision to make-is this
the organization where you want to work? Interviews are a great time to collect this information.
Interviews usually end with the interviewers letting the candidates ask questions. You should
make the best use of this time by getting the information you would need and communicating to
the interviewer that you are genuinely interested in the job. Based on your interaction with the
interviewers, you may get a good idea of their intellect, passion, and faimess. This extends to the
team and company.
In addition to knowing your interviewers, you should know about the company vision, history,
organization, Products, and technology. You should be ready to talk about what specifically appeals
15
```

### Printed page 16

```text
to you, and to ask intelligent questions about the company and the job. Prepare a list of questions
in advance; it gets you helpful information as well as shows your knowledge and enthusiasm for
the organization. You may also want to think of some concrete ideas around things you could do
for the companyi be careful not to come across as a pushy know-it-all.
All companies want bright and motivated engineers, Howeve{, companies differ greatly in their
culture and organization. Here is a brief classification.
Mature consumer-facing compan!1 e.gv Google: wants candidates who understand emerging
technologies from the user's perspective. Such companies have a deeper technology stack, much
of which is developed in-house. They have the resources and the time to train a new hire.
Enterprise-oriented comparlrlr e.g.r Oracle: looks for developers familiar with how large projects
are organized, e.g., engineers who are familiar with reviews, documentation, and rigorous testing.
Government contractor, e.g., Lockheed-Martin: values knowledge of specifications and testing,
and looks for engineers who are familiar with govemment-mandated processes.
Startup, e.g., Uber: values engineers who take initiative and develop products on their own.
Such companies do not have time to train new hires, and tend to hire candidates who are very fast
learners or are already familiar with their technology stack, e.g., their web application framework,
machine leaming system, etc.
Embedded systems/chip design company, e.g, National Instruments: wants software engi-
neers who know enough about hardware to interface with the hardware engineers. The tool chain
and development practices at such companies tend to be very mature.
General conoersation
Often interviewers will ask you questions about your past projects, such as a senior design project
or an intemship. The point of this conversation is to answer the following questions:
Can the candidate clearly communicate a complex idea? This is one of the most important
skills for working in an engineering team. If you have a grand idea to redesign a big system, can
you corununicate it to your colleagues and bring them on board? It is crucial to practice how you
will present your best work. Being precise, clear, and having concrete examples can go a long way
here. Candidates communicating in a language that is not their first language, should take extra
care to speak slowly and make more use of the whiteboard to augment their words.
Is the candidate passionate about his work? We always want our colleagues to be excited,
energetic, and inspiring to work with. If you feel passionately about your work, and your eyes light
up when describing what you've done, it goes a long way in establishing you as a great colleague.
Hence, when you are asked to describe a project from the past, it is best to pick something that you
are passionate about rather than a project that was complex but did not interest you.
Is there a potential interest match with some project? The interviewer may gauge areas of
strengths for a potential project match. If you know the requirements of the job, you may want
to steer the conversation in that direction. Keep in mind that because technology changes so fast
many teams prefer a strong generalist, so don't pigeonhole yourself.
Other ailaice
A bad mental and physical attitude can lead to a negative outcome. Don't let these simple mistakes
lead to your years of preparation going to waste.
1,6
```

### Printed page 17

```text
Be honest Nobody wants a colleague who falsely claims to have tested code or done a code
review Dishonesty in an interview is a fast pass to an early exit.
Remember, nothing breaks the truth more than stretching it-you should be ready to defend
anything you claim on your r6sum6. If your knowledge of Python extends only as far as having
cut-and-paste sample code, do not add Python to your r6sum6.
Similarly, if you have seen a problem before, you should say so. (Be sure that it really is the
same problem, and bear in mind you should describe a correct solution quickly if you claim to have
solved it before.) Interviewers have been known to collude to ask the same question of a candidate
to see if he tells the second interviewer about the first instance. An interviewer may feign ignorance
on a topic he knows in depth to see if a candidate pretends to know it.
Keep a positive spirit: A cheerful and optimistic attitude can go a long way. Absolutely nothing
is to be gained, and much can be lost, by complaining how difficult your joumey was, how you are
not a moming person, how inconsiderate the airline/hotefHR staff were, etc.
Don't apologize: Candidates sometimes apologize in advance for a weak GPA, rusty coding
skills, or not knowing the technology stack. Their logic is thatby being proactive they will somehow
benefit from lowered expectations. Nothing can be further from the truth. It focuses attention on
shortcomings. More generally, if you do not believe in yourself, you cannot expect others to believe
in you.
Keep money and perks out of the interview: Money is a big element i. *y job but it is best
left discussed with the HR division after an offer is made. The same is true for vacation time, day
care support, and funding for conference travel.
Appearance: Most software companies have a relaxed dress-code, and new graduates may
wonder if they will look foolish by overdressing. The damage done when you are too casual is
greater than the minor embarrassment you may feel at being overdressed. It is always a good idea
to err on the side of caution and dress formally for your interviews. At the minimum, be clean and
well-groomed.
Be aware of your body language: Think of a friend or coworker slouched all the time or
absentmindedly doing things that may offend others. Work on your posture, eye contact and
handshake, and remember to smile.
Sfuess interuiews
Some companies, primarily in the finance industry, make a practice of having one of the interviewers
create a stressful situation for the candidate. The stress may be injected technically, e.g., via a ninja
problem, or through behavioral means, e.g., the interviewer rejecting a correct answer or ridiculing
the candidate. The goal is to see how a candidate reacts to such situations-does he fall apart,
become belligerent, or get swayed easily. The guidelines in the previous section should help you
through a stress interview. (Bear in mind you will not know a priori if a particular interviewer will
be conducting a stress interview.)
Le arning from b ad outc omes
The reality is that not every interview results in a job offer. There are many reasons for not getting
a particular job. Some are technical: you may have missed that key flash of insight, e.g., the key
17
```

### Printed page 18

```text
to solving the maximum-profit on Page 1 in linear time. If this is the case, go back and solve that
problem, as well as related problems.
Often, your interviewer may have spent a few minutes looking at your r6sum6-this is a
depressingly corunon practice. This can lead to your being asked questions on topics outside of the
area of expertise you claimed on your r6sum6, e.9., routing protocols or Structured Query Language
(SQL). If so, make sure your r6sum6 is accurate, and brush up on that topic for the future.
You can fail an interview for nontechnical reasons, e.g., you c€une across as uninterested, or you
did not communicate clearly. The company may have decided not to hire in your area, or another
candidate with similar ability but more relevant experience was hired.
You will not get any feedback from a bad outcome, so it is your responsibility to try and piece
together the causes. Remember the only mistakes are the ones you don't leam from.
Negotiating an offer
An offer is not an offer till it is on paper, with all the details filled in. All offers are negotiable.
We have seen compensation packages bargained up to twice the initial offer, but 10-20% is more
typical. \rVhen negotiating, remember there is nothing to be gained, and much to lose, by being
rude. (Being firm is not the s€une as being rude.)
To get the best possible offer, get multiple offers, and be flexible about the form of your com-
pensation. For example, base salary is less flexible than stock options, sign-on bonus, relocation
expenses, and Immigration and Naturalization Service (INS) filing costs. Be concrete-instead of
just asking for more money, ask for a P% higher salary. Otherwise the recruiter will simply come
back with a small increase in the sign-on bonus and claim to have met your request.
Your HR contact is a professional negotiator, whose fiduciary duty is to the company. He will
know and use negotiating techniques such as reciprocity, getting consensus, putting words in your
mouth ("don't you think that's reasonable?"), as well as threats, to get the best possible deal for the
company. (This is what recruiters themselves are evaluated on internally.) The Wikipedia article on
negotiation lays bare many tricks we have seen recruiters employ.
One suggestion: stick to email, where it is harder for someone to paint you into a comer. If you
are asked for something (such as a copy of a competing offer), get something in retum. Often it is
better to bypass the HR contact and speak directly with the hiring manager.
At the end of the day, remember your long term career is what counts, and joining a company
that has a brighter future (social-mobile vs. legacy enterprise), or offers a position that has more
opportunities to rise (developer vs. tester) is much more important than a 1C_20% difference in
compensation.
18
```
