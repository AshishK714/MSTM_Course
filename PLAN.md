# Midterm Study Guide: Content Plan

Exam: Thursday 24 September, in class. Guide promised to students by Thursday 17 September, end of day. It is now Friday 18 September.

## A. What this is

One document that replaces nothing and consolidates everything. Reading Notes 1 to 3 and the Class 4 note stay posted for depth. The guide is what students read the night before the exam: every examinable idea at one section each, the worked example named rather than re-taught, and practice built into every part.

Format: one folder, one stylesheet, one navigation, one HTML file per part, hostable as a static site. Same design system as the reading notes. Practice items are hash-checked in the page so no answers sit in the source, plus open prompts with a model answer behind a reveal.

Three rules for the whole document:

1. Nothing said twice. Where two sources cover one idea, the guide picks the clearer example and names the other in one line.
2. Practice uses the examples students already know. The exam re-clothes every one of them.
3. Every figure is recomputed from FPF_Case_Study_data.csv or fpf_trainer_demo.csv. Figures in this plan have been verified against the files.

## B. The five ideas, and the spine

| Part | Idea | The question a student should be able to ask |
|---|---|---|
| 1 | The decision and the roles | What job is this column doing for this decision-maker? |
| 2 | What one row is | What does one row represent, and did the comparison choose it? |
| 3 | What a column measures | What did this number stand in for, and what did that leave out? |
| 4 | Who is in the file | What filtered these rows, and what does that make the number mean? |
| 5 | Summarising, and what it costs | What did this summary throw away, and would the decision change if I could see it? |

The spine, stated in the closing section: conditioning is one move that has appeared in four costumes. Choosing what one row is. Choosing which level to decide at. Choosing which percentage direction to read. Holding a third column still. Each is picking what to hold constant so that what varies becomes visible.

## C. Source review, one by one

| Source | What it contains | Into the guide | Left out, and why |
|---|---|---|---|
| Reading Note 1 (Data Literacy Foundations) | What a dataset represents and what it leaves out; sections 1 to 7 ran as the working session (what is not in the file, the tables that died, the mentorship trap, two learners earning 60,000); section 6 three placement rates; section 12 the five questions | Part 1 framing; the five questions as the closing checklist; "what is not in the file" feeds Part 4 | The narrative arcs. Students have read them; the guide names them |
| Reading Note 2 (Rows and Columns) | Unit chain (decision, analysis, observation) and one-way folding; additivity and averaging averages; aggregator encodes a theory; denominators; comparability (two learners, three decision-makers); Robinson; closing questions | Part 2 sections 2.1; Part 3 sections 3.3, 3.4, 3.9 | Data model and many-to-many, unless it was taught in class. Aggregator chain stays as one line under 3.4, not a section |
| Class 4 deck and interactive note | Comparison decides the level (three tables from one file); the ladder; mentorship pivot in three directions; careful with the average (53.7 vs 38.2); facts and dimensions as a role; no trainer identifier; what "better" would mean; league table and reversal; text-typed percentages; which average salary (63,140 vs 24,145); the employed chain | Almost all of it. Part 2 sections 2.2 to 2.4; Part 1 section 1.3; Part 3 sections 3.1 to 3.5; Part 5 section 5.7 | Nothing of substance. Slide 20's homework reference is stale |
| Reading Note 3 (Describing Data) | Why summarise; centre and spread; mean vs median; percentiles and the bimodal column; building the spread metric; what the metric assumes; variable types and binning; two columns; three columns; charts; questions added | Part 5, compressed to about a third of its length. Section 2 (facts and dimensions) merges into Part 1 | The calorie exercise as a walkthrough. Keep its conclusion: squaring is a claim about the world. Coefficient of variation becomes one line |
| Class 7 activities deck | Seven activities: three honest placement rates; the same mistake five times; rural pays better; everything engagement could have been; who is not in this file; rank columns by trust; two columns both in percent. Plus six closing questions | Part 3 sections 3.3, 3.4, 3.6, 3.7, 3.8, 3.9; Part 4 section 4.1; Part 5 section 5.7 (rural by education). Closing questions become practice prompts | Nothing. This deck is the closest thing to a Part 3 draft that exists |
| Class 7 and 8 instructor notes (docx) | Proxies and the label; the data dictionary and derived variables; the rural centre and selection as a filter; signaling; survivorship and Simpson's tied to HW 3; variable types; a continuous world recorded discretely; grading scales and survey scales; age banded, Titanic, cutoffs; why summarise (HBS); mean, median, mid-80% range; bimodal attendance; die throws; luck and adaptation | Part 3 section 3.10; Part 4 sections 4.2, 4.4; Part 5 section 5.5 (recording, scales, cutoffs); mid-80% range added to 5.2; die throws as the appendix | Luck cancelling and hedonic adaptation. Good teaching, not examinable, and they would read as filler in a study guide |
| HW 1 (Building Blocks Sort) | Fifteen items into five blocks with a reason; perspective as who is deciding and what | Part 1 section 1.3 and its practice | The item list itself |
| HW 2 (bank marketing, grain) | The row is one customer's final persuasion attempt, not one call, established by non-monotonic campaign counts | Part 2 section 2.5 | The PyAnalytica mechanics |
| HW 3 (Northgate) | Two teams, hidden severity tier, portal closing 40 enterprise contacts before they became tickets; two honest reports; recording change; audit of a third-party report | Part 4 section 4.3 (survivorship); Part 5 section 5.7 (the reversal); the audit format as a practice item | The exhibits and pivot instructions. HW 3 closed Wednesday 16 September, so naming survivorship and Simpson's paradox in the guide is safe |

