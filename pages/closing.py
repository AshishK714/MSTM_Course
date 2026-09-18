from build import sec, ask, src, box, table

P = 'cl'

intro = """
<p>One move runs through Parts 2 and 5, and the five questions below run through all five parts.</p>
"""

s1 = sec('s1', 'C.1', 'Conditioning, in four places', """
<p>Conditioning is choosing what to hold constant so that what varies becomes visible. It appears four times in this guide, under a different name each time.</p>
""" + table(['Where it appeared', 'What is held constant', 'What becomes visible'], [
    ['Choosing what one row is (2.1)', 'everything folded into the row', 'differences between rows, and nothing finer'],
    ['Choosing the level to decide at (2.3)', 'the group a participant belongs to', 'whether mentorship works differently inside different groups'],
    ['Choosing the percentage direction (2.4)', 'the group you can act on', 'what tends to follow when you act on it'],
    ['Holding a third column still (5.7)', 'a column distributed unevenly across the groups compared', 'whether the first comparison survives'],
]) + """
<p>In each case something is deliberately frozen. Choosing a row, you freeze whatever was folded into it. Comparing within one education level, you freeze education, so the difference you read is not a difference in schooling. Reading a row percentage, you freeze the row group and read across it. Splitting by tier, you freeze the difficulty of the work.</p>
<p>Three of the four fail in the same way: you hold the first column constant and the second does not vary inside it. Hold location at rural, and mentorship does not vary, because all 637 of the participants who went without mentorship are urban. Take a row percentage across a group whose members all had the same outcome, and there is nothing to read. Hold the tier still, and a team that handled only one tier has an empty cell in the other.</p>
<p>The first fails differently. A comparison between modules has no row to stand on, because folding runs one way and the finer row was never recorded. Check for the variation before running the comparison, because a comparison computed on an empty cell looks like any other comparison.</p>
<p>A question that looks like four topics is usually one topic asked four ways, and you begin the answer the same way each time: name what is being held constant, and ask what that choice makes invisible.</p>
""" + ask('What am I holding constant here, and does the thing I want to see actually vary once I have?')
+ src('this draws together 2.1, 2.3, 2.4 and 5.7.'))

s2 = sec('s2', 'C.2', 'The five questions', """
<p>Reading Note 1 closes with five questions to ask before applying any technique. Reading Note 3 extends the third and the fourth. This guide adds a line to the first, the second and the fifth.</p>
""" + table(['The question', 'What it establishes', 'What is added, and by whom'], [
    ['1. What slice of reality is this dataset a record of?',
     'the time window, the setting, and which units are included or excluded',
     'ask what filtered the rows in, and whether the decision applies to people who passed that filter (this guide, Part 4)'],
    ['2. What is a row, exactly?',
     'the unit of analysis and the level of granularity',
     'the comparison chooses it, and folding runs one way (this guide, Part 2)'],
    ['3. What do the numbers mean?',
     'units and scaling conventions, and whether baseline differences require normalising',
     'establish the type of each column before summarising it, because the type decides which summaries are legal; ordered categories can be ranked but not safely averaged; where a metric had to be chosen, say what claim about the world that choice makes (Reading Note 3)'],
    ['4. What is the pattern, and what story are we tempted to tell?',
     'observed association separated from causal interpretation, and the alternative explanations that fit the same data',
     'a two-column pattern is not settled until you have tried the third columns that could overturn it; when a summary and its parts disagree, the summary is usually measuring the composition of the groups rather than the thing you named (Reading Note 3)'],
    ['5. What is measured directly, and what is inferred?',
     'the proxies in use, what they are assumed to represent, and what they might miss',
     'name the four decisions behind the column, and write them down where the next person will find them (this guide, Part 3)'],
], txt=True) + """
<p>Reading Note 3 adds one more. This guide places it after the other five: before reporting any summary, say what it left out. If you cannot say what was lost, you do not yet understand what you computed.</p>
<p>Questions 1 and 2 are the ones that cannot be repaired later. If the rows are the wrong people, or at the wrong grain, no amount of care with questions 3 to 5 recovers anything. That is why Part 2 comes early, and why a question that looks like it is about a number is so often answered by looking at the rows instead.</p>
<p>In an exam answer, naming the question you are applying is worth as much as the answer itself, because a marker can then see which of the five you think the situation depends on.</p>
""" + ask('Can I say, in one sentence, what this number left out?')
+ src('Reading Note 1, section 12; Reading Note 3, section 12, which extends the third and the fourth and adds the last.'))

PAGE = {
    'file': 'closing.html', 'nav': 'closing',
    'title': 'Closing. One move, four times', 'sub': 'Closing',
    'dek': 'What the five parts have in common, and the questions to carry into the exam.',
    'toc': [('s1', 'C.1 Conditioning, in four places'), ('s2', 'C.2 The five questions')],
    'body': intro + s1 + s2,
    'prev': ('part5.html', 'Part 5. Summarising, and what it costs'),
    'next': ('appendix.html', 'Appendix. Many trials'),
}
