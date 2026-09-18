from build import sec, ask, src, box, table, kc, resp, score, lost

P = 'p3'

intro = """
<p>Part 2 was about which people you can see in a file. This part is about what you can see of them. Every column is the end of a process in which somebody decided what to record, in what form, on what scale, and standing in for what. None of those decisions is written in the column, and all of them limit what the number can be used for.</p>
<p>The nine sections below work through those decisions in the order they were made. Each section asks the same two things of the reader: read the column name, then ask what had to happen before a value could be written underneath it.</p>
"""

s1 = sec('s1', '3.1', 'A structural blank is not missing data', """
<p>Three columns in the FPF file are blank for exactly the same 3,088 participants: salary, employment_type and sector. Those are precisely the participants for whom employed is No. There are no blanks anywhere else.</p>
<p>That pattern is what a structural blank looks like. The value is absent because another column made it impossible, so the blank records that there was nothing to collect, rather than recording that something was lost. There is no salary to collect from somebody without a job, and no sector for them to work in. Nothing was lost and nothing needs repairing.</p>
<p>The reason to be able to recognise this is that the usual remedies do damage. Suppose somebody tidies the file by filling the blanks in employment_type with the word None. The column now has four values, Full-time, Contract, Part-time and None, and a count by employment type reports 3,088 people in a category that describes no employment arrangement at all. Anyone reading that table later has no way of knowing that the fourth category means the person was not employed. Filling salary with zero is worse, because the mean then changes from 63,140 to 24,145 without anyone recording that a change was made.</p>
<p>The test is to find the column that controls the blank. If the blanks line up exactly with the values of another column, they are structural, and they should be left alone and explained. If they do not line up with anything, that is a different problem and it needs a different answer.</p>
""" + ask('Was there nothing to record here, or was something lost?')
+ src('the in-class question about filling structural blanks with None; Part 4 takes up the difference between a blank cell and a person who is not in the file at all.'))

s2 = sec('s2', '3.2', 'Denominators', """
<p>The FPF board asks one question: does the programme work. Three answers are available, and all three are correct arithmetic on the same 5,000 people.</p>
""" + table(['The figure', 'What it counts', 'Out of'], [
    ['38.24%', 'placed in any employment', 'all 5,000 enrolled'],
    ['28.88%', 'placed in full-time employment', 'all 5,000 enrolled'],
    ['75.52%', 'placed in full-time employment', 'the 1,912 who were placed'],
]) + """
<p>Nobody lied and nobody made an error. Only the denominator changed. Choosing between the three is a decision about which claim FPF is making, and it is made by a person, not by the data.</p>
<p>The third figure is the most flattering, and it is honest. It is the right number if the question is about the quality of the placements that happened. It is the wrong number if the question is what happens to somebody who enrols, because most of the people who enrolled are not in its denominator.</p>
<p>The same choice appears in the salary column. Among the 1,912 employed participants the mean salary is 63,140. Across all 5,000 enrolled, counting those with no job as zero, it is 24,145. Whoever writes a funder report that says "average salary" without saying which one has made a choice and has not recorded it.</p>
<p>The working habit is to write the denominator into the sentence rather than the footnote. A rate reported without its denominator is a claim that the reader has no way to check.</p>
""" + ask('What is the denominator here, and would the claim still be made if it had to be said aloud?')
+ src('the in-class activity on three honest placement rates; Reading Note 2 on denominators; Reading Note 1, section 6.'))

