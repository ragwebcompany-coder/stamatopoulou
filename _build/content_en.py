# -*- coding: utf-8 -*-
"""Το αγγλικό περιεχόμενο του ιστότοπου.

Δεν είναι αυτόματη μετάφραση: το κλινικό κείμενο έχει ύφος και οριοθετήσεις που
χάνονται σε μηχανική απόδοση. Οι σελίδες υπηρεσιών περνούν από την ίδια
`service_page()` του gen_pages — αλλάζει μόνο το λεξιλόγιο, ώστε δομή, JSON-LD
και breadcrumbs να μένουν ένα πράγμα και όχι δύο που αποκλίνουν.

Οι διευθύνσεις είναι κανονικά αγγλικά slugs (βλ. PAGE_SLUGS στο gen_common) και
όχι μεταγραφές των ελληνικών: αυτά διαβάζει η Google για την αγγλική έκδοση.
"""
# Το gen_pages εισάγεται ΟΛΟΚΛΗΡΟ (φέρνει και τα gen_common/gen_layout μαζί με
# τους helpers σελίδας: U, svc_cards, cat_cards, aside, facts, cta_button…).
# Δεν υπάρχει κύκλος: το gen_pages μάς εισάγει μέσα από το build(), δηλαδή αφού
# έχει ήδη φορτωθεί πλήρως.
from gen_pages import *

# Οι τιμές αυτές σκιάζουν όσες ήρθαν με το import *: τα f-strings αυτού του
# αρχείου διαβάζουν πρώτα τα δικά του globals, οπότε «{CITY}» εδώ σημαίνει
# «Ilioupoli» χωρίς να πειραχθεί η ελληνική έκδοση.
CITY = CITY_EN
CITY_ACC = CITY_GEN = CITY_EN
REGION = REGION_EN
STREET = STREET_EN
NAME = NAME_EN
NAME_FULL = NAME_EN + ", MSc"
SPECIALTY = "Clinical Psychologist"
TITLE_LINE = "Clinical Psychologist MSc"
BRAND = "Psychoptia — Christina Stamatopoulou, Clinical Psychologist MSc"

COMMON_FACTS_EN = [
    ("Duration", f"{SESSION} minutes per session"),
    ("Setting", f"At the practice in {CITY}, or online"),
    ("Appointments", "By phone or through the contact form"),
]