## D. The guide, section by section

Each section is one idea, one named example with its real numbers, and one practice item. Target length: 150 to 250 words of prose per section. Sources in brackets.

### Part 1. The decision and the roles

| # | Section | Example | Source |
|---|---|---|---|
| 1.1 | A business is a conversion of activities into outcomes; five blocks | FPF mapping sheet | RN1, Class 2 |
| 1.2 | Signal versus outcome: would you want it if it led nowhere | Employer feedback vs community trust | RN1, Class 2 |
| 1.3 | A role is not a property: who is deciding and what they are deciding | attendance_pct as a fact in one question and a dimension in the next | HW 1, Class 4 slide 9, RN3 §2 |
| 1.4 | Facts and dimensions: facts add, dimensions slice, ratios were already divided | FPF column table; partnership strength is ordered; sector blanks are structural | Class 4 slide 8, RN3 §2 |

Practice: a sort with reasons; the decision-change item (same eight columns, two decisions, which roles move and which column now does no work).

### Part 2. What one row is

| # | Section | Example | Source |
|---|---|---|---|
| 2.1 | The unit chain: decision, analysis, observation; folding runs one way | Advertising by customer vs customer within time of day | RN2 §2, Class 4 slide 3 |
| 2.2 | The comparison decides the level | Three questions, three tables from one file: 5,000 learner rows, 3 track rows, 4 partnership rows; the track table cannot answer the mentorship question | Class 4 slides 4 to 6 |
| 2.3 | The ladder: programme, group, individual | Whole programme 38.90 vs 33.75; by education High School +9.68, Masters +4.95, Bachelors +2.10; individual level unsupported because mentorship does not vary within a person; and every unmentored learner is Urban, 1 to 3 years, Mid AI exposure, so Rural has no comparison group either | Class 4 note, computed |
| 2.4 | Conditioning: grand, column and row percent | Mentorship on rows, employed on columns. Row % 38.90 vs 33.75; column % 88.76 vs 86.33 because 87% of everyone was mentored. The direction is decided by the layout, not by a rule | Class 4 note, computed |
| 2.5 | Grain in a real file | One row per customer's final attempt, not one per call; how the campaign counts gave it away | HW 2 |
| 2.6 | Two things called granularity | Row granularity (what one row is, chosen by the comparison) against column granularity (how finely a value is recorded, chosen by cost and use). Hands the second to 5.5 | New, bridging |

Practice: state the row for three described decisions; pick the lowest level the data supports and say what one rung up loses; a crosstab with the intervention variable on the columns, which percentage answers the decision.

### Part 3. What a column measures

| # | Section | Example | Source |
|---|---|---|---|
| 3.1 | Form: a recorded thing whose form somebody chose | attendance_pct and digital_lit_score stored as text with a percent sign; mean is 93.13 once converted | Class 4 slide 17 |
| 3.2 | Structural blanks are not missing data | salary blank for exactly the 3,088 not employed; employment_type and sector likewise | Class 4 slide 18, RN3 §2, Activity 5 |
| 3.3 | Denominators | 38.24 placed of all; 28.88 full-time of all; 75.52 full-time of placed. Salary 63,140 among employed vs 24,145 across everyone | Activity 1, Class 4 slide 18, RN1 §6, RN2 |
| 3.4 | What can be added up | Same mistake five times: gender +15.48 from a group of 13; partnership strength off by 0.03 because its groups are equal. The rule is about group sizes | Activity 2, Class 4 slide 7, RN2 |
| 3.5 | The operationalization chain | employed: definition, instrument, rules, timing; two analysts who agree completely still produce different numbers | Class 4 slide 19, RN2 |
| 3.6 | What a measure records and what it leaves out | Eight ways to be engaged, one recorded; who attendance describes badly | Activity 4, docx |
| 3.7 | Proxies, and being recordable is not being a good measure | Four columns ranked by trust; correlations with placement of -0.05, 0.04, 0.03; employed is the only one not standing in for something else | Activity 6, docx |
| 3.8 | Scale | Two percent columns, ranges 24 and 49, sd 5.21 and 11.88; 84% of the readiness score comes from one column; partnership strength coded 1 to 4 averages to 2.57, which means nothing | Activity 7, RN3 §8 |
| 3.9 | Comparability | Two learners, three decision-makers, three answers; 68,172 rural vs 62,503 urban when living costs are not in the file | RN2 §7, Activity 3 |
| 3.10 | Write it down | Derived variables recorded in a data dictionary; ask for one when you receive data | docx |

