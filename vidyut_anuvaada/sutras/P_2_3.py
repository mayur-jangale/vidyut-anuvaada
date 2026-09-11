"""Shared logic for the 73 sutras of P.2.3.x - karaka (semantic role)
rules mapping to vibhakti (case endings).

Karaka types and their default vibhakti:
 kartā (agent) → प्रथमा (1st case) / तृतीया (3rd in certain verbs)
 karman (object) → द्वितीया (2nd case)
 karaṇam (instrument)→ तृतीया (3rd case)
 sampradānam (recipient) → चतुर्थी (4th case)
 apādānam (source) → पञ्चमी (5th case)
 adhikaraṇam (location) → सप्तमी (7th case)

Sections:
 P.2.3.1-18 kartṛ-karman (agent-object rules)
 P.2.3.19 karaṇam definition
 P.2.3.20-28 karaṇam rules
 P.2.3.29 sampradānam definition
 P.2.3.30-34 sampradānam rules
 P.2.3.35 apādānam definition
 P.2.3.36-46 apādānam rules
 P.2.3.47 sambandha (relation) definition
 P.2.3.48-50 sambandha rules
 P.2.3.51 adhikaraṇam definition
 P.2.3.52-73 remaining karaka rules, abhāvādi
"""
from __future__ import annotations

# ------------------ Karaka type constants ------------------
KARTRI = "kartā"
KARMAN = "karman"
KARANAM = "karaṇam"
SAMPRADANAM = "sampradānam"
APADANAM = "apādānam"
ADHIKARANAM = "adhikaraṇam"
SAMBANDHA = "sambandha"
AKATHITAM = "akathitam"

# ------------------ Default vibhakti mapping ------------------
DEFAULT_VIBHAKTI = {
	KARTRI: "प्रथमा (1st case)",
	KARMAN: "द्वितीया (2nd case)",
	KARANAM: "तृतीया (3rd case)",
	SAMPRADANAM: "चतुर्थी (4th case)",
	APADANAM: "पञ्चमी (5th case)",
	SAMBANDHA: "षष्ठी (6th case)",
	ADHIKARANAM: "सप्तमी (7th case)",
}

# ------------------ Verb groups for kartṛ classification ------------------
# Verbs that mark the agent with तृतीया (3rd case) instead of प्रथमा
_THIRD_CASE_AGENT_VERBS = {
	"दृश्", "श्रु", "ज्ञा", "स्मृ", "मत्", "बुध्", "रुह्",
	"स्वप्", "क्रीड्", "क्लिद्", "प्याय्", "रोद्धि",
}

# Verbs where karman (object) takes तृतीया (3rd case)
_THIRD_CASE_KARMAN_VERBS = {
	"बुध्", "विद्", "क्लीब", "सुख्", "दुःख्", "पीड्", "ज्वर्",
}

# Verbs requiring sampradānam (4th case) as karman
_SAMPRADANA_AS_KARMAN = {
	"दे", "आ-दा", "नी", "परा-मृज्", "अर्ह", "याच्", "स्वद्",
}

# Verbs requiring karaṇam (3rd case)
_KARANA_VERBS = {
	"कृ", "लिख्", "खाद्", "पिब्", "आद्", "गम्", "यम्", "धा",
	"सृ", "रुह्", "वद्", "कथ्",
}

# Words marking karaṇam
_KARANA_MARKERS = {
	"हस्तेन", "मुखेन", "वचनेन", "कटकेन", "चक्रिणा", "लिखनया",
	"कूटेन", "शस्त्रेण", "दण्डेन", "बाहुणा",
}

# Words marking sampradānam (recipient)
_SAMPRADANA_MARKERS = {
	"गुरवे", "ब्राह्मणाय", "देवाय", "स्वामिने", "पुत्राय",
	"विश्वासः", "भक्ताय",
}

# Words marking apādānam (source)
_APADANA_MARKERS = {
	"ग्रामात्", "अग्नेः", "देवदत्तात्", "वनात्", "गृहात्",
	"स्कन्धात्", "शिरसः", "पार्श्वात्", "पृष्ठात्",
}

# Words marking adhikaraṇam (location)
_ADHIKARANA_MARKERS = {
	"ग्रामे", "वने", "गृहे", "आकाशे", "पृथिव्याम्", "जलके",
}

# Words marking sambandha (relation)
_SAMBANDHA_MARKERS = {
	"देवदत्तस्य", "गुरोः", "वृक्षस्य", "ग्रामस्य",
}

# ------------------ Abhāvādi (negation) verbs ------------------
_ABHAVA_VERBS = {
	"अस्", "नास्ति", "विद्यते", "भवति", "भू", "स्था",
}

