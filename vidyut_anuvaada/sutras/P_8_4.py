# -*- coding: utf-8 -*-
"""Shared apply_8_4_1..apply_8_4_68 functions for P.8.4.x (final pada of Tripadi).

P.8.4 covers final transformations, special exceptions, feminine derivation,
special imperative forms, and concluding rules of the Tripadi.
"""

# Unicode Devanagari constants
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

# Vowel and consonant sets
HAL = set('कखगघङचछजझञटठडढणतथदधनपफबभयरलवशषसह')
CONSONANTS = HAL | {AH}
ALL_VOWELS = {A, AA, I, II, U, UU, R, RL, E, AI, O, AU}
IK = {I, U, R, RL}

# Helpers

def _analyse(word):
	if '+' not in word:
		return word, ''
	idx = word.index('+')
	return word[:idx], word[idx + 1:]


def _phonetic_vowel(syllable):
	if not syllable:
		return ''
	for ch in reversed(syllable):
		if ch in ALL_VOWELS:
			return ch
	return ''


def _remove_last_vowel(s):
	if not s:
		return s
	last_vowel_idx = -1
	for i, ch in enumerate(s):
		if ch in ALL_VOWELS:
			last_vowel_idx = i
	if last_vowel_idx >= 0:
		return s[:last_vowel_idx] + s[last_vowel_idx + 1:]
	return s


def _apply_guna(v):
	GUNA_MAP = {'इ': 'ए', 'उ': 'ओ', 'ऋ': 'ओ', 'ऌ': 'ओ', 'अ': 'अ'}
	return GUNA_MAP.get(v, v)


def _apply_vrddhi(v):
	VRDDHI_MAP = {'इ': 'ऐ', 'उ': 'औ', 'ऋ': 'औ', 'ऌ': 'औ', 'अ': 'आ'}
	return VRDDHI_MAP.get(v, v)


def _fmt(n, tag, word, extra=''):
	s = n + ':' + tag + ';input=' + word
	if extra:
		s += ';' + extra
	return s


def _fmt_ok(n, tag, result, detail=''):
	if detail:
		return n + ':' + tag + '=' + detail + ';result=' + result
	return n + ':' + tag + ';result=' + result


# ============================================================
# P.8.4.1 - P.8.4.10 (visarga, nasal, final consonant rules)
# ============================================================

def apply_8_4_1(word, pos='', SUTRA_TOKEN=''):
	"""रषाभ्यां नो णः समानपदे — final transformations"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.1', 'input', word)
	return _fmt('8.4.1', 'ra-sha-abhyam-no-Nah', word)


def apply_8_4_2(word, pos='', SUTRA_TOKEN=''):
	"""अट्कुप्वाङ्नुम्व्यवायेऽपि"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.2', 'input', word)
	return _fmt('8.4.2', 'at-kup-vang-num-vyavaye', word)


def apply_8_4_3(word, pos='', SUTRA_TOKEN=''):
	"""पूर्वपदात् संज्ञायामगः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.3', 'input', word)
	if w1.endswith('अग') and SUTRA_TOKEN == 'samjna':
		return _fmt_ok('8.4.3', 'ag-removal', w1[:-2] + '+' + w2, 'अग् removed')
	return _fmt('8.4.3', 'not-aga', word)


def apply_8_4_4(word, pos='', SUTRA_TOKEN=''):
	"""वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.4', 'input', word)
	return _fmt('8.4.4', 'vanam-puragamishraka', word)


def apply_8_4_5(word, pos='', SUTRA_TOKEN=''):
	"""प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपीयूक्षाभ्योऽसंज्ञायामपि"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.5', 'input', word)
	return _fmt('8.4.5', 'pranirantaH-sarekshu', word)


def apply_8_4_6(word, pos='', SUTRA_TOKEN=''):
	"""विभाषौषधिवनस्पतिभ्यः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.6', 'input', word)
	return _fmt('8.4.6', 'vibhasha-oshadhivanaspatibhyah', word)


