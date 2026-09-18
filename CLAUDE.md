# Midterm study guide: instructions for Claude Code

## What this is

A multi-page HTML study guide for the midterm of a graduate analytics course. Students read it on a
static site (Hugging Face Space). The instructor, AV, reviews every page before it is posted.

PLAN.md is the content plan. It lists every section of every part, the example each section uses,
and the source it comes from. Build from it. Do not restructure it without asking.

Pages already built and reviewed: index.html and part4.html. Read pages/part4.py before writing
anything, because it is the reference for voice, section shape and practice-item shape.

## Before starting

Pause and confirm with AV: which part to build next (the plan says Part 2, then 3, 5, 1, then
closing, appendix, practice set), and whether the source files listed below are all in the folder.
Say which Claude Code features you intend to use for this job and why, then wait.

## Folder

    guide.css        shared stylesheet. Tokens copied from Reading Note 3; guide additions at the end.
    guide.js         shared script: contents drawer, progress bar, hashed practice items, model-answer reveals.
    build.py         builds pages. Inlines CSS and JS so every page is self-contained. Runs checks.
    pages/<name>.py  one page each. Defines PAGE = {file, nav, title, sub, dek, toc, body, prev, next}.
    PLAN.md          the content plan. Sections, examples, sources, build order.

Build: `python3 build.py` builds every page in pages/. `python3 build.py part2` builds one.
Output goes to /mnt/user-data/outputs/study-guide/ by default; change OUT in build.py to a local
folder. Rebuild index.html every time a new part is added, because the index only links pages
whose source file exists in pages/.

Helpers in build.py: sec(anchor, number, title, html), ask(text), src(text), table(head, rows, caption, txt),
box(title, paras, kind), lost(text), kc(page, n, question, four options, correct index, why),
resp(prompt, model answer), score().

## Source files needed in the working folder

    FPF_Case_Study_data.csv                         5,000 learners. Every number is computed from this.
    fpf_trainer_demo.csv                            400 learners, four trainers. Simpson's paradox demo.
    Reading_Note_3_Describing_Data.html             source for Part 5.
    Reading Note 1 and Reading Note 2 (html or docx)   source for Parts 1, 2 and 3 wording. Ask AV for them.
    The Class 4 interactive note (html)             source for Part 2 and Part 3. Ask AV for it.
    Class_4_AMDM_Rows_Finished_and_Columns.pptx     slides for Part 2 and Part 3.
    BADM579_Activities_What_a_Column_Measures.pptx  seven activities. Nearly a draft of Part 3.
    Week_4_class_7_8_notes.docx                     instructor notes for Part 3 (proxies), Part 4, Part 5, appendix.

## Rules that are checked by the build

- No em dash anywhere. The build refuses to write a page containing one.
- Practice items pass an option-bias audit: the correct option is the longest in at most 2 of 15,
  the mean word count of correct options is within one word of the incorrect ones, and correct
  positions are spread across A to D. The build prints pass or FAIL.
- A HARD list of words stops the build. A WATCH list prints a warning wherever one appears, and so does
  the "not X but Y" construction. Every warning gets a second look. Both lists are in build.py, and
  AV's style document (STYLE.md, when supplied) is the source for adding to them.

## Rules that are not checked by the build, and matter more

1. Ideas and objects are not actors. Do not write that a number carries, lands, reaches, sits,
   hides, tells, reveals, drives or shapes anything. Say who did what, or say what is the case.
   Examples of the standard, all from Part 4:
     "The people who are not in it leave no trace" became "The file has no record of the people who are not in it."
     "That cost worked as a filter" became "Only some rural people were willing to pay that cost, so the cost decided who enrolled."
     "having produced it carries information" became "having produced it is informative."
     "The measured number moved because the filter moved" became "The number changed because the filter changed."
   A person reaching the end of a programme, or a report saying 38 percent, is ordinary English and is fine.
   Phrases AV has corrected in earlier materials, all of the same kind: "a rate that travels",
   "earns its keep", "arrived at rather than announced". If a phrase would sound odd in a textbook
   written in 1995, do not use it.
2. Simple, descriptive sentences. No flashy phrases, no headlines, no wordplay in titles. A section
   title says what the section is about.
3. Conventional academic register. British spelling, to match Reading Note 3 (summarise, centre, signalling).
   Plain words in plain phrases. Where a short common word will do, use it. Do not reach for an idiom
   when a plain verb is available: say what a summary leaves out, or loses, rather than what it
   "throws away". That phrase is now a hard stop in build.py.
4. No week numbers, class numbers or course codes in student-facing text. Say "in class" or "the
   in-class activity on denominators". Reading Notes and Homeworks are named by number.
5. Every number is computed from the CSV files, never recalled or copied from a slide. Compute first,
   then write. The figures below were verified during planning; verify them again before use.
6. Nothing is said twice across parts. Where two sources cover one idea, use the clearer example and
   name the other in the "Where this was covered" line.
7. Practice uses the examples students already know. The exam will use new ones.
   Stronger form of the same rule, and it applies to the prose as well as the practice: anchor
   every section and every practice item to a named Homework or to something that was discussed
   in class, and say which in the "Where this was covered" line. Prefer a worked example students
   sat through over a cleaner invented one, because the point of the guide is to reach what they
   already remember. Do not invent a hospital, a college or a charity to carry an idea when the
   FPF file, the trainer file, Homework 1, 2 or 3, or an in-class activity carries it. If nothing
   taught covers the idea, that is a reason to ask AV whether it belongs in the guide at all,
   not a reason to invent a setting for it.
