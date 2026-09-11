"""Devanagari sandhi splitter for Sanskrit.

Strategy (greedy longest-match with phonotactic rules):
1. Try common sandhi splits at known boundaries
2. Apply dvitva (double → single consonant) rule
3. Apply ik→ya (P.6.1.77) rule
4. Apply vrddhi rule before vowels
5. Apply n (पठ्+इति → पठन्) → नम् (नासीत् → न+आसीत्)

Rules are ordered by specificity.
"""
from __future__ import annotations

import re

# ── phoneme inventory ────────────────────────────────────────────────────────
VRDDHI = {"आ", "ऐ", "औ"}
GUNA = {"अ", "ए", "ओ"}
IK = {"इ", "उ", "ऋ", "ऌ"}
IK_ALL = IK | {"ई", "ऊ", "ॠ", "ॡ"}
AC = VRDDHI | GUNA | IK_ALL
HAL = set("कखगघङचछजझञटठडढणतथदधनपफबभयरलवशषसह")
VOWELS = AC | {"अ", "अः", "अम्"}
MATRA = set("ािीुूृेैोौ")
CONSONANTS = HAL | {"ङ", "ञ", "ण", "न", "म"}

def _is_vowel(c: str) -> bool:
	return c in VOWELS

def _ends_with_vowel(s: str) -> bool:
	return bool(s) and s[-1] in VOWELS

def _starts_with_vowel(s: str) -> bool:
	return bool(s) and s[0] in VOWELS

def _ends_with_consonant(s: str) -> bool:
	return bool(s) and s[-1] in CONSONANTS


# ── Rule 1: Dvitva (P.6.1.1) — double consonant → single ────────────────────

def _apply_dvitva(word: str) -> list:
	"""If last two chars are same consonant, split after the first one.
	e.g. अग्निः+इष्यते → agni + iṣyate (अग्निष्यते, split → अग्नि + इष्यते)"""
	results = []
	for i in range(len(word) - 1):
		c1, c2 = word[i], word[i+1]
		if c1 == c2 and c1 in HAL:
			part1 = word[:i+1]
			part2 = word[i+1:]
			# part2 loses one consonant (the dvitva reduction)
			part2 = part2[1:]
			# If part2 still starts with something and ends, yield split
			if part1 and part2:
				results.append(part1 + "+" + part2)
	# Also try matching known ending patterns after dvitva
	# e.g. कर्माणि → कर्म + ाणि (but actually it's कर्म + णि via adesa)
	# For now, just return dvitva splits
	return results


# ── Rule 2: ik→ya (P.6.1.77) before vowel ───────────────────────────────────

YAN_MAP = {"इ": "य", "उ": "व", "ऋ": "र", "ऌ": "ल"}

def _apply_ik_yan(word: str) -> list:
	"""ik sound followed by vowel → corresponding yan sound.
	e.g. प्रति+इ → प्रतिय्, अत्+इति → अतिय्"""
	results = []
	for i in range(len(word) - 1):
		c1 = word[i]
		c2 = word[i+1]
		if c1 in YAN_MAP and _is_vowel(c2):
			part1 = word[:i+1]
			part2 = word[i+1:]
			ya = YAN_MAP[c1]
			results.append(part1 + ya + "+" + part2)
	return results


# ── Rule 3: n→ṇ before dental (P.8.4.1) and similar ─────────────────────────

def _apply_nuna(word: str) -> list:
	"""न् before dental → ण् (nUN).
	e.g. गुरु+इन् → गुरुणिन्, but more commonly: सन्+इति → सन्निति"""
	results = []
	# nUN: n → ṇ before dental
	DENTAL = set("तथदधनलस")
	for i in range(len(word) - 1):
		if word[i] == "न" and word[i+1] in DENTAL:
			results.append(word[:i+1] + "ँ" + word[i+1:])
	return results


# ── Rule 4: Scrape off common affixes ────────────────────────────────────────

# Case endings (sup) — longest first
_SUP_ENDINGS = [
	("इनाम्", "g pl"), ("आम्", "g"), ("औस्", "d"), ("अम्यौ", "d acc"),
	("अस्", "a/d"), ("अम्", "d acc"), ("सु", "s"), ("आम्", "d"),
	("इ", "s loc"), ("ओः", "d dat"), ("अन्त", "loc"),
	("तस्", "a/d"), ("त्रा", "dat"), ("अर्थे", "dat"),
	("जस्", "d"), ("औ", "d/s"), ("अमि", "p acc"),
]

# tiG endings — longest first
_TIG_ENDINGS = [
	("ध्वम्", "2p"), ("आथाम्", "2d"), ("थास्", "2s"),
	("स्व्", "2s"), ("मस्", "1p"), ("मतम्", "2d"),
	("वस्", "1d"), ("तिप्", "3s"), ("तस्", "3d"),
	("झि", "3p"), ("सिप्", "2s"), ("थस्", "2d"),
	("थ", "2p"), ("मिप्", "1s"),
]

# Infinitival / participial endings
_INF_ENDINGS = [
	("क्त्वा", "ger"), ("तुमुन्", "inf"), ("तव्य", "inf"),
	("अनीयर", "inf"), ("शतृ", "part"), ("शानच्", "part"),
	("क्था", "perf-part"), ("क्विन्", "perf-part"),
]

# Adjectival / participial endings
_PPP_ENDINGS = [
	("त", "ppp masc sg"), ("ता", "ppp fem sg"), ("तं", "ppp acc"),
	("ते", "ppp dat"), ("ति", "ppp loc"),
	("न्त्", "pres part masc sg"), ("ती", "pres part fem sg"),
	("न्तः", "pres part masc pl"), ("न्तौ", "pres part dual"),
]