SERVICE_PAGES_EN = {

# ------------------------------------------------------------------ children
"ypiresies/psychotherapeia-paidion.html": dict(
 title=f"Child Psychologist {CITY} | Child Psychotherapy",
 desc=(f"Child psychotherapy in {CITY}, Athens: play therapy and creative arts, clinical "
       "assessment and parallel parent counselling."),
 eyebrow="Children",
 marq="CHILDREN",
 h1="Child<br>Psychotherapy",
 lede=("A child will not sit down and explain what is troubling it. It will show you — in play, at "
       "school, in its sleep, in its body. Therapy follows that language."),
 facts=[("For", "Pre-school and school-age children")] + COMMON_FACTS_EN +
       [("Parents", "Parallel parent sessions, at an agreed frequency")],
 body="""
<h2 class="cb-h2" style="margin-top:0">How we work with a child</h2>
<p>Child psychotherapy is not "psychotherapy for adults, but smaller". A child does not yet have the
cognitive maturity to observe and describe its inner world in words — but it is entirely capable of
<strong>expressing that world symbolically</strong>: through play, drawing, the stories it invents
and the roles it takes on.</p>
<p>Sessions draw on <a href="play-therapy-creative-arts.html">play therapy and creative arts</a>,
adapted to the child's age and to what is being asked. Play is not a lure to pass the time; it is
the therapeutic medium itself, the means by which a child can safely approach what troubles it.</p>

<h2 class="cb-h2">When it helps</h2>
<ul>
<li>Intense fears, separation anxiety, difficulty sleeping or nightmares.</li>
<li>Outbursts of anger and aggression — or, conversely, excessive "goodness" and withdrawal.</li>
<li>Difficulty adjusting at school or in relationships with peers.</li>
<li>Reactions to family change: parental separation, a new sibling, moving house, bereavement.</li>
<li>Regressive behaviour — bedwetting, clinginess, stammering — after a stressful event.</li>
<li>Psychosomatic complaints: headaches or stomach aches with no organic cause, especially before school.</li>
<li>Low self-esteem, "I'm no good at anything".</li>
</ul>

<h2 class="cb-h2">The role of parents</h2>
<p>There is no work with a child without work with the parents. A child lives inside a system and
returns to it after every session; if the system does not move, change rarely holds.</p>
<p>For that reason, alongside the child's sessions we schedule regular
<a href="parent-counselling.html">parent meetings</a>. There we discuss the direction of the work,
what is being noticed at home, and which practical changes can support the child. The
<em>content</em> of the play and of the sessions remains the child's own.</p>

<div class="cb-note"><strong>Parents first.</strong> Very often the first meeting is with the parents
alone, without the child. That way we can take the history freely, without the child hearing itself
discussed as a problem, and decide together how the process will be presented to them.</div>
""",
 faq=[("From what age do you see children?",
       "<p>From pre-school age upwards. The younger the child, the more weight the work with parents "
       "carries — at very young ages <a href=\"parent-counselling.html\">parent counselling</a> may "
       "well be the most appropriate setting on its own.</p>"),
      ("What do I tell my child about where we are going?",
       "<p>The truth, in words suited to their age: that they are going to meet someone who helps "
       "children when something upsets them or is hard for them, and that there they will play and "
       "talk. Never as a punishment and never as a surprise. This is exactly what we discuss in the "
       "first meeting.</p>"),
      ("Will you tell me what my child does and says in session?",
       "<p>You will know the direction of the work, what we are working on and how you can help. The "
       "content of the play or of confidential moments is not passed on — if a child knows that "
       "everything is reported, it stops using the space. The exception is anything concerning their "
       "safety, which is always communicated.</p>"),
      ("How long will it take?",
       "<p>It depends on what is being asked. Some adjustment difficulties need a few months; other "
       "issues take longer. At regular intervals we reassess the course together, so that nothing "
       "simply continues by inertia.</p>")]),

# ------------------------------------------------------------------ adolescents
"ypiresies/psychotherapeia-efivon.html": dict(
 title=f"Psychologist for Teenagers {CITY} | Adolescent Psychotherapy",
 desc=(f"Adolescent psychotherapy in {CITY}, Athens: anxiety, mood, identity, relationships and body "
       "image, with a clear confidentiality framework and cooperation with parents."),
 eyebrow="Teenagers",
 marq="ADOLESCENCE",
 h1="Adolescent<br>Psychotherapy",
 lede=("Adolescence is a period of intense reorganisation — of body, identity and relationships. A "
       "teenager needs a space of their own, where they can speak without being judged."),
 facts=[("For", "Teenagers and young adults")] + COMMON_FACTS_EN +
       [("Confidentiality", "Content stays with the teenager; the framework is set from the start")],
 body="""
<h2 class="cb-h2" style="margin-top:0">What adolescent therapy is</h2>
<p>A teenager is in a developmental phase whose central task is <strong>forming an identity</strong>
and gradually becoming autonomous from the family. By its nature this produces tension: the same
young person who demands independence also needs safety.</p>
<p>Therapy provides a third space, outside home and outside school, where a teenager can think out
loud without consequences. Depending on what is being asked, the work draws on
<strong>cognitive–behavioural</strong> tools for managing anxiety, a <strong>systemic</strong> view
for relationships, and often <a href="play-therapy-creative-arts.html">creative techniques</a> when
words get stuck.</p>

<h2 class="cb-h2">When it helps</h2>
<ul>
<li>Anxiety, panic attacks, intense worry about performance or the future.</li>
<li>Low mood, withdrawal from friends and activities, loss of interest.</li>
<li>Intense conflict at home, or the sense that "nobody understands".</li>
<li>Questions of identity, body image and self-esteem.</li>
<li>Difficulties in the relationship with food and with body image.</li>
<li>Bullying, exclusion or difficulties with peers — online as well as offline.</li>
<li>School refusal or a drop in performance that cognitive ability does not explain.</li>
<li>Reactions to family change: parental separation, bereavement, moving house.</li>
</ul>

<h2 class="cb-h2">The confidentiality framework</h2>
<p>Without confidentiality there is no adolescent therapy. A teenager has to know that what they say
will not be reported to their parents — otherwise, quite simply, they will not say it.</p>
<p>The framework is set out clearly and <strong>in front of everyone</strong>, from the first
meeting: parents are told the direction of the work and what they need in order to support their
child, not the content of the conversations. The single exception is serious risk to the safety of
the young person or of others — stated explicitly at the outset, so that it can never come as a
surprise.</p>

<div class="cb-note"><strong>Worth knowing:</strong> the hardest part at the beginning is usually
that the teenager arrives "sent", not because they asked to come. The first piece of work is exactly
that: making therapy their own business rather than one more demand from adults.</div>
""",
 faq=[("My teenager refuses to come. What do I do?",
       "<p>Start by coming yourself. <a href=\"parent-counselling.html\">Parent counselling</a> is "
       "often where the work begins, and it changes the context around the young person even when "
       "they never walk through the door. Forcing attendance rarely produces therapy.</p>"),
      ("Will you tell me what my child says?",
       "<p>No — and that is what makes the work possible. You will be told the direction of the work "
       "and anything that concerns your child's safety. Everything else stays in the room.</p>"),
      ("Do parents take part at all?",
       "<p>Yes, at an agreed frequency and with the young person's knowledge. Adolescent therapy "
       "works best when parents are informed allies rather than an audience or an authority to be "
       "reported to.</p>"),
      ("Is online therapy suitable for teenagers?",
       "<p>Often very much so — many young people find it easier to speak from their own room. What "
       "matters is a quiet space where they will not be overheard.</p>")]),

# ------------------------------------------------------------------ adults
"ypiresies/psychotherapeia-enilikon.html": dict(
 title=f"Adult Psychotherapy {CITY} | Anxiety, Panic, Mood",
 desc=(f"Individual adult psychotherapy in {CITY}, Athens: anxiety, panic attacks, low mood, "
       "burnout, relationships and identity. Clinical assessment and goals set together."),
 eyebrow="Adults",
 marq="ADULTS",
 h1="Adult<br>Psychotherapy",
 lede=("A space and a time of your own, where you can look at what is happening to you without "
       "hurry and without judgement — and work on it in a way that makes sense for your life."),
 facts=[("For", "Adults of any age")] + COMMON_FACTS_EN +
       [("Frequency", "Usually weekly at first; adjusted to the goals")],
 body="""
<h2 class="cb-h2" style="margin-top:0">How we work</h2>
<p>The first meeting is one of <strong>getting acquainted and clinical assessment</strong>: we take a
history, map out what brings you here and discuss therapeutic goals. You do not need to have
formulated your request clearly — formulating it is already part of the work.</p>
<p>From there the work moves on two levels at once. In <strong>understanding</strong>: where the
patterns come from, which relationships and stories sustain them, what they once served. And in
<strong>practice</strong>: concrete tools for regulating anxiety, managing daily life and gradually
trying out new ways of doing things.</p>
<p>The balance between the two depends on what is being asked. A panic attack needs tools
<em>now</em>; a repeating relational pattern first needs to be seen for what it is.</p>

<h2 class="cb-h2">When it helps</h2>
<ul>
<li>Anxiety that will not lift, constant worry, panic attacks.</li>
<li>Obsessive–compulsive symptoms: persistent thoughts and rituals that eat time and energy.</li>
<li>Depressed mood, loss of interest, a sense of emptiness.</li>
<li>Professional burnout and chronic stress.</li>
<li>Difficulties in the relationship with food and with body image.</li>
<li>Psychosomatic symptoms with no organic finding.</li>
<li>When something keeps repeating — in relationships, at work, in how you treat yourself.</li>
<li>In transitions: separation, bereavement, moving, changing jobs, becoming a parent.</li>
<li>When relationships with your family of origin still weigh on your adult life.</li>
<li>When you simply want to understand yourself better — that is reason enough.</li>
</ul>

<div class="cb-note"><strong>The therapeutic relationship is the tool.</strong> A sense of safety and
trust is not the backdrop to the work — it is the work. Inside a relationship that holds, the
nervous system settles and it becomes possible to process experiences that elsewhere stay
untouched.</div>
""",
 faq=[("Do I need a \"serious problem\" to start therapy?",
       "<p>No. Therapy does not presuppose a diagnosis or a crisis. Many people come because they "
       "want to understand themselves better, or because they are going through a period of "
       "change.</p>"),
      ("What if I don't know what to say?",
       "<p>That is completely usual, especially at the beginning. You do not need to arrive prepared; "
       "the conversation takes shape between us, and silences have their place too.</p>"),
      ("Will you give me \"advice\" about what to do?",
       "<p>The work is not to tell you what to do. It is to understand together what is happening and "
       "to widen your options, so that the decision is genuinely yours. Practical tools do exist, "
       "however, and are used wherever they help.</p>"),
      ("I take medication. Can I also have psychotherapy?",
       "<p>Yes, and often the combination is what is indicated. A psychologist does not prescribe or "
       "adjust medication; where needed, cooperation with your treating psychiatrist happens in "
       "parallel and always with your consent.</p>")]),

# ------------------------------------------------------------------ parents
"ypiresies/symvouleftiki-goneon.html": dict(
 title=f"Parent Counselling {CITY} | Boundaries &amp; Communication",
 desc=(f"Parent counselling in {CITY}, Athens: boundaries, communication and the parent–child "
       "relationship, with a systemic view. Alongside a child's therapy or on its own."),
 eyebrow="Parents",
 marq="PARENTS",
 h1="Parent<br>Counselling",
 lede=("When the context around a child changes, so does the difficulty. Very often the most "
       "effective intervention for a child is not carried out on the child."),
 facts=[("For", "Parents of children and teenagers")] + COMMON_FACTS_EN +
       [("Setting", "On its own, or alongside the child's therapy")],
 body="""
<h2 class="cb-h2" style="margin-top:0">What parent counselling is</h2>
<p>Parent counselling is not a class in correct upbringing, nor an assessment of the parents. It is a
space in which we look together at the <strong>parent–child relationship</strong> and at the patterns
that have built up around a difficulty — and test what can move.</p>
<p>The view is <strong>systemic</strong>: a child's behaviour does not appear in a vacuum. It makes
sense inside the family system, it often serves something, and it is sustained by cycles of
interaction in which everyone takes part. The question is not who is at fault, but what keeps the
cycle going and where it can be broken.</p>

<h2 class="cb-h2">When it helps</h2>
<ul>
<li>When boundaries either collapse or turn into war, and daily life has become a negotiation.</li>
<li>In repeating conflicts around screens, homework, sleep, food.</li>
<li>When the two parents operate differently and the child moves between them.</li>
<li>In separation or divorce: how we talk to the child, how parental cooperation is maintained.</li>
<li>When the child refuses to come to therapy — this is often where the work begins.</li>
<li>In sibling conflict and jealousy.</li>
<li>When the parent themselves feels exhausted, guilty or inadequate.</li>
</ul>

<h2 class="cb-h2">How we work</h2>
<p>We start from specific everyday scenes — not from abstract principles. A typical piece of work
looks like this: you describe an episode step by step, we look at what came before and after, we
identify the cycle that repeats, and we try one small, concrete change before the next meeting.</p>
<p>Meetings can be with one parent or with both. Where there is disagreement within the parental
couple, the work often focuses precisely there: a child finds it far harder to follow two different
sets of rules than one strict one.</p>

<div class="cb-note"><strong>You are not the problem.</strong> Parents who ask for help are, by
definition, parents who care. Counselling is not looking for what you did wrong — it is looking for
what can be done from here on.</div>
""",
 faq=[("Do both parents have to come?",
       "<p>It is not essential, but it helps considerably — especially where the two of you take "
       "different lines. The work can perfectly well start with one parent and have the second join "
       "later.</p>"),
      ("Does the child need to come too?",
       "<p>Not necessarily. Very often parent counselling is a sufficient intervention in itself, "
       "particularly at younger ages. If the assessment shows that individual work with the child is "
       "also needed, we will discuss it.</p>"),
      ("We are separated and cannot agree. Is there any point?",
       "<p>There is, a great deal. Parental cooperation is a different matter from the couple "
       "relationship and can work even when the latter has ended. The work focuses exclusively on "
       "the child, not on the history of the separation.</p>"),
      ("Will you tell us what to do?",
       "<p>I will suggest specific practices and explain the reasoning behind them. But putting them "
       "into practice goes through you and your own style: a technique that does not suit you is one "
       "you will not use, and rightly so.</p>")]),

# ------------------------------------------------------------------ play therapy
"ypiresies/paigniotherapeia-dimiourgikes-technes.html": dict(
 title=f"Play Therapy {CITY} | Creative Arts",
 desc=(f"Play therapy and creative arts in {CITY}, Athens: symbolic play, drawing, storytelling and "
       "dramatisation as therapeutic tools for children and teenagers."),
 eyebrow="Play Therapy",
 marq="PLAY",
 h1="Play Therapy &amp;<br>Creative Arts",
 lede=("Play is a child's language and toys are its words. In play therapy, play is not a break from "
       "the work — it is the work."),
 facts=[("For", "Children and teenagers; selectively, adults too")] + COMMON_FACTS_EN +
       [("Training", "Play Therapy &amp; Creative Arts, Metropolitan College")],
 body="""
<h2 class="cb-h2" style="margin-top:0">Why play</h2>
<p>A frightened child will not say "I have felt insecure since we moved house". But it will build a
house out of blocks and knock it down, again and again. Symbolic play is how the human psyche
processes before it finds words — and it remains available long after childhood.</p>
<p>The <strong>distance of the symbol</strong> is the key. It is far safer to talk about the bear who
is afraid of the dark than about yourself; and through the bear, in the end, the same fear gets
worked through. The child always controls how close it comes.</p>

<h2 class="cb-h2">What it involves</h2>
<ul>
<li><strong>Symbolic and directed play</strong> — with figures, dolls, construction, board games that
work on taking turns, losing and cooperating.</li>
<li><strong>Art materials</strong> — drawing, clay, collage. The hand often arrives before speech.</li>
<li><strong>Storytelling and story-making</strong> — therapeutic tales, stories the child continues
or whose ending it changes.</li>
<li><strong>Dramatisation and roles</strong> — trying out different positions within a scene: what
would happen if I answered differently.</li>
<li><strong>Expression and regulation techniques</strong> — recognising feelings, settling the body,
putting tension onto paper instead of into an outburst.</li>
</ul>

<h2 class="cb-h2">When it helps most</h2>
<ul>
<li>When a child will not talk about what happened — or insists that "nothing is wrong".</li>
<li>After a traumatic or stressful event: an accident, a loss, a separation, a hospital stay.</li>
<li>In difficulties regulating anger, where talking alone is not enough.</li>
<li>With children who have speech or communication difficulties.</li>
<li>With teenagers and adults who "know everything" about their problem and yet nothing changes.</li>
</ul>

<div class="cb-note"><strong>No talent required.</strong> Nothing made in a session is assessed —
neither aesthetically, nor interpreted "behind the child's back". What is produced is a starting
point, not evidence.</div>
""",
 faq=[("My child doesn't draw and gets bored with toys. Will this work?",
       "<p>The materials adapt. There is no one \"right\" medium: some children connect through "
       "construction, others through stories, others through board games, others through movement. "
       "The first sessions are spent finding exactly that.</p>"),
      ("Is it the same as creative activities or arts clubs?",
       "<p>No. Creative activities aim at skill and enjoyment. Play therapy has a therapeutic aim, is "
       "carried out by a trained mental health professional, within a stable framework and with a "
       "specific direction that follows from clinical assessment.</p>"),
      ("Is it used with adults as well?",
       "<p>Yes, selectively. Creative and expressive techniques are often useful with adults who "
       "understand their difficulty intellectually but find that nothing shifts — the symbol reaches "
       "where explanation has stopped working.</p>"),
      ("How is progress measured if it is \"just playing\"?",
       "<p>Through what changes outside the room: sleep, school, relationships, the frequency of "
       "outbursts. The play itself also changes — themes that were repeated compulsively begin to "
       "resolve, and that is visible.</p>")]),

# ------------------------------------------------------------------ energy therapies
"ypiresies/energeiakes-therapeies.html": dict(
 title="Energy Therapies | Theta Healing &amp; Therapeutic Dowsing",
 desc=("Energy therapies: Theta Healing and therapeutic dowsing as complementary relaxation "
       "methods, in a setting entirely separate from psychotherapy."),
 eyebrow="Complementary",
 marq="ENERGY",
 h1="Energy<br>Therapies",
 lede=("Complementary methods of relaxation and energy work. They are offered in a setting entirely "
       "separate from psychotherapy — and this page explains why."),
 facts=[("For", "Adults, after discussion")] +
       [("Duration", f"{SESSION} minutes per session"),
        ("Setting", "Separate sessions, not within psychotherapy"),
        ("Not offered", "To minors, or in active clinical cases"),
        ("Appointments", "By phone or through the contact form")],
 body="""
<div class="cb-note cb-note--scope" style="margin-top:0"><strong>Before anything else.</strong>
<strong>Theta Healing</strong> and <strong>therapeutic dowsing</strong> are complementary practices.
They are <em>not</em> psychotherapy, they do <em>not</em> have scientific evidence comparable to that
of recognised psychotherapeutic approaches, and they do <em>not</em> replace psychological,
psychiatric or medical care. They promise no cure, no diagnosis and no treatment of any
condition.</div>

<h2 class="cb-h2" style="margin-top:2.5rem">The two methods</h2>
<p>Two distinct practices are presented here under the heading "energy therapies". They are not a
single unified method and they do not work in the same way:</p>
<ul>
<li><strong>Theta Healing.</strong> A guided process of deep relaxation, focusing on beliefs and
patterns that the person themselves recognises as limiting.</li>
<li><strong>Therapeutic dowsing.</strong> Work with a pendulum and charts, as a tool for focus and
reflection within a relaxation session.</li>
</ul>

<h2 class="cb-h2">Why this page exists</h2>
<p>It would be easier not to mention them at all. I choose to mention them, with clear boundaries,
for two reasons: because they are genuinely offered, and because someone looking for them deserves
to find accurate information about what they are and what they are not — rather than promises.</p>

<h2 class="cb-h2">What a session is like</h2>
<p>A quiet, structured hour. There is no diagnosis, no interpretation of your history and no advice
about medical decisions. Most people describe it as a period of deep rest in which something they
were carrying becomes easier to name.</p>

<h2 class="cb-h2">When they are not offered</h2>
<ul>
<li>To minors, under any circumstances.</li>
<li>In place of psychotherapy, psychiatric or medical treatment.</li>
<li>During an acute crisis, or where there is risk to safety.</li>
<li>Where someone is looking for a cure for a physical or mental illness.</li>
</ul>

<div class="cb-note"><strong>Kept separate on purpose.</strong> These sessions never take place
inside psychotherapy. Mixing the two would blur what rests on clinical evidence and what does not —
and that distinction is yours to have, not mine to smooth over.</div>
""",
 faq=[("Is this psychotherapy?",
       "<p>No. It is a complementary relaxation practice. Psychotherapy is a separate service, with "
       "separate sessions, based on recognised therapeutic approaches and clinical assessment.</p>"),
      ("Can it replace treatment I am already having?",
       "<p>No, and it should not. Never stop psychiatric or medical treatment on the basis of a "
       "complementary practice. If you are considering a change, discuss it with your treating "
       "clinician.</p>"),
      ("Do you offer this to children?",
       "<p>No. These methods are not offered to minors under any circumstances.</p>"),
      ("How do I know whether it is for me?",
       "<p>We discuss it first. If what you are looking for is treatment for a difficulty, the "
       "appropriate route is <a href=\"adult-psychotherapy.html\">psychotherapy</a> — and I will say "
       "so plainly rather than book you a session.</p>")]),
}


