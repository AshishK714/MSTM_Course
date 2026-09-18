from build import sec, ask, src, box, table, kc, resp, score, lost, case

P = 'p2'

intro = """
<p>Part 1 asked what job a column is doing. This part asks what one row is. The two questions are separate, and this one comes first, because a column can only measure something about whatever the row represents.</p>
<p>The answer is never a property of the data. Somebody chose it, usually years before anyone thought about analysis, and that choice fixed the set of comparisons that can ever be made from the file. This part is about how the choice is made, how to recognise it in a file you did not build, and what it costs when the choice and the question do not agree.</p>
"""

s1 = sec('s1', '2.1', 'The unit chain: decision, analysis, observation', """
<p>Begin with the decision rather than the data. Every decision has a unit attached to it, and that unit is fixed by what the organisation can act on separately.</p>
<p>A retailer wants to personalise its advertising. If it can assign one advertising policy per customer, the decision unit is the customer. If it can show one advertisement in the morning and a different one in the evening, the decision unit becomes the customer within a time of day. The same person is now two decision units, because there are two separate choices to make about that person.</p>
<p>The decision unit fixes the unit of analysis, which is what has to be compared. That in turn fixes the unit of observation, which is what has to appear as a row. Three questions, in order: what can the business act on separately, what has to be compared to inform that, and what therefore has to be a row.</p>
<p>The chain runs one way. Rows recorded by customer and day can be folded into rows by customer whenever you want. The reverse is impossible. Once the file holds one row per customer, the days are gone, and no technique can recover them.</p>
<p>The FuturePath Foundation file is an example of what this costs in practice. It holds 5,000 rows, one per participant. Suppose the programme runs ten modules and mentorship could be offered to each participant for each module separately. That decision has 50,000 participant-module pairs attached to it. Every value in the file is constant within a participant, so nothing in it separates one module from another. The file cannot support that decision, and its size is beside the point.</p>
""" + ask('What can this organisation act on separately, and does the file vary at that level?')
+ src('Reading Note 2, section 2, on the unit chain and one-way folding; recapped in class before the pivot exercise.'))

s2 = sec('s2', '2.2', 'The comparison decides the level', """
<p>Three questions were asked of the FPF file in class. All three are about the same 5,000 learners, and each one requires a different table.</p>
""" + table(['The question', 'What varies', 'The table it needs'], [
    ['Do mentored learners place better?', 'Between mentored and unmentored learners', 'One row per mentorship value (2 rows)'],
    ['Which track places best?', 'Between tracks', 'One row per track (3 rows)'],
    ['Does partnership strength relate to placement?', 'Between partnership levels', 'One row per level (4 rows)'],
]) + """
<p>The second table is the three-row one. Of the 738 learners in the AI track, 37.0 percent were placed; of the 2,091 in Hybrid, 40.0 percent; of the 2,171 in Traditional, 36.9 percent.</p>
<p>Now put the first question to that second table. Do mentored learners place better? The three-row table cannot answer it. Each of its rows holds mentored and unmentored learners together, and the summary was taken across both, so the difference the question asks about was averaged away when the table was made. You put in 5,000 learner rows and got back three, which is the one-way property from 2.1.</p>
<p>This is the practical form of the rule. A table is adequate for a comparison when the thing being compared still varies inside it. The mentorship question needs learner rows, because mentorship varies between learners. The track question needs track rows for the reporting, although those rows are themselves built from learner rows. Each level supports a comparison the others cannot, and no level is the correct one in general.</p>
""" + ask('Does the thing I am comparing still vary inside the table in front of me?')
+ src('the in-class exercise that built three tables from one file; Reading Note 2, section 3, on declaring the grain.'))

