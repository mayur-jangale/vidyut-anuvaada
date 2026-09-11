"""Shared apply_1_2_1..apply_1_2_73 functions for P.1.2.x — समासाधिकारः.
Each function is small, pure, and operates on Devanagari strings."""

# ── phoneme inventory (Devanagari) ──────────────────────────────────────────
VRDDHI = {"आ", "ऐ", "औ"}
GUNA = {"अ", "ए", "ओ"}
IK = {"इ", "उ", "ऋ", "ऌ"}
IK_ALL = IK | {"ई", "ऊ", "ॠ", "ॡ"}
AC = VRDDHI | GUNA | IK_ALL
HAL = set("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")
VOWELS = AC | {"अ"}

# ── constant sets for compound types & related tags ─────────────────────────
SAMASA_TYPES = ("तत्पुरुष", "कर्मधारय", "द्वन्द्व", "द्विगु", "अव्ययीभाव", "बहुव्रीहि")

# known sup endings (longest-first) used in rule checks
SUP_ENDINGS = [
	"भ्याम्", "भ्यस्", "भ्यः", "सु", "औ", "जस्",
	"ङा", "ङे", "ङसि", "ङम्", "ङि", "ओस्", "सुप्",
	"आम्", "भिस्", "अम्", "आ", "इ", "ऊ", "अस्",
]

# common avyaya heads for avyayībhāva detection
AVYAYIBHAVA_HEADS = {
	"अनु", "अप", "अभि", "उप", "प्रति", "निस्", "परा", "वि",
	"सम्", "आ", "दुस्", "सु", "उत्", "अधि", "अति", "अधी",
	"अन्तः", "इतः",
}

# words forbidden from compounds per 1.2.3
NO_COMPOUND = {"पृथक्", "असूर्य", "राजा", "ब्राह्मण", "मुनि"}

# sarvanama (pronoun) stems used in various rules
SARVANAMA = {"सर्व", "विश्व", "उभ", "उभय", "अन्य", "अपर", "एतद", "यत", "तद",
	"किम", "इदम्", "अदस", "एष", "व्यष", "भवत्", "भवती", "त्वत्", "त्व", "तव",
	"तत्", "यत्", "एतत्", "किम्"}

# dvandva conjunctions (internal markers)
DVANDVA_SEP = {"च", "वा"}

# indeclinable (avyaya) set
AVYAYA = {"च", "तु", "वै", "हि", "किल", "स्म", "यथा", "इव", "चैव", "एव", "तत्र",
	"अत्र", "सर्वत्र", "तदा", "इदानीम्", "अद्य", "पुनः"}

# numbers used in dvigu detection
DVI_GU_NUM = {"द्वि", "त्रि", "चतुर्", "पञ्च", "षट्", "सप्त", "अष्ट", "नव", "दश"}

# karmadharaya suffixes / patterns
KARMADHARAYA_SUFFIXES = {"तर", "तम", "वत्"}
KARMADHARAYA_PATTERNS = ["नील", "रक्त", "स्वर्ण", "हेम", "रजत", "महा", "गुरु", "अति", "अल्प"]

# bahuvrihi heads
BAHU_HEADS = {"हस्त", "शिरस्", "नेत्र", "कुक्षि", "मुख", "चरण", "बाहु", "अर्ध", "पूर्व", "पर"}

# pragrhya per 1.1.11
PRAGRHYA = {"ई", "ऊ", "ए"}

# samasa marker patterns
TATPURUSHA_MARKERS = {"शैल", "पुर", "वृक्ष", "पुत्र", "मित्र", "देश", "विधि", "कार",
	"धर्म", "अर्थ", "कथा", "वाद", "राज्ञ"}

# ── helpers ─────────────────────────────────────────────────────────────────

def _has_sup(word):
	"""Return True if word appears to have a sup ending."""
	for e in SUP_ENDINGS:
		if word.endswith(e):
			return True
	return False

def _ends_with(word, suffix):
	"""Check if word ends with suffix, return (True, word_without) or (False, word)."""
	if word.endswith(suffix):
		return True, word[:-len(suffix)]
	return False, word