# ==================================================================== FAQ
HOME_FAQ_EN = [
 ("How do I book a first session?",
  f'<p>One phone call to <a href="tel:+30{PHONE}">{PHONE_P}</a>: a short conversation is enough to '
  f'see what is on your mind, which setting fits and when we could start. If you prefer to write, '
  f'use the <a href="contact.html#rantevou">contact form</a> or email '
  f'<a href="mailto:{EMAIL}">{EMAIL}</a> and I will get back to you.</p>'),
 ("How long is a session and how often do we meet?",
  f"<p>Each session lasts {SESSION} minutes. Frequency is usually weekly at the start and is "
  "adjusted as the work progresses and the goals change.</p>"),
 ("Do you work in English?",
  "<p>Yes. Sessions are held in Greek and in English, in person or online. If English is the "
  "language you think and feel in, that is the language we work in.</p>"),
 ("Can sessions be held online?",
  f"<p>Yes, with the same duration and the same way of working. Online sessions are held across "
  f"Greece and abroad — you need a quiet space and a stable connection. In person, the practice is "
  f"in {CITY} and serves all of Attica.</p>"),
 ("Is everything I say confidential?",
  "<p>Yes. Confidentiality is protected by professional and legal obligation. The exceptions are "
  "narrow and stated from the outset: serious risk to your safety or that of another person, and "
  "cases where the law requires disclosure.</p>"),
 ("Do I need a diagnosis or a referral?",
  "<p>Neither. You can come simply because something is difficult, or because you want to "
  "understand yourself better. The first meeting includes a clinical assessment, and from that we "
  "decide together what is appropriate.</p>"),
]