def apply_8_4_7(word, pos='', SUTRA_TOKEN=''):
	"""अह्नोऽदन्तात्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.7', 'input', word)
	if w1.endswith('अह्न') or w1.endswith('अह्नो'):
		return _fmt_ok('8.4.7', 'ahno-lopa', w1.rstrip('ओ').rstrip('ः') + '+' + w2, 'o dropped')
	return _fmt('8.4.7', 'not-ahna', word)


def apply_8_4_8(word, pos='', SUTRA_TOKEN=''):
	"""वाहनमाहितात्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.8', 'input', word)
	return _fmt('8.4.8', 'vahanam-ahitat', word)


def apply_8_4_9(word, pos='', SUTRA_TOKEN=''):
	"""पानं देशे"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.9', 'input', word)
	return _fmt('8.4.9', 'panam-dese', word)


def apply_8_4_10(word, pos='', SUTRA_TOKEN=''):
	"""वा भावकरणयोः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.10', 'input', word)
	return _fmt('8.4.10', 'va-bhava-karanayoh', word)


# ============================================================
# P.8.4.11 - P.8.4.20 (continued final transformations)
# ============================================================

def apply_8_4_11(word, pos='', SUTRA_TOKEN=''):
	"""प्रातिपदिकान्तनुम्विभक्तिषु च"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.11', 'input', word)
	return _fmt('8.4.11', 'pratipadikanta-num-vibhaktishu', word)


def apply_8_4_12(word, pos='', SUTRA_TOKEN=''):
	"""एकाजुत्तरपदे णः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.12', 'input', word)
	pv1 = _phonetic_vowel(w1)
	if pv1 == A and w1.endswith('ण'):
		return _fmt_ok('8.4.12', 'eka-a-juttarapade-Nah', w1[:-1] + '+' + w2, 'ṇ->n')
	return _fmt('8.4.12', 'not-eka-a-juttara', word)


def apply_8_4_13(word, pos='', SUTRA_TOKEN=''):
	"""कुमति च"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.13', 'input', word)
	return _fmt('8.4.13', 'kumati-ca', word)


def apply_8_4_14(word, pos='', SUTRA_TOKEN=''):
	"""उपसर्गादसमासेऽपि णोपदेशस्य"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.14', 'input', word)
	return _fmt('8.4.14', 'upasrgad-asame-api', word)


def apply_8_4_15(word, pos='', SUTRA_TOKEN=''):
	"""हिनुमीना"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.15', 'input', word)
	return _fmt('8.4.15', 'hinumina', word)


def apply_8_4_16(word, pos='', SUTRA_TOKEN=''):
	"""आनि लोट्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.16', 'input', word)
	if w1.endswith('आनि'):
		return _fmt_ok('8.4.16', 'ani-lot', w1 + '+' + w2, 'lot suffix ani')
	return _fmt('8.4.16', 'not-ani-lot', word)


def apply_8_4_17(word, pos='', SUTRA_TOKEN=''):
	"""नेर्गदनदपतपदघुमास्यतिहन्तियातिवातिद्रातिप्सातिवपतिवहतिशाम्यतिचिनोतिदेग्धिषु च"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.17', 'input', word)
	return _fmt('8.4.17', 'ner-gadana-dapata', word)


def apply_8_4_18(word, pos='', SUTRA_TOKEN=''):
	"""शेषे विभाषाऽकखादावषान्त उपदेशे"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.18', 'input', word)
	return _fmt('8.4.18', 'sese-vibhasha-kakha', word)


def apply_8_4_19(word, pos='', SUTRA_TOKEN=''):
	"""अनितेः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.19', 'input', word)
	return _fmt('8.4.19', 'aniteh', word)


def apply_8_4_20(word, pos='', SUTRA_TOKEN=''):
	"""अन्तः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.20', 'input', word)
	return _fmt('8.4.20', 'antah', word)


# ============================================================
# P.8.4.21 - P.8.4.30 (bhAvakaraNa, hanti, vamu specials)
# ============================================================

def apply_8_4_21(word, pos='', SUTRA_TOKEN=''):
	"""उभौ साभ्यासस्य"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.21', 'input', word)
	return _fmt('8.4.21', 'ubhau-sabhyasya', word)


def apply_8_4_22(word, pos='', SUTRA_TOKEN=''):
	"""हन्तेरत्पूर्वस्य"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.22', 'input', word)
	return _fmt('8.4.22', 'hanterat-purvasya', word)