s3 = sec('s3', '3.3', 'What can be added up', """
<p>Averaging a set of group rates, while ignoring how many people are in each group, was done five times in class on the same file. The true placement rate is 38.24 percent every time.</p>
""" + table(['Slice by', 'Mean of the group rates', 'How far out', 'Smallest group'], [
    ['gender', '53.72%', '+15.48', '13'],
    ['location', '39.68%', '+1.44', '518'],
    ['education', '39.63%', '+1.39', '1,263'],
    ['track', '37.99%', '-0.25', '738'],
    ['employer partnership strength', '38.21%', '-0.03', '1,141'],
]) + """
<p>The same mistake was made five times and the damage ranges from fifteen percentage points to three hundredths of one. What separates them is the group sizes. Gender has a group of 13 counted as heavily as a group of 2,763. Partnership strength has four groups of roughly 1,200 each, so weighting them equally happens to be close to weighting them by size.</p>
<p>The last row is the one a reader is most likely to be misled by. Anyone who tried this method only on partnership strength would conclude it was sound, and would carry it to the next question, where the groups are not equal.</p>
<p>Rates can be combined, but because a rate is a quotient, combining them means recovering the counts underneath them and dividing once at the end. Totals and counts can be added across any grouping. Rates and percentages were already divided, and adding them divides again by something nobody chose.</p>
""" + ask('Are the groups I am averaging over the same size, and what does the answer become if I weight them by how many people are in each?')
+ src('the in-class activity that repeated the same averaging mistake five times; Reading Note 2, section 8.'))

s4 = sec('s4', '3.4', 'The chain of decisions behind one column', """
<p>The employed column holds one value per participant, Yes or No. Before anybody could write either word, four questions had to be settled.</p>
""" + table(['The decision', 'The question actually being answered'], [
    ['Definition', 'Does any paid work count, or only work related to the training track?'],
    ['Instrument', 'Is this self-reported, confirmed by the employer, or taken from a payroll record?'],
    ['Rules', 'Does somebody who starts a job and leaves after three weeks count?'],
    ['Timing', 'Employed within three months of finishing, or six, or twelve?'],
], txt=True) + """
<p>Two analysts who agree completely about what employment means will still produce different numbers, because agreement about the concept does not settle any of the four. One may count a three-week job and the other may not. Both are defensible and the two columns will disagree.</p>
<p>None of those four choices is recorded in the file. The file has a column called employed, holding a word that looks like a plain fact about the world. The word Yes does not record which definition produced it.</p>
<p>The practical consequence is for anyone comparing two numbers that came from different places. A placement rate from FPF and a placement rate from another programme are comparable only if the four questions were answered the same way, and the column names do not record which answers were given. When a comparison across organisations looks surprising, this is the first place to look.</p>
""" + ask('What had to be settled before somebody could write this value down, and would another careful person have settled it the same way?')
+ src('the in-class breakdown of what employed means; Reading Note 2, section 7; Homework 2.'))

s5 = sec('s5', '3.5', 'What a measure records and what it leaves out', """
<p>FPF wants to know whether its learners are engaged. Asked in class to list the ways a learner could show engagement, the room produced eight without difficulty: turning up, asking questions, helping other learners, finishing work early, coming back after failing, emailing the trainer, staying late, and doing the optional reading.</p>
<p>One of those eight was recorded. The FPF file has attendance_pct and nothing else from the list.</p>
<p>Nobody measured engagement badly. Somebody chose one of the eight ways it is visible and recorded that one. A concept like engagement is visible in many ways, a measure records some of them, and the rest are never recorded at all. The seven that were left out are not missing from the file in any way you could detect, because the file has no column for them at all.</p>
<p>The useful next question is who the chosen measure describes badly. Attendance describes badly any learner with shift work or caring responsibilities. Such a learner may be highly engaged and rarely present, and their attendance figure will be low, so anyone reading it will take them for disengaged. They are also, in a programme like this one, among the people the programme most wants to help, so on this measure the people it exists to serve appear to be its problem cases.</p>
<p>Ask the same question of any measure by asking whether it would come out differently if a different sample of the concept had been taken. A different Tuesday. A different five questions. If the answer is yes, the number describes the sample and not the concept.</p>
""" + ask('In how many ways is this concept visible, how many were recorded, and who does the recorded one describe badly?')
+ src('the in-class activity on everything engagement could have been; the instructor notes on proxies.'))

