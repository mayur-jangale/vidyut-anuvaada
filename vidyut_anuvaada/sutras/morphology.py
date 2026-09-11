"""Devanagari Sanskrit morphology: tiG (verbal) and sup (nominal) endings.
All functions operate on Devanagari strings — no SLP1 anywhere."""
from __future__ import annotations

# ── tiG endings (P.3.1.33 onwards) ───────────────────────────────────────────
# Format: (suffix, person_number, mood)
_TIG_LIT = [
	("तिप्", "3s", " indicative"),
	("तस्", "3d", " indicative"),
	("झि", "3p", " indicative"),
	("सिप्", "2s", " indicative"),
	("थस्", "2d", " indicative"),
	("थ", "2p", " indicative"),
	("मिप्", "1s", " indicative"),
	("वस्", "1d", " indicative"),
	("मस्", "1p", " indicative"),
	("ताम्", "3s", " imperative"),
	("ध्वम्", "2p", " imperative"),
	("आट्", "3s", " perfect"),
	("आथाम्", "2d", " perfect"),
	("झिवाम्", "3d", " perfect"),
	("क्वस्व्", "2s", " perfect"),
	("क्स्वस्", "2s", " perfect"),
	("साङ्", "2s", " perfect"),
	("स्वस्", "2s", " perfect"),
	("कृत्वा", "ger", " gerund"),
	("कृत्य", "ger", " gerund"),
	("तुम्", "inf", " infinitive"),
	("तवे", "inf", " infinitive"),
	("अम्", "inf", " infinitive"),
	("शतृ", "part", " present participle"),
	("शानच्", "part", " present participle"),
	("यङ्", "part", " frequentative"),
	("यङ्‌लुक्", "part", " frequentative (base)"),
	("अङ्", "part", " frequentative"),
	("अङ्‌लुक्", "part", " frequentative (base)"),
	("क्था", "perf-part", " perfect participle"),
	("क्विन्", "perf-part", " perfect participle"),
	("कव्य", "perf-part", " perfect participle"),
	("कानच्", "perf-part", " perfect participle"),
	("क्त्वा", "ger", " gerund"),
	("तुमुन्", "inf", " infinitive"),
	("तव्य", "inf", " infinitive"),
	("अनीयर", "inf", " infinitive"),
	("य", "inf", " infinitive"),
	("अम्", "inf", " infinitive"),
	("तासि", "1s", " optative"),
	("तास्थः", "2d", " optative"),
	("तास्थ", "2p", " optative"),
	("तासम्", "1d", " optative"),
	("तास्म", "1p", " optative"),
	("तास्ताम्", "3d", " optative"),
	("तास्व्", "2p", " optative"),
	("तास्ताम्", "3d", " optative"),
	("तासतुः", "3d", " optative"),
	("तासथुः", "2d", " optative"),
	("तास्", "3p", " optative"),
]

# Longest-first ordering for suffix matching
_TIG_SUFFIXES = sorted(
	[(s, pn, md) for s, pn, md in _TIG_LIT],
	key=lambda x: len(x[0]),
	reverse=True,
)

