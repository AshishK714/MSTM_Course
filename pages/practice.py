from build import sec, ask, src, box, table, kc, resp, score, lost, case

P = 'ps'

intro = """
<p>One dataset you have not seen, and four kinds of task. The four are the shapes the homeworks used: sort items and justify the sorting, compute a figure and apply a stated rule to it, write the strongest honest case on each side, and audit somebody else's claim. Everything on this page draws on Parts 1 to 5, and none of it needs the FPF file.</p>
<p>Read the description once. Then work the questions with it in front of you, and write the four tasks out properly rather than in your head, because you find out whether you can use an idea under exam conditions only by writing it out.</p>
"""

thecase = case('The dataset', [
    'Verdance Bikes runs a public bike-share scheme for a city council. Members take a bike from a docking station, ride, and return it to another docking station. The council pays Verdance a fee per quarter and wants to know whether the scheme is worth renewing.',
    'You have the trip file for one quarter, April to June, 91 days. It has one row for each trip that ended at a docking station, with the bike, the starting station, the ending station, the start time, the duration in minutes, the membership type, and whether the bike was flagged for repair when it was returned. Every rider holds an account, annual or casual, so the registered members below include both kinds, and so does the count of those who rode. Vans that move bikes between stations are logged separately and produce no trip row.',
], table(['What was recorded', 'Value'], [
    ['Trips in the file', '412,000'],
    ['Of those, by annual members', '318,000'],
    ['Of those, by casual members', '94,000'],
    ['Registered members', '18,400'],
    ['Members who took at least one trip', '11,040'],
    ['Bikes in the fleet', '1,200'],
    ['Docking stations', '90'],
    ['Trips ending with a repair flag', '2,140'],
    ['Trips starting at the busiest station', '9,800'],
    ['Van moves between stations', '27,500'],
], txt=True) + table(['Trip duration', 'Trips'], [
    ['4 to 14 minutes', '289,000'],
    ['25 to 45 minutes', '123,000'],
], caption='Mean duration is 16.3 minutes and the median is 11.') +
 '<p>Three things are true of the scheme and are not in the trip file. A bike left outside the network is not returned to a dock, so the trip has no end and no row; there were 3,100 recoveries of bikes from the street during the quarter. Bikes withdrawn for repair are out of the fleet until they are fixed, and the file records the flag but not the days lost. And the council cares about trips that would otherwise have been made by car, which nobody has ever measured.</p>')

checks = """
<section id="checks">
<h2><span class="n">Check yourself</span>Eight questions</h2>
<p>These mark themselves. They run across all five parts, in no particular order, as the exam will.</p>
""" + thecase + kc(P, 1,
   'What does one row of the trip file represent?',
   ['One member of the scheme during the quarter',
    'One bike during the quarter, with its trips summarised',
    'One trip that ended at a docking station',
    'One ride taken by a member, whether or not it ended at a dock'],
   2, 'The file was built from dock returns, and the 3,100 street recoveries are rides of a kind that produced no row. A row is not a member and not a bike either: one member and one bike each appear on many rows.',
   ['One member appears on many rows, one for each trip taken.',
    'One bike appears on many rows too, and nothing in the file summarises a bike.',
    'The file was built from dock returns, so what a row records is a trip that ended at a dock.',
    'A ride that ended anywhere else produced no row. The 3,100 street recoveries are rides of that kind.']) \
+ kc(P, 2,
   'Verdance wants to decide, for each station and each hour, whether to send a van. What does that decision need?',
   ['One row per station and hour, which this file can be folded into',
    'One row per bike, which this file does not contain',
    'One row per member, which this file does not contain',
    'Nothing more; 412,000 trips is enough for any question about stations'],
   0, 'Each trip has a start station and a start time recorded on it, so the trips can be counted into station-hours. The finer rows already exist, which is what makes the coarser table available.',
   ['Each trip has a start station and a start time on it, so the trips can be counted into station-hours.',
    'A bike row could be built from these trips as well, and a bike is the wrong unit for this decision.',
    'A member row could be built too, and a member is the wrong unit for sending a van.',
    'The decision needs rows at the level the decision varies, which is the station and the hour, and no number of trips supplies that on its own.']) \
+ kc(P, 3,
   'Verdance reports trips per bike per day, which is 3.77. For the council\'s decision, what role does that figure play?',
   ['An outcome for the council, which is paying for the trips themselves',
    'A signal, watched because the thing the council wants arrives later',
    'Context, because Verdance cannot change how often bikes are used',
    'A mechanism, because it explains why members keep their membership'],
   1, 'The council wants trips shifted out of cars, and that is not in the file. Trips per bike is watched instead, and it can be raised by shrinking the fleet. A mechanism is something that happens inside a person, so D is the wrong kind of thing: a count is not a reason a member rides again.',
   ['The council is buying car trips replaced, not trips as such, so trips are not wanted for their own sake.',
    'What the council wants is not in the file, so this is watched instead, and it can be raised by shrinking the fleet.',
    'Verdance can change it, by rebalancing, by pricing and by the size of the fleet.',
    'A mechanism is something that happens inside a person. A count is not a reason a member rides again.']) \