s6 = sec('s6', '3.6', 'Proxies, and why being recordable is not being a good measure', """
<p>Four columns in the FPF file were put in front of the class with the question of how much to trust each one. Three of them stand in for something that was never measured, and each of those three was then checked against whether the participant was placed.</p>
""" + table(['Column', 'Standing in for', 'Relationship with placement'], [
    ['attendance_pct', 'engagement', '-0.0496'],
    ['digital_lit_score', 'capability', '0.0445'],
    ['instr_student_ratio', 'the attention a learner received', '0.0315'],
    ['employed', 'nothing; it is the outcome itself', 'not applicable'],
]) + """
<p>All three are flat or backwards. Attendance runs the wrong way, so higher attendance goes with slightly lower placement. The other two barely move at all. Whatever these columns are recording, it is not something that tracks the outcome the programme exists to produce.</p>
<p>The reason all three are in the file is that they could be recorded. An attendance register already existed, a score was already being collected, a ratio could be calculated from numbers the administration already held. Nobody checked that any of them measures what it is being used for, because being recordable and being a good measure are separate properties and only the first one is obvious at the time.</p>
<p>Whenever a proxy is used, three statements are owed: what it is intended to represent, what it might miss, and how those limitations could change the conclusion. If the three cannot be written, the proxy is not ready to be used.</p>
<p>One further warning. A proxy that is also used as a target stops being a good measure. If FPF paid its trainers a bonus based on attendance, attendance would rise and would stop being evidence about engagement, because effort would move to the measure.</p>
""" + ask('What is this column standing in for, and has anybody checked that it does?')
+ src('the in-class activity ranking four columns by trust; Reading Note 2, section 7, on proxies.'))

s7 = sec('s7', '3.7', 'Scale', """
<p>FPF proposes a single readiness score for each learner, made by averaging attendance_pct and digital_lit_score. Both are percentages, so the calculation looks safe.</p>
""" + table(['Column', 'Min', 'Max', 'Range', 'Standard deviation'], [
    ['attendance_pct', '76', '100', '24', '5.21'],
    ['digital_lit_score', '51', '100', '49', '11.89'],
]) + """
<p>The two columns are not on the same scale. Digital literacy varies more than twice as widely as attendance, so in the average of the two, about 84 percent of the variation comes from digital literacy alone. A learner's attendance would barely move the readiness score. Nobody intended to weight one column four times as heavily as the other, and a reader of the readiness score cannot tell from it that this happened.</p>
<p>Both columns end in a percent sign, and neither column name records what the percent is of. Attendance is a percentage of sessions available. Digital literacy is a percentage of marks on an assessment. Two columns that use the percent sign are not therefore on the same scale.</p>
<p>The same warning applies to ordered categories. Code employer_partnership_strength from 1 to 4 and the mean is 2.57. There is no partnership of strength 2.57, and the number assumes the step from Very Low to Low is the same size as the step from High to Very High, which nobody has established. The placement rates across the four levels run 40.88, 36.99, 36.21 and 38.78, and they do not even rise in order.</p>
""" + ask('Are these values on the same scale, and what is the unit a proportion of?')
+ src('the in-class activity on two columns both in percent; Reading Note 3, section 8.'))

s8 = sec('s8', '3.8', 'Comparability', """
<p>Two learners are assessed before and after a programme.</p>
""" + table(['Learner', 'Before', 'After', 'National percentile'], [
    ['A', '90', '92', '95'],
    ['B', '55', '78', '70'],
]) + """
<p>Which is the stronger candidate? The question cannot be answered as posed. An employer selecting on current capability should prefer A. Somebody evaluating the teaching should notice that B gained twenty-three points against two. A scholarship committee weighing distance travelled may reach a third conclusion. None of these numbers changes, and the correct summary changes with the decision.</p>
<p>Putting two things on the same footing is itself a decision, and sometimes the file does not contain what the decision requires. Among the placed participants, the 215 from rural areas earn a mean salary of 68,172 and the 1,697 from urban areas earn 62,503. Treating the first as the better outcome assumes the two amounts buy the same things. Housing, transport and living costs differ between rural areas and cities, and none of them is in this file.</p>
<p>That assumption cannot be checked from the data, and no calculation on these columns will supply it. It has to be settled outside the file, or the comparison has to be abandoned. Saying that rural placements pay 5,669 more is reporting arithmetic and calling it a finding.</p>
""" + ask('Are these two numbers on the same footing, and is what it would take to put them on one anywhere in this file?')
+ src('Reading Note 2, section 9, for the two learners; the in-class activity on rural and urban salaries. Part 4 covers who ended up in the rural group; Part 5 covers what happens to this comparison when education is held still.'))