# ------------------ Helper utilities ------------------

def _karaka_tag(role: str, vibhakti: str, word: str, note: str = "") -> str:
	note_str = f";{note}" if note else ""
	return f"kāraka={role}:vibhakti={vibhakti}{note_str};word={word}"


def _default(role: str, word: str) -> str:
	vib = DEFAULT_VIBHAKTI.get(role, "unknown")
	return f"kāraka={role}:vibhakti={vib};word={word}"


def _no_match(word: str, role: str = "") -> str:
	if role:
		return f"no-match:{role}:{word}"
	return f"no-match:{word}"


# =====================================================================
# SECTION A P.2.3.1-18 kartṛ-karman (agent-object rules)
# =====================================================================


def apply_2_3_1(word, pos=""):
	"""P.2.3.1 kartur karmaṇaḥ dravyaṃ...
	Agent's action on object: object → द्वितीया (karman)."""
	if KARMAN in pos or "karma" in pos == "dvitIyA":
		return _karaka_tag(KARMAN, "द्वितीया", word, "kartṛ-karman")
	if KARTRI in pos or "kartA" in pos:
		return _karaka_tag(KARTRI, "प्रथमा", word, "kartṛ-karman")
	return _no_match(word, "kartṛ-karman")


def apply_2_3_2(word, pos=""):
	"""P.2.3.2 karmaṇā hiṃsā.
	With violence, agent → तृतीया (instrument of violence)."""
	violence_verbs = {"हन्", "वध्", "घात्", "क्रुध्", "रोद्धि", "प्रहर्"}
	if pos in violence_verbs or any(v in pos for v in violence_verbs):
		return _karaka_tag(KARTRI, "तृतीया", word, "hiṃsā-violence")
	return f"no-violence:{word}"


def apply_2_3_3(word, pos=""):
	"""P.2.3.3 bhīṣmādibhyo'nyatrasmāḥ.
	Except bhīṣma etc., smā (consumption) → तृतीया."""
	if word.endswith("स्मा") or pos == "smA":
		return _karaka_tag(KARTRI, "तृतीया", word, "smā-consumption")
	return _karaka_tag(KARTRI, "प्रथमा", word, "default-kartṛ")


def apply_2_3_4(word, pos=""):
	"""P.2.3.4 bhīṣmādibhyo'nyatrasmāḥ.
	bhīṣma etc. take प्रथमा."""
	bhisma = {"भीष्म", "दुर्योधन", "कर्ण", "द्रोण"}
	if word in bhisma or pos == "bhISma-etc":
		return _karaka_tag(KARTRI, "प्रथमा", word, "bhISma-viSeṣa")
	return _no_match(word, "bhISma-exception")


def apply_2_3_5(word, pos=""):
	"""P.2.3.5 ṣaṣṭhī vaidyute karmaṇi.
	In destruction (vaidyuta), agent → षष्ठी."""
	if pos in ("vaidyuta", "kṣaya") or "वेद्युत" in pos:
		return _karaka_tag(KARTRI, "षष्ठी", word, "vaidyuta-destruction")
	return _no_match(word, "vaidyuta")


def apply_2_3_6(word, pos=""):
	"""P.2.3.6 ktva-cāvāsyatāyāṃ kartari.
	ktvA suffix in 'having done' sense → तृतीया kartṛ."""
	if pos.endswith("ktvA") or "ktvA" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "ktvA-perfect")
	return _no_match(word, "ktvA")


def apply_2_3_7(word, pos=""):
	"""P.2.3.7 ktva-cāvāsyatāyāṃ kartari.
	avatāra (descent) agent → तृतीया."""
	if pos in ("avataraNa", "avatAra") or "अवतर" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "avataraṇa")
	return _no_match(word, "avataraṇa")


def apply_2_3_8(word, pos=""):
	"""P.2.3.8 ktva-cāvāsyatāyāṃ kartari.
	utkrānta (transcending) agent → तृतीया."""
	if pos in ("utkrAnti", "utkrAta") or "उत्क्रान्त" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "utkrānta")
	return _no_match(word, "utkrānta")


def apply_2_3_9(word, pos=""):
	"""P.2.3.9 ktva-cāvāsyatāyāṃ kartari.
	vyāpanna (perishing) agent → तृतीया."""
	if pos in ("vyApanna", "vyApatti") or "व्याप" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "vyāpanna")
	return _no_match(word, "vyāpanna")