+ kc(P, 4,
   'A councillor asks how much the scheme is used per member. What should the report do?',
   ['Divide by the 1,200 bikes, which are what the council pays for',
    'Divide by the 11,040 who rode, and print 37.3 trips each',
    'Divide by the 18,400 registered, because that is who it is for',
    'Give either figure, and say which denominator produced it'],
   3, '412,000 over 18,400 is 22.4 and over 11,040 is 37.3. Both are honest and they answer different questions. What is not honest is printing one without saying which.',
   ['That gives trips per bike, which answers a question about the fleet rather than about members.',
    '37.3 is right, and a reader given it alone would not learn that 7,360 members did not ride at all.',
    '22.4 is right too, and a reader given it alone would not learn that the people who do ride ride far more often.',
    'Both are honest and they answer different questions. What is not honest is printing one without saying which.']) \
+ kc(P, 5,
   'Duration is measured from the moment the bike leaves one dock to the moment it enters another. What does that measure include?',
   ['Only the time the member was riding the bike',
    'Time the bike was stopped and locked partway through',
    'The time the member waited for a bike to become free',
    'Time the bike spent being moved between stations by van'],
   1, 'Nothing in the measurement separates riding from standing. A member who stops for twenty minutes produces a long trip, and so does a member who rides for twenty minutes. The wait for a bike happens before the bike leaves the dock, so C is outside the measured interval, and van moves are logged separately, so D is not in this column at all.',
   ['Nothing in the measurement separates riding from standing.',
    'A member who stops for twenty minutes produces a long trip, and so does one who rides for twenty minutes.',
    'The clock starts when the bike leaves the dock, so any wait before that is outside the interval.',
    'Van moves are logged separately and produce no trip row.']) \
+ kc(P, 6,
   'The 3,100 street recoveries produced no trip row. What follows for a figure computed from the file?',
   ['It is wrong, and should be recomputed once those trips have been added in',
    'It is unaffected, because 3,100 is small against 412,000',
    'It describes trips that ended at a dock, which is a narrower group',
    'It overstates duration, because those trips were the longest ones'],
   2, 'Those rides are not rows, so nothing computed from the file can describe them. They cannot be added back either, because no end time was ever recorded.',
   ['They cannot be added back, because no end time was ever recorded for them.',
    'What counts is that the figures describe a group narrower than the label suggests.',
    'Those rides are not rows, so nothing computed from the file describes them.',
    'Nothing is known about how long they lasted, which is the whole difficulty.']) \
+ kc(P, 7,
   'Mean duration is 16.3 minutes and the median is 11. Using the duration table, what is the best account of that gap?',
   ['A recording error in the longer trips has inflated the mean',
    'Most trips last about 16 minutes, with a few much shorter and a few longer',
    'Duration is recorded in whole minutes, which raises the mean',
    'There are two groups of trips, and 16.3 describes neither well'],
   3, '289,000 trips run 4 to 14 minutes and 123,000 run 25 to 45. 16.3 is between the two groups, and no trip in the file lasts 16 minutes.',
   ['Nothing suggests an error. The long trips are a real group of 123,000.',
    'This is the single-centre reading that the table rules out. No trip in the file lasts 16 minutes.',
    'Rounding to whole minutes does not move a mean by five.',
    '289,000 trips run 4 to 14 minutes and 123,000 run 25 to 45, so 16.3 is between the two groups.']) \
+ kc(P, 8,
   'Verdance proposes one chart for the council showing mean duration by month. What would the council not be able to see?',
   ['Whether the mean in April was higher than the mean in June',
    'That the trips fall into two groups of very different length',
    'Which of the three months had the longest mean trip',
    'The direction of the change in mean duration across the quarter'],
   1, 'A mean per month is three numbers, so A, C and D can all be read straight off the chart. The two groups are inside every month, and they are visible at once in a histogram of duration.',
   ['Read the April bar against the June bar and you have it.',
    'The two groups are inside every month. A histogram of duration would make them visible at once.',
    'Whichever of the three bars is tallest answers this.',
    'Reading the three bars from left to right gives the direction of the change.']) \
+ score() + """
</section>
"""