def apply_8_4_23(word, pos='', SUTRA_TOKEN=''):
	"""वमोर्वा"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.23', 'input', word)
	return _fmt('8.4.23', 'vamorva', word)


def apply_8_4_24(word, pos='', SUTRA_TOKEN=''):
	"""अन्तरदेशे"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.24', 'input', word)
	return _fmt('8.4.24', 'antaradese', word)


def apply_8_4_25(word, pos='', SUTRA_TOKEN=''):
	"""अयनं च"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.25', 'input', word)
	return _fmt('8.4.25', 'ayana-ca', word)


def apply_8_4_26(word, pos='', SUTRA_TOKEN=''):
	"""छन्दस्यृदवग्रहात्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.26', 'input', word)
	return _fmt('8.4.26', 'chandasy-rdavagrahAt', word)


def apply_8_4_27(word, pos='', SUTRA_TOKEN=''):
	"""नश्च धातुस्थोरुषुभ्यः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.27', 'input', word)
	if w1.endswith('न') or w1.endswith('नश'):
		return _fmt_ok('8.4.27', 'nash-ca-dhatu-sthorushubhyah', w1 + '+' + w2, 'n->nas before certain roots')
	return _fmt('8.4.27', 'not-nash', word)


def apply_8_4_28(word, pos='', SUTRA_TOKEN=''):
	"""उपसर्गाद् बहुलम्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.28', 'input', word)
	return _fmt('8.4.28', 'upasrgad-bahulam', word)


def apply_8_4_29(word, pos='', SUTRA_TOKEN=''):
	"""कृत्यचः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.29', 'input', word)
	return _fmt('8.4.29', 'kRtyachaH', word)


def apply_8_4_30(word, pos='', SUTRA_TOKEN=''):
	"""णेर्विभाषा"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.30', 'input', word)
	return _fmt('8.4.30', 'NervibhAsha', word)


# ============================================================
# P.8.4.31 - P.8.4.40 (iJa upadhA, hal-related, padAnta)
# ============================================================

def apply_8_4_31(word, pos='', SUTRA_TOKEN=''):
	"""हलश्च इजुपधात्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.31', 'input', word)
	return _fmt('8.4.31', 'halash-ca-ijupadhat', word)


def apply_8_4_32(word, pos='', SUTRA_TOKEN=''):
	"""इजादेः सनुमः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.32', 'input', word)
	return _fmt('8.4.32', 'ijadeh-sanumaH', word)


def apply_8_4_33(word, pos='', SUTRA_TOKEN=''):
	"""वा निंसनिक्षनिन्दाम्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.33', 'input', word)
	return _fmt('8.4.33', 'va-nimsanikshanindam', word)


def apply_8_4_34(word, pos='', SUTRA_TOKEN=''):
	"""न भाभूपूकमिगमिप्यायीवेपाम्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.34', 'input', word)
	return _fmt('8.4.34', 'na-bhAbhUpUkamigami', word)


def apply_8_4_35(word, pos='', SUTRA_TOKEN=''):
	"""षात् पदान्तात्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.35', 'input', word)
	if w1.endswith('ष'):
		return _fmt_ok('8.4.35', 'shAt-padanta', w1[:-1] + '+' + w2, 'ṣ dropped at word-end')
	return _fmt('8.4.35', 'not-shAt', word)


def apply_8_4_36(word, pos='', SUTRA_TOKEN=''):
	"""नशेः षान्तस्य"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.36', 'input', word)
	return _fmt('8.4.36', 'nasheH-shAntasya', word)


def apply_8_4_37(word, pos='', SUTRA_TOKEN=''):
	"""पदान्तस्य"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.37', 'input', word)
	return _fmt('8.4.37', 'padAntasya', word)


def apply_8_4_38(word, pos='', SUTRA_TOKEN=''):
	"""पदव्यवायेऽपि"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.38', 'input', word)
	return _fmt('8.4.38', 'padavyavaye-api', word)


def apply_8_4_39(word, pos='', SUTRA_TOKEN=''):
	"""क्षुभ्नाऽऽदिषु च"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.39', 'input', word)
	return _fmt('8.4.39', 'kShubhna-adishu-ca', word)


def apply_8_4_40(word, pos='', SUTRA_TOKEN=''):
	"""स्तोः श्चुना श्चुः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.40', 'input', word)
	return _fmt('8.4.40', 'stoH-shchuna-shchuh', word)