# ── sup endings (P.4.1.1 onwards) ───────────────────────────────────────────
# Base endings → after internal sandhi (guna, visarga, etc.)
# Format: (suffix, case_number) — longest first
_SUP_LIT = [
	# ── Masculine a-stem (after guṇa: अस् → आः/आम्/ए etc.) ──
	("युक्तोः", "m-nom-d"), ("युक्तौ", "m-nom-d"), ("युक्तः", "m-nom-s"),
	("युक्ता", "f-nom-s"), ("युक्ते", "f-nom-d"), ("युक्ताः", "f-nom-p"),
	("युक्तान्", "m-acc-p"), ("युक्तस्य", "gen-s"), ("युक्ताय", "dat-s"),
	("युक्तेन", "inst-s"), ("युक्तात्", "abl-s"), ("युक्ते", "loc-s"),
	# ── Generic patterns (after guna/vrddhi sandhi) ──
	("आः", "f-nom-p"), ("आम्", "f-acc-d"), ("आन्", "m-acc-p"),
	("ौ", "m-nom-d"), ("ाः", "f-nom-p"), ("ः", "m-nom-s"), ("ः", "n-nom-d"),
	("योः", "gen-d"), ("योस्", "loc-d"),
	("स्य", "gen-s"), ("स्मै", "dat-s"), ("स्मात्", "abl-s"),
	("स्मिन्", "loc-s"), ("स्मेषु", "loc-p"),
	("स्याम्", "gen-p"), ("भ्याम्", "d"), ("भ्यः", "p"),
	("स्युः", "3p"), ("सि", "2s"), ("थः", "2d"),
	# ── Neuter ──
	("इ", "n-nom-d"), ("इनि", "n-acc-d"), ("इनाम्", "gen-p"),
	("ई", "n-nom-d"), ("ईनि", "n-acc-d"),
	# ── Original base forms (pre-sandhi) ──
	("सुप्", "1s"), ("अस्", "2s"), ("जस्", "2d"), ("अम्", "2d"),
	("औस्", "3d"), ("अम्यौ", "3d"), ("अमि", "3p"), ("सु", "3s"),
	("भिस्", "p"), ("ङे", "d"), ("ङसि", "2s"), ("ङम्", "d"),
	("ङि", "p"), ("ओस्", "d"), ("आम्", "gen-s"),
	("इति", "loc"), ("तस्", "abl"), ("त्रा", "dat"), ("अर्थे", "dat"),
	("ओः", "dat-d"), ("इनाम्", "gen-p"),
	("अन्त्", "loc"), ("कृत्य", "dat"),
]

