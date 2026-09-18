from build import sec, ask, src, box, table, kc, resp, score, lost, case

P = 'p1'

intro = """
<p>An organisation acts on the world long before it analyses anything. FPF recruits participants, runs training, arranges mentorship, approaches employers and reports to funders, and all of that happens whether or not anybody opens a file afterwards. The file exists because somebody decided which parts of that activity were worth recording.</p>
<p>So a dataset is a selective record of real activity, kept for a purpose, at one level of detail, and it is smaller than the programme it records. Everything in Parts 2 to 5 follows from that, and this part is about the step before any of it: knowing which decision you are serving, and what job each column is doing for that decision.</p>
"""

s1 = sec('s1', '1.1', 'A programme converts activities into outcomes', """
<p>FPF pulls levers. It recruits, it delivers technical and soft-skills training, it provides mentorship and career counselling, it runs mock interviews and job-readiness workshops, it builds employer partnerships, it places people in work and it reports to funders. Those are the things it can choose to do more or less of.</p>
<p>Everything else around them has a different job. The five roles used in Homework 1 are a way of sorting them.</p>
""" + table(['Role', 'What it is', 'An FPF example'], [
    ['Activity', 'the work the organisation does, and the lever it can pull', 'running a mock-interview workshop'],
    ['Signal', 'what you watch instead of the outcome, because the outcome arrives too late to steer by', 'the share of enrolled participants who finish'],
    ['Outcome', 'what the organisation exists to produce, wanted for its own sake', 'a graduate moving into a better role two years on'],
    ['Context', 'what shapes the result and cannot be moved within the planning horizon', 'whether a participant has childcare available'],
    ['Mechanism', 'what has to happen inside a person between the activity and the result', 'coming to believe the qualification is worth finishing'],
], txt=True) + """
<p>Sorting them decides what you will act on, what you will watch, and what you will have to work around.</p>
<p>One condition applies throughout, and it was put in class as the definition of the subject: analytics is the study of variation and co-variation. To learn anything about a lever you need the lever to vary and the outcome to vary. If every participant received the same training there is nothing to compare training against, and if every participant ended up in the same job there is nothing to explain. Part 2 is what happens when that condition fails inside a real file.</p>
""" + ask('Which of the five is this item, and for whose decision am I sorting it?')
+ src('Homework 1 and the five roles sheet issued with it; the in-class mapping of FPF activities and measures. Reading Note 1, section 1, is behind the opening of this part.'))

s2 = sec('s2', '1.2', 'Signal and outcome', """
<p>One question settles whether something is a signal or an outcome.</p>
""" + box('The question', ['Do you care about this on its own? If yes, it is an outcome: you want it whether or not it leads to anything else. If no, it is a signal: it stands in for something else, which means it can be pushed up while the thing it stands for gets no better.'], 'principle') + """
<p>Take two items from Homework 1. Employer feedback on graduate readiness is a signal. FPF does not exist to collect good feedback; it collects it because good feedback from employers is the earliest sign that interviews and offers will follow. Community trust in FPF is harder, and it is one of the items Homework 1 expects students to find a close call. A funder may treat it as a signal, because people who trust FPF enrol. The organisation may treat it as an outcome, because a body that exists to serve a community and is not trusted by it has failed at something it cares about directly.</p>
<p>The answer depends on who is asking, and both readings can be defended. Asking the question is what matters.</p>
<p>The reason it is worth the trouble is what happens when a signal is used as a target. A completion rate can be raised by making the course easier, and the number will rise while the thing it was standing in for gets no better. Part 3 takes up what that does to a measure.</p>
""" + ask('Would I still want this if it led to nothing else?')
+ src('Homework 1, items 11 and 15, and the one-question test on the five roles sheet.'))