def apply_2_3_10(word, pos=""):
	"""P.2.3.10 ktva-cāvāsyatāyāṃ kartari.
	āmnāta (recited) agent → तृतीया."""
	if pos in ("AmnAta", "AmnAna") or "आम्ना" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "āmnāta")
	return _no_match(word, "āmnāta")


def apply_2_3_11(word, pos=""):
	"""P.2.3.11 ktva-cāvāsyatāyāṃ kartari.
	ārāḍita (sought) agent → तृतीया."""
	if pos in ("ArAqita", "ArAqi") or "आराड" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "ārāḍita")
	return _no_match(word, "ārāḍita")


def apply_2_3_12(word, pos=""):
	"""P.2.3.12 ktva-cāvāsyatāyāṃ kartari.
	ārohaṇa (ascending) agent → तृतीया."""
	if pos in ("ArohaRa", "ArohaNa") or "आरोहण" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "ārohaṇa")
	return _no_match(word, "ārohaṇa")


def apply_2_3_13(word, pos=""):
	"""P.2.3.13 ktva-cāvāsyatāyāṃ kartari.
	praṇidhāna (devotion) agent → तृतीया."""
	if pos in ("praRadhAna", "praRadhAna") or "प्रणिधान" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "praṇidhāna")
	return _no_match(word, "praṇidhāna")


def apply_2_3_14(word, pos=""):
	"""P.2.3.14 ktva-cāvāsyatāyāṃ kartari.
	abhyāsa (repetition) agent → तृतीया."""
	if pos in ("aByAsa", "aByasta") or "अभ्यास" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "abhyāsa")
	return _no_match(word, "abhyāsa")


def apply_2_3_15(word, pos=""):
	"""P.2.3.15 ktva-cāvāsyatāyāṃ kartari.
	pratibandha (obstruction) agent → तृतीया."""
	if pos in ("pratibanDa", "pratibaddha") or "प्रतिबध" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "pratibandha")
	return _no_match(word, "pratibandha")


def apply_2_3_16(word, pos=""):
	"""P.2.3.16 ktva-cāvāsyatāyāṃ kartari.
	parābhava (defeat) agent → तृतीया."""
	if pos in ("parAbhava", "parA-BU") or "पराभव" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "parābhava")
	return _no_match(word, "parābhava")


def apply_2_3_17(word, pos=""):
	"""P.2.3.17 ktva-cāvāsyatāyāṃ kartari.
	upabhoga (enjoyment) agent → तृतीया."""
	if pos in ("upaBoga", "upaBuj") or "उपभोग" in pos:
		return _karaka_tag(KARTRI, "तृतीया", word, "upabhoga")
	return _no_match(word, "upabhoga")


def apply_2_3_18(word, pos=""):
	"""P.2.3.18 ktva-cāvāsyatāyāṃ kartari.
	General exception: agent normally → प्रथमा."""
	return _default(KARTRI, word)


# =====================================================================
# SECTION B P.2.3.19 karaṇam definition
# =====================================================================


def apply_2_3_19(word, pos=""):
	"""P.2.3.19 karaṇaṃ kārakāṇāṃ...
	karaṇam = that which is most efficacious for the action.
	karaṇam → तृतीया vibhakti."""
	karana_keywords = {"करण", "साधक", "साधन", "साधकतम"}
	if any(k in word for k in karana_keywords) or KARANAM in pos:
		return _karaka_tag(KARANAM, "तृतीया", word, "sādhakatama-def")
	# Check for instrument markers
	for marker in _KARANA_MARKERS:
		if marker in word:
			return _karaka_tag(KARANAM, "तृतीया", word, "instrument-marker")
	return _no_match(word, KARANAM)


# =====================================================================
# SECTION C P.2.3.20-28 karaṇam rules
# =====================================================================


def apply_2_3_20(word, pos=""):
	"""P.2.3.20 sādhakatamaṃ karaṇaṃ.
	Most efficacious means = karaṇam → तृतीया."""
	if pos in ("sADakatama", "sADakam") or "साधकतम" in pos:
		return _karaka_tag(KARANAM, "तृतीया", word, "sādhakatama")
	return _no_match(word, "sādhakatama")


def apply_2_3_21(word, pos=""):
	"""P.2.3.21 svayaṃ ca.
	Self (svayam) is NOT karaṇam."""
	if word == "स्वयम्" or pos == "svayam":
		return "not-karaṇam:svayam;word=" + word
	return _no_match(word, "svayam-not-karaṇa")


def apply_2_3_22(word, pos=""):
	"""P.2.3.22 avyayena ca sādhakatamāt.
	Avyaya (indeclinable) is NOT karaṇam."""
	if pos in ("avyaya", "upa", "antar", "bahiH"):
		return "not-karaṇam:avyaya;word=" + word
	return _no_match(word, "avyaya-not-karaṇa")


