# -*- coding: utf-8 -*-
"""Shared apply_7_2_1..apply_7_2_118 functions for P.7.2.x — taddhita (secondary derivation).

P.7.2 covers vRddhi / guNa replacements before specific taddhita suffixes,
kRt affixes, and special samAsa / compound rules.
"""

VRDDHI = {chr(0x0936), chr(0x0910), chr(0x0914)}
GUNA = {chr(0x093f), chr(0x090f), chr(0x0913)}
IK = {chr(0x0907), chr(0x0909), chr(0x090b), chr(0x090c)}
IK_LONG = {chr(0x0908), chr(0x090a), chr(0x0940), chr(0x0944)}
VOWELS = VRDDHI | GUNA | IK | IK_LONG | {chr(0x0905)+chr(0x094d), chr(0x0905)+chr(0x0939)}


def _vrddhi_of(vowel):
	m = {chr(0x0907): chr(0x0910), chr(0x0909): chr(0x0914), chr(0x090b): chr(0x0914), chr(0x090c): chr(0x0914), chr(0x0905): chr(0x093e)}
	return m.get(vowel, vowel)


def _guna_of(vowel):
	m = {chr(0x0907): chr(0x090f), chr(0x0909): chr(0x0913), chr(0x090b): chr(0x0913), chr(0x090c): chr(0x0913), chr(0x0905): chr(0x0905)}
	return m.get(vowel, vowel)


def _analyse(word):
	if "+" not in word:
		return word, ""
	idx = word.index("+")
	return word[:idx], word[idx+1:]


def apply_7_2_1(word, pos="", SUTRA_TOKEN=""):
	"""si-ci vRddhiH parasmaipadeSu — vRddhi before sic in parasmaipada."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.1:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.1:vRddhi-before-si=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.1:no-vRddhi;" + word


def apply_7_2_2(word, pos="", SUTRA_TOKEN=""):
	"""ato lrAntasya — vRddhi of the final vowel of a stem ending in a before lR suffixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.2:input=" + word
	e1 = w1[-1] if w1 else ""
	if e1 == chr(0x0905):
		v = _vrddhi_of(e1)
		return "7.2.2:vRddhi-ato-lrAnta=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.2:no-lrAnta;" + word


def apply_7_2_3(word, pos="", SUTRA_TOKEN=""):
	"""vada-vraja-halantasya acaH — vRddhi before suffixes after vad, vraj, or hal-final stems."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.3:input=" + word
	e1 = w1[-1] if w1 else ""
	if e1 not in VOWELS:
		return "7.2.3:vRddhi-halanta;" + w1 + "+" + w2
	return "7.2.3:not-halanta;" + word


def apply_7_2_4(word, pos="", SUTRA_TOKEN=""):
	"""acaH — vRddhi of the final vowel before a following suffix starting with a vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.4:input=" + word
	e1 = w1[-1] if w1 else ""
	s2 = w2[0]
	if e1 in VOWELS and s2 in VOWELS:
		v = _vrddhi_of(e1)
		if v != e1:
			return "7.2.4:vRddhi-acaH=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.4:no-vRddhi;" + word


def apply_7_2_5(word, pos="", SUTRA_TOKEN=""):
	"""hm-y-anta-kSaNa-Svasa-jAgR-Ni-Svy-ed-itAm — no vRddhi for hm/y-final etc."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.5:input=" + word
	return "7.2.5:no-vRddhi-exceptions;" + word


def apply_7_2_6(word, pos="", SUTRA_TOKEN=""):
	"""naH — no vRddhi for n before certain suffixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.6:input=" + word
	if w1.endswith(chr(0x0928)):
		return "7.2.6:no-vRddhi-n;" + word
	return "7.2.6:apply-vRddhi;" + word


def apply_7_2_7(word, pos="", SUTRA_TOKEN=""):
	"""aH — no vRddhi for a-final before certain suffixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.7:input=" + word
	e1 = w1[-1] if w1 else ""
	if e1 == chr(0x0905):
		return "7.2.7:no-vRddhi-a;" + word
	return "7.2.7:apply-vRddhi;" + word


def apply_7_2_8(word, pos="", SUTRA_TOKEN=""):
	"""neD vaSi kRti — naH sArvadhAtuka-suffix: eD-Agama."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.8:input=" + word
	return "7.2.8:eD-Agama-flag;" + word


