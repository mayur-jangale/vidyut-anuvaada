"""Morphology engine: generate Sanskrit inflected forms from root data.

All rules are data-driven — no hardcoded word lists.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Declension / conjugation templates
# ---------------------------------------------------------------------------

# Noun endings: (case, number, gender) -> suffix applied to stem
# case: 0=nom, 1=acc, 2=ins, 3=dat, 4=abl, 5=gen, 6=loc, 7=voc
# number: 0=sg, 1=du, 2=pl
# gender: m=masc, f=fem, n=neut

ST_A_M = {
	# (case, number): suffix
	(0, 0): "ः", # nom sg
	(1, 0): "म्", # acc sg
	(2, 0): "ेन", # ins sg
	(3, 0): "ाय", # dat sg
	(4, 0): "ात्", # abl sg
	(5, 0): "स्य", # gen sg
	(6, 0): "े", # loc sg
	(7, 0): "ः", # voc sg
	(0, 1): "ौ", # nom du
	(1, 1): "ौ", # acc du
	(2, 1): "ाभ्याम्", # ins du
	(3, 1): "ाभ्याम्", # dat du
	(4, 1): "ाभ्याम्", # abl du
	(5, 1): "योः", # gen du
	(6, 1): "योः", # loc du
	(7, 1): "ौ", # voc du
	(0, 2): "ाः", # nom pl
	(1, 2): "ान्", # acc pl
	(2, 2): "ैः", # ins pl
	(3, 2): "ेभ्यः", # dat pl
	(4, 2): "ेभ्यः", # abl pl
	(5, 2): "ानाम्", # gen pl
	(6, 2): "ेषु", # loc pl
	(7, 2): "ाः", # voc pl
}

# Same endings but stem ends in आ (long a) – like कर्मा
ST_A_LONG = {
	(0, 0): "ः",
	(1, 0): "म्",
	(2, 0): "ेन",
	(3, 0): "े", # shortened from आय
	(4, 0): "ात्",
	(5, 0): "स्य",
	(6, 0): "े",
	(7, 0): "ः",
	(0, 1): "े",
	(1, 1): "े",
	(2, 1): "ाभ्याम्",
	(3, 1): "ाभ्याम्",
	(4, 1): "ाभ्याम्",
	(5, 1): "योः",
	(6, 1): "योः",
	(7, 1): "े",
	(0, 2): "ाः",
	(1, 2): "ान्",
	(2, 2): "ैः",
	(3, 2): "ेभ्यः",
	(4, 2): "ेभ्यः",
	(5, 2): "ानाम्",
	(6, 2): "ेषु",
	(7, 2): "ाः",
}

# Feminine -a stems (अ -> आ)
ST_A_F = {k: ("ा" + v if v and not v.startswith(("ा","े","ै","ाभ्य")) else v)
 for k, v in ST_A_M.items()}

# neuter -a stems (no visarga in nom/acc sg)
ST_A_N = dict(ST_A_M)
ST_A_N[(0, 0)] = "म्" # nom sg
ST_A_N[(1, 0)] = "म्" # acc sg (same)
ST_A_N[(0, 2)] = "ानि" # nom pl
ST_A_N[(1, 2)] = "ानि" # acc pl

# -i stems (masculine/feminine)
ST_I = {
	(0, 0): "ः",
	(1, 0): "म्",
	(2, 0): "िना",
	(3, 0): "ये",
	(4, 0): "ेः",
	(5, 0): "ेः",
	(6, 0): "ौ",
	(7, 0): "े",
	(0, 1): "ी",
	(1, 1): "ी",
	(2, 1): "िभ्याम्",
	(3, 1): "िभ्याम्",
	(4, 1): "िभ्याम्",
	(5, 1): "योः",
	(6, 1): "योः",
	(7, 1): "ी",
	(0, 2): "यः",
	(1, 2): "ीन्",
	(2, 2): "िभिः",
	(3, 2): "िभ्यः",
	(4, 2): "िभ्यः",
	(5, 2): "ीनाम्",
	(6, 2): "िषु",
	(7, 2): "यः",
}

# -u stems (masculine)
ST_U = {
	(0, 0): "ः",
	(1, 0): "म्",
	(2, 0): "ुना",
	(3, 0): "वे",
	(4, 0): "ोः",
	(5, 0): "ोः",
	(6, 0): "ौ",
	(7, 0): "ो",
	(0, 1): "ू",
	(1, 1): "ू",
	(2, 1): "ुभ्याम्",
	(3, 1): "ुभ्याम्",
	(4, 1): "ुभ्याम्",
	(5, 1): "योः",
	(6, 1): "योः",
	(7, 1): "ू",
	(0, 2): "वः",
	(1, 2): "ून्",
	(2, 2): "ुभिः",
	(3, 2): "ुभ्यः",
	(4, 2): "ुभ्यः",
	(5, 2): "ूनाम्",
	(6, 2): "ुषु",
	(7, 2): "वः",
}

# -n/-an stems (अ -> अ, nom sg ends in आ्)
ST_AN = {
	(0, 0): "ा",
	(1, 0): "म्",
	(2, 0): "ता",
	(3, 0): "ते",
	(4, 0): "तः",
	(5, 0): "तुः",
	(6, 0): "ति",
	(7, 0): "न्",
	(0, 1): "तौ",
	(1, 1): "तौ",
	(2, 1): "द्वाभ्याम्",
	(3, 1): "द्वाभ्याम्",
	(4, 1): "द्वाभ्याम्",
	(5, 1): "द्वयोः",
	(6, 1): "द्वयोः",
	(7, 1): "तौ",
	(0, 2): "न्तः",
	(1, 2): "तः",
	(2, 2): "द्भिः",
	(3, 2): "द्भ्यः",
	(4, 2): "द्भ्यः",
	(5, 2): "ताम्",
	(6, 2): "त्सु",
	(7, 2): "न्तः",
}

# Verb present endings (parasmaipada, 3rd person only for now)
# person: 1=3s, 2=3d, 3=3p
VERB_PRES_M = {1: "ति", 2: "तः", 3: "न्ति"}
VERB_PRES_N = {1: " ति", 2: "ते", 3: "न्ते"} # root + ending (sandhi handled elsewhere)

# Past passive participle (krtanta -ta)
PPF_SUFFIX = "त"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

CASE_NAMES = ["nom", "acc", "ins", "dat", "abl", "gen", "loc", "voc"]
NUM_NAMES = ["sg", "du", "pl"]
GENDER_NAMES = {"m": "masc", "f": "fem", "n": "neut"}


def _decline(stem: str, endings: dict, case: int, num: int) -> str:
	return stem + endings.get((case, num), "")


def decline_noun(root: str, pos: str, case: int, num: int) -> tuple[str, str, str] | None:
	"""Generate a declined form. Returns (form, pos, gloss_extra) or None."""
	# Determine stem class from pos
	if pos == "noun-m":
		if root.endswith("न्"):
			stem = root[:-1] # drop न्
			endings = ST_AN
		elif root.endswith("ि"):
			stem = root[:-1] # drop final i -> i-stem
			# Add i back for i-stem
			stem_i = root
			endings = ST_I
			form = _decline(stem_i, endings, case, num)
			return (form, pos, f"[{CASE_NAMES[case]} {NUM_NAMES[num]}]")
		elif root.endswith("ु"):
			stem_u = root
			endings = ST_U
			form = _decline(stem_u, endings, case, num)
			return (form, pos, f"[{CASE_NAMES[case]} {NUM_NAMES[num]}]")
		else:
			# a-stem masculine
			if root.endswith("ा"):
				stem = root[:-1] + ""
				endings = ST_A_LONG
			else:
				stem = root + "अ" if not root.endswith("अ") else root
				endings = ST_A_M
			form = _decline(stem, endings, case, num)
			return (form, pos, f"[{CASE_NAMES[case]} {NUM_NAMES[num]}]")
	elif pos == "noun-f":
		if root.endswith("ि") or root.endswith("ी"):
			stem = root
			endings = ST_I
		elif root.endswith("ा"):
			stem = root[:-1] # stem is अ
			endings = ST_A_F
		else:
			stem = root + "ा" if not root.endswith("ा") else root
			endings = ST_A_F
		form = _decline(stem, endings, case, num)
		return (form, pos, f"[{CASE_NAMES[case]} {NUM_NAMES[num]}]")
	elif pos == "noun-n":
		if root.endswith("स्") or root.endswith("स"):
			stem = root.rstrip("स्स")
			endings = ST_AN
		elif root.endswith("म्") or root.endswith("म"):
			stem = root.rstrip("म्म")
			endings = ST_A_LONG
		elif root.endswith("ा"):
			stem = root[:-1]
			endings = ST_A_N
		else:
			stem = root
			endings = ST_A_N
		form = _decline(stem, endings, case, num)
		return (form, pos, f"[{CASE_NAMES[case]} {NUM_NAMES[num]}]")
	return None


def conjugate_verb(root: str, pos: str, person: int, num: int) -> tuple[str, str, str] | None:
	"""Generate a conjugated verb form. person=1(sg),2(du),3(pl)."""
	if "verb" in pos:
		# Present system: root + personal ending
		# For parasmaipada
		if num == 0: # singular
			if person == 1:
				ending_map = {"verb": "ति", "verb-pr": "ति", "verb-pr-3s": "ति"}
				end = ending_map.get(pos, "ति")
			elif person == 2:
				end = "सि"
			else:
				end = "ति"
		elif num == 1: # dual
			end = "तः"
		else: # plural
			end = "न्ति"
		form = root + end
		return (form, pos, f"[{person+1}p {NUM_NAMES[num]}]")
	return None


def make_participle(root: str, pos: str) -> tuple[str, str, str] | None:
	"""Make past passive participle (ppp) with -ta suffix."""
	if "verb" in pos or root.endswith(("ा", "ि", "ु", "ू")):
		# Add -ta to strengthened stem
		ppp = root + PPF_SUFFIX
		return (ppp, "verb-ppp", "[past passive participle]")
	return None