def apply_2_3_23(word, pos=""):
	"""P.2.3.23 samānaviṣaye tu kartṛkaraṇayoḥ pūrvanipātaḥ.
	When agent and instrument share object, agent comes first."""
	if pos in ("samAna-viSaya", "kartṛ-karaṇa"):
		return "order:kartṛ>karaṇa:samAna-viSaya;word=" + word
	return _no_match(word, "samAna-viSaya")


def apply_2_3_24(word, pos=""):
	"""P.2.3.24 svabhāvasiddhau karaṇam.
	Natural/self-manifest = not karaṇam."""
	if pos in ("svabhAvasiddha", "svABAvika") or "स्वभाव" in pos:
		return "not-karaṇam:svabhāvasiddha;word=" + word
	return _no_match(word, "svabhāvasiddha")


def apply_2_3_25(word, pos=""):
	"""P.2.3.25 deśakālārthayukte tu karaṇam.
	With place/time/object qualification = karaṇam → तृतीया."""
	if pos in ("deza-kAla-artha-yukta", "karaṇa-qualified"):
		return _karaka_tag(KARANAM, "तृतीया", word, "deza-kAla-qualified")
	return _no_match(word, "deza-kAla-karaṇa")


def apply_2_3_26(word, pos=""):
	"""P.2.3.26 saṃpradānāpādānayorhyanavasāye sādharmyeṇa karaṇatvam.
	Sampradānam/apādānam with homogeneity → karaṇam."""
	if pos in ("sampradāna-avasāya", "sādharmya"):
		return _karaka_tag(KARANAM, "तृतीया", word, "sādharmya-homogeneity")
	return _no_match(word, "sādharmya")


def apply_2_3_27(word, pos=""):
	"""P.2.3.27 na ca tadvati.
	Not in that which already exists."""
	if pos in ("nAsti", "abhAva") or "नस्ति" in pos:
		return "not-karaṇam:tadvati;word=" + word
	return _no_match(word, "tadvati")


def apply_2_3_28(word, pos=""):
	"""P.2.3.28 karaṇam.
	General karaṇam rule → तृतीया."""
	for marker in _KARANA_MARKERS:
		if marker in word:
			return _karaka_tag(KARANAM, "तृतीया", word, "karaṇam-general")
	return _no_match(word, "karaṇam-general")


# =====================================================================
# SECTION D P.2.3.29-34 sampradānam (recipient) rules
# =====================================================================


def apply_2_3_29(word, pos=""):
	"""P.2.3.29 saṃpradānam.
	sampradānam = that which is intended to be given/received.
	sampradānam → चतुर्थी (4th case)."""
	for marker in _SAMPRADANA_MARKERS:
		if marker in word:
			return _karaka_tag(SAMPRADANAM, "चतुर्थी", word, "sampradānam-def")
	if SAMPRADANAM in pos or "sampradAna" in pos:
		return _karaka_tag(SAMPRADANAM, "चतुर्थी", word, "sampradānam-def")
	# Check for dative markers (suffixes)
	for sfx in ("वे", "ये", "ने", "ब्ये"):
		if word.endswith(sfx):
			return _karaka_tag(SAMPRADANAM, "चतुर्थी", word, "dative-suffix")
	return _no_match(word, SAMPRADANAM)


def apply_2_3_30(word, pos=""):
	"""P.2.3.30 caturthyabhidheyaṃ saṃpradānam.
	sampradānam named by चतुर्थी case."""
	if pos == "caturthI":
		return _karaka_tag(SAMPRADANAM, "चतुर्थी", word, "caturthI-viBakti")
	return _no_match(word, "caturthI-sampradāna")


def apply_2_3_31(word, pos=""):
	"""P.2.3.31 dattasya.
	Given (datta) → sampradānam → चतुर्थी."""
	if word.startswith("दत्") or pos == "datta":
		return _karaka_tag(SAMPRADANAM, "चतुर्थी", word, "datta-given")
	return _no_match(word, "datta")


def apply_2_3_32(word, pos=""):
	"""P.2.3.32 prayoktaryupamāne ca.
	In causative and comparison → sampradānam."""
	if pos in ("prayojana", "upamAna") or "प्रयोजन" in pos:
		return _karaka_tag(SAMPRADANAM, "चतुर्थी", word, "prayoktari-upamAne")
	return _no_match(word, "prayoktari")