# ── Common irregular stems ───────────────────────────────────────────────────
_IRREGULAR = {
	"अस्": ("अस्", "verb", "to be"),
	"वद्": ("वद्", "verb", "to speak"),
	"कृ": ("कृ", "verb", "to do"),
	"गम्": ("गम्", "verb", "to go"),
	"पच्": ("पच्", "verb", "to cook"),
	"नस्": ("नस्", "verb", "to perish"),
	"यज्": ("यज्", "verb", "to sacrifice"),
	"दृश्": ("दृश्", "verb", "to see"),
	"श्रु": ("श्रु", "verb", "to hear"),
	"भू": ("भू", "verb", "to become"),
	"सू": ("सू", "verb", "to generate"),
	"पा": ("पा", "verb", "to drink"),
	"दा": ("दा", "verb", "to give"),
	"धा": ("धा", "verb", "to put"),
	"मा": ("मा", "verb", "to measure"),
	"सा": ("सा", "verb", "to destroy"),
	"हा": ("हा", "verb", "to leave"),
	"लभ्": ("लभ्", "verb", "to obtain"),
	"मुच्": ("मुच्", "verb", "to free"),
	"नृत्य": ("नृत्य", "noun-n", "dance"),
	"गन्ध": ("गन्ध", "noun-m", "smell"),
	"वचस्": ("वचस्", "noun-n", "speech"),
	"वाक्": ("वाक्", "noun-f", "speech"),
	"मनस्": ("मनस्", "noun-n", "mind"),
	"यज्ञ": ("यज्ञ", "noun-m", "sacrifice"),
	"पुरुष": ("पुरुष", "noun-m", "person"),
	"अग्नि": ("अग्नि", "noun-m", "fire"),
	"सömad": ("सोमदत्त", "noun-m", "Saumadatti"),
	"ब्रह्मवित्": ("ब्रह्मवित्", "noun-m", "knower of Brahman"),
	"परन्तप": ("परन्तप", "noun-m", "scorcher of foes"),
	"निराहार": ("निराहार", "noun-m", "fasting"),
	"महाबाहु": ("महाबाहु", "noun-m", "mighty-armed"),
	"महाबल": ("महाबल", "noun-m", "very mighty"),
	"प्रहृष्यत्": ("प्रहृष्यत्", "adj", "would rejoice"),
	"नोद्विजेत्": ("उद्विज्", "verb-opt", "would grieve"),
	"आसक्तचित्त": ("आसक्तचित्त", "adj", "engaged mind"),
	"आसक्तमनस्": ("आसक्तमनस्", "adj", "engaged mind"),
	"अनसूयवत्": ("अनसूयवत्", "adj", "without envy"),
	"सुकृतिन्": ("सुकृतिन्", "noun-m", "good-doer"),
	"दुष्कृतिन्": ("दुष्कृतिन्", "noun-m", "wicked doer"),
	"मयोदित": ("उद्+दा", "verb-ppp", "declared by me"),
	"योगमायासमावृत": ("माया", "noun-f", "covered by Maya"),
	"स्वरूपवत्": ("स्वरूपवत्", "adj", "having own form"),
	"भरतर्षभ": ("भरतर्षभ", "noun-m", "best of Bharatas"),
	"गुडाकेश": ("गुडाकेश", "noun-m", "Arjuna (conqueror of sleep)"),
	"अभिज्ञा": ("अभिज्ञा", "verb-pr", "to know, recognize"),
	"संतुष्ट": ("संतुष्ट", "adj", "content"),
	"यतात्मन्": ("यतात्मन्", "noun-m", "self-controlled"),
	"दृढनिश्चय": ("दृढनिश्चय", "adj", "firmly resolved"),
	"मय्यासक्त": ("मय्यासक्त", "adj", "attached to me"),
	"मय्यर्पित": ("मय्यर्पित", "adj", "surrendered to me"),
	"ब्रह्मविद्": ("ब्रह्मवित्", "noun-m", "knower of Brahman"),
	"ब्रह्मवित्": ("ब्रह्मवित्", "noun-m", "knower of Brahman"),
	"मुक्तसङ्ग": ("मुक्तसङ्ग", "adj", "free from attachment"),
	"अमनीन्": ("अमनीन्", "adj", "without pride"),
	"सत्त्विक": ("सत्त्विक", "adj", "sattvic"),
	"फलप्रेप्सु": ("फलप्रेप्सु", "adj", "desiring fruit"),
	"सङ्गरहित": ("सङ्गरहित", "adj", "without attachment"),
	"समदुःखसुख": ("समदुःखसुख", "adj", "equal in pleasure and pain"),
	"सततयुक्त": ("सततयुक्त", "adj", "ever-engaged"),
	"दृढनिश्चय": ("दृढनिश्चय", "adj", "firmly resolved"),
	"निरहङ्कार": ("निरहङ्कार", "adj", "without ego"),
	"अव्यक्तसंस्थान": ("अव्यक्तसंस्थान", "adj", "unmanifest state"),
	"कर्मफलहेतु": ("कर्मफलहेतु", "noun-m", "attached to action-fruit"),
	"कर्मबन्धन": ("कर्मबन्धन", "noun-m", "bondage of action"),
	"महाभारत": ("महाभारत", "noun-m", "Mahabharata"),
	"पितामह": ("पितामह", "noun-m", "grandfather"),
	"कुरुवृद्ध": ("कुरुवृद्ध", "noun-m", "elder of Kurus"),
	"स्वयंप्रभ": ("स्वयंप्रभ", "adj", "self-luminous"),
	"अनघ": ("अनघ", "adj", "sinless"),
	"प्रभु": ("प्रभु", "noun-m", "Lord, master"),
	"देवदेव": ("देवदेव", "noun-m", "Lord of lords"),
	"सर्वभूत": ("सर्वभूत", "noun-n", "all beings"),
	"सर्वज्ञ": ("सर्वज्ञ", "noun-m", "omniscient"),
	"सर्ववित्": ("सर्ववित्", "noun-m", "knower of all"),
	"पुण्यतम": ("पुण्यतम", "adj", "most virtuous"),
	"विजय": ("विजय", "noun-m", "victory"),
	"गोविन्द": ("गोविन्द", "noun-m", "Govinda"),
	"माधव": ("माधव", "noun-m", "Madhava"),
	"अच्युत": ("अच्युत", "noun-m", "Achyuta"),
	"केशव": ("केशव", "noun-m", "Kesava"),
	"धनंजय": ("धनंजय", "noun-m", "Dhananjaya"),
	"हृषीकेश": ("हृषीकेश", "noun-m", "Hrishikesha"),
	"जगन्नाथ": ("जगन्नाथ", "noun-m", "Lord of universe"),
	"पृथिवीपति": ("पृथिवीपति", "noun-m", "king of earth"),
	"सेना": ("सेना", "noun-f", "army"),
	"रथ": ("रथ", "noun-m", "chariot"),
	"शोक": ("शोक", "noun-m", "grief"),
	"हर्ष": ("हर्ष", "noun-m", "joy"),
	"सिंहनाद": ("सिंहनाद", "noun-m", "lion-roar"),
	"महाशङ्ख": ("महाशङ्ख", "noun-m", "great conch"),
	"पाञ्चजन्य": ("पाञ्चजन्य", "noun-m", "Panchajanya"),
	"देवदत्त": ("देवदत्त", "noun-m", "Devadatta"),
	"पौण्ड्र": ("पौण्ड्र", "noun-m", "Paundra"),
	"वृकोदर": ("वृकोदर", "noun-m", "Vrikodara"),
	"भीमकर्मन्": ("भीमकर्मन्", "noun-m", "Bhima of terrible deeds"),
	"उत्तमौजस्": ("उत्तमौजस्", "noun-m", "Uttamaujas"),
	"द्रौपदेय": ("द्रौपदेय", "noun-m", "son of Draupadi"),
	"सौमदत्ति": ("सौमदत्ति", "noun-m", "Saumadatti"),
	"विराट": ("विराट", "noun-m", "Virata"),
	"द्रुपद": ("द्रुपद", "noun-m", "Drupada"),
	"अश्वत्थामा": ("अश्वत्थामन्", "noun-m", "Ashvatthama"),
	"विकर्ण": ("विकर्ण", "noun-m", "Vikarna"),
	"कर्ण": ("कर्ण", "noun-m", "Karna"),
	"व्यास": ("व्यास", "noun-m", "Vyasa"),
	"वेदव्यास": ("वेदव्यास", "noun-m", "Vedavyasa"),
	"सञ्जय": ("सञ्जय", "noun-m", "Sanjaya"),
	"धृतराष्ट्र": ("धृतराष्ट्र", "noun-m", "Dhritarashtra"),
	"युधिष्ठिर": ("युधिष्ठिर", "noun-m", "Yudhishthira"),
	"भीम": ("भीम", "noun-m", "Bhima"),
	"अर्जुन": ("अर्जुन", "noun-m", "Arjuna"),
	"नकुल": ("नकुल", "noun-m", "Nakula"),
	"सहदेव": ("सहदेव", "noun-m", "Sahadeva"),
	"दुर्योधन": ("दुर्योधन", "noun-m", "Duryodhana"),
	"कौरव": ("कौरव", "noun-m", "Kaurava"),
	"पाण्डव": ("पाण्डव", "noun-m", "Pandava"),
	"भारत": ("भारत", "noun-m", "Bharata"),
	"इन्द्र": ("इन्द्र", "noun-m", "Indra"),
	"शिव": ("शिव", "noun-m", "Shiva"),
	"विष्णु": ("विष्णु", "noun-m", "Vishnu"),
	"ब्रह्मन्": ("ब्रह्मन्", "noun-m", "Brahman"),
	"आदित्य": ("आदित्य", "noun-m", "Aditya"),
	"वसु": ("वसु", "noun-m", "Vasu"),
	"रुद्र": ("रुद्र", "noun-m", "Rudra"),
	"सूर्य": ("सूर्य", "noun-m", "sun"),
	"चन्द्र": ("चन्द्र", "noun-m", "moon"),
	"अग्नि": ("अग्नि", "noun-m", "fire"),
	"वायु": ("वायु", "noun-m", "wind"),
	"कuber": ("कुबेर", "noun-m", "Kubera"),
	"वरुण": ("वरुण", "noun-m", "Varuna"),
	"यम": ("यम", "noun-m", "Yama"),
	"सनत्कुमार": ("सनत्कुमार", "noun-m", "Sanatkumara"),
	"नारद": ("नारद", "noun-m", "Narada"),
	"पराशर": ("पराशर", "noun-m", "Parashara"),
	"वशिष्ठ": ("वशिष्ठ", "noun-m", "Vashishtha"),
	"विश्वामित्र": ("विश्वामित्र", "noun-m", "Vishvamitra"),
	"अत्रि": ("अत्रि", "noun-m", "Atri"),
	"भृगु": ("भृगु", "noun-m", "Bhrigu"),
	"अङ्गिरस्": ("अङ्गिरस्", "noun-m", "Angiras"),
	"कश्यप": ("कश्यप", "noun-m", "Kashyapa"),
	"गौतम": ("गौतम", "noun-m", "Gautama"),
	"भारद्वाज": ("भारद्वाज", "noun-m", "Bharadvaja"),
	"विष्व Mitra": ("विश्वामित्र", "noun-m", "Vishvamitra"),
}

