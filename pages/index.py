from build import table, built

PARTS = [
    ('part1.html', 'Part 1', 'The decision and the roles',
     'What job is this column doing, for this decision, for this decision-maker?',
     ['A business is a conversion of activities into outcomes', 'Signal and outcome', 'A role is not a property',
      'Facts and dimensions']),
    ('part2.html', 'Part 2', 'What one row is',
     'What does one row represent, and did the comparison choose it?',
     ['The unit chain: decision, analysis, observation', 'The comparison decides the level',
      'The ladder: programme, group, individual', 'Conditioning: grand, column and row percent',
      'Grain in a real file', 'Two things called granularity']),
    ('part3.html', 'Part 3', 'What a column measures',
     'What does this number stand in for, and what did that leave out?',
     ['Structural blanks are not missing data', 'Denominators', 'What can be added up',
      'The chain of decisions behind one column', 'What a measure records and what it leaves out',
      'Proxies', 'Scale', 'Comparability', 'Write it down']),
    ('part4.html', 'Part 4', 'Who is in the file',
     'What filtered these rows, and what does the number mean as a result?',
     ['A blank cell and a missing person are different things', 'Selection: the people in the file passed through a filter',
      'Survivorship: cases that were resolved earlier never became rows', 'A filter can be evidence',
      'Every number in this file describes people who enrolled and completed']),
    ('part5.html', 'Part 5', 'Summarising, and what it costs',
     'What did this summary leave out, and would the decision change if I could see it?',
     ['Why summarise at all', 'Centre, spread, and which centre',
      'Percentiles, and the column with two clusters', 'Spread is a constructed metric',
      'Types, and a continuous world recorded in discrete steps', 'Two columns, three ways',
      'Three columns, and why the third can reverse the answer', 'Choosing a chart']),
]

def card(f, label, title, text, secs=None):
    inner = '<b>%s</b><strong>%s</strong><span>%s</span>' % (label, title, text)
    if secs:
        inner += '<ul>%s</ul>' % ''.join('<li>%s</li>' % s for s in secs)
    if built(f):
        return '<a class="part" href="%s">%s</a>' % (f, inner)
    return '<div class="part soon">%s<span class="tag">Not yet posted</span></div>' % inner


grid = '<div class="grid">'
for f, p, t, q, secs in PARTS:
    grid += card(f, p.upper(), t, q, secs)
grid += card('closing.html', 'CLOSING', 'One move, four times',
             'Conditioning, and the questions to ask of any dataset before applying a technique.')
grid += card('appendix.html', 'APPENDIX', 'Many trials',
             'The die-throw table and a simulation. Discussed in class. Not on the midterm.')
grid += card('practice.html', 'PRACTICE SET', 'A full practice paper',
             'One dataset you have not seen, with questions in the same forms the midterm uses.')
grid += '</div>'

body = f"""
<div class="date">The midterm is on Thursday 24 September, in class.</div>
<p class="note">This is a first version of the guide. Parts are being posted one at a time, and small edits may follow before the exam. The scope described on this page will not change.</p>

<section id="how">
<h2><span class="n">Read this first</span>How to use this guide</h2>
<p>This guide brings together everything the midterm can ask about. It covers the material in Reading Notes 1, 2 and 3, the class sessions, and Homeworks 1, 2 and 3. It is organised around five ideas rather than around the order in which things were taught, because the midterm asks you to recognise an idea in a situation you have not seen before, and that is easier when the ideas are few and clearly separated.</p>
<p>Every section is built the same way. It states one idea. It names the example from class or from a reading note that showed the idea, with the actual numbers from the FuturePath Foundation file. It ends with the question you should be able to ask of any dataset. Then it gives you practice.</p>
<p>The reading notes stay posted and hold the fuller treatment of most of this material. The guide is shorter and is meant to be read in full. Where a section is short, the reading note already covers the material in full, and the section gives the reference.</p>
<p>There are practice questions in every part. The multiple-choice items mark themselves and show the reason for the answer. The open questions have a model answer you can compare against after writing your own. Nothing you type is stored, so print a page or save it as a PDF if you want to keep your answers.</p>
</section>

<section id="covers">
<h2><span class="n">Scope</span>What the midterm covers</h2>
<p>Five ideas. Every question on the paper belongs to one of them. Most questions ask you to apply one of the five questions below to a dataset you are shown.</p>
{table(['Part', 'Idea', 'The question'], [[p, t, q] for f, p, t, q, s in PARTS], txt=True)}
<p>Everything in the five parts is examinable. The closing page is short and shows how the five parts are connected. Read it last.</p>
</section>


<section id="answers">
<h2><span class="n">Standard</span>What a good answer looks like</h2>
<p>The midterm is marked on the same standard as the homework. The question is whether the reason you give supports the conclusion you reach. A correct conclusion with no reason, or with a reason that does not support it, scores below an incorrect conclusion supported by sound reasoning from the information given.</p>
<p>Most questions can be answered in two to four sentences. In a good answer you name the idea that applies, state what it does to the number or the decision in the question, and stop. Definitions on their own do not score. Listing every idea from the course in the hope that one applies does not score either.</p>
<p>If a question asks you to choose between two numbers, two levels or two columns, it is usually asking you to choose for a named decision-maker. Say who is deciding and what they are deciding, and the choice usually becomes clear.</p>
</section>

<section id="contents">
<h2><span class="n">Contents</span>The five parts</h2>
{grid}
</section>
"""

PAGE = {
    'file': 'index.html', 'nav': 'index',
    'title': 'Midterm Study Guide', 'sub': 'Start here',
    'dek': 'Analytics for Management Decision Making',
    'toc': [('how', 'How to use this guide'), ('covers', 'What the midterm covers'),
            ('answers', 'What a good answer looks like'),
            ('contents', 'Contents')],
    'body': body,
    'prev': None, 'next': ('part1.html', 'Part 1. The decision and the roles'),
}