def apply_2_3_33(word, pos=""):
	"""P.2.3.33 karaṇābhyāṃ karaṇam.
	With karaṇa, also sampradānam."""
	if KARANAM in pos or _KARANA_VERBS & set(pos.split()):
		return _karaka_tag(SAMPRADANAM, "चतुर्थी", word, "karaṇa-sampradāna")
	return _no_match(word, "karaṇa-sampradāna")


def apply_2_3_34(word, pos=""):
	"""P.2.3.34 saṃpradānam.
	General sampradānam → चतुर्थी."""
	for marker in _SAMPRADANA_MARKERS:
		if marker in word:
			return _karaka_tag(SAMPRADANAM, "चतुर्थी", word, "sampradānam-general")
	# Check dative endings
	for sfx in ("वे", "ये", "ने"):
		if word.endswith(sfx):
			return _karaka_tag(SAMPRADANAM, "चतुर्थी", word, "caturthI-default")
	return _no_match(word, "sampradānam-general")


# =====================================================================
# SECTION E P.2.3.35-46 apādānam (source / fixed point) rules
# =====================================================================


def apply_2_3_35(word, pos=""):
	"""P.2.3.35 apādānam.
	apādānam = fixed point from which motion departs.
	apādānam → पञ्चमी (5th case)."""
	for marker in _APADANA_MARKERS:
		if marker in word:
			return _karaka_tag(APADANAM, "पञ्चमी", word, "apādānam-def")
	if APADANAM in pos or "apAdAna" in pos:
		return _karaka_tag(APADANAM, "पञ्चमी", word, "apādānam-def")
	# Check for पञ्चमी suffixes (āt, tas)
	for sfx in ("वात्", "तस्", "हि", "शि"):
		if word.endswith(sfx) and word not in _SAMBANDHA_MARKERS:
			return _karaka_tag(APADANAM, "पञ्चमी", word, "pañcamī-suffix")
	return _no_match(word, APADANAM)


def apply_2_3_36(word, pos=""):
	"""P.2.3.36 apāye'padānam.
	Departure (apāya) → apādānam → पञ्चमी."""
	if pos in ("apAya", "apAya-gamana") or "अपाय" in pos:
		return _karaka_tag(APADANAM, "पञ्चमी", word, "apāya-departure")
	return _no_match(word, "apāya")


def apply_2_3_37(word, pos=""):
	"""P.2.3.37 prayojane'padānam.
	Purpose (prayojana) → apādānam."""
	if pos in ("prayojana", "prayoktR") or "प्रयोजन" in pos:
		return _karaka_tag(APADANAM, "पञ्चमी", word, "prayojana-purpose")
	return _no_match(word, "prayojana")


def apply_2_3_38(word, pos=""):
	"""P.2.3.38 viśiṣṭe'padānam.
	Special qualification → apādānam."""
	if pos in ("viSizwa", "viSesha") or "विशिष्ट" in pos:
		return _karaka_tag(APADANAM, "पञ्चमी", word, "viśiṣṭa")
	return _no_match(word, "viśiṣṭa")


def apply_2_3_39(word, pos=""):
	"""P.2.3.39 pratipūrvāt kṛño'padānam.
	From pra + kṛ (doing/effecting) → apādānam."""
	if word.startswith("प्र") or pos.startswith("pra-kf"):
		return _karaka_tag(APADANAM, "पञ्चमी", word, "pra-kṛ-apādāna")
	return _no_match(word, "pra-kṛ")


def apply_2_3_40(word, pos=""):
	"""P.2.3.40 parājerasoḍhaḥ.
	Conquered/overcome → apādānam."""
	if pos in ("parAjita", "asUDha") or "पराजित" in pos:
		return _karaka_tag(APADANAM, "पञ्चमी", word, "parājita-conquered")
	return _no_match(word, "parājita")


def apply_2_3_41(word, pos=""):
	"""P.2.3.41 vāraṇārthānāmīpsitaḥ.
	For protection (vāraṇa) → apādānam."""
	if pos in ("vAraRa", "trANa") or "वारण" in pos:
		return _karaka_tag(APADANAM, "पञ्चमी", word, "vāraṇa-protection")
	return _no_match(word, "vāraṇa")


def apply_2_3_42(word, pos=""):
	"""P.2.3.42 antarddho yenādṛśyamicchati.
	Concealment → apādānam."""
	if pos in ("antarddhi", "antar-DR") or "अन्तर्द्धि" in pos:
		return _karaka_tag(APADANAM, "पञ्चमी", word, "antarddhi-concealment")
	return _no_match(word, "antarddhi")