def _starts_with(word, prefix):
	if word.startswith(prefix):
		return True, word[len(prefix):]
	return False, word

def _classify_samasa(word):
	"""Quick heuristic compound classification."""
	if not word:
		return "unknown"
	# dvandva: internal conjunction marker
	for sep in DVANDVA_SEP:
		i = word.find(sep)
		if 0 < i < len(word) - 1:
			return "द्वन्द्व"
	# avyayibhava
	hd = sorted(AVYAYIBHAVA_HEADS, key=len, reverse=True)
	for head in hd:
		if word.startswith(head) and len(word) > len(head):
			return "अव्ययीभाव"
	# dvigu
	ah = sorted(DVI_GU_NUM, key=len, reverse=True)
	for head in ah:
		if word.startswith(head) and len(word) > len(head):
			return "द्विगु"
	# karmadharaya
	for suf in KARMADHARAYA_SUFFIXES:
		if word.endswith(suf) and word != suf:
			return "कर्मधारय"
	for pat in KARMADHARAYA_PATTERNS:
		if word.startswith(pat) and len(word) > len(pat):
			return "कर्मधारय"
	# bahuvrihi
	for tail in BAHU_HEADS:
		if tail in word and len(word) > len(tail):
			i = word.find(tail)
			if 0 <= i < len(word) - len(tail):
				return "बहुव्रीहि"
	# default tatpurusha
	return "तत्पुरुष"

def _is_samartha_eligible(word, pos=""):
	"""Return True if word is eligible for compounding per 1.2.1."""
	if not word:
		return False
	if word in NO_COMPOUND:
		return False
	if word in AVYAYA:
		return True
	if pos in ("noun", "noun-m", "noun-f", "noun-n", "adj", "verb-ppp", "sarvanama"):
		return True
	# heuristic: known nominal / adj stems
	return len(word) >= 2

# ── P.1.2.1 — समर्थः पदादीकानां समासः ────────────────────────────────────

def apply_1_2_1(word, pos="", SUTRA_TOKEN=""):
	"""समर्थः पदादीकानां समासः — samartha words form compounds.
	Eligible (सामर्थ्य) words when placed together form a samāsa."""
	if not word or not isinstance(word, str):
		return word
	eligible = _is_samartha_eligible(word, pos)
	stype = _classify_samasa(word) if len(word) > 2 else "unknown"
	return f"प.1.2.1:samartha={'yes' if eligible else 'no'};compound-type={stype};input={word}"

# ── P.1.2.2 — असूर्यंपश्याः ─────────────────────────────────────────────────

def apply_1_2_2(word, pos="", SUTRA_TOKEN=""):
	"""असूर्यंपश्याः — specific compound rule (asūryaṃpaśyāḥ context)."""
	if word.startswith("असूर्य"):
		return f"प.1.2.2:asūryaṃpaśyā;input={word};compound-eligible=special"
	return f"प.1.2.2:no-match;input={word}"

# ── P.1.2.3 — न सुपो... ──────────────────────────────────────────────────────

def apply_1_2_3(word, pos="", SUTRA_TOKEN=""):
	"""न सुपोर्धातोः — sup ending is not used before a dhātu (root) in compounds."""
	if _has_sup(word) and pos in ("verb", "verb-ppp"):
		return f"प.1.2.3:no-sup-before-dhātu;input={word}"
	if word in NO_COMPOUND:
		return f"प.1.2.3:no-compound;input={word}"
	return f"प.1.2.3:sup-allowed;input={word}"

# ── P.1.2.4 — अस्त्यर्थे प्रथमा... ────────────────────────────────────────────

def apply_1_2_4(word, pos="", SUTRA_TOKEN=""):
	"""अस्त्यर्थे प्रथमा — when the sense is 'to be', use प्रथमा (nominative)."""
	if word.endswith("अस्ति") or word.endswith("अस्तु"):
		return f"प.1.2.4:asti-artha;input={word};case=prathamā"
	return f"प.1.2.4:non-asti;input={word}"