FAQ_EXTRA_EN = [
 ("What is the difference between a psychologist and a psychiatrist?",
  "<p>A psychiatrist is a medical doctor and can prescribe medication. A psychologist works through "
  "psychotherapy and does not prescribe. The two often work in parallel, and where that is "
  "indicated I will say so and — with your consent — cooperate with your treating psychiatrist.</p>"),
 ("How much does a session cost?",
  "<p>Fees are discussed openly on the first phone call, before anything is booked, so that there "
  "are no surprises. Please call for current fees.</p>"),
 ("What if I need to cancel?",
  "<p>Let me know as early as you can. A session cancelled at short notice is time that cannot be "
  "offered to anyone else, and the cancellation policy is explained clearly when we agree the "
  "framework.</p>"),
 ("How will I know whether therapy is working?",
  "<p>By what changes outside the room: sleep, relationships, how you handle what used to floor "
  "you. We also review the course together at regular intervals, including the question of when "
  "therapy should end.</p>"),
 ("Can I bring my partner or a family member?",
  "<p>Depending on what is being asked, yes. Some work is individual by nature; other requests are "
  "better served by working with the couple or with parents. We decide this in the assessment.</p>"),
 ("What if I don't get on with you?",
  "<p>Then say so, and I will help you find someone else. Fit between therapist and client is a "
  "real clinical variable, not a matter of politeness — and it matters more than any technique.</p>"),
]

ALL_FAQ_EN = HOME_FAQ_EN + FAQ_EXTRA_EN


# ==================================================================== ΑΡΧΙΚΗ
def home_en():
    d = 1
    hero = f"""<section class="cb-hero" id="top">
<div class="cb-hero__bg" data-anim="hero-img" aria-hidden="true">
<img class="cb-hero__photo" src="../assets/img/hero-grafeio.jpg" width="1440" height="1080"
 fetchpriority="high" decoding="async" alt="">
<div class="cb-hero__scrim"></div>
<div class="cb-hero-glow"></div><div class="cb-hero-grid"></div>
</div>
<div class="container mx-auto px-6 md:px-12 relative z-10" data-anim="hero-content">
<div class="cb-hero__in">
<span class="cb-eyebrow cb-eyebrow--light" data-anim="hero-in" data-delay=".4">Clinical Psychologist MSc · {CITY}, Athens</span>
<h1 class="cb-hero__h1" data-anim="hero-in" data-delay=".55">Where light meets understanding,<br class="cb-hero__br"> connection is born</h1>
<p class="cb-hero__lede" data-anim="hero-in" data-delay=".7">Psychotherapy for children, teenagers
and adults, parent counselling and play therapy. The therapeutic process starts from a clinical
assessment and takes shape around what you bring — not around a ready-made protocol.
Sessions in Greek and in English.</p>
<div class="cb-hero__actions" data-anim="hero-in" data-delay=".85">
<a class="cb-btn cb-btn--light" href="tel:+30{PHONE}">{icon('phone','w-4 h-4')}<span>{PHONE_P}</span></a>
<a class="cb-btn cb-btn--outline" href="#services">THE SERVICES<span class="cb-btn__arrow">&#8594;</span></a>
</div>
</div>
</div>
<div class="cb-hero__cue" data-anim="cue" aria-hidden="true"><span>SCROLL</span><div data-anim="bounce">{icon('chev','w-5 h-5','2')}</div></div>
</section>"""

    trust = f"""<section class="cb-section cb-section--tight">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-cards cb-cards--3">
<div class="cb-card" data-reveal><span class="cb-card__ic">{icon('brain','w-7 h-7')}</span>
<span class="cb-card__t">Clinical assessment from the start</span>
<span class="cb-card__d">The first meeting includes history-taking and clinical assessment, so that the setting is chosen on evidence rather than by chance.</span></div>
<div class="cb-card" data-reveal><span class="cb-card__ic">{icon('flower','w-7 h-7')}</span>
<span class="cb-card__t">Three age groups</span>
<span class="cb-card__d">Children, teenagers and adults — with different tools for each, from play to language.</span></div>
<div class="cb-card" data-reveal><span class="cb-card__ic">{icon('palette','w-7 h-7')}</span>
<span class="cb-card__t">Play therapy &amp; the arts</span>
<span class="cb-card__d">Specialist training in play therapy and the creative arts — for where words alone do not reach.</span></div>
<div class="cb-card" data-reveal><span class="cb-card__ic">{icon('hands','w-7 h-7')}</span>
<span class="cb-card__t">Parents inside the process</span>
<span class="cb-card__d">In work with children and teenagers, parents are not spectators: there are parallel meetings within an agreed framework.</span></div>
<div class="cb-card" data-reveal><span class="cb-card__ic">{icon('monitor','w-7 h-7')}</span>
<span class="cb-card__t">In person or online</span>
<span class="cb-card__d">At the practice in {CITY} or online, with the same way of working and the same duration — in Greek or in English.</span></div>
<div class="cb-card" data-reveal><span class="cb-card__ic">{icon('shield','w-7 h-7')}</span>
<span class="cb-card__t">Framework and confidentiality</span>
<span class="cb-card__d">Licensed to practise, member of the Association of Greek Psychologists, in regular clinical supervision.</span></div>
</div>
</div>
</section>"""

    approach = f"""<section class="cb-section cb-section--lilac cb-section--marq" id="approach">
{marquee("PSYCHOPTIA", "1", "12%")}
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2">
<figure class="cb-figure" data-reveal>
<img src="../assets/img/grafeio-synedria.jpg" width="1000" height="1333" loading="lazy" decoding="async"
 alt="Christina Stamatopoulou in the consulting room in {CITY}, with the Psychoptia artwork behind her">
<figcaption>The consulting room in {CITY} — quiet, warm and unhurried.</figcaption>
</figure>
<div data-reveal>
<span class="cb-eyebrow">The approach</span>
<h2 class="cb-h2">The right tool for each person</h2>
<div class="cb-prose">
<p>There is no single method that suits everyone. That is why my work rests on
<strong>three distinct trainings</strong> that speak to one another: the cognitive–behavioural
approach, systemic and family therapy, and play therapy with the creative arts.</p>
<p>Which of them is used — and in what proportion — is not decided in advance. It follows from the
<strong>clinical assessment</strong> in the first meeting: from age, from what is being asked, from
the context of a life and from the way each person finds it easiest to express themselves.</p>
<p>A seven-year-old will not talk about their anxiety; they will play it. An adult with panic attacks
needs both understanding and concrete tools for tomorrow morning. A teenager first needs to trust
that the space is genuinely their own.</p>
</div>
<p style="margin-top:2rem"><a class="cb-btn cb-btn--ghost" href="about.html">STUDIES &amp; TRAINING<span class="cb-btn__arrow">&#8594;</span></a></p>
</div>
</div>
</div>
</section>"""

    services = f"""<section class="cb-section cb-section--marq" id="services">
{marquee("PSYCHOTHERAPY", "-1", "58%")}
<div class="container mx-auto px-6 md:px-12">
<div style="max-width:56rem;margin-bottom:3rem" data-reveal>
<span class="cb-eyebrow">The services</span>
<h2 class="cb-h2">Three directions</h2>
<p class="cb-lede">Psychotherapy and counselling for every age, play therapy with the creative arts,
and — in an entirely separate setting — energy therapies. In every case, the work starts from what
you bring.</p>
</div>
{cat_cards(d)}
<p style="margin-top:2rem"><a class="cb-btn cb-btn--ghost" href="services.html">SEE ALL SERVICES<span class="cb-btn__arrow">&#8594;</span></a></p>
</div>
</section>"""

    who = f"""<section class="cb-section cb-section--dark cb-section--marq" id="about">
{marquee("STAMATOPOULOU", "1", "22%", dark=True)}
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2">
<div data-reveal>
<span class="cb-eyebrow cb-eyebrow--light">Who I am</span>
<h2 class="cb-h2">{NAME_FULL}</h2>
<div class="cb-prose" style="color:rgba(248,247,252,.72)">
<p style="color:rgba(248,247,252,.72)">A Clinical Psychologist with an undergraduate degree in
Applied Psychology (University of Derby) and a master's in Clinical and Community Psychology
(University of East London). Trained in Counselling, in Play Therapy and the Creative Arts, and in
Systemic and Family Therapy.</p>
<p style="color:rgba(248,247,252,.72)">I have been in private practice since 2020. I have worked in
private mental health counselling centres and completed placements in interdisciplinary settings,
observing real cases alongside experienced clinicians.</p>
</div>
<p style="margin-top:2rem"><a class="cb-btn cb-btn--outline" href="about.html">FULL PROFILE<span class="cb-btn__arrow">&#8594;</span></a></p>
</div>
<div data-reveal>
<figure class="cb-portrait">
<img src="../assets/img/christina-stamatopoulou.jpg" width="1000" height="1502" loading="lazy" decoding="async"
 alt="Portrait of Christina Stamatopoulou, Clinical Psychologist MSc">
</figure>
</div>
</div>
<div class="cb-stats" style="margin-top:3.5rem" data-reveal>
<div class="cb-stat"><b>{SESSION}′</b><span>minutes per session</span></div>
<div class="cb-stat"><b>MSc</b><span>Clinical &amp; Community Psychology</span></div>
<div class="cb-stat"><b>3</b><span>therapeutic trainings</span></div>
<div class="cb-stat"><b>2020</b><span>in private practice since</span></div>
</div>
<div style="margin-top:2.5rem;max-width:34rem" data-reveal>{online_note()}</div>
</div>
</section>"""

    faq = f"""<section class="cb-section cb-section--lilac" id="faq">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div data-reveal>
<span class="cb-eyebrow">Frequently asked</span>
<h2 class="cb-h2">Before the first meeting</h2>
{faq_block(HOME_FAQ_EN)}
<p style="margin-top:2rem"><a class="cb-btn cb-btn--ghost" href="faq.html">ALL QUESTIONS<span class="cb-btn__arrow">&#8594;</span></a></p>
</div>
{aside(d)}
</div>
</div>
</section>"""

    booking = f"""<section class="cb-section" id="rantevou">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2">
<div data-reveal>
<span class="cb-eyebrow">Appointments</span>
<h2 class="cb-h2">Let's take the first step</h2>
<p class="cb-lede">One phone call is enough. We will talk briefly about what is on your mind and
arrange a first introductory meeting — at the practice in {CITY} or online.</p>
<div style="margin-top:2rem">{online_note()}</div>
<div style="margin-top:2rem">{contact_card(d)}</div>
</div>
<div data-reveal>{contact_form(d)}</div>
</div>
</div>
</section>"""

    slug = "en/index.html"
    ld = [practice_ld(), person_ld(), website_ld(),
          {"@type": "WebPage", "@id": U(slug) + "#page", "url": U(slug),
           "name": BRAND, "isPartOf": {"@id": SITE_URL + "/#website"},
           "about": {"@id": SITE_URL + "/#grafeio"}, "inLanguage": "en-GB"},
          faq_ld(HOME_FAQ_EN)]
    return render(
        depth=d,
        title=f"Psychologist in {CITY}, Athens | {NAME}, MSc",
        description=(f"English-speaking clinical psychologist in {CITY}, Athens. Psychotherapy for "
                     f"children, teenagers and adults, parent counselling, play therapy. In person "
                     f"or online. Tel. {PHONE_P}."),
        canonical=U(slug), ld_graph=ld, active="index.html",
        content=hero + trust + approach + services + who + faq + booking)


