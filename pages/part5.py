from build import sec, ask, src, box, table, kc, resp, score, lost, case

P = 'p5'

intro = """
<p>Parts 2, 3 and 4 were about what is in a file. This part is about what happens when you reduce it to something a person can read. Every summary replaces many values with few, and something is lost each time. The question to carry through the part is what was lost, and whether the decision in front of you would change if you could see it.</p>
"""

s1 = sec('s1', '5.1', 'Why summarise at all', """
<p>The class started from a business school report on an incoming cohort. Nobody reading it wants to read every row. They want a handful of numbers that describe who is in the class, and they accept that most of the detail in the rows is gone.</p>
<p>That trade is the point. Compression loses information, and we do it anyway, because a number a person can hold in mind and act on is worth more than a table nobody reads. A summary is a different object from the data. It is made for a reader, by somebody who chose what to keep.</p>
<p>So the useful habit is to ask, of any summary put in front of you, what it left out, and then to ask whether the thing it left out would change what you were about to do. Sometimes the answer is no, and the summary is adequate. The rest of this part is a set of cases where the answer is yes.</p>
""" + ask('What did this summary leave out, and would my decision change if I could see it?')
+ src('the in-class discussion of why we summarise, using the incoming class report.'))

s2 = sec('s2', '5.2', 'Centre, spread, and which centre', """
<p>Among the 1,912 FPF participants who were placed, the mean salary is 63,140 and the median is 60,128. The mean is higher by 3,012.</p>
<p>The gap is itself informative about the shape of the salaries. A mean is pulled by values far from the centre and a median is not, so when the mean is above the median there are large values stretching the top of the distribution. Here the largest salary is 236,319 against a smallest of 16,609. Only 44.9 percent of the placed participants earn more than the mean, which is the clearest sign that the mean is not a typical person.</p>
<p>Which one to report depends on the question. For the total wage bill the mean is right, because the mean times the count is the total. For what a participant might expect, the median is right, because half are above it and half below.</p>
<p>Neither number describes how spread out the salaries are. The standard deviation, computed over the whole group, is 25,204, and it is hard to read against a mean. The mid-80 percent range is easier to act on. A percentile is the value a given share of the group falls below, so the tenth percentile is the 191st lowest of the 1,912 salaries, at 33,637, and the ninetieth is 94,447. Eight of every ten placed participants earn between those two figures. That is a sentence a board can use, and one very large salary does not change it, while it does change the mean.</p>
""" + ask('Is the centre I am reporting the one my question needs, and have I said anything about the spread?')
+ src('the in-class discussion of mean against median and of the mid-80 percent range; Reading Note 3, sections 3 and 4.'))

s3 = sec('s3', '5.3', 'When one mean represents nobody', """
<p>Mean attendance across the 5,000 participants is 93.13 percent. Count how many participants are at each value and the reason is clear.</p>
""" + table(['Attendance', 'Participants'], [
    ['76 to 90', '943'],
    ['91', '10'],
    ['92 to 100', '4,047'],
], caption='The lower group peaks at 83 percent, the upper group at 96 percent.') + """
<p>There are two groups of participants, not one, which is what a column is called bimodal for: it has two peaks rather than one. The larger group attends almost everything, peaking at 96 percent. The smaller group of 943 attends far less, peaking at 83. Only 10 participants attend 91 percent, and 4,047 attend 92 percent or more.</p>
<p>The mean of 93.13 falls between the two peaks, because a mean is a balance point between the groups, pulled towards the bigger one. The 943 average 82.91 and the 4,047 average 95.51, and weighting those by their sizes gives back 93.13. It is higher than every participant in the smaller group and lower than most of the larger one, so it describes neither. The median does not rescue you here either: at 95 it lands inside the larger group and describes the 943 no better.</p>
<p>What to do instead is to report the two groups separately, once you have satisfied yourself that they are two groups and not one. The way to satisfy yourself is to draw the histogram in 5.8 and look, which is how the two attendance groups became visible in the first place. The same applies wherever a population is a mixture, as adult heights are. Whether two peaks appear depends on how far apart the two centres are compared with the spread inside each group: the attendance groups are 13 points apart with most people within a few points of their own peak, which is why the dip is plain, and a mixture whose centres are close together shows one hump and hides its own composition.</p>
<p>A mean is safe to report when the values gather around one centre. Look at the shape before summarising it, because the calculation gives a number in both cases.</p>
""" + ask('Does this column have one centre or more than one, and have I looked?')
+ src('the in-class work on the two attendance distributions and the mixture of heights; Reading Note 3, section 5.'))

