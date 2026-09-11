# -*- coding: utf-8 -*-
"""Shared apply_6_1_1..apply_6_1_223 functions for P.6.1.x."""

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

# Matra-to-phonetic-vowel map (combining -> standalone)
MATRA_MAP = {
	0x093E: AA,
	0x093F: I,
	0x0940: II,
	0x0941: U,
	0x0942: UU,
	0x0943: R,
	0x0944: RL,
	0x0947: E,
	0x0948: AI,
	0x094B: O,
	0x094C: AU,
}

# Vowel constants sets
IK = {I, U, R, RL}
ALL_VOWELS = {A, AA, I, II, U, UU, R, RL, E, AI, O, AU}
HAL = set('कखगघङचछजझञटठडढणतथदधनपफबभयरलवशषसह')
CONSONANTS = HAL | {AH}
PALATAL = {'च','छ','ज','झ','श','ष'}

YAN_MAP = {I: 'य', U: 'व', R: 'र', RL: 'ल'}
GUNA_MAP = {I: E, U: O, R: O, RL: O, A: A}
VRDDHI_MAP = {I: AI, U: AU, R: AU, RL: AU, A: AA}


# Helpers

def _analyse(word):
	if '+' not in word:
		return word, ''
	idx = word.index('+')
	return word[:idx], word[idx + 1:]


def _phonetic_vowel(syllable):
	if not syllable:
		return ''
	# Scan RIGHT to LEFT for the last vowel (sandhi operates on word-final vowel)
	for ch in reversed(syllable):
		if ch in ALL_VOWELS:
			return ch
		mv = ord(ch)
		if mv in (0x093E,0x093F,0x0940,0x0941,0x0942,0x0943,0x0944,0x0947,0x0948,0x094B,0x094C):
			return MATRA_MAP[mv]
	return ''


def _remove_last_vowel(s):
	if not s:
		return s
	# Find last vowel position (scan left to right, keep track)
	last_vowel_idx = -1
	for i, ch in enumerate(s):
		if ch in ALL_VOWELS:
			last_vowel_idx = i
		mv = ord(ch)
		if mv in (0x093E,0x093F,0x0940,0x0941,0x0942,0x0943,0x0944,0x0947,0x0948,0x094B,0x094C):
			last_vowel_idx = i
	if last_vowel_idx >= 0:
		return s[:last_vowel_idx] + s[last_vowel_idx+1:]
	return s


def _apply_guna(v):
	return GUNA_MAP.get(v, v)


def _apply_vrddhi(v):
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
# 6.1.1 - 6.1.7 dvitva (doubling)
# ============================================================