# ==================================================================== ΒΙΟΓΡΑΦΙΚΟ
STUDIES_EN = [
 ("MSc Clinical &amp; Community Psychology",
  "University of East London, United Kingdom."),
 ("BSc Applied Psychology",
  "University of Derby, United Kingdom."),
 ("Licence to practise as a Psychologist",
  f"Licence number {LICENSE}, for the Greek territory."),
 ("Member", "Association of Greek Psychologists (S.E.PS.)."),
]

TRAINING_EN = [
 ("2023 – 2024", "MSc Clinical &amp; Community Psychology", "University of East London"),
 ("2022 – 2023", "Training in Counselling Skills", "\"Empsychosis\" Centre"),
 ("—", "Play Therapy &amp; Creative Arts", "Metropolitan College"),
 ("—", "Systemic &amp; Family Therapy", "Ke.Se.Me.Th., Athens"),
 ("2017 – 2020", "BSc Applied Psychology", "University of Derby"),
]

EXPERIENCE_EN = [
 ("2020 — present", "Clinical Psychologist · Private practice, Psychoptia",
  "Individual psychotherapy sessions with children, teenagers and adults, parent counselling and "
  "play therapy, at the practice in Ilioupoli or online. Every collaboration starts with "
  "history-taking and clinical assessment, so that the therapeutic framework and its goals are set "
  "jointly and on clear grounds."),
 ("2020 — 2022", "Mental Health Counsellor · Private counselling centres",
  "Counselling and supportive work with adults and teenagers in a mental health centre setting, "
  "with regular supervision and cooperation with other specialties."),
 ("Placement", "Hellenic Institute of RECBT",
  "Observation of real cases in an interdisciplinary setting and familiarisation with "
  "cognitive–behavioural methodology. Within this placement I wrote the psychoeducational material "
  "\"The self care of the caregivers\"."),
 ("Placement", "\"Charis Kataki\" Laboratory for the Exploration of Human Relations",
  "Familiarisation with the systemic view of human relationships and family dynamics."),
]


def about_en():
    d, slug = 1, "en/about.html"
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")), (T("nav.bio"), None)])
    hero = page_hero("Who I am", f"{NAME},<br>MSc",
                     "Clinical Psychologist. Studies in the United Kingdom, three therapeutic "
                     f"trainings, and a practice in {CITY} since 2020.", crumbs, marq_word="PROFILE")
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div>
<figure class="cb-figure" data-reveal style="margin-bottom:2.5rem">
<img src="../assets/img/christina-stamatopoulou.jpg" width="1000" height="1502" loading="lazy"
 decoding="async" alt="Portrait of Christina Stamatopoulou, Clinical Psychologist MSc">
</figure>
<div class="cb-prose" data-reveal>
<h2 class="cb-h2" style="margin-top:0">How I work</h2>
<p>I am a Clinical Psychologist and I have been working in private practice since 2020, with
children, teenagers, adults and parents. What I have kept from every training I have done is the
same thing: that the method serves the person, never the other way round.</p>
<p>My work rests on three trainings that speak to one another — the cognitive–behavioural approach,
systemic and family therapy, and play therapy with the creative arts. Which of them is used, and in
what proportion, follows from the <strong>clinical assessment</strong> of the first meeting rather
than from a preference of mine.</p>
<p>My continuing education in systemic and family therapy is ongoing. I mention it because it shapes
how I think about families — not as a completed qualification.</p>
<p>Sessions are held in Greek and in English, in person in {CITY} or online.</p>

<h2 class="cb-h2">Studies and credentials</h2>
</div>
{simple_list([(a, b, "") for a, b in STUDIES_EN])}
<h2 class="cb-h2" data-reveal>Training</h2>
{timeline(TRAINING_EN)}
<h2 class="cb-h2" data-reveal>Experience</h2>
{timeline(EXPERIENCE_EN)}
<div data-reveal style="margin-top:2.5rem">{online_note()}</div>
</div>
{aside(d, extra=cta_button(d))}
</div>
</div>
</section>"""
    ld = [practice_ld(), person_ld(),
          {"@type": "AboutPage", "@id": U(slug) + "#page", "url": U(slug),
           "name": f"{NAME} — Clinical Psychologist MSc", "inLanguage": "en-GB",
           "mainEntity": {"@id": SITE_URL + "/viografiko.html#psychologos"}},
          breadcrumb_ld([(T("nav.home"), U("en/index.html")), ("About", U(slug))])]
    return render(depth=d, title=f"{NAME}, MSc | Clinical Psychologist {CITY}, Athens",
                  description=("Clinical Psychologist MSc (University of East London). Trained in "
                               "counselling, play therapy and systemic family therapy. In practice "
                               f"in {CITY}, Athens since 2020."),
                  canonical=U(slug), ld_graph=ld, active="viografiko.html", content=hero + body)


# ==================================================================== ΥΠΗΡΕΣΙΕΣ
def services_en():
    d, slug = 1, "en/services.html"
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")), (T("nav.services"), None)])
    hero = page_hero("Services", "Psychotherapy &amp;<br>counselling",
                     "Psychotherapy for children, teenagers and adults, parent counselling and play "
                     f"therapy — at the practice in {CITY} or online, in Greek or in English.",
                     crumbs, marq_word="SESSIONS")
    body = f"""<section class="cb-section cb-section--marq">
{marquee("SESSIONS", "1", "8%")}
<div class="container mx-auto px-6 md:px-12">
<div style="max-width:62rem;margin-bottom:3rem" data-reveal>
<div class="cb-prose">
<p>Every request arrives in its own way. An adult comes because something keeps repeating. A parent
comes for their child and discovers that the work starts with themselves. A teenager arrives "sent"
and stays because they found a space of their own.</p>
<p>The framework of the work is not fixed in advance. It follows from the
<strong>clinical assessment</strong> of the first meeting, on the basis of what best serves what is
being asked — and it can change along the way if the circumstances do.</p>
</div>
</div>
{cat_cards(d)}
</div>
</section>

