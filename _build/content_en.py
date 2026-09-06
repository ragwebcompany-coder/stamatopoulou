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
       "burnout, relationships and identity. The request and the goals are set together."),
 eyebrow="Adults",
 marq="ADULTS",
 h1="Adult<br>Psychotherapy",
 lede=("A space and a time of your own, where you can look at what is happening to you without "
       "hurry and without judgement — and work on it in a way that makes sense for your life."),
 facts=[("For", "Adults of any age")] + COMMON_FACTS_EN +
       [("Frequency", "Usually weekly at first; adjusted to the goals")],
 body="""
<h2 class="cb-h2" style="margin-top:0">How we work</h2>
<p>The first meeting is one of <strong>getting acquainted</strong>: we take a
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
 desc=(f"Play therapy and creative arts in {CITY}, Athens: symbolic techniques, drawing, "
       "storytelling and dramatisation — working through deep material without having to name it."),
 eyebrow="Play Therapy",
 marq="PLAY",
 h1="Play Therapy &amp;<br>Creative Arts",
 lede=("Play is a child's language and toys are its words. In play therapy, play is not a break from "
       "the work — it is the work. And it is not only play: these are symbolic techniques, and they "
       "reach where words do not."),
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

<h2 class="cb-h2">Not "just playing"</h2>
<p>Play therapy does not stop at play. At its core are <strong>symbolic techniques</strong> — the
symbol, the figure, the image, the role, the story — through which material that has not yet found
words can be worked with.</p>
<p>That is precisely their value: a person can work through deep material at a
<strong>subconscious and unconscious level</strong>, without having to put it into words. The
understanding of what happens there rests largely on the psychoanalytic tradition, from which play
therapy takes its theory of the symbol and the unconscious.</p>
<p>So this is not a method "for small children who play". It is a process with depth — and it works
with teenagers and with adults too, when words alone have reached their limit.</p>

<h2 class="cb-h2">What it involves</h2>
<ul>
<li><strong>Symbolic play, non-directive and directive</strong> — with figures, dolls,
construction, board games that work on taking turns, losing and cooperating. Most of it is led by the
child; directive work comes in deliberately, where it is needed.</li>
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
       "specific direction that follows from the therapeutic request.</p>"),
      ("Is it used with adults as well?",
       "<p>Yes, selectively. Creative and expressive techniques are often useful with adults who "
       "understand their difficulty intellectually but find that nothing shifts — the symbol reaches "
       "where explanation has stopped working.</p>"),
      ("How is progress measured if it is \"just playing\"?",
       "<p>Through what changes outside the room: sleep, school, relationships, the frequency of "
       "outbursts. The play itself also changes — themes that were repeated compulsively begin to "
       "resolve, and that is visible.</p>")]),

# ------------------------------------------------------------------ energy therapies
"ypiresies/theta-healing.html": dict(
 title=f"Theta Healing {CITY}, Athens | Work in the theta state",
 desc=("Theta Healing in " + CITY + ", Athens or online: guided work in the theta brainwave state, "
       "where very deep material can be reached. No age limit."),
 eyebrow="Theta Healing",
 marq="THETA",
 h1="Theta<br>Healing",
 lede=("Guided work in the theta brainwave state — where the mind becomes receptive and material "
       "that stays out of reach in ordinary waking alertness can be worked with."),
 facts=[("For", "Any age; for minors, always with the parents' agreement")] + COMMON_FACTS_EN,
 body="""
<h2 class="cb-h2" style="margin-top:0">A route towards deeper beliefs and self-knowledge</h2>
<p>ThetaHealing® is a technique of personal and spiritual development created by Vianna Stibal. It
combines the meditative state, natural intuition and the exploration of the deeper beliefs that may
shape how we perceive ourselves, how we relate and how we move through life.</p>
<p>At its basis lies the idea that behind many conscious thoughts and choices there may be deeper
beliefs and repeating patterns. Through targeted questions, a person has the chance to recognise
them, to explore where they came from and to gain greater awareness of how they operate in their
life.</p>

<h2 class="cb-h2">The Theta state</h2>
<p>The name of the technique is connected to the theta brainwaves, a normal form of electrical
activity in the brain. Activity in the theta band has been studied, among other things, in relation
to different states of meditation and inward concentration.</p>
<p>ThetaHealing® uses a guided meditative process, aiming at a state of deeper inward focus and
observation. No previous experience of meditation is required, and the person remains conscious,
present and active throughout the session.</p>

<h2 class="cb-h2">What can we explore?</h2>
<p>A session may focus on different areas of personal exploration, such as:</p>
<ul><li>limiting beliefs and subconscious patterns</li><li>fears, insecurities and inner
obstacles</li><li>repeating patterns in relationships</li><li>self-image, self-esteem and a sense of
personal worth</li><li>boundaries, trust and expressing personal needs</li><li>beliefs about love,
relationships, work, success and abundance</li><li>personal goals and the changes one wants</li>
<li>the wish for deeper self-knowledge, inner connection and personal development</li></ul>
<p>Of particular interest are often those points where a person feels they know consciously what
they want, yet something within seems to lead them back to the same pattern.</p>

