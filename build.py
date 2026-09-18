"""Builds the midterm study guide.

Each page lives in pages/<name>.py and defines PAGE = {
  'file': 'part4.html', 'nav': 'part4', 'title': ..., 'sub': ..., 'dek': ...,
  'toc': [(anchor, label), ...], 'body': html, 'prev': (file, label) or None, 'next': (file, label) or None }

Every page is written self-contained: the stylesheet and script are inlined, so a page works
when copied anywhere on its own, and the whole folder works as a static site.
"""
import importlib, os, re, sys, html as H

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'docs')
CSS = open(os.path.join(ROOT, 'guide.css'), encoding='utf-8').read()
JS = open(os.path.join(ROOT, 'guide.js'), encoding='utf-8').read()

GUIDE_NAV = [
    ('index.html', 'index', 'Start'),
    ('part1.html', 'part1', 'Part 1'),
    ('part2.html', 'part2', 'Part 2'),
    ('part3.html', 'part3', 'Part 3'),
    ('part4.html', 'part4', 'Part 4'),
    ('part5.html', 'part5', 'Part 5'),
    ('closing.html', 'closing', 'Closing'),
    ('appendix.html', 'appendix', 'Appendix'),
    ('practice.html', 'practice', 'Practice set'),
]


def fnv(s: str) -> str:
    h = 0x811c9dc5
    for ch in s:
        h ^= ord(ch)
        h = (h * 0x01000193) & 0xffffffff
    return '%08x' % h


# ---------- content helpers ----------

def sec(anchor, number, title, inner):
    return ('<section id="%s"><h2><span class="n">Section %s</span>%s</h2>\n%s</section>\n'
            % (anchor, number, title, inner))


def ask(text):
    return ('<div class="box principle"><h4>The question to ask</h4><p>%s</p></div>\n' % text)


def src(text):
    return '<p class="src">Where this was covered: %s</p>\n' % text


def box(title, paras, kind=''):
    cls = 'box' + (' ' + kind if kind else '')
    return ('<div class="%s"><h4>%s</h4>%s</div>\n'
            % (cls, title, ''.join('<p>%s</p>' % p for p in paras)))


def lost(text):
    return '<div class="lostbox"><b>What this leaves out</b>%s</div>\n' % text


def table(head, rows, caption=None, txt=False):
    th = ''.join('<th>%s</th>' % h for h in head)
    body = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows)
    cap = '<caption>%s</caption>' % caption if caption else ''
    return '<div class="tw"><table%s><thead><tr>%s</tr></thead><tbody>%s</tbody>%s</table></div>\n' % (
        ' class="txt"' if txt else '', th, body, cap)


KC_LOG = []

# Words that stop the build. Add to this list from AV's style document.
HARD = ['delve', 'leverage', 'robust', 'nuanced', 'landscape', 'journey', 'unpack', 'underscore', 'showcase',
        'testament', 'tapestry', 'navigate', 'crucially', 'importantly', 'notably', 'ultimately', 'at its core',
        'the key insight', 'put simply', 'simply put', 'in other words', "here's the thing", 'it is worth noting',
        "it's worth noting", 'think of it as', 'earns its keep', 'arrived at rather than', 'quietly', 'elegant',
        'powerful', 'game-changer', 'seamless', 'dive into', 'a deep dive', 'in short', 'the takeaway',
        # added from STYLE.md, section B (buzzword library) and section C (stock phrases)
        'harness', 'unlock', 'unlocks', 'foster', 'fosters', 'embark', 'elevate', 'streamline', 'spearhead',
        'revolutionize', 'revolutionise', 'utilize', 'utilise', 'realm', 'beacon', 'cornerstone', 'paradigm',
        'synergy', 'pivotal', 'crucial', 'vital', 'meticulous', 'intricate', 'vibrant', 'transformative',
        'groundbreaking', 'multifaceted', 'intriguing', 'profound',
        "in today's fast-paced world", 'in the ever-evolving', 'in an increasingly', "let's dive in", 'buckle up',
        'when it comes to', 'needless to say', 'i hope this email finds you well', 'seamlessly',
        'stands as a testament', 'highlights the enduring', 'it is important to note', "it's important to note",
        'in conclusion', 'furthermore', 'moreover']