# Feminine endings
_FEM_ENDINGS = [
	("का", "f"), ("का", "f"), ("की", "f"), ("कु", "f"),
	("ता", "f"), ("ती", "f"), ("तु", "f"),
	("नी", "f"), ("ना", "f"), ("नी", "f"),
	("षा", "f"), ("षी", "f"),
	("सा", "f"), ("सी", "f"),
	("धा", "f"), ("धी", "f"),
	("वा", "f"), ("वी", "f"),
	("ला", "f"), ("ली", "f"),
	("ना", "f"), ("नी", "f"),
]

def _try_strip(word: str, endings: list) -> tuple:
	"""Try stripping any ending. Returns (stem, suffix_label) or (word, '')."""
	for ending, label in endings:
		if word.endswith(ending) and len(word) > len(ending):
			return word[:-len(ending)], label
		if word == ending:
			return "", label
	return word, ""


# ── Rule 5: Avalana (P.7.3.1-2) — अ after अ ────────────────────────────────

_AVALANA = {
	"अः": "ाः", "अम्": "ाम्", "अत्": "ात्",
	"अव": "ाव", "अ": "ा",
}

def _apply_avalanas(word: str) -> list:
	"""If word ends with अ-vowel combination that could be avalana, split.
	Used for forms like पिता (पितु+अ) → पितु + अ."""
	results = []
	# तादitha case: आ after long vowel might be stem+अ
	if len(word) >= 2 and word[-1] == "ा" and word[-2] in VOWELS:
		stem = word[:-1]
		results.append(stem + "+अ")
	return results


# ── Rule 6: 'm' as anusvara (P.1.1.8-9) ─────────────────────────────────────

def _apply_anusvara(word: str) -> list:
	"""म् as anusvara before labial: म → ं.
	e.g. गुरुम् → गुरुं, पितरम् → पितरं (already shown, but useful for matching)"""
	results = []
	if word.endswith("म्") and len(word) > 2:
		# Could be nom sg -m, or anusvara + next word boundary
		results.append(word[:-1]) # remove final m
	return results


# ── Rule 7: Compound boundaries ───────────────────────────────────────────────

KNOWN_COMPOUND_SUFFIXES = [
	# tatp- compounds (endings that mark the final member)
	"ता", "त्व", "वत्", "मत्", "सार", "गत", "पूर्ण",
]

# dvandva markers
_DVANDVA_MARKERS = {"च", "वा", "न"}

def _try_dvandva(word: str) -> list:
	"""Split on dvandva conjunction 'च'.
	e.g. शमदमौ → शम + च + दम → split at च"""
	results = []
	for marker in _DVANDVA_MARKERS:
		if marker in word:
			idx = word.index(marker)
			part1 = word[:idx]
			part2 = word[idx+1:]
			if part1 and part2:
				results.append(part1 + "+" + part2)
	return results


# ── Main splitter ─────────────────────────────────────────────────────────────

def split(word: str) -> list:
	"""Split a Sanskrit word into candidate component sequences.
	Returns list of '+' joined strings, sorted by plausibility."""
	if not word or len(word) < 2:
		return [word]

	candidates = set()

	# ── A. Try sandhi-based splits ───────────────────────────────────────────

	# A1. dvitva (consonant doubling)
	for s in _apply_dvitva(word):
		candidates.add(s)

	# A2. ik→ya rule
	for s in _apply_ik_yan(word):
		candidates.add(s)

	# A3. avalana (ā after vowel)
	for s in _apply_avalanas(word):
		candidates.add(s)

	# A4. anusvara
	for s in _apply_anusvara(word):
		candidates.add(s)

	# A5. dvandva conjunctions
	for s in _try_dvandva(word):
		candidates.add(s)

	# ── B. Try affix stripping ───────────────────────────────────────────────

	B_affixes = []
	for ending_list in [_SUP_ENDINGS, _TIG_ENDINGS, _INF_ENDINGS, _PPP_ENDINGS, _FEM_ENDINGS]:
		stem, label = _try_strip(word, ending_list)
		if stem != word:
			B_affixes.append(stem)

	# If we have a good stem from affix stripping, try further splitting it
	for stem in B_affixes:
		if len(stem) >= 2:
			candidates.add(stem)

	# ── C. Try samasa-based splits (compound markers) ────────────────────────
	# Just try to detect known compound patterns
	for suffix in KNOWN_COMPOUND_SUFFIXES:
		if word.endswith(suffix) and len(word) > len(suffix):
			stem = word[:-len(suffix)]
			if stem:
				candidates.add(stem)

	# ── D. Try greedy sub-word splits ────────────────────────────────────────
	# Look for known sub-words within the token
	from vidyut_anuvaada.sutras.dictionary import _BUILTIN

	if len(word) >= 4:
		for length in range(len(word)-1, 2, -1):
			prefix = word[:length]
			suffix = word[length:]
			if prefix in _BUILTIN and suffix in _BUILTIN:
				candidates.add(prefix + "+" + suffix)

	# ── E. Fallback: longest prefix match ────────────────────────────────────
	if not candidates:
		for length in range(len(word)-1, 2, -1):
			if word[:length] in _BUILTIN:
				candidates.add(word[:length] + "+" + word[length:])
				break

	# Always include the original word as fallback
	candidates.add(word)

	# Sort by number of parts (more parts = more informative)
	results = sorted(candidates, key=lambda x: -x.count("+"))
	return results[:8] # limit to top 8 candidates
