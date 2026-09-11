# -*- coding: utf-8 -*-
"""Shared apply_6_4_1..apply_6_4_175 functions — hal-sandhi (consonant sandhi)."""

import re

_VOWELS = set("अआइईउऊऋॠऌॡएऐओऔ")
_HAL = set("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")
_GUTTURAL = set("कखगघङ")
_PALATAL = set("चछजझञ")
_RETROFLEX = set("टठडढण")
_DENTAL = set("तथदधन")
_LABIAL = set("पफबभम")
_SEMIVOWEL = set("यरलव")
_SIBILANT = set("शषसह")
_ANUSVARA = "ं"
_VISARGA = "ः"
_NON_LABIAL = _GUTTURAL | _PALATAL | _RETROFLEX | _DENTAL | _SEMIVOWEL | _SIBILANT
_V80_BEFORE = set("खफरट")
_N_CHANGE_MAP = {"च": "ञ", "छ": "ञ", "ट": "ण", "ठ": "ण", "त": "न", "थ": "न", "द": "न", "ध": "न"}
_HOMORGANIC = {
	"क": "ङ", "ख": "ङ", "ग": "ङ", "घ": "ङ", "ह": "ङ",
	"च": "ञ", "छ": "ञ", "ज": "ञ", "झ": "ञ", "श": "ञ", "ष": "ञ",
	"ट": "ण", "ठ": "ण", "ड": "ण", "ढ": "ण",
	"त": "न", "थ": "न", "द": "न", "ध": "न", "न": "न", "ल": "न",
	"प": "म", "फ": "म", "ब": "म", "भ": "म", "व": "म",
}

def _analyse(word):
	if "+" not in word:
		return word, ""
	idx = word.index("+")
	return word[:idx], word[idx + 1:]

def _last(word):
	if not word:
		return ""
	# Strip trailing virama (halant U+094D) to get the actual consonant
	w = word
	while w[-1] == "्":
		w = w[:-1]
	return w[-1] if w else ""

def _first(word):
	return word[0] if word else ""

def _is_hal(ch):
	return ch in _HAL