# ── tiG suffix stripping ────────────────────────────────────────────────────

def strip_tig(word: str) -> tuple[str, str, str]:
	"""Strip tiG ending from a Sanskrit verb form.
	Returns (stem, suffix, person_number_mood) or (word, '', '') if no match."""
	for suffix, pn, mood in _TIG_SUFFIXES:
		if word.endswith(suffix) and len(word) > len(suffix):
			stem = word[:-len(suffix)]
			return stem, suffix, pn + mood
		if word == suffix:
			return "", suffix, pn + mood
	return word, "", ""

# ── sup suffix stripping ────────────────────────────────────────────────────

def strip_sup(word: str) -> tuple[str, str, str]:
	"""Strip sup ending from a Sanskrit nominal form.
	Returns (stem, suffix, case_number) or (word, '', '') if no match."""
	_SUP_SUFFIXES = sorted(
		[(s, cn) for s, cn in _SUP_LIT],
		key=lambda x: len(x[0]),
		reverse=True,
	)
	for suffix, cn in _SUP_SUFFIXES:
		if word.endswith(suffix) and len(word) > len(suffix):
			stem = word[:-len(suffix)]
			return stem, suffix, cn
		if word == suffix:
			return "", suffix, cn
	return word, "", ""

# ── Public API ───────────────────────────────────────────────────────────────