Practice: the proxy item (a concept, two candidate columns, what each misses, who it disadvantages, the dictionary entry); a denominator call for a named decision-maker; the "filling structural blanks with None" question from the activities deck.

### Part 4. Who is in the file

| # | Section | Example | Source |
|---|---|---|---|
| 4.1 | A blank cell tells you it is blank; a person who is not there tells you nothing | IDs run P0001 to P5000 with no gaps; who never appears: considered and did not enrol, left before an outcome, employers who declined | Activity 5 |
| 4.2 | Selection as a filter | Rural learners in the file bore the travel cost; a rural centre would enrol different rural people; the number describes the ones who survived the cost | docx |
| 4.3 | Survivorship | The portal closes simple enterprise queries before they become tickets, so enterprise tickets are the hard ones | HW 3 |
| 4.4 | Filters that signal | When motivation cannot be observed, the degree carries information because of what it cost to get | docx |
| 4.5 | Everyone here enrolled and completed | Every number in the file describes completers | Activity 5 |

Practice: a new filter scenario; what would change if the filter were removed; the HW 3 audit format on a short third-party claim.

### Part 5. Summarising, and what it costs

| # | Section | Example | Source |
|---|---|---|---|
| 5.1 | Why summarise, and the question to carry | Five thousand values to two; what did this throw away | RN3 §1, HBS class report |
| 5.2 | Centre, spread, and which centre | Salary mean 63,140 vs median 60,128 and what the gap says; the mid-80% range as the safe report | RN3 §3 to 4, docx |
| 5.3 | Percentiles, and the column with two clusters | Attendance mean 93.13 sits in the empty middle; 941 learners between 76 and 90 | RN3 §5 |
| 5.4 | Spread is a constructed metric | Squaring claims a large deviation is worse than proportionally worse; one paragraph, not the walkthrough | RN3 §6 to 7 |
| 5.5 | Types, and a continuous world recorded discretely | Continuous, discrete, ordinal, nominal and what each permits; grading scales across countries; 1 to 3 vs 1 to 10; age banded loses variation; when the cutoff is real (Titanic, legal thresholds) binning matches the world, otherwise it hides it | RN3 §8, docx |
| 5.6 | Two columns, three ways | Crosstab, group comparison, scatterplot; hold one still and watch the other | RN3 §9 |
| 5.7 | Three columns, and why the third can reverse the answer | Trainers 68, 66, 64, 62 reversing to 90, 85, 80, 75 within Bachelors; rural pays better until education is held still; Northgate's tiers; what the split does not prove; no stopping rule | RN3 §10, Class 4 slides 12 to 16, Activity 3, HW 3 |
| 5.8 | Choosing a chart | The type follows from how many columns and of what kind; every chart hides what it summarised | RN3 §11 |

Practice: a table where the aggregate and the subgroups agree, does the composition argument apply; mean, median or mid-range for a described distribution; which chart answers this question and which flatters it.

### Closing

One section: conditioning as one move, with the four instances named. Then the five questions from Reading Note 1 with the lines Reading Note 3 added, extended by one line each from Parts 3 and 4.

### Appendix. Many trials

The die-throw table, with the simulation. Opens with one sentence: this is where the course goes next and it is not on the midterm.

### Practice set

A separate file. One unfamiliar dataset described in half a page, then items in the exam's four formats across all five parts. Posted with the guide or one day after.

## E. What the exam takes from this

The guide weights by teaching time, so Part 2 is the longest. The exam does not. Homework has already graded roles, grain, survivorship and the reversal. The exam adds most information on Parts 3 and 4, which nothing graded has touched. Rough exam weights: Part 3 and Part 4 together about half; Parts 1, 2 and 5 share the rest; rows present because everything depends on them, not in proportion to hours spent.

Out of scope, stated in the guide and on the paper: the appendix, sampling, standard error, confidence intervals, hypothesis testing.

## F. Build order

1. Shell: stylesheet, navigation, the practice-item and reveal components, index page with the scope statement.
2. Part 4. Entirely new writing, no dependency on earlier note wording.
3. Part 2. Numbers computed and verified; Class 4 deck in hand.
4. Part 3. Activities deck and Class 4 deck in hand. Needs Reading Note 2 for the chain and comparability wording.
5. Part 5. Compression of Reading Note 3 plus the docx additions.
6. Part 1. Needs Reading Note 1 and the Class 2 sheets for wording.
7. Closing, appendix with the simulator, practice set.

Still needed from you: Reading Note 1, Reading Note 2, and the Class 4 interactive note, for wording in Parts 1, 2 and 3. Parts 4, 5 and the shell can start now.

## G. Two things to fix before the guide goes out

1. The activities deck says the midterm is Tuesday 24 September. The 24th is a Thursday. Some students will have written down Tuesday the 22nd. Say which in the guide's first line and in an announcement.
2. The same slide promised the guide by Thursday end of day. Students are waiting. A one-line announcement giving a new time costs less than silence.

One small thing in the trainer file: mentorship varies across trainers from 83 to 91 percent. Not large enough to matter, but a careful student will find it. The guide should say the file was built with education as the intended third column, or not mention mentorship in that file at all.