<section class="cb-section cb-section--lilac">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div data-reveal>
<span class="cb-eyebrow">Step by step</span>
<h2 class="cb-h2">What to expect</h2>
<div class="cb-prose">
<ol>
<li><strong>First contact.</strong> A phone call or a message. A short conversation is enough to see
whether and how we can work together, and to arrange the first meeting.</li>
<li><strong>First meeting: history and clinical assessment.</strong> I listen to what brings you
here, take a history and make an initial clinical evaluation. You do not need to have "sorted" the
problem — that is part of the work.</li>
<li><strong>Setting the therapeutic framework.</strong> We agree goals, frequency and setting
(individual, parental, play-based) together. The framework is an agreement, not an imposition.</li>
<li><strong>The therapeutic process.</strong> Sessions of {SESSION} minutes, combining understanding
of the patterns, emotional processing and practical tools for everyday life.</li>
<li><strong>Review.</strong> At regular intervals we look together at what has changed and what is
still needed — including when therapy should come to an end.</li>
</ol>
</div>
{online_note()}
<div style="margin-top:2rem">{crisis_note()}</div>
</div>
{aside(d)}
</div>
</div>
</section>"""
    ld = [practice_ld(), person_ld(),
          {"@type": "CollectionPage", "@id": U(slug) + "#page", "url": U(slug),
           "name": "Psychotherapy and counselling services", "inLanguage": "en-GB",
           "hasPart": [{"@type": "Service", "name": plain(L(x, "short")), "url": U(S(x))}
                       for x in SERVICES]},
          breadcrumb_ld([(T("nav.home"), U("en/index.html")), ("Services", U(slug))])]
    return render(depth=d, title=f"Psychotherapy Services {CITY}, Athens | Children, Teens, Adults",
                  description=("Psychotherapy for children, teenagers and adults, parent counselling, "
                               f"play therapy and creative arts in {CITY}, Athens or online."),
                  canonical=U(slug), ld_graph=ld, active="", content=hero + body)


def category_en(cat):
    d, slug = 2, cat["slug_en"]
    name = plain(L(cat, "nav"))
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")), (name, None)])
    hero = page_hero("Services", "Psychotherapy &amp;<br>Counselling",
                     "One therapeutic process, four settings. Which one fits follows from the "
                     "clinical assessment of the first meeting — not from a ready-made protocol.",
                     crumbs, marq_word="SESSIONS")
    kids = cat_children(cat)
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div>
<div class="cb-prose" data-reveal>
<h2 class="cb-h2" style="margin-top:0">What they all have in common</h2>
<p>Whether it is a child, a teenager, an adult or a parent, the work starts from the same place: a
<strong>clinical assessment</strong> in the first meeting, where we take a history and look together
at what best serves what is being asked.</p>
<p>What changes is the tools. A seven-year-old will not talk about their anxiety; they will play it.
An adult with panic attacks needs both understanding and concrete tools for tomorrow morning. A
teenager first needs to trust that the space is their own. And often, when the request concerns a
child, the most substantial work happens with the parents.</p>
<p>Sessions last {SESSION} minutes and take place at the practice in {CITY} or online, in Greek or
in English.</p>
</div>
<h2 class="cb-h2" data-reveal>Choose a setting</h2>
{svc_cards(d, items=kids, cls="cb-cards")}
<div data-reveal style="margin-top:2.5rem">{online_note()}</div>
<div data-reveal style="margin-top:2rem">{crisis_note()}</div>
</div>
{aside(d, extra=cta_button(d))}
</div>
</div>
</section>"""
    ld = [practice_ld(), person_ld(),
          {"@type": "CollectionPage", "@id": U(slug) + "#page", "url": U(slug),
           "name": name, "inLanguage": "en-GB",
           "hasPart": [{"@type": "Service", "name": plain(L(k, "short")), "url": U(S(k))}
                       for k in kids]},
          breadcrumb_ld([(T("nav.home"), U("en/index.html")), (name, U(slug))])]
    return render(depth=d,
                  title=f"Psychotherapy &amp; Counselling {CITY}, Athens | Children, Teens, Adults",
                  description=("Psychotherapy for children, teenagers and adults and parent "
                               f"counselling in {CITY}, Athens or online, with clinical assessment "
                               "from the first meeting."),
                  canonical=U(slug), ld_graph=ld, active=S(cat), content=hero + body)


# ==================================================================== ΕΠΙΚΟΙΝΩΝΙΑ
def contact_en():
    d, slug = 1, "en/contact.html"
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")), (T("nav.contact"), None)])
    hero = page_hero("Contact", "Book your<br>appointment",
                     f"By phone on {PHONE_P}, or with a message through the form below. "
                     "A first contact commits you to nothing.", crumbs, marq_word="CONTACT")
    maps_embed = ("https://www.google.com/maps?q=" +
                  "%CE%95%CE%B8%CE%BD%CE%AC%CF%81%CF%87%CE%BF%CF%85%20"
                  "%CE%9C%CE%B1%CE%BA%CE%B1%CF%81%CE%AF%CE%BF%CF%85%2025%20"
                  "%CE%97%CE%BB%CE%B9%CE%BF%CF%8D%CF%80%CE%BF%CE%BB%CE%B7&output=embed")
    body = f"""<section class="cb-section" id="rantevou">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2">
<div data-reveal>
<h2 class="cb-h2" style="margin-top:0">Contact details</h2>
{contact_card(d)}
<div style="margin-top:2rem">{online_note()}</div>
<div class="cb-prose" style="margin-top:2rem">
<h3>Getting here</h3>
<p>The practice is at {STREET}, in {CITY}, in a central spot with easy access from across Attica.
See <a href="psychologist-ilioupoli.html">detailed directions and the areas served</a>.</p>
<h3>Online sessions</h3>
<p>Sessions can also be held online, with the same duration and the same way of working — from
anywhere in Greece or abroad. You need only a quiet space and a stable connection. Sessions are held
in Greek and in English.</p>
<h3>Writing to me</h3>
<p>If you prefer to write, use the form or email <a href="mailto:{EMAIL}">{EMAIL}</a> with a contact
number and I will call you back. Please <strong>do not send sensitive health data by email</strong>
— email is not a secure channel for that kind of information.</p>
</div>
{crisis_note()}
</div>
<div data-reveal>{contact_form(d)}</div>
</div>
</div>
</section>

<section class="cb-section cb-section--lilac">
<div class="container mx-auto px-6 md:px-12">
<div style="max-width:62rem" data-reveal>
<span class="cb-eyebrow">Areas served</span>
<h2 class="cb-h2">Where we can meet</h2>
{areas_block()}
</div>
</div>
</section>

<section class="cb-section--tight" style="padding-bottom:0">
<div class="cb-mapsection">
<h2 class="cb-h2" style="text-align:center">Where to find me</h2>
</div>
<div style="margin-top:2rem">
<iframe class="cb-map" src="{maps_embed}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
 title="Map: {STREET}, {CITY}"></iframe>
</div>
</section>"""
    ld = [practice_ld(), person_ld(),
          {"@type": "ContactPage", "@id": U(slug) + "#page", "url": U(slug),
           "name": "Contact", "inLanguage": "en-GB", "about": {"@id": SITE_URL + "/#grafeio"}},
          breadcrumb_ld([(T("nav.home"), U("en/index.html")), ("Contact", U(slug))])]
    return render(depth=d, title=f"Contact &amp; Appointments | Psychologist {CITY}, Athens",
                  description=(f"Book an appointment with {NAME}, Clinical Psychologist MSc in "
                               f"{CITY}, Athens. Tel. {PHONE_P}, email {EMAIL}. In person or online."),
                  canonical=U(slug), ld_graph=ld, active="epikoinonia.html", content=hero + body)


# ==================================================================== ΤΟΠΙΚΗ
def local_en():
    d, slug = 1, "en/psychologist-ilioupoli.html"
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")),
                             (f"Psychologist in {CITY}", None)])
    hero = page_hero(f"{CITY} · {REGION}", f"Psychologist<br>in {CITY}",
                     "Where the practice is, how to get here and which areas are served — together "
                     "with online sessions across Greece and abroad.", crumbs, marq_word=CITY.upper())
    area_items = "".join(f"<li>{a}</li>" for a in AREAS_NEAR)
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div>
<figure class="cb-figure" data-reveal style="margin-bottom:2.5rem">
<img src="../assets/img/grafeio-43.jpg" width="900" height="675" loading="lazy" decoding="async"
 alt="The consulting room in {CITY}: armchair, floor lamp, plants and the qualifications on the wall">