def apply_2_3_43(word, pos=""):
	"""P.2.3.43 ṣaṣṭhī cānāpādāne'pūrvasya.
	ṣaṣṭhī (6th) for apādānam when not new."""
	if pos in ("sazWI-apAdAna", "apUrva"):
		return _karaka_tag(APADANAM, "षष्ठी", word, "sazWI-apAdāna")
	return _no_match(word, "sazWI-apAdāna")


def apply_2_3_44(word, pos=""):
	"""P.2.3.44 apūrvasya ṣaṣṭhī.
	Unusual/exceptional → apādānam with षष्ठी."""
	if pos in ("apUrva", "apUrva-viSizwa") or "अपूर्व" in pos:
		return _karaka_tag(APADANAM, "षष्ठी", word, "apūrva-ṣaṣṭhī")
	return _no_match(word, "apūrva")


def apply_2_3_45(word, pos=""):
	"""P.2.3.45 pāṇḍimādiṣu ca.
	pāṇḍu etc. → apādānam."""
	if word.startswith("पाण्ड") or pos in ("pANDu-viSizwa",):
		return _karaka_tag(APADANAM, "पञ्चमी", word, "pANDu-apAdāna")
	return _no_match(word, "pANDu")


def apply_2_3_46(word, pos=""):
	"""P.2.3.46 apādānam.
	General apādānam rule → पञ्चमी."""
	for marker in _APADANA_MARKERS:
		if marker in word:
			return _karaka_tag(APADANAM, "पञ्चमी", word, "apādānam-general")
	return _no_match(word, "apādānam-general")


# =====================================================================
# SECTION F P.2.3.47 sambandha (relation) definition
# =====================================================================


def apply_2_3_47(word, pos=""):
	"""P.2.3.47 sambandhaḥ.
	sambandha = relation between two entities.
	sambandha → षष्ठी (6th case)."""
	for marker in _SAMBANDHA_MARKERS:
		if marker in word:
			return _karaka_tag(SAMBANDHA, "षष्ठी", word, "sambandha-def")
	if SAMBANDHA in pos or "sambandha" in pos:
		return _karaka_tag(SAMBANDHA, "षष्ठी", word, "sambandha-def")
	# षष्ठी endings: syaH
	for sfx in ("स्य", "र्", "स्यस्य"):
		if word.endswith(sfx):
			return _karaka_tag(SAMBANDHA, "षष्ठी", word, "sazTI-ending")
	return _no_match(word, SAMBANDHA)


# =====================================================================
# SECTION G P.2.3.48-50 sambandha rules
# =====================================================================


def apply_2_3_48(word, pos=""):
	"""P.2.3.48 saṃbandhaḥ.
	sambandha (relation) marked by षष्ठी."""
	if pos in ("sambandha", "sambandha-viSizwa"):
		return _karaka_tag(SAMBANDHA, "षष्ठी", word, "sambandha")
	return _no_match(word, "sambandha")


def apply_2_3_49(word, pos=""):
	"""P.2.3.49 tatsambandhi.
	Related to that → sambandha."""
	if pos in ("tat-sambandhi", "sambandha-viSizwa"):
		return _karaka_tag(SAMBANDHA, "षष्ठी", word, "tat-sambandhi")
	return _no_match(word, "tat-sambandhi")


def apply_2_3_50(word, pos=""):
	"""P.2.3.50 saṃbandhaḥ.
	General sambandha → षष्ठी."""
	for marker in _SAMBANDHA_MARKERS:
		if marker in word:
			return _karaka_tag(SAMBANDHA, "षष्ठी", word, "sambandha-general")
	return _no_match(word, "sambandha-general")


# =====================================================================
# SECTION H P.2.3.51 adhikaraṇam (location) definition
# =====================================================================


def apply_2_3_51(word, pos=""):
	"""P.2.3.51 adhikaraṇaṃ ca.
	adhikaraṇam = location where the action takes place.
	adhikaraṇam → सप्तमी (7th case)."""
	for marker in _ADHIKARANA_MARKERS:
		if marker in word:
			return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "adhikaraṇam-def")
	if ADHIKARANAM in pos or "adhikaraNa" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "adhikaraṇam-def")
	# सप्तमी endings: i, Su, oS, sup etc. for neuter
	for sfx in ("इ", "सुप्", "ओस्"):
		if word.endswith(sfx):
			return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "saptamI-ending")
	return _no_match(word, ADHIKARANAM)


# =====================================================================
# SECTION I P.2.3.52-60 adhikaraṇam rules
# =====================================================================


def apply_2_3_52(word, pos=""):
	"""P.2.3.52 saptamyarthe.
	In the 7th case sense → adhikaraṇam."""
	if pos in ("saptamI-artha", "adhikaraNa") or "सप्तमी" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "saptamI-artha")
	return _no_match(word, "saptamI-artha")