s4 = sec('s4', '5.4', 'Spread is a constructed measure', """
<p>The standard deviation is built, not read off, and whoever built it made an assumption.</p>
<p>To measure spread you take each value's distance from the mean, and those distances cancel if you simply add them, since some are above and some below. Something has to be done to stop the cancelling. Squaring each distance is one choice. Taking the size of each distance and ignoring its sign is another, and it is simpler.</p>
<p>The standard deviation takes the first route: square every distance, average the squares, then take the square root of that average to get back to the original units. The root rescales the final number and does not undo what the squaring did on the way.</p>
<p>What the squaring did is a claim about the world: that a value twice as far from the centre is four times as bad. A participant ten points from the mean contributes 100 to the total and one twenty points away contributes 400, so the second counts four times as heavily, not twice. For a bank that would be ruined by one very large loss, that is the right claim. For a programme where a participant thirty points below the mean is roughly three times the concern of one ten points below, it is the wrong claim, and options ranked by that measure will come out in an order nobody intended.</p>
<p>None of this is an argument for abandoning the standard deviation. The point is that a spread figure rests on an assumption made by whoever built it, and that the assumption should be one you would defend if asked.</p>
""" + ask('What does this measure assume about which differences are worse, and would I defend that assumption here?')
+ src('Reading Note 3, sections 6 and 7, on building the spread measure.'))

s5 = sec('s5', '5.5', 'A continuous world recorded in steps', """
<p>Most things vary continuously and are recorded at separated points, because recording finely costs more. Part 2 set that out for one file. Here it matters for what you may do with the result.</p>
<p>Counting and grouping are available for any recorded value. Ranking needs an order. Adding and averaging need the steps between values to be equal, which is exactly what an ordered category does not give you. A satisfaction rating of 4 is above a 2 and is not twice it, so averaging ratings assumes something the scale never established.</p>
<p>The scale itself is a decision somebody made. A company choosing between a 1 to 3, a 1 to 5 and a 1 to 10 satisfaction scale is choosing how much of the variation in what customers feel is recorded in the file. Grading works the same way, and the granularity differs by country, which is worth asking about: a system with a handful of grades and one with a fine percentage scale are recording the same student differently, and neither is simply better.</p>
<p>Banding can be right. When the world has a real threshold in it, a band with its edge at that threshold records something true, which is the Titanic case from Part 2 and the reason ages fixed by law behave the same way. When there is no threshold and the bands were chosen for convenience, the variation inside each band is lost and nothing is gained.</p>
""" + ask('Does this scale support the operation I am about to perform on it, and was its coarseness chosen for a reason?')
+ src('the in-class discussion of variable types, grading scales across countries and survey scales; Reading Note 3, section 8. Part 2 covers the recording choice itself.'))

s6 = sec('s6', '5.6', 'Two columns, three ways', """
<p>One column at a time gives you centre and spread. Two columns let you ask whether they move together, and there are three ways to look, chosen by what kind of columns they are.</p>
""" + table(['The two columns', 'What to build', 'What you read'], [
    ['Both categories', 'a crosstab', 'the rates, read in the direction you control'],
    ['One category, one number', 'a group comparison', 'the centre and spread within each group'],
    ['Both numbers', 'a scatterplot', 'the shape, including shapes a single figure does not distinguish'],
], txt=True) + """
<p>The first is Part 2's crosstab, and everything there about which direction to read still applies. The second is the kind of comparison Part 3 makes with salary by location, where the 215 placed rural participants average 68,172 against 62,503 for the 1,697 urban ones. The third needs two numeric columns, such as attendance against salary among the placed. It is the one most often left out, because a correlation can be computed without drawing anything.</p>
<p>That is a mistake worth avoiding. A correlation is a single number between -1 and 1 that measures how close two columns come to a straight-line relationship, with 0 meaning no straight-line relationship at all. Attendance correlates with placement at -0.0496, and a figure that close to zero is consistent with several different pictures: no relationship, or a relationship that rises and then falls, which averages out to nothing. The correlation does not distinguish them. The scatterplot does.</p>
<p>In a crosstab you hold the row category still; in a group comparison you hold the group still. A scatterplot is different, because every pair is drawn, which is why it is the one to start with when both columns are numbers.</p>
""" + ask('Which of the three does this pair of columns call for, and have I looked at the shape before computing a single figure?')
+ src('Reading Note 3, section 9.'))

