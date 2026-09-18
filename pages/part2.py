from build import sec, ask, src, box, table, kc, resp, score, lost

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
<p>Homework 2 gave you 41,188 rows of telemarketing records from a Portuguese bank, with the instruction that every call is one row. That description is worth testing, because the file was built by someone else and the description came with it.</p>
<p>The test is in the columns. One column, campaign, records how many times this customer was contacted during this campaign. Read that against the stated grain. If one row were one call, a customer contacted five times would occupy five rows, and the contact count would run from one to five across them. Instead the count appears once, as a single value on a single row, which is only sensible if the row already stands for the whole sequence of calls to that customer. One row is one customer's last contact of the campaign, with the earlier attempts summarised into a column rather than recorded as rows of their own.</p>
<p>Getting this right changes which questions the file can answer. You can ask whether mobile beats landline for a customer, because channel and outcome are both recorded at customer level. You cannot ask whether the third call converts better than the first, because the first two calls are not rows. They were folded into a count before you received the file, and the rule in 2.1 applies: the folding cannot be undone.</p>
<p>The general habit is to treat the stated grain as a claim to be checked rather than a fact. Look for a column that counts something, or repeats where you expected uniqueness, or an identifier that appears more than once. From those columns you can work out what the row really is.</p>
""" + ask('What does one row represent here, and do the columns agree with what I was told?')
+ src('Homework 2, part 1, on stating what one row is.'))

s6 = sec('s6', '2.6', 'Two things are called granularity', """
<p>The word granularity is used for two separate choices, and confusing them causes trouble later.</p>
<p>Row granularity is what one row represents. Everything above is about that. It follows from the comparison, as in 2.2, and once fixed it limits which questions the file can answer.</p>
<p>Column granularity is how finely a value is recorded inside a row. The FPF file has three settings of it at once. Salary is recorded to the currency unit, which is why 1,912 employed participants have 1,884 distinct salaries between them. Attendance is recorded to the whole percentage point, so 5,000 participants share only 25 distinct attendance values, from 76 to 100. Prior experience is recorded as one of two bands, one to three years or four years and over, so a participant with eighteen months and a participant with thirty-four months are identical in the file.</p>
<p>These are recording choices, made by whoever designed the form or the system, and they were made for reasons of cost and convenience. Someone decided that attendance to the nearest percent was close enough and that exact months of experience were not worth collecting.</p>
<p>The one-way property holds for both kinds of granularity. A salary recorded to the unit can be banded into ranges at any point. A band cannot be turned back into a salary. What separates them is who decides and why. You choose the row granularity from the comparison you need, and whoever built the system chose the column granularity for reasons of cost and convenience.</p>
<p>What a coarse column costs you, and when a band is the honest way to record something, belongs to Part 5.</p>
""" + ask('Was this value recorded finely enough for the distinction I am about to draw with it?')
+ src('this section draws the two ideas together; the recording side is taken up again in Part 5.'))

practice = """
<section id="practice">
<h2><span class="n">Practice</span>Check yourself</h2>
<p>Six questions that mark themselves, then three to write out.</p>
""" + kc(P, 1,
   'A retailer can show one advertisement in the morning and a different one in the evening. Its file holds one row per customer. What does that file support?',
   ['One policy per customer, and nothing finer',
    'One policy per customer for each time of day',
    'Only a single policy for the whole customer base',
    'Any policy, once the rows are split by time of day'],
   0, 'Folding runs one way. Customer rows can be built from customer-and-time rows, never the reverse, so the time-of-day decision has no data underneath it.') \
+ kc(P, 2,
   'You have a three-row table of placement rates by track. Can that table answer whether mentored learners place better?',
   ['Yes, provided the table also lists the mentorship counts',
    'No, the track rows no longer separate mentored learners',
    'Yes, because all 5,000 learners are still represented in it',
    'No, because three rows are too few for a fair comparison'],
   1, 'Each track row was summarised across mentored and unmentored learners together, so the difference the question asks about is no longer in the table.') \
+ kc(P, 3,
   'All 637 unmentored participants in the FPF file are urban. What follows for a comparison by location?',
   ['Rural learners must have been excluded from the programme',
    'The rural placement rate of 41.51 percent is unreliable',
    'Rural learners have no unmentored group to compare with',
    'Location has to be dropped from the analysis altogether'],
   2, 'A group supports the comparison only if it contains both mentored and unmentored members. No rural learner went unmentored, so there is nothing to compare rural mentored learners against.') \
+ kc(P, 4,
   'FPF decides who receives mentorship. It does not decide who becomes employed. Which direction answers its question?',
   ['The grand percentage, because its denominator is all 5,000',
    'The column percentage, read down the employed column',
    'Either one, since both describe the same four counts',
    'The row percentage, read across the mentorship rows'],
   3, 'The denominator has to be the group FPF can act on. Mentorship is assigned; employment is observed afterwards.') \
+ kc(P, 5,
   'Of the 1,912 employed, 88.76 percent had been mentored. Of the 3,088 not employed, 86.33 percent had been mentored. Why are these so close?',
   ['Mentorship made almost no difference to who was employed',
    '87.26 percent of the whole cohort had been mentored',
    'The two groups being compared are of very different sizes',
    'The percentages were computed with the wrong denominator'],
   1, 'Almost any group drawn from this file is about 87 percent mentored, so both column percentages are close to the cohort figure whatever mentorship did.') \
+ kc(P, 6,
   'Salary is recorded to the currency unit, attendance to the whole percentage point, prior experience as one of two bands. What kind of choice is this?',
   ['How finely each value was recorded, which somebody chose',
    'What one row of the file is taken to represent',
    'A fixed property of the quantity being measured',
    'A defect that should have been repaired before the analysis'],
   0, 'This is column granularity, a recording decision made for reasons of cost and convenience, separate from the choice of what a row is.') \
+ score() + """
<h3>Write it out</h3>
<p>There is no single correct answer to these. Write yours first, then compare.</p>
""" + resp(
   'State what one row must be for each of these three decisions, and say why. (a) A hospital decides which of its clinics to extend opening hours at. (b) A hospital decides whether to send each patient a reminder before each appointment. (c) A regulator decides whether to license the hospital.',
   'Begin from what can be acted on separately. (a) One row per clinic, because opening hours are set per clinic. The comparison is between clinics, and patient rows would work only if they could be folded up to clinics. (b) One row per patient and appointment, because a reminder is sent or withheld for each appointment separately. A file with one row per patient cannot support it, since nothing in it varies across that patient\'s appointments. (c) One row per hospital, because the licence is granted or refused to the hospital as a whole. Note that (b) is finer than (a), and that a file built for (b) could be folded to answer either of the others, while the reverse is impossible.') \
+ resp(
   'Using the education table in 2.3, say what the lowest level the FPF file supports for a mentorship decision is, and state what is lost by moving up to the programme level.',
   'The lowest supported level is the group, and education is one workable grouping, because each education level contains both mentored and unmentored participants. Moving up to the programme level replaces three gaps with one: a single figure of 5.15 points stands in for +9.68 among High School participants, +4.95 among Masters and +2.10 among Bachelors. What is lost is the ordering. A reader given only the programme figure would take mentorship to be worth a similar amount to everyone, when in fact the largest gap is among the participants with the least education and the smallest is among those with a Bachelors degree. If mentorship is limited and has to be rationed, there is no basis in the programme figure for choosing who receives it.') \
+ resp(
   'A charity runs a job club. Its crosstab puts attendance at the job club on the columns and employment six months later on the rows. It reports that 71 percent of those now employed had attended the job club. The trustees are deciding whether to fund the club for another year. Say what is wrong with the reported figure and what you would ask for instead.',
   'The 71 percent is a column percentage read from an outcome. Its denominator is the people who ended up employed, so it describes who those people turn out to be, and it would be high whenever most of the charity\'s clients attend the job club, whatever the club achieved. The trustees control attendance at the club and do not control employment, so the number they need runs the other way: of those who attended, what share were employed six months later, and of those who did not attend, what share were employed. I would ask for the two row percentages with the counts behind them, and I would check that the non-attenders are a group that exists in usable numbers rather than a handful of people.') + """
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