<h2 class="cb-h2">How does a ThetaHealing® session work?</h2>
<p>The session begins with the subject the person themselves wishes to explore. Through
conversation and targeted questions, we gradually attempt to recognise the deeper beliefs that may
be connected to it.</p>
<p>The technique may use muscle testing as a tool for exploring beliefs, as well as the digging
process: a sequence of questions intended to lead from the initial issue to deeper levels of meaning
and belief.</p>
<p>The practitioner works as a guide rather than a director: they do not decide for the person, nor
tell them what to do. The process is founded on respect for their personal autonomy and their own
pace, and any intervention presupposes their consent.</p>
<p>The aim is not to hand over ready answers, but to create a space of deeper inward observation: to
bring light to beliefs and patterns that operate less consciously, and to open room for different
perspectives, choices and possibilities.</p>
<p>Every session is different, because so is the person who comes to it.</p>

<h2 class="cb-h2">A complementary approach</h2>
<div class="cb-note cb-note--scope">ThetaHealing® is used as a complementary tool for
self-knowledge, personal exploration and spiritual development. It is not psychotherapy, nor
psychological or medical treatment, and it does not replace assessment, diagnosis or care by the
appropriate health professional where that is needed.</div>
""",
 faq=[("Is there an age limit?",
       "<p>No. It can be applied at any age. Where a minor is involved, the <strong>parents' "
       "agreement</strong> always comes first.</p>"),
      ("What will I need to do in a session?",
       "<p>I will guide you into a state of deep relaxation, and from there we work together. No "
       "previous experience of meditation or similar practices is needed.</p>"),
      ("Can it replace my medication?",
       "<p>No. It does not replace medication or medical follow-up, and no recommendation to stop "
       "either is given. If you are considering a change to your treatment, discuss it with your "
       "treating clinician.</p>"),
      ("How many sessions are needed?",
       "<p>It depends on what you bring. Some requests are worked through in a few sessions, others "
       "need more. It is discussed from the start and revisited as we go.</p>")]),

"ypiresies/therapeftiki-radiaisthisia.html": dict(
 title=f"Therapeutic Dowsing {CITY}, Athens | Pendulum &amp; charts",
 desc=("Therapeutic dowsing in " + CITY + ", Athens or online: work with a pendulum and charts as a "
       "method of locating and rebalancing. No age limit."),
 eyebrow="Therapeutic Dowsing",
 marq="DOWSING",
 h1="Therapeutic<br>Dowsing",
 lede=("Work with a pendulum and charts, as a method of locating and rebalancing — a standalone "
       "method, with its own sessions."),
 facts=[("For", "Any age; for minors, always with the parents' agreement")] + COMMON_FACTS_EN +
       [("Training", "Radiestezyjne Studio Subtelnych Energii, Poland")],
 body="""
<p>Therapeutic Dowsing is an energy practice based on the idea that a person has an energy field,
within which different states can be expressed as different qualities of vibration or frequency.</p>
<p>In practice, specialist dowsing tools and frequency systems are used. First a dowsing exploration
is carried out, in order to identify the energetic parameters that, according to the method, need
work. The corresponding frequencies are then selected and applied, with the aim of releasing
possible energetic burdens and returning the field to a more balanced state.</p>
<p>This means that the same protocol is not applied to everyone. The process and the frequencies
used are chosen individually, on the basis of the personal request and of the dowsing
exploration.</p>
<p>Depending on the school and the system of application, dowsing may also make use of colour
vibrations, frequency charts and different specialist tools. Its applications are found mainly in
energy work with people, while more broadly dowsing is also applied to animals, spaces and the
environment.</p>
<p>Therapeutic Dowsing may be chosen by people interested in a more holistic and energetic approach
to personal wellbeing, who already have an interest in energy practices, or who wish to get to know
a different way of working with energy.</p>
<p>A session can take place in person or at a distance, since, according to the methodology of
dowsing, its application does not require the physical presence of the person in the same room as
the practitioner. The process is always carried out after the person has been informed and has given
their consent.</p>

<h2 class="cb-h2">The certification</h2>
<figure class="cb-figure cb-figure--cert">
<img src="../../assets/img/cert-radiaisthisia.jpg" width="760" height="1140" loading="lazy"
 decoding="async"
 alt="Certificate in Therapeutic Dowsing in the name of Christina Stamatopoulou, from the Polish Radiestezyjne Studio Subtelnych Energii Non Profit">
<figcaption>Certification in <strong>Therapeutic Dowsing</strong> (Radiestezja Terapeutyczna) from
the Polish <strong>Radiestezyjne Studio Subtelnych Energii &ldquo;Non Profit&rdquo; (RSSE)</strong>.
The training covers the Technology of Therapeutic Dowsing, the use of specialist dowsing tools and
of the Prometheus system, and work with frequencies and colour vibrations.</figcaption>
</figure>