s3 = sec('s3', '1.3', 'A role is not a property of a column', """
<p>The same item plays different roles depending on who is looking, and Homework 1 was built around that. Participant satisfaction is a signal to somebody running the programme and closer to an outcome for the participant feeling it. An economic downturn is context for FPF and the outcome a regional funder is judged on.</p>
<p>The same is true inside a file. Take attendance_pct in the FPF data. Ask what average attendance was, and the answer is 93.13 percent: the column is the thing being measured. Now ask whether participants who attended more were placed more often. To answer that you sort participants into higher and lower attenders and compare placement between the two groups. The column is now the thing you are slicing by, and placement is what is being measured.</p>
<p>Nothing about the column changed. The values are identical in both questions. What changed is the question, and with it the job the column is doing.</p>
<p>This is why a column cannot be labelled once and filed. The label belongs to the pairing of a column with a decision, and if three decision-makers work from one file, the same columns are labelled three different ways.</p>
""" + ask('What job is this column doing in this question, and would it change job in the next one?')
+ src('Homework 1, question 2, on how a role changes with perspective; the in-class treatment of attendance as a fact and then as a dimension; Reading Note 3, section 2.'))

s4 = sec('s4', '1.4', 'Facts and dimensions', """
<p>Inside a table the same distinction has a working name. Facts are the measured quantities the decision is about, recorded at one grain, which is what one row stands for. Dimensions are the descriptive context you slice those facts by.</p>
""" + table(['In the FPF file', 'Columns'], [
    ['Facts', 'employed, salary, attendance_pct, digital_lit_score'],
    ['Dimensions', 'track, education, gender, mentorship, location_category, employer_partnership_strength'],
], txt=True) + """
<p>The rule that follows is about what may be added. Facts add: two salaries make a total, two placements make a count. Dimensions do not: adding a track to an education level produces nothing. Ratios and rates were already divided once, and adding two of them gives a number whose denominator is nobody's, which is why a rate is a fact you may not total.</p>
<p>Partnership strength needs care. Its levels are ordered from very low to very high, so it can be put in order, and being able to rank it does not make the steps between its levels equal. Two further columns, employment type and sector, were recorded only for participants who were employed, so those blanks follow from the value in another column rather than from anything going wrong.</p>
<p>Both of those are taken further in Part 3. What belongs here is the habit of asking, of any column, whether it is the thing being measured or the thing you are cutting by, because the answer decides what arithmetic is allowed on it.</p>
""" + ask('Is this column the thing being measured, or the thing I am cutting by, and what does that permit?')
+ src('the in-class table of facts and dimensions in the FPF file; Reading Note 3, section 2. Part 3 covers ordered categories and structural blanks.'))

practice = """
<section id="practice">
<h2><span class="n">Practice</span>Check yourself</h2>
<p>All the questions below are worked from one situation. Read it once, then answer with the list in front of you.</p>
""" + case('The situation', [
    'FPF has two decisions to make this month and one file to make them from. The first is operational: how much mentorship to fund next year, and for whom. The second is a reporting decision: the annual report will give the placement rate and the average salary of those placed, broken down by education, and nothing else.',
    'Eight items are available.',
], table(['Item', 'What it records'], [
    ['mentorship', 'whether the participant was assigned a mentor'],
    ['attendance_pct', 'the share of sessions the participant attended'],
    ['employed', 'whether the participant was in work when the outcome was recorded'],
    ['salary', 'what the employed participant was paid'],
    ['education', 'highest level of education at enrolment'],
    ['location_category', 'rural or urban'],
    ['employer_partnership_strength', 'how strong the partnership with the employer is, from very low to very high'],
    ['Regional unemployment', 'not in the file; published quarterly by the government'],
], txt=True)) + """
<p>Six questions that mark themselves, then three to write out.</p>
""" + kc(P, 1,
   'For the mentorship decision, which role does mentorship play?',
   ['An activity, because it is the lever FPF can choose to pull',
    'A signal, because it is watched instead of the real outcome',
    'An outcome, because FPF exists to provide mentorship to people',
    'Context, because it was settled before the participant enrolled'],
   0, 'FPF decides who receives mentorship, so it is the lever. It is not something watched in place of an outcome, and it is not fixed before enrolment. FPF does not exist to provide mentorship either; it provides mentorship so that participants find work. Part 2 follows the same decision into the file.',
   ['FPF chooses who receives mentorship, so it is the thing FPF can do more or less of.',
    'A signal is watched in place of an outcome that arrives too late. Nobody watches mentorship to find out how the programme is doing; FPF sets it.',
    'FPF does not exist to produce mentorship. It provides mentorship so that participants find work, so it fails the one-question test.',
    'Mentorship is assigned during the programme, and it is the one thing in this decision FPF can move.']) \