s3 = sec('s3', '2.3', 'The ladder: programme, group, individual', """
<p>Once the level follows from the comparison, the question becomes which level a decision about mentorship should be made at. There are three levels, and the file supports two of them.</p>
<p>At programme level FPF decides one thing: run mentorship for everyone, or for nobody. Two numbers are enough to decide it. Among the 4,363 mentored participants, 38.90 percent ended up employed, against 33.75 percent of the 637 unmentored, a gap of 5.15 percentage points. Every participant is affected by that decision, and no fact about any particular participant was used in making it.</p>
<p>At group level the decision is still made per participant, by virtue of the group they belong to. Splitting the participants by education gives three separate gaps.</p>
""" + table(['Highest education', 'Unmentored rate', 'Mentored rate', 'Gap', 'Unmentored / mentored'], [
    ['High School', '24.30%', '33.98%', '+9.68', '251 / 2,072'],
    ['Masters', '41.21%', '46.16%', '+4.95', '182 / 1,081'],
    ['Bachelors', '38.73%', '40.83%', '+2.10', '204 / 1,210'],
]) + """
<p>At individual level the file cannot support a decision. To decide correctly for one named participant you would need to know what happened to that participant both with mentorship and without it. Only one of the two was ever observed, so there is nothing to compare.</p>
<p>There is one condition on deciding at group level, and it rules out several groups here. A group is usable only if it contains both mentored and unmentored members. All 637 unmentored participants are urban, all have one to three years of prior experience, and all have mid-level AI exposure. Rural learners, those with four years or more, and those at low or high AI exposure therefore have no unmentored members at all. For those groups the file contains no comparison.</p>
""" + lost('Slicing until a difference appears will always succeed, because with enough slices differences arise from noise alone. A gap of nine points among 251 people and the same gap among twenty are not the same finding. Check each gap against the size of the groups behind it.')
+ ask('At which level does the file still hold both sides of the comparison?')
+ src('the in-class work on the decision unit and on nesting a context variable; the education and track figures were recomputed for this guide.'))

s4 = sec('s4', '2.4', 'Conditioning: grand, column and row percent', """
<p>Put mentorship on the rows and employment on the columns and you get four counts: 1,697 mentored and employed, 2,666 mentored and not, 215 unmentored and employed, 422 unmentored and not. Those four counts can be shown as percentages three ways. All three appear in the same menu in a spreadsheet, they look alike on screen, and they answer different questions.</p>
""" + table(['Direction', 'The denominator', 'What the employed cells read'], [
    ['Grand percent', 'all 5,000 participants', '33.94% mentored and employed, 4.30% unmentored and employed'],
    ['Column percent', 'the 1,912 employed and the 3,088 not', '88.76% of the employed were mentored, 86.33% of the not employed were mentored'],
    ['Row percent', 'the 4,363 mentored and the 637 not', '38.90% of the mentored were employed, 33.75% of the unmentored were employed'],
]) + """
<p>The grand percentages describe the composition of the cohort and compare nothing, since every cell is divided by the same 5,000. The column percentages are close together, 88.76 against 86.33, and the reason has nothing to do with mentorship: 87.26 percent of everybody was mentored, so almost any group drawn from this file is about 87 percent mentored.</p>
<p>The row percentages answer FPF's question. The reason is what FPF controls. FPF decides who receives mentorship. It does not decide who becomes employed. A percentage is useful for a decision when its denominator is the group you can act on, because you can then read it forward: set mentorship this way for this group, and here is what tends to follow. The column percentage is read backward, from an outcome to what those people had received, and you can observe an outcome after the fact but never assign one.</p>
<p>The direction is decided by which variable you put on the rows, which is a layout choice made in a menu. The data does not record which direction was chosen.</p>
""" + box('The rule', ['Condition on the thing you control, and read the percentage forward from it. If the denominator is an outcome, the number describes who ended up there, which is a different question from what to do next.'], 'principle')
+ ask('Which group is the denominator here, and is it the group I can act on?')
+ src('the in-class pivot exercise on the three ways to show a percentage; Reading Note 2 on denominators.'))

s5 = sec('s5', '2.5', 'Grain in a file somebody else built', """
<p>Homework 2 gave you 41,188 rows of telemarketing records from a Portuguese bank, and asked you to complete one sentence: one row of this dataset is one what. The file was built by someone else, and nothing in it answers that question directly.</p>
<p>The answer is in the columns. One column, campaign, records how many times this customer was contacted during this campaign. Read that as a test of what a row is. If one row were one call, a customer contacted five times would occupy five rows, and the contact count would run from one to five across them. Instead the count appears once, as a single value on a single row, which is only sensible if the row already stands for the whole sequence of calls to that customer. One row is one customer's last contact of the campaign, with the earlier attempts summarised into a column rather than recorded as rows of their own.</p>
<p>Getting this right changes which questions the file can answer. You can ask whether mobile beats landline for a customer, because channel and outcome are both recorded at customer level. You cannot ask whether the third call converts better than the first, because the first two calls are not rows. They were folded into a count before you received the file, and the rule in 2.1 applies: the folding cannot be undone.</p>
<p>The general habit is to treat any stated grain as a claim to be checked, and to work it out from the columns when none is stated. Look for a column that counts something, or repeats where you expected uniqueness, or an identifier that appears more than once. From those columns you can work out what the row really is.</p>
""" + ask('What does one row represent here, and do the columns agree with what I was told?')
+ src('Homework 2, part 1, which asks you to complete the sentence: one row of this dataset is one what.'))

