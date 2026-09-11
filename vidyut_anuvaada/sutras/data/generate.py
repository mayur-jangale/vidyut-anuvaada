"""Generate inflected Sanskrit forms from root data.

Data-driven: takes (root, decl_class) tuples from roots.py,
applies declension templates with basic vowel sandhi,
and builds a flat surface_form -> (lemma, pos, gloss) lookup.
"""
from __future__ import annotations
from typing import Optional
from vidyut_anuvaada.sutras.data import ALL

VOWELS = set("अआइईउऊऋऌएऐओऔाीूृेैोौ")

def last_vowel(s: str) -> str:
	for ch in reversed(s):
		if ch in VOWELS:
			return ch
	return "अ"

def apply_sandhi(stem: str, suffix: str) -> str:
	if not stem or not suffix:
		return stem + suffix
	s_last = stem[-1]
	e_first = suffix[0]
	if s_last not in VOWELS:
		return stem + suffix
	if e_first not in VOWELS:
		return stem + suffix
	sv = last_vowel(stem)
	# Guṇa: अ→आ, इ→ए, उ→ओ
	guni = {"अ": "आ", "इ": "ए", "उ": "ओ", "ऋ": "अर्"}
	g = guni.get(sv, sv)
	# Drop first vowel of suffix if stem had a vowel
	return stem[:-1] + g + suffix[1:]

# ---------------------------------------------------------------------------
# Stem building
# ---------------------------------------------------------------------------
def make_stem(root: str, decl: str) -> str:
	if decl in ("a-m", "a-n", "a-f"):
		# a-stem: ensure stem ends in अ
		if root.endswith("अ"):
			return root
		return root + "अ"
	if decl in ("i-m", "i-f"):
		# i-stem: ensure ends in इ
		if root.endswith("ि"):
			return root
		return root + "ि"
	if decl == "u-m":
		if root.endswith("ु"):
			return root
		return root + "उ"
	if decl == "an":
		# Drop final न्/न, stem ends in अ (added via endings)
		if root.endswith("न्"):
			return root[:-1]
		if root.endswith("न"):
			return root[:-1]
		return root
	return root

# ---------------------------------------------------------------------------
# Declension tables — raw suffixes after stem vowel (for a-stem)
# These combine with stem that already ends in अ
# ---------------------------------------------------------------------------
# a-stem masculine: धर्म + अ + स् → through sandhi → धर्मः
A_M = {
	(0,0): "स्", (1,0): "म्", (2,0): "ेन", (3,0): "अय", (4,0): "अस्",
	(5,0): "स्य", (6,0): "इ", (7,0): "स्",
	(0,1): "औ", (1,1): "औ", (2,1): "आभ्याम्", (3,1): "ए", (4,1): "योः",
	(5,1): "योः", (6,1): "योः", (7,1): "औ",
	(0,2): "आस्",(1,2): "ान्",(2,2): "एः", (3,2): "एभ्यः",(4,2): "एभ्यः",
	(5,2): "ानाम्",(6,2): "एषु",(7,2): "आस्",
}

# a-stem neuter: same but nom/acc sg/pl = म्/ानि
A_N = dict(A_M)
A_N[(0,0)] = "म्"; A_N[(1,0)] = "म्"
A_N[(0,2)] = "ानि"; A_N[(1,2)] = "ानि"

# a-stem feminine: सेना-type
# stem = अ, endings have leading आ for most cases
A_F = {
	(0,0): "आ", (1,0): "आम्", (2,0): "आया", (3,0): "आयै", (4,0): "आयाः",
	(5,0): "आयाः", (6,0): "आयाम्", (7,0): "ए",
	(0,1): "ए", (1,1): "ए", (2,1): "योः", (3,1): "योः", (4,1): "योः",
	(5,1): "योः", (6,1): "योः", (7,1): "ए",
	(0,2): "यः", (1,2): "यः", (2,2): "याः", (3,2): "याः", (4,2): "याः",
	(5,2): "यानाम्", (6,2): "यासु", (7,2): "यः",
}

# i-stem masculine: गुरु-type (stem ends in इ)
I_M = {
	(0,0): "स्", (1,0): "म्", (2,0): "ना", (3,0): "ए", (4,0): "एः",
	(5,0): "एः", (6,0): "औ", (7,0): "ए",
	(0,1): "ई", (1,1): "ई", (2,1): "योः", (3,1): "योः", (4,1): "योः",
	(5,1): "योः", (6,1): "योः", (7,1): "ई",
	(0,2): "यः", (1,2): "ीन्", (2,2): "िभिः", (3,2): "यः", (4,2): "यः",
	(5,2): "ीनाम्", (6,2): "िषु", (7,2): "यः",
}