</figure>
<div class="cb-prose" data-reveal>
<h2 class="cb-h2" style="margin-top:0">The practice</h2>
<p>The practice is at <strong>{STREET}</strong>, in {CITY} ({ZIP_PRETTY}). The space has been set up
to be discreet and warm: a therapeutic meeting needs quiet, daylight and the sense that nobody is in
a hurry.</p>
<h2 class="cb-h2">Getting here</h2>
<p>{CITY} sits in the southern suburbs of Athens with good road access from across Attica, and there
is street parking nearby. Exact directions are sent with your appointment confirmation.</p>
<h2 class="cb-h2">English-speaking psychologist in Athens</h2>
<p>Sessions are held in Greek and in English. If you have recently moved to Athens, or if English is
the language you think and feel in, therapy can be conducted entirely in English — in person here in
{CITY}, or online.</p>
<h2 class="cb-h2">Areas served in person</h2>
<p>The nearest areas to the practice:</p>
<ul class="cb-cols">{area_items}</ul>
<p>All other areas of Attica are served equally. For anyone further afield — or abroad — online
sessions carry exactly the same framework.</p>
</div>
<div data-reveal style="margin-top:2.5rem">{online_note()}</div>
<h2 class="cb-h2" data-reveal style="margin-top:3rem">Services</h2>
{cat_cards(d)}
</div>
{aside(d, extra=cta_button(d))}
</div>
</div>
</section>"""
    ld = [practice_ld(), person_ld(),
          {"@type": "WebPage", "@id": U(slug) + "#page", "url": U(slug),
           "name": f"Psychologist in {CITY}", "inLanguage": "en-GB",
           "about": {"@id": SITE_URL + "/#grafeio"}},
          breadcrumb_ld([(T("nav.home"), U("en/index.html")),
                         (f"Psychologist {CITY}", U(slug))])]
    return render(depth=d, title=f"English-speaking Psychologist in {CITY}, Athens | {NAME}",
                  description=(f"Clinical psychologist in {CITY}, Athens. Sessions in English and "
                               "Greek, in person across Attica or online worldwide."),
                  canonical=U(slug), ld_graph=ld, active="index.html", content=hero + body)


# ==================================================================== ΕΡΩΤΗΣΕΙΣ
def faq_en():
    d, slug = 1, "en/faq.html"
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")), ("FAQ", None)])
    hero = page_hero("FAQ", "Frequently asked<br>questions",
                     "Practical answers about how therapy works, what a first session involves, "
                     "confidentiality and appointments.", crumbs, marq_word="QUESTIONS")
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div>
<div data-reveal>{faq_block(ALL_FAQ_EN)}</div>
<div data-reveal style="margin-top:2.5rem">{crisis_note()}</div>
</div>
{aside(d, extra=cta_button(d))}
</div>
</div>
</section>"""
    ld = [practice_ld(), person_ld(), faq_ld(ALL_FAQ_EN),
          breadcrumb_ld([(T("nav.home"), U("en/index.html")), ("FAQ", U(slug))])]
    return render(depth=d, title=f"Frequently Asked Questions | Psychologist {CITY}, Athens",
                  description=("Answers about psychotherapy: how to book, session length, "
                               "confidentiality, online sessions and sessions in English."),
                  canonical=U(slug), ld_graph=ld, active="index.html", content=hero + body)


# ==================================================================== ΑΡΘΡΑ
def articles_en():
    d, slug = 1, "en/articles.html"
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")), (T("nav.articles"), None)])
    hero = page_hero("Articles", "Reading<br>room",
                     "Psychoeducational texts on what comes up most often in the consulting room.",
                     crumbs, marq_word="ARTICLES")
    card = f"""<a class="cb-card" href="articles/carer-self-care.html" data-reveal>
<span class="cb-card__ic">{icon('book','w-7 h-7')}</span>
<span class="cb-card__t">The self-care of those who care</span>
<span class="cb-card__d">When you look after someone every day — a parent, a child, a partner, a
patient — your own exhaustion becomes invisible. What carer burden is, how to recognise it and what
actually helps.</span>
<span class="cb-card__more">{T("cta.more")} <span>&#8594;</span></span></a>"""
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-cards cb-cards--3">{card}</div>
</div>
</section>"""
    ld = [practice_ld(), person_ld(),
          {"@type": "CollectionPage", "@id": U(slug) + "#page", "url": U(slug),
           "name": "Articles", "inLanguage": "en-GB"},
          breadcrumb_ld([(T("nav.home"), U("en/index.html")), ("Articles", U(slug))])]
    return render(depth=d, title=f"Articles | {NAME}, Clinical Psychologist",
                  description="Psychoeducational articles on psychotherapy, parenting and self-care.",
                  canonical=U(slug), ld_graph=ld, active="arthra.html", content=hero + body)


ARTICLE_FAQ_EN = [
 ("Is it selfish to think about myself when someone else is ill?",
  "<p>No. A carer who collapses stops being able to care. Looking after yourself is not taken away "
  "from the person you care for — it is what makes continuing to care possible.</p>"),
 ("I don't have time for self-care. What can I realistically do?",
  "<p>Start from what takes ten minutes, not from what takes a weekend. A short walk, a phone call "
  "to someone who knows, a meal eaten sitting down. Small and repeatable beats large and "
  "hypothetical.</p>"),
 ("How do I know whether I have crossed from tiredness into burnout?",
  "<p>Tiredness lifts with rest; burnout does not. If sleep no longer restores you, if you feel "
  "detached from the person you care for, or if you are irritable in a way that is not like you, "
  "that is worth taking seriously.</p>"),
 ("Where do I ask for help?",
  "<p>From your GP, from a mental health professional, or from a carers' support group. If you "
  "would like to talk it through, <a href=\"../contact.html#rantevou\">get in touch</a>.</p>"),
]


def article_en():
    d, slug = 2, "en/articles/carer-self-care.html"
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")),
                             (T("nav.articles"), page_slug("arthra.html")),
                             ("The self-care of those who care", None)])
    hero = page_hero("Psychoeducation", "The self-care of<br>those who care",
                     "When you look after someone every day, your own exhaustion becomes invisible "
                     "— first of all to you.", crumbs, marq_word="CARE")
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div>
<div class="cb-prose" data-reveal>
<h2 class="cb-h2" style="margin-top:0">Care as invisible work</h2>
<p>Looking after someone who depends on you — an ageing parent, a child with additional needs, a
partner who is ill — is work. It is rarely named as such, it is almost never counted in hours, and
it usually falls to one person in the family rather than being shared.</p>
<p>Because it is invisible, the tiredness it produces is invisible too. Carers routinely describe
feeling that they have no right to be tired, since "they are not the one who is ill".</p>

<h2 class="cb-h2">What carer burden is</h2>
<p>Carer burden is the cumulative physical, emotional and practical strain of sustained caring. It
is not a personal weakness and it is not a failure of love. It is a predictable outcome of a
demanding role carried without enough support, and it shows itself in recognisable ways:</p>
<ul>
<li>Exhaustion that sleep does not repair.</li>
<li>Irritability or anger that feels out of character, often followed by guilt.</li>
<li>Emotional numbness or distance towards the person being cared for.</li>
<li>Withdrawal from friendships and from anything that used to be pleasure.</li>
<li>Physical symptoms: headaches, disrupted sleep, changes in appetite, frequent minor illness.</li>
<li>The persistent thought that whatever you do, it is not enough.</li>
</ul>

<h2 class="cb-h2">The paradox of self-care</h2>
<p>The advice "look after yourself" tends to land badly on carers, because it sounds like one more
task on a list that is already impossible. Worse, it can sound like an accusation: as though the
exhaustion were the result of not having tried hard enough.</p>
<p>It helps to reframe it. Self-care here is not indulgence and not a project. It is
<strong>maintenance of the resource the other person depends on</strong>. A carer who breaks down
does not care better; they stop caring altogether.</p>

<h2 class="cb-h2">What actually helps</h2>
<ul>
<li><strong>Name the role.</strong> Saying "I am a carer" out loud changes how the tiredness is
understood — by you first, and then by the people around you.</li>
<li><strong>Make the work visible.</strong> Write down what you actually do in a week. Most carers
are startled by the list, and it becomes far easier to ask for specific help.</li>
<li><strong>Ask for concrete things.</strong> "Help me sometime" gets nowhere. "Can you take
Thursday afternoons" gets an answer.</li>
<li><strong>Protect something small and regular.</strong> Twenty minutes that reliably belong to you
outperform a holiday you keep postponing.</li>
<li><strong>Let the guilt be there without obeying it.</strong> Guilt is almost universal among
carers and it is a poor guide to decisions.</li>
<li><strong>Find people who understand.</strong> A carers' group, or one friend in the same
position, does something no amount of general sympathy can.</li>
</ul>

<h2 class="cb-h2">When to talk to someone</h2>
<p>Speak to a professional if the exhaustion has stopped lifting, if you feel persistently low or
anxious, if you are relying on alcohol or medication to get through, or if you have thoughts of
harming yourself. None of this means you have failed at caring. It means the load has outgrown what
one person can carry alone, which is a fact about the load, not about you.</p>
</div>
<div data-reveal style="margin-top:2.5rem">{crisis_note()}</div>
<h2 class="cb-h2" data-reveal style="margin-top:2.5rem">Frequently asked questions</h2>
<div data-reveal>{faq_block(ARTICLE_FAQ_EN)}</div>
<h2 class="cb-h2" data-reveal style="margin-top:3rem">Related services</h2>
{related_chips(d, "ypiresies/psychotherapeia-paidion.html")}
</div>
{aside(d, extra=cta_button(d))}
</div>
</div>
</section>"""
    ld = [practice_ld(), person_ld(),
          {"@type": "Article", "@id": U(slug) + "#article", "url": U(slug),
           "headline": "The self-care of those who care", "inLanguage": "en-GB",
           "datePublished": "2026-08-26", "dateModified": TODAY,
           "author": {"@id": SITE_URL + "/viografiko.html#psychologos"},
           "publisher": {"@id": SITE_URL + "/#grafeio"}},
          faq_ld(ARTICLE_FAQ_EN),
          breadcrumb_ld([(T("nav.home"), U("en/index.html")),
                         ("Articles", U("en/articles.html")),
                         ("The self-care of those who care", U(slug))])]
    return render(depth=d, title="The Self-Care of Those Who Care | Carer Burnout",
                  description=("What carer burden is, how to recognise it and what actually helps "
                               "when you look after someone every day."),
                  canonical=U(slug), ld_graph=ld, active="arthra.html",
                  content=hero + body, og_type="article")