s6 = sec('s6', '2.6', 'Two things are called granularity', """
<p>Granularity means two separate choices.</p>
<p>Row granularity is what one row represents, and it follows from the comparison (2.2).</p>
<p>Column granularity is how finely a value is recorded. Most things vary continuously, and we record them at separated points because that is cheaper and easier. How finely you record decides which kind of variable you have, and the level you choose depends on how you plan to use it.</p>
<p>Age was the class example. In years and months it is continuous. Rounded to whole years it is discrete. Put into bands it is categorical, and because those bands have an order it is more exactly called ordinal. Each step loses variation: held in whole years, half a year, three quarters and a full year are all recorded as one year. The skill, effort and knowledge a student brings to an exam vary continuously, and the recorded result may be only a pass or a fail.</p>
<p>Coarser is not always worse. The Titanic example in class was a case where banding is right. Age and survival are related in a complicated way, one way up to about twenty and the other above fifty. But suppose a person had to be at least fourteen to swim. Ability to swim then rises sharply at fourteen, and survival with it. A band with its edge at fourteen matches something real, as do ages fixed by law, such as driving or drinking.</p>
<p>In the FPF file, salary is recorded to the currency unit, attendance to the whole percentage point, and prior experience as one of two bands, so eighteen and thirty-four months are recorded alike.</p>
<p>Both go one way only: rows can be combined and salaries banded, and neither can be undone. You choose the row granularity; whoever built the system chose the column granularity.</p>
""" + ask('Was this value recorded finely enough for the distinction I am about to draw with it?')
+ src('the in-class discussion of variable types, of recording age, and of the swimming and legal cutoffs in the Titanic example; Part 5 works through when a band matches the world and when it hides something.'))

practice = """
<section id="practice">
<h2><span class="n">Practice</span>Check yourself</h2>
<p>All the questions below are worked from one situation. Read it once, then answer with the table in front of you.</p>
""" + case('The situation', [
    'Mentorship is expensive, and FPF can afford it for some participants but not all. The director has decided to look at the 2,323 participants whose highest education is High School, because that is where the programme recruits hardest. She has built the pivot in counts and stopped there, and she wants your advice on what to do with it.',
], table(['', 'Not employed', 'Employed', 'Total'], [
    ['Not mentored', '190', '61', '251'],
    ['Mentored', '1,368', '704', '2,072'],
    ['Total', '1,558', '765', '2,323'],
]) + '<p>Two other facts are in the file and not in this table. Across all 5,000 participants, 87.26 percent were mentored. Every one of the 637 participants who went without mentorship is urban, has one to three years of prior experience, and has mid-level AI exposure.</p>') + """
<p>Six questions that mark themselves, then three to write out.</p>
""" + kc(P, 1,
   'FPF decides who receives mentorship. It does not decide who becomes employed. Which percentage from this table should the director act on?',
   ['704 out of 2,072, the share of the mentored who were employed',
    '61 out of 765, the share of the employed who had gone unmentored',
    '704 out of 765, the share of the employed who were mentored',
    '704 out of 2,323, the share of everybody who was both'],
   0, 'Read forward from the thing FPF controls. That gives 33.98 percent against 24.30 percent for the unmentored, a gap of 9.68 points.') \
+ kc(P, 2,
   'A colleague computes that 92.03 percent of the employed had been mentored, and calls it strong evidence for mentorship. What is wrong with that?',
   ['The arithmetic is wrong; the correct figure is 87.80 percent',
    'It should have been computed on all 5,000 rather than 2,323',
    'Every group in this table is between 88 and 92 percent mentored',
    'It compares the mentored with the employed, which are different groups'],
   2, 'The denominator is an outcome. 2,072 of the 2,323 in this table were mentored, 89.19 percent; among the not employed the figure is 87.80 percent and among the employed 92.03 percent, so it would be high whatever mentorship did. A is wrong: 704 of 765 really is 92.03 percent, and the colleague&#39;s arithmetic being right is the point. B is wrong because the director asked about High School participants, so 2,323 is the right population and widening it would answer a different question. D misdescribes the error, because the colleague reported one percentage rather than comparing two groups.') \
+ kc(P, 3,
   'The director asks for the same comparison for rural participants. What should you tell her?',
   ['It can be done, but the rural groups will be small',
    'It will show a larger gap, because rural learners travel further',
    'Rural and urban have to be combined before the gap can be computed',
    'No rural participant went unmentored, so there is no comparison'],
   3, 'All 637 unmentored participants are urban. A group supports the comparison only when it contains both mentored and unmentored members.') \
