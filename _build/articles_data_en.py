# -*- coding: utf-8 -*-
"""Τα άρθρα της Χριστίνας Σταματοπούλου στα αγγλικά.

Απόδοση —όχι μηχανική μετάφραση— των κειμένων του `articles_data.py`. Η δομή
είναι η ίδια (μπλοκ HTML + βιβλιογραφία), ώστε να τα διαβάζει ο ίδιος renderer.
Οι βιβλιογραφικές αναφορές είναι διεθνείς και μένουν αυτούσιες: εισάγονται από
την ελληνική έκδοση αντί να αντιγραφούν.
"""
from articles_data import ARTICLES_EL

_SRC = {a["slug"]: a["sources"] for a in ARTICLES_EL}


# Ορισμένες αναφορές φέρουν ελληνικό επεξηγηματικό σχόλιο της ίδιας. Στην
# αγγλική έκδοση αποδίδεται, ώστε να μη μένουν ελληνικά μέσα σε αγγλική σελίδα.
_GLOSS = {
 "Περιγραφή εφαρμογών του συστήματος σε ενεργειακό πεδίο ανθρώπων, ζώων και χώρων.":
 "A description of the system's applications to the energy field of people, animals and spaces.",
 "Εκπαιδευτικό πλαίσιο και φιλοσοφία της Θεραπευτικής Ραδιαισθησίας.":
 "The training framework and philosophy of Therapeutic Dowsing.",
 "Περιγραφή του συστήματος Prometheus και της ραδιαισθητικής εργασίας με διαφορετικά φάσματα συχνοτήτων.":
 "A description of the Prometheus system and of dowsing work with different frequency ranges.",
 "Παρουσίαση της ιστορίας του Radiestezyjne Studio Subtelnych Energii \u201cNON PROFIT\u201d (RSSE), της εξέλιξης της συγκεκριμένης παράδοσης και των συστημάτων Prometeusz και Merkaba.":
 "An account of the history of Radiestezyjne Studio Subtelnych Energii \u201cNON PROFIT\u201d (RSSE), of the development of this tradition and of the Prometeusz and Merkaba systems.",
 "Στο The Child, the Family and the Outside World.":
 "In The Child, the Family and the Outside World.",
 "Εργασίες για το ψυχαναλυτικό ψυχόδραμα και την ψυχοθεραπευτική εργασία με παιδιά και εφήβους.":
 "Works on analytic psychodrama and psychotherapeutic work with children and adolescents.",
}


def _s(el_slug):
    out = []
    for row in _SRC["arthra/%s.html" % el_slug]:
        for gr, en in _GLOSS.items():
            if gr in row:
                row = row.replace(gr, en)
        out.append(row)
    return out