8. Each section: one idea, one named example with real numbers, a "Where this was covered" line, and
   the question to ask. 150 to 300 words of prose. Each part ends with about six self-marking items
   and three written prompts with model answers.

## Verified figures (from planning; recompute before use)

FPF file, 5,000 rows, one per participant.
- Mentorship: 4,363 yes, 637 no. Employed among mentored 38.90%, among unmentored 33.75%.
- Same crosstab, column %: of the employed, 88.76% were mentored; of the not employed, 86.33%.
  Grand %: 33.94 / 53.32 / 4.30 / 8.44 (mentored employed, mentored not, unmentored employed, unmentored not).
- Employed rate by education, unmentored vs mentored: High School 24.30 vs 33.98 (+9.68; n 251 / 2,072);
  Masters 41.21 vs 46.16 (+4.95; 182 / 1,081); Bachelors 38.73 vs 40.83 (+2.10; 204 / 1,210).
- By gender: Female 32.35 vs 40.78 (+8.43; 272 / 1,952); Male 34.71 vs 37.12 (+2.41; 363 / 2,400);
  Prefer not to say 50.00 vs 90.91 (n 2 / 11; use as the small-group warning).
- All 637 unmentored participants are Urban, prior experience 1-3y, ai_roles Mid. No unmentored rows
  exist in Rural, 4y+, Low or High ai_roles, so those groups have no comparison.
- Track: AI 37.0% (n 738), Hybrid 40.0% (2,091), Traditional 36.9% (2,171).
- Gender counts 2,224 / 2,763 / 13. Mean of the three gender rates 53.72% against a true rate of 38.24%.
- Placement: 38.24% of all 5,000; 28.88% full-time of all; 75.52% full-time of the 1,912 placed.
- Salary among the 1,912 employed: mean 63,140, median 60,128, sd 25,204. Mean across all 5,000 with blanks as zero: 24,145.
- Salary is blank for exactly the 3,088 not employed. Identifiers P0001 to P5000 with no gap.
- Attendance: mean 93.13, median 95.00, sd 5.21; percentiles 10/25/50/75/90 = 83/93/95/96/97;
  range 76 to 100. Two clusters: about 941 between 76 and 90, about 4,047 between 92 and 100.
- digital_lit_score: range 51 to 100, sd 11.88. Both columns are stored as text with a percent sign.
- Rural vs urban among the placed: 215 rural, mean 68,172, median 66,254; 1,697 urban, mean 62,503,
  median 59,653. Rural placement rate 41.51% (n 518), urban 37.86%.
- From the activities deck, not yet recomputed: rural vs urban salary by education (High School 45,347 vs
  40,387; Bachelors 63,724 vs 63,303; Masters 91,667 vs 92,867); share of placed rural with a Masters
  34.9% vs 29.4% urban; correlations with placement of attendance -0.0496, digital literacy 0.0445,
  ratio 0.0315; 84% of the readiness-score variation from digital literacy; partnership strength coded
  1 to 4 averages 2.57 and its placement rates run 40.88, 36.99, 36.21, 38.78; averaging group rates
  by location 39.68, education 39.63, track 37.99, partnership 38.21.

Trainer file, 400 rows, 100 per trainer.
- Overall placed: Okonkwo 68, Haddad 66, Silva 64, Mensah 62.
- Within Bachelors: Okonkwo 75, Haddad 80, Silva 85, Mensah 90. Within High School: 40, 45, 50, 55.
- Bachelors in intake: Okonkwo 80, Haddad 60, Silva 40, Mensah 20. Bachelors place at 80%, High School at 50%.
- Mentorship also varies across trainers (83 to 91% yes). Either say education was the intended third
  column or do not mention mentorship in this file.

Homework 3 (Northgate): Team A 32 contacts, 0 portal, 32 tickets. Team B 72 contacts, 40 portal, 32 tickets.

## Review protocol

AV cannot read every page in full. The review has to do most of the work before he sees a page.

1. Write the page.
2. Run a separate review pass before building. Use a subagent that is given only STYLE.md, the rules
   in this file, and the page's prose (not the plan, not the reasoning behind the page). Its job is
   to list every sentence that breaks a rule, with a rewrite. Apply the rewrites. Run the pass again
   until it returns nothing. A reviewer that did not write the text catches what the writer defends.
3. Build. Fix every HARD stop. Read every WATCH warning and either rewrite or keep it deliberately.
4. Render the page headless. Click one correct and one incorrect practice option and confirm the
   marking. Open one model answer. Check the page at mobile width.
5. Hand AV a short note, not the page: the list of WATCH warnings that were kept and why, and the
   six practice items with their answers. He reads that note, the practice items, and one section of
   his choosing. Practice items get read in full every time, because a wrong item produces appeals.
6. Do not start the next part until AV has replied, because his corrections to one part apply to all
   the later ones. Fold each correction into STYLE.md or the word lists so it is not made twice.

## Publishing

The site is a Hugging Face static Space. Each page is self-contained, so uploading the HTML files
to the root of the Space is enough. index.html must be at the root. If AV prefers, the Space can be
cloned as a git repository and pushed to from the working folder after each build.
