# Chapter 3: Conducting An Interview

**Starts at printed page 19.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 19

```text
CrIaprrn
Conducting An Interview
me*E't[ 'EHnTtf,.
Tianslated-"If you know both yourself and your en-
emy, you can win numerous battles without jeopardy,"
- 
"The Art of War,"
Sur.r Tzu,5L5 B.C.
In this chapter we review practices that help interviewers identify a top hire. We strongly rec-
ommend interviewees read it-knowing what an interviewer is looking for will help you present
yourself better and increase the likelihood of a successful outcome.
For someone at the beginning of their career, interviewing may feel like a huge responsibility.
Hiring a bad candidate is expensive for the organization, not just because the hire is unproductive,
but also because he is a drain on the productivity of his mentors and managers, and sets a bad
example. Firing someone is extremely painful as well as bad for to the morale of the team. On
the other hand, discarding good candidates is problematic for a rapidly growing organization.
Interviewers also have a moral responsibility not to unfairly crush the interviewee's dreams and
aspirations.
Objectiae
The ultimate goal of any interview is to determine the odds that a candidate will be a successful
employee of the company. The ideal candidate is smart, dedicated, articulate, collegial, and gets
things done quickly, both as an individual and in a team. Ideally, your interviews should be
designed such that a good candidate scores 1.0 and a bad candidate scores 0.0.
One mistake, frequently made by novice interviewers, is to be indecisive. Unless the candidate
walks on water or completely disappoints, the interviewer tries not to make a decision and scores
the candidate somewhere in the middle. This means that the interview was a wasted effort.
A secondary objective of the interview process is to turn the candidate into a brand ambassador
for the recruiting organization. Even if a candidate is not a good fit for the organization, he may
know others who would be. It is important for the candidate to have an overall positive experience
during the process. It seems obvious that it is a bad idea for an interviewer to check email while
the candidate is talking or insult the candidate over a mistake he made, but such behavior is
depressingly common. Outside of a stress interview, the interviewer should work on making the
candidate feel positively about the experience, and, by extension, the position and the company.
19
```

### Printed page 20

```text
What to ask
One important question you should ask yourself as an interviewer is how much training time your
work environment allows. For a startup it is important that a new hire is productive from the first
week, whereas a larger organization can budget for several months of training. Consequently, in a
startup it is important to test the candidate on the specific technologies that he will use, in addition
to his general abilities.
For a larger organization, it is reasonable not to emphasize domain knowledge and instead test
candidates on data structures, algorithms, system design skills, and problem solving techniques.
The justification for this is as follows. Algorithms, data structures, and system design underlie all
software. Algorithms and data structure code is usually a small component of a system dominated
by the user interface (UI), input/output (VO), and format conversion. It is often hidden in library
calls. However, such code is usually the crucial component in terms of performance and correctness,
and often serves to differentiate products. Furthermore, platforms and programming languages
change quickly but a firm grasp of data structures, algorithms, and system design principles, will
always be a foundational part of any successful software endeavor. Finally, many of the most
successful software companies have hired based on ability and potential rather than experience or
knowledge of specifics, underlying the effectiveness of this approach to selecting candidates.
Most big organizations have a structured interview process where designated interviewers are
responsible for probing specific areas. For example, you may be asked to evaluate the candidate on
their coding skills, algorithm knowledge, critical thinking, or the ability to design complex systems.
This book gives interviewers access to a fairly large collection of problems to choose from. lvVhen
selecting a problem keep the following in mind:
No single point of failure-if you are going to ask just one question, you should not pick a
problem where the candidate passes the interview if and only if he gets one particular insight. The
best candidate may miss a simple insight, and a mediocre candidate may stumble across the right
idea. There should be at least two or three opportunities for the candidates to redeem themselves.
For example, problems that can be solved by dynamic programming can almost always be solved
through a grcedy algorithm that is fast but suboptimum or a brute-force algorithm that is slow but
optimum. br such cases, even if the candidate cannot get the key insight, he can still demonstrate
some problem solving abilities. Problem 5.6 on Page 46 exemplifies this type of question.
Multiple possible solutions-if a given problem has multiple solutions, the chances of a good
candidate coming up with a solution increases. It also gives the interviewer more freedom to steer
the candidate. A great candidate may finish with one solution quickly enough to discuss other
approaches and the trade-offs between them. For example, Problem 11.9 on Page 155 can be solved
using a hash table or a bit array; the best solution makes use of binary search.
Cover multiple areas---even if you are responsible for testing the candidate on algorithms, you
could easily pick a problem that also exposes some aspects of design and software development.
For example, Problem 19.8 on Page298 tests candidates on concurrency as well as data structures.
Problem 5.16 on Page 58 requires knowledge of both probability and binary search.
Calibrate on colleagues-interviewers often have an incorrect notion of how difficult a problem
is for a thirty minute or one hour interview. It is a good idea to check the appropriateness of a
problem by asking one of your colleagues to solve it and seeing how much difficulty they have with
20
```

### Printed page 21

```text
it.
No unnecessary domain knowledge-it is not a good idea to quiz a candidate on advanced
SaPh algorithms if the job does not require it and the candidate does not claim any special knowl-
edge of the field. (The exception to this rule is if you want to test the candidate's response to
stress.)
C onducting the intentiew
Conducting a good interview is akin to juggling. At a high level, you want to ask your questions
and evaluate the candidate's responses. Many things can happen in an interview that could help
you reach a decision, so it is important to take notes. At the same time, it is important to keep a
conversation going with the candidate and help him out if he gets stuck. Ideally, have a series of
hints worked out beforehand, which can then be provided progressively as needed. Coming up
with the right set of hints may require some thinking. You do not want to give away the problem,
yet find a way for the candidate to make progress. Here are situations that may throw you off:
A candidate that gets stuck and shuts up: Some candidates get intimidated by the problem, the
Process/ or the interviewer, and just shut up. In such situations, a candidate's performance does
not reflect his true caliber. It is important to put the candidate at ease, e.g.,by beginning with a
straightforward question, mentioning that a problem is tough, or asking them to think out loud.
A verbose candidate: Candidates who go off on tangents and keep on talking without making
Progress render an interview ineffective. Again, it is important to take control of the conversation.
For example you could assert that a particular path will not make progress.
An overconfident candidate: It is common to meet candidates who weaken their case by
defending an incorrect answer. To give the candidate a fair chance, it is important to demonstrate
to him that he is making a mistake, and allow him to correct it. Often the best way of doing this is
to construct a test case where the candidate's solution breaks down.
Scoring anil rcporting
At the end of an interview, the interviewers usually have a good idea of how the candidate scored.
However, it is important to keep notes and revisit thembefore making a final decision. Whiteboard
snapshots and samples of any code that the candidate wrote should also be recorded. You should
standardize scoring based on which hints were given, how many questions the candidate was able
to get to, etc. Although isolated minor mistakes can be ignored, sometimes when you look at all the
mistakes togethe4 clear signs of weakness in certain areas may emerge, such as a lack of attention
to detail and unfamiliarity with a language.
\Alhen the right choice is not clear, wait for the next candidate instead of possibly making a bad
hiring decision. The litmus test is to see if you would react positively to the candidate replacing a
valuable member of your team.
21
```

### Printed page 22

```text
Part ll
Data Structures and Algorithms
```