ARTICLES_EN = [
 dict(
  slug="en/articles/why-we-repeat-the-same-patterns.html",
  el="arthra/thetahealing-epanalipsi-motivon.html",
  kicker="ThetaHealing",
  title="ThetaHealing®: Why do we repeat the same patterns, even when we want to change?",
  marq="PATTERNS",
  date="2026-09-06",
  teaser="We know exactly what we want to change — and still we end up in the same place. What "
         "ThetaHealing® is, what digging is, and why a conscious wish is not always enough.",
  body=[
   '<p>There are moments when we know very well what we want to change.</p>',
   '<p>We know a relationship is not good for us, and yet we end up in similar ones again. We want '
   'to set boundaries, but we struggle to say &ldquo;no&rdquo;. We wish to move forward '
   'professionally, but something holds us back. We recognise a fear as excessive and, even so, we '
   'go on feeling it.</p>',
   '<h2 class="cb-h2">Why is a conscious wish to change not always enough?</h2>',
   '<p>One of the central ideas ThetaHealing® rests on is that the way we perceive ourselves and '
   'our lives is not shaped only by what we think consciously. Deeper beliefs, lived experiences '
   'and repeating patterns can influence how we relate, choose and react.</p>',
   '<p>So sometimes what matters is not only &ldquo;what am I doing?&rdquo;, but &ldquo;what lies '
   'deeper and leads me to do it?&rdquo;.</p>',
   '<h2 class="cb-h2">What is ThetaHealing®?</h2>',
   '<p>ThetaHealing® is a technique of personal and spiritual development created by Vianna '
   'Stibal, focused on exploring deeper beliefs and patterns.</p>',
   '<p>Through a guided meditative process and targeted questions, a person is invited to turn '
   'their attention inward and observe beliefs they may not have consciously recognised until '
   'that moment.</p>',
   '<p>This is not a process in which someone else decides what is &ldquo;wrong&rdquo; and what '
   'must change. The person remains conscious, present and active throughout, and their personal '
   'autonomy and consent are a fundamental part of the process.</p>',
   '<h2 class="cb-h2">The beliefs that work &ldquo;below the surface&rdquo;</h2>',
   '<p>A belief does not have to be something we say to ourselves consciously.</p>',
   '<p>Someone may, for instance, long for a meaningful relationship and at the same time have '
   'connected intimacy, at a deeper level, with the possibility of rejection. They may want '
   'success, but have learned that exposure comes with criticism. They may want to set '
   'boundaries, but have linked &ldquo;no&rdquo; with guilt, or with the fear of losing other '
   "people's acceptance.</p>",
   '<p>An interesting contradiction can form:</p>',
   '<p class="cb-quote">&ldquo;I know what I want. So why do I keep doing something '
   'different?&rdquo;</p>',
   '<p>Exploring that distance — between the conscious &ldquo;I want&rdquo; and the deeper '
   'meanings we have given our experiences — is one of the most interesting points of the '
   'process.</p>',
   '<h2 class="cb-h2">Why is it called ThetaHealing®?</h2>',
   '<p>The name of the technique is connected to the theta brainwaves.</p>',
   '<p>Theta waves are a normal part of the electrical activity of the brain and are usually '
   'placed at roughly 4–8 Hz, depending on the scientific definition used. They have been studied '
   'in relation to functions such as memory and learning, and also in research on different forms '
   'of meditation and inward concentration.</p>',
   '<p>Some meditation studies have observed increased theta activity, while the research '
   'literature as a whole shows considerable heterogeneity depending on the type of meditation '
   "and each study's methodology.</p>",
   '<p>ThetaHealing® uses a guided meditative process which, according to the philosophy of the '
   'technique, is connected to the Theta state and supports deeper inward focus.</p>',
   '<p>No previous experience of meditation is required. The person is guided through the process '
   'and remains in full contact with what happens in the session.</p>',
   '<h2 class="cb-h2">What is Digging?</h2>',
   '<p>One of the characteristic tools of ThetaHealing® is Digging: the gradual exploration of a '
   'subject through targeted questions.</p>',
   '<p>Someone might arrive saying, for example:</p>',
   '<p class="cb-quote">&ldquo;I am afraid to start something new.&rdquo;</p>',
   '<p>The interest does not necessarily stop at the fear itself. Through the questions we look at '
   'what this change means for this particular person:</p>',
   '<p>What do they fear might happen? What would that mean for them? What is the hardest part of '
   'that possibility?</p>',
   '<p>Gradually a deeper belief, or a meaning that was not obvious at the start, may surface.</p>',
   '<p>The aim is not to &ldquo;find something wrong&rdquo;, but to gain greater awareness of what '
   'may lie behind a reaction or a repeating pattern.</p>',
   '<h2 class="cb-h2">What is muscle testing?</h2>',
   '<p>Within the technique, muscle testing may also be used as a tool for exploring beliefs.</p>',
   '<p>Muscle testing is a practice used in ThetaHealing® and in other complementary approaches. '
   'It is important, however, to distinguish it from scientifically validated psychological or '
   'medical diagnostic tools: it is not used to diagnose any mental or physical condition.</p>',
   '<h2 class="cb-h2">What can be explored in a session?</h2>',
   '<p>The content of a session is individual and depends on the subject the person themselves '
   'wishes to bring.</p>',
   '<p>It may concern:</p>',
   '<ul><li>repeating patterns in relationships</li><li>limiting beliefs</li><li>fears and '
   'insecurities</li><li>self-image and a sense of personal worth</li><li>difficulty setting '
   'boundaries</li><li>trust and connection with others</li><li>beliefs about love and '
   'relationships</li><li>work, success and abundance</li><li>personal goals and the changes one '
   'wants</li><li>deeper self-knowledge and personal or spiritual development</li></ul>',
   '<p>You do not need to know from the start &ldquo;which belief has to change&rdquo;. You can '
   'begin simply from something that troubles you, or from a point in your life where you feel '
   'stuck.</p>',
   '<h2 class="cb-h2">Can awareness become the beginning of change?</h2>',
   '<p>Much of what we do in our lives once acquired a meaning.</p>',
   '<p>A way of protecting ourselves, a belief or a behaviour may have formed in a different '
   'period of life and may go on repeating even after the circumstances have changed.</p>',
   '<p>Personal exploration gives us the chance to ask:</p>',
   '<p class="cb-quote">&ldquo;What I once needed — does it still serve me today?&rdquo;</p>',
   '<p>And perhaps that is one of the most interesting points of self-knowledge. Not to fight a '
   'part of ourselves, but to understand why it formed, what it tried to do for us, and whether '
   'today we can choose something different.</p>',
   '<h2 class="cb-h2">An invitation to look a little deeper</h2>',
   '<p>You do not have to be in crisis to want to know yourself better.</p>',
   '<p>Sometimes there is simply a question. A pattern that makes you wonder. A change you want '
   'but find hard to make. Or the sense that behind what you can see there is something more '
   'worth exploring.</p>',
   '<p>ThetaHealing® can be a complementary route to personal exploration and self-knowledge, '
   'particularly for people who wish to approach their inner world through an experiential and '
   'spiritual lens as well.</p>',
   '<p>Because very often change begins the moment what was working in the background starts to '
   'become visible.</p>',
   '<div class="cb-note cb-note--scope">ThetaHealing® is a technique of personal and spiritual '
   'development. It is not psychotherapy, nor psychological or medical treatment, and it is not '
   'used to diagnose or treat any mental or physical condition. It does not replace appropriate '
   'care from a health professional.</div>',
  ],
  sources=_s("thetahealing-epanalipsi-motivon")),

 dict(
  slug="en/articles/energy-and-the-human-body.html",
  el="arthra/energeia-kai-anthropino-soma.html",
  kicker="Energy therapies",
  title="Energy and the human body: what does modern science tell us about energy therapies?",
  marq="ENERGY",
  date="2026-09-06",
  teaser="Quantum biology, bioelectricity and the concept of the biofield. Where current research "
         "and energy practices meet — and where they do not.",
  body=[
   '<p>The idea of &ldquo;energy&rdquo; has appeared for centuries in different therapeutic and '
   'philosophical traditions. Today, though, we know that energy is not merely an abstract or '
   'spiritual notion. It is a fundamental element of the workings of life itself.</p>',
   '<p>The human body is an extraordinarily complex and dynamic system. At every moment countless '
   'biochemical, electrical and electromagnetic processes are taking place within it. Neurons '
   'communicate through electrochemical signals, the heart produces measurable electrical '
   'activity, and the brain shows different patterns of electrical activity that can be '
   'recorded.</p>',
   '<p>Modern science, therefore, no longer sees the human body simply as a collection of '
   'independent organs, but as a complex system of constant communication, interaction and '
   'regulation.</p>',
   '<h2 class="cb-h2">From matter to energy: what did quantum physics change?</h2>',
   '<p>Quantum physics radically changed the way we understand matter at the atomic and subatomic '
   'level.</p>',
   '<p>Matter is no longer described simply as a set of tiny, solid &ldquo;particles&rdquo;. '
   'Modern physics describes a world in which matter, energy, fields and the interactions between '
   'them are far more complex than the classical picture of reality allowed.</p>',
   '<p>Out of this development a particularly interesting scientific field has emerged: quantum '
   'biology.</p>',
   '<p>Quantum biology examines the role quantum phenomena may play within biological systems '
   'themselves. Phenomena such as quantum coherence, quantum tunnelling and spin-dependent '
   'processes are studied today in functions related, among others, to photosynthesis, enzymatic '
   'reactions and the magnetoreception of certain animals.</p>',
   '<p>The very existence of this field reminds us how complex life is, and how much we still have '
   'to understand about the way energy and information are organised and carried within living '
   'systems.</p>',
   '<h2 class="cb-h2">The human body as a dynamic system</h2>',
   '<p>One of the most significant shifts in the modern understanding of biology is that the body '
   'is not examined through its chemistry alone.</p>',
   '<p>Electrical activity is an inseparable part of how the human organism works. Cell membranes '
   'maintain electrical potentials, the nervous system relies on electrochemical communication, '
   'and the functioning of the heart and brain is accompanied by electrical and electromagnetic '
   'phenomena.</p>',
   '<p>At the same time, current research increasingly highlights the interaction between '
   'different levels of the organism: biological, neurological, psychological and '
   'environmental.</p>',
   '<p>A person, then, can be understood as a continually changing and self-regulating system, in '
   'which body, brain, environment and psychological state are in constant interaction.</p>',
   '<h2 class="cb-h2">What is the biofield?</h2>',
   '<p>It is precisely here that the concept of the biofield appears in the international '
   'literature.</p>',
   '<p>The term was created in the 1990s, in discussions organised by what was then the Office of '
   'Alternative Medicine at the American National Institutes of Health, as a broader term for '
   'studying therapeutic approaches that referred to energetic interactions of the human '
   'organism.</p>',
   '<p>In the relevant research literature, the biofield has been proposed as a wider model for '
   'understanding the flow of energy and information associated with living systems.</p>',
   '<p>There is in fact now a distinct research literature on biofield therapies, which includes '
   'practices such as Reiki, Therapeutic Touch, Healing Touch and External Qigong. These practices '
   'have been the subject of clinical studies in areas such as stress, anxiety, pain and '
   'subjective wellbeing.</p>',
   '<p>That research is not complete; it is, however, an interesting meeting point between '
   'practices with a long history and the modern attempt to investigate them with scientific '
   'methods.</p>',
   '<h2 class="cb-h2">And where do the aura and the energy body come in?</h2>',
   '<p>Long before the modern term biofield was created, different cultures described the human '
   'being as something more than the visible physical body.</p>',
   '<p>We find concepts such as qi in the Chinese tradition, prana in Indian philosophical '
   'traditions and, in various esoteric systems, terms such as the energy or etheric body and the '
   'aura.</p>',
   '<p>Despite the significant differences between these traditions, there is a common core: the '
   'idea that life is connected to a form of vital energy, and that the balance of that energy is '
   "related to a person's overall condition.</p>",
   '<p>The modern concept of the biofield is not scientifically identical to the traditional idea '
   'of the aura or the etheric body. Even so, it is interesting that both the older energy '
   'traditions and certain modern research approaches attempt — in entirely different language '
   'and methodology — to look at the human being beyond a purely mechanistic model.</p>',
   '<h2 class="cb-h2">Where do science and energy therapies meet?</h2>',
   '<p>Here, perhaps, is the most interesting point.</p>',
   '<p>Modern physics has shown us that matter and energy at a fundamental level have a far more '
   'complex relationship than we once took for granted.</p>',
   '<p>Biophysics and neuroscience study the electrical and electromagnetic processes of the human '
   'organism.</p>',
   '<p>Quantum biology examines genuine quantum phenomena within living systems.</p>',
   '<p>And biofield research attempts to investigate whether there are still broader mechanisms of '
   'energetic and informational interaction that could contribute to our understanding of how '
   'living organisms work.</p>',
   '<p>Energy therapies approach this question from a different direction. They see the person '
   'holistically and work from the idea that physical, psychological and energetic states are '
   'different dimensions of one system.</p>',
   '<p>For someone interested in exploring this approach, energy practices can be a different kind '
   'of space for relaxation, personal exploration, self-observation and care for their wellbeing, '
   'alongside the conventional forms of care they may need.</p>',
   '<h2 class="cb-h2">A conversation that continues</h2>',
   '<p>Perhaps the most fascinating element is not the need to choose between science and a more '
   'holistic understanding of the person.</p>',
   '<p>It lies in the way knowledge evolves.</p>',
   '<p>A few decades ago, the idea that quantum phenomena might have a functional role inside warm '
   'and complex biological systems was met with considerable scepticism. Today quantum biology is '
   'a real research field, with studies on photosynthesis, enzymatic processes, magnetoreception '
   'and other biological mechanisms.</p>',
   '<p>In the same way, biofield therapies are the subject of published research and clinical '
   'trials, and specific guidelines have even been developed for reporting their clinical studies '
   'more systematically.</p>',
   '<p>This does not mean that quantum physics has &ldquo;proved&rdquo; the aura or the mechanism '
   'of energy therapies. It does mean that the scientific investigation of life, energy and '
   'information is far more open and multidimensional than we often imagine.</p>',
   '<p>And perhaps that is where the real bridge lies: in being able to stay open to exploration, '
   'without confusing what we already know with what we are still trying to understand.</p>',
   '<div class="cb-note cb-note--scope"><strong>An important clarification.</strong> Energy '
   'practices are not a substitute for medical, psychological or psychiatric care. The concepts of '
   'the aura, the etheric body and a therapeutic &ldquo;subtle&rdquo; energy field have not to '
   'date been confirmed as established biological mechanisms of modern science. Choosing an energy '
   'practice is not a reason to stop or alter any treatment or medication recommended by a '
   'qualified health professional.</div>',
  ],
  sources=_s("energeia-kai-anthropino-soma")),

 dict(
  slug="en/articles/dowsing-beyond-the-person.html",
  el="arthra/radiaisthisia-pera-apo-ton-anthropo.html",
  kicker="Dowsing",
  title="Beyond the person: the different applications of Dowsing",
  marq="APPLICATIONS",
  date="2026-09-06",
  teaser="Dowsing is not only the pendulum. A far wider field of practice, from personal "
         "exploration to spaces and animals.",
  body=[
   '<p>When we hear the word &ldquo;Dowsing&rdquo;, the first thing that usually comes to mind is '
   'the pendulum. In fact, though, dowsing describes a much wider field of practices, based on the '
   'idea that people, animals and spaces have an energy field that can be explored through '
   'specialised dowsing tools.</p>',
   '<p>In Therapeutic Dowsing, the interest turns first of all to the person.</p>',
   '<h2 class="cb-h2">When the question is not only &ldquo;what is happening to me?&rdquo;</h2>',
   '<p>There are times when what we are looking for is not necessarily one more explanation, but a '
   'different way of turning towards ourselves.</p>',
   '<p>For someone interested in energy approaches, dowsing can be an additional field of personal '
   'exploration, self-observation and connection with their inner state.</p>',
   '<p>The approach does not begin from a psychological diagnosis, nor does it attempt to replace '
   'psychotherapy. It approaches the same request through a different language: that of the energy '
   'field, of vibrations and frequencies.</p>',
   '<p>And perhaps that is what makes it interesting for people who want to explore themselves '
   'through a different lens as well.</p>',
   '<h2 class="cb-h2">From personal exploration to energetic balance</h2>',
   '<p>In modern Therapeutic Dowsing we find applications focused on energetic release, a sense of '
   'balance, relaxation and personal or spiritual development.</p>',
   '<p>Depending on the school and the system used, the practice may include work with different '
   'qualities of vibration, with frequencies and with colour vibrations.</p>',
   '<p>The interest here lies less in adding one more &ldquo;label&rdquo; to what someone is '
   'experiencing, and more in creating a different space for observation and personal '
   'exploration.</p>',
   '<h2 class="cb-h2">And beyond the person?</h2>',
   '<p>Here is one of the less well-known sides of dowsing.</p>',
   '<p>Historically, and across different schools, its applications are not limited to people. '
   'Dowsing practice has been used to explore environments and spaces, while modern systems of '
   'energetic dowsing describe applications with animals and living spaces as well.</p>',
   '<p>So we find practices of energetic exploration of a home or a workplace, of observing how an '
   'environment is experienced energetically, and also applications concerning the energy field of '
   'animals.</p>',
   '<p>This shows the breadth of dowsing itself: more than one specific technique, it is a body of '
   'different traditions and tools that use the notion of energetic information as their main '
   'point of reference.</p>',
   '<h2 class="cb-h2">A different route towards oneself</h2>',
   '<p>Not everyone needs to choose an energy approach — nor does every difficulty need to be '
   'interpreted energetically.</p>',
   '<p>For someone with an interest or an inclination towards such practices, though, Therapeutic '
   'Dowsing can be one more way of exploring themselves.</p>',
   '<p>Not in place of psychological or medical care, but as a different experience of contact '
   'with oneself, with one&rsquo;s inner state and with the way one experiences balance.</p>',
   '<p>Perhaps, in the end, the most interesting question is not only &ldquo;what can dowsing '
   'do?&rdquo;, but:</p>',
   '<p class="cb-quote">&ldquo;What might someone notice about themselves when they choose to '
   'approach themselves from a different perspective too?&rdquo;</p>',
   '<div class="cb-note cb-note--scope"><strong>An important clarification.</strong> Therapeutic '
   'Dowsing is an energy practice of personal exploration and wellbeing. The concepts of the '
   'energy field and of dowsing frequencies belong to the theoretical framework of this method and '
   'are not established biomedical mechanisms. The practice is not a method of medical or '
   'psychological diagnosis or treatment and does not replace the corresponding professional '
   'care.</div>',
  ],
  sources=_s("radiaisthisia-pera-apo-ton-anthropo")),

 dict(
  slug="en/articles/when-play-speaks.html",
  el="arthra/otan-to-paixnidi-mila.html",
  kicker="Play Therapy",
  title="When play speaks: symbolism in Play Therapy",
  marq="SYMBOL",
  date="2026-09-06",
  teaser="A small animal always left alone. A house knocked down again and again. Why a child does "
         "not need words to show what is happening inside them.",
  body=[
   '<p>Children do not always need words to show us what is happening inside them.</p>',
   '<p>A small animal that is always left alone. A hero who must always save the others. Two '
   'figures who clash again and again. A house that is destroyed and rebuilt.</p>',
   '<p>Within play, fears, wishes, relationships and inner conflicts can appear that the child '
   'cannot yet describe directly.</p>',
   '<h2 class="cb-h2">Play as a symbolic language</h2>',
   '<p>Melanie Klein was one of the most important figures in establishing play as a way into the '
   "child's inner world.</p>",
   '<p>Through figures, objects, characters and stories, a child can carry elements of their '
   'experience into a symbolic scene. Something difficult no longer has to be said directly: it '
   'can first be represented.</p>',
   '<p>The French psychoanalytic tradition developed this notion of symbolisation in particular. '
   "Play can allow a child's anxiety, relationships and inner experiences to take a form that can "
   'gradually be observed and worked through.</p>',
   '<h2 class="cb-h2">There is no &ldquo;dictionary of symbols&rdquo;</h2>',
   '<p>Symbolic observation, however, does not mean that every object has one fixed psychological '
   'interpretation.</p>',
   '<p>A lion does not always mean anger.</p>',
   '<p>A house does not always mean family.</p>',
   '<p>The colour black does not automatically mean sadness.</p>',
   '<p>The same symbol can mean something entirely different for two different children.</p>',
   '<p>What is interesting is the personal meaning it takes on within the story of this particular '
   'child: how it is used, what role it is given, what comes before, what comes after, what '
   'feeling accompanies it and whether it returns within the play.</p>',
   '<h2 class="cb-h2">Sometimes it is easier to play it</h2>',
   '<p>Imagine a child who finds it hard to say:</p>',
   '<p class="cb-quote">&ldquo;I am afraid my mum will leave.&rdquo;</p>',
   '<p>They may, though, be able to create a story in which a small animal loses its mother and '
   'tries to find her.</p>',
   '<p>The experience is there, but it has gained a safer distance.</p>',
   '<p>Within symbolic play a child can approach something difficult at their own pace, without '
   'having to explain it before they are ready to.</p>',
   '<p>This is one of the most important features of the symbolic function of play: it creates a '
   'space between inner experience and immediate reality.</p>',
   '<p>It does not mean that every game hides a deeper message, nor that every move a child makes '
   'needs interpreting.</p>',
   '<p>It means that when a child feels safe enough to play, a different route of communication '
   'can open.</p>',
   '<p>Because sometimes, before a child can say what they feel, they first need to be able to '
   'play it.</p>',
  ],
  sources=_s("otan-to-paixnidi-mila")),

 dict(
  slug="en/articles/drawing-and-creative-techniques.html",
  el="arthra/sxedio-kai-dimiourgikes-technikes.html",
  kicker="Play Therapy",
  title="When words are not enough: drawing and creative techniques in Play Therapy",
  marq="DRAWING",
  date="2026-09-06",
  teaser="A sheet of paper, a few colours, a little clay. How children's drawing works "
         "therapeutically — and why it is not &ldquo;read&rdquo; like a test.",
  body=[
   '<p>A blank sheet of paper, a few colours, a little clay or one simple line can sometimes open '
   'a route of communication that words have not yet managed to find.</p>',
   '<p>Creative techniques hold a particular place in therapeutic work with children precisely '
   'because they do not ask the child to explain straight away what they are feeling.</p>',
   '<p>They let the child create first.</p>',
   '<h2 class="cb-h2">Drawing as a way of expressing</h2>',
   "<p>Children's drawing has a long history in psychotherapeutic work.</p>",
   '<p>Through a drawing, characters, relationships, imaginary worlds, fears or wishes can appear. '
   'That does not mean, however, that the therapist &ldquo;reads&rdquo; the picture like a '
   'psychological test, or automatically assigns fixed interpretations to colours and shapes.</p>',
   '<p>What matters more is the child themselves:</p>',
   '<p>What did they draw?</p>',
   '<p>What story do they give the picture?</p>',
   '<p>What happens to the characters?</p>',
   '<p>What do they choose to change?</p>',
   '<p>What do they want to add or rub out?</p>',
   '<p>The drawing can in this way become the starting point of a story and of a conversation.</p>',
   '<h2 class="cb-h2">From a &ldquo;scribble&rdquo; to a story</h2>',
   '<p>One of the most characteristic examples of creative communication with children comes from '
   'Donald Winnicott and the well-known Squiggle Game.</p>',
   '<p>The idea was extremely simple.</p>',
   '<p>The therapist or the child would draw a spontaneous line — a &ldquo;squiggle&rdquo; — and '
   'the other would turn it into something recognisable. The roles could then be reversed.</p>',
   '<p>A random line could become a face.</p>',
   '<p>An animal.</p>',
   '<p>A monster.</p>',
   '<p>A house.</p>',
   '<p>A whole story.</p>',
   "<p>What mattered was not the child's artistic ability. It was the meeting and the making that "
   'happened through the process.</p>',
   '<p>French psychoanalytic writing has also highlighted the Squiggle as a characteristic example '
   'of how drawing can work as a therapeutic mediation and open a dialogue with the child.</p>',
   '<h2 class="cb-h2">You do not need to be &ldquo;good at drawing&rdquo;</h2>',
   '<p>Creative techniques have no aesthetic aim.</p>',
   '<p>The result is not judged as beautiful or ugly.</p>',
   '<p>A child can draw, use clay, build something, make characters, or turn something abstract '
   'into a personal story.</p>',
   '<p>And that has a particular value: something that until then was only a feeling can take '
   'form.</p>',
   '<p>When something takes form, it can be observed.</p>',
   '<p>It can change.</p>',
   '<p>It can be transformed.</p>',
   '<p>It can be given a different story.</p>',
   '<p>Current literature on creative and art-based therapeutic interventions with children '
   'continues to investigate their usefulness across different populations and mental health '
   'settings.</p>',
   '<p>The most important thing, though, remains perhaps extremely simple:</p>',
   '<p>not every child needs to find the right words first. Sometimes they can first find a '
   'colour, an image or a story — and the words can follow later.</p>',
  ],
  sources=_s("sxedio-kai-dimiourgikes-technikes")),

 dict(
  slug="en/articles/roles-stories-and-imaginary-worlds.html",
  el="arthra/roloi-istories-fantastikoi-kosmoi.html",
  kicker="Play Therapy",
  title="&ldquo;Let&rsquo;s pretend that…&rdquo;: roles, stories and imaginary worlds in Play Therapy",
  marq="ROLES",
  date="2026-09-06",
  teaser="When a child becomes the director of their own scene: why changing roles matters so "
         "much, and how play leads to psychodrama.",
  body=[
   '<p class="cb-quote">&ldquo;You be the teacher and I&rsquo;ll be the child.&rdquo;</p>',
   '<p class="cb-quote">&ldquo;This one is the bad guy.&rdquo;</p>',
   '<p class="cb-quote">&ldquo;The doll is scared and hides here.&rdquo;</p>',
   '<p>In a few minutes a child can create a whole world.</p>',
   '<p>In symbolic play roles change, characters take on personalities, and things that seem '
   'impossible in real life can suddenly happen.</p>',
   '<p>And this possibility of &ldquo;let&rsquo;s pretend that…&rdquo; is of particular '
   'psychological interest.</p>',
   '<h2 class="cb-h2">When the child becomes the director</h2>',
   '<p>Within play the child can decide who is strong and who is weak, who leaves and who returns, '
   'who protects, who is afraid and — above all — how the story ends.</p>',
   '<p>As early as 1929 Melanie Klein described personification in child play: the tendency of '
   'children to create characters and give them different roles, qualities and feelings.</p>',
   '<p>One character can become angry.</p>',
   '<p>Another frightened.</p>',
   '<p>Another all-powerful.</p>',
   '<p>In this way a child can &ldquo;distribute&rdquo; different sides of a story across '
   'different figures and observe them within the safety of play.</p>',
   '<h2 class="cb-h2">Why does changing roles matter?</h2>',
   '<p>In real life a child does not always have control over what happens.</p>',
   '<p>In play, though, they can become the author of the story.</p>',
   '<p>They can play the strong one while feeling weak.</p>',
   '<p>They can become the parent.</p>',
   '<p>They can make the monster small.</p>',
   '<p>They can save a character who previously could not be saved.</p>',
   '<p>That does not mean every such scenario is a direct representation of a real event.</p>',
   '<p>Play is a far more complex mixture of real experiences, imagination, fears, wishes and '
   'creativity.</p>',
   '<p>That is precisely why a therapist does not look for a quick &ldquo;translation&rdquo; of '
   'the play. They observe how the story develops and accompany the child inside it.</p>',
   '<h2 class="cb-h2">From individual play to psychodrama</h2>',
   '<p>The power of roles took on particular significance in the French psychoanalytic tradition '
   'as well.</p>',
   '<p>After the Second World War, figures such as René Diatkine, Serge Lebovici and Évelyne and '
   'Jean Kestemberg contributed to the development of analytic psychodrama in France.</p>',
   '<p>Here the story is not represented only with toys or figures.</p>',
   '<p>It can be acted.</p>',
   '<p>The person proposes a scene and different people take on the roles of the characters. A '
   'space is created in which feelings, relationships and conflicts can take form through '
   'action.</p>',
   '<p>The French tradition describes this process through the idea of &ldquo;faire semblant pour '
   'de vrai&rdquo; — pretending within the play, while the feelings that surface can be entirely '
   'real.</p>',
   '<h2 class="cb-h2">A story can be given a different ending</h2>',
   '<p>This is perhaps one of the most interesting features of symbolic play.</p>',
   '<p>The story is not fixed.</p>',
   '<p>It can be played again.</p>',
   '<p>A character can react differently.</p>',
   '<p>An ending can change.</p>',
   '<p>A figure who was alone may this time find someone.</p>',
   '<p>The child does not change the real event. What they gain is a space in which they can '
   'experiment with different positions, feelings and possibilities.</p>',
   '<p>And so a seemingly simple:</p>',
   '<p class="cb-quote">&ldquo;Let&rsquo;s pretend that…&rdquo;</p>',
   '<p>can open a whole world of psychological processing and creativity.</p>',
  ],
  sources=_s("roloi-istories-fantastikoi-kosmoi")),

 dict(
  slug="en/articles/why-children-replay-the-same-story.html",
  el="arthra/giati-to-paidi-paizei-xana-kai-xana.html",
  kicker="Play Therapy",
  title="Why does a child play the same story again and again?",
  marq="REPETITION",
  date="2026-09-06",
  teaser="The same animal gets lost, the same &ldquo;bad guy&rdquo; comes back. What repetition "
         "means in children's play — from Freud's fort-da to today.",
  body=[
   '<p>The same little animal gets lost. The same &ldquo;bad guy&rdquo; comes back. A family is in '
   'danger again and again. A battle is repeated in almost exactly the same way.</p>',
   '<p>To a parent, a repeating game can look strange or even worrying. In fact, though, '
   "repetition is a particularly interesting element of children's play.</p>",
   '<p>It does not necessarily mean that something difficult or traumatic has happened. Children '
   'repeat games because they enjoy them, because they are practising skills, or because '
   'predictability offers them safety.</p>',
   '<p>There are times, though, when repetition seems to take on a different psychological '
   'function.</p>',
   '<h2 class="cb-h2">From &ldquo;it&rsquo;s gone&rdquo; to &ldquo;it came back&rdquo;</h2>',
   '<p>One of the best-known observations in the history of psychoanalysis is the fort-da game '
   'described by Sigmund Freud.</p>',
   '<p>Watching a small child repeatedly throw a reel away so that it disappeared and then pull it '
   'back so that it returned, Freud connected the game with the experience of absence and '
   'return.</p>',
   '<p>The idea behind that observation remains particularly interesting: within play, a child can '
   'turn something that happens to them into something they can themselves represent.</p>',
   '<p>In real life they do not always decide who leaves or when they come back.</p>',
   '<p>In play, though, they hold the thread.</p>',
   '<h2 class="cb-h2">What can repetition mean?</h2>',
   '<p>Sometimes a child returns to the same story because through it they are trying to organise '
   'an experience, to approach a feeling, to gain a greater sense of control, or to try out '
   'different versions of a situation.</p>',
   '<p>This matters particularly in childhood, when complex experiences cannot always be described '
   'easily in words.</p>',
   '<p>The literature on play after difficult or traumatic experiences shows that repeating themes '
   'can indeed appear. That does not mean, however, that every repeating game is a sign of '
   'trauma.</p>',
   '<p>So we look not only at what a child plays, but at the way they play it, the feeling that '
   'accompanies the story, the flexibility of the play and the overall context in which it '
   'appears.</p>',
   '<h2 class="cb-h2">When the same story begins to change</h2>',
   '<p>Perhaps the most interesting element is not always the repetition itself, but the small '
   'changes that begin to appear within it.</p>',
   '<p>A character who was previously helpless finds an ally.</p>',
   '<p>A little animal that used to get lost every time manages to come back.</p>',
   '<p>A hero discovers a different solution.</p>',
   '<p>A story is given a new ending for the first time.</p>',
   '<p>The child does not change what has already happened in reality. Within the safe frame of '
   'play, though, they can experiment with different roles, feelings and possible outcomes.</p>',
   '<p>That is why, in therapeutic observation, what matters is not only:</p>',
   '<p class="cb-quote">&ldquo;Why is the child playing the same story again?&rdquo;</p>',
   '<p>but also:</p>',
   '<p class="cb-quote">&ldquo;What stays the same — and what is slowly beginning to '
   'change?&rdquo;</p>',
   '<p>Because sometimes a child needs to tell the same story many times before they can imagine a '
   'different ending.</p>',
  ],
  sources=_s("giati-to-paidi-paizei-xana-kai-xana")),

 dict(
  slug="en/articles/september-and-the-whole-family.html",
  el="arthra/septemvrios-epistrofi-oikogeneias.html",
  kicker="Parent counselling",
  title="September again: when it is not only the child who goes back to school, but the whole family",
  marq="SEPTEMBER",
  date="2026-09-06",
  teaser="Alarm clocks, school bags, timetables — and a whole family trying to find its rhythm "
         "again. Whose anxiety is it, in the end?",
  body=[
   '<p>And suddenly it is September again.</p>',
   '<p>Alarm clocks, school bags, activities, homework, timetables — and with them the familiar '
   'effort of a whole family to find its rhythm again.</p>',
   '<p>For a child, though, going back to school is not simply a change of schedule. It can mean a '
   'new teacher, a different class, demands, friendships, separation from a parent, or a return to '
   'something that was hard for them last year.</p>',
   '<h2 class="cb-h2">And for the parent?</h2>',
   '<p>Often it means an anxiety of their own, beginning at almost the same moment:</p>',
   '<p class="cb-quote">&ldquo;Will they settle in? Will they manage? Will they do their homework? '
   'Will they make friends? What if the same difficulties come back this year?&rdquo;</p>',
   '<h2 class="cb-h2">Whose anxiety is it, in the end?</h2>',
   "<p>A parent's anxiety for their child is natural. The challenge lies in being able to tell "
   "when we are seeing a real difficulty of the child's, and when — without realising it — we are "
   'starting to see the situation through our own fears.</p>',
   '<p>A child may simply need a little time to adjust.</p>',
   '<p>They may come home more tired.</p>',
   '<p>They may be more irritable.</p>',
   '<p>They may need more closeness with a parent in the first few days.</p>',
   '<p>Not every change in behaviour needs to be turned immediately into a problem that must be '
   '&ldquo;fixed&rdquo;.</p>',
   '<p>Sometimes what a child needs most is an adult who can stay steady beside them.</p>',
   '<h2 class="cb-h2">Routine does not mean a military schedule</h2>',
   '<p>Returning to a predictable daily rhythm can help children a great deal in adjusting to the '
   'new school period.</p>',
   '<p>Regular sleep times, time for food and rest, a reasonably predictable day and clear '
   'boundaries create a frame within which a child roughly knows what to expect.</p>',
   '<p>That does not mean everything has to work perfectly from the first week.</p>',
   '<p>Adjustment takes time.</p>',
   '<p>And sometimes the parent needs time too.</p>',
   '<h2 class="cb-h2">When &ldquo;will they manage?&rdquo; becomes &ldquo;how can I help '
   'them?&rdquo;</h2>',
   '<p>Here the whole perspective shifts.</p>',
   "<p>Instead of constantly trying to eliminate the child's difficulty, we can ask ourselves:</p>",
   '<p>What do they need from me right now?</p>',
   '<p>More stability?</p>',
   '<p>A clearer boundary?</p>',
   '<p>More space?</p>',
   '<p>To be listened to without being given an immediate solution?</p>',
   '<p>To change something in the way I react?</p>',
   '<p>These are exactly the questions that can be worked on in Parent Counselling.</p>',
   '<p>Not because someone &ldquo;does not know how to be a parent&rdquo;.</p>',
   '<p>But because parenting is a role that keeps changing along with the child.</p>',
   '<p>Every new age brings different needs. Every school year can bring new challenges. And '
   'sometimes a different perspective is enough to change the way a whole family lives through a '
   'difficult period.</p>',
   '<p>Because the aim is not a parent who always has the right answer. It is a parent who can '
   'observe, adapt and stay available in the relationship with their child.</p>',
  ],
  sources=_s("septemvrios-epistrofi-oikogeneias")),

 dict(
  slug="en/articles/parent-counselling-without-a-problem.html",
  el="arthra/symvouleftiki-goneon-xreiazetai-provlima.html",
  kicker="Parent counselling",
  title="Does my child need to have a &ldquo;problem&rdquo; before I ask for Parent Counselling?",
  marq="PARENTS",
  date="2026-09-06",
  teaser="&ldquo;Am I overreacting?&rdquo; &ldquo;Is it serious enough?&rdquo; Why parent "
         "counselling does not require a diagnosis — and what it actually offers.",
  body=[
   '<p class="cb-quote">&ldquo;Am I overreacting?&rdquo;</p>',
   '<p class="cb-quote">&ldquo;Is it serious enough to see a psychologist?&rdquo;</p>',
   '<p class="cb-quote">&ldquo;My child does not have a diagnosis, so why would I need Parent '
   'Counselling?&rdquo;</p>',
   '<p>The answer is simple: there does not have to be a &ldquo;problem&rdquo; for a parent to ask '
   'for support.</p>',
   '<p>Parenting is a role that keeps evolving. Along with the child, the needs, the challenges '
   'and the boundaries change — and often the way we stand in front of them has to change '
   'too.</p>',
   '<h2 class="cb-h2">When the question is not &ldquo;what is wrong with the child?&rdquo;</h2>',
   '<p>A child may struggle to follow boundaries, have intense outbursts, be fearful, withdraw, or '
   'find school or friendships difficult.</p>',
   '<p>At other times, though, the child may show no particular difficulty and it is the parent '
   'who feels that something in the relationship between them is troubling.</p>',
   '<p class="cb-quote">&ldquo;Why do we end up shouting every time?&rdquo;</p>',
   '<p class="cb-quote">&ldquo;When should I hold firm and when should I give way?&rdquo;</p>',
   '<p class="cb-quote">&ldquo;How do I set a boundary without feeling I am moving away from my '
   'child?&rdquo;</p>',
   '<p class="cb-quote">&ldquo;Am I reacting more strongly than I would like?&rdquo;</p>',
   '<p>And these are important questions.</p>',
   '<h2 class="cb-h2">Counselling does not mean &ldquo;tell me what to do&rdquo;</h2>',
   '<p>Parent Counselling is not a manual of instructions for the &ldquo;right parent&rdquo;.</p>',
   '<p>It is a space in which we can better understand what lies behind a behaviour, what a child '
   'needs at their particular developmental stage, and also what happens to the parent themselves '
   'when they are facing a difficult situation.</p>',
   "<p>Because often it is not simply a child's behaviour that needs to change.</p>",
   '<p>What needs to change is the way we understand it and respond to it.</p>',
   '<p>Current literature on parenting interventions places particular emphasis on the '
   'parent–child relationship, on positive communication, on managing boundaries and behaviour, '
   "and also on the parent's own skills, such as emotion regulation, communication and problem "
   'solving.</p>',
   '<h2 class="cb-h2">The parental role can evolve</h2>',
   '<p>A parent asking for help does not mean they have failed to manage their child.</p>',
   '<p>It may simply mean they are choosing to stand back for a moment from their parental role '
   'and ask:</p>',
   '<p>What is working? What no longer works? What can I understand differently? And what can I '
   'change within our relationship?</p>',
   '<p>So we do not have to wait for a situation to become &ldquo;serious enough&rdquo;.</p>',
   '<p>Sometimes Parent Counselling begins simply from a question.</p>',
   '<p>And one question can be enough to open a different way of communicating with our child.</p>',
  ],
  sources=_s("symvouleftiki-goneon-xreiazetai-provlima")),

 dict(
  slug="en/articles/invisible-challenges-of-modern-parents.html",
  el="arthra/aorates-prokliseis-tou-sygxronou-gonea.html",
  kicker="Parent counselling",
  title="&ldquo;I am trying to keep up with everything&rdquo;: the invisible challenges of the modern parent",
  marq="PARENTING",
  date="2026-09-06",
  teaser="Be available, set boundaries, do not shout — and keep up with everything at the same "
         "time. On parental exhaustion and the guilt that comes with it.",
  body=[
   '<p>Be available. Set boundaries. Do not shout. Listen. Understand. Spend quality time with '
   'your child. Look after your relationship.</p>',
   '<h2 class="cb-h2">And at the same time?</h2>',
   '<p>Work, pay the bills, run the house, the school, the activities, the appointments, the '
   'obligations — and somewhere in among all of it, try not to lose yourself as well.</p>',
   '<p>Being a parent today is not an easy role.</p>',
   '<h2 class="cb-h2">Behind a tired parent there is often someone who is trying very hard</h2>',
   '<p>There are days when patience runs out earlier.</p>',
   '<p>When a behaviour you could have handled calmly under other circumstances finds you already '
   'exhausted.</p>',
   '<p>And then the guilt can arrive.</p>',
   '<p class="cb-quote">&ldquo;I shouldn&rsquo;t have shouted.&rdquo; &ldquo;I could have handled '
   'that better.&rdquo; &ldquo;Am I not giving them enough?&rdquo;</p>',
   '<p>Parental fatigue and parental stress are not a sign that someone does not love their child '
   'enough. Current research recognises that parenting can carry a significant psychological load, '
   'particularly when demands accumulate and the available resources — time, energy, financial '
   'security, practical help and social support — are limited.</p>',
   '<h2 class="cb-h2">A parent does not exist outside their own life</h2>',
   '<p>Sometimes we talk about parenting as though a parent had unlimited patience and emotional '
   'availability.</p>',
   '<p>They do not.</p>',
   '<p>They are a person who may have slept little, spent eight hours at work, be worried about '
   'money, be facing difficulties in their relationship, or simply not have had a single moment '
   'alone all day.</p>',
   '<p>And yet, in the evening, they are called on again to be the adult who will hold the '
   'tension, set the boundary and help a child regulate a feeling that they themselves may be '
   'struggling to regulate at that very moment.</p>',
   '<p>That is demanding.</p>',
   '<h2 class="cb-h2">There is no need for a &ldquo;perfect&rdquo; parent</h2>',
   '<p>Perhaps one of the greatest pressures of modern parenting is precisely the idea that there '
   'is one right way to do everything.</p>',
   '<p>But the parent–child relationship is not built through perfection.</p>',
   '<p>It is built also through the moments when something did not go as we would have wanted, but '
   'we can come back to it. Acknowledge what happened. Talk again. Try a different way.</p>',
   '<p>And this applies to the parent themselves.</p>',
   '<p>Being able to notice when they are running out, what triggers them, what expectations they '
   'hold of themselves, and when they too need support.</p>',
   '<h2 class="cb-h2">Who looks after the one who does the looking after?</h2>',
   '<p>Parent Counselling does not have to begin because &ldquo;something is wrong&rdquo; with a '
   'child.</p>',
   '<p>It can begin because a parent feels tired, confused, or caught in ways of reacting that no '
   'longer represent them.</p>',
   '<p>It can be a space for understanding better not only their child, but themselves within '
   'their parental role.</p>',
   '<p>Because the question is not always:</p>',
   '<p class="cb-quote">&ldquo;How can I become a better parent?&rdquo;</p>',
   '<p>Sometimes a more useful question is:</p>',
   '<p class="cb-quote">&ldquo;What do I need too, so that I can be the parent I want to '
   'be?&rdquo;</p>',
   '<p>And perhaps a different relationship begins there — not only with the child, but with '
   'ourselves.</p>',
  ],
  sources=_s("aorates-prokliseis-tou-sygxronou-gonea")),

 dict(
  slug="en/articles/parents-children-and-screens.html",
  el="arthra/goneis-kai-paidia-stin-epochi-tis-othonis.html",
  kicker="Parent counselling",
  title="&ldquo;Put the tablet down&rdquo;: parents and children in the age of the screen",
  marq="SCREENS",
  date="2026-09-06",
  teaser="Not all screens are the same, and the aim is not a war. How a boundary that actually "
         "holds is built — and what role the parent's own phone plays.",
  body=[
   '<p class="cb-quote">&ldquo;Turn the tablet off.&rdquo;</p>',
   '<p class="cb-quote">&ldquo;In five minutes.&rdquo;</p>',
   '<p class="cb-quote">&ldquo;I told you to turn it off.&rdquo;</p>',
   '<p>And just like that, an ordinary moment of the day can turn into a negotiation, a tension or '
   'a conflict.</p>',
   "<p>Technology has become an inseparable part of children's lives — and of adults' lives too. "
   'It is used for entertainment, communication, schoolwork, play and social contact. That is why '
   'the question today is not simply &ldquo;how long is a child allowed in front of a '
   'screen?&rdquo;.</p>',
   '<p>We also need to ask: what are they watching, when are they watching it, why are they using '
   'it, and what else is starting to lose its place in their day?</p>',
   '<h2 class="cb-h2">Not all screens are the same</h2>',
   '<p>An hour of video calling with a relative, a creative game, a piece of schoolwork and an '
   'hour of non-stop scrolling are not the same experience.</p>',
   '<p>The more recent guidance from the American Academy of Pediatrics now places particular '
   'emphasis not only on duration, but on the quality of the content and on whether the use of '
   'technology is beginning to displace basic needs: sleep, movement, play, reading, schoolwork '
   'and real contact with the family.</p>',
   '<p>The aim, then, is not a home without technology.</p>',
   '<p>It is a home in which technology has a place — without taking over all the others.</p>',
   '<h2 class="cb-h2">Why does a &ldquo;war&rdquo; start when the tablet goes off?</h2>',
   '<p>If a child has become used to using a device freely, a sudden &ldquo;from tomorrow, only '
   'half an hour&rdquo; is likely to provoke a reaction.</p>',
   '<p>A boundary is understood more easily when it is clear, predictable and consistent.</p>',
   '<p>When do we use screens? When do we put them away? What content is allowed? What happens on '
   'weekdays and what at the weekend?</p>',
   '<p>The AAP in fact suggests creating a Family Media Plan: a family framework for using '
   'technology that concerns not only the child but the whole household.</p>',
   "<h2 class=\"cb-h2\">And the parent's phone?</h2>",
   '<p>Here, perhaps, is the hardest part.</p>',
   '<p>It is difficult to ask a child to put the tablet down at mealtimes while we are constantly '
   'checking our own phone.</p>',
   '<p>Research has now turned its attention to what is called technoference: the moments when '
   'technology interrupts parent–child interaction. Current recommendations on this concern the '
   "digital habits of the whole family, not only the children's.</p>",
   '<p>A child does not learn only from the boundary we set them.</p>',
   '<p>They learn from the example they see.</p>',
   '<h2 class="cb-h2">From control to gradual self-regulation</h2>',
   '<p>The final aim cannot be a parent standing over their child forever with a stopwatch.</p>',
   '<p>As a child grows, they gradually need to learn to recognise for themselves when technology '
   'is starting to interfere with their sleep, their concentration, their responsibilities or '
   'their relationships. In adolescence, the APA suggests monitoring and conversation adapted to '
   'age, with gradually greater autonomy as the necessary digital skills develop.</p>',
   '<p>And when every attempt at setting boundaries ends in a daily battle, Parent Counselling can '
   'help not simply with &ldquo;how many hours do I allow&rdquo;, but with how to build boundaries '
   'that this particular family can actually apply consistently.</p>',
   '<p>Because perhaps the most useful question is not:</p>',
   '<p class="cb-quote">&ldquo;How do I get my child to put the screen down?&rdquo;</p>',
   '<p>but:</p>',
   '<p class="cb-quote">&ldquo;How can we, as a family, learn to use technology without letting '
   'technology organise our lives?&rdquo;</p>',
  ],
  sources=_s("goneis-kai-paidia-stin-epochi-tis-othonis")),

 dict(
  slug="en/articles/from-holidays-back-to-school.html",
  el="arthra/apo-tis-diakopes-sto-scholeio.html",
  kicker="Parent counselling",
  title="From the holidays back to school: how do we find a rhythm again without turning the house into a barracks?",
  marq="RHYTHM",
  date="2026-09-06",
  teaser="Six practical steps for the move from summer to the school year, without the house "
         "becoming a negotiating table.",
  body=[
   '<p>Summer has its own rules.</p>',
   '<p>A child goes to bed later, wakes up later, meals shift, screens increase and the schedule '
   'becomes — understandably — a good deal looser.</p>',
   '<p>And then September comes.</p>',
   '<p class="cb-quote">&ldquo;How is he going to get up in the mornings now?&rdquo; &ldquo;She has '
   'completely forgotten her routine.&rdquo; &ldquo;All summer he was on the tablet.&rdquo;</p>',
   '<p>Returning to the school routine, though, does not have to happen in a single day. Just as a '
   'child needed time to unwind from the school schedule, they may need a gradual period of '
   'readjustment too.</p>',
   '<h2 class="cb-h2">1. Move bedtime gradually</h2>',
   '<p>If a child has grown used to going to bed much later over the holidays, it is difficult to '
   'demand suddenly that they sleep two hours earlier because &ldquo;school starts '
   'tomorrow&rdquo;.</p>',
   '<p>Start shifting bedtime and waking time gradually towards the school timetable. Morning '
   'daylight, a consistent waking time and a calm evening routine can also help the body clock '
   'adjust. Specialists recommend this gradual transition rather than an abrupt last-minute '
   'change.</p>',
   '<h2 class="cb-h2">2. Bring back the &ldquo;anchors&rdquo; of the day first</h2>',
   '<p>The whole day does not need organising from day one.</p>',
   '<p>Start with a few fixed points: waking time, meals, an afternoon activity and bedtime.</p>',
   '<p>Once those start to become predictable, the rest of the schedule can be built around '
   'them.</p>',
   '<h2 class="cb-h2">3. Screens do not have to disappear because school has started</h2>',
   '<p>If the tablet was used for several hours over the summer, a sudden ban will most likely '
   'create more tension.</p>',
   '<p>Instead, we can gradually reintroduce specific times of use and, above all, protect certain '
   'moments of the day: homework, the family meal and sleep.</p>',
   '<p>The AAP recommends no screens at mealtimes, during study and for roughly an hour before '
   'bed, as well as keeping devices out of the bedroom at night.</p>',
   '<h2 class="cb-h2">4. Prepare together whatever can be anticipated</h2>',
   '<p>Bag, clothes, school supplies, the route, the timetable.</p>',
   '<p>Particularly for a child who struggles with transitions, knowing what is about to happen '
   'can significantly reduce the chaos of that first morning.</p>',
   '<p>You can even make a simple visual schedule together for the first few days.</p>',
   '<h2 class="cb-h2">5. Do not fill every afternoon straight away</h2>',
   '<p>School, English, sport, homework, another activity — and suddenly a child moves from total '
   'relaxation to a day without a single free hour.</p>',
   '<p>Free time is not wasted time.</p>',
   '<p>Going back to school demands adjustment in itself. Leave room for play, rest, movement and '
   'a daily life the child can actually sustain.</p>',
   '<h2 class="cb-h2">6. Expect a little grumbling</h2>',
   '<p>Difficulty adjusting does not necessarily mean something is going wrong.</p>',
   '<p>In the first few days a child may be more tired, more irritable, or react more strongly to '
   'boundaries.</p>',
   '<p>Instead of:</p>',
   '<p class="cb-quote">&ldquo;You had everything your own way for months and now you need to pull '
   'yourself together&rdquo;</p>',
   '<p>we can say:</p>',
   '<p class="cb-quote">&ldquo;I know it is hard to change your routine again. We will need a few '
   'days to get used to it.&rdquo;</p>',
   '<p>The boundary stays. But it can sit alongside understanding.</p>',
   '<h2 class="cb-h2">Not everything has to be perfect by the first bell</h2>',
   '<p>Returning to a routine is a transition, not a switch.</p>',
   '<p>A little more predictability each day, boundaries that are firm but realistic, and time to '
   'adjust are often far more effective than an abrupt attempt to put everything back &ldquo;in '
   'its place&rdquo;.</p>',
   '<p>And perhaps this is a useful reminder for parents themselves:</p>',
   '<p>It is not only children who return to the school routine. The whole family returns.</p>',
   '<p>So give them a little time — and yourselves too.</p>',
  ],
  sources=_s("apo-tis-diakopes-sto-scholeio")),

 dict(
  slug="en/articles/identity-acceptance-and-safety.html",
  el="arthra/taftotita-apodochi-asfaleia.html",
  kicker="Identity & acceptance",
  title="When the hard part is not who you are, but whether you can be yourself safely",
  marq="IDENTITY",
  date="2026-09-06",
  teaser="Identity and sexual orientation are not something to be &ldquo;corrected&rdquo;. What "
         "becomes hard is the context in which a person is asked to live them.",
  body=[
   '<p>Being able to be yourself without fearing that you will be judged, rejected, or that you '
   'will have to hide an important part of your identity seems self-evident.</p>',
   '<p>For many LGBTQ+ people, though, it is not always so.</p>',
   '<p>And here an important distinction is needed:</p>',
   "<p>A person's sexual identity or sexual orientation is not a psychological problem that needs "
   'to be &ldquo;corrected&rdquo;.</p>',
   '<p>What can become difficult is the way a person is asked to live that identity within '
   'relationships, family, work and a social environment that is not always accepting.</p>',
   '<h2 class="cb-h2">When you have to think about whether it is safe to be yourself</h2>',
   '<p class="cb-quote">&ldquo;Should I tell my parents?&rdquo;</p>',
   '<p class="cb-quote">&ldquo;Will our relationship change if they find out?&rdquo;</p>',
   '<p class="cb-quote">&ldquo;Can I talk openly about my relationship at work?&rdquo;</p>',
   '<p class="cb-quote">&ldquo;Why do I still feel guilty about something I know is part of who I '
   'am?&rdquo;</p>',
   '<p>The psychological literature uses the term minority stress to describe the additional '
   'psychological load that can build up when a person belongs to a socially stigmatised '
   'group.</p>',
   "<p>Discrimination, rejection, negative remarks, fear of other people's reactions, the need to "
   'conceal one&rsquo;s identity, or even the internalising of negative social messages can weigh '
   'significantly on mental health.</p>',
   "<p>The difficulty, then, does not lie in the person's identity. It may lie in the conditions "
   'within which they are asked to live it.</p>',
   '<h2 class="cb-h2">Acceptance is not only about other people</h2>',
   '<p>There is also a more personal road.</p>',
   '<p>A person may need time to explore their sexuality or their identity, to understand what it '
   'means for them, to manage contradictory feelings, or to gradually let go of guilt and '
   'expectations they have internalised.</p>',
   '<p>They do not have to have all the answers.</p>',
   '<p>Nor to choose a particular label before it feels like theirs.</p>',
   '<p>Psychological support can offer a safe space in which these thoughts can be explored, '
   "without any attempt to change or question the person's identity.</p>",
   '<h2 class="cb-h2">The power of relationships that let us exist</h2>',
   '<p>Social and family support can act protectively against the effects of minority stress.</p>',
   '<p>And that matters particularly.</p>',
   '<p>Because when we talk about LGBTQ+ mental health we do not have to talk only about '
   'difficulties.</p>',
   '<p>We also need to talk about resilience, connection, community, self-acceptance and '
   'relationships in which a person can feel they belong without having to hide.</p>',
   '<h2 class="cb-h2">A space where you do not have to apologise for who you are</h2>',
   '<p>Psychological support for an LGBTQ+ person can concern exactly the same things that might '
   'concern anyone else: anxiety, relationships, separation, self-esteem, family, loneliness, work '
   'or a difficult period of life.</p>',
   '<p>Alongside that, though, there may also be a part of their experience connected to their '
   'identity: coming out, acceptance by the family, fear of rejection, discrimination, their '
   'relationship with their body, or the effort to build relationships in which they feel '
   'safe.</p>',
   '<p>In a psychological setting that respects difference, the aim is not to change who a person '
   'is.</p>',
   '<p>It is for them to understand themselves, their relationships and their experiences better, '
   'and to shape a way of living that is more in keeping with who they really are.</p>',
   '<p>Because sometimes the most important step is not learning to become something '
   'different.</p>',
   '<p>It is being able to exist as ourselves, without fear and without having to apologise for '
   'it.</p>',
  ],
  sources=_s("taftotita-apodochi-asfaleia")),
]
