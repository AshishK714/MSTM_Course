<!--
Source: C:\Users\ashishk\Documents_new\Claude_Sessions\Projects\2026-06-18_writing-cleanup\docs\01_ai-tells-cleanup-checklist.md
Written 2026-06-18. Copied here unchanged on 2026-09-18 as the style authority for this guide.

One conflict with CLAUDE.md, resolved in favour of CLAUDE.md: section E below says
enforce US English. CLAUDE.md requires British spelling to match Reading Note 3
(summarise, centre, signalling). This guide uses British spelling. The rest of the
document applies as written.
-->

# ai-tells-cleanup-checklist.md

_Project: Writing / cleanup · added 2026-06-18_

---

# AI-Writing Cleanup Checklist

A reference for stripping machine-writing signatures out of a draft. Two parts: a paste-ready instruction you hand to the model, and a full reference explaining each tell, how to spot it, and how to fix it.

No single item below proves AI authorship; humans do all of these too. The signal is *density*. The fix is almost never "ban the word"; it's "earn the word or cut it."

---

## Part 1 — Paste-ready cleanup instruction

> Clean this draft of AI-writing tells. Do not change my argument, facts, or structure unless a fix requires it. Work through these passes and report what you changed:
>
> 1. **Kill negative parallelism.** Remove "It's not X, it's Y," "not only X but also Y," "isn't just X, it's Y." First check whether the line is needed at all and cut the whole sentence if not; only rewrite as a direct claim when the claim genuinely carries weight.
> 2. **Break the rule of three.** Find triplets (three adjectives, three-item lists, three parallel clauses). Keep the count only where it's load-bearing; otherwise make it two or four, or cut to the one that matters.
> 3. **Cut significance-inflation.** Delete sentences that exist only to tell the reader the topic is important, meaningful, a testament to, a reflection of, or part of a broader movement. End on a concrete point, not a moral.
> 4. **Cut hedging filler.** Remove "It's important to note," "It's worth noting," "It's worth mentioning." If the point matters, just state it.
> 5. **De-puff the tone.** Replace promotional/travel-guide phrasing with plain description. No "titan of," "rich tapestry of," "stands as a testament."
> 6. **Strip the buzzword vocabulary** (see list). Replace each with a plain word or cut it.
> 7. **Fix false balance.** Where I take a position, commit to it. Don't append a "both sides have merit" sentence that softens it to nothing.
> 8. **Vary sentence length.** Flag stretches where every sentence is the same length and rhythm.
> 9. **Punctuation:** thin out em-dashes (use commas/periods where natural), don't open with em-dash-emphasis, reduce bold, kill title-case headers if the rest is sentence case.
> 10. **Specificity check.** Flag any sentence so generic it could appear in an article on a different topic. Those need a real detail or they get cut.
> 11. **Empty-restatement flag.** Flag (don't silently rewrite) any paragraph whose body just rephrases its opening sentence without adding a fact, example, or argumentative step. Since this touches my argument, surface it for me to decide rather than cutting it yourself. If I've pasted the original prompt, also flag answers that echo the prompt's wording instead of advancing it.
>
> Output the cleaned draft, then a short list of what you changed and any line where you think the "tell" was actually doing real work and shouldn't be removed.

---

## Part 2 — Full reference

### A. Structural and rhetorical patterns

| Tell | How to spot it | How to fix it |
|---|---|---|
| **Negative parallelism** ("It's not X, it's Y") | Scan for "not just," "isn't merely," "more than just," "not only... but also." Often one per paragraph. | First ask whether the line is needed at all. The construction usually adds emphasis to a point already made, so the best fix is often to cut the whole sentence. Only if a claim is genuinely needed, state it directly: "It's not a tool, it's a philosophy" becomes "It's a philosophy" (or, more often, nothing). |
| **Rule of three** | Three adjectives stacked ("creative, smart, and funny"); every list landing on exactly three; three parallel clauses. Watch for "and so on" / "even..." tacked onto a triplet to fake a fourth. | Vary the count to fit the content. Use two when two is true, four when four is. Cut padding adjectives to the one that earns its place. |
| **Significance-inflating conclusion** (the "moral lesson") | Final paragraph zooms out to the wider world: "stands as a testament to," "highlights the enduring legacy," "underscores the importance of," "in an increasingly ___ world." | End on the last concrete point or a specific implication, not a sermon. If the importance is real, show it earlier with evidence instead of asserting it at the end. |
| **Importance/puffery inflation** | Mundane subjects described as pivotal, vital, crucial, groundbreaking. Hedging preamble ("while a minor figure...") followed by importance claims anyway. | Delete the importance sentence. Let the facts carry their own weight. |
| **False balance / both-sidesing** | Position stated, then immediately softened: "However, others argue... both perspectives have merit... the debate is ongoing." | Commit. If you're arguing X, anticipate the strongest objection and dismantle it, don't just acknowledge it neutrally. |
| **Formulaic paragraph openers** | Paragraphs starting with "Furthermore," "Moreover," "Additionally," "Overall." | Open with the actual content. Use transitions only when the logical link genuinely needs signposting. |
| **Sentence-rhythm monotony** | Read aloud; if every sentence is the same length and cadence, it's machine-flat. | Deliberately mix a very short sentence against a long one. Fragments are allowed. |
| **Sanded-down genericness** | A sentence that could appear unchanged in an article on a different topic. No names, numbers, or specifics. | Add a concrete detail, example, or figure, or cut the sentence. |
| **Third-person detachment** | Personal or opinion prompt answered in dispassionate third person; "I" appears once or never. | Write in the voice the piece calls for. If it's your view, say "I think," and say why. |

### B. Vocabulary (the buzzword library)

Spot: search the draft for these. One or two is fine; a cluster is the tell. Fix: replace with a plain word or cut.

**Verbs:** delve, leverage, harness, unlock, foster, showcase, underscore, navigate, embark, elevate, streamline, spearhead, revolutionize, utilize (use "use").

**Nouns:** tapestry, realm, landscape, beacon, testament, cornerstone, paradigm, synergy, ecosystem (when not literal).

**Adjectives:** pivotal, crucial, vital, meticulous, intricate, nuanced, robust, seamless, vibrant, transformative, groundbreaking, comprehensive, multifaceted, intriguing, profound.

**The reliable red flags:** *delve* and *tapestry* are the two most-flagged words in circulation. If either survives an edit, it should be load-bearing.

### C. Stock phrases

| Phrase pattern | Fix |
|---|---|
| "In today's fast-paced world," "In the ever-evolving landscape of," "In an increasingly ___ world" | Delete the opener. Start with your first real sentence. |
| "Let's dive in," "Let's dive into," "Buckle up" | Cut. |
| "When it comes to ___" | Replace with a direct subject. "When it comes to pricing, X" becomes "Pricing: X" or just "X." |
| "It's important to note that," "It's worth noting," "Needless to say" | Delete. Keep the point that follows. |
| "Imagine..." as an opener (often with ellipsis) | Use only if the scene is specific and earns it. |
| "I hope this email finds you well" | Open with the actual reason for the message. |
| "Seamlessly integrated," "robust solution," "game-changer" | Replace with what it actually does. |

### D. Punctuation and formatting

| Tell | How to spot | How to fix |
|---|---|---|
| **Em-dash overuse** | Multiple em-dashes per paragraph, used where a comma, colon, or period would do; em-dash-for-emphasis at sentence ends. | Convert most to commas or periods. Keep an em-dash only where it does something the others can't. (Note: you dislike these, so default to cutting.) |
| **Colon habit** | Colons in titles and before list headers everywhere. | Use colons sparingly; rewrite headers as plain phrases. |
| **Missing en-dashes** | Hyphens used for ranges (1990-2000, pages 3-5) where an en-dash belongs. A *negative* tell: real editors use en-dashes. | Use en-dashes (–) for ranges if you're being careful, or don't worry about it for casual writing. |
| **Curly quotes in casual text** | "Smart" quotes appearing where fast human typing would produce straight ones. | Context-dependent; not worth chasing unless other tells stack up. |
| **Bold overuse** | Key terms bolded as if everything is a textbook. | Bold at most one or two genuinely critical terms per section, or none. |
| **List addiction** | Bulleted lists with bold title-case headers and colons, used where prose would flow better. | Convert to prose unless the content is genuinely a list (steps, specs, options). |
| **Title-case headers** | Headers in Title Case while body is sentence case. | Match the style; sentence case reads more human. |
| **Stray emojis** | Emojis in op-ed, academic, or formal writing. | Remove unless the register clearly invites them. |

### E. Content integrity

| Tell | How to spot | How to fix |
|---|---|---|
| **Hallucinated citations/specifics** | Confident references to studies, quotes, or stats with no verifiable source. | Verify or cut every named source, figure, and quote. |
| **Empty restatement** (paragraph adds nothing past its opening) | A paragraph whose body only rephrases its own first sentence without adding a new fact, example, or step in the argument. Reads full but says one thing. (If the original prompt is supplied, this also catches answers that echo the question's wording instead of advancing it.) | Cut the padding so the paragraph earns its length, or add the substance it was meant to deliver. If neither, the paragraph can usually go entirely. |
| **Inconsistent English variant** | Bounces between US and UK spelling (color/colour, organize/organise). | Enforce US English throughout: color, organize, -ize endings, "analyze," "toward" not "towards," "gray" not "grey." |
| **Uniform certainty** | Every claim at the same confidence level, none stronger or weaker. | Calibrate: assert what you're sure of, hedge only what genuinely warrants it. |

---

## Note on using this

The goal isn't sterile prose with every flagged word removed; that just produces a different, equally detectable flatness. The point is that each of these patterns is a place where the model reached for the average move. Replace the average move with the specific, true, slightly unexpected one and the writing stops reading as machine-made because it no longer is.