def analyse_verb(word: str) -> dict:
	"""Analyse a verbal form. Returns dict with stem, suffix, pn_mood, or None."""
	stem, suffix, pn_mood = strip_tig(word)
	if suffix:
		return {
			"surface": word,
			"stem": stem,
			"suffix": suffix,
			"pn_mood": pn_mood,
			"source": "tiG-ending",
		}
	return None

def analyse_nominal(word: str) -> dict:
	"""Analyse a nominal form. Returns dict with stem, suffix, case_number, or None."""
	stem, suffix, cn = strip_sup(word)
	if suffix:
		return {
			"surface": word,
			"stem": stem,
			"suffix": suffix,
			"case_number": cn,
			"source": "sup-ending",
		}
	return None

def lookup_irregular(word: str):
	"""Look up irregular forms. Returns (lemma, pos, gloss) or None."""
	entry = _IRREGULAR.get(word)
	if entry:
		return entry
	return None

def all_stems() -> dict:
	"""Return all known stems (lemma form -> (pos, gloss))."""
	stems = {}
	for word, entry in _IRREGULAR.items():
		if isinstance(entry, tuple) and len(entry) == 3:
			lemma, pos, gloss = entry
			# Use the word itself as the base form
			if word not in stems:
				stems[word] = entry
	return stems