def apply_2_3_53(word, pos=""):
	"""P.2.3.53 nir upasargāt.
	nir (separate) → सप्तमी adhikaraṇam."""
	if word.startswith("निर्") or pos == "nir-upasarga":
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "nir-upasarga")
	return _no_match(word, "nir-upasarga")


def apply_2_3_54(word, pos=""):
	"""P.2.3.54 api ca.
	api (also) → adhikaraṇam → सप्तमी."""
	if word.startswith("अपि") or pos == "api-adhikaraRa":
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "api-adhikaraRa")
	return _no_match(word, "api-adhikaraRa")


def apply_2_3_55(word, pos=""):
	"""P.2.3.55 anupasarge.
	Without upasarga → adhikaraṇam."""
	if pos in ("anupasarga", "no-upasarga") or not pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "anupasarge")
	return _no_match(word, "anupasarge")


def apply_2_3_56(word, pos=""):
	"""P.2.3.56 alpe saptamī.
	Smallness → सप्तमी adhikaraṇam."""
	if pos in ("alpa", "alpa-saptamI") or "अल्प" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "alpe")
	return _no_match(word, "alpe")


def apply_2_3_57(word, pos=""):
	"""P.2.3.57 bahutve.
	Multiplicity → सप्तमी adhikaraṇam."""
	if pos in ("bahutva", "bahutve") or "बहुत्व" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "bahutve")
	return _no_match(word, "bahutve")


def apply_2_3_58(word, pos=""):
	"""P.2.3.58 kāle.
	Time → सप्तमी adhikaraṇam."""
	if pos in ("kAla", "kAla-adhikaraRa") or "काल" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "kāle")
	return _no_match(word, "kāle")


def apply_2_3_59(word, pos=""):
	"""P.2.3.59 yāvad upamāne.
	Comparison extent → सप्तमी adhikaraṇam."""
	if pos in ("yAvat-upamAna", "upamAna") or "यावत्" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "yāvat-upamāne")
	return _no_match(word, "yāvat-upamāne")


def apply_2_3_60(word, pos=""):
	"""P.2.3.60 pramāṇe.
	Measure → सप्तमी adhikaraṇam."""
	if pos in ("pramANa", "pramANa-adhikaraRa") or "प्रमाण" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "pramāṇe")
	return _no_match(word, "pramāṇe")


# =====================================================================
# SECTION J P.2.3.61-69 adhikaraṇam (continued)
# =====================================================================


def apply_2_3_61(word, pos=""):
	"""P.2.3.61 dravye.
	Substance → सप्तमी adhikaraṇam."""
	if pos in ("dravya", "dravya-adhikaraRa") or "द्रव्य" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "dravye")
	return _no_match(word, "dravye")


def apply_2_3_62(word, pos=""):
	"""P.2.3.62 deśakālayoś ca.
	Place and time → सप्तमी adhikaraṇam."""
	if pos in ("deza-kAla", "deza", "kAla") or "देश" in pos or "काल" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "deśa-kāla")
	return _no_match(word, "deśa-kāla")


def apply_2_3_63(word, pos=""):
	"""P.2.3.63 viṣaye.
	Subject/object of knowledge → सप्तमी adhikaraṇam."""
	if pos in ("viSaya", "jñāna-viSaya") or "विषय" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "viṣaye")
	return _no_match(word, "viṣaye")


def apply_2_3_64(word, pos=""):
	"""P.2.3.64 kriyāyām.
	Action itself → सप्तमी adhikaraṇam."""
	if pos in ("kriyA", "kriyA-adhikaraRa") or "क्रिया" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "kriyāyām")
	return _no_match(word, "kriyāyām")


def apply_2_3_65(word, pos=""):
	"""P.2.3.65 hetau.
	Reason/cause → सप्तमी adhikaraṇam."""
	if pos in ("hetu", "hetu-adhikaraRa") or "हेतु" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "hetau")
	return _no_match(word, "hetau")


def apply_2_3_66(word, pos=""):
	"""P.2.3.66 saṃjñāyām.
	Designation → सपत्तमी adhikaraṇam."""
	if pos in ("saMjñA", "saMjñA-adhikaraRa") or "संज्ञा" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "saṃjñāyām")
	return _no_match(word, "saṃjñāyām")


def apply_2_3_67(word, pos=""):
	"""P.2.3.67 samāse.
	Compound → सप्तमी adhikaraṇam."""
	if pos in ("samAsa", "samAsa-adhikaraRa") or "समास" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "samāse")
	return _no_match(word, "samāse")