# ============================================================
# P.8.4.41 - P.8.4.50 (ṣṭu, special consonants, directional)
# ============================================================

def apply_8_4_41(word, pos='', SUTRA_TOKEN=''):
	"""ष्टुना ष्टुः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.41', 'input', word)
	return _fmt('8.4.41', 'ShTuna-ShTuh', word)


def apply_8_4_42(word, pos='', SUTRA_TOKEN=''):
	"""न पदान्ताट्टोरनाम्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.42', 'input', word)
	return _fmt('8.4.42', 'na-padanta-aTTor-anam', word)


def apply_8_4_43(word, pos='', SUTRA_TOKEN=''):
	"""तोः षि"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.43', 'input', word)
	return _fmt('8.4.43', 'toH-zi', word)


def apply_8_4_44(word, pos='', SUTRA_TOKEN=''):
	"""शात्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.44', 'input', word)
	if w1.endswith('श'):
		return _fmt_ok('8.4.44', 'shAt', w1[:-1] + '+' + w2, 'ś dropped')
	return _fmt('8.4.44', 'not-shAt', word)


def apply_8_4_45(word, pos='', SUTRA_TOKEN=''):
	"""यरोऽनुनासिकेऽनुनासिको वा"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.45', 'input', word)
	return _fmt('8.4.45', 'yaro-anunasike-anunasiko-va', word)


def apply_8_4_46(word, pos='', SUTRA_TOKEN=''):
	"""अचो रहाभ्यां द्वे"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.46', 'input', word)
	return _fmt('8.4.46', 'acho-rahabhyam-dve', word)


def apply_8_4_47(word, pos='', SUTRA_TOKEN=''):
	"""अनचि च"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.47', 'input', word)
	return _fmt('8.4.47', 'anaci-ca', word)


def apply_8_4_48(word, pos='', SUTRA_TOKEN=''):
	"""नादिन्याक्रोशे पुत्रस्य"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.48', 'input', word)
	return _fmt('8.4.48', 'nAdinyAkrose-putrasya', word)


def apply_8_4_49(word, pos='', SUTRA_TOKEN=''):
	"""शरोऽचि"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.49', 'input', word)
	return _fmt('8.4.49', 'sharo-aci', word)


def apply_8_4_50(word, pos='', SUTRA_TOKEN=''):
	"""त्रिप्रभृतिषु शाकटायनस्य"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.50', 'input', word)
	return _fmt('8.4.50', 'tri-prabhritishu-shAkATAyana', word)


# ============================================================
# P.8.4.51 - P.8.4.60 (sarvatra, dirgha, jha-sound changes)
# ============================================================

def apply_8_4_51(word, pos='', SUTRA_TOKEN=''):
	"""सर्वत्र शाकल्यस्य"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.51', 'input', word)
	return _fmt('8.4.51', 'sarvatra-shAkalyasya', word)


def apply_8_4_52(word, pos='', SUTRA_TOKEN=''):
	"""दीर्घादाचार्याणाम्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.52', 'input', word)
	return _fmt('8.4.52', 'dIrghAd-AcAryANAm', word)


def apply_8_4_53(word, pos='', SUTRA_TOKEN=''):
	"""झलां जश् झशि"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.53', 'input', word)
	JHAL = {'ज','झ','ब','भ','म','य','र','ल','व'}
	pv2 = _phonetic_vowel(w2)
	pv1 = _phonetic_vowel(w1)
	if w1[-1] in JHAL and pv2 == AH:
		return _fmt_ok('8.4.53', 'jhalam-jash-jhashi', w1[:-1] + 'श्' + '+' + w2, 'jhal->jash before visarga')
	return _fmt('8.4.53', 'not-jhal-jash', word)


def apply_8_4_54(word, pos='', SUTRA_TOKEN=''):
	"""अभ्यासे चर्च"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.54', 'input', word)
	return _fmt('8.4.54', 'abhyAse-carca', word)


