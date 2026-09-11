# -*- coding: utf-8 -*-
"""P.8.1.x - Tripadi start: visarga, anusvara, final sandhi, imperative exceptions.
74 sutras: apply_8_1_1 .. apply_8_1_74
Sutra texts and descriptions gathered from existing P_8_1_N.py stubs.
"""

from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Devanagari constants
# ---------------------------------------------------------------------------
A = "अ"
AA = "आ"
I = "इ"
II = "ई"
U = "उ"
UU = "ऊ"
R = "ऋ"
RL = "ऌ"
E = "ए"
AI = "ऐ"
O = "ओ"
AU = "औ"
AH = "ः"

# ---------------------------------------------------------------------------
# Transliteration helpers (ASCII-safe)
# ---------------------------------------------------------------------------

def _to_ascii(s):
	"""Dev transliteration: diacritics for retroflex, guttural, palatal."""
	table = {
		"अ": "a", "आ": "A", "इ": "i", "ई": "I", "उ": "u", "ऊ": "U",
		"ऋ": ".r", "ॠ": ".R", "ऌ": ".l", "ए": "e", "ऐ": "ai",
		"ओ": "o", "औ": "au", "ं": "M", "ः": "H", "ँ": "~N",
		"क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "N",
		"च": "c", "छ": "ch", "ज": "j", "झ": "jh", "ञ": "J",
		"ट": ".t", "ठ": ".T", "ड": ".d", "ढ": ".D", "ण": ".N",
		"त": "t", "थ": "th", "द": "d", "ध": "dh", "न": "n",
		"प": "p", "फ": "ph", "ब": "b", "भ": "bh", "म": "m",
		"य": "y", "र": "r", "ल": "l", "व": "v",
		"श": "z", "ष": ".S", "स": "s", "ह": "h",
		"ा": "A", "ि": "i", "ी": "I", "ु": "u", "ू": "U",
		"ृ": ".r", "े": "e", "ै": "ai", "ो": "o", "ौ": "au",
		"्": "", "ँ": "~N", "ं": "M", "ः": "H", "ऽ": "'",
		" ": " ", "।": ".", "॥": "..",
	}
	result = []
	for ch in s:
		result.append(table.get(ch, ch))
	return "".join(result)


def _slug(s):
	"""Collapse ascii transliteration to a compact tag-safe slug."""
	t = _to_ascii(s).lower()
	t = re.sub(r"[^a-z0-9]", "-", t)
	t = re.sub(r"-+", "-", t).strip("-")
	return t


# ---------------------------------------------------------------------------
# Phonetic helpers
# ---------------------------------------------------------------------------

VOWELS_DEV = {A, AA, I, II, U, UU, R, RL, E, AI, O, AU}

CONSONANTS_DEV = set(
	"कखगघङचछजझञटठडढणतथदधनपफबभयरलवशषसह"
)

HAL_DEV = CONSONANTS_DEV

ALL_SOUNDS_DEV = VOWELS_DEV | CONSONANTS_DEV | {AH}


def _is_vowel_DEV(ch):
	return ch in VOWELS_DEV


def _is_consonant_DEV(ch):
	return ch in CONSONANTS_DEV


def _is_hal_DEV(ch):
	return ch in HAL_DEV


def _last_char_DEV(word):
	return word[-1] if word else ""


def _last2_DEV(word):
	return word[-2:] if len(word) >= 2 else word


def _last3_DEV(word):
	return word[-3:] if len(word) >= 3 else word


def _ends_visarga(word):
	return bool(word[-1] == AH)


def _ends_anusvara(word):
	return bool(word[-1] == "ं")


def _ends_hal(word):
	if not word:
		return False
	return _is_hal_DEV(word[-1]) or word[-1] == AH


def _ends_vowel(word):
	if not word:
		return False
	return _is_vowel_DEV(word[-1])


def _before_last(word):
	"""Return everything before the last character."""
	return word[:-1] if word else ""


def _split_first(word):
	"""Split word into (first_char, rest)."""
	if not word:
		return "", ""
	return word[0], word[1:]


def _replace_last(word, new_last):
	return _before_last(word) + new_last


# ---------------------------------------------------------------------------
# Core formatting helpers
# ---------------------------------------------------------------------------

def _fmt(tag, word, pos, extra=""):
	s = tag + ";input=" + word + ";pos=" + pos
	if extra:
		s += ";" + extra
	return s


def _fmt_ok(tag, result, word, pos, detail=""):
	s = tag + ";result=" + result + ";input=" + word + ";pos=" + pos
	if detail:
		s += ";" + detail
	return s


def _fmt_none(tag, word, pos):
	return tag + ";no-change;input=" + word + ";pos=" + pos


# ---------------------------------------------------------------------------
# P.8.1 processing context
# ---------------------------------------------------------------------------
# P.8.1 deals with word-final changes before suffix attachment.
# The key context is: what suffix follows (the "uttara" or "paras").

def _context_visarga(word):
	"""Return the visarga-related context for a word."""
	if not _ends_visarga(word):
		return {"visarga": False}
	stem = word[:-1]
	return {
		"visarga": True,
		"stem": stem,
		"original": word,
	}


def _context_anusvara(word):
	"""Return the anusvara context for a word."""
	if not _ends_anusvara(word):
		return {"anusvara": False}
	stem = word[:-1]
	return {
		"anusvara": True,
		"stem": stem,
		"original": word,
	}


# ---------------------------------------------------------------------------
# Sutra registry
# ---------------------------------------------------------------------------