# Words that print a warning. Most are verbs that make an idea or an object into an actor.
WATCH = ['sit', 'sits', 'reached', 'reaches', 'landed', 'lands', 'carries', 'carry', 'lives', 'hides', 'hiding',
         'tells you', 'tells us', 'says', 'speaks', 'reveals', 'unlocks', 'drives', 'shapes', 'captures',
         'delivers', 'surfaces', 'leans on', 'ties together', 'lies in', 'points to', 'throws away', 'threw away',
         'travels', 'earns', 'invites', 'demands', 'rewards', 'punishes', 'betrays', 'whispers', 'matters',
         # added from STYLE.md. Section A: negative parallelism, formulaic openers, significance inflation.
         'not just', 'not only', "isn't just", 'is not just', "isn't merely", 'is not merely',
         'more than just', 'rather than merely', 'additionally', 'overall', 'essentially', 'fundamentally',
         # Section A and B: significance inflation and the softer end of the buzzword list
         'highlights', 'reflects', 'stands as', 'comprehensive', 'ecosystem', 'significant', 'significantly',
         'ever-evolving', 'both sides', 'have merit', 'the debate is ongoing',
         # Section C and E: stock phrases and false balance
         'imagine', 'that said', 'on the other hand', 'however, others']


def kc(page, n, q, opts, correct, why):
    """opts: list of four option strings; correct: index of the right one."""
    qid = '%s-k%d' % (page, n)
    KC_LOG.append((qid, opts, correct))
    letters = 'ABCD'
    o = ''.join('<button class="opt" data-a="%d"><span class="ltr">%s</span><span>%s</span></button>'
                % (i, letters[i], t) for i, t in enumerate(opts))
    return ('<div class="kc" data-id="%s" data-h="%s"><span class="tag">Practice %d</span>'
            '<p class="q">%s</p><div class="opts">%s</div><div class="fb"><b>Why:</b> %s</div></div>\n'
            % (qid, fnv('%s:%d' % (qid, correct)), n, q, o, why))


def resp(prompt, model):
    return ('<div class="resp"><div class="p">%s</div><textarea rows="3" placeholder="Write your answer"></textarea>'
            '<div class="f"><button class="rev" type="button">Compare with a model answer</button></div>'
            '<div class="ans"><span class="k">Model answer</span>%s</div></div>\n' % (prompt, model))


def score():
    return ('<div class="score">Practice questions answered: <b id="scoreN">0</b>. '
            'Correct first time: <b id="scoreC">0</b>.</div>\n')


# ---------- audit ----------

def audit():
    """Correct answer is the longest option in no more than 2 of 15; mean length of correct
    options within one word of mean length of incorrect ones; positions spread across A to D."""
    if not KC_LOG:
        return True
    longest = sum(1 for _, o, c in KC_LOG if len(o[c]) == max(len(x) for x in o))
    limit = max(1, round(2 * len(KC_LOG) / 15))
    wc = lambda s: len(s.split())
    cw = [wc(o[c]) for _, o, c in KC_LOG]
    iw = [wc(x) for _, o, c in KC_LOG for i, x in enumerate(o) if i != c]
    gap = abs(sum(cw) / len(cw) - sum(iw) / len(iw))
    pos = [0, 0, 0, 0]
    for _, o, c in KC_LOG:
        pos[c] += 1
    ties = [qid for qid, o, c in KC_LOG if sorted(len(x) for x in o)[-1] == sorted(len(x) for x in o)[-2] and len(o[c]) == max(len(x) for x in o)]
    print('audit: %d items; correct-is-longest %d (limit %d); mean-length gap %.2f words; positions A-D %s; ties-on-longest %s'
          % (len(KC_LOG), longest, limit, gap, pos, ties))
    ok = longest <= limit and gap <= 1.0 and min(pos) >= 1
    print('audit:', 'pass' if ok else 'FAIL')
    return ok