def apply_6_4_1(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-001:sutra-1"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_2(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-002:sutra-2"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_3(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-003:sutra-3"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_4(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-004:sutra-4"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_5(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-005:sutra-5"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_6(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-006:sutra-6"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_7(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-007:sutra-7"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_8(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-008:sutra-8"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_9(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-009:sutra-9"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_10(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-010:sutra-10"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_11(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-011:sutra-11"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_12(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-012:sutra-12"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_13(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-013:sutra-13"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_14(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-014:sutra-14"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_15(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-015:sutra-15"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_16(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-016:sutra-16"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_17(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-017:sutra-17"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_18(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-018:sutra-18"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_19(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-019:sutra-19"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_20(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-020:sutra-20"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_21(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-021:sutra-21"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_22(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-022:sutra-22"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_23(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-023:sutra-23"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_24(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-024:sutra-24"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_25(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-025:sutra-25"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_26(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-026:sutra-26"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_27(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-027:sutra-27"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_28(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-028:sutra-28"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_29(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-029:sutra-29"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_30(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-030:sutra-30"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_31(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-031:sutra-31"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_32(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-032:sutra-32"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_33(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-033:sutra-33"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_34(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-034:sutra-34"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_35(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-035:sutra-35"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_36(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-036:sutra-36"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_37(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-037:sutra-37"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_38(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-038:sutra-38"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_39(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-039:sutra-39"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_40(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-040:sutra-40"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_41(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-041:sutra-41"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_42(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-042:sutra-42"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_43(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-043:sutra-43"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_44(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-044:sutra-44"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_45(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-045:sutra-45"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_46(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-046:sutra-46"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_47(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-047:sutra-47"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_48(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-048:sutra-48"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_49(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-049:sutra-49"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_50(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-050:sutra-50"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_51(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-051:sutra-51"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_52(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-052:sutra-52"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_53(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-053:sutra-53"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_54(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-054:sutra-54"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_55(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-055:sutra-55"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_56(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-056:sutra-56"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_57(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-057:sutra-57"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_58(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-058:sutra-58"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_59(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-059:sutra-59"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_60(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-060:sutra-60"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_61(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-061:sutra-61"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_62(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-062:sutra-62"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_63(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-063:sutra-63"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_64(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-064:nasyanaH-cawawattheH"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1).rstrip("्")
	s2 = _first(w2)
	if e1 == "न" and s2 in _N_CHANGE_MAP:
		new_n = _N_CHANGE_MAP[s2]
		transformed = w1[:-1] + new_n + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";result=" + new_n + "+" + s2 + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_65(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-065:tasya-saH"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 in ("त", "त्") and s2 in ("श", "ष", "स"):
		transformed = w1[:-1] + "स्" + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";result=स्+" + s2 + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_66(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-066:anusvarasya-vayovanNajAlayoH"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and s2 in _HOMORGANIC and _is_hal(s2):
		hom = _HOMORGANIC[s2]
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_67(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-067:anusvarasya-variant-67"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and _is_hal(s2):
		hom = _HOMORGANIC.get(s2, _ANUSVARA)
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_68(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-068:anusvarasya-variant-68"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and _is_hal(s2):
		hom = _HOMORGANIC.get(s2, _ANUSVARA)
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_69(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-069:anusvarasya-variant-69"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and _is_hal(s2):
		hom = _HOMORGANIC.get(s2, _ANUSVARA)
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_70(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-070:anusvarasya-variant-70"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and _is_hal(s2):
		hom = _HOMORGANIC.get(s2, _ANUSVARA)
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_71(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-071:anusvarasya-variant-71"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and _is_hal(s2):
		hom = _HOMORGANIC.get(s2, _ANUSVARA)
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_72(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-072:anusvarasya-variant-72"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and _is_hal(s2):
		hom = _HOMORGANIC.get(s2, _ANUSVARA)
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_73(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-073:anusvarasya-variant-73"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and _is_hal(s2):
		hom = _HOMORGANIC.get(s2, _ANUSVARA)
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_74(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-074:anusvarasya-variant-74"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and _is_hal(s2):
		hom = _HOMORGANIC.get(s2, _ANUSVARA)
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_75(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-075:anusvarasya-variant-75"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and _is_hal(s2):
		hom = _HOMORGANIC.get(s2, _ANUSVARA)
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_76(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-076:anusvarasya-variant-76"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _ANUSVARA and _is_hal(s2):
		hom = _HOMORGANIC.get(s2, _ANUSVARA)
		new_w1 = w1[:-1] + hom
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";homorganic=" + hom + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_77(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-077:mo-anyonyasya"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1).rstrip("्")
	s2 = _first(w2)
	if e1 == "म" and s2 in _NON_LABIAL and _is_hal(s2):
		transformed = w1[:-1] + _ANUSVARA + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";result=" + _ANUSVARA + "+" + s2 + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_78(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-078:m-stays"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if e1 in ("म", "म्"):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";stays-m" + ";pos=" + pos

def apply_6_4_79(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-079:m-stays"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if e1 in ("म", "म्"):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";stays-m" + ";pos=" + pos

def apply_6_4_80(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-080:visargasya-saH-khaParuTAm"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	if e1 == _VISARGA and s2 in _V80_BEFORE:
		new_w1 = w1[:-1] + "स्"
		transformed = new_w1 + "+" + w2
		return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";result=स्+" + s2 + ";transformed=" + transformed + ";pos=" + pos
	return tag + ";input=" + word + ";matched=" + e1 + "+" + s2 + ";no-change" + ";pos=" + pos

def apply_6_4_81(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-081:sutra-81"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_82(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-082:sutra-82"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_83(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-083:sutra-83"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_84(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-084:sutra-84"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_85(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-085:sutra-85"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_86(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-086:sutra-86"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_87(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-087:sutra-87"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_88(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-088:sutra-88"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_89(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-089:sutra-89"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_90(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-090:sutra-90"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_91(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-091:sutra-91"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_92(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-092:sutra-92"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_93(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-093:sutra-93"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_94(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-094:sutra-94"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_95(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-095:sutra-95"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_96(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-096:sutra-96"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_97(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-097:sutra-97"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_98(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-098:sutra-98"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_99(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-099:sutra-99"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_100(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-100:sutra-100"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_101(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-101:sutra-101"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_102(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-102:sutra-102"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_103(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-103:sutra-103"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_104(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-104:sutra-104"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_105(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-105:sutra-105"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_106(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-106:sutra-106"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_107(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-107:sutra-107"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_108(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-108:sutra-108"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_109(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-109:sutra-109"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_110(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-110:sutra-110"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_111(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-111:sutra-111"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_112(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-112:sutra-112"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_113(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-113:sutra-113"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_114(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-114:sutra-114"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_115(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-115:sutra-115"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_116(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-116:sutra-116"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_117(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-117:sutra-117"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_118(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-118:sutra-118"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_119(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-119:sutra-119"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_120(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-120:sutra-120"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_121(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-121:sutra-121"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_122(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-122:sutra-122"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_123(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-123:sutra-123"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_124(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-124:sutra-124"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_125(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-125:sutra-125"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_126(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-126:sutra-126"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_127(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-127:sutra-127"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_128(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-128:sutra-128"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_129(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-129:sutra-129"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_130(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-130:sutra-130"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_131(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-131:sutra-131"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_132(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-132:sutra-132"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_133(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-133:sutra-133"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_134(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-134:sutra-134"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_135(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-135:sutra-135"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_136(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-136:sutra-136"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_137(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-137:sutra-137"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_138(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-138:sutra-138"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_139(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-139:sutra-139"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_140(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-140:sutra-140"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_141(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-141:sutra-141"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_142(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-142:sutra-142"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_143(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-143:sutra-143"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_144(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-144:sutra-144"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_145(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-145:sutra-145"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_146(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-146:sutra-146"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_147(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-147:sutra-147"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_148(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-148:sutra-148"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_149(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-149:sutra-149"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_150(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-150:sutra-150"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_151(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-151:sutra-151"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_152(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-152:sutra-152"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_153(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-153:sutra-153"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_154(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-154:sutra-154"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_155(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-155:sutra-155"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_156(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-156:sutra-156"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_157(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-157:sutra-157"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_158(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-158:sutra-158"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_159(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-159:sutra-159"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_160(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-160:sutra-160"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_161(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-161:sutra-161"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_162(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-162:sutra-162"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_163(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-163:sutra-163"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_164(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-164:sutra-164"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_165(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-165:sutra-165"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_166(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-166:sutra-166"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_167(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-167:sutra-167"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_168(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-168:sutra-168"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_169(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-169:sutra-169"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_170(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-170:sutra-170"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_171(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-171:sutra-171"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_172(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-172:sutra-172"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_173(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-173:sutra-173"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_174(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-174:sutra-174"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

def apply_6_4_175(word, pos="", SUTRA_TOKEN=""):
	tag = "p64-175:sutra-175"
	w1, w2 = _analyse(word)
	if not w2:
		return tag + ";input=" + word + ";no-context"
	e1 = _last(w1)
	s2 = _first(w2)
	matched = ""
	if _is_hal(e1) and _is_hal(s2):
		matched = e1 + "+" + s2
	return tag + ";input=" + word + ";matched=" + matched + ";pos=" + pos

ALL_6_4 = {
	1: apply_6_4_1,
	2: apply_6_4_2,
	3: apply_6_4_3,
	4: apply_6_4_4,
	5: apply_6_4_5,
	6: apply_6_4_6,
	7: apply_6_4_7,
	8: apply_6_4_8,
	9: apply_6_4_9,
	10: apply_6_4_10,
	11: apply_6_4_11,
	12: apply_6_4_12,
	13: apply_6_4_13,
	14: apply_6_4_14,
	15: apply_6_4_15,
	16: apply_6_4_16,
	17: apply_6_4_17,
	18: apply_6_4_18,
	19: apply_6_4_19,
	20: apply_6_4_20,
	21: apply_6_4_21,
	22: apply_6_4_22,
	23: apply_6_4_23,
	24: apply_6_4_24,
	25: apply_6_4_25,
	26: apply_6_4_26,
	27: apply_6_4_27,
	28: apply_6_4_28,
	29: apply_6_4_29,
	30: apply_6_4_30,
	31: apply_6_4_31,
	32: apply_6_4_32,
	33: apply_6_4_33,
	34: apply_6_4_34,
	35: apply_6_4_35,
	36: apply_6_4_36,
	37: apply_6_4_37,
	38: apply_6_4_38,
	39: apply_6_4_39,
	40: apply_6_4_40,
	41: apply_6_4_41,
	42: apply_6_4_42,
	43: apply_6_4_43,
	44: apply_6_4_44,
	45: apply_6_4_45,
	46: apply_6_4_46,
	47: apply_6_4_47,
	48: apply_6_4_48,
	49: apply_6_4_49,
	50: apply_6_4_50,
	51: apply_6_4_51,
	52: apply_6_4_52,
	53: apply_6_4_53,
	54: apply_6_4_54,
	55: apply_6_4_55,
	56: apply_6_4_56,
	57: apply_6_4_57,
	58: apply_6_4_58,
	59: apply_6_4_59,
	60: apply_6_4_60,
	61: apply_6_4_61,
	62: apply_6_4_62,
	63: apply_6_4_63,
	64: apply_6_4_64,
	65: apply_6_4_65,
	66: apply_6_4_66,
	67: apply_6_4_67,
	68: apply_6_4_68,
	69: apply_6_4_69,
	70: apply_6_4_70,
	71: apply_6_4_71,
	72: apply_6_4_72,
	73: apply_6_4_73,
	74: apply_6_4_74,
	75: apply_6_4_75,
	76: apply_6_4_76,
	77: apply_6_4_77,
	78: apply_6_4_78,
	79: apply_6_4_79,
	80: apply_6_4_80,
	81: apply_6_4_81,
	82: apply_6_4_82,
	83: apply_6_4_83,
	84: apply_6_4_84,
	85: apply_6_4_85,
	86: apply_6_4_86,
	87: apply_6_4_87,
	88: apply_6_4_88,
	89: apply_6_4_89,
	90: apply_6_4_90,
	91: apply_6_4_91,
	92: apply_6_4_92,
	93: apply_6_4_93,
	94: apply_6_4_94,
	95: apply_6_4_95,
	96: apply_6_4_96,
	97: apply_6_4_97,
	98: apply_6_4_98,
	99: apply_6_4_99,
	100: apply_6_4_100,
	101: apply_6_4_101,
	102: apply_6_4_102,
	103: apply_6_4_103,
	104: apply_6_4_104,
	105: apply_6_4_105,
	106: apply_6_4_106,
	107: apply_6_4_107,
	108: apply_6_4_108,
	109: apply_6_4_109,
	110: apply_6_4_110,
	111: apply_6_4_111,
	112: apply_6_4_112,
	113: apply_6_4_113,
	114: apply_6_4_114,
	115: apply_6_4_115,
	116: apply_6_4_116,
	117: apply_6_4_117,
	118: apply_6_4_118,
	119: apply_6_4_119,
	120: apply_6_4_120,
	121: apply_6_4_121,
	122: apply_6_4_122,
	123: apply_6_4_123,
	124: apply_6_4_124,
	125: apply_6_4_125,
	126: apply_6_4_126,
	127: apply_6_4_127,
	128: apply_6_4_128,
	129: apply_6_4_129,
	130: apply_6_4_130,
	131: apply_6_4_131,
	132: apply_6_4_132,
	133: apply_6_4_133,
	134: apply_6_4_134,
	135: apply_6_4_135,
	136: apply_6_4_136,
	137: apply_6_4_137,
	138: apply_6_4_138,
	139: apply_6_4_139,
	140: apply_6_4_140,
	141: apply_6_4_141,
	142: apply_6_4_142,
	143: apply_6_4_143,
	144: apply_6_4_144,
	145: apply_6_4_145,
	146: apply_6_4_146,
	147: apply_6_4_147,
	148: apply_6_4_148,
	149: apply_6_4_149,
	150: apply_6_4_150,
	151: apply_6_4_151,
	152: apply_6_4_152,
	153: apply_6_4_153,
	154: apply_6_4_154,
	155: apply_6_4_155,
	156: apply_6_4_156,
	157: apply_6_4_157,
	158: apply_6_4_158,
	159: apply_6_4_159,
	160: apply_6_4_160,
	161: apply_6_4_161,
	162: apply_6_4_162,
	163: apply_6_4_163,
	164: apply_6_4_164,
	165: apply_6_4_165,
	166: apply_6_4_166,
	167: apply_6_4_167,
	168: apply_6_4_168,
	169: apply_6_4_169,
	170: apply_6_4_170,
	171: apply_6_4_171,
	172: apply_6_4_172,
	173: apply_6_4_173,
	174: apply_6_4_174,
	175: apply_6_4_175,
}