def apply_6_1_1(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.1", "input", word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == pv2 and pv1 in ALL_VOWELS and pv1 != A:
		return _fmt_ok("6.1.1", "dvitva", w1 + "+" + pv1 + "." + w2[1:], pv1 + "+" + pv1)
	return _fmt("6.1.1", "no-dvitva", word)


def apply_6_1_2(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.2", "input", word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == A and pv2 == A:
		return _fmt_ok("6.1.2", "dvitva-a", w1 + "+" + AA + "." + w2[1:], "a+a->aa")
	return _fmt("6.1.2", "no-dvitva", word)


def apply_6_1_3(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.3", "input", word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == pv2 and pv1 in ALL_VOWELS:
		return _fmt_ok("6.1.3", "dvitva-all", w1 + "+" + pv1 + "." + w2[1:], pv1 + "+" + pv1)
	return _fmt("6.1.3", "no-dvitva", word)


def apply_6_1_4(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.4", "input", word)
	pv1 = _phonetic_vowel(w1)
	s2 = w2[0] if w2 else ""
	if pv1 == I and s2 in HAL:
		return _fmt_ok("6.1.4", "dvitva-i", w1 + "+" + I + "." + I + w2, "i+i before hal")
	return _fmt("6.1.4", "no-i-dvitva", word)


def apply_6_1_5(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.5", "input", word)
	pv1 = _phonetic_vowel(w1)
	s2 = w2[0] if w2 else ""
	if pv1 == U and s2 in HAL:
		return _fmt_ok("6.1.5", "dvitva-u", w1 + "+" + U + "." + U + w2, "u+u before hal")
	return _fmt("6.1.5", "no-u-dvitva", word)


def apply_6_1_6(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.6", "input", word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (E, O) and pv2 in ALL_VOWELS:
		return _fmt("6.1.6", "no-dvitva-pluta", word, pv1 + " not doubled")
	return _fmt("6.1.6", "not-pluta", word)


def apply_6_1_7(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.7", "input", word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == A and pv2 == A:
		return _fmt("6.1.7", "no-dvitva-anac", word, "a not doubled")
	return _fmt("6.1.7", "anac-na", word)

def apply_6_1_8(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.8", "input", word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == pv2 and pv1 in ALL_VOWELS and pv1 != A:
		return _fmt_ok("6.1.8", "sampattau", w1 + "+" + pv1 + "." + w2[1:], pv1 + "+" + pv1)
	return _fmt("6.1.8", "no-sampatti", word)


def apply_6_1_9(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.9", "input", word)
	return _fmt("6.1.9", "antAdivat", w1 + "+" + w2, "end=beginning")


def apply_6_1_10(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.10", "input", word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == pv2 and pv1 in ALL_VOWELS:
		return _fmt_ok("6.1.10", "padanta", w1 + "+" + pv1 + "." + w2[1:], "padanta doubling")
	return _fmt("6.1.10", "no-padanta", word)


def apply_6_1_11(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.11", "input", word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == pv2 and pv1 in ALL_VOWELS:
		return _fmt("6.1.11", "no-samAna", word, "no doubling same word")
	return _fmt("6.1.11", "not-samAna", word)


def apply_6_1_12(word, pos="", SUTRA_TOKEN=""):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt("6.1.12", "input", word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == pv2 and pv1 in ALL_VOWELS:
		return _fmt_ok("6.1.12", "svarasya", w1 + "+" + pv1 + "." + w2[1:], "svara doubling")
	return _fmt("6.1.12", "no-svara", word)

def apply_6_1_13(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.13', 'exclusion', word)

def apply_6_1_14(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.14', 'exclusion', word)

def apply_6_1_15(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.15', 'exclusion', word)

def apply_6_1_16(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.16', 'exclusion', word)

def apply_6_1_17(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.17', 'exclusion', word)

def apply_6_1_18(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.18', 'exclusion', word)

def apply_6_1_19(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.19', 'exclusion', word)

def apply_6_1_20(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.20', 'exclusion', word)

def apply_6_1_21(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.21', 'exclusion', word)

def apply_6_1_22(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.22', 'exclusion', word)

def apply_6_1_23(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.23', 'exclusion', word)

def apply_6_1_24(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.24', 'exclusion', word)

def apply_6_1_25(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.25', 'exclusion', word)

def apply_6_1_26(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.26', 'na-nityam', word)

def apply_6_1_27(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.27', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == pv2 and pv1 in ALL_VOWELS:
		return _fmt_ok("6.1.27", "upasargasya", w1 + "+" + pv1 + "." + w2[1:], "upasarga dvitva")
	return _fmt('6.1.27', 'no-upasarga', word)

def apply_6_1_28(word, pos='', SUTRA_TOKEN=''):
	return _fmt('6.1.28', 'no-nipAta', word)

def apply_6_1_29(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.29', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == pv2 and pv1 in ALL_VOWELS:
		return _fmt_ok("6.1.29", "gatiH", w1 + "+" + pv1 + "." + w2[1:], "gati dvitva")
	return _fmt('6.1.29', 'no-gati', word)

def apply_6_1_30(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.30', 'input', word)
	return _fmt('6.1.30', 'context', w1 + '+' + w2)

def apply_6_1_31(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.31', 'input', word)
	return _fmt('6.1.31', 'context', w1 + '+' + w2)

def apply_6_1_32(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.32', 'input', word)
	return _fmt('6.1.32', 'context', w1 + '+' + w2)

def apply_6_1_33(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.33', 'input', word)
	return _fmt('6.1.33', 'context', w1 + '+' + w2)

def apply_6_1_34(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.34', 'input', word)
	return _fmt('6.1.34', 'context', w1 + '+' + w2)

def apply_6_1_35(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.35', 'input', word)
	return _fmt('6.1.35', 'context', w1 + '+' + w2)

def apply_6_1_36(word, pos='', SUTRA_TOKEN=''):
	return _fmt("6.1.36", "interjection-ha", word)

def apply_6_1_37(word, pos='', SUTRA_TOKEN=''):
	return _fmt("6.1.37", "interjection-ah", word)

def apply_6_1_38(word, pos='', SUTRA_TOKEN=''):
	return _fmt("6.1.38", "evam", word)

def apply_6_1_39(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.39', 'input', word)
	return _fmt("6.1.39", "ityevam", w1 + "+" + w2, "iti+evam")

def apply_6_1_40(word, pos='', SUTRA_TOKEN=''):
	return _fmt("6.1.40", "particle-iti", word)

def apply_6_1_41(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.41', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == pv2 and pv1 in ALL_VOWELS:
		return _fmt_ok("6.1.41", "santi", w1 + "+" + pv1 + "." + w2[1:], "santi dvitva")
	return _fmt('6.1.41', 'no-santi', word)

def apply_6_1_42(word, pos='', SUTRA_TOKEN=''):
	return _fmt("6.1.42", "particle", word)

def apply_6_1_43(word, pos='', SUTRA_TOKEN=''):
	return _fmt("6.1.43", "particle", word)

def apply_6_1_44(word, pos='', SUTRA_TOKEN=''):
	return _fmt("6.1.44", "particle", word)

def apply_6_1_45(word, pos='', SUTRA_TOKEN=''):
	return _fmt("6.1.45", "particle", word)

def apply_6_1_46(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.46', 'input', word)
	return _fmt('6.1.46', 'rule', w1 + '+' + w2)

def apply_6_1_47(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.47', 'input', word)
	return _fmt('6.1.47', 'rule', w1 + '+' + w2)

def apply_6_1_48(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.48', 'input', word)
	return _fmt('6.1.48', 'rule', w1 + '+' + w2)

def apply_6_1_49(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.49', 'input', word)
	return _fmt('6.1.49', 'rule', w1 + '+' + w2)

def apply_6_1_50(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.50', 'input', word)
	return _fmt('6.1.50', 'rule', w1 + '+' + w2)

def apply_6_1_51(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.51', 'input', word)
	return _fmt('6.1.51', 'rule', w1 + '+' + w2)

def apply_6_1_52(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.52', 'input', word)
	return _fmt('6.1.52', 'rule', w1 + '+' + w2)

def apply_6_1_53(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.53', 'input', word)
	return _fmt('6.1.53', 'rule', w1 + '+' + w2)

def apply_6_1_54(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.54', 'input', word)
	return _fmt('6.1.54', 'rule', w1 + '+' + w2)

def apply_6_1_55(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.55', 'input', word)
	return _fmt('6.1.55', 'rule', w1 + '+' + w2)

def apply_6_1_56(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.56', 'input', word)
	return _fmt('6.1.56', 'rule', w1 + '+' + w2)

def apply_6_1_57(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.57', 'input', word)
	return _fmt('6.1.57', 'rule', w1 + '+' + w2)

def apply_6_1_58(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.58', 'input', word)
	return _fmt('6.1.58', 'rule', w1 + '+' + w2)

def apply_6_1_59(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.59', 'input', word)
	return _fmt('6.1.59', 'rule', w1 + '+' + w2)

def apply_6_1_60(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.60', 'input', word)
	return _fmt('6.1.60', 'rule', w1 + '+' + w2)

def apply_6_1_61(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.61', 'input', word)
	return _fmt('6.1.61', 'rule', w1 + '+' + w2)

def apply_6_1_62(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.62', 'input', word)
	return _fmt('6.1.62', 'rule', w1 + '+' + w2)

def apply_6_1_63(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.63', 'input', word)
	return _fmt('6.1.63', 'rule', w1 + '+' + w2)

def apply_6_1_64(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.64', 'input', word)
	return _fmt('6.1.64', 'rule', w1 + '+' + w2)

def apply_6_1_65(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.65', 'input', word)
	return _fmt('6.1.65', 'rule', w1 + '+' + w2)

def apply_6_1_66(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.66', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in YAN_MAP and pv2 in ALL_VOWELS:
		ya = YAN_MAP[pv1]
		return _fmt_ok("6.1.66", "iko-yaN", _remove_last_vowel(w1) + ya + w2, pv1 + "->" + ya)
	return _fmt('6.1.66', 'no-iko-yaN', word)

def apply_6_1_67(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.67', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (IK | {A}) and pv2 in ALL_VOWELS:
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.67", "vrddhi", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.67', 'no-match', word)

def apply_6_1_68(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.68', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (IK | {A}) and pv2 in ALL_VOWELS:
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.68", "vrddhi", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.68', 'no-match', word)

def apply_6_1_69(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.69', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (IK | {A}) and pv2 in ALL_VOWELS:
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.69", "vrddhi", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.69', 'no-match', word)

def apply_6_1_70(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.70', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (IK | {A}) and pv2 in ALL_VOWELS:
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.70", "vrddhi", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.70', 'no-match', word)

def apply_6_1_71(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.71', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (IK | {A}) and pv2 in ALL_VOWELS:
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.71", "vrddhi", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.71', 'no-match', word)

def apply_6_1_72(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.72', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (IK | {A}) and pv2 in ALL_VOWELS:
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.72", "vrddhi", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.72', 'no-match', word)

def apply_6_1_73(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.73', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (IK | {A}) and pv2 in ALL_VOWELS:
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.73", "vrddhi", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.73', 'no-match', word)

def apply_6_1_74(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.74', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (IK | {A}) and pv2 in ALL_VOWELS:
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.74", "vrddhi", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.74', 'no-match', word)

def apply_6_1_75(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.75', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (IK | {A}) and pv2 in ALL_VOWELS:
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.75", "vrddhi", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.75', 'no-match', word)

def apply_6_1_76(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.76', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in (IK | {A}) and pv2 in ALL_VOWELS:
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.76", "vrddhi", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.76', 'no-match', word)

def apply_6_1_77(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.77', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in YAN_MAP and pv2 in ALL_VOWELS:
		ya = YAN_MAP[pv1]
		return _fmt_ok("6.1.77", "iko-yaN", _remove_last_vowel(w1) + ya + w2, pv1 + "->" + ya)
	return _fmt('6.1.77', 'no-iko-yaN', word)

def apply_6_1_78(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.78', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == E and pv2 in ALL_VOWELS:
		return _fmt_ok("6.1.78", "eco-y", _remove_last_vowel(w1) + "अय" + w2, "e->ay")
	if pv1 == O and pv2 in ALL_VOWELS:
		return _fmt_ok("6.1.78", "eco-v", _remove_last_vowel(w1) + "अव" + w2, "o->av")
	return _fmt('6.1.78', 'no-eco', word)

def apply_6_1_79(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.79', 'input', word)
	return _fmt('6.1.79', 'context', w1 + '+' + w2)

def apply_6_1_80(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.80', 'input', word)
	return _fmt('6.1.80', 'context', w1 + '+' + w2)

def apply_6_1_81(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.81', 'input', word)
	return _fmt('6.1.81', 'context', w1 + '+' + w2)

def apply_6_1_82(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.82', 'input', word)
	return _fmt('6.1.82', 'context', w1 + '+' + w2)

def apply_6_1_83(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.83', 'input', word)
	return _fmt('6.1.83', 'context', w1 + '+' + w2)

def apply_6_1_84(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.84', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in ALL_VOWELS and pv2 in ALL_VOWELS:
		return _fmt_ok("6.1.84", "ekaH", w1 + "+" + w2, "single vowel preserved")
	return _fmt('6.1.84', 'not-between-cons', word)

def apply_6_1_85(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.85', 'input', word)
	return _fmt('6.1.85', 'context', w1 + '+' + w2)

def apply_6_1_86(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.86', 'input', word)
	return _fmt('6.1.86', 'context', w1 + '+' + w2)

def apply_6_1_87(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.87', 'input', word)
	return _fmt('6.1.87', 'context', w1 + '+' + w2)

def apply_6_1_88(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.88', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 in IK and pv2 in (E, I, II):
		v = _apply_vrddhi(pv1)
		return _fmt_ok("6.1.88", "vrddhir-eci", _remove_last_vowel(w1) + v + w2, pv1 + "->" + v)
	return _fmt('6.1.88', 'no-vrddhir-eci', word)

def apply_6_1_89(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.89', 'input', word)
	return _fmt('6.1.89', 'context', w1 + '+' + w2)

def apply_6_1_90(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.90', 'input', word)
	return _fmt('6.1.90', 'context', w1 + '+' + w2)

def apply_6_1_91(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.91', 'input', word)
	return _fmt('6.1.91', 'context', w1 + '+' + w2)

def apply_6_1_92(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.92', 'input', word)
	return _fmt('6.1.92', 'context', w1 + '+' + w2)

def apply_6_1_93(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.93', 'input', word)
	return _fmt('6.1.93', 'context', w1 + '+' + w2)

def apply_6_1_94(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.94', 'input', word)
	return _fmt('6.1.94', 'context', w1 + '+' + w2)

def apply_6_1_95(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.95', 'input', word)
	return _fmt('6.1.95', 'context', w1 + '+' + w2)

def apply_6_1_96(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.96', 'input', word)
	return _fmt('6.1.96', 'context', w1 + '+' + w2)

def apply_6_1_97(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.97', 'input', word)
	return _fmt('6.1.97', 'context', w1 + '+' + w2)

def apply_6_1_97(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.97', 'input', word)
	pv1 = _phonetic_vowel(w1)
	pv2 = _phonetic_vowel(w2)
	if pv1 == A and pv2 in IK:
		g = _apply_guna(pv2)
		return _fmt_ok("6.1.97", "ato-guNe", w1 + g + w2[1:], "a+" + pv2 + "->" + g)
	return _fmt('6.1.97', 'no-ato-guNe', word)

def apply_6_1_98(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.98', 'input', word)
	return _fmt('6.1.98', 'context', w1 + '+' + w2)

def apply_6_1_99(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.99', 'input', word)
	return _fmt('6.1.99', 'context', w1 + '+' + w2)

def apply_6_1_100(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.100', 'input', word)
	return _fmt('6.1.100', 'context', w1 + '+' + w2)

def apply_6_1_101(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.101', 'input', word)
	return _fmt('6.1.101', 'context', w1 + '+' + w2)

def apply_6_1_102(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.102', 'input', word)
	return _fmt('6.1.102', 'context', w1 + '+' + w2)

def apply_6_1_103(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.103', 'input', word)
	return _fmt('6.1.103', 'context', w1 + '+' + w2)

def apply_6_1_104(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.104', 'input', word)
	return _fmt('6.1.104', 'context', w1 + '+' + w2)

def apply_6_1_105(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.105', 'input', word)
	return _fmt('6.1.105', 'context', w1 + '+' + w2)

def apply_6_1_106(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.106', 'input', word)
	return _fmt('6.1.106', 'context', w1 + '+' + w2)

def apply_6_1_107(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.107', 'input', word)
	return _fmt('6.1.107', 'context', w1 + '+' + w2)

def apply_6_1_108(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.108', 'input', word)
	return _fmt('6.1.108', 'context', w1 + '+' + w2)

def apply_6_1_109(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.109', 'input', word)
	return _fmt('6.1.109', 'context', w1 + '+' + w2)

def apply_6_1_110(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.110', 'input', word)
	return _fmt('6.1.110', 'context', w1 + '+' + w2)

def apply_6_1_111(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.111', 'input', word)
	return _fmt('6.1.111', 'context', w1 + '+' + w2)

def apply_6_1_112(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.112', 'input', word)
	return _fmt('6.1.112', 'context', w1 + '+' + w2)

def apply_6_1_113(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.113', 'input', word)
	return _fmt('6.1.113', 'context', w1 + '+' + w2)

def apply_6_1_114(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.114', 'input', word)
	return _fmt('6.1.114', 'context', w1 + '+' + w2)

def apply_6_1_115(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.115', 'input', word)
	return _fmt('6.1.115', 'context', w1 + '+' + w2)

def apply_6_1_116(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.116', 'input', word)
	return _fmt('6.1.116', 'context', w1 + '+' + w2)

def apply_6_1_117(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.117', 'input', word)
	pv1 = _phonetic_vowel(w1)
	if pv1 == A:
		return _fmt_ok("6.1.117", "antyati", _remove_last_vowel(w1) + AA + w2, "a->aa")
	return _fmt('6.1.117', 'no-antyati', word)

def apply_6_1_118(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.118', 'input', word)
	return _fmt('6.1.118', 'context', w1 + '+' + w2)

def apply_6_1_119(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.119', 'input', word)
	return _fmt('6.1.119', 'context', w1 + '+' + w2)

def apply_6_1_120(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.120', 'input', word)
	return _fmt('6.1.120', 'context', w1 + '+' + w2)

def apply_6_1_121(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.121', 'input', word)
	return _fmt('6.1.121', 'context', w1 + '+' + w2)

def apply_6_1_122(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.122', 'input', word)
	return _fmt('6.1.122', 'context', w1 + '+' + w2)

def apply_6_1_123(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.123', 'input', word)
	return _fmt('6.1.123', 'context', w1 + '+' + w2)

def apply_6_1_124(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.124', 'input', word)
	return _fmt('6.1.124', 'context', w1 + '+' + w2)

def apply_6_1_125(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.125', 'input', word)
	return _fmt('6.1.125', 'context', w1 + '+' + w2)

def apply_6_1_126(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.126', 'input', word)
	return _fmt('6.1.126', 'context', w1 + '+' + w2)

def apply_6_1_127(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.127', 'input', word)
	return _fmt('6.1.127', 'context', w1 + '+' + w2)

def apply_6_1_128(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.128', 'input', word)
	return _fmt('6.1.128', 'context', w1 + '+' + w2)

def apply_6_1_129(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.129', 'input', word)
	return _fmt('6.1.129', 'context', w1 + '+' + w2)

def apply_6_1_130(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.130', 'input', word)
	pv2 = _phonetic_vowel(w2)
	if w1.endswith('स') and pv2 in ALL_VOWELS:
		return _fmt_ok('6.1.130', 'SAkalasya-lopa', w1[:-1] + '+' + w2, 's dropped')
	if w1.endswith('स्') and pv2 in ALL_VOWELS:
		return _fmt_ok('6.1.130', 'SAkalasya-lopa', w1[:-1] + '+' + w2, 's dropped')
	return _fmt('6.1.130', 'no-SAkalasya', word)

def apply_6_1_131(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.131', 'input', word)
	return _fmt('6.1.131', 'context', w1 + '+' + w2)

def apply_6_1_132(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.132', 'input', word)
	return _fmt('6.1.132', 'context', w1 + '+' + w2)

def apply_6_1_133(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.133', 'input', word)
	return _fmt('6.1.133', 'context', w1 + '+' + w2)

def apply_6_1_134(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.134', 'input', word)
	s2 = w2[0] if w2 else ''
	if s2 in PALATAL:
		if w1.endswith('ास'):
			new_w1 = w1[:-2] + 'ा'
			return _fmt_ok("6.1.134", "SAsaH-lopa", new_w1 + "+" + w2, "s dropped after a before palatal")
		if 'अस' in w1:
			new_w1 = w1.replace('अस', 'अ')
			return _fmt_ok("6.1.134", "SAsaH-lopa", new_w1 + "+" + w2, "s dropped")
		if w1.endswith('स'):
			return _fmt_ok("6.1.134", "SAsaH-lopa2", w1[:-1] + "+" + w2, "s dropped")
	return _fmt('6.1.134', 'no-SAsaH-lopa', word)

def apply_6_1_135(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.135', 'input', word)
	return _fmt('6.1.135', 'context', w1 + '+' + w2)

def apply_6_1_136(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.136', 'input', word)
	return _fmt('6.1.136', 'context', w1 + '+' + w2)

def apply_6_1_137(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.137', 'input', word)
	return _fmt('6.1.137', 'context', w1 + '+' + w2)

def apply_6_1_138(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.138', 'input', word)
	return _fmt('6.1.138', 'context', w1 + '+' + w2)

def apply_6_1_139(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.139', 'input', word)
	s2 = w2[0] if w2 else ''
	if w1.endswith('स्') or w1.endswith('स'):
		if s2 in ALL_VOWELS or s2 in ('स','ह','श','ष'):
			new_w1 = w1[:-1] if w1.endswith('स') else w1[:-2]
			return _fmt_ok("6.1.139", "saH-visarga", new_w1 + AH + w2, "s->visarga")
	return _fmt('6.1.139', 'no-saH', word)

def apply_6_1_140(word, pos='', SUTRA_TOKEN=''):
	if word.endswith('ः') or word.endswith('ह'):
		return _fmt_ok("6.1.140", "padAntasya-lopa", word[:-1], "h dropped")
	if word.endswith('ह्'):
		return _fmt_ok("6.1.140", "padAntasya-lopa", word[:-2], "h dropped")
	return _fmt('6.1.140', 'no-h', word)

def apply_6_1_141(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.141', 'input', word)
	return _fmt('6.1.141', 'context', w1 + '+' + w2)

def apply_6_1_142(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.142', 'input', word)
	return _fmt('6.1.142', 'context', w1 + '+' + w2)

def apply_6_1_143(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.143', 'input', word)
	return _fmt('6.1.143', 'context', w1 + '+' + w2)

def apply_6_1_144(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.144', 'input', word)
	return _fmt('6.1.144', 'context', w1 + '+' + w2)

def apply_6_1_145(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.145', 'input', word)
	return _fmt('6.1.145', 'context', w1 + '+' + w2)

def apply_6_1_146(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.146', 'input', word)
	return _fmt('6.1.146', 'context', w1 + '+' + w2)

def apply_6_1_147(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.147', 'input', word)
	return _fmt('6.1.147', 'context', w1 + '+' + w2)

def apply_6_1_148(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.148', 'input', word)
	return _fmt('6.1.148', 'context', w1 + '+' + w2)

def apply_6_1_149(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.149', 'input', word)
	return _fmt('6.1.149', 'context', w1 + '+' + w2)

def apply_6_1_150(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.150', 'input', word)
	return _fmt('6.1.150', 'context', w1 + '+' + w2)

def apply_6_1_151(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.151', 'input', word)
	return _fmt('6.1.151', 'context', w1 + '+' + w2)

def apply_6_1_152(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.152', 'input', word)
	return _fmt('6.1.152', 'context', w1 + '+' + w2)

def apply_6_1_153(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.153', 'input', word)
	return _fmt('6.1.153', 'context', w1 + '+' + w2)

def apply_6_1_154(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.154', 'input', word)
	return _fmt('6.1.154', 'context', w1 + '+' + w2)

def apply_6_1_155(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.155', 'input', word)
	return _fmt('6.1.155', 'context', w1 + '+' + w2)

def apply_6_1_156(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.156', 'input', word)
	return _fmt('6.1.156', 'context', w1 + '+' + w2)

def apply_6_1_157(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.157', 'input', word)
	return _fmt('6.1.157', 'context', w1 + '+' + w2)

def apply_6_1_158(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.158', 'input', word)
	return _fmt('6.1.158', 'context', w1 + '+' + w2)

def apply_6_1_159(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.159', 'input', word)
	return _fmt('6.1.159', 'context', w1 + '+' + w2)

def apply_6_1_160(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.160', 'input', word)
	return _fmt('6.1.160', 'context', w1 + '+' + w2)

def apply_6_1_161(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.161', 'input', word)
	return _fmt('6.1.161', 'context', w1 + '+' + w2)

def apply_6_1_162(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.162', 'input', word)
	return _fmt('6.1.162', 'context', w1 + '+' + w2)

def apply_6_1_163(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.163', 'input', word)
	return _fmt('6.1.163', 'context', w1 + '+' + w2)

def apply_6_1_164(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.164', 'input', word)
	return _fmt('6.1.164', 'context', w1 + '+' + w2)

def apply_6_1_165(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.165', 'input', word)
	return _fmt('6.1.165', 'context', w1 + '+' + w2)

def apply_6_1_166(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.166', 'input', word)
	return _fmt('6.1.166', 'context', w1 + '+' + w2)

def apply_6_1_167(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.167', 'input', word)
	return _fmt('6.1.167', 'context', w1 + '+' + w2)

def apply_6_1_168(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.168', 'input', word)
	return _fmt('6.1.168', 'context', w1 + '+' + w2)

def apply_6_1_169(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.169', 'input', word)
	return _fmt('6.1.169', 'context', w1 + '+' + w2)

def apply_6_1_170(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.170', 'input', word)
	return _fmt('6.1.170', 'context', w1 + '+' + w2)

def apply_6_1_171(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.171', 'input', word)
	return _fmt('6.1.171', 'context', w1 + '+' + w2)

def apply_6_1_172(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.172', 'input', word)
	return _fmt('6.1.172', 'context', w1 + '+' + w2)

def apply_6_1_173(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.173', 'input', word)
	return _fmt('6.1.173', 'context', w1 + '+' + w2)

def apply_6_1_174(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.174', 'input', word)
	return _fmt('6.1.174', 'context', w1 + '+' + w2)

def apply_6_1_175(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.175', 'input', word)
	return _fmt('6.1.175', 'context', w1 + '+' + w2)

def apply_6_1_176(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.176', 'input', word)
	return _fmt('6.1.176', 'context', w1 + '+' + w2)

def apply_6_1_177(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.177', 'input', word)
	return _fmt('6.1.177', 'context', w1 + '+' + w2)

def apply_6_1_178(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.178', 'input', word)
	return _fmt('6.1.178', 'context', w1 + '+' + w2)

def apply_6_1_179(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.179', 'input', word)
	return _fmt('6.1.179', 'context', w1 + '+' + w2)

def apply_6_1_180(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.180', 'input', word)
	return _fmt('6.1.180', 'context', w1 + '+' + w2)

def apply_6_1_181(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.181', 'input', word)
	return _fmt('6.1.181', 'context', w1 + '+' + w2)

def apply_6_1_182(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.182', 'input', word)
	return _fmt('6.1.182', 'context', w1 + '+' + w2)

def apply_6_1_183(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.183', 'input', word)
	return _fmt('6.1.183', 'context', w1 + '+' + w2)

def apply_6_1_184(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.184', 'input', word)
	return _fmt('6.1.184', 'context', w1 + '+' + w2)

def apply_6_1_185(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.185', 'input', word)
	return _fmt('6.1.185', 'context', w1 + '+' + w2)

def apply_6_1_186(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.186', 'input', word)
	return _fmt('6.1.186', 'context', w1 + '+' + w2)

def apply_6_1_187(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.187', 'input', word)
	return _fmt('6.1.187', 'context', w1 + '+' + w2)

def apply_6_1_188(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.188', 'input', word)
	return _fmt('6.1.188', 'context', w1 + '+' + w2)

def apply_6_1_189(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.189', 'input', word)
	return _fmt('6.1.189', 'context', w1 + '+' + w2)

def apply_6_1_190(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.190', 'input', word)
	return _fmt('6.1.190', 'context', w1 + '+' + w2)

def apply_6_1_191(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.191', 'input', word)
	return _fmt('6.1.191', 'context', w1 + '+' + w2)

def apply_6_1_192(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.192', 'input', word)
	return _fmt('6.1.192', 'context', w1 + '+' + w2)

def apply_6_1_193(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.193', 'input', word)
	return _fmt('6.1.193', 'context', w1 + '+' + w2)

def apply_6_1_194(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.194', 'input', word)
	return _fmt('6.1.194', 'context', w1 + '+' + w2)

def apply_6_1_195(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.195', 'input', word)
	return _fmt('6.1.195', 'context', w1 + '+' + w2)

def apply_6_1_196(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.196', 'input', word)
	return _fmt('6.1.196', 'context', w1 + '+' + w2)

def apply_6_1_197(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.197', 'input', word)
	return _fmt('6.1.197', 'context', w1 + '+' + w2)

def apply_6_1_198(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.198', 'input', word)
	return _fmt('6.1.198', 'context', w1 + '+' + w2)

def apply_6_1_199(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.199', 'input', word)
	return _fmt('6.1.199', 'context', w1 + '+' + w2)

def apply_6_1_200(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.200', 'input', word)
	return _fmt('6.1.200', 'context', w1 + '+' + w2)

def apply_6_1_201(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.201', 'input', word)
	return _fmt('6.1.201', 'context', w1 + '+' + w2)

def apply_6_1_202(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.202', 'input', word)
	return _fmt('6.1.202', 'context', w1 + '+' + w2)

def apply_6_1_203(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.203', 'input', word)
	return _fmt('6.1.203', 'context', w1 + '+' + w2)

def apply_6_1_204(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.204', 'input', word)
	return _fmt('6.1.204', 'context', w1 + '+' + w2)

def apply_6_1_205(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.205', 'input', word)
	return _fmt('6.1.205', 'context', w1 + '+' + w2)

def apply_6_1_206(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.206', 'input', word)
	return _fmt('6.1.206', 'context', w1 + '+' + w2)

def apply_6_1_207(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.207', 'input', word)
	return _fmt('6.1.207', 'context', w1 + '+' + w2)

def apply_6_1_208(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.208', 'input', word)
	return _fmt('6.1.208', 'context', w1 + '+' + w2)

def apply_6_1_209(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.209', 'input', word)
	return _fmt('6.1.209', 'context', w1 + '+' + w2)

def apply_6_1_210(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.210', 'input', word)
	return _fmt('6.1.210', 'context', w1 + '+' + w2)

def apply_6_1_211(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.211', 'input', word)
	return _fmt('6.1.211', 'context', w1 + '+' + w2)

def apply_6_1_212(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.212', 'input', word)
	return _fmt('6.1.212', 'context', w1 + '+' + w2)

def apply_6_1_213(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.213', 'input', word)
	return _fmt('6.1.213', 'context', w1 + '+' + w2)

def apply_6_1_214(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.214', 'input', word)
	return _fmt('6.1.214', 'context', w1 + '+' + w2)

def apply_6_1_215(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.215', 'input', word)
	return _fmt('6.1.215', 'context', w1 + '+' + w2)

def apply_6_1_216(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.216', 'input', word)
	return _fmt('6.1.216', 'context', w1 + '+' + w2)

def apply_6_1_217(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.217', 'input', word)
	return _fmt('6.1.217', 'context', w1 + '+' + w2)

def apply_6_1_218(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.218', 'input', word)
	return _fmt('6.1.218', 'context', w1 + '+' + w2)

def apply_6_1_219(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.219', 'input', word)
	return _fmt('6.1.219', 'context', w1 + '+' + w2)

def apply_6_1_220(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.220', 'input', word)
	return _fmt('6.1.220', 'context', w1 + '+' + w2)

def apply_6_1_221(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.221', 'input', word)
	return _fmt('6.1.221', 'context', w1 + '+' + w2)

def apply_6_1_222(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.222', 'input', word)
	return _fmt('6.1.222', 'context', w1 + '+' + w2)

def apply_6_1_223(word, pos='', SUTRA_TOKEN=''):
	w1, w2 = _analyse(word)
	if not w2:
		return _fmt('6.1.223', 'input', word)
	return _fmt('6.1.223', 'context', w1 + '+' + w2)


ALL_6_1 = {
 "प.6.1.1": apply_6_1_1,
 "प.6.1.2": apply_6_1_2,
 "प.6.1.3": apply_6_1_3,
 "प.6.1.4": apply_6_1_4,
 "प.6.1.5": apply_6_1_5,
 "प.6.1.6": apply_6_1_6,
 "प.6.1.7": apply_6_1_7,
 "प.6.1.8": apply_6_1_8,
 "प.6.1.9": apply_6_1_9,
 "प.6.1.10": apply_6_1_10,
 "प.6.1.11": apply_6_1_11,
 "प.6.1.12": apply_6_1_12,
 "प.6.1.13": apply_6_1_13,
 "प.6.1.14": apply_6_1_14,
 "प.6.1.15": apply_6_1_15,
 "प.6.1.16": apply_6_1_16,
 "प.6.1.17": apply_6_1_17,
 "प.6.1.18": apply_6_1_18,
 "प.6.1.19": apply_6_1_19,
 "प.6.1.20": apply_6_1_20,
 "प.6.1.21": apply_6_1_21,
 "प.6.1.22": apply_6_1_22,
 "प.6.1.23": apply_6_1_23,
 "प.6.1.24": apply_6_1_24,
 "प.6.1.25": apply_6_1_25,
 "प.6.1.26": apply_6_1_26,
 "प.6.1.27": apply_6_1_27,
 "प.6.1.28": apply_6_1_28,
 "प.6.1.29": apply_6_1_29,
 "प.6.1.30": apply_6_1_30,
 "प.6.1.31": apply_6_1_31,
 "प.6.1.32": apply_6_1_32,
 "प.6.1.33": apply_6_1_33,
 "प.6.1.34": apply_6_1_34,
 "प.6.1.35": apply_6_1_35,
 "प.6.1.36": apply_6_1_36,
 "प.6.1.37": apply_6_1_37,
 "प.6.1.38": apply_6_1_38,
 "प.6.1.39": apply_6_1_39,
 "प.6.1.40": apply_6_1_40,
 "प.6.1.41": apply_6_1_41,
 "प.6.1.42": apply_6_1_42,
 "प.6.1.43": apply_6_1_43,
 "प.6.1.44": apply_6_1_44,
 "प.6.1.45": apply_6_1_45,
 "प.6.1.46": apply_6_1_46,
 "प.6.1.47": apply_6_1_47,
 "प.6.1.48": apply_6_1_48,
 "प.6.1.49": apply_6_1_49,
 "प.6.1.50": apply_6_1_50,
 "प.6.1.51": apply_6_1_51,
 "प.6.1.52": apply_6_1_52,
 "प.6.1.53": apply_6_1_53,
 "प.6.1.54": apply_6_1_54,
 "प.6.1.55": apply_6_1_55,
 "प.6.1.56": apply_6_1_56,
 "प.6.1.57": apply_6_1_57,
 "प.6.1.58": apply_6_1_58,
 "प.6.1.59": apply_6_1_59,
 "प.6.1.60": apply_6_1_60,
 "प.6.1.61": apply_6_1_61,
 "प.6.1.62": apply_6_1_62,
 "प.6.1.63": apply_6_1_63,
 "प.6.1.64": apply_6_1_64,
 "प.6.1.65": apply_6_1_65,
 "प.6.1.66": apply_6_1_66,
 "प.6.1.67": apply_6_1_67,
 "प.6.1.68": apply_6_1_68,
 "प.6.1.69": apply_6_1_69,
 "प.6.1.70": apply_6_1_70,
 "प.6.1.71": apply_6_1_71,
 "प.6.1.72": apply_6_1_72,
 "प.6.1.73": apply_6_1_73,
 "प.6.1.74": apply_6_1_74,
 "प.6.1.75": apply_6_1_75,
 "प.6.1.76": apply_6_1_76,
 "प.6.1.77": apply_6_1_77,
 "प.6.1.78": apply_6_1_78,
 "प.6.1.79": apply_6_1_79,
 "प.6.1.80": apply_6_1_80,
 "प.6.1.81": apply_6_1_81,
 "प.6.1.82": apply_6_1_82,
 "प.6.1.83": apply_6_1_83,
 "प.6.1.84": apply_6_1_84,
 "प.6.1.85": apply_6_1_85,
 "प.6.1.86": apply_6_1_86,
 "प.6.1.87": apply_6_1_87,
 "प.6.1.88": apply_6_1_88,
 "प.6.1.89": apply_6_1_89,
 "प.6.1.90": apply_6_1_90,
 "प.6.1.91": apply_6_1_91,
 "प.6.1.92": apply_6_1_92,
 "प.6.1.93": apply_6_1_93,
 "प.6.1.94": apply_6_1_94,
 "प.6.1.95": apply_6_1_95,
 "प.6.1.96": apply_6_1_96,
 "प.6.1.97": apply_6_1_97,
 "प.6.1.98": apply_6_1_98,
 "प.6.1.99": apply_6_1_99,
 "प.6.1.100": apply_6_1_100,
 "प.6.1.101": apply_6_1_101,
 "प.6.1.102": apply_6_1_102,
 "प.6.1.103": apply_6_1_103,
 "प.6.1.104": apply_6_1_104,
 "प.6.1.105": apply_6_1_105,
 "प.6.1.106": apply_6_1_106,
 "प.6.1.107": apply_6_1_107,
 "प.6.1.108": apply_6_1_108,
 "प.6.1.109": apply_6_1_109,
 "प.6.1.110": apply_6_1_110,
 "प.6.1.111": apply_6_1_111,
 "प.6.1.112": apply_6_1_112,
 "प.6.1.113": apply_6_1_113,
 "प.6.1.114": apply_6_1_114,
 "प.6.1.115": apply_6_1_115,
 "प.6.1.116": apply_6_1_116,
 "प.6.1.117": apply_6_1_117,
 "प.6.1.118": apply_6_1_118,
 "प.6.1.119": apply_6_1_119,
 "प.6.1.120": apply_6_1_120,
 "प.6.1.121": apply_6_1_121,
 "प.6.1.122": apply_6_1_122,
 "प.6.1.123": apply_6_1_123,
 "प.6.1.124": apply_6_1_124,
 "प.6.1.125": apply_6_1_125,
 "प.6.1.126": apply_6_1_126,
 "प.6.1.127": apply_6_1_127,
 "प.6.1.128": apply_6_1_128,
 "प.6.1.129": apply_6_1_129,
 "प.6.1.130": apply_6_1_130,
 "प.6.1.131": apply_6_1_131,
 "प.6.1.132": apply_6_1_132,
 "प.6.1.133": apply_6_1_133,
 "प.6.1.134": apply_6_1_134,
 "प.6.1.135": apply_6_1_135,
 "प.6.1.136": apply_6_1_136,
 "प.6.1.137": apply_6_1_137,
 "प.6.1.138": apply_6_1_138,
 "प.6.1.139": apply_6_1_139,
 "प.6.1.140": apply_6_1_140,
 "प.6.1.141": apply_6_1_141,
 "प.6.1.142": apply_6_1_142,
 "प.6.1.143": apply_6_1_143,
 "प.6.1.144": apply_6_1_144,
 "प.6.1.145": apply_6_1_145,
 "प.6.1.146": apply_6_1_146,
 "प.6.1.147": apply_6_1_147,
 "प.6.1.148": apply_6_1_148,
 "प.6.1.149": apply_6_1_149,
 "प.6.1.150": apply_6_1_150,
 "प.6.1.151": apply_6_1_151,
 "प.6.1.152": apply_6_1_152,
 "प.6.1.153": apply_6_1_153,
 "प.6.1.154": apply_6_1_154,
 "प.6.1.155": apply_6_1_155,
 "प.6.1.156": apply_6_1_156,
 "प.6.1.157": apply_6_1_157,
 "प.6.1.158": apply_6_1_158,
 "प.6.1.159": apply_6_1_159,
 "प.6.1.160": apply_6_1_160,
 "प.6.1.161": apply_6_1_161,
 "प.6.1.162": apply_6_1_162,
 "प.6.1.163": apply_6_1_163,
 "प.6.1.164": apply_6_1_164,
 "प.6.1.165": apply_6_1_165,
 "प.6.1.166": apply_6_1_166,
 "प.6.1.167": apply_6_1_167,
 "प.6.1.168": apply_6_1_168,
 "प.6.1.169": apply_6_1_169,
 "प.6.1.170": apply_6_1_170,
 "प.6.1.171": apply_6_1_171,
 "प.6.1.172": apply_6_1_172,
 "प.6.1.173": apply_6_1_173,
 "प.6.1.174": apply_6_1_174,
 "प.6.1.175": apply_6_1_175,
 "प.6.1.176": apply_6_1_176,
 "प.6.1.177": apply_6_1_177,
 "प.6.1.178": apply_6_1_178,
 "प.6.1.179": apply_6_1_179,
 "प.6.1.180": apply_6_1_180,
 "प.6.1.181": apply_6_1_181,
 "प.6.1.182": apply_6_1_182,
 "प.6.1.183": apply_6_1_183,
 "प.6.1.184": apply_6_1_184,
 "प.6.1.185": apply_6_1_185,
 "प.6.1.186": apply_6_1_186,
 "प.6.1.187": apply_6_1_187,
 "प.6.1.188": apply_6_1_188,
 "प.6.1.189": apply_6_1_189,
 "प.6.1.190": apply_6_1_190,
 "प.6.1.191": apply_6_1_191,
 "प.6.1.192": apply_6_1_192,
 "प.6.1.193": apply_6_1_193,
 "प.6.1.194": apply_6_1_194,
 "प.6.1.195": apply_6_1_195,
 "प.6.1.196": apply_6_1_196,
 "प.6.1.197": apply_6_1_197,
 "प.6.1.198": apply_6_1_198,
 "प.6.1.199": apply_6_1_199,
 "प.6.1.200": apply_6_1_200,
 "प.6.1.201": apply_6_1_201,
 "प.6.1.202": apply_6_1_202,
 "प.6.1.203": apply_6_1_203,
 "प.6.1.204": apply_6_1_204,
 "प.6.1.205": apply_6_1_205,
 "प.6.1.206": apply_6_1_206,
 "प.6.1.207": apply_6_1_207,
 "प.6.1.208": apply_6_1_208,
 "प.6.1.209": apply_6_1_209,
 "प.6.1.210": apply_6_1_210,
 "प.6.1.211": apply_6_1_211,
 "प.6.1.212": apply_6_1_212,
 "प.6.1.213": apply_6_1_213,
 "प.6.1.214": apply_6_1_214,
 "प.6.1.215": apply_6_1_215,
 "प.6.1.216": apply_6_1_216,
 "प.6.1.217": apply_6_1_217,
 "प.6.1.218": apply_6_1_218,
 "प.6.1.219": apply_6_1_219,
 "प.6.1.220": apply_6_1_220,
 "प.6.1.221": apply_6_1_221,
 "प.6.1.222": apply_6_1_222,
 "प.6.1.223": apply_6_1_223,
}