_SUTRA_TEXTS = {
	1: ("सर्वस्य द्वे", "visarga doubled before vowels (general)"),
	2: ("तस्य परमाम्रेडितम्", "reduplicated param prefix"),
	3: ("अनुदात्तं च", "n -> ng before ng-i suffixes"),
	4: ("नित्यवीप्सयोः", "m -> anusvara in nitya/vipsa"),
	5: ("परेर्वर्जने", "visarga omission before consonants"),
	6: ("प्रसमुपोदः पादपूरणे", "elision of visarga in pr/sam/up/ud"),
	7: ("उपर्यध्यधसः सामीप्ये", "visarga in proximity terms"),
	8: ("वाक्यादेरामन्त्रितस्यासूयासम्मतिकोपकुत्सनभर्त्सनेषु", "visarga rule in vocative/negative contexts"),
	9: ("एकं बहुव्रीहिवत्", "single form like bahuvrihi"),
	10: ("आबाधे च", "visarga in abadhe (hindrance)"),
	11: ("कर्मधारयवत् उत्तरेषु", "karmadharaya pattern in uttara"),
	12: ("प्रकारे गुणवचनस्य", "guna-vacana in prakara"),
	13: ("अकृच्छ्रे प्रियसुखयोरन्यतरस्याम्", "optional in not-difficult, pleasant contexts"),
	14: ("यथास्वे यथायथम्", "visarga in yatha-sve/yatha-yatham"),
	15: ("द्वन्द्वं रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्रप्रयोगाभिव्यक्तिषु", "dvivandva visarga"),
	16: ("पदस्य", "visarga at pada boundary"),
	17: ("पदात्", "visarga from pada"),
	18: ("अनुदात्तं सर्वमपादादौ", "anudatta forms at pada-adi"),
	19: ("आमन्त्रितस्य च", "visarga in amantrita (vocative)"),
	20: ("युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ", "yushmad-asmad -> vaan/nnau"),
	21: ("बहुवचनस्य वस्नसौ", "plural -vas/-nas"),
	22: ("तेमयावेकवचनस्य", "te/maya for singular"),
	23: ("त्वामौ द्वितीयायाः", "tvaam in dual second"),
	24: ("न चवाहाहैवयुक्ते", "no ca/vaaha/hai in compounds"),
	25: ("पश्यार्थैश्चानालोचने", "pashya-artha before analocane"),
	26: ("सपूर्वायाः प्रथमाया विभाषा", "vibhasha with sapurva prathama"),
	27: ("तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः", "ting gotra-adi in kutsana/abhikshnya"),
	28: ("तिङ्ङतिङः", "ting-ng-ting"),
	29: ("न लुट्", "not lut"),
	30: ("निपातैर्यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्रयुक्तम्", "nipata with yad/yadi/ihan"),
	31: ("नह प्रत्यारम्भे", "nah in pratyarambhe"),
	32: ("सत्यं प्रश्ने", "satyam in prashne"),
	33: ("अङ्गाप्रातिलोम्ये", "anga-apratilomye"),
	34: ("हि च", "hi cha"),
	35: ("छन्दस्यनेकमपि साकाङ्क्षम्", "chandasi anekam api sakankksham"),
	36: ("यावद्यथाभ्याम्", "yavad-yatha"),
	37: ("पूजायां नानन्तरम्", "pujayam na-anantaram"),
	38: ("उपसर्गव्यपेतं च", "upasarga-vyapeta cha"),
	39: ("तुपश्यपश्यताहैः पूजायाम्", "tu/pashya/pashyatahai in pujayam"),
	40: ("अहो च", "aho cha"),
	41: ("शेषे विभाषा", "sheshe vibhasha"),
	42: ("पुरा च परीप्सायाम्", "pura cha paripsayam"),
	43: ("नन्वित्यनुज्ञैषणायाम्", "nanvi ty-anujnaishana"),
	44: ("किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम्", "kim in kriya-prashne"),
	45: ("लोपे विभाषा", "lope vibhasha"),
	46: ("एहिमन्ये प्रहासे लृट्", "ehimanye prahase l.rt"),
	47: ("जात्वपूर्वम्", "jatvapurvam"),
	48: ("किम्वृत्तं च चिदुत्तरम्", "kimvrittam cha cid-uttaram"),
	49: ("आहो उताहो चानन्तरम्", "aho utaho cha-anantaram"),
	50: ("शेषे विभाषा", "seshe vibhasha"),
	51: ("गत्यर्थलोटा लृण्न चेत् कारकं सर्वान्यत्", "gatyartha-lota l.rn cet karakam"),
	52: ("लोट् च", "lot cha"),
	53: ("विभाषितं सोपसर्गमनुत्तमम्", "vibhashitam sopasargam-anuttamam"),
	54: ("हन्त च", "hanta cha"),
	55: ("आम एकान्तरमामन्त्रितमनन्तिके", "ama eka-antaram-amantritam-anantike"),
	56: ("यद्धितुपरं छन्दसि", "yaddhituparam chandas"),
	57: ("चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः", "cana-cid-iva gotradi taddhita-amreditesh"),
	58: ("चादिषु च", "cadishu cha"),
	59: ("चवायोगे प्रथमा", "cava-yoge prathama"),
	60: ("हेति क्षियायाम्", "heti kshiyayam"),
	61: ("अहेति विनियोगे च", "aheti viniyoge cha"),
	62: ("चाहलोप एवेत्यवधारणम्", "ca-halopa evety-avadharanam"),
	63: ("चादिलोपे विभाषा", "cadi-lope vibhasha"),
	64: ("वैवावेति च च्छन्दसि", "vaivaveti cha chandas"),
	65: ("एकान्याभ्यां समर्थाभ्याम्", "eka-anyabhyam samarthabhyam"),
	66: ("यद्वृत्तान्नित्यं", "yadvrttan-nityam"),
	67: ("पूजनात् पूजितमनुदात्तं काष्ठादिभ्यः", "pujanat pujitam-anudattam kasthadibhyah"),
	68: ("सगतिरपि तिङ्", "sagatirapi ting"),
	69: ("कुत्सने च सुप्यगोत्रादौ", "kutsane cha supy-agotradi"),
	70: ("गतिर्गतौ", "gatir-gatau"),
	71: ("तिङि चोदात्तवति", "tingi cha udattavati"),
	72: ("आमन्त्रितं पूर्वमविद्यमानवत्", "amantritam purvam-avidymanavat"),
	73: ("नामन्त्रिते समानाधिकरणे सामान्यवचनम्", "namantrite samanadhikarane samanyavachanam"),
	74: ("विभाषितं विशेषवचने बहुवचनम्", "vibhashitam visheshavachane bahuvachanam"),
}