def apply_8_4_55(word, pos='', SUTRA_TOKEN=''):
	"""खरि च"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.55', 'input', word)
	KHAR = set('कखगघङचछजझञटठडढणतथदधनपफबभयरलवशषसह')
	if w1[-1] in KHAR:
		return _fmt_ok('8.4.55', 'khar-ca', w1 + '+' + w2, 'khar context')
	return _fmt('8.4.55', 'not-khar', word)


def apply_8_4_56(word, pos='', SUTRA_TOKEN=''):
	"""वाऽवसाने"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.56', 'input', word)
	return _fmt('8.4.56', 'va-avasane', word)


def apply_8_4_57(word, pos='', SUTRA_TOKEN=''):
	"""अणोऽप्रगृह्यस्यानुनासिकः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.57', 'input', word)
	return _fmt('8.4.57', 'aNo-apragRhyasya-anunasikaH', word)


def apply_8_4_58(word, pos='', SUTRA_TOKEN=''):
	"""अनुस्वारस्य ययि परसवर्णः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.58', 'input', word)
	pv2 = _phonetic_vowel(w2)
	if w1.endswith(AH) and pv2 in {I, II, U, UU, R, RL, E, AI, O, AU}:
		return _fmt_ok('8.4.58', 'anusvArasya-yayi-parasavarNaH', w1[:-1] + 'य्' + '+' + w2, 'anusvAra->y before vowel')
	return _fmt('8.4.58', 'not-anusvara-yayi', word)


def apply_8_4_59(word, pos='', SUTRA_TOKEN=''):
	"""वा पदान्तस्य"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.59', 'input', word)
	return _fmt('8.4.59', 'va-padAntasya', word)


def apply_8_4_60(word, pos='', SUTRA_TOKEN=''):
	"""तोर्लि"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.60', 'input', word)
	return _fmt('8.4.60', 'tor-li', word)


# ============================================================
# P.8.4.61 - P.8.4.68 (udaH, jhay, saSh, yam, jhara, svara)
# ============================================================

def apply_8_4_61(word, pos='', SUTRA_TOKEN=''):
	"""उदः स्थास्तम्भोः पूर्वस्य"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.61', 'input', word)
	return _fmt('8.4.61', 'udaH-sthAstambhoh-purvasya', word)


def apply_8_4_62(word, pos='', SUTRA_TOKEN=''):
	"""झयो होऽन्यतरस्याम्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.62', 'input', word)
	JHAY = {'झ','य'}
	pv2 = _phonetic_vowel(w2)
	pv1 = _phonetic_vowel(w1)
	if pv1 in {I, U, R, RL, A} and pv2 in {I, U, R, RL, E, AI, O, AU}:
		if w1[-1] in JHAY:
			return _fmt_ok('8.4.62', 'jhay-ho-anyatarasyam', w1[:-1] + 'ह्' + '+' + w2, 'jhay->h optionally')
	return _fmt('8.4.62', 'not-jhay-ho', word)


def apply_8_4_63(word, pos='', SUTRA_TOKEN=''):
	"""शश्छोऽटि"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.63', 'input', word)
	if w1.endswith('श'):
		return _fmt_ok('8.4.63', 'shash-chho-aTi', w1[:-1] + 'छ्' + '+' + w2, 'ś->ch before aṭ')
	return _fmt('8.4.63', 'not-shash-chho', word)


def apply_8_4_64(word, pos='', SUTRA_TOKEN=''):
	"""हलो यमां यमि लोपः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.64', 'input', word)
	pv2 = _phonetic_vowel(w2)
	pv1 = _phonetic_vowel(w1)
	if pv1 in IK and pv2 == I:
		ya = YAN_MAP.get(pv1, 'य')
		if w1.endswith(ya):
			return _fmt_ok('8.4.64', 'halo-yamam-yami-lopaH', w1[:-1] + '+' + w2, ya + ' dropped before i')
	return _fmt('8.4.64', 'not-yami-lopa', word)


def apply_8_4_65(word, pos='', SUTRA_TOKEN=''):
	"""झरो झरि सवर्णे"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.65', 'input', word)
	JHAR = {'य','र','ल','व','श','ष','स','ह'}
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if w1[-1] in JHAR and w2[0] in JHAR and pv1 == pv2:
		return _fmt_ok('8.4.65', 'jharo-jhari-savarNe', w1[:-1] + '+' + w2, 'jhar consonant doubled savarna')
	return _fmt('8.4.65', 'not-jhara-savarNa', word)


def apply_8_4_66(word, pos='', SUTRA_TOKEN=''):
	"""उदात्तादनुदात्तस्य स्वरितः"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.66', 'input', word)
	return _fmt('8.4.66', 'udAttAd-anudAttasya-svaritaH', word)