+ kc(P, 2,
   'Regional unemployment is published quarterly and is not in the file. What is it for the mentorship decision?',
   ['A signal, because it can be watched every quarter',
    'An outcome, because reducing it is what FPF exists to do',
    'Context, because it shapes the result and FPF cannot move it',
    'Irrelevant, because a decision can only use what is in the file'],
   2, 'FPF cannot move regional unemployment within its planning horizon, and it shapes how many participants find work whatever the programme does. Something can be watched every quarter without being a signal, because a signal stands in for an outcome FPF is trying to produce. And a decision may use anything that bears on it, whether or not it was recorded in the file.',
   ['Being published every quarter makes it easy to watch. A signal has to stand in for an outcome FPF is trying to produce, and this does not.',
    'FPF places its own participants. It could not move the regional rate at its size, and nobody funds it to.',
    'It shapes how many participants find work, and FPF cannot change it within a year.',
    'A decision may use anything that bears on it. Being outside the file makes a figure harder to get, not irrelevant.']) \
+ kc(P, 3,
   'Apply the one-question test to attendance_pct. Which is right?',
   ['An outcome, because attending is worth having for its own sake',
    'A signal, because nobody wants attendance if it leads nowhere',
    'A fact for one decision and an outcome for the other',
    'Neither, because it is recorded as a percentage rather than a count'],
   1, 'Nobody runs a programme in order to produce attendance, so it fails the one-question test and is not an outcome. It is watched because it is meant to stand in for engagement, which is what Part 3 examines. It is a fact in the table, but that is a separate question from the role it plays. The unit makes no difference either, because the one-question test asks what you want the item for, not how it was recorded.',
   ['Nobody funds a programme in order to produce attendance, so it fails the one-question test.',
    'It is watched early because the outcome, a job, arrives months later.',
    "Attendance is a fact in both decisions, and an outcome in neither. The reporting decision's outcomes are placement and salary.",
    'How a value was recorded has no bearing on the role it plays. A count and a percentage can each be a signal.']) \
+ kc(P, 4,
   'In one internal memo, FPF writes that average attendance was 93.13 percent. In a second memo it compares placement between higher and lower attenders. What has happened to attendance_pct?',
   ['It has been used first as a fact, then as a dimension',
    'It has been used incorrectly in one of the two places',
    'It has changed from a signal into an outcome between them',
    'It has been recorded more finely, changing from banded to continuous'],
   0, 'The values never changed, and nothing was re-recorded, so D has the direction backwards: splitting into higher and lower attenders is coarser, not finer. In the first use the column is the thing being measured; in the second it is the thing being sliced by. Both uses are legitimate, and the role it plays for the decision, signal rather than outcome, is the same in both.',
   ['The same values are reported in one memo and used to split participants in the other.',
    'Both uses are legitimate. That is the point: the role belongs to the pairing of column and question.',
    'Placement is the outcome in both memos. Nothing about attendance moved between signal and outcome.',
    'This has the direction backwards. Splitting into higher and lower attenders is coarser than the percentage, not finer, and nothing was re-recorded.']) \
+ kc(P, 5,
   'Which of these four can be added up across participants without producing a meaningless number?',
   ['employer_partnership_strength, once its levels are coded 1 to 4',
    'attendance_pct, because every value is on the same percentage scale',
    'location_category, by coding rural as one and urban as two and adding the codes',
    'salary, because two salaries together make a wage bill'],
   3, 'Salary totals to something real. A rate cannot be totalled, an ordered category has no equal steps, and adding arbitrary codes for rural and urban gives a number that counts nothing.',
   ['Its levels are ordered, so they can be ranked, and nothing establishes that the step from low to high is the same size as the step from high to very high.',
    "A percentage was already divided once. Adding two of them gives a number whose denominator is nobody's.",
    'Rural and urban have no order, so codes of one and two are arbitrary and their total counts nothing.',
    'Salary is an amount on a common scale with a real zero, so two of them add to a third amount that means something.']) \