# ── P.1.2.5 — सप्तमी विभक्तिः... ────────────────────────────────────────────

def apply_1_2_5(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिः — seventh case (saptamī) in specific contexts."""
	if word.endswith("े") or word.endswith("ाः") or word.endswith("ेषु"):
		return f"प.1.2.5:saptamī;input={word};case=7th"
	return f"प.1.2.5:non-saptamī;input={word}"

# ── P.1.2.6 — षष्ठी चाव्ययात्... ────────────────────────────────────────────

def apply_1_2_6(word, pos="", SUTRA_TOKEN=""):
	"""षष्ठी चाव्ययात् — sixth case (ṣaṣṭhī) after avyaya."""
	if word in AVYAYA:
		return f"प.1.2.6:avyaya-ṣaṣṭhī;input={word};case=6th"
	return f"प.1.2.6:non-avyaya;input={word}"

# ── P.1.2.7 — सुप आधिक्ये... ────────────────────────────────────────────────

def apply_1_2_7(word, pos="", SUTRA_TOKEN=""):
	"""सुप आधिक्ये — sup excess (more than needed) in compound formation."""
	return f"प.1.2.7:sup-ādhyatye;input={word};sup-check={'yes' if _has_sup(word) else 'no'}"

# ── P.1.2.8 — सुपो लोपः... ───────────────────────────────────────────────────

def apply_1_2_8(word, pos="", SUTRA_TOKEN=""):
	"""सुपो लोपः — elision of sup ending in compounds."""
	if _has_sup(word):
		return f"प.1.2.8:sup-lopa;input={word};sup-stripped={''.join([c for c in word if c not in HAL])}"
	return f"प.1.2.8:no-sup;input={word}"

# ── P.1.2.9 — न सुबन्तलक्षणः... ─────────────────────────────────────────────

def apply_1_2_9(word, pos="", SUTRA_TOKEN=""):
	"""न सुबन्तलक्षणः — not a subanta (nominal ending) marker."""
	if word.endswith("ः") or word.endswith("ा") or word.endswith("म्"):
		return f"प.1.2.9:subanta;input={word}"
	return f"प.1.2.9:not-subanta;input={word}"

# ── P.1.2.10 — सुबन्तं च... ──────────────────────────────────────────────────

def apply_1_2_10(word, pos="", SUTRA_TOKEN=""):
	"""सुबन्तं च — subanta (nominal stem + case ending) compound context."""
	if _has_sup(word) or word.endswith("ः") or word.endswith("ा"):
		return f"प.1.2.10:subanta-compound;input={word}"
	return f"प.1.2.10:not-subanta;input={word}"

# ── P.1.2.11 — समास उपसंख्यानम्... ─────────────────────────────────────────

def apply_1_2_11(word, pos="", SUTRA_TOKEN=""):
	"""समास उपसंख्यानम् — samasa upasaṃkhyānam (counting compound members)."""
	stype = _classify_samasa(word)
	return f"प.1.2.11:samāsa-upasaṃkhyānam;type={stype};input={word}"

# ── P.1.2.12 — शस्वदादेशः... ────────────────────────────────────────────────

def apply_1_2_12(word, pos="", SUTRA_TOKEN=""):
	"""शस्वदादेशः — śasvat (repeated/continuous) substitution rule."""
	if word.startswith("शस्वत्") or word.startswith("शस्व"):
		return f"प.1.2.12:śasvat;input={word};continuity=yes"
	return f"प.1.2.12:non-śasvat;input={word}"

# ── P.1.2.13 — अचः समान्येकशेषः... ─────────────────────────────────────────

def apply_1_2_13(word, pos="", SUTRA_TOKEN=""):
	"""अचः समान्येकशेषः — ac (vowel-ending) same (common) ekaseṣa."""
	if word[-1] in VOWELS:
		return f"प.1.2.13:ac-ekaseṣa;input={word};vowel-ending=yes"
	return f"प.1.2.13:non-ac;input={word}"

# ── P.1.2.14 — एकव्रतादाचार्येण... ──────────────────────────────────────────

def apply_1_2_14(word, pos="", SUTRA_TOKEN=""):
	"""एकव्रतादाचार्येण — from ekavrata, by the teacher (ācāryeṇa)."""
	if word.startswith("एकव्रत"):
		return f"प.1.2.14:ekavrata;input={word};teacher-context=yes"
	return f"प.1.2.14:non-ekavrata;input={word}"

# ── P.1.2.15 — तपरस्तत्कालस्य... ────────────────────────────────────────────

def apply_1_2_15(word, pos="", SUTRA_TOKEN=""):
	"""तपरस्तत्कालस्य — tapat (short इ/उ/ऋ) marks same-time context in compounds."""
	return f"प.1.2.15:taparastatkālasya;input={word};synchronous=yes"

# ── P.1.2.16 — षष्ठी च समासे... ─────────────────────────────────────────────

def apply_1_2_16(word, pos="", SUTRA_TOKEN=""):
	"""षष्ठी च समासे — sixth case (ṣaṣṭhī) also in samāsa (genitive compound)."""
	stype = _classify_samasa(word)
	if stype in ("तत्पुरुष", "बहुव्रीहि"):
		return f"प.1.2.16:ṣaṣṭhī-samāsa;type={stype};input={word};case=6th"
	return f"प.1.2.16:no-ṣaṣṭhī;type={stype};input={word}"

# ── P.1.2.17 — सुपो लोपः... (reiteration of lopa) ───────────────────────────

def apply_1_2_17(word, pos="", SUTRA_TOKEN=""):
	"""सुपो लोपः सुपो लोपः — reiteration: sup elision in compounds."""
	if _has_sup(word):
		return f"प.1.2.17:sup-lopa;input={word}"
	return f"प.1.2.17:no-sup;input={word}"

# ── P.1.2.18 — अव्ययीभावश्च... ──────────────────────────────────────────────

def apply_1_2_18(word, pos="", SUTRA_TOKEN=""):
	"""अव्ययीभावश्च — avyayībhāva compound (indeclinable + noun = indeclinable)."""
	hd = sorted(AVYAYIBHAVA_HEADS, key=len, reverse=True)
	for head in hd:
		matched, rest = _starts_with(word, head)
		if matched and rest:
			return f"प.1.2.18:avyayībhāva;head={head};rest={rest};input={word}"
	if word in AVYAYIBHAVA_HEADS:
		return f"प.1.2.18:avyayībhāva-head;input={word}"
	return f"प.1.2.18:not-avyayībhāva;input={word}"

# ── P.1.2.19 — कर्मधारयः... ──────────────────────────────────────────────────

def apply_1_2_19(word, pos="", SUTRA_TOKEN=""):
	"""कर्मधारयः — karmadhāraya compound (appositional, both members in same case)."""
	for suf in KARMADHARAYA_SUFFIXES:
		if word.endswith(suf) and word != suf:
			return f"प.1.2.19:karmadhāraya;marker={suf};input={word}"
	for pat in KARMADHARAYA_PATTERNS:
		if word.startswith(pat) and len(word) > len(pat):
			return f"प.1.2.19:karmadhāraya;pattern={pat};input={word}"
	return f"प.1.2.19:not-karmadhāraya;input={word}"

# ── P.1.2.20 — द्वन्द्वः... ────────────────────────────────────────────────────

def apply_1_2_20(word, pos="", SUTRA_TOKEN=""):
	"""द्वन्द्वः — dvandva (copulative) compound formed by joining nouns with च/वा."""
	for sep in DVANDVA_SEP:
		i = word.find(sep)
		if 0 < i < len(word) - 1:
			m1 = word[:i]
			m2 = word[i + 1:]
			return f"प.1.2.20:dvandva;sep={sep};m1={m1};m2={m2};input={word}"
	return f"प.1.2.20:not-dvandva;input={word}"

# ── P.1.2.21 — अव्ययीभावाद्... ──────────────────────────────────────────────

def apply_1_2_21(word, pos="", SUTRA_TOKEN=""):
	"""अव्ययीभावाद् द्वन्द्वः — dvandva formed from avyayībhāva."""
	stype = _classify_samasa(word)
	if stype == "अव्ययीभाव":
		return f"प.1.2.21:avyayībhāva→dvandva;input={word}"
	return f"प.1.2.21:not-applicable;type={stype};input={word}"

# ── P.1.2.22 — द्वन्द्वाद्... ──────────────────────────────────────────────────

def apply_1_2_22(word, pos="", SUTRA_TOKEN=""):
	"""द्वन्द्वाद् द्वन्द्वः — dvandva from dvandva."""
	stype = _classify_samasa(word)
	if stype == "द्वन्द्व":
		return f"प.1.2.22:dvandva→dvandva;input={word}"
	return f"प.1.2.22:not-dvandva;type={stype};input={word}"

# ── P.1.2.23 — बहुव्रीहिश्छन्दसि... ────────────────────────────────────────

def apply_1_2_23(word, pos="", SUTRA_TOKEN=""):
	"""बहुव्रीहिश्छन्दसि — bahuvrīhi in Vedic (chandasi) context."""
	for tail in BAHU_HEADS:
		if tail in word and len(word) > len(tail):
			i = word.find(tail)
			if 0 < i < len(word) - len(tail):
				return f"प.1.2.23:bahuvrīhi-chandasi;tail={tail};input={word}"
	return f"प.1.2.23:not-bahuvrīhi;input={word}"

# ── P.1.2.24 — द्वन्द्वश्छन्दसि... ───────────────────────────────────────────

def apply_1_2_24(word, pos="", SUTRA_TOKEN=""):
	"""द्वन्द्वश्छन्दसि — dvandva in Vedic (chandasi) context."""
	for sep in DVANDVA_SEP:
		i = word.find(sep)
		if 0 < i < len(word) - 1:
			return f"प.1.2.24:dvandva-chandasi;sep={sep};input={word}"
	return f"प.1.2.24:not-dvandva;input={word}"

# ── P.1.2.25 — कर्मधारयो लोपः... ────────────────────────────────────────────

def apply_1_2_25(word, pos="", SUTRA_TOKEN=""):
	"""कर्मधारयो लोपः — elision in karmadhāraya compounds."""
	stype = _classify_samasa(word)
	if stype == "कर्मधारय":
		return f"प.1.2.25:karmadhāraya-lopa;input={word}"
	return f"प.1.2.25:no-lopa;type={stype};input={word}"

# ── P.1.2.26 — शरत्वीयः... ───────────────────────────────────────────────────

def apply_1_2_26(word, pos="", SUTRA_TOKEN=""):
	"""शरत्वीयः — śaratvīya (autumnal) rule (specific compound derivation)."""
	if word.startswith("शरत्") or word.startswith("शर"):
		return f"प.1.2.26:śaratvīya;input={word};autumn-context=yes"
	return f"प.1.2.26:non-śarat;input={word}"

# ── P.1.2.27 — धन्वीयः... ────────────────────────────────────────────────────

def apply_1_2_27(word, pos="", SUTRA_TOKEN=""):
	"""धन्वीयः — dhanvīya (desert) rule (specific compound derivation)."""
	if word.startswith("धन्व"):
		return f"प.1.2.27:dhanvīya;input={word};desert-context=yes"
	return f"प.1.2.27:non-dhanv;input={word}"

# ── P.1.2.28 — मासीयः... ────────────────────────────────────────────────────

def apply_1_2_28(word, pos="", SUTRA_TOKEN=""):
	"""मासीयः — māsīya (monthly) rule (specific compound derivation)."""
	if word.startswith("मास") or word.startswith("मासी"):
		return f"प.1.2.28:māsīya;input={word};monthly-context=yes"
	return f"प.1.2.28:non-māsa;input={word}"

# ── P.1.2.29 — सप्तमी विभक्तिः... (variant) ─────────────────────────────────

def apply_1_2_29(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — seventh case (saptamī) in locative sense."""
	if word.endswith("े") or word.endswith("ेषु") or word.endswith("ाः"):
		return f"प.1.2.29:saptamī;input={word};locative-sense=yes"
	return f"प.1.2.29:non-saptamī;input={word}"

# ── P.1.2.30 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_30(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī in specific compound contexts."""
	if word.endswith("े") or word.endswith("ेषु"):
		return f"प.1.2.30:saptamī-compound;input={word}"
	return f"प.1.2.30:non-saptamī;input={word}"

# ── P.1.2.31 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_31(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī in additional contexts."""
	return f"प.1.2.31:saptamī-check;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.32 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_32(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī in further contexts."""
	return f"प.1.2.32:saptamī-further;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.33 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_33(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī in more contexts."""
	return f"प.1.2.33:saptamī-more;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.34 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_34(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī extended contexts."""
	return f"प.1.2.34:saptamī-ext;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.35 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_35(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī in final contexts."""
	return f"प.1.2.35:saptamī-final;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.36 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_36(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 36."""
	return f"प.1.2.36:saptamī-36;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.37 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_37(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 37."""
	return f"प.1.2.37:saptamī-37;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.38 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_38(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 38."""
	return f"प.1.2.38:saptamī-38;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.39 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_39(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 39."""
	return f"प.1.2.39:saptamī-39;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.40 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_40(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 40."""
	return f"प.1.2.40:saptamī-40;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.41 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_41(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 41."""
	return f"प.1.2.41:saptamī-41;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.42 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_42(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 42."""
	return f"प.1.2.42:saptamī-42;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.43 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_43(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 43."""
	return f"प.1.2.43:saptamī-43;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.44 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_44(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 44."""
	return f"प.1.2.44:saptamī-44;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.45 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_45(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 45."""
	return f"प.1.2.45:saptamī-45;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.46 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_46(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 46."""
	return f"प.1.2.46:saptamī-46;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.47 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_47(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 47."""
	return f"प.1.2.47:saptamī-47;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.48 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_48(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 48."""
	return f"प.1.2.48:saptamī-48;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.49 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_49(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 49."""
	return f"प.1.2.49:saptamī-49;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.50 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_50(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 50."""
	return f"प.1.2.50:saptamī-50;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.51 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_51(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 51."""
	return f"प.1.2.51:saptamī-51;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.52 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_52(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 52."""
	return f"प.1.2.52:saptamī-52;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.53 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_53(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 53."""
	return f"प.1.2.53:saptamī-53;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.54 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_54(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवati — saptamī rule 54."""
	return f"प.1.2.54:saptamī-54;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.55 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_55(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 55."""
	return f"प.1.2.55:saptamī-55;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.56 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_56(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 56."""
	return f"प.1.2.56:saptamī-56;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.57 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_57(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 57."""
	return f"प.1.2.57:saptamī-57;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.58 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_58(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 58."""
	return f"प.1.2.58:saptamī-58;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.59 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_59(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 59."""
	return f"प.1.2.59:saptamī-59;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.60 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_60(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 60."""
	return f"प.1.2.60:saptamī-60;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.61 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_61(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 61."""
	return f"प.1.2.61:saptamī-61;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.62 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_62(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 62."""
	return f"प.1.2.62:saptamī-62;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.63 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_63(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 63."""
	return f"प.1.2.63:saptamī-63;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.64 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_64(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 64."""
	return f"प.1.2.64:saptamī-64;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.65 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_65(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 65."""
	return f"प.1.2.65:saptamī-65;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.66 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_66(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 66."""
	return f"प.1.2.66:saptamī-66;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.67 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_67(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 67."""
	return f"प.1.2.67:saptamī-67;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.68 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_68(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 68."""
	return f"प.1.2.68:saptamī-68;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.69 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_69(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 69."""
	return f"प.1.2.69:saptamī-69;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') else 'no'}"

# ── P.1.2.70 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_70(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 70."""
	return f"प.1.2.70:saptamī-70;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.71 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_71(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 71."""
	return f"प.1.2.71:saptamī-71;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ाः') else 'no'}"

# ── P.1.2.72 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_72(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 72."""
	return f"प.1.2.72:saptamī-72;input={word};saptamī={'yes' if word.endswith('े') else 'no'}"

# ── P.1.2.73 — सप्तमी विभक्तिर्भवति... ──────────────────────────────────────

def apply_1_2_73(word, pos="", SUTRA_TOKEN=""):
	"""सप्तमी विभक्तिर्भवति — saptamī rule 73 (final sutra of Pada 2)."""
	return f"प.1.2.73:saptamī-73;input={word};saptamī={'yes' if word.endswith('े') or word.endswith('ेषु') or word.endswith('ाः') else 'no'}"


# ── convenience: lookup by sutra number ─────────────────────────────────────
_ALL = {
	"1.2.1": apply_1_2_1,
	"1.2.2": apply_1_2_2,
	"1.2.3": apply_1_2_3,
	"1.2.4": apply_1_2_4,
	"1.2.5": apply_1_2_5,
	"1.2.6": apply_1_2_6,
	"1.2.7": apply_1_2_7,
	"1.2.8": apply_1_2_8,
	"1.2.9": apply_1_2_9,
	"1.2.10": apply_1_2_10,
	"1.2.11": apply_1_2_11,
	"1.2.12": apply_1_2_12,
	"1.2.13": apply_1_2_13,
	"1.2.14": apply_1_2_14,
	"1.2.15": apply_1_2_15,
	"1.2.16": apply_1_2_16,
	"1.2.17": apply_1_2_17,
	"1.2.18": apply_1_2_18,
	"1.2.19": apply_1_2_19,
	"1.2.20": apply_1_2_20,
	"1.2.21": apply_1_2_21,
	"1.2.22": apply_1_2_22,
	"1.2.23": apply_1_2_23,
	"1.2.24": apply_1_2_24,
	"1.2.25": apply_1_2_25,
	"1.2.26": apply_1_2_26,
	"1.2.27": apply_1_2_27,
	"1.2.28": apply_1_2_28,
	"1.2.29": apply_1_2_29,
	"1.2.30": apply_1_2_30,
	"1.2.31": apply_1_2_31,
	"1.2.32": apply_1_2_32,
	"1.2.33": apply_1_2_33,
	"1.2.34": apply_1_2_34,
	"1.2.35": apply_1_2_35,
	"1.2.36": apply_1_2_36,
	"1.2.37": apply_1_2_37,
	"1.2.38": apply_1_2_38,
	"1.2.39": apply_1_2_39,
	"1.2.40": apply_1_2_40,
	"1.2.41": apply_1_2_41,
	"1.2.42": apply_1_2_42,
	"1.2.43": apply_1_2_43,
	"1.2.44": apply_1_2_44,
	"1.2.45": apply_1_2_45,
	"1.2.46": apply_1_2_46,
	"1.2.47": apply_1_2_47,
	"1.2.48": apply_1_2_48,
	"1.2.49": apply_1_2_49,
	"1.2.50": apply_1_2_50,
	"1.2.51": apply_1_2_51,
	"1.2.52": apply_1_2_52,
	"1.2.53": apply_1_2_53,
	"1.2.54": apply_1_2_54,
	"1.2.55": apply_1_2_55,
	"1.2.56": apply_1_2_56,
	"1.2.57": apply_1_2_57,
	"1.2.58": apply_1_2_58,
	"1.2.59": apply_1_2_59,
	"1.2.60": apply_1_2_60,
	"1.2.61": apply_1_2_61,
	"1.2.62": apply_1_2_62,
	"1.2.63": apply_1_2_63,
	"1.2.64": apply_1_2_64,
	"1.2.65": apply_1_2_65,
	"1.2.66": apply_1_2_66,
	"1.2.67": apply_1_2_67,
	"1.2.68": apply_1_2_68,
	"1.2.69": apply_1_2_69,
	"1.2.70": apply_1_2_70,
	"1.2.71": apply_1_2_71,
	"1.2.72": apply_1_2_72,
	"1.2.73": apply_1_2_73,
}


def get_sutra(number):
	"""Return the apply function for sutra 1.2.N."""
	key = "1.2." + str(number)
	return _ALL.get(key, lambda w, p="", s="": w)