def apply_8_4_67(word, pos='', SUTRA_TOKEN=''):
	"""नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम्"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.67', 'input', word)
	return _fmt('8.4.67', 'nodAttasvaritodayam-agArgya', word)


def apply_8_4_68(word, pos='', SUTRA_TOKEN=''):
	"""अ अ — closing sutra of Tripadi"""
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('8.4.68', 'input', word)
	return _fmt('8.4.68', 'a-a-tripadi-close', word)


# ============================================================
# ALL_8_4 registry (sutra-code -> apply function)
# ============================================================

ALL_8_4 = {
	"प.8.4.1": apply_8_4_1,
	"प.8.4.2": apply_8_4_2,
	"प.8.4.3": apply_8_4_3,
	"प.8.4.4": apply_8_4_4,
	"प.8.4.5": apply_8_4_5,
	"प.8.4.6": apply_8_4_6,
	"प.8.4.7": apply_8_4_7,
	"प.8.4.8": apply_8_4_8,
	"प.8.4.9": apply_8_4_9,
	"प.8.4.10": apply_8_4_10,
	"प.8.4.11": apply_8_4_11,
	"प.8.4.12": apply_8_4_12,
	"प.8.4.13": apply_8_4_13,
	"प.8.4.14": apply_8_4_14,
	"प.8.4.15": apply_8_4_15,
	"प.8.4.16": apply_8_4_16,
	"प.8.4.17": apply_8_4_17,
	"प.8.4.18": apply_8_4_18,
	"प.8.4.19": apply_8_4_19,
	"प.8.4.20": apply_8_4_20,
	"प.8.4.21": apply_8_4_21,
	"प.8.4.22": apply_8_4_22,
	"प.8.4.23": apply_8_4_23,
	"प.8.4.24": apply_8_4_24,
	"प.8.4.25": apply_8_4_25,
	"प.8.4.26": apply_8_4_26,
	"प.8.4.27": apply_8_4_27,
	"प.8.4.28": apply_8_4_28,
	"प.8.4.29": apply_8_4_29,
	"प.8.4.30": apply_8_4_30,
	"प.8.4.31": apply_8_4_31,
	"प.8.4.32": apply_8_4_32,
	"प.8.4.33": apply_8_4_33,
	"प.8.4.34": apply_8_4_34,
	"प.8.4.35": apply_8_4_35,
	"प.8.4.36": apply_8_4_36,
	"प.8.4.37": apply_8_4_37,
	"प.8.4.38": apply_8_4_38,
	"प.8.4.39": apply_8_4_39,
	"प.8.4.40": apply_8_4_40,
	"प.8.4.41": apply_8_4_41,
	"प.8.4.42": apply_8_4_42,
	"प.8.4.43": apply_8_4_43,
	"प.8.4.44": apply_8_4_44,
	"प.8.4.45": apply_8_4_45,
	"प.8.4.46": apply_8_4_46,
	"प.8.4.47": apply_8_4_47,
	"प.8.4.48": apply_8_4_48,
	"प.8.4.49": apply_8_4_49,
	"प.8.4.50": apply_8_4_50,
	"प.8.4.51": apply_8_4_51,
	"प.8.4.52": apply_8_4_52,
	"प.8.4.53": apply_8_4_53,
	"प.8.4.54": apply_8_4_54,
	"प.8.4.55": apply_8_4_55,
	"प.8.4.56": apply_8_4_56,
	"प.8.4.57": apply_8_4_57,
	"प.8.4.58": apply_8_4_58,
	"प.8.4.59": apply_8_4_59,
	"प.8.4.60": apply_8_4_60,
	"प.8.4.61": apply_8_4_61,
	"प.8.4.62": apply_8_4_62,
	"प.8.4.63": apply_8_4_63,
	"प.8.4.64": apply_8_4_64,
	"प.8.4.65": apply_8_4_65,
	"प.8.4.66": apply_8_4_66,
	"प.8.4.67": apply_8_4_67,
	"प.8.4.68": apply_8_4_68,
}