<div class="cb-note cb-note--scope"><strong>An important clarification.</strong> Therapeutic Dowsing
belongs to the field of energy practices and is not a method of medical or psychological diagnosis
or treatment. The concepts of the energy field and of frequencies are described according to the
theoretical framework of the method and are not scientifically established mechanisms of modern
biomedical science. It does not replace medical, psychological or psychiatric care, nor medication
or any other treatment recommended by a qualified health professional.</div>
""",
 faq=[("Is there an age limit?",
       "<p>No. It can be applied at any age. Where a minor is involved, the <strong>parents' "
       "agreement</strong> always comes first.</p>"),
      ("Is it available online?",
       f"<p>Yes. Sessions take place at the practice in {CITY} or online, with the same "
       f"{SESSION}-minute duration.</p>"),
      ("Can it replace my medication or medical follow-up?",
       "<p>No. It does not replace medication or medical follow-up, and no recommendation to "
       "discontinue either is given.</p>")]),
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
  "understand yourself better. The first sessions are given to history-taking and to shaping the "
  "therapeutic request, and from that we "
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
</div>
<div class="container mx-auto px-6 md:px-12 relative z-10" data-anim="hero-content">
<div class="cb-hero__in">
<span class="cb-eyebrow cb-eyebrow--light" data-anim="hero-in" data-delay=".4">Clinical Psychologist MSc · {CITY}, Athens</span>
<h1 class="cb-hero__h1" data-anim="hero-in" data-delay=".55">Where light meets understanding,<br class="cb-hero__br"> connection is born</h1>
<div class="cb-hero__actions" data-anim="hero-in" data-delay=".85">
<a class="cb-btn cb-btn--light" href="tel:+30{PHONE}">{icon('phone','w-4 h-4')}<span>{PHONE_P}</span></a>
<a class="cb-btn cb-btn--outline" href="#services">THE SERVICES<span class="cb-btn__arrow">&#8594;</span></a>
</div>
</div>
</div>
<div class="cb-hero__cue" data-anim="cue" aria-hidden="true"><span>SCROLL</span><div data-anim="bounce">{icon('chev','w-5 h-5','2')}</div></div>
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
<p>There is no single method that suits everyone. I work with a <strong>holistic
outlook</strong>: I draw together techniques and tools from the evidence-based approaches I have
trained in and from the energy therapies, into a therapeutic plan made for the particular person.</p>
<p>What is used — and in what proportion — is not decided in advance. It follows from the
<strong>nature of what is being asked</strong>, from age, from the context of a life and from the way
each person finds it easiest to express themselves. Where I judge it will help, I suggest bringing
energy methods into the plan — and you are free to ask for them yourself. The aim is always the
<strong>fullest possible therapeutic outcome</strong>.</p>
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
and energy therapies. In every case, the work starts from what you bring.</p>
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
        content=hero + approach + services + who + faq + booking)


# ==================================================================== ΒΙΟΓΡΑΦΙΚΟ
STUDIES_EN = [
 ("MSc Clinical &amp; Community Psychology",
  "University of East London, United Kingdom."),
 ("BSc Applied Psychology",
  "University of Derby, United Kingdom."),
 ("Licence to practise as a Psychologist",
  f"Licence number {LICENSE}, for the Greek territory."),
 ("Member", "Association of Greek Psychologists (S.E.PS.)."),
 ("Play Therapy &amp; Creative Arts",
  "Two-year specialisation, Metropolitan College of Athens."),
 ("Systemic &amp; Family Psychotherapy",
  "Centre for Systemic Study and Therapy (KESMETH), Athens — in progress."),
 ("Counselling, Psychoeducation, Children's Drawing, Psychometric Tools",
  "A series of certified trainings, professional development programmes and seminars."),
 ("ThetaHealing®",
  "Certified practitioner — six separate certifications across different fields of application."),
 ("Therapeutic Dowsing (Radiestezja Terapeutyczna)",
  "Radiestezyjne Studio Subtelnych Energii \u201eNon Profit\u201d (RSSE), Poland."),
 ("First university studies",
  "School of Theology, National and Kapodistrian University of Athens."),
]

TRAINING_EN = [
 ("2023 – 2024", "MSc Clinical &amp; Community Psychology", "University of East London"),
 ("2022 – 2023", "Training in Counselling Skills", "\"Empsychosis\" Centre"),
 ("—", "Play Therapy &amp; Creative Arts", "Metropolitan College"),
 ("In progress", "Systemic &amp; Family Therapy", "Ke.Se.Me.Th., Athens"),
 ("2017 – 2020", "BSc Applied Psychology", "University of Derby"),
]

EXPERIENCE_EN = [
 ("2020 — present", "Clinical Psychologist · Private practice, Psychoptia",
  "Individual psychotherapy sessions with children, teenagers and adults, parent counselling and "
  "play therapy, at the practice in Ilioupoli or online. Every collaboration starts with "
  "history-taking and the shaping of the therapeutic request, so that the framework and its goals "
  "are set jointly with the person."),
 ("Present", "External associate · Specialist therapy centres, Attica",
  "Member of interdisciplinary teams in mental health services and specialist therapy centres: "
  "<strong>Brainbow</strong> — Centre for Special Therapies &amp; Neurofeedback, "
  "<strong>Amilla</strong> — Centre for Therapy and Rehabilitation, and "
  "<strong>Atypical Center</strong> in Dafni, specialising in support for people on the autism "
  "spectrum, among other therapeutic settings."),
 ("Pandemic", "Free counselling sessions",
  "Took part in providing free sessions to people in need, in cooperation with private "
  "counselling and psychotherapy practices."),
 ("Placement", "RECBT Institute",
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
                     "Clinical Psychologist. Studies in the United Kingdom, training in more than "
                     f"one therapeutic approach, and a practice in {CITY} since 2020.",
                     crumbs, marq_word="PROFILE")
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div>
<figure class="cb-figure" data-reveal style="margin-bottom:2.5rem">
<img src="../assets/img/christina-stamatopoulou.jpg" width="1000" height="1502" loading="lazy"
 decoding="async" alt="Portrait of Christina Stamatopoulou, Clinical Psychologist MSc">
</figure>
<div class="cb-prose" data-reveal>
<h2 class="cb-h2" style="margin-top:0">Why me</h2>
<p>To me, every person who walks through the door of the therapy room is a unique phenomenon. A
whole world of experiences, relationships, feelings and meanings, which cannot be contained in a
diagnosis, a symptom or one particular therapeutic technique.</p>
<p>With a holistic and systemic outlook, I try to understand not only the difficulty but the person
within the history, the relationships and the context of a life that have shaped them. That is why I
build every therapeutic plan individually, with respect for the needs, the pace and the singularity
of the person in front of me.</p>
<p>Above all, I believe in the power of the therapeutic relationship. I want my room to be a place
where a person can relax, feel safe, come to trust — and, when they are ready, express even the most
difficult or vulnerable parts of themselves without fear of judgement.</p>
<p>Being a therapist also means, for me, a continuing personal responsibility to develop. Personal
therapy, supervision, ongoing training and contact with current scientific developments are an
inseparable part of my professional path.</p>
<p>The way I work is <strong>holistic</strong>: I draw together techniques and tools from the
evidence-based approaches I have trained in — among them the cognitive–behavioural approach,
systemic and family therapy, and play therapy with the creative arts — and, where I judge it is
needed, from the energy therapies. What is used, and in what proportion, follows from the
<strong>nature of what is being asked</strong> rather than from a preference of mine, and the plan
is built for the fullest possible outcome for the person in front of me.</p>
<p>My training in systemic and family therapy is <strong>ongoing</strong>. I mention it because it
shapes how I think about families — not as a completed qualification.</p>
<p>I do not consider my training a closed chapter. I keep training — because the field moves, but
mostly because my own development is part of the work. The list below describes where I am today,
not where I stop.</p>
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
<strong>therapeutic request</strong>, shaped over the first sessions, on the basis of what best serves what is
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
<li><strong>First meeting: getting acquainted.</strong> I listen to what brings you
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


CAT_PAGE_EN = {
"ypiresies/psychotherapeia-symvouleftiki.html": dict(
 h1="Psychotherapy &amp;<br>Counselling",
 marq="SESSIONS",
 lede=("One therapeutic process, four settings. Which one fits follows from the therapeutic request "
       "as it is shaped — not from a ready-made protocol."),
 introH2="Why me",
 intro="""<p>I work with a <strong>holistic outlook</strong>. I do not apply one method to everyone:
