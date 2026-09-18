from build import sec, ask, src, box, table, kc, resp, score

P = 'p4'

intro = """
<p>Everything you can examine in a dataset is already in it. The file has no record of the people who are not in it, and no calculation on the rows that exist can tell you about them. This part is about how rows come to be in a file, and what that means for every number computed from the file.</p>
<p>Part 3 asked what a column measures. This part asks a question that comes before it: who are the rows, and why these rows rather than others. The two questions are separate. A column can be measured perfectly on a set of rows that were chosen in a way that makes the measurement useless for the decision in front of you.</p>
"""

s1 = sec('s1', '4.1', 'A blank cell and a missing person are different things', """
<p>The FuturePath Foundation file has 5,000 rows. The participant identifiers run from P0001 to P5000 without a gap, so nobody was removed after the file was built. The salary column has 3,088 blank cells, and counting them takes a few seconds in any tool.</p>
<p>Both checks are easy, and both answer a narrow question. A blank cell means that a value was not recorded for a row that exists. You can see the blank, count it, and ask why it is there. In this file the answer is that those 3,088 people were not employed, so there was no salary to record. The blank is what not having a job looks like when the column is salary.</p>
<p>There is no information in the file about a person who is not in it. There is no row to look at, no cell to count, and nothing in the data that shows the person was ever a candidate for a row. Three groups of people matter to FPF and never appear.</p>
""" + table(['Who never appears', 'Why it matters'], [
    ['People who considered FPF and did not enrol', 'This is the most useful thing FPF could know about its own recruiting, and the file contains nothing about it.'],
    ['People who enrolled and left before an outcome was recorded', 'Whether they are in the file at all depends on when the file was built and on a rule nobody wrote down.'],
    ['Employers that FPF approached and that declined', 'Partnership strength is measured only among the employers who agreed.'],
], txt=True) + """
<p>The check that takes seconds answers a question that does not matter much. The question that matters cannot be answered from inside the file. You have to find out how the file was built, and usually that means asking the people who built it.</p>
""" + ask('Who would have been in this file if things had gone differently, and what would it cost to find out about them?')
+ src('the in-class activity on who is not in the file; Reading Note 1 on what a dataset leaves out.'))

s2 = sec('s2', '4.2', 'Selection: the people in the file passed through a filter', """
<p>Among the 1,912 placed participants, the 215 from rural areas earn an average salary of 68,172. The 1,697 from urban areas earn an average of 62,503. The rural figure is higher by 5,669.</p>
<p>Suppose FPF reads this and decides to open a rural centre, so that rural learners no longer have to travel to a city to attend. It would be a mistake to expect the new rural learners to do as well as the rural learners in the file.</p>
<p>The reason is in how the current rural learners came to be in the file. Every one of them travelled to a city centre to attend, and paid for that in time, money and effort. Only some rural people were willing to pay that cost, so the cost decided who enrolled. The rural people who did enrol are not typical rural people. They are the ones with the most motivation, the most support at home, or the fewest other demands on their time. The file contains the people who passed the filter. It contains nothing about the people who did not.</p>
<p>Opening a rural centre removes the cost, and with it the filter. Once attending is easy, the rural learners who enrol will include the people the travel cost used to keep out. The average for the new learners will be closer to the average for rural people in general, and the file has no information about where that average is, because those people were never in it.</p>
<p>There is a second problem with the comparison, and it is a different one. A salary of 68,172 in a rural area and a salary of 62,503 in a city are not the same kind of number if living costs differ between the two places, and living costs are not in the file. That is a comparability problem, and it belongs to Part 3. The selection problem is separate. Even if the two salaries bought exactly the same things, the rural learners in the file would still be unusual rural people.</p>
<p>The general point is this. A row is in the file because something happened to put it there. Whatever that was, the people who ended up in the file may differ from the people who did not. Before using an average to predict what will happen when the process changes, ask whether the change also changes who gets into the file.</p>
""" + ask('What did a person have to do, or pay, or pass through, to become a row in this file, and would that still be true after the decision is made?')
+ src('the rural centre discussion in class; the in-class activity on comparing rural and urban salaries.'))

