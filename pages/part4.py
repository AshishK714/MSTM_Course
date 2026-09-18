from build import sec, ask, src, box, table, kc, resp, score, case

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
    ['People who enrolled and left before an outcome was recorded', 'They are not rows: the file holds only participants who were still in contact when employment was recorded. What became of them is not recoverable from it.'],
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
<p>The ticket file bears this out. Team A resolved 71.9 percent of its tickets within the service level and Team B 65.6 percent, so on the headline figure Team A looks better. Any comparison of the two on their tickets is a comparison of all retail contacts against only the hard enterprise contacts. Part of the 6.3 point gap may be a real difference in the work, and part of it is the portal, and you cannot separate the two from the ticket file alone.</p>
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
<p>All the questions below are worked from one situation. Read it once, then answer with the table in front of you.</p>
""" + case('The situation', [
    'FPF is deciding where to put next year&#39;s recruitment budget. Rural participants currently travel to a city centre to attend, and the board is considering opening a centre in a rural district so that they no longer have to. The director has given you this from the file of 5,000 enrolled participants.',
], table(['', 'Enrolled', 'Placed', 'Placement rate', 'Mean salary of those placed'], [
    ['Rural', '518', '215', '41.51%', '68,172'],
    ['Urban', '4,482', '1,697', '37.86%', '62,503'],
    ['All', '5,000', '1,912', '38.24%', '63,140'],
]) + '<p>Three other facts are in the file. The participant identifiers run from P0001 to P5000 with no gaps. The salary column is blank for exactly the 3,088 participants who were not employed. Every participant in the file enrolled, attended enough to have an attendance figure, and was still in contact when employment was recorded.</p>') + """
<p>Six questions that mark themselves, then three to write out.</p>
""" + kc(P, 1,
   'A board member reads the table and proposes opening the rural centre, on the ground that rural participants do better on both measures. What is the strongest objection?',
   ['Rural participants in the file are those who paid the travel cost',
    'The rural figures are computed from 518 people and 215 placements',
    'The two mean salaries are not adjusted for differences in living costs',
    'A placement rate and a mean salary should not be read together'],
   0, 'Travelling to a city cost time and money, so only some rural people were willing to pay it. If the cost is removed, rural people who were unwilling to pay it will enrol, and the file has no record of them. B is a real caution, and it appears in the model answer below, but 518 enrolments and 215 placements are enough to compare. C and D are about how the figures should be read, not about who is in the file.',
   ['The 518 rural rows passed a filter, and the centre removes that filter, so their rates do not carry to a new intake.',
    'A real caution, and it appears in the model answer below, but 518 enrolments and 215 placements are enough to compare.',
    'A genuine caveat on the salary column, and it leaves the placement rate untouched, so it is not the strongest objection.',
    'There is no such rule. Both figures were computed on stated bases.']) \
+ kc(P, 2,
   'The identifiers run from P0001 to P5000 with no gaps. What does checking that establish?',
   ['That the 5,000 are representative of the district FPF serves',
    'That nobody was removed from the file after it was built',
    'That everybody who applied to the programme has a row',
    'That the rural and urban groups can be compared directly'],
   1, 'If the sequence is unbroken, no row was deleted after the file was built. That is all you learn, and you learn nothing about who never entered it.',
   ['From complete identifiers you learn nothing about who enrolled in the first place.',
    'If the sequence is unbroken, no row was deleted after the file was assembled, and that is all you learn.',
    'The file is of people who enrolled. Anybody who applied and did not enrol was never given an identifier.',
    'Identifier integrity has no bearing on whether two self-selected groups are comparable.']) \
+ kc(P, 3,
   'Which of these could you find out from this file?',
   ['How many rural people considered FPF and did not enrol',
    'How many people enrolled but dropped out before the file was built',
    'How many rural participants enrolled and were not placed',
    'How rural people who never travelled to a centre would do'],
   2, 'The first, second and fourth describe people who are not rows at all, and somebody who dropped out before the file was built was never given a row to count. The third is a subtraction inside the table, 518 less 215, which is 303.',
   ['They have no rows, and nothing in the file records that they existed.',
    'Somebody who dropped out before the file was built was never given a row to count.',
    '518 less 215, which is 303, read straight off the table.',
    'A counterfactual about people the file excludes by construction.']) \
+ kc(P, 4,
   'The 3,088 blank cells in the salary column took seconds to count. What does that check fail to establish?',
   ['How many of the 5,000 participants have no salary recorded',
    'What share of the 5,000 the blank cells are',
    'That all 3,088 blanks are in the salary column',
    'Anything about the people who are not in the file at all'],
   3, 'Counting the blanks gives you A and B directly, 3,088 and 61.76 percent, and C as well, since you counted them in that one column. A blank cell means there was no job to report, and blank cells can be counted. The file has no record of the people who are not in it, and that is the harder question.',
   ['Counting the blank cells gives this directly: there are 3,088 of them.',
    'This follows from the same count: 3,088 out of 5,000 is 61.76 percent.',
    'This follows too, since the blanks were counted in the salary column and nowhere else.',
    'Nothing counted inside a file bears on who is outside it, and that is the harder question.']) \
+ kc(P, 5,
   'Suppose the rural centre opens and the rural placement rate falls to 36 percent in the following year. What is the most defensible reading?',
   ['The centre made rural participants worse off than they were before',
    'The new rural intake includes people the travel cost kept out',
    'The 41.51 percent must have been computed incorrectly',
    'Rural recruitment should be reduced back to its old level'],
   1, 'The number changed because the filter changed. The work of the programme need not have changed at all, and the two years describe different groups of rural people.',
   ["Nobody's outcome is shown to have worsened. What changed is who now enrols.",
    'The number changed because the filter changed, and the two years describe different groups of rural people.',
    '215 of 518 is 41.51 percent. The arithmetic was never in doubt.',
    'A recommendation built on the same misreading as A.']) \
+ kc(P, 6,
   'An employer tells FPF it prefers participants who travelled to attend, because the travel shows commitment. Is that reasoning sound?',
   ['No, because commitment is a feeling and only a self-report can measure it',
    'No, because asking the applicant directly would give the same information',
    'Yes, because travelling was costly and hard to fake',
    'Yes, because travelling participants were placed more often than they otherwise would be'],
   2, 'A costly action is evidence, because someone unwilling to pay the cost would not have taken it. The reasoning runs one way only: travelling suggests commitment, and not travelling does not show a lack of it. A and B both have it backwards: a self-report is the cheap thing anyone can produce, which is exactly why asking does not separate applicants. D is a claim about what the travel did to the outcome, which this file cannot establish.',
   ['This has it backwards. A self-report is the cheap thing anyone can produce.',
    'Asking fails for the same reason. Every applicant says they are committed.',
    'Somebody unwilling to pay the cost would not have travelled, so having travelled is informative.',
    'A claim about what the travel did to the outcome, which this file cannot establish.']) \
+ score() + """
<h3>Write it out</h3>
<p>The same situation. There is no single correct answer to these. Write yours first, then compare.</p>
""" + resp(
   'Write the note you would send the board about the rural centre. Say what the table does support, what it does not, and what you would want to know before the decision is made.',
   'The table supports one claim: among the people who enrolled, the 518 rural participants were placed more often than the 4,482 urban ones and the 215 placed rural participants earned more on average. It does not support the claim that a rural centre will produce those figures. Every rural participant in the file travelled to a city to attend, so the file describes rural people who were willing and able to pay that cost. With a centre there is no travel cost, so rural people who previously did not enrol will, and the file has no record of them. Two further cautions: the salary comparison assumes 68,172 in a rural area and 62,503 in a city buy the same things, and living costs are not recorded; and the placement rates are computed from 215 rural placements. Before deciding I would want the enquiry records for the rural district, so we know how many rural people considered enrolling and did not, and I would want a figure for what rural people earn locally without the programme.') \
+ resp(
   'A funder asks why FPF cannot simply report the outcomes of everybody it has ever recruited. Answer in the terms of this part, and say what FPF would have to change to be able to do it.',
   'The file begins at enrolment and ends at a recorded outcome, so it holds people who enrolled, attended and were still in contact when employment was recorded. Anyone who enquired and did not enrol was never a row. Anyone who left before an outcome was recorded is not a row either, because the file holds only participants who were still in contact at that point. So every figure FPF reports, including 38.24 percent, describes the people who enrolled, attended and stayed in contact, and reporting it as the outcome for everybody recruited would overstate what enrolling does for a typical enquirer. To be able to answer the question FPF would have to record every enquiry at first contact with a few fields, record a leaving date and reason for anyone who stops attending, and write down the rule that decides who enters the file. It would cost little money. The work is the difficulty, because somebody has to record enquiries consistently and follow up people who have already declined.') \
+ resp(
   'Northgate Software&#39;s self-service portal closed 40 of Team B&#39;s 72 enterprise contacts before they became tickets, while none of Team A&#39;s 32 retail contacts met a portal. Explain what that does to a comparison of the two teams, and say which mechanism from this part it is.',
   'The portal answers simple questions, so the contacts it closes are the simple ones and the contacts it does not close are the harder ones. Team B&#39;s 32 tickets are what remained after the easy cases were removed, while Team A&#39;s 32 tickets went through no such step. Comparing the two on their tickets therefore compares all retail contacts against only the hard enterprise contacts, and Team B will look slower whether or not it is. This is survivorship: cases were removed before the file was built, and which cases were removed depended on the thing being measured. It is the same mechanism as the rural travel cost, with the direction reversed. Because of the travel cost, only unusual rural people enrolled. Because of the portal, only the harder enterprise contacts became tickets. In both, the file is named after a wider group than the one it contains.') + """
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