+ kc(P, 6,
   'FPF switches from the mentorship decision to the reporting decision. Which of these items now does no work?',
   ['salary, because funders are not told what participants earn',
    'education, because the report is not broken down by education',
    'mentorship, because the report is not broken down by who was mentored',
    'None of them; both decisions need all eight items'],
   2, 'The report is broken down by education and by nothing else, so it never compares the mentored with the unmentored. Salary and education are both in it. For the mentorship decision, mentorship is the whole point.',
   ['Average salary of those placed is one of the two figures the report gives.',
    'The report is broken down by education, so education is the dimension it slices by.',
    'The report gives placement rate and average salary by education, and nothing else, so it never compares the mentored with the unmentored.',
    'Five of the eight do no work in the report. Mentorship is the one that was the whole point of the other decision.']) \
+ score() + """
<h3>Write it out</h3>
<p>The same situation. There is no single correct answer to these. Write yours first, then compare.</p>
""" + resp(
   'Four items from Homework 1, which are not in the file. Sort them into the five roles, and give a reason for each that is not a restatement of the item: number of employers offering interviews; participants gaining technical AI skills; social norms discouraging rural women from enrolling; employment stability at one year.',
   'Number of employers offering interviews is a signal. FPF does not exist to generate interviews, and the number can be raised by approaching more employers of lower quality, which is exactly what a signal allows someone to do. Participants gaining technical AI skills is a mechanism. It is what has to happen inside a person between the training and the job, and it is wanted because of what it leads to rather than for itself, although a participant might reasonably call it an outcome. Social norms discouraging rural women from enrolling is context. It shapes who enrols and FPF cannot change it in a year, though it could work around it by changing where it recruits. Employment stability at one year is an outcome. It is wanted on its own terms, and it is the thing the placement rate is standing in for.') \
+ resp(
   'Take employer_partnership_strength. Say what role it plays for the mentorship decision, what role it plays for the reporting decision, and one thing you are not allowed to do with it in either.',
   'For the mentorship decision it is context. FPF builds partnerships, so their strength is not fixed in general, but nothing in the mentorship decision moves it, and it shapes how many participants are placed, so it belongs in the comparison rather than in the decision. For the reporting decision it is closer to a signal, because a funder reading that partnerships are strong takes it as evidence that placements will follow; and it is arguably an outcome for the partnerships team, who are judged on it directly. In neither case may it be averaged. Its levels are ordered, so a partnership at very high ranks above one at low, but nothing establishes that the step from low to high is the same size as the step from high to very high, so a mean of the coded values is a number with no referent.') \
+ resp(
   'A funder asks FPF for one number to report as the evidence that the programme is working. Name the number you would report, say which role it plays, and give the strongest argument against your own choice.',
   'I would report the share of participants in work one year after finishing. It is the closest thing in reach to an outcome, since it is wanted for its own sake rather than as evidence of something else, and it is harder to move without doing the underlying work than a placement rate measured at three months. The strongest argument against it is timing. It is a year late, which makes it useless for steering: by the time the figure is known, the cohort it describes has finished and the decisions it should have informed have been made. That is the whole reason signals exist. A funder who wants one number and wants it now is asking for a signal, and the honest response is to give the signal, name what it stands in for, and say what could push it up without the outcome improving.') + """
</section>
"""

PAGE = {
    'file': 'part1.html', 'nav': 'part1',
    'title': 'Part 1. The decision and the roles', 'sub': 'Part 1',
    'dek': 'What job is this column doing, for this decision, for this decision-maker?',
    'toc': [('s1', '1.1 Activities into outcomes'), ('s2', '1.2 Signal and outcome'),
            ('s3', '1.3 A role is not a property'), ('s4', '1.4 Facts and dimensions'),
            ('practice', 'Practice')],
    'body': intro + s1 + s2 + s3 + s4 + practice,
    'prev': ('index.html', 'Start here'),
    'next': ('part2.html', 'Part 2. What one row is'),
}