# ===================================================================
# P.8.1 - 74 sutra functions
# ===================================================================

def apply_8_1_1(word, pos="", SUTRA_TOKEN=""):
	"""सर्वस्य द्वे - Every final becomes double (before vowel-initial suffix)."""
	tag = "p81-001:" + _slug(_SUTRA_TEXTS[1][0])
	if not word:
		return _fmt(tag, word, pos)
	last = _last_char_DEV(word)
	if last == AH:
		result = _before_last(word) + "स्"
		return _fmt_ok(tag, result, word, pos, "dve:visarga->sa")
	return _fmt_none(tag, word, pos)


def apply_8_1_2(word, pos="", SUTRA_TOKEN=""):
	"""तस्य परमाम्रेडितम् - Reduplication of param before this."""
	tag = "p81-002:" + _slug(_SUTRA_TEXTS[2][0])
	if "पर" in word:
		return _fmt_ok(tag, word, word, pos, "amredita-param")
	return _fmt_none(tag, word, pos)


def apply_8_1_3(word, pos="", SUTRA_TOKEN=""):
	"""अनुदात्तं च - n becomes ng before ng-i endings."""
	tag = "p81-003:" + _slug(_SUTRA_TEXTS[3][0])
	if word.endswith("न्"):
		stem = word[:-2]
		return _fmt_ok(tag, stem + "ङ्", word, pos, "na->nga before ng-i")
	return _fmt_none(tag, word, pos)


def apply_8_1_4(word, pos="", SUTRA_TOKEN=""):
	"""नित्यवीप्सयोः - ngam replaced by hal in nitya/vipsa contexts."""
	tag = "p81-004:" + _slug(_SUTRA_TEXTS[4][0])
	if _ends_anusvara(word):
		stem = _before_last(word)
		return _fmt_ok(tag, stem + "म्", word, pos, "ngam->m nitya/vipsa")
	return _fmt_none(tag, word, pos)


def apply_8_1_5(word, pos="", SUTRA_TOKEN=""):
	"""परेर्वर्जने - Elision of visarga before consonants (parer)."""
	tag = "p81-005:" + _slug(_SUTRA_TEXTS[5][0])
	if _ends_visarga(word):
		stem = _before_last(word)
		return _fmt_ok(tag, stem, word, pos, "visarga-lopa before consonant")
	return _fmt_none(tag, word, pos)


def apply_8_1_6(word, pos="", SUTRA_TOKEN=""):
	"""प्रसमुपोदः पादपूरणे - Visarga elision in pra/sam/up/ud pada-purane."""
	tag = "p81-006:" + _slug(_SUTRA_TEXTS[6][0])
	prefixes = ("प्र", "सम", "उप", "उद")
	if any(word.startswith(p) for p in prefixes) and _ends_visarga(word):
		stem = _before_last(word)
		return _fmt_ok(tag, stem, word, pos, "visarga-lopa pra/sam/up/ud")
	return _fmt_none(tag, word, pos)


def apply_8_1_7(word, pos="", SUTRA_TOKEN=""):
	"""उपर्यध्यधसः सामीप्ये - Visarga in upari/adhy/adhas proximity."""
	tag = "p81-007:" + _slug(_SUTRA_TEXTS[7][0])
	proximity_terms = ("उपरि", "अधि", "अधस्")
	if any(word.startswith(t) for t in proximity_terms):
		return _fmt_ok(tag, word, word, pos, "proximity visarga rule")
	return _fmt_none(tag, word, pos)


def apply_8_1_8(word, pos="", SUTRA_TOKEN=""):
	"""वाक्यादेरामन्त्रितस्यासूयासम्मतिकोपकुत्सनभर्त्सनेषु - Visarga in vocative contexts."""
	tag = "p81-008:" + _slug(_SUTRA_TEXTS[8][0])
	contexts = ("आसूया", "सम्मति", "कुत्सन", "भर्त्सन")
	if _ends_visarga(word) and any(word.startswith(c) for c in ("वाक्य", "आमन्त्रित")):
		return _fmt_ok(tag, word, word, pos, "vocative-context visarga")
	return _fmt_none(tag, word, pos)


def apply_8_1_9(word, pos="", SUTRA_TOKEN=""):
	"""एकं बहुव्रीहिवत् - Single form like bahuvrihi compound."""
	tag = "p81-009:" + _slug(_SUTRA_TEXTS[9][0])
	return _fmt_ok(tag, word, word, pos, "ekaM bahuvrihi-vat")