s7 = sec('s7', '5.7', 'Three columns, and why the third can reverse the answer', """
<p>Four trainers, one hundred participants each. The placement rates rank them cleanly.</p>
""" + table(['Trainer', 'Placed overall', 'Within Bachelors', 'Within High School', 'Bachelors in intake'], [
    ['Okonkwo', '68%', '75%', '40%', '80'],
    ['Haddad', '66%', '80%', '45%', '60'],
    ['Silva', '64%', '85%', '50%', '40'],
    ['Mensah', '62%', '90%', '55%', '20'],
]) + """
<p>Read the overall column and Okonkwo is the best trainer and Mensah the worst. Read the two within-group columns and the order is exactly reversed: Mensah is the best with Bachelors participants and the best with High School participants. Mensah is better with both kinds of participant and worse overall.</p>
<p>The intake column is the reason, and one line of arithmetic shows it. Okonkwo's overall rate is just his two within-group rates weighted by his intake: 0.75 times 80 plus 0.40 times 20 is 68. Mensah's is 0.90 times 20 plus 0.55 times 80, which is 62. Give Mensah Okonkwo's intake instead, and she scores 0.90 times 80 plus 0.55 times 20, which is 83, far above Okonkwo's 68.</p>
<p>Across all 400 participants, Bachelors are placed at 80 percent and High School at 50 percent. A trainer sent more Bachelors participants will therefore post a higher overall rate whatever they do, so the overall figure measures the intake as much as the trainer.</p>
<p>Homework 3 was the same shape. Team A resolved 71.9 percent of its tickets within the service level against Team B's 65.6, so Team A looks better. Within Complex tickets Team B is ahead, 58.3 against 50.0, and within Simple tickets Team B is ahead again, 87.5 against 79.2. Team B was handling 24 Complex tickets against Team A's 8.</p>
""" + lost('A reversal is evidence that the third column matters to the comparison. It does not show that the third column is the right one to hold still, and it does not prove the finer answer is the true one. There is no rule that says when to stop adding columns. What settles it is an argument about the situation: the tier was assigned by a triage desk before either team saw the ticket, so holding it still compares like with like. A column the teams themselves controlled would not.')
+ ask('Is there a third column that decides who ended up in each group, and what happens to the comparison when I hold it still?')
+ src('the in-class trainer comparison; Homework 3, where the same reversal appears between the All rows and the tier rows; Reading Note 3, section 10.'))

s8 = sec('s8', '5.8', 'Choosing a chart', """
<p>The chart follows from the same question as the summary: how many columns, and of what kind. One number over categories is a bar chart. One number's distribution is a histogram, and a histogram of the attendance column in 5.3 would have made the two groups plain at once. Two numbers are a scatterplot. A quantity over time is a line.</p>
<p>The choice that does the damage is the one made for appearance. In a bar chart whose axis starts partway up, a small difference looks large. A pie chart of seven slices is unreadable, and a pie chart of two is no more informative than one sentence. If the points have no order between them, a line drawn through them will be read as a trend that is not there.</p>
<p>Every chart is a summary, so everything in this part applies to it. A bar chart of mean attendance by track would give three bars near 93 percent, and the two groups would not appear at all, as they do not in the mean. A chart of a mean is the same mean, drawn larger.</p>
<p>The test before drawing is to say what the reader should be able to see, then check that the chart makes that thing the most visible part of the picture. If the thing you want seen is a difference between two groups, and the eye goes to the overall height of the bars instead, the chart is not answering the question you drew it for.</p>
""" + ask('What should a reader see here, and is that what the eye goes to first?')
+ src('Reading Note 3, section 11.'))