# i-stem feminine: बुद्धि-type
I_F = {
	(0,0): "स्", (1,0): "म्", (2,0): "या", (3,0): "यै", (4,0): "याः",
	(5,0): "याः", (6,0): "याम्", (7,0): "ये",
	(0,1): "ये", (1,1): "ये", (2,1): "योः", (3,1): "योः", (4,1): "योः",
	(5,1): "योः", (6,1): "योः", (7,1): "ये",
	(0,2): "यः", (1,2): "यः", (2,2): "याः", (3,2): "याः", (4,2): "याः",
	(5,2): "यानाम्", (6,2): "यासु", (7,2): "यः",
}

# u-stem masculine: गुरु-type
U_M = {
	(0,0): "स्", (1,0): "म्", (2,0): "ना", (3,0): "औ", (4,0): "ओः",
	(5,0): "ओः", (6,0): "औ", (7,0): "ओ",
	(0,1): "ऊ", (1,1): "ऊ", (2,1): "योः", (3,1): "योः", (4,1): "योः",
	(5,1): "योः", (6,1): "योः", (7,1): "ऊ",
	(0,2): "वः", (1,2): "ून्", (2,2): "ुभिः", (3,2): "वः", (4,2): "वः",
	(5,2): "ूनाम्", (6,2): "उषु", (7,2): "वः",
}

# an-stem masculine: राजन्-type (stem = root without न्, implicit अ added)
AN_M = {
	(0,0): "ता", (1,0): "म्", (2,0): "ता", (3,0): "ते", (4,0): "तः",
	(5,0): "तुः", (6,0): "ति", (7,0): "न्",
	(0,1): "तौ", (1,1): "तौ", (2,1): "द्वाभ्याम्", (3,1): "तौ", (4,1): "द्वयोः",
	(5,1): "द्वयोः", (6,1): "तौ", (7,1): "तौ",
	(0,2): "न्तः", (1,2): "तः", (2,2): "द्भिः", (3,2): "ते", (4,2): "द्भ्यः",
	(5,2): "ताम्", (6,2): "त्सु", (7,2): "न्तः",
}

END_MAP = {
	"a-m": A_M, "a-n": A_N, "a-f": A_F,
	"i-m": I_M, "i-f": I_F,
	"u-m": U_M, "an": AN_M,
}

CASE_NAMES = ["nom","acc","ins","dat","abl","gen","loc","voc"]
NUM_NAMES = ["sg","du","pl"]

def decline(root: str, decl: str, case: int, num: int) -> Optional[str]:
	endings = END_MAP.get(decl)
	if endings is None:
		return None
	suf = endings.get((case, num))
	if suf is None:
		return None
	st = make_stem(root, decl)
	result = apply_sandhi(st, suf)
	# Apply visarga: final स् → सः
	# Actually in Sanskrit, स् at end of word → visarga (ः)
	if result.endswith("स्"):
		result = result[:-2] + "ः"
	elif result.endswith("स"):
		# Keep स् as स् (not final position really)
		pass
	return result

# ---------------------------------------------------------------------------
# Build flat lookup
# ---------------------------------------------------------------------------

def build_forms() -> dict[str, tuple[str, str, str]]:
	forms: dict[str, tuple[str, str, str]] = {}

	def add(frm: str, root: str, pos: str, gloss: str):
		if frm not in forms:
			forms[frm] = (root, pos, gloss)

	for entry in ALL:
		root, pos, gloss, decl = entry
		add(root, root, pos, gloss)
		if decl is None:
			continue

		if pos in ("noun-m", "noun-n", "noun-f", "adj"):
			for c in range(8):
				for n in range(3):
					f = decline(root, decl, c, n)
					if f:
						extra = f" [{CASE_NAMES[c]} {NUM_NAMES[n]}]"
						add(f, root, pos, gloss + extra)
		elif pos.startswith("verb") and pos not in ("verb-ger", "verb-ppp", "verb-pp"):
			add(root + "ति", root, pos, gloss + " [3s]")
			add(root + "तः", root, pos, gloss + " [3d]")
			add(root + "न्ति", root, pos, gloss + " [3p]")

	return forms