def apply_2_3_68(word, pos=""):
	"""P.2.3.68 taddhite.
	Taddhita derivative → सप्तमी adhikaraṇam."""
	if pos in ("taddhita", "taddhita-samAsa") or "तद्धित" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "taddhite")
	return _no_match(word, "taddhite")


def apply_2_3_69(word, pos=""):
	"""P.2.3.69 sāmānye.
	Universality → सप्तमी adhikaraṇam."""
	if pos in ("sAmAnya", "sAmAnya-adhikaraRa") or "सामान्य" in pos:
		return _karaka_tag(ADHIKARANAM, "सप्तमी", word, "sāmānye")
	return _no_match(word, "sāmānye")


# =====================================================================
# SECTION K P.2.3.70-73 abhāvādi (negation) rules
# =====================================================================


def apply_2_3_70(word, pos=""):
	"""P.2.3.70 abhāve kṛtyas tu.
	Negation with kṛtya → karman → द्वितीया."""
	if pos in ("abhAva", "abhAva-karman") or "अभाव" in pos:
		return _karaka_tag(KARMAN, "द्वितीया", word, "abhāva-kṛtya")
	return _no_match(word, "abhāva-kṛtya")


def apply_2_3_71(word, pos=""):
	"""P.2.3.71 abhāvaśabdaḥ.
	Negation word → karman."""
	abhava_words = {"अस्ति", "नास्ति", "न", "नहि", "मा", "नैत"}
	if word in abhava_words or pos in ("abhAva", "na"):
		return _karaka_tag(KARMAN, "द्वितीया", word, "abhāva-śabda")
	return _no_match(word, "abhāva-śabda")


def apply_2_3_72(word, pos=""):
	"""P.2.3.72 abhāvasya prāg abhidhānāt.
	Before mentioning negation → karman."""
	if pos in ("prag-abhidhAna", "pUrva-abhidhAna") or "प्राग्" in pos:
		return _karaka_tag(KARMAN, "द्वितीया", word, "prāg-abhidhānāt")
	return _no_match(word, "prāg-abhidhānāt")


def apply_2_3_73(word, pos=""):
	"""P.2.3.73 abhāvādi.
	General abhāvādi (negation) rule → karman → द्वितीया."""
	abhava_roots = {"अस्", "भू", "स्था", "गम्", "इ", "आगम्", "प्राप्"}
	for root in abhava_roots:
		if pos.startswith(root) or root in pos:
			return _karaka_tag(KARMAN, "द्वितीया", word, "abhāvādi-general")
	return _no_match(word, "abhāvādi-general")


# =====================================================================
# Utility: run all karaka rules for a word
# =====================================================================

def apply_2_3_all(word, pos=""):
	"""Apply all 73 karaka rules and return matching results."""
	import re
	results = []
	for i in range(1, 74):
		func_name = f"apply_2_3_{i}"
		func = globals().get(func_name)
		if func:
			result = func(word, pos)
			if result and not result.startswith("no-match") and not result.startswith("not-") and not result.startswith("no-"):
				results.append((f"P.2.3.{i}", result))
	return results


# =====================================================================
# Karaka → Vibhakti lookup
# =====================================================================

def karaka_to_vibhakti(karaka: str) -> str:
	"""Return the default vibhakti for a given karaka type."""
	return DEFAULT_VIBHAKTI.get(karaka, "unknown")


# =====================================================================
# Karaka classification entry point
# =====================================================================

def classify_karaka(word: str, pos: str = "", context: str = "") -> dict:
	"""Classify a word into its karaka role(s) with vibhakti.

	Args:
		word: Sanskrit word (Devanagari).
		pos: Part-of-speech / verb root hint.
		context: Optional context hint for disambiguation.

	Returns:
		Dict with karaka role, vibhakti, confidence, and source sutra.
	"""
	results = apply_2_3_all(word, pos)
	if not results:
		return {
			"word": word,
			"pos": pos,
			"karaka": "unknown",
			"vibhakti": "unknown",
			"confidence": 0.0,
			"sutra": "",
		}
	# Return the best match (first match)
	sutra, tag = results[0]
	role = "unknown"
	vibhakti = "unknown"
	if "kāraka=" in tag:
		role_part = tag.split("kāraka=")[1].split(":")[0]
		vibh_part = tag.split("vibhakti=")[1].split(";")[0]
		role = role_part
		vibhakti = vibh_part
	return {
		"word": word,
		"pos": pos,
		"karaka": role,
		"vibhakti": vibhakti,
		"confidence": 0.8,
		"sutra": sutra,
	}

# EOF