practice = """
<section id="practice">
<h2><span class="n">Practice</span>Check yourself</h2>
<p>All the questions below are worked from one situation. Read it once, then answer with the figures in front of you.</p>
""" + case('The situation', [
    'FPF is writing the salary and attendance page of its annual report, and the director wants one honest paragraph on each. She has given you these figures, computed from the file of 5,000 participants and the 1,912 of them who were placed.',
], table(['Salary of the 1,912 placed', 'Value'], [
    ['Mean', '63,140'],
    ['Median', '60,128'],
    ['Smallest', '16,609'],
    ['Largest', '236,319'],
    ['Tenth percentile', '33,637'],
    ['Ninetieth percentile', '94,447'],
    ['Standard deviation', '25,204'],
    ['Share earning more than the mean', '44.9%'],
], txt=True) + table(['Attendance of all 5,000', 'Participants'], [
    ['76 to 90 percent', '943'],
    ['91 percent', '10'],
    ['92 to 100 percent', '4,047'],
]) + '<p>Mean attendance is 93.13 percent and the median is 95. The lower attendance group peaks at 83 percent and the upper group at 96.</p>') + """
<p>Six questions that mark themselves, then three to write out.</p>
""" + kc(P, 1,
   'The mean salary is 3,012 above the median. What can you infer from that gap about the shape of the salaries?',
   ['A few large salaries are stretching the top of the range',
    'The salaries are evenly spread between 16,609 and 236,319',
    'Most placed participants earn more than 63,140 a year',
    'Roughly half the placed participants were paid nothing'],
   0, 'A mean is pulled by values far from the centre and a median is not. With only 44.9 percent earning above the mean, the mean is not describing a typical person.',
   ['A mean is pulled by values far from the centre and a median is not, and only 44.9 percent earn above the mean.',
    'An even spread would put the mean near 126,000, and the mean and median together.',
    '44.9 percent do, which is a minority.',
    'The smallest salary in the group is 16,609. Nobody placed was paid nothing.']) \
+ kc(P, 2,
   'The director wants one figure for what a typical placed participant earns. Which should she use?',
   ['The mean, 63,140, because it uses every salary in the group',
    'The median, 60,128, with half above and half below',
    'The largest salary, 236,319, as the figure to aim at',
    'The standard deviation, because it describes the whole spread'],
   1, 'Half the placed participants earn above the median and half below. The mean answers a different question, which is what the total wage bill divided by the count comes to.',
   ['It does use every salary, and that is why a few very large ones pull it above what a typical participant earns. It is the right figure for the total wage bill.',
    'Half of the placed participants earn more and half less, and unlike the mean it is not pulled up by the few very large salaries.',
    'The largest value describes one person rather than the group.',
    'A spread figure rather than a centre, so it answers a different question.']) \
+ kc(P, 3,
   'She adds a sentence on the spread. Which is the safest to print?',
   ['Salaries run from 16,609 to 236,319, so a typical one is near the middle of that',
    'Salaries vary by about 25,204 either side of the mean',
    'Eight in ten placed participants earn between 33,637 and 94,447',
    'The mean and the median are close, so the spread must be quite narrow'],
   2, 'The mid-80 percent range comes from the tenth and ninetieth percentiles and is not moved by one very large salary. The full range is decided by two people, and the middle of it, about 126,000, is nowhere near the mean or the median.',
   ['The two figures are right and the conclusion drawn from them is wrong. The middle of that range is about 126,000, nowhere near the mean or the median.',
    'This treats the spread as symmetric about the mean, which it is not, and it understates the top badly.',
    'The tenth and ninetieth percentiles, so eight in ten fall between them, and one very large salary does not move either figure.',
    'Centre and spread are separate. The standard deviation is 25,204 on a mean of 63,140.']) \
+ kc(P, 4,
   'The report says mean attendance was 93.13 percent. Using the attendance table, what is wrong with that as a description of a typical participant?',
   ['It is too high, because 943 participants attended 90 percent or less',
    'It should have been the median, which is the correct centre to report',
    'It falls between two groups and describes neither of them',
    'It was computed across 5,000 rather than across the 1,912 placed'],
   2, '943 participants peak at 83 percent and 4,047 peak at 96. The mean is above everyone in the first group and below most of the second.',
   ['The count is right, and so is the direction for those 943. The fault is that it names one side only: for most of the 4,047 in the upper group the mean is too low.',
    'The median is 95, which falls inside the upper group and describes the 943 no better.',
    '943 peak at 83 and 4,047 peak at 96, so the mean is above everyone in the first group and below most of the second.',
    'Attendance is about all participants, so 5,000 is the right population.']) \
+ kc(P, 5,
   'Which chart would have made the problem in the attendance figure plain fastest?',
   ['A bar chart of mean attendance by track',
    'A scatterplot of mean attendance against mean salary for each track',
    'A line chart of attendance over the course',
    'A histogram of attendance across all 5,000'],
   3, 'In a histogram every value appears on the page arranged by how often it occurs, so two separate peaks are visible at once. A bar chart of means would give three bars near 93, and the two groups would not appear at all, as they do not in the mean.',
   ['Three bars near 93, which reproduces the problem rather than exposing it.',
    'Aggregating to three track means removes the shape you are looking for.',
    'There is no time column here, and a trend line would tell you nothing about the shape of the column.',
    'Every value appears, arranged by how often it occurs, so the two peaks and the gap between them are visible at once.']) \