# ---------- page shell ----------

def built(file):
    return os.path.exists(os.path.join(ROOT, 'pages', file.replace('.html', '.py')))


def gnav(here):
    out = '<div class="gnav">'
    for f, k, lab in GUIDE_NAV:
        if built(f):
            out += '<a href="%s"%s>%s</a>' % (f, ' class="here"' if k == here else '', lab)
        else:
            out += '<span class="soon" title="Not yet posted">%s</span>' % lab
    return out + '</div>\n'


def render(page):
    toc = ''.join('<li><a href="#%s">%s</a></li>\n' % (a, l) for a, l in page['toc'])
    pn = ''
    if page.get('prev') or page.get('next'):
        p = page.get('prev'); n = page.get('next')
        link = lambda t, lab: ('<a href="%s"><span>%s</span>%s</a>' % (t[0], lab, t[1]) if t and built(t[0])
                               else ('<em><span>%s</span>%s (not yet posted)</em>' % (lab, t[1]) if t else ''))
        pn = '<div class="pn"><div>%s</div><div style="text-align:right">%s</div></div>' % (link(p, 'Previous'), link(n, 'Next'))
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H.escape(page['title'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<div class="bar"><div class="bar-in">
 <div class="bar-t">Midterm Study Guide <span>&nbsp;{H.escape(page['sub'])}</span></div>
 <div class="bar-sp"></div>
 <button class="btn" id="printBtn" type="button">Print or save PDF</button>
 <button class="btn" id="tocBtn" type="button" aria-expanded="false">Contents</button>
</div><div class="prog" id="prog"></div></div>
<div class="scrim" id="scrim"></div>
<div class="shell">
<nav class="toc" id="toc" aria-label="Contents"><ol>
{toc}</ol></nav>
<main>
{gnav(page['nav'])}
<h1>{page['title']}</h1>
<p class="dek">{page['dek']}</p>
{page['body']}
{pn}
<div class="end">Nothing you type on this page is stored. Use Print or save PDF to keep your answers.</div>
</main>
</div>
<script>
{JS}
</script>
</body>
</html>
"""
    # house rule: no em dashes anywhere
    if '\u2014' in doc:
        raise SystemExit('em dash found in ' + page['file'])
    # writing rule: ideas and objects are not actors. Warn on the usual verbs so they get a second look.
    text = re.sub(r'<[^>]+>', ' ', page['body'])
    low = text.lower()
    bad = [w for w in HARD if re.search(r'\b' + re.escape(w) + r'\b', low)]
    if bad:
        raise SystemExit('banned words in %s: %s' % (page['file'], ', '.join(bad)))
    for m in re.finditer(r'\bnot (only |just |merely |simply )?[^.,;]{2,60}\bbut\b', low):
        print('  watch: "not ... but" construction ... %s ...' % text[max(0, m.start()-20):m.end()+30].replace('\n', ' '))
    for m in re.finditer(r'[^.!?]{12,}\?(?=\s)', text):
        pass  # questions are allowed in this guide; the ask boxes are questions by design
    for w in WATCH:
        for m in re.finditer(r'\b' + w + r'\b', text):
            print('  watch: "%s" in ... %s ...' % (w, text[max(0, m.start()-45):m.end()+45].replace('\n', ' ')))
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, page['file'])
    open(path, 'w', encoding='utf-8').write(doc)
    print('wrote', path, len(doc), 'bytes')


if __name__ == '__main__':
    sys.path.insert(0, ROOT)
    import build as B  # the module the pages import from, so the audit log is shared
    names = sys.argv[1:] or [f[:-3] for f in sorted(os.listdir(os.path.join(ROOT, 'pages'))) if f.endswith('.py') and not f.startswith('__')]
    for name in names:
        B.KC_LOG.clear()
        mod = importlib.import_module('pages.' + name)
        B.render(mod.PAGE)
        B.audit()