s3 = sec('s3', '4.3', 'Survivorship: cases that were resolved earlier never became rows', """
<p>Homework 3 gave you two support teams at Northgate Software. Team A handled retail customers and Team B handled enterprise customers. The contact summary looked like this.</p>
""" + table(['Team', 'Contacts received', 'Closed by the portal', 'Became tickets'], [
    ['Team A (retail)', '32', '0', '32'],
    ['Team B (enterprise)', '72', '40', '32'],
]) + """
<p>The self-service portal answers simple questions. So the contacts the portal closes are the simple ones, and the contacts that get past it and become tickets are the harder ones. Team B's tickets are not a fair sample of enterprise contacts. They are what remained after the easy cases were removed. Team A's tickets went through no such step.</p>
<p>Any comparison of the two teams on their tickets is therefore a comparison of all retail contacts against only the hard enterprise contacts. Team B looks slower and less successful in the ticket file. Part of that may be a real difference in the work, and part of it is the portal, and you cannot separate the two from the ticket file alone.</p>
<p>This is called survivorship bias. The name comes from situations where only the survivors of some process are available to study, and the cases that did not survive are not there to be counted. The mechanism is the same as in 4.2: some cases were removed before the file was built, and which cases were removed depended on the thing being measured.</p>
<p>The two situations differ in one useful way. In 4.2 the filter let unusual people in. Here the filter took ordinary cases out. In both cases the file describes a narrower group than its name suggests.</p>
""" + ask('Was there a step before this file where some cases were resolved, dropped or turned away, and were those cases like the ones that remain?')
+ src('Homework 3, the portal contacts and the honest answer; discussed again in class alongside the rural centre.'))

s4 = sec('s4', '4.4', 'A filter can be evidence', """
<p>A filter is not only a problem. Sometimes knowing what filter a person passed through is the most useful information you have about them.</p>
<p>An employer wants to hire someone with strong motivation and a real commitment to the work. Motivation cannot be observed directly. Every applicant says they are motivated, so asking does not separate them. A degree in a relevant field costs years of sustained effort, and someone who holds one has shown that they were willing and able to pay that cost. The degree does not measure motivation. It is evidence of motivation, because of what it cost to obtain.</p>
<p>Economists call this signalling. A signal is something that is costly to produce, and more costly for people who lack the quality than for people who have it, so that having produced it is informative. The reasoning works in one direction only. The presence of the degree suggests commitment. The absence of a degree does not show a lack of it, because there are many reasons a committed person might not have one.</p>
<p>The same reasoning applies to data. A column that records something costly that a person did is better evidence than a column that records a claim anyone could make. Attendance taken from a register is better evidence than attendance reported by the learner. And the filter in 4.2 can be read the other way round. The fact that a rural learner is in the file at all is evidence about that learner, and it is evidence precisely because the file is not representative of rural people in general.</p>
<p>The two effects of a filter go together. The filter makes the file unrepresentative of the wider group, which limits what you can conclude about that group from the file. The same filter makes membership of the file informative about each person in it, which is something you can conclude from the file.</p>
""" + ask('What did producing this value cost the person, and does that cost tell me something the value itself does not?')
+ src('the signalling discussion in class, following the rural centre example.'))

s5 = sec('s5', '4.5', 'Every number in this file describes people who enrolled and completed', """
<p>Take the four sections together. The FPF file holds 5,000 people. All of them chose to enrol. All of them attended enough to have an attendance figure. All of them were still in contact when employment was recorded. The file was built from the people who completed that process.</p>
<p>So every number computed from it describes that group. The placement rate of 38.24 percent is the placement rate of completers. The mentorship comparison in Part 2 compares mentored completers with unmentored completers. The file has no record of what happened to people who enrolled and stopped attending, and none of what would have happened to people who never enrolled.</p>
<p>This does not make the numbers wrong. It makes them narrower than they look. A report that says 38 percent of participants were placed means, without saying so, that 38 percent of the participants who completed and stayed in touch were placed. Whether the narrowing matters depends on the decision. For a funder asking whether completing the programme goes with finding work, it may not matter. For a board deciding whether to recruit from a population FPF has not served before, it matters a great deal, because that population has not been through the filter.</p>
<p>The habit to form is to state the denominator, and then to state how the denominator came to be. Part 3 covers the first half. This part is the second half.</p>
""" + ask('Which process produced these rows, and does the decision in front of me apply to people who have been through that process, or to people who have not?')
+ src('the in-class activity on who is not in the file; Reading Note 1.'))

practice = """
<section id="practice">
<h2><span class="n">Practice</span>Check yourself</h2>
<p>Six questions that mark themselves, then three to write out.</p>
""" + kc(P, 1,
   'A dataset has 3,088 blank cells in one column and no gaps in its identifier sequence. What does the identifier check establish?',
   ['That no participant was removed after the file was built',
    'That the file includes everyone who applied to the programme',
    'That the blank cells can safely be filled with zero',
    'That every participant reached the end of the programme'],
   0, 'An unbroken identifier sequence shows that nothing was deleted from the file. It does not show who never entered it.') \