+ kc(P, 6,
   'A colleague reports that attendance correlates with placement at -0.0496 and concludes there is no relationship between them. What is the flaw?',
   ['The correlation should have been computed among the placed only',
    'A figure near zero also fits a relationship that rises then falls',
    'A negative correlation always means the relationship is backwards',
    'Correlation cannot be computed on a column recorded as a percentage'],
   1, 'A single figure near zero is consistent with several different pictures. Drawing the scatterplot separates them; the correlation on its own cannot.',
   ['Placement is one of the two columns. Among the placed it does not vary, so there is nothing to correlate.',
    'A correlation measures straight-line association, and a relationship that rises and then falls averages out to near zero.',
    'The word always is too strong, and at -0.0496 the sign carries almost no information.',
    'A percentage is a number. Nothing prevents the calculation.']) \
+ score() + """
<h3>Write it out</h3>
<p>The same situation. There is no single correct answer to these. Write yours first, then compare.</p>
""" + resp(
   'Write the paragraph on salary for the annual report. Use no more than three figures in the paragraph itself and say who each one describes. Then, separately, say what the paragraph leaves out.',
   'Among the 1,912 participants who were placed, half earned more than 60,128 and half less. Eight in ten earned between 33,637 and 94,447. The figures describe the participants who found work, not the 5,000 who enrolled, and they are salaries at one moment rather than over a career. What the paragraph leaves out is the shape above the ninetieth percentile: a small number of very large salaries, the highest of them 236,319, which is why the mean is not quoted here. If a reader wants the total the programme produced, the mean is the right figure and this paragraph is the wrong one.') \
+ resp(
   'The director asks you to report a single mean attendance figure, because the report has room for one number. Explain why you would refuse, and say what you would print instead in the same space.',
   'A single mean would be 93.13 percent, and almost nobody attends 93 percent. There are two groups: 943 participants around 83 percent and 4,047 around 96. The mean is above every participant in the first group and below most of the second, so it describes neither, and a reader would take it as the typical participant. In the same space I would print: most participants attended around 96 percent, and about one in five attended around 83. That is two numbers instead of one, it is the same length in print, and from it the reader learns there are two kinds of participant, which is the thing the programme would want to act on.') \
+ resp(
   'Using the trainer table in 5.7: Mensah has the lowest overall placement rate of the four and argues that she is in fact the best trainer. Set out the argument she should make, the figures she needs, and the one objection that would defeat it.',
   'She should argue that her overall rate is measuring her intake. The figures she needs are the placement rate within each education level for every trainer, and the composition of each trainer\'s intake. On the file she is at 90 percent within Bachelors and 55 percent within High School, the best of the four on both, while only 20 of her 100 participants held a Bachelors degree against 80 of the highest-ranked trainer\'s. Since Bachelors participants are placed at 80 percent overall and High School participants at 50, a trainer given more Bachelors participants will rank higher whatever they do. The objection that would defeat it is that she arranged her own intake. Holding education still is only fair if education was assigned independently of the trainer. If an admissions or assignment process gave her the harder participants, the comparison is fair. If she arranged it herself, the comparison is hers to explain.') + """
</section>
"""

PAGE = {
    'file': 'part5.html', 'nav': 'part5',
    'title': 'Part 5. Summarising, and what it costs', 'sub': 'Part 5',
    'dek': 'What did this summary leave out, and would the decision change if I could see it?',
    'toc': [('s1', '5.1 Why summarise at all'), ('s2', '5.2 Centre, spread, and which centre'),
            ('s3', '5.3 When one mean represents nobody'), ('s4', '5.4 Spread is a constructed measure'),
            ('s5', '5.5 A continuous world recorded in steps'), ('s6', '5.6 Two columns, three ways'),
            ('s7', '5.7 Three columns, and the reversal'), ('s8', '5.8 Choosing a chart'),
            ('practice', 'Practice')],
    'body': intro + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + practice,
    'prev': ('part4.html', 'Part 4. Who is in the file'),
    'next': ('closing.html', 'Closing'),
}