def apply_8_1_10(word, pos="", SUTRA_TOKEN=""):
	"""आबाधे च - Visarga in abadhe (hindrance/obstruction)."""
	tag = "p81-010:" + _slug(_SUTRA_TEXTS[10][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "abadhe visarga")
	return _fmt_none(tag, word, pos)


def apply_8_1_11(word, pos="", SUTRA_TOKEN=""):
	"""कर्मधारयवत् उत्तरेषु - Karmadharaya pattern in uttara."""
	tag = "p81-011:" + _slug(_SUTRA_TEXTS[11][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "karmadharaya-vat visarga")
	return _fmt_none(tag, word, pos)


def apply_8_1_12(word, pos="", SUTRA_TOKEN=""):
	"""प्रकारे गुणवचनस्य - Visarga in prakara of guna-vachana."""
	tag = "p81-012:" + _slug(_SUTRA_TEXTS[12][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "prakare gunavachanasya")
	return _fmt_none(tag, word, pos)


def apply_8_1_13(word, pos="", SUTRA_TOKEN=""):
	"""अकृच्छ्रे प्रियसुखयोरन्यतरस्याम् - Optional in easy/pleasant contexts."""
	tag = "p81-013:" + _slug(_SUTRA_TEXTS[13][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "akricchre priyasukhayoH anyatarasyam")
	return _fmt_none(tag, word, pos)


def apply_8_1_14(word, pos="", SUTRA_TOKEN=""):
	"""यथास्वे यथायथम् - Visarga in yatha-sve/yatha-yatham."""
	tag = "p81-014:" + _slug(_SUTRA_TEXTS[14][0])
	if word.startswith("यथा"):
		return _fmt_ok(tag, word, word, pos, "yathasve yathayatham")
	return _fmt_none(tag, word, pos)


def apply_8_1_15(word, pos="", SUTRA_TOKEN=""):
	"""द्वन्द्वं रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्रप्रयोगाभिव्यक्तिषु - Dvivandva visarga."""
	tag = "p81-015:" + _slug(_SUTRA_TEXTS[15][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "dvandvam visarga contexts")
	return _fmt_none(tag, word, pos)


def apply_8_1_16(word, pos="", SUTRA_TOKEN=""):
	"""पदस्य - Visarga at pada boundary."""
	tag = "p81-016:" + _slug(_SUTRA_TEXTS[16][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "padasya visarga")
	return _fmt_none(tag, word, pos)


def apply_8_1_17(word, pos="", SUTRA_TOKEN=""):
	"""पदात् - Visarga from pada."""
	tag = "p81-017:" + _slug(_SUTRA_TEXTS[17][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "padat visarga")
	return _fmt_none(tag, word, pos)


def apply_8_1_18(word, pos="", SUTRA_TOKEN=""):
	"""अनुदात्तं सर्वमपादादौ - Anudatta at pada-adi."""
	tag = "p81-018:" + _slug(_SUTRA_TEXTS[18][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "anudattam sarvam apadadau")
	return _fmt_none(tag, word, pos)


def apply_8_1_19(word, pos="", SUTRA_TOKEN=""):
	"""आमन्त्रितस्य च - Visarga in amantrita (vocative)."""
	tag = "p81-019:" + _slug(_SUTRA_TEXTS[19][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "amantritasya cha")
	return _fmt_none(tag, word, pos)


def apply_8_1_20(word, pos="", SUTRA_TOKEN=""):
	"""युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ - yushmad/asmad: vaan/nnau."""
	tag = "p81-020:" + _slug(_SUTRA_TEXTS[20][0])
	if word.startswith("युष्म"):
		if word.startswith("युष्मद्"):
			return _fmt_ok(tag, "युष्मान्", word, pos, "yushmat->yushman")
		if word.startswith("युष्म"):
			return _fmt_ok(tag, "यूयं", word, pos, "yushmad->yuyam")
	if word.startswith("अस्म"):
		if word.startswith("अस्मद्"):
			return _fmt_ok(tag, "अस्मान्", word, pos, "asmat->asman")
		if word.startswith("अस्म"):
			return _fmt_ok(tag, "अहम्", word, pos, "asmad->aham")
	return _fmt_none(tag, word, pos)


def apply_8_1_21(word, pos="", SUTRA_TOKEN=""):
	"""बहुवचनस्य वस्नसौ - Plural: vas/nas endings."""
	tag = "p81-021:" + _slug(_SUTRA_TEXTS[21][0])
	if word.endswith("वः") or word.endswith("नः"):
		return _fmt_ok(tag, word, word, pos, "bahuvachan vas-nas")
	return _fmt_none(tag, word, pos)


def apply_8_1_22(word, pos="", SUTRA_TOKEN=""):
	"""तेमयावेकवचनस्य - te/maya for singular (sip)."""
	tag = "p81-022:" + _slug(_SUTRA_TEXTS[22][0])
	if "ते" in word or "मया" in word:
		return _fmt_ok(tag, word, word, pos, "te-maya ekavachana")
	return _fmt_none(tag, word, pos)


def apply_8_1_23(word, pos="", SUTRA_TOKEN=""):
	"""त्वामौ द्वितीयायाः - tvaam dual second."""
	tag = "p81-023:" + _slug(_SUTRA_TEXTS[23][0])
	if word == "त्वाम्":
		return _fmt_ok(tag, "त्वाम्", word, pos, "tvaam dual 2nd")
	return _fmt_none(tag, word, pos)


def apply_8_1_24(word, pos="", SUTRA_TOKEN=""):
	"""न चवाहाहैवयुक्ते - No ca/vaaha/hai in compounds."""
	tag = "p81-024:" + _slug(_SUTRA_TEXTS[24][0])
	if any(x in word for x in ("च", "वाह", "हैव")):
		return _fmt_ok(tag, word, word, pos, "na-cavaaha-hai yukte")
	return _fmt_none(tag, word, pos)


def apply_8_1_25(word, pos="", SUTRA_TOKEN=""):
	"""पश्यार्थैश्चानालोचने - Pashya-artha before analocane."""
	tag = "p81-025:" + _slug(_SUTRA_TEXTS[25][0])
	if word.startswith("पश्य"):
		return _fmt_ok(tag, word, word, pos, "pashyarthaish analocane")
	return _fmt_none(tag, word, pos)


def apply_8_1_26(word, pos="", SUTRA_TOKEN=""):
	"""सपूर्वायाः प्रथमाया विभाषा - Vibhasha with sapurva prathama."""
	tag = "p81-026:" + _slug(_SUTRA_TEXTS[26][0])
	if "सपूर्व" in word.startswith("स"):
		return _fmt_ok(tag, word, word, pos, "sapurvayah prathamaya vibhasha")
	return _fmt_none(tag, word, pos)


def apply_8_1_27(word, pos="", SUTRA_TOKEN=""):
	"""तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः - Ting gotra-adi in kutsana/abhikshnya."""
	tag = "p81-027:" + _slug(_SUTRA_TEXTS[27][0])
	if word.startswith("त"):
		return _fmt_ok(tag, word, word, pos, "tingo gotradi kutsanabhikshnyayoh")
	return _fmt_none(tag, word, pos)


def apply_8_1_28(word, pos="", SUTRA_TOKEN=""):
	"""तिङ्ङतिङः - Ting-ng-ting (suffix interchange)."""
	tag = "p81-028:" + _slug(_SUTRA_TEXTS[28][0])
	if word.startswith("तिङ"):
		return _fmt_ok(tag, word, word, pos, "ting-ng-ting")
	return _fmt_none(tag, word, pos)


def apply_8_1_29(word, pos="", SUTRA_TOKEN=""):
	"""न लुट् - No luT (periphrastic perfect) in this context."""
	tag = "p81-029:" + _slug(_SUTRA_TEXTS[29][0])
	return _fmt_ok(tag, word, word, pos, "na lut")


def apply_8_1_30(word, pos="", SUTRA_TOKEN=""):
	"""निपातैर्यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्रयुक्तम् - Nipata with yad/yadi etc."""
	tag = "p81-030:" + _slug(_SUTRA_TEXTS[30][0])
	nipatas = ("यत्", "यदि", "इह", "अन्त", "कु", "विन्", "एव", "च", "चन्", "क", "चित्", "यत्र")
	if any(word.startswith(n) for n in nipatas):
		return _fmt_ok(tag, word, word, pos, "nipata yad-yadi-ihan")
	return _fmt_none(tag, word, pos)


def apply_8_1_31(word, pos="", SUTRA_TOKEN=""):
	"""नह प्रत्यारम्भे - nah in pratyarambhe (re-attempt)."""
	tag = "p81-031:" + _slug(_SUTRA_TEXTS[31][0])
	if word == "नह्" or word.startswith("नह"):
		return _fmt_ok(tag, word, word, pos, "nah pratyarambhe")
	return _fmt_none(tag, word, pos)


def apply_8_1_32(word, pos="", SUTRA_TOKEN=""):
	"""सत्यं प्रश्ने - Satyam in prashne (question)."""
	tag = "p81-032:" + _slug(_SUTRA_TEXTS[32][0])
	if word.startswith("सत्य"):
		return _fmt_ok(tag, word, word, pos, "satyam prashne")
	return _fmt_none(tag, word, pos)


def apply_8_1_33(word, pos="", SUTRA_TOKEN=""):
	"""अङ्गाप्रातिलोम्ये - Anga-apratilomye (not opposite order)."""
	tag = "p81-033:" + _slug(_SUTRA_TEXTS[33][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "anga-apratilomye")
	return _fmt_none(tag, word, pos)


def apply_8_1_34(word, pos="", SUTRA_TOKEN=""):
	"""हि च - hi cha (indeed, also)."""
	tag = "p81-034:" + _slug(_SUTRA_TEXTS[34][0])
	if word.startswith("हि"):
		return _fmt_ok(tag, word, word, pos, "hi cha")
	return _fmt_none(tag, word, pos)


def apply_8_1_35(word, pos="", SUTRA_TOKEN=""):
	"""छन्दस्यनेकमपि साकाङ्क्षम् - Chando-si anekam api sakankksham."""
	tag = "p81-035:" + _slug(_SUTRA_TEXTS[35][0])
	if word.startswith("छन्द"):
		return _fmt_ok(tag, word, word, pos, "chandasi anekam api sakankksham")
	return _fmt_none(tag, word, pos)


def apply_8_1_36(word, pos="", SUTRA_TOKEN=""):
	"""यावद्यथाभ्याम् - yavad-yatha (as-much-as / as)."""
	tag = "p81-036:" + _slug(_SUTRA_TEXTS[36][0])
	if word.startswith("यावत्") or word.startswith("यथा"):
		return _fmt_ok(tag, word, word, pos, "yavad-yathabhyam")
	return _fmt_none(tag, word, pos)


def apply_8_1_37(word, pos="", SUTRA_TOKEN=""):
	"""पूजायां नानन्तरम् - No anantaram in pujayam."""
	tag = "p81-037:" + _slug(_SUTRA_TEXTS[37][0])
	if "पूजा" in word:
		return _fmt_ok(tag, word, word, pos, "pujayam na-anantaram")
	return _fmt_none(tag, word, pos)


def apply_8_1_38(word, pos="", SUTRA_TOKEN=""):
	"""उपसर्गव्यपेतं च - Upasarga-vyapeta (without prefix) also."""
	tag = "p81-038:" + _slug(_SUTRA_TEXTS[38][0])
	return _fmt_ok(tag, word, word, pos, "upasarga-vyapetam cha")


def apply_8_1_39(word, pos="", SUTRA_TOKEN=""):
	"""तुपश्यपश्यताहैः पूजायाम् - tu/pashya/pashyatahai in pujayam."""
	tag = "p81-039:" + _slug(_SUTRA_TEXTS[39][0])
	if word.startswith(("तु", "पश्य", "पश्यत")):
		return _fmt_ok(tag, word, word, pos, "tupashyapashyatahaih pujayam")
	return _fmt_none(tag, word, pos)


def apply_8_1_40(word, pos="", SUTRA_TOKEN=""):
	"""अहो च - aho cha (oh / alas)."""
	tag = "p81-040:" + _slug(_SUTRA_TEXTS[40][0])
	if word.startswith("अहो"):
		return _fmt_ok(tag, word, word, pos, "aho cha")
	return _fmt_none(tag, word, pos)


def apply_8_1_41(word, pos="", SUTRA_TOKEN=""):
	"""शेषे विभाषा - Vibhasha in sesha (remaining) cases."""
	tag = "p81-041:" + _slug(_SUTRA_TEXTS[41][0])
	return _fmt_ok(tag, word, word, pos, "seshe vibhasha")


def apply_8_1_42(word, pos="", SUTRA_TOKEN=""):
	"""पुरा च परीप्सायाम् - Pura cha paripsayam (desire to precede)."""
	tag = "p81-042:" + _slug(_SUTRA_TEXTS[42][0])
	if word.startswith("पुरा"):
		return _fmt_ok(tag, word, word, pos, "pura cha paripsayam")
	return _fmt_none(tag, word, pos)


def apply_8_1_43(word, pos="", SUTRA_TOKEN=""):
	"""नन्वित्यनुज्ञैषणायाम् - nanvi in anujnaishana (permission seeking)."""
	tag = "p81-043:" + _slug(_SUTRA_TEXTS[43][0])
	if word.startswith("नन्व"):
		return _fmt_ok(tag, word, word, pos, "nanvi ty-anujnaishanayam")
	return _fmt_none(tag, word, pos)


def apply_8_1_44(word, pos="", SUTRA_TOKEN=""):
	"""किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम् - kim in kriya-prashne without upasarga."""
	tag = "p81-044:" + _slug(_SUTRA_TEXTS[44][0])
	if word == "किं" or word.startswith("कि"):
		return _fmt_ok(tag, word, word, pos, "kim kriya-prashne anupasargam")
	return _fmt_none(tag, word, pos)


def apply_8_1_45(word, pos="", SUTRA_TOKEN=""):
	"""लोपे विभाषा - Vibhasha in lopa (elision)."""
	tag = "p81-045:" + _slug(_SUTRA_TEXTS[45][0])
	return _fmt_ok(tag, word, word, pos, "lope vibhasha")


def apply_8_1_46(word, pos="", SUTRA_TOKEN=""):
	"""एहिमन्ये प्रहासे लृट् - ehimarye prahase l.rt (sarcastic past)."""
	tag = "p81-046:" + _slug(_SUTRA_TEXTS[46][0])
	if word.startswith("एहि"):
		return _fmt_ok(tag, word, word, pos, "ehimanye prahase lrt")
	return _fmt_none(tag, word, pos)


def apply_8_1_47(word, pos="", SUTRA_TOKEN=""):
	"""जात्वपूर्वम् - jatva-purvam (indeed + previously)."""
	tag = "p81-047:" + _slug(_SUTRA_TEXTS[47][0])
	if word.startswith("जातु"):
		return _fmt_ok(tag, word, word, pos, "jatvapurvam")
	return _fmt_none(tag, word, pos)


def apply_8_1_48(word, pos="", SUTRA_TOKEN=""):
	"""किम्वृत्तं च चिदुत्तरम् - kimvrittam cha cid-uttaram."""
	tag = "p81-048:" + _slug(_SUTRA_TEXTS[48][0])
	if word.startswith("किम्वृत्त"):
		return _fmt_ok(tag, word, word, pos, "kimvrittam cha cid-uttaram")
	return _fmt_none(tag, word, pos)


def apply_8_1_49(word, pos="", SUTRA_TOKEN=""):
	"""आहो उताहो चानन्तरम् - aho/utaho not consecutive."""
	tag = "p81-049:" + _slug(_SUTRA_TEXTS[49][0])
	if word.startswith("आहो") or word.startswith("उताहो"):
		return _fmt_ok(tag, word, word, pos, "aho utaho cha-anantaram")
	return _fmt_none(tag, word, pos)


def apply_8_1_50(word, pos="", SUTRA_TOKEN=""):
	"""शेषे विभाषा - Vibhasha in remaining contexts."""
	tag = "p81-050:" + _slug(_SUTRA_TEXTS[50][0])
	return _fmt_ok(tag, word, word, pos, "seshe vibhasha")


def apply_8_1_51(word, pos="", SUTRA_TOKEN=""):
	"""गत्यर्थलोटा लृण्न चेत् कारकं सर्वान्यत् - gatyartha-lota l.rn cet karakam."""
	tag = "p81-051:" + _slug(_SUTRA_TEXTS[51][0])
	if pos == "verb" and "गति" in pos:
		return _fmt_ok(tag, word, word, pos, "gatyartha-lota l.rn cet karakam")
	return _fmt_none(tag, word, pos)


def apply_8_1_52(word, pos="", SUTRA_TOKEN=""):
	"""लोट् च - lot cha (imperative also)."""
	tag = "p81-052:" + _slug(_SUTRA_TEXTS[52][0])
	if pos == "verb-imperative" or word.endswith("तु"):
		return _fmt_ok(tag, word, word, pos, "lot cha")
	return _fmt_none(tag, word, pos)


def apply_8_1_53(word, pos="", SUTRA_TOKEN=""):
	"""विभाषितं सोपसर्गमनुत्तमम् - Vibhashitam sopasargam anuttamam."""
	tag = "p81-053:" + _slug(_SUTRA_TEXTS[53][0])
	upasargas = ("प्र", "सम", "उप", "अप", "अभि", "अति", "सु", "दुर्", "निर्", "परि", "वि", "आ")
	if any(word.startswith(u) for u in upasargas):
		return _fmt_ok(tag, word, word, pos, "sopasargam anuttamam")
	return _fmt_none(tag, word, pos)


def apply_8_1_54(word, pos="", SUTRA_TOKEN=""):
	"""हन्त च - hanta cha."""
	tag = "p81-054:" + _slug(_SUTRA_TEXTS[54][0])
	if word.startswith("हन्त"):
		return _fmt_ok(tag, word, word, pos, "hanta cha")
	return _fmt_none(tag, word, pos)


def apply_8_1_55(word, pos="", SUTRA_TOKEN=""):
	"""आम एकान्तरमामन्त्रितमनन्तिके - ama eka-antaram amantritam anantike."""
	tag = "p81-055:" + _slug(_SUTRA_TEXTS[55][0])
	if word.startswith("आम"):
		return _fmt_ok(tag, word, word, pos, "ama eka-antaram amantritam anantike")
	return _fmt_none(tag, word, pos)


def apply_8_1_56(word, pos="", SUTRA_TOKEN=""):
	"""यद्धितुपरं छन्दसि - yaddhituparam chandasi (Vedic context)."""
	tag = "p81-056:" + _slug(_SUTRA_TEXTS[56][0])
	if word.startswith("यद्धि"):
		return _fmt_ok(tag, word, word, pos, "yaddhituparam chandas")
	return _fmt_none(tag, word, pos)


def apply_8_1_57(word, pos="", SUTRA_TOKEN=""):
	"""चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः - ca-na/cid/iva/gotradi/taddhita/amreditesh."""
	tag = "p81-057:" + _slug(_SUTRA_TEXTS[57][0])
	particles = ("चन", "चिद्", "इव", "गोत्र", "तद्धित", "आम्रेडित")
	if any(word.startswith(p) for p in particles):
		return _fmt_ok(tag, word, word, pos, "cana-cid-iva gotradi taddhita amreditesh")
	return _fmt_none(tag, word, pos)


def apply_8_1_58(word, pos="", SUTRA_TOKEN=""):
	"""चादिषु च - cadishu cha (in ca-adi particles)."""
	tag = "p81-058:" + _slug(_SUTRA_TEXTS[58][0])
	particles_58 = ("च", "चन", "चिद्", "इव", "न", "मा", "उ", "आह", "अहो", "पुरा", "ननु", "किं")
	if any(word == p or word.startswith(p) for p in particles_58):
		return _fmt_ok(tag, word, word, pos, "cadishu cha")
	return _fmt_none(tag, word, pos)


def apply_8_1_59(word, pos="", SUTRA_TOKEN=""):
	"""चवायोगे प्रथमा - cava-yoge prathama (when not combined, first case)."""
	tag = "p81-059:" + _slug(_SUTRA_TEXTS[59][0])
	if word.startswith("चवा"):
		return _fmt_ok(tag, word, word, pos, "cava-yoge prathama")
	return _fmt_none(tag, word, pos)


def apply_8_1_60(word, pos="", SUTRA_TOKEN=""):
	"""हेति क्षियायाम् - heti kshiyayam (perishing with 'hi')."""
	tag = "p81-060:" + _slug(_SUTRA_TEXTS[60][0])
	if word.startswith("हेति"):
		return _fmt_ok(tag, word, word, pos, "heti kshiyayam")
	return _fmt_none(tag, word, pos)


def apply_8_1_61(word, pos="", SUTRA_TOKEN=""):
	"""अहेति विनियोगे च - aheti viniyoge cha."""
	tag = "p81-061:" + _slug(_SUTRA_TEXTS[61][0])
	if word.startswith("अहेति"):
		return _fmt_ok(tag, word, word, pos, "aheti viniyoge cha")
	return _fmt_none(tag, word, pos)


def apply_8_1_62(word, pos="", SUTRA_TOKEN=""):
	"""चाहलोप एवेत्यवधारणम् - ca-halopa evety-avadharanam (assertion: halopa only)."""
	tag = "p81-062:" + _slug(_SUTRA_TEXTS[62][0])
	if word.startswith("चाह"):
		return _fmt_ok(tag, word, word, pos, "ca-halopa evety-avadharanam")
	return _fmt_none(tag, word, pos)


def apply_8_1_63(word, pos="", SUTRA_TOKEN=""):
	"""चादिलोपे विभाषा - cadi-lope vibhasha (optional in ca-adi elision)."""
	tag = "p81-063:" + _slug(_SUTRA_TEXTS[63][0])
	return _fmt_ok(tag, word, word, pos, "cadi-lope vibhasha")


def apply_8_1_64(word, pos="", SUTRA_TOKEN=""):
	"""वैवावेति च च्छन्दसि - vaivaveti cha chandasi."""
	tag = "p81-064:" + _slug(_SUTRA_TEXTS[64][0])
	if word.startswith("वैव"):
		return _fmt_ok(tag, word, word, pos, "vaivaveti cha chandas")
	return _fmt_none(tag, word, pos)


def apply_8_1_65(word, pos="", SUTRA_TOKEN=""):
	"""एकान्याभ्यां समर्थाभ्याम् - eka-anyabhyam samarthabhyam."""
	tag = "p81-065:" + _slug(_SUTRA_TEXTS[65][0])
	if word.startswith("एकान्य"):
		return _fmt_ok(tag, word, word, pos, "eka-anyabhyam samarthabhyam")
	return _fmt_none(tag, word, pos)


def apply_8_1_66(word, pos="", SUTRA_TOKEN=""):
	"""यद्वृत्तान्नित्यं - yadvrttan-nityam (what-happened, necessarily)."""
	tag = "p81-066:" + _slug(_SUTRA_TEXTS[66][0])
	if word.startswith("यद्वृत्त"):
		return _fmt_ok(tag, word, word, pos, "yadvrttan-nityam")
	return _fmt_none(tag, word, pos)


def apply_8_1_67(word, pos="", SUTRA_TOKEN=""):
	"""पूजनात् पूजितमनुदात्तं काष्ठादिभ्यः - pujanat pujitam anudattam kasthadibhyah."""
	tag = "p81-067:" + _slug(_SUTRA_TEXTS[67][0])
	if word.startswith("पूजन"):
		return _fmt_ok(tag, word, word, pos, "pujanat pujitam anudattam")
	return _fmt_none(tag, word, pos)


def apply_8_1_68(word, pos="", SUTRA_TOKEN=""):
	"""सगतिरपि तिङ् - sagatirapi ting (verb with sa-gati also)."""
	tag = "p81-068:" + _slug(_SUTRA_TEXTS[68][0])
	if word.startswith("सगति"):
		return _fmt_ok(tag, word, word, pos, "sagatirapi ting")
	return _fmt_none(tag, word, pos)


def apply_8_1_69(word, pos="", SUTRA_TOKEN=""):
	"""कुत्सने च सुप्यगोत्रादौ - kutsane cha supy-agotradi."""
	tag = "p81-069:" + _slug(_SUTRA_TEXTS[69][0])
	if word.startswith("कुत्सन"):
		return _fmt_ok(tag, word, word, pos, "kutsane cha supy-agotradi")
	return _fmt_none(tag, word, pos)


def apply_8_1_70(word, pos="", SUTRA_TOKEN=""):
	"""गतिर्गतौ - gatir-gatau (same form in motion)."""
	tag = "p81-070:" + _slug(_SUTRA_TEXTS[70][0])
	if word.startswith("गति"):
		return _fmt_ok(tag, word, word, pos, "gatir-gatau")
	return _fmt_none(tag, word, pos)


def apply_8_1_71(word, pos="", SUTRA_TOKEN=""):
	"""तिङि चोदात्तवति - tingi cha udattavati (verb with udatta)."""
	tag = "p81-071:" + _slug(_SUTRA_TEXTS[71][0])
	if word.startswith("तिङ्"):
		return _fmt_ok(tag, word, word, pos, "tingi cha udattavati")
	return _fmt_none(tag, word, pos)


def apply_8_1_72(word, pos="", SUTRA_TOKEN=""):
	"""आमन्त्रितं पूर्वमविद्यमानवत् - amantritam purvam-avidymanavat."""
	tag = "p81-072:" + _slug(_SUTRA_TEXTS[72][0])
	if word.startswith("आमन्त्रित"):
		return _fmt_ok(tag, word, word, pos, "amantritam purvam avidymanavat")
	return _fmt_none(tag, word, pos)


def apply_8_1_73(word, pos="", SUTRA_TOKEN=""):
	"""नामन्त्रिते समानाधिकरणे सामान्यवचनम् - namantrite samanadhikarane samanyavachanam."""
	tag = "p81-073:" + _slug(_SUTRA_TEXTS[73][0])
	if word.startswith("नामन्त्रित"):
		return _fmt_ok(tag, word, word, pos, "namantrite samanadhikarane samanyavachanam")
	return _fmt_none(tag, word, pos)


def apply_8_1_74(word, pos="", SUTRA_TOKEN=""):
	"""विभाषितं विशेषवचने बहुवचनम् - vibhashitam visheshavachane bahuvachanam."""
	tag = "p81-074:" + _slug(_SUTRA_TEXTS[74][0])
	if _ends_visarga(word):
		return _fmt_ok(tag, word, word, pos, "vibhashitam visheshavachane bahuvachanam")
	return _fmt_none(tag, word, pos)


# ---------------------------------------------------------------------------
# ALL_8_1 registry (for dynamic iteration in pipeline)
# ---------------------------------------------------------------------------

ALL_8_1 = {}

for _i in range(1, 75):
	_fn_name = "apply_8_1_" + str(_i)
	ALL_8_1[_i] = _fn_name