s9 = sec('s9', '3.9', 'Write it down', """
<p>Everything in this part is a decision that somebody made and nobody recorded. The four questions behind employed, the eight ways of being engaged of which one was recorded, the choice of denominator, the scale a percentage is a percentage of. None of it is in the file, and all of it is needed to use the file.</p>
<p>The place it belongs is a data dictionary: one entry per column, saying what the column is meant to represent, how it was collected, what its values mean, and, for a proxy, the three statements owed under 3.6. The FPF case came with one.</p>
<p>Derived columns need this most, because they have no existence outside the decision that made them. A readiness score built by averaging two percentages is exactly the averaging in 3.7, and six months later the only difference between a defensible column and an indefensible one is whether somebody wrote down how it was built. Write the entry when you build the column, because that is the only moment at which you still know.</p>
<p>The other half of the habit is to ask for the dictionary when you receive data. If none exists, the questions in this part are the ones to ask, and the answers should be written down by you.</p>
""" + ask('If I hand this column to somebody in a year, what will they need to know that is not in its name?')
+ src('the instructor notes on derived variables and data dictionaries; the data dictionary issued with the FPF case.'))

practice = """
<section id="practice">
<h2><span class="n">Practice</span>Check yourself</h2>
<p>Six questions that mark themselves, then three to write out.</p>
""" + kc(P, 1,
   'Someone tidies the FPF file by filling the blanks in employment_type with the word None. What does that do?',
   ['Nothing, because the blanks were going to be ignored anyway',
    'It repairs the column so it can now be counted correctly',
    'It invents a fourth employment category',
    'It changes the mean salary from 63,140 down to 24,145'],
   2, 'Those blanks were structural. Filling them invents a category of employment arrangement that describes nobody, and the reason for the blank is no longer recoverable.') \
+ kc(P, 2,
   'FPF reports that 75.52 percent were placed in full-time work. Which question does that figure answer well?',
   ['What happens to somebody who enrols in the programme',
    'How many of the 5,000 enrolled found full-time work',
    'Whether the programme places more people than it used to',
    'How good the placements were among those who got one'],
   3, 'Its denominator is the 1,912 who were placed, so it describes placement quality. The figure for what happens to somebody who enrols is 28.88 percent.') \
+ kc(P, 3,
   'Averaging group rates without weighting gave an answer 15.48 points too high for gender but 0.03 points out for partnership strength. Why the difference?',
   ['A group of 13 is weighted as heavily as one of 2,763',
    'Gender is a categorical column and partnership strength is ordered',
    'Partnership strength has four groups and gender has only three',
    'The placement rates vary much more across the gender groups'],
   0, 'The method is equally wrong both times. It only does visible damage when the groups differ sharply in size.') \
+ kc(P, 4,
   'Attendance correlates with placement at -0.0496. Why was attendance put in the file in the first place?',
   ['Because earlier analysis had shown it predicted placement',
    'Because engagement had been defined as attendance by the board',
    'Because a register already existed and it could be recorded',
    'Because it was the best available of the measures considered'],
   2, 'It was recordable, which is a separate property from being a good measure, and only the first one is obvious at the time of collection.') \
+ kc(P, 5,
   'Attendance runs 76 to 100 and digital literacy 51 to 100. A readiness score averages the two. What follows?',
   ['The score is sound, since both columns are percentages',
    'Digital literacy supplies about 84 percent of the variation',
    'The score should be recomputed using the medians instead',
    'Attendance is weighted too heavily because its values are larger'],
   1, 'Digital literacy varies more than twice as widely, so averaging the two weights it about four times as heavily as attendance, which nobody intended.') \
+ kc(P, 6,
   'Learner A scores 90 before the programme and 92 after. Learner B scores 55 before and 78 after. Which is the stronger candidate?',
   ['Learner A, who scored higher after the programme',
    'Learner B, who gained twenty-three points against two',
    'Learner A, because A ranks at the 95th percentile nationally',
    'It depends on which decision the figure is being used for'],
   3, 'Each of the other three is right for one decision and wrong for the rest. An employer hiring on capability now would take A, a trainer judging the teaching would take B, and the national percentile in C is a fourth way of ranking the two rather than a tie-breaker between the first three. Nothing about the learners settles it until the decision is named.') \