+ kc(P, 4,
   'Someone proposes replacing this pivot with one row per education level, covering all 5,000 participants, to make the report shorter. Which of these would the new table not answer?',
   ['Which education level had the highest employment rate',
    'Whether mentored participants were placed more often',
    'How many participants there are at each education level',
    'What share of all 5,000 participants ended up employed'],
   1, 'Mentored and unmentored participants would be combined in each education row, so the difference between them would no longer appear. The other three are answerable from the three education rows.') \
+ kc(P, 5,
   'The director asks whether the file can tell her which individual participants to give mentorship to next year. What is the honest answer?',
   ['No, because mentorship does not vary within a single person',
    'Yes, by ranking participants on attendance and digital literacy',
    'Yes, provided the sample is large enough to support it',
    'No, because the file records education but not motivation'],
   0, 'To decide for one named person you would need what happened to that person with mentorship and without it. Only one of the two was ever observed.') \
+ kc(P, 6,
   'She now wants to offer mentorship separately for each of ten modules. The file has one row for each of the 5,000 participants. What stops her?',
   ['Ten modules would need ten separate pivot tables',
    'The file has no row for a participant in a module',
    'The counts in each module would be too small to compare',
    'Module-level mentorship was never offered, so there is no precedent'],
   1, 'The decision has 5,000 participants times ten modules, so 50,000 units, against 5,000 rows. Everything in the file is constant within a participant, so nothing in it separates one module from another.') \
+ score() + """
<h3>Write it out</h3>
<p>The same situation. There is no single correct answer to these. Write yours first, then compare.</p>
""" + resp(
   'The director wants one sentence she can say to the board about this table. Write it, with the denominator in the sentence. Then say what the table does not license her to claim.',
   'I would write: among the 2,323 participants whose highest education is High School, 33.98 percent of the 2,072 who received mentorship were employed, against 24.30 percent of the 251 who did not. The table does not license a causal claim. Nobody was assigned to mentorship at random, so the 9.68 point gap may be a consequence of who received mentorship rather than of what mentorship did, and the 251 unmentored participants may differ from the 2,072 in ways the file does not record. It also does not license anything about rural participants, about anyone with four or more years of experience, or about any individual, because the file holds no unmentored participants in the first two groups and mentorship does not vary within a person.') \
+ resp(
   'FPF can fund mentorship for a limited number of participants. Using this table and the figures for the other education levels in 2.3, say who you would give it to and what would change your mind.',
   'I would give it to the High School participants first. Their gap is the largest of the three, 9.68 points against 4.95 for Masters and 2.10 for Bachelors, and they are also the group the programme recruits hardest. Two things would change my mind. The first is evidence that the unmentored 251 differ systematically from the mentored 2,072, since they were not assigned at random and the ordering may be a consequence of who was chosen rather than of mentorship. The second is cost per participant: if mentorship costs more to deliver to this group, the ranking by gap is not the ranking by value. I would also want the same table for the participants who left before an outcome was recorded, and the file does not contain them.') \
+ resp(
   'In Homework 2 the campaign manager had to decide whether to pay for mobile calls. Suppose a colleague reports the share of the customers who subscribed who had been called on a mobile, and recommends mobile for everyone. In Homework 2 the rule was to use the more expensive channel for a group only if it raised that group&#39;s subscription rate by at least eight percentage points. Say what is wrong with the colleague&#39;s figure and what you would ask for instead.',
   'The figure has an outcome as its denominator. It describes who the subscribers turn out to have been, and it would be high whenever most calls in the file were mobile, whatever the channel achieved. The manager chooses the channel and does not choose who subscribes, so the percentage has to be computed the other way round: of the customers called on a mobile, what share subscribed, and of those called on a landline, what share subscribed. That is the row percentage, and the lift the eight point rule is applied to is the difference between those two figures. I would also ask for the counts beside the percentages, because a group with very few landline calls gives a lift that cannot be relied on, which is the same problem FPF has with rural participants.') + """
</section>
"""


PAGE = {
    'file': 'part2.html', 'nav': 'part2',
    'title': 'Part 2. What one row is', 'sub': 'Part 2',
    'dek': 'What does one row represent, and did the comparison choose it?',
    'toc': [('s1', '2.1 The unit chain'), ('s2', '2.2 The comparison decides the level'),
            ('s3', '2.3 The ladder'), ('s4', '2.4 Conditioning: grand, column and row percent'),
            ('s5', '2.5 Grain in a file somebody else built'),
            ('s6', '2.6 Two things are called granularity'), ('practice', 'Practice')],
    'body': intro + s1 + s2 + s3 + s4 + s5 + s6 + practice,
    'prev': ('part1.html', 'Part 1. The decision and the roles'),
    'next': ('part3.html', 'Part 3. What a column measures'),
}