I draw together techniques and tools from the approaches I have trained in and build an
<strong>individualised therapeutic programme</strong> for each person.</p>
<p>What is used follows from the <strong>therapeutic request</strong>, as it is shaped over the first
sessions, together with you. The aim is the fullest possible therapeutic outcome — not fidelity to a
protocol.</p>""",
 chooseH2="Choose a setting",
 title=f"Psychotherapy &amp; Counselling {CITY}, Athens | Children, Teens, Adults",
 desc=("Psychotherapy for children, teenagers and adults and parent counselling in "
       f"{CITY}, Athens or online, with an individualised therapeutic programme."),
 crisis=True),

"ypiresies/energeiakes-therapeies.html": dict(
 h1="Energy<br>Therapies",
 marq="ENERGY",
 lede=("Two standalone methods, with their own framework and their own sessions: Theta Healing and "
       "therapeutic dowsing."),
 introH2="Two distinct methods",
 intro="""<p><strong>Theta Healing</strong> and <strong>therapeutic dowsing</strong> are not one
single method and do not work in the same way. Each has its own framework and its own sessions.</p>
<p>Neither has an age limit. Where a minor is involved, the <strong>parents' agreement</strong>
always comes first.</p>
<div class="cb-note cb-note--scope">These methods <em>never</em> replace medication or medical
follow-up, and no recommendation to discontinue either is given.</div>""",
 chooseH2="Choose a method",
 title=f"Energy Therapies {CITY}, Athens | Theta Healing &amp; Dowsing",
 desc=("Theta Healing and therapeutic dowsing in " + CITY + ", Athens or online: two standalone "
       "methods, with their own sessions and no age limit."),
 crisis=False),
}


def category_en(cat):
    d, slug = 2, cat["slug_en"]
    c = CAT_PAGE_EN[cat["slug"]]
    name = plain(L(cat, "nav"))
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")), (name, None)])
    hero = page_hero("Services", c["h1"], c["lede"], crumbs, marq_word=c["marq"])
    kids = cat_children(cat)
    crisis = f'<div data-reveal style="margin-top:2rem">{crisis_note()}</div>' if c["crisis"] else ""
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div>
<div class="cb-prose" data-reveal>
<h2 class="cb-h2" style="margin-top:0">{c["introH2"]}</h2>
{c["intro"]}
<p>Sessions last {SESSION} minutes and take place at the practice in {CITY} or online.</p>
</div>
<h2 class="cb-h2" data-reveal>{c["chooseH2"]}</h2>
{svc_cards(d, items=kids, cls="cb-cards")}
<div data-reveal style="margin-top:2.5rem">{online_note()}</div>
{crisis}
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
    return render(depth=d, title=c["title"], description=c["desc"],
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

    # Ίδια ομαδοποίηση με την ελληνική σελίδα: δεκαπέντε άρθρα σε ενιαία λίστα
    # θα ήταν τοίχος.
    items = [dict(slug="articles/carer-self-care.html", kicker="Psychoeducation",
                  title="The self-care of those who care",
                  teaser="When you look after someone every day — a parent, a child, a partner, a "
                         "patient — your own exhaustion becomes invisible. What carer burden is, "
                         "how to recognise it and what actually helps."),
             dict(slug="articles/short-term-or-long-term-therapy.html", kicker="Framework",
                  title="Short-term or long-term therapy?",
                  teaser="One or two sessions rarely solve a problem. The pros and cons of each, "
                         "how the request sets the length, and why time here is an investment "
                         "rather than a cost.")] + [
             dict(slug=a["slug"][len("en/"):], kicker=a["kicker"], title=a["title"],
                  teaser=a["teaser"]) for a in ARTICLES_EN]

    order = ["Psychoeducation", "Framework", "Play Therapy", "Parent counselling",
             "Identity & acceptance", "ThetaHealing", "Energy therapies", "Dowsing"]
    groups = {}
    for a in items:
        groups.setdefault(plain(a["kicker"]), []).append(a)
    seen = [k for k in order if k in groups] + [k for k in groups if k not in order]

    def card(a):
        return (f'<a class="cb-post" href="{a["slug"]}" data-reveal>'
                f'<span class="cb-post__k">{a["kicker"]}</span>'
                f'<span class="cb-post__t">{a["title"]}</span>'
                f'<span class="cb-post__d">{a["teaser"]}</span>'
                f'<span class="cb-post__more">{T("cta.more")} <span>&#8594;</span></span></a>')

    sections = "".join(
        f'<h2 class="cb-h2" data-reveal style="margin-top:3.5rem">{k}</h2>'
        f'<div class="cb-posts">{"".join(card(a) for a in groups[k])}</div>'
        for k in seen)

    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
{sections}
<div class="cb-prose" data-reveal style="max-width:60ch;margin-top:3.5rem">
<p>The texts on this page are <strong>informational and psychoeducational</strong>. They are not a
diagnosis, a therapeutic instruction or a substitute for a session with a mental health
professional. If something you read here speaks to you, the next step is not to read more — it is
to talk about it.</p>
</div>
<p style="margin-top:2rem"><a class="cb-btn" href="tel:+30{PHONE}">{icon('phone','w-4 h-4')}<span>{PHONE_P}</span></a></p>
</div>
</section>"""
    ld = [practice_ld(), person_ld(),
          {"@type": "CollectionPage", "@id": U(slug) + "#page", "url": U(slug),
           "name": "Articles", "inLanguage": "en-GB",
           "hasPart": [{"@type": "Article", "headline": plain(a["title"]),
                        "url": U("en/" + a["slug"])} for a in items]},
          breadcrumb_ld([(T("nav.home"), U("en/index.html")), ("Articles", U(slug))])]
    return render(depth=d, title=f"Articles | {NAME}, Clinical Psychologist",
                  description=("Psychoeducational articles on play therapy, parent counselling, "
                               "energy therapies and identity."),
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

<h2 class="cb-h2">Energy therapies</h2>
<p>The energy methods referred to (Theta Healing, therapeutic dowsing) <strong>do not replace
medication or medical follow-up</strong>, and no recommendation to discontinue either is given.
<a href="services/energy-therapies.html">The full description is set out here</a>.</p>

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


# ============================================================ the story of the name
def onoma_en():
    d, slug = 1, "en/the-story-behind-the-name.html"
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")), ("The name", None)])
    hero = page_hero("Psychoptia",
                     "The story behind<br>the name",
                     "<em>Psychoptia</em> is a word born from the meeting of two ideas: "
                     "<strong>psyche</strong> and <strong>optics</strong> — the soul, and the way "
                     "we see.", crumbs, marq_word="PSYCHOPTIA")

    onoma_sec = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div>
<div class="cb-prose" data-reveal>
<h2 class="cb-h2" style="margin-top:0">Soul and perspective</h2>
<p>It was made to name something therapy often does without ever naming it: <strong>the birth of a
new way of seeing human experience</strong>.</p>
<p>Psychotherapy is about the possibility of widening how we see, understand and relate to the
people around us — and above all, to ourselves.</p>
<p>Every therapeutic journey is its own. It does not lead to one shared truth, but to a deeper
relationship with oneself, through greater awareness, fuller understanding and new ways of looking
at a life.</p>
</div>
{infinity_rule()}
</div>
{aside(d, extra=cta_button(d))}
</div>
</div>
</section>"""

    iliotropio = f"""<section class="cb-section cb-section--beige">
<div class="container mx-auto px-6 md:px-12">
<div style="max-width:56rem" data-reveal>
<span class="cb-eyebrow">The symbol</span>
<h2 class="cb-h2">The sunflower</h2>
<p class="cb-lede">It was not the symbol of Psychoptia from the start. Its natural turning towards
the light became the starting point of a new idea: a therapeutic way of seeing oneself, others and
life.</p>
</div>
<figure class="cb-figure cb-figure--wide" data-reveal style="margin:2.75rem 0">
<img src="../assets/img/psychoptia-iliotropio.jpg" width="1440" height="959" loading="lazy"
 decoding="async"
 alt="Five sunflowers in a line of transformation, from yellow to deep violet, with the Psychoptia logotype">
<figcaption>The sunflower's transformation: from the yellow of vitality to the violet of depth.</figcaption>
</figure>
<div class="cb-prose" data-reveal style="max-width:60ch">
<p>In its own transformation, the sunflower begins in <strong>bright yellow</strong> — the colour of
vitality, movement and hope — and gradually turns to deeper shades of <strong>blue and
violet</strong>, which stand for calm, the wisdom of the mind and the depth of human experience:
the light now taken in and carried within.</p>
</div>
</div>
</section>"""

    creed = f"""<section class="cb-section cb-section--dark">
<div class="container mx-auto px-6 md:px-12">
<ul class="cb-creed" data-reveal>
<li><span>Light</span> is the medium.</li>
<li><span>Understanding</span> is the process.</li>
<li><span>Connection</span> is the outcome.</li>
<li><span>Perspective</span> is the change.</li>
</ul>
{infinity_rule()}
</div>
</section>"""

    ld = [practice_ld(), person_ld(),
          {"@type": "AboutPage", "@id": U(slug) + "#page", "url": U(slug),
           "name": "Psychoptia — the story behind the name", "inLanguage": "en-GB",
           "mainEntity": {"@id": SITE_URL + "/viografiko.html#psychologos"}},
          breadcrumb_ld([(T("nav.home"), U("en/index.html")), ("The name", U(slug))])]
    return render(depth=d,
        title="Psychoptia — the story behind the name",
        description=("Psychoptia: psyche and optics. The story of the name and of the sunflower — "
                     "light as the medium, understanding as the process, perspective as the change."),
        canonical=U(slug), ld_graph=ld, active=slug, content=hero + onoma_sec + iliotropio + creed)

# ---------------------------------------------- short-term / long-term therapy
ARTICLE2_FAQ_EN = [
 ("How long will my therapy take?",
  "<p>It cannot honestly be answered over the phone. After the first few meetings it can be answered "
  "approximately: once the request has taken shape, it becomes clear whether we are talking about a "
  "few months or a longer road. That is discussed openly, and revisited as we go — not decided once "
  "and for all.</p>"),
 ("I came for one specific thing and other things are opening up. Is that normal?",
  "<p>It is the most common thing that happens. The initial request is often the door, not the room. "
  "That does not oblige you to go further: it means there is a choice, and the choice is yours. "
  "Closing a short-term piece of work having achieved what you asked for is a perfectly good "
  "outcome, not an unfinished one.</p>"),
 ("Can I stop whenever I want?",
  "<p>Yes — therapy is not a contract. What I do ask is that stopping is not done silently: one "
  "closing session helps the gains stay with you and keeps the ending from feeling like flight. "
  "Quite often the wish to stop appears exactly where the work begins to touch something that "
  "matters — and that is worth saying out loud rather than acting on.</p>"),
]


def article_duration_en():
    d, slug = 2, "en/articles/short-term-or-long-term-therapy.html"
    title = "Short-term or long-term therapy?"
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")),
                             (T("nav.articles"), page_slug("arthra.html")),
                             (title, None)])
    hero = page_hero("Framework", "Short-term or<br>long-term therapy?",
                     "One or two sessions rarely \u201csolve\u201d anything. What each one does, where "
                     "they really differ, and why the answer always starts from the request.",
                     crumbs, marq_word="DURATION")
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div>
<div class="cb-prose" data-reveal>
<p class="cb-lede">One of the most common things I meet: someone is in a difficult — sometimes
urgent — place, books a session, and expects that one or two meetings will have settled it. The
expectation is entirely understandable. It is not, however, how psychotherapy works, and it is worth
saying so from the start.</p>

<h2 class="cb-h2">A cry for help is not the solution — it is the beginning</h2>
<p>Picking up the phone when you cannot take any more is a significant step, and often the hardest
one. On its own, though, it does not solve the problem. A session in a crisis can bring relief, put
things in order, give you a plan for the next few days. What caused it does not disappear with it.</p>
<p>A psychologist is not a magician and therapy is not a prescription given in a single dose. It is a
<strong>process</strong> — and, like any process, it needs time to pay off. That time is not a cost;
it is the investment itself, and it is one of the few that keep paying decades later.</p>

<div class="cb-note"><strong>If what you are living through is urgent</strong>, psychotherapy is not
the first line. See the 24-hour support lines below — and then, in your own time, arrange a first
meeting.</div>

<h2 class="cb-h2">It all starts from the request</h2>
<p>The length of a therapy is not chosen in advance, nor decided by the calendar. It follows from the
<strong>request</strong>: from what exactly is being asked, and at what depth.</p>
<p>A request can be <em>bounded</em>: a specific phobia, a decision that is stuck, preparing for an
event, stabilising after a crisis. It can equally be <em>open</em>: "I keep repeating the same
relationships", "I don't know who I am outside my roles", "something has weighed on me since
childhood". These two do not need the same amount of time, because they are not asking for the same
thing.</p>
<p>That is why <strong>shaping the request</strong> is the first real work we do together. Very
often, the request someone arrives with is not the one they end up working on.</p>

<h2 class="cb-h2">Short-term therapy</h2>
<p>It is focused and structured. A specific goal is set, we work mainly with <strong>tools and
techniques</strong> — identifying thoughts, exposure, regulation skills, psychoeducation, tasks
between sessions — and progress is reviewed regularly against that goal. Sessions are {SESSION}
minutes, as always; what changes is the scope, not the hour.</p>
{pros_cons("What it offers",
           ["Relief within a relatively short span, when the request is clear.",
            "Concrete tools that remain available after the work ends.",
            "A clear frame: you know what we are working on and how we will know it worked.",
            "A smaller overall commitment of time and money."],
           "What it does not cover",
           ["It does not reach patterns formed over many years.",
            "Where the request was the tip of the iceberg, it eases it without resolving it.",
            "Relapse is more likely if the cause was left untouched.",
            "It asks for enough stability to be able to work in a focused way."])}

<h2 class="cb-h2">Long-term therapy</h2>
<p>Here the goal is not only for a symptom to recede, but for the relationship with oneself to
change: repeating patterns, how one attaches, boundaries, self-image, the history one carries. It is
a slower and less linear process — but what changes, changes at a level that needs no maintenance.</p>
{pros_cons("What it offers",
           ["Change in depth, which holds long after the therapy ends.",
            "The cause is worked with, not only how it shows itself.",
            "Room for what does not fit a narrow goal: relationships, identity, history.",
            "The therapeutic relationship itself becomes a tool — often the strongest one."],
           "What it asks of you",
           ["Time and consistency; it does not work in sparse, occasional meetings.",
            "Tolerance for stretches where there is no measurable \u201cprogress\u201d.",
            "A larger overall financial investment.",
            "A willingness to discuss the unwelcome too, not only the presenting complaint."])}

<h2 class="cb-h2">Not two camps</h2>
<p>In practice the two are not in competition. Many pieces of work begin short-term, with a clear
goal, and there the request deepens: the symptom recedes and the question of where it came from
surfaces. Others stay deliberately brief and close having achieved exactly what was asked — which is
a thoroughly good outcome, not a half-finished one.</p>
<p>What does not change is how it is decided: on <strong>clinical grounds</strong>, discussed with
you, and not on what would be more convenient for either of us.</p>

<h2 class="cb-h2">Why the time is worth it</h2>
<p>Psychotherapy is one of the very few investments that cannot be taken away. What you come to
understand about yourself, what you learn to recognise as it happens, what you gain in boundaries and
in relationships — you keep. It does not expire, it needs no renewal, and it carries into every later
period of a life — very often, into your children's.</p>
<p>So the question is not "how many sessions do I need to be done with this". It is "what do I
actually want to change, and what am I willing to give for it".</p>
</div>

<div data-reveal style="margin-top:2.5rem">{crisis_note()}</div>

<div class="cb-prose" data-reveal style="margin-top:2rem">
<p style="font-size:.9rem;opacity:.75">This text is informational and psychoeducational. It is not a
diagnosis and does not replace a session with a mental health professional.</p>
</div>

<h2 class="cb-h2" data-reveal style="margin-top:3rem">Frequently asked questions</h2>
<div data-reveal>{faq_block(ARTICLE2_FAQ_EN)}</div>

<h2 class="cb-h2" data-reveal style="margin-top:3rem">Related services</h2>
{related_chips(d, "ypiresies/psychotherapeia-paidion.html")}
</div>
{aside(d, extra=cta_button(d))}
</div>
</div>
</section>"""
    ld = [practice_ld(), person_ld(),
          {"@type": "Article", "@id": U(slug) + "#article", "url": U(slug),
           "headline": title, "inLanguage": "en-GB",
           "datePublished": "2026-09-06", "dateModified": TODAY,
           "author": {"@id": SITE_URL + "/viografiko.html#psychologos"},
           "publisher": {"@id": SITE_URL + "/#grafeio"}},
          faq_ld(ARTICLE2_FAQ_EN),
          breadcrumb_ld([(T("nav.home"), U("en/index.html")),
                         ("Articles", U("en/articles.html")), (title, U(slug))])]
    return render(depth=d, title=f"{title} | Pros and cons",
                  description=("The pros and cons of short-term and long-term psychotherapy, how the "
                               "request sets the length, and why one or two sessions do not solve a "
                               "problem."),
                  canonical=U(slug), ld_graph=ld, active="arthra.html", content=hero + body,
                  og_type="article")

# ---------------------------------------------------------------- γενικό άρθρο EN
from articles_data_en import ARTICLES_EN


def article_page_en(a):
    d = 2
    slug = a["slug"]
    crumbs = breadcrumbs(d, [(T("nav.home"), page_slug("index.html")),
                             (T("nav.articles"), page_slug("arthra.html")),
                             (plain(a["title"]), None)])
    hero = page_hero(a["kicker"], a["title"], a["teaser"], crumbs, marq_word=a["marq"])
    body_html = a["body"][0].replace("<p>", '<p class="cb-lede">', 1) + "".join(a["body"][1:])
    body = f"""<section class="cb-section">
<div class="container mx-auto px-6 md:px-12">
<div class="cb-grid-2 cb-grid-2--aside">
<div>
<div class="cb-prose" data-reveal>
{body_html}
</div>

{sources_block_en(a["sources"])}

<div class="cb-prose" data-reveal style="margin-top:2rem">
<p style="font-size:.9rem;opacity:.75">This text is informational and psychoeducational. It is not a
diagnosis and does not replace a session with a mental health professional.</p>
</div>

<div data-reveal style="margin-top:2rem">{crisis_note()}</div>

<h2 class="cb-h2" data-reveal style="margin-top:3rem">Related services</h2>
{related_chips(d, None)}
</div>
{aside(d, extra=cta_button(d))}
</div>
</div>
</section>"""
    ld = [practice_ld(), person_ld(),
          {"@type": "Article", "@id": U(slug) + "#article", "url": U(slug),
           "headline": plain(a["title"]), "description": plain(a["teaser"]),
           "inLanguage": "en-GB", "datePublished": a["date"], "dateModified": TODAY,
           "author": {"@id": SITE_URL + "/viografiko.html#psychologos"},
           "publisher": {"@id": SITE_URL + "/#grafeio"},
           "image": SITE_URL + "/assets/img/og-image.jpg",
           "isAccessibleForFree": True,
           "citation": a["sources"]},
          breadcrumb_ld([(T("nav.home"), U("en/index.html")),
                         ("Articles", U("en/articles.html")), (plain(a["title"]), U(slug))])]
    return render(depth=d,
        title=plain(a["title"]) + (" | " + BRAND_SHORT if len(plain(a["title"])) < 48 else ""),
        description=plain(a["teaser"]),
        canonical=U(slug), ld_graph=ld, active="arthra.html", content=hero + body,
        og_type="article")


def sources_block_en(rows):
    if not rows:
        return ""
    li = "".join("<li>%s</li>" % r for r in rows)
    return (f'<details class="cb-src" data-reveal><summary>Sources &amp; references '
            f'({len(rows)})</summary><ol>{li}</ol></details>')

# ==================================================================== ΣΥΓΚΕΝΤΡΩΣΗ
def pages_en():
    """Όλες οι αγγλικές σελίδες, με κλειδί το αγγλικό τους slug."""
    out = {
        "en/index.html":                  home_en(),
        "en/about.html":                  about_en(),
        "en/the-story-behind-the-name.html": onoma_en(),
        "en/services.html":               services_en(),
        "en/contact.html":                contact_en(),
        "en/psychologist-ilioupoli.html": local_en(),
        "en/faq.html":                    faq_en(),
        "en/articles.html":               articles_en(),
        "en/articles/carer-self-care.html": article_en(),
        "en/articles/short-term-or-long-term-therapy.html": article_duration_en(),
    }
    for a in ARTICLES_EN:
        out[a["slug"]] = article_page_en(a)
    out.update({
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
            "energy therapies and intellectual property."),
        "en/404.html":                    not_found_en(),
    })
    for slug, cfg in SERVICE_PAGES_EN.items():
        out[PAGE_SLUGS[slug]] = service_page(slug, cfg)
    for cat in CATEGORIES:
        if cat["children"]:
            out[cat["slug_en"]] = category_en(cat)
    return out