tasks = """
<section id="tasks">
<h2><span class="n">Four tasks</span>Write these out</h2>
<p>The same dataset. Each task is one of the four shapes the homeworks used. There is no single correct answer; write yours before opening the model.</p>

<h3>1. Sort and justify</h3>
""" + resp(
   'Sort these six into the five roles from Part 1, which are activity, signal, outcome, context and mechanism, and give a reason for each that is not a restatement of the item. Two of them are close calls; say which and why. The items: bikes moved between stations by van; trips per bike per day; the number of car trips the scheme replaces; a wet April; a member coming to feel confident riding in traffic; the repair flag.',
   'Bikes moved by van is an activity. It is the thing Verdance can change, and each move costs money. Trips per bike per day is a signal. Nobody wants it for itself, and Verdance can raise it by shrinking the fleet, which is the weakness of any signal. Car trips replaced is the outcome. It is what the council is buying, it is wanted for its own sake, and it is measured by nobody. A wet April is context. It affects how many trips are taken, and nobody can change it within the quarter. Coming to feel confident in traffic is a mechanism. It is what has to happen inside a person between the activity and the outcome, and it explains why a member rides again. The close calls are the repair flag and trips per bike. The repair flag is an activity from the workshop\'s side, since somebody decides to flag and fix, and a signal from the council\'s side, since the council can use a rising flag rate as a proxy for a fleet in worse condition. Trips per bike is a signal for the council and closer to an outcome for Verdance, whose fee may depend on it.') + """

<h3>2. Compute and choose against a rule</h3>
""" + resp(
   'The council has a rule: it will fund a new docking station at a location only if the stations already there are handling more than 5 percent of all trips between them. Verdance points at the busiest station, with 9,800 trips, and asks for a new station beside it. Work out the figure you can compute from what you have, say whether it settles the rule, and say what else you would need before applying it.',
   '9,800 of 412,000 is 2.4 percent of starts, so on starts alone the rule is not met. But the rule is about the stations already at a location, plural, so the figure to compute is the share of trips starting at all the stations near that one, which the file can give by grouping the start station column. Three things would settle it. Whether handling counts arrivals as well as departures, since every row has an ending station too, and counting both could roughly double the figure. Whether the 5 percent is of all trips or of trips in that part of the city, since 5 percent of a citywide total is a high bar that perhaps no location meets. And whether the station is busy because demand is high or because it is one of the few stations in that area, which is the difference between a rule that picks out where demand is high and one that funds the places already funded.') + """

<h3>3. Two honest reports</h3>
""" + resp(
   'Write the strongest honest case that the scheme is working, then the strongest honest case that it is not, using only the description. Then say which you believe and why. You may compute from the figures given; you may not bring in a figure from anywhere else.',
   'Working: members took 412,000 trips in 91 days, which is 3.77 trips per bike per day across a fleet of 1,200. Annual members took 318,000 of those trips, 77.2 percent, so most of the demand is repeat use by committed members. Only 2,140 trips, about one in 200, ended with a repair flag, so the bikes are in reasonable condition. Not working: of 18,400 registered members, only 11,040 took any trip at all, so 40 percent of the people who signed up did not use it in three months. The median trip is 11 minutes, which is short enough that many could have been walked. Vans made 27,500 moves, roughly 23 per bike in the quarter, which is a substantial hidden cost. And there were 3,100 recoveries of bikes from the street. I believe the second case is closer, with one reservation. Both cases are about use. Neither is about what the council is paying for, which is car trips replaced. Nothing in this file measures that, so on the question actually asked the file cannot settle it either way, and the honest answer to the council is that the evidence they need was never collected.') + """

<h3>4. Audit a claim</h3>
""" + resp(
   'A consultant reports to the council: "Average trip duration is 16.3 minutes, and 77 percent of trips are taken by annual members, so the scheme has built a base of committed regular users. We recommend renewal." Audit it. Say what is true, what does not follow, and what you would ask for.',
   'True: 16.3 minutes is the mean of the duration column, and 318,000 of 412,000 is 77.2 percent. What does not follow: the mean is the wrong summary here, because the trips fall into a group of 289,000 at 4 to 14 minutes and a group of 123,000 at 25 to 45, so 16.3 describes no trip in the file, and the consultant writes as though there were a typical rider. The 77 percent is a share of trips, not of people, and a small number of heavy users can produce it; it is consistent with a committed base and equally consistent with about 1,800 commuters riding twice a day while the rest ride rarely. The membership figures are evidence against it: 7,360 of 18,400 registered members took no trip at all. And renewal depends on car trips replaced, which is not in the file. I would ask for the spread of trips per member rather than the total alone, so the concentration is visible; for the duration distribution rather than its mean; and for whatever the council has on how members travelled before they joined, which is the only thing that bears on the recommendation.') + """
</section>
"""

PAGE = {
    'file': 'practice.html', 'nav': 'practice',
    'title': 'Practice set', 'sub': 'Practice set',
    'dek': 'One dataset you have not seen, eight questions and four written tasks.',
    'toc': [('checks', 'Check yourself'), ('tasks', 'Four tasks')],
    'body': intro + checks + tasks,
    'prev': ('appendix.html', 'Appendix. Many trials'),
    'next': None,
}