# ==================================================================== ΝΟΜΙΚΑ
PRIVACY_EN = f"""
<h2 class="cb-h2" style="margin-top:0">Data controller</h2>
<p>{NAME}, Clinical Psychologist (licence no. {LICENSE}), {STREET}, {ZIP_PRETTY} {CITY}, Greece.
Phone <a href="tel:+30{PHONE}">{PHONE_P}</a>, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 class="cb-h2">What data is collected</h2>
<ul>
<li><strong>Contact details:</strong> name, phone number and email address, when you contact me by
phone, by email or through the website form.</li>
<li><strong>What you write in the form:</strong> only what you choose to include. Please do not send
sensitive health data through the form or by email — neither is a secure channel.</li>
<li><strong>Clinical records:</strong> if a therapeutic relationship begins, notes are kept as
required by professional practice. These are never collected through this website.</li>
<li><strong>The website itself sets no analytics or advertising cookies.</strong></li>
</ul>

<h2 class="cb-h2">Embedded map</h2>
<p>The contact page embeds a Google Maps frame so that you can find the practice. When that frame
loads, Google may receive your IP address and set its own cookies, under
<a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer">Google's
privacy policy</a>. If you would rather avoid this, use the postal address rather than the map.</p>

<h2 class="cb-h2">Purpose and legal basis</h2>
<p>Contact details are processed solely in order to answer your message and, where relevant, to
arrange an appointment — on the basis of your consent and of steps taken at your request prior to
entering into a contract. Clinical records are processed on the basis of the provision of health
care and of professional obligations.</p>

<h2 class="cb-h2">Confidentiality and its limits</h2>
<p>Everything discussed in session is covered by professional confidentiality. The exceptions are
narrow, and they are stated at the outset of any therapeutic relationship: serious and immediate
risk to your safety or to that of another person, the protection of a minor, and cases where
disclosure is required by law or by a judicial authority.</p>

<h2 class="cb-h2">Minors</h2>
<p>Where the client is a minor, therapy requires the consent of those holding parental
responsibility. Parents are informed of the direction of the work and of anything affecting the
child's safety, but not of the content of sessions — that distinction is what makes the work
possible.</p>

<h2 class="cb-h2">Retention</h2>
<p>Messages sent through the form or by email are kept only for as long as is needed to deal with
your request, and are then deleted. Clinical records are retained for the period required by
professional and legal obligations.</p>

<h2 class="cb-h2">Your rights</h2>
<p>Under the GDPR you have the right of access to your data, and to rectification, erasure,
restriction of processing, objection and portability. To exercise any of these, write to
<a href="mailto:{EMAIL}">{EMAIL}</a>. You also have the right to lodge a complaint with the Hellenic
Data Protection Authority (<a href="https://www.dpa.gr" target="_blank" rel="noopener noreferrer">dpa.gr</a>).</p>

<h2 class="cb-h2">Security</h2>
<p>Reasonable technical and organisational measures are applied to protect your data. No transmission
over the internet, however, is entirely secure — which is why sensitive health information should be
discussed in session rather than sent electronically.</p>
"""

TERMS_EN = f"""
<h2 class="cb-h2" style="margin-top:0">The nature of this content</h2>
<p>Everything published on this website is general information and psychoeducational material. It
does <strong>not</strong> constitute a diagnosis, a treatment plan or personalised clinical advice,
and it cannot replace an assessment by a qualified professional who knows your situation.</p>

<h2 class="cb-h2">Emergencies</h2>
<p>This website is not an emergency service and messages are not monitored around the clock. If you
are thinking of harming yourself or another person, call <a href="tel:1018">1018</a> (Suicide
Intervention Line, 24/7), <a href="tel:10306">10306</a> (Psychological Support Line) or
<a href="tel:112">112</a>.</p>

<h2 class="cb-h2">Appointments and cancellations</h2>
<p>Sessions are by appointment only and last {SESSION} minutes. Fees, frequency and the cancellation
policy are discussed openly before any therapeutic relationship begins, so that the framework is
agreed rather than assumed.</p>

<h2 class="cb-h2">Complementary methods</h2>
<p>Theta Healing and therapeutic dowsing are offered as complementary relaxation practices, in a
setting entirely separate from psychotherapy. They are not psychotherapy, they do not have
scientific evidence comparable to that of recognised psychotherapeutic approaches, and they do not
replace psychological, psychiatric or medical care.
<a href="services/energy-therapies.html">The full framework is set out here</a>.</p>

<h2 class="cb-h2">Intellectual property</h2>
<p>The texts, images and design of this website are protected by copyright. Reproduction in whole or
in part without written permission is not permitted. Short quotations with a clear attribution and a
link to the source are welcome.</p>

<h2 class="cb-h2">Third-party links</h2>
<p>Where this site links to third-party websites, it does so for your convenience. No responsibility
is accepted for their content or their privacy practices.</p>

<h2 class="cb-h2">Governing law</h2>
<p>These terms are governed by Greek law. Professional practice is subject to the code of conduct
for psychologists and to the relevant Greek legislation.</p>
"""


def legal_en(slug, eyebrow, h1, lede, prose, title, desc):
    d = 1
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")), (h1, None)])
    hero = page_hero(eyebrow, h1, lede, crumbs)
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-prose" style="max-width:72ch">{prose}
<p style="margin-top:2.5rem;font-size:.85rem;opacity:.7">Last updated: August 2026.</p></div>
</div>
</section>"""
    ld = [practice_ld(), breadcrumb_ld([(T("nav.home"), U("en/index.html")), (h1, U(slug))])]
    return render(depth=d, title=title, description=desc, canonical=U(slug), ld_graph=ld,
                  active="", content=hero + body, with_cta=False)


def not_found_en():
    d = 1
    hero = page_hero("404", "Page not found",
                     "The address you asked for does not exist or has moved. Try one of the links "
                     "below.", "")
    links = "".join(f'<a class="cb-chip" href="{rel(d)}{h}">{l}</a>' for l, h in nav_items())
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-prose"><p>You can carry on from here:</p></div>
<div class="cb-chips">{links}</div>
<p style="margin-top:2.5rem"><a class="cb-btn" href="tel:+30{PHONE}">{icon('phone','w-4 h-4')}<span>{PHONE_P}</span></a></p>
</div>
</section>"""
    return render(depth=d, title="Page not found | " + BRAND_SHORT,
                  description="The page you asked for was not found.",
                  canonical=U("en/404.html"), ld_graph=[practice_ld()], active="",
                  content=hero + body, noindex=True, with_cta=False)


# ==================================================================== ΣΥΓΚΕΝΤΡΩΣΗ
def pages_en():
    """Όλες οι αγγλικές σελίδες, με κλειδί το αγγλικό τους slug."""
    out = {
        "en/index.html":                  home_en(),
        "en/about.html":                  about_en(),
        "en/services.html":               services_en(),
        "en/contact.html":                contact_en(),
        "en/psychologist-ilioupoli.html": local_en(),
        "en/faq.html":                    faq_en(),
        "en/articles.html":               articles_en(),
        "en/articles/carer-self-care.html": article_en(),
        "en/privacy-policy.html": legal_en(
            "en/privacy-policy.html", "Legal", "Privacy Policy",
            "How your personal data is collected, used and protected, in accordance with the GDPR.",
            PRIVACY_EN, "Privacy Policy | " + BRAND_SHORT,
            "Privacy policy: what data is collected, confidentiality and its limits, the framework "
            "for minors, retention periods and your rights under the GDPR."),
        "en/terms-of-use.html": legal_en(
            "en/terms-of-use.html", "Legal", "Terms of Use",
            "The terms under which the content and services of this website are provided.",
            TERMS_EN, "Terms of Use | " + BRAND_SHORT,
            "Terms of use: the nature of the content, appointments and cancellations, emergencies, "
            "complementary methods and intellectual property."),
        "en/404.html":                    not_found_en(),
    }
    for slug, cfg in SERVICE_PAGES_EN.items():
        out[PAGE_SLUGS[slug]] = service_page(slug, cfg)
    for cat in CATEGORIES:
        if cat["children"]:
            out[cat["slug_en"]] = category_en(cat)
    return out