+ score() + """
<h3>Write it out</h3>
<p>There is no single correct answer to these. Write yours first, then compare.</p>
""" + resp(
   'A college wants to measure teaching quality. Two columns are available: the mean student rating of the module, and the share of students who passed it. Take each in turn and say what it is standing in for, what it misses, and which teachers it treats unfairly. Then write the data dictionary entry you would attach to the one you would use.',
   'The student rating stands in for the quality of the teaching as experienced. It misses everything students cannot judge, such as whether the syllabus was current, and it varies with things that are not teaching, such as the hour the class met and how hard the module is. It treats unfairly anyone teaching a required quantitative module to a reluctant class. The pass share stands in for how much was learned. It misses what was learned by those who passed either way, and it can be raised without teaching anybody anything, by setting an easier paper. It treats unfairly anyone teaching the weakest intake. I would use the student rating, because the pass share can be moved directly by the person being measured. The entry: mean of end-of-module student ratings, one to five, collected online in the final week, response rate recorded alongside; intended to represent teaching quality as students experienced it; known to vary with class size, timetable slot and module difficulty, so it is comparable only within a subject and level; not to be used for any decision about an individual teacher without the response rate and the class size beside it.') \
+ resp(
   'The FPF director, a funder, and a prospective participant each ask how well the programme places people. Give each of them one of the three figures from 3.2, say why that one, and say what each would wrongly conclude from one of the other two.',
   'The prospective participant should be given 38.24 percent, because they are deciding whether to enrol and they want to know what happens to people who enrol. Given 75.52 percent they would conclude that three quarters of people who join get full-time work, which is wrong by a wide margin. The funder should be given 28.88 percent, since a funder is usually paying for full-time employment as the outcome and wants it as a share of everybody paid for. Given 75.52 percent they would conclude that the programme converts its intake far more effectively than it does. The director needs all three, and specifically 75.52 percent alongside 38.24, because the gap between them is the operational question: whether the problem is placing people at all or placing them into full-time work. Given only 38.24 percent the director could not tell which of the two to work on.') \
+ resp(
   'A hospital records a column called readmitted, Yes or No. Write the four decisions that had to be settled before anybody could fill it in, and for each one describe a way two careful analysts could disagree and still both be right.',
   'Definition: readmitted for anything, or only for a condition related to the original admission? One analyst counts a fall at home, the other does not, and both can defend it depending on whether the question is about patient outcomes or about the quality of the original treatment. Instrument: taken from this hospital\'s own records, or from a regional system? A patient readmitted to a different hospital is invisible in the first and counted in the second. Rules: does a planned follow-up procedure count as a readmission, and does a patient who arrives at the emergency department and is sent home after four hours count as admitted? Timing: within thirty days of discharge, or ninety? The thirty-day window is conventional, the ninety-day window includes slower failures, and the two produce different rates from the same patients. None of the four choices appears anywhere in a column named readmitted, so two hospitals reporting their readmission rates may be reporting numbers that were never comparable.') + """
</section>
"""

PAGE = {
    'file': 'part3.html', 'nav': 'part3',
    'title': 'Part 3. What a column measures', 'sub': 'Part 3',
    'dek': 'What does this number stand in for, and what did that leave out?',
    'toc': [('s1', '3.1 Structural blanks'), ('s2', '3.2 Denominators'),
            ('s3', '3.3 What can be added up'),
            ('s4', '3.4 The chain of decisions behind one column'),
            ('s5', '3.5 What a measure leaves out'), ('s6', '3.6 Proxies'),
            ('s7', '3.7 Scale'), ('s8', '3.8 Comparability'), ('s9', '3.9 Write it down'),
            ('practice', 'Practice')],
    'body': intro + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + practice,
    'prev': ('part2.html', 'Part 2. What one row is'),
    'next': ('part4.html', 'Part 4. Who is in the file'),
}