def apply_7_2_9(word, pos="", SUTRA_TOKEN=""):
	"""ato vRddhiH — vRddhi of a before a suffix in samAsa."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.9:input=" + word
	e1 = w1[-1] if w1 else ""
	if e1 == chr(0x0905):
		v = _vrddhi_of(e1)
		return "7.2.9:vRddhi-atoH=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.9:no-vRddhi-atoH;" + word


def apply_7_2_10(word, pos="", SUTRA_TOKEN=""):
	"""ekAca upadeze-anudAttAt — guNA after an anudAtt ekAca in upadeza."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.10:input=" + word
	e1 = w1[-1] if w1 else ""
	g = _guna_of(e1)
	if g != e1:
		return "7.2.10:gunaH=" + e1 + "->" + g + ";" + w1[:-1] + g + "+" + w2
	return "7.2.10:no-guna;" + word


def apply_7_2_11(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.11 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.11:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.11:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.11:no-vRddhi;" + word


def apply_7_2_12(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.12 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.12:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.12:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.12:no-vRddhi;" + word


def apply_7_2_13(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.13 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.13:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.13:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.13:no-vRddhi;" + word


def apply_7_2_14(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.14 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.14:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.14:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.14:no-vRddhi;" + word


def apply_7_2_15(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.15 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.15:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.15:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.15:no-vRddhi;" + word


def apply_7_2_16(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.16 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.16:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.16:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.16:no-vRddhi;" + word


def apply_7_2_17(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.17 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.17:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.17:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.17:no-vRddhi;" + word


def apply_7_2_18(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.18 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.18:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.18:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.18:no-vRddhi;" + word


def apply_7_2_19(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.19 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.19:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.19:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.19:no-vRddhi;" + word


def apply_7_2_20(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.20 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.20:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.20:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.20:no-vRddhi;" + word


def apply_7_2_21(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.21 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.21:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.21:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.21:no-vRddhi;" + word


def apply_7_2_22(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.22 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.22:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.22:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.22:no-vRddhi;" + word


def apply_7_2_23(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.23 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.23:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.23:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.23:no-vRddhi;" + word


def apply_7_2_24(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.24 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.24:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.24:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.24:no-vRddhi;" + word


def apply_7_2_25(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.25 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.25:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.25:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.25:no-vRddhi;" + word


def apply_7_2_26(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.26 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.26:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.26:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.26:no-vRddhi;" + word


def apply_7_2_27(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.27 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.27:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.27:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.27:no-vRddhi;" + word


def apply_7_2_28(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.28 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.28:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.28:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.28:no-vRddhi;" + word


def apply_7_2_29(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.29 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.29:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.29:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.29:no-vRddhi;" + word


def apply_7_2_30(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.30 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.30:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.30:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.30:no-vRddhi;" + word


def apply_7_2_31(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.31 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.31:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.31:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.31:no-vRddhi;" + word


def apply_7_2_32(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.32 — guNA before kiti suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.32:input=" + word
	e1 = w1[-1] if w1 else ""
	g = _guna_of(e1)
	if g != e1:
		return "7.2.32:gunaH=" + e1 + "->" + g + ";" + w1[:-1] + g + "+" + w2
	return "7.2.32:no-guna;" + word


def apply_7_2_33(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.33 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.33:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.33:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.33:no-vRddhi;" + word


def apply_7_2_34(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.34 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.34:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.34:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.34:no-vRddhi;" + word


def apply_7_2_35(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.35 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.35:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.35:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.35:no-vRddhi;" + word


def apply_7_2_36(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.36 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.36:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.36:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.36:no-vRddhi;" + word


def apply_7_2_37(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.37 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.37:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.37:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.37:no-vRddhi;" + word


def apply_7_2_38(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.38 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.38:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.38:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.38:no-vRddhi;" + word


def apply_7_2_39(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.39 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.39:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.39:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.39:no-vRddhi;" + word


def apply_7_2_40(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.40 — guNA before lat-sit-am."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.40:input=" + word
	e1 = w1[-1] if w1 else ""
	g = _guna_of(e1)
	if g != e1:
		return "7.2.40:gunaH=" + e1 + "->" + g + ";" + w1[:-1] + g + "+" + w2
	return "7.2.40:no-guna;" + word


def apply_7_2_41(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.41 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.41:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.41:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.41:no-vRddhi;" + word


def apply_7_2_42(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.42 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.42:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.42:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.42:no-vRddhi;" + word


def apply_7_2_43(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.43 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.43:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.43:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.43:no-vRddhi;" + word


def apply_7_2_44(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.44 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.44:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.44:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.44:no-vRddhi;" + word


def apply_7_2_45(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.45 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.45:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.45:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.45:no-vRddhi;" + word


def apply_7_2_46(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.46 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.46:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.46:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.46:no-vRddhi;" + word


def apply_7_2_47(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.47 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.47:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.47:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.47:no-vRddhi;" + word


def apply_7_2_48(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.48 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.48:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.48:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.48:no-vRddhi;" + word


def apply_7_2_49(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.49 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.49:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.49:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.49:no-vRddhi;" + word


def apply_7_2_50(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.50 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.50:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.50:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.50:no-vRddhi;" + word


def apply_7_2_51(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.51 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.51:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.51:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.51:no-vRddhi;" + word


def apply_7_2_52(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.52 — vRddhi before ktvoH."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.52:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.52:vRddhi-ktvoH=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.52:no-vRddhi;" + word


def apply_7_2_53(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.53 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.53:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.53:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.53:no-vRddhi;" + word


def apply_7_2_54(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.54 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.54:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.54:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.54:no-vRddhi;" + word


def apply_7_2_55(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.55 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.55:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.55:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.55:no-vRddhi;" + word


def apply_7_2_56(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.56 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.56:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.56:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.56:no-vRddhi;" + word


def apply_7_2_57(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.57 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.57:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.57:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.57:no-vRddhi;" + word


def apply_7_2_58(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.58 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.58:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.58:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.58:no-vRddhi;" + word


def apply_7_2_59(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.59 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.59:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.59:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.59:no-vRddhi;" + word


def apply_7_2_60(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.60 — guNA before aci SnuH."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.60:input=" + word
	e1 = w1[-1] if w1 else ""
	g = _guna_of(e1)
	if g != e1:
		return "7.2.60:gunaH=" + e1 + "->" + g + ";" + w1[:-1] + g + "+" + w2
	return "7.2.60:no-guna;" + word


def apply_7_2_61(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.61 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.61:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.61:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.61:no-vRddhi;" + word


def apply_7_2_62(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.62 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.62:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.62:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.62:no-vRddhi;" + word


def apply_7_2_63(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.63 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.63:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.63:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.63:no-vRddhi;" + word


def apply_7_2_64(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.64 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.64:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.64:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.64:no-vRddhi;" + word


def apply_7_2_65(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.65 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.65:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.65:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.65:no-vRddhi;" + word


def apply_7_2_66(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.66 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.66:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.66:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.66:no-vRddhi;" + word


def apply_7_2_67(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.67 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.67:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.67:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.67:no-vRddhi;" + word


def apply_7_2_68(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.68 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.68:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.68:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.68:no-vRddhi;" + word


def apply_7_2_69(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.69 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.69:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.69:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.69:no-vRddhi;" + word


def apply_7_2_70(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.70 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.70:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.70:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.70:no-vRddhi;" + word


def apply_7_2_71(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.71 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.71:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.71:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.71:no-vRddhi;" + word


def apply_7_2_72(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.72 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.72:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.72:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.72:no-vRddhi;" + word


def apply_7_2_73(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.73 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.73:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.73:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.73:no-vRddhi;" + word


def apply_7_2_74(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.74 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.74:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.74:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.74:no-vRddhi;" + word


def apply_7_2_75(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.75 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.75:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.75:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.75:no-vRddhi;" + word


def apply_7_2_76(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.76 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.76:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.76:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.76:no-vRddhi;" + word


def apply_7_2_77(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.77 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.77:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.77:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.77:no-vRddhi;" + word


def apply_7_2_78(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.78 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.78:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.78:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.78:no-vRddhi;" + word


def apply_7_2_79(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.79 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.79:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.79:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.79:no-vRddhi;" + word


def apply_7_2_80(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.80 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.80:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.80:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.80:no-vRddhi;" + word


def apply_7_2_81(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.81 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.81:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.81:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.81:no-vRddhi;" + word


def apply_7_2_82(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.82 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.82:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.82:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.82:no-vRddhi;" + word


def apply_7_2_83(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.83 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.83:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.83:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.83:no-vRddhi;" + word


def apply_7_2_84(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.84 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.84:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.84:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.84:no-vRddhi;" + word


def apply_7_2_85(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.85 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.85:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.85:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.85:no-vRddhi;" + word


def apply_7_2_86(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.86 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.86:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.86:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.86:no-vRddhi;" + word


def apply_7_2_87(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.87 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.87:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.87:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.87:no-vRddhi;" + word


def apply_7_2_88(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.88 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.88:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.88:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.88:no-vRddhi;" + word


def apply_7_2_89(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.89 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.89:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.89:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.89:no-vRddhi;" + word


def apply_7_2_90(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.90 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.90:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.90:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.90:no-vRddhi;" + word


def apply_7_2_91(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.91 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.91:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.91:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.91:no-vRddhi;" + word


def apply_7_2_92(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.92 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.92:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.92:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.92:no-vRddhi;" + word


def apply_7_2_93(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.93 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.93:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.93:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.93:no-vRddhi;" + word


def apply_7_2_94(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.94 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.94:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.94:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.94:no-vRddhi;" + word


def apply_7_2_95(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.95 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.95:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.95:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.95:no-vRddhi;" + word


def apply_7_2_96(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.96 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.96:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.96:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.96:no-vRddhi;" + word


def apply_7_2_97(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.97 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.97:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.97:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.97:no-vRddhi;" + word


def apply_7_2_98(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.98 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.98:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.98:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.98:no-vRddhi;" + word


def apply_7_2_99(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.99 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.99:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.99:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.99:no-vRddhi;" + word


def apply_7_2_100(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.100 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.100:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.100:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.100:no-vRddhi;" + word


def apply_7_2_101(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.101 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.101:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.101:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.101:no-vRddhi;" + word


def apply_7_2_102(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.102 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.102:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.102:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.102:no-vRddhi;" + word


def apply_7_2_103(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.103 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.103:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.103:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.103:no-vRddhi;" + word


def apply_7_2_104(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.104 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.104:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.104:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.104:no-vRddhi;" + word


def apply_7_2_105(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.105 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.105:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.105:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.105:no-vRddhi;" + word


def apply_7_2_106(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.106 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.106:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.106:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.106:no-vRddhi;" + word


def apply_7_2_107(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.107 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.107:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.107:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.107:no-vRddhi;" + word


def apply_7_2_108(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.108 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.108:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.108:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.108:no-vRddhi;" + word


def apply_7_2_109(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.109 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.109:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.109:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.109:no-vRddhi;" + word


def apply_7_2_110(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.110 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.110:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.110:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.110:no-vRddhi;" + word


def apply_7_2_111(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.111 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.111:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.111:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.111:no-vRddhi;" + word


def apply_7_2_112(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.112 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.112:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.112:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.112:no-vRddhi;" + word


def apply_7_2_113(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.113 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.113:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.113:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.113:no-vRddhi;" + word


def apply_7_2_114(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.114 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.114:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.114:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.114:no-vRddhi;" + word


def apply_7_2_115(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.115 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.115:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.115:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.115:no-vRddhi;" + word


def apply_7_2_116(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.116 — vRddhi before specified consonant suffix."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.116:input=" + word
	e1 = w1[-1] if w1 else ""
	v = _vrddhi_of(e1)
	if v != e1:
		return "7.2.116:vRddhi=" + e1 + "->" + v + ";" + w1[:-1] + v + "+" + w2
	return "7.2.116:no-vRddhi;" + word


def apply_7_2_117(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.117 — atoH: no change rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.117:input=" + word
	return "7.2.117:no-change;" + word


def apply_7_2_118(word, pos="", SUTRA_TOKEN=""):
	"""P.7.2.118 — guni: guNA before a vowel following a guNa vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return "7.2.118:input=" + word
	e1 = w1[-1] if w1 else ""
	g = _guna_of(e1)
	if g != e1:
		return "7.2.118:guni=" + e1 + "->" + g + ";" + w1[:-1] + g + "+" + w2
	return "7.2.118:no-guni;" + word


ALL_7_2 = {
	"प.7.2.1": apply_7_2_1,
	"प.7.2.2": apply_7_2_2,
	"प.7.2.3": apply_7_2_3,
	"प.7.2.4": apply_7_2_4,
	"प.7.2.5": apply_7_2_5,
	"प.7.2.6": apply_7_2_6,
	"प.7.2.7": apply_7_2_7,
	"प.7.2.8": apply_7_2_8,
	"प.7.2.9": apply_7_2_9,
	"प.7.2.10": apply_7_2_10,
	"प.7.2.11": apply_7_2_11,
	"प.7.2.12": apply_7_2_12,
	"प.7.2.13": apply_7_2_13,
	"प.7.2.14": apply_7_2_14,
	"प.7.2.15": apply_7_2_15,
	"प.7.2.16": apply_7_2_16,
	"प.7.2.17": apply_7_2_17,
	"प.7.2.18": apply_7_2_18,
	"प.7.2.19": apply_7_2_19,
	"प.7.2.20": apply_7_2_20,
	"प.7.2.21": apply_7_2_21,
	"प.7.2.22": apply_7_2_22,
	"प.7.2.23": apply_7_2_23,
	"प.7.2.24": apply_7_2_24,
	"प.7.2.25": apply_7_2_25,
	"प.7.2.26": apply_7_2_26,
	"प.7.2.27": apply_7_2_27,
	"प.7.2.28": apply_7_2_28,
	"प.7.2.29": apply_7_2_29,
	"प.7.2.30": apply_7_2_30,
	"प.7.2.31": apply_7_2_31,
	"प.7.2.32": apply_7_2_32,
	"प.7.2.33": apply_7_2_33,
	"प.7.2.34": apply_7_2_34,
	"प.7.2.35": apply_7_2_35,
	"प.7.2.36": apply_7_2_36,
	"प.7.2.37": apply_7_2_37,
	"प.7.2.38": apply_7_2_38,
	"प.7.2.39": apply_7_2_39,
	"प.7.2.40": apply_7_2_40,
	"प.7.2.41": apply_7_2_41,
	"प.7.2.42": apply_7_2_42,
	"प.7.2.43": apply_7_2_43,
	"प.7.2.44": apply_7_2_44,
	"प.7.2.45": apply_7_2_45,
	"प.7.2.46": apply_7_2_46,
	"प.7.2.47": apply_7_2_47,
	"प.7.2.48": apply_7_2_48,
	"प.7.2.49": apply_7_2_49,
	"प.7.2.50": apply_7_2_50,
	"प.7.2.51": apply_7_2_51,
	"प.7.2.52": apply_7_2_52,
	"प.7.2.53": apply_7_2_53,
	"प.7.2.54": apply_7_2_54,
	"प.7.2.55": apply_7_2_55,
	"प.7.2.56": apply_7_2_56,
	"प.7.2.57": apply_7_2_57,
	"प.7.2.58": apply_7_2_58,
	"प.7.2.59": apply_7_2_59,
	"प.7.2.60": apply_7_2_60,
	"प.7.2.61": apply_7_2_61,
	"प.7.2.62": apply_7_2_62,
	"प.7.2.63": apply_7_2_63,
	"प.7.2.64": apply_7_2_64,
	"प.7.2.65": apply_7_2_65,
	"प.7.2.66": apply_7_2_66,
	"प.7.2.67": apply_7_2_67,
	"प.7.2.68": apply_7_2_68,
	"प.7.2.69": apply_7_2_69,
	"प.7.2.70": apply_7_2_70,
	"प.7.2.71": apply_7_2_71,
	"प.7.2.72": apply_7_2_72,
	"प.7.2.73": apply_7_2_73,
	"प.7.2.74": apply_7_2_74,
	"प.7.2.75": apply_7_2_75,
	"प.7.2.76": apply_7_2_76,
	"प.7.2.77": apply_7_2_77,
	"प.7.2.78": apply_7_2_78,
	"प.7.2.79": apply_7_2_79,
	"प.7.2.80": apply_7_2_80,
	"प.7.2.81": apply_7_2_81,
	"प.7.2.82": apply_7_2_82,
	"प.7.2.83": apply_7_2_83,
	"प.7.2.84": apply_7_2_84,
	"प.7.2.85": apply_7_2_85,
	"प.7.2.86": apply_7_2_86,
	"प.7.2.87": apply_7_2_87,
	"प.7.2.88": apply_7_2_88,
	"प.7.2.89": apply_7_2_89,
	"प.7.2.90": apply_7_2_90,
	"प.7.2.91": apply_7_2_91,
	"प.7.2.92": apply_7_2_92,
	"प.7.2.93": apply_7_2_93,
	"प.7.2.94": apply_7_2_94,
	"प.7.2.95": apply_7_2_95,
	"प.7.2.96": apply_7_2_96,
	"प.7.2.97": apply_7_2_97,
	"प.7.2.98": apply_7_2_98,
	"प.7.2.99": apply_7_2_99,
	"प.7.2.100": apply_7_2_100,
	"प.7.2.101": apply_7_2_101,
	"प.7.2.102": apply_7_2_102,
	"प.7.2.103": apply_7_2_103,
	"प.7.2.104": apply_7_2_104,
	"प.7.2.105": apply_7_2_105,
	"प.7.2.106": apply_7_2_106,
	"प.7.2.107": apply_7_2_107,
	"प.7.2.108": apply_7_2_108,
	"प.7.2.109": apply_7_2_109,
	"प.7.2.110": apply_7_2_110,
	"प.7.2.111": apply_7_2_111,
	"प.7.2.112": apply_7_2_112,
	"प.7.2.113": apply_7_2_113,
	"प.7.2.114": apply_7_2_114,
	"प.7.2.115": apply_7_2_115,
	"प.7.2.116": apply_7_2_116,
	"प.7.2.117": apply_7_2_117,
	"प.7.2.118": apply_7_2_118,
	}