+ kc(P, 2,
   'Rural learners in the file earn 5,669 more on average than urban learners. FPF opens a rural centre so that rural learners no longer need to travel. Why should FPF not expect the same result from the new learners?',
   ['Rural salaries are lower once living costs are taken into account',
    'The travel cost let in unusually motivated rural learners',
    'The 215 rural placements are too few to compute an average from',
    'A new centre will take several years to reach the same standard'],
   1, 'The rural learners in the file paid the travel cost. Removing the cost admits the people it used to keep out, and the file contains nothing about them.') \
+ kc(P, 3,
   'Team B resolved tickets more slowly than Team A. Forty of Team B\'s contacts were closed by a portal before becoming tickets. What does the portal do to the comparison?',
   ['It removes the easy enterprise cases, so Team B\'s tickets are the hard ones',
    'It reduces Team B\'s ticket count, so its averages are less reliable',
    'It has no effect, because the portal contacts never became tickets',
    'It makes Team B look better by leaving out the contacts that failed'],
   0, 'The portal answers simple questions. What gets past it is harder than what Team A receives, so the ticket file compares unlike work.') \
+ kc(P, 4,
   'An employer treats a degree as evidence of motivation, although motivation was never measured. What does that reasoning rest on?',
   ['Degree holders report higher motivation when surveyed',
    'Motivation and the degree are recorded in the same file',
    'The degree was costly to obtain and hard to fake',
    'Employers have no other information about applicants'],
   2, 'The degree is evidence because it was costly to obtain. A claim that costs nothing to make is not.') \
+ kc(P, 5,
   'Which of the following can the FPF file tell you?',
   ['How many people considered enrolling and decided against it',
    'How many enrolled participants left before an outcome was recorded',
    'How many employers declined a partnership with FPF',
    'How many placed participants were placed in full-time work'],
   3, 'The first three groups never became rows. The fourth is a count within the rows that exist.') \
+ kc(P, 6,
   'A report says that 38 percent of participants were placed. Which decision does that figure describe well?',
   ['Whether to recruit from a population FPF has not served before',
    'Whether completing the programme goes with finding work',
    'Whether people who left early would have been placed',
    'Whether the programme changes outcomes for typical rural residents'],
   1, 'The figure describes completers. The other three decisions concern people who did not pass through that process.') \
+ score() + """
<h3>Write it out</h3>
<p>There is no single correct answer to these. Write yours first, then compare.</p>
""" + resp(
   'FPF wants to know whether its recruiting is working. Name one group of people the file cannot see, say why that group matters to the question, and describe one way of finding out about them and what it would cost.',
   'People who enquired or applied and did not enrol. Recruiting is about turning interest into enrolment, and the file begins at enrolment, so there is no way to measure that conversion from it. FPF could record every enquiry with a few fields at first contact, then follow up by phone or email with a sample of those who did not enrol. The cost in money is small. The cost in process is larger: someone has to record enquiries consistently, and the follow-up will reach only some of the people, who will themselves be the ones willing to answer.') \
+ resp(
   'Northgate removes the portal, so every enterprise contact becomes a ticket. Describe what happens to Team B\'s resolution figures in the next quarter and why, and say whether the team\'s work has changed.',
   'Team B\'s figures improve. The easy contacts the portal used to close now become tickets, so the average ticket is easier, and the share resolved within the service level rises. The team\'s work has not changed. Each hard ticket takes as long as it did before. The number changed because the filter changed. Anyone comparing the two quarters without knowing the portal was removed would conclude that the team improved.') \
+ resp(
   'A new column records whether a learner attended an optional evening session. Argue that this column is better evidence of engagement than the attendance percentage. Then argue that it is worse.',
   'Better: the evening session was optional and cost the learner an evening, so attending it is a costly signal of engagement in a way that ordinary attendance, which is expected, is not. Worse: it is a single yes or no for one occasion, so it measures one evening rather than a term, and it also filters by circumstance. Learners with shift work or caring duties could not attend whatever their engagement, so the column mixes engagement with availability. Which argument wins depends on who the column will be used to describe.') + """
</section>
"""

PAGE = {
    'file': 'part4.html', 'nav': 'part4',
    'title': 'Part 4. Who is in the file', 'sub': 'Part 4',
    'dek': 'What filtered these rows, and what does the number mean as a result?',
    'toc': [('s1', '4.1 A blank cell and a missing person'), ('s2', '4.2 Selection'),
            ('s3', '4.3 Survivorship'), ('s4', '4.4 A filter can be evidence'),
            ('s5', '4.5 Everyone here enrolled and completed'), ('practice', 'Practice')],
    'body': intro + s1 + s2 + s3 + s4 + s5 + practice,
    'prev': ('part3.html', 'Part 3. What a column measures'),
    'next': ('part5.html', 'Part 5. Summarising, and what it costs'),
}
