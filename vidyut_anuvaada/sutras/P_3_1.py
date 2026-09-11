"""Shared logic for P.3.1.x sutras - vikaraNa and ardhadhAtuka rules."""
from __future__ import annotations


# dhatu-class membership sets
JUHOTYADI = {"हु", "इन्ध", "पू", "दीप", "रुधिर", "आस", "वस", "कृद्"}
DIVADI = {"दिव्", "परिव्यप", "वर्ध", "सिञ्च्"}
SUPYADI = {"स्वप्", "प्रेम्फ्", "प्रमोद्"}
RUDHADI = {"रुध्", "रम्भ्", "बध्", "अञ्च्", "कूज्"}
TANADI = {"तन्", "स्कन्द्", "क्रन्द्", "क्रुध्", "क्रुश्"}
KRYADI = {"कृ", "भू", "अस्", "कम्", "गम्", "दा", "धा", "नी", "पा", "भ्रम्"}
CURADI = {"चुर्", "चुरा"}
BHVA_DI = {"भू", "अस्", "कम्", "कृ", "गम्", "दा", "धा", "नी", "पा", "भ्रम्"}
IT_ROOTS = {"कृष्", "लिख्", "वच्", "वप्", "पुष्"}


# helper utilities
def _last_char(word):
	return word[-1] if word else ""


def _is_svara(c):
	return c in "अआइईउऊऋॠऌॡएऐओऔाीूृॄॢॣेैोौंः"


def _is_consonant(c):
	return c in "कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ"


def _root_of(word):
	for s in ("य", "ा", "ी", "ू", "ं", "त्", "म्"):
		if word.endswith(s):
			return word[:-1]
	return word


def apply_3_1_1(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.1 - vikaraNa rule."""
	tag = "p31-001"
	return tag + ";input=" + (word or "") + ";vikaraNa=applied"

def apply_3_1_2(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.2 - vikaraNa rule."""
	tag = "p31-002"
	return tag + ";input=" + (word or "") + ";vikaraNa=applied"

def apply_3_1_3(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.3 - vikaraNa rule."""
	tag = "p31-003"
	return tag + ";input=" + (word or "") + ";vikaraNa=applied"

def apply_3_1_4(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.4 - vikaraNa rule."""
	tag = "p31-004"
	return tag + ";input=" + (word or "") + ";vikaraNa=applied"

def apply_3_1_5(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.5 - हुस्: sa-vikaraNa for juhotyAdi-class dhatus."""
	tag = "p31-005"
	root = _root_of(word)
	flag = "yes" if root in JUHOTYADI else "no"
	return tag + ";input=" + word + ";root=" + root + ";sa=" + flag

def apply_3_1_6(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.6 - आदेशः: vrddhi/adesha substitution."""
	tag = "p31-006"
	return tag + ";input=" + (word or "") + ";adesha=vrddhi"

def apply_3_1_7(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.7 - न: na-vikaraNa for specific roots."""
	tag = "p31-007"
	NA_ROOTS = {"गम्", "लभ्", "यज्", "याच्", "दांश्"}
	flag = "yes" if word in NA_ROOTS else "no"
	return tag + ";input=" + word + ";na=" + flag

def apply_3_1_8(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.8 - शेन: ya-vikaraNa for specific roots."""
	tag = "p31-008"
	YA_ROOTS = {"रम्", "दर्श्", "स्पर्ध्"}
	flag = "yes" if word in YA_ROOTS else "no"
	return tag + ";input=" + word + ";ya=" + flag

def apply_3_1_9(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.9 - इ: i-vikaraNa for atmanepada."""
	tag = "p31-009"
	return tag + ";input=" + (word or "") + ";vikaraNa=i;Atmanepada=yes"

def apply_3_1_10(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.10 - उ: u-vikaraNa for supyAdi."""
	tag = "p31-010"
	flag = "yes" if _root_of(word) in SUPYADI else "no"
	return tag + ";input=" + word + ";u=" + flag

def apply_3_1_11(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.11 - आर्धधातुकस्येडागमः: it-Agama after ardhadhAtuka."""
	tag = "p31-011"
	return tag + ";input=" + (word or "") + ";Agama=iT-inserted"

def apply_3_1_12(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.12 - अचोऽचेऽन्ते: it-agama after final vowel."""
	tag = "p31-012"
	if not word: return tag + ";input=;Agama=none"
	final = _last_char(word)
	vowel = _is_svara(final)
	return tag + ";input=" + word + ";final=" + final + ";vowel=" + ("yes" if vowel else "no") + ";Agama=" + ("iT-inserted" if vowel else "none")

def apply_3_1_13(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.13 - vikaraNa rule."""
	tag = "p31-013"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_14(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.14 - vikaraNa rule."""
	tag = "p31-014"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_15(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.15 - vikaraNa rule."""
	tag = "p31-015"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_16(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.16 - vikaraNa rule."""
	tag = "p31-016"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_17(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.17 - vikaraNa rule."""
	tag = "p31-017"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_18(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.18 - vikaraNa rule."""
	tag = "p31-018"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_19(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.19 - vikaraNa rule."""
	tag = "p31-019"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_20(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.20 - vikaraNa rule."""
	tag = "p31-020"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_14(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.14 - सस्य: sa for shamyAdi roots."""
	tag = "p31-014"
	SHAM_ROOTS = {"शम्", "कम्"}
	flag = "yes" if word in SHAM_ROOTS else "no"
	return tag + ";input=" + word + ";sa=" + flag

def apply_3_1_21(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.21 - vikaraNa/affix rule."""
	tag = "p31-021"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_22(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.22 - vikaraNa/affix rule."""
	tag = "p31-022"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_23(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.23 - vikaraNa/affix rule."""
	tag = "p31-023"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_24(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.24 - vikaraNa/affix rule."""
	tag = "p31-024"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_25(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.25 - vikaraNa/affix rule."""
	tag = "p31-025"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_26(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.26 - vikaraNa/affix rule."""
	tag = "p31-026"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_27(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.27 - vikaraNa/affix rule."""
	tag = "p31-027"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_28(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.28 - vikaraNa/affix rule."""
	tag = "p31-028"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_29(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.29 - vikaraNa/affix rule."""
	tag = "p31-029"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_30(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.30 - थ: tha affix."""
	tag = "p31-030"
	return tag + ";input=" + (word or "") + ";affix=tha"

def apply_3_1_31(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.31 - affix rule."""
	tag = "p31-031"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_32(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.32 - affix rule."""
	tag = "p31-032"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_33(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.33 - affix rule."""
	tag = "p31-033"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_34(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.34 - affix rule."""
	tag = "p31-034"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_35(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.35 - affix rule."""
	tag = "p31-035"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_36(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.36 - affix rule."""
	tag = "p31-036"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_37(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.37 - affix rule."""
	tag = "p31-037"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_38(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.38 - affix rule."""
	tag = "p31-038"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_39(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.39 - affix rule."""
	tag = "p31-039"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_40(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.40 - affix rule."""
	tag = "p31-040"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_41(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.41 - affix rule."""
	tag = "p31-041"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_42(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.42 - affix rule."""
	tag = "p31-042"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_43(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.43 - affix rule."""
	tag = "p31-043"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_44(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.44 - affix rule."""
	tag = "p31-044"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_45(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.45 - affix rule."""
	tag = "p31-045"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_46(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.46 - affix rule."""
	tag = "p31-046"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_47(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.47 - affix rule."""
	tag = "p31-047"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_48(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.48 - affix rule."""
	tag = "p31-048"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_49(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.49 - affix rule."""
	tag = "p31-049"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_50(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.50 - affix rule."""
	tag = "p31-050"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_51(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.51 - affix rule."""
	tag = "p31-051"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_52(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.52 - affix rule."""
	tag = "p31-052"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_53(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.53 - affix rule."""
	tag = "p31-053"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_54(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.54 - affix rule."""
	tag = "p31-054"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_55(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.55 - affix rule."""
	tag = "p31-055"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_56(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.56 - affix rule."""
	tag = "p31-056"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_57(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.57 - affix rule."""
	tag = "p31-057"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_58(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.58 - affix rule."""
	tag = "p31-058"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_59(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.59 - affix rule."""
	tag = "p31-059"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_60(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.60 - affix rule."""
	tag = "p31-060"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_61(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.61 - affix rule."""
	tag = "p31-061"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_62(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.62 - affix rule."""
	tag = "p31-062"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_63(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.63 - affix rule."""
	tag = "p31-063"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_64(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.64 - affix rule."""
	tag = "p31-064"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_65(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.65 - affix rule."""
	tag = "p31-065"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_66(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.66 - affix rule."""
	tag = "p31-066"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_67(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.67 - affix rule."""
	tag = "p31-067"
	return tag + ";input=" + (word or "") + ";affix=none"

def apply_3_1_68(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.68 - षो लोपः: drop final h after vikaraNa."""
	tag = "p31-068"
	if not word: return tag + ";input=;lopa=none"
	has_h = word.endswith("ह") or word.endswith("ह्")
	return tag + ";input=" + word + ";has-h=" + ("yes" if has_h else "no") + ";lopa=" + ("drop-h" if has_h else "none")

def apply_3_1_69(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.69 - आदिः: Adi-class rule."""
	tag = "p31-069"
	return tag + ";input=" + (word or "") + ";class=adi"

def apply_3_1_70(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.70 - affix rule for juhotyAdi-class."""
	tag = "p31-070"
	root = _root_of(word)
	flag = "yes" if root in JUHOTYADI else "no"
	return tag + ";input=" + word + ";root=" + root + ";in-class=" + flag

def apply_3_1_71(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.71 - affix rule for divAdi-class."""
	tag = "p31-071"
	root = _root_of(word)
	flag = "yes" if root in DIVADI else "no"
	return tag + ";input=" + word + ";root=" + root + ";in-class=" + flag

def apply_3_1_72(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.72 - affix rule for supyAdi-class."""
	tag = "p31-072"
	root = _root_of(word)
	flag = "yes" if root in SUPYADI else "no"
	return tag + ";input=" + word + ";root=" + root + ";in-class=" + flag

def apply_3_1_73(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.73 - affix rule for rudhAdi-class."""
	tag = "p31-073"
	root = _root_of(word)
	flag = "yes" if root in RUDHADI else "no"
	return tag + ";input=" + word + ";root=" + root + ";in-class=" + flag

def apply_3_1_74(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.74 - affix rule for tanAdi-class."""
	tag = "p31-074"
	root = _root_of(word)
	flag = "yes" if root in TANADI else "no"
	return tag + ";input=" + word + ";root=" + root + ";in-class=" + flag

def apply_3_1_75(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.75 - affix rule for kriyAdi-class."""
	tag = "p31-075"
	root = _root_of(word)
	flag = "yes" if root in KRYADI else "no"
	return tag + ";input=" + word + ";root=" + root + ";in-class=" + flag

def apply_3_1_76(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.76 - affix rule for curAdi-class."""
	tag = "p31-076"
	root = _root_of(word)
	flag = "yes" if root in CURADI else "no"
	return tag + ";input=" + word + ";root=" + root + ";in-class=" + flag

def apply_3_1_77(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.77 - vikaraNa/affix rule."""
	tag = "p31-077"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_78(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.78 - vikaraNa/affix rule."""
	tag = "p31-078"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_79(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.79 - vikaraNa/affix rule."""
	tag = "p31-079"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_80(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.80 - vikaraNa/affix rule."""
	tag = "p31-080"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_81(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.81 - vikaraNa/affix rule."""
	tag = "p31-081"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_82(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.82 - vikaraNa/affix rule."""
	tag = "p31-082"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_83(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.83 - vikaraNa/affix rule."""
	tag = "p31-083"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_84(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.84 - vikaraNa/affix rule."""
	tag = "p31-084"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_85(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.85 - vikaraNa/affix rule."""
	tag = "p31-085"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_86(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.86 - vikaraNa/affix rule."""
	tag = "p31-086"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_87(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.87 - vikaraNa/affix rule."""
	tag = "p31-087"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_88(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.88 - vikaraNa/affix rule."""
	tag = "p31-088"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_89(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.89 - vikaraNa/affix rule."""
	tag = "p31-089"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_90(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.90 - vikaraNa/affix rule."""
	tag = "p31-090"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_91(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.91 - vikaraNa/affix rule."""
	tag = "p31-091"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_92(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.92 - vikaraNa/affix rule."""
	tag = "p31-092"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_93(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.93 - vikaraNa/affix rule."""
	tag = "p31-093"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_94(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.94 - vikaraNa/affix rule."""
	tag = "p31-094"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_95(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.95 - vikaraNa/affix rule."""
	tag = "p31-095"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_96(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.96 - vikaraNa/affix rule."""
	tag = "p31-096"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_97(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.97 - vikaraNa/affix rule."""
	tag = "p31-097"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_98(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.98 - vikaraNa/affix rule."""
	tag = "p31-098"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_99(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.99 - vikaraNa/affix rule."""
	tag = "p31-099"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_100(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.100 - vikaraNa/affix rule."""
	tag = "p31-100"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_101(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.101 - vikaraNa/affix rule."""
	tag = "p31-101"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_102(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.102 - vikaraNa/affix rule."""
	tag = "p31-102"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_103(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.103 - vikaraNa/affix rule."""
	tag = "p31-103"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_104(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.104 - vikaraNa/affix rule."""
	tag = "p31-104"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_105(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.105 - vikaraNa/affix rule."""
	tag = "p31-105"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_106(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.106 - vikaraNa/affix rule."""
	tag = "p31-106"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_107(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.107 - vikaraNa/affix rule."""
	tag = "p31-107"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_108(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.108 - vikaraNa/affix rule."""
	tag = "p31-108"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_109(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.109 - vikaraNa/affix rule."""
	tag = "p31-109"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_110(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.110 - vikaraNa/affix rule."""
	tag = "p31-110"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_111(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.111 - vikaraNa/affix rule."""
	tag = "p31-111"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_112(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.112 - vikaraNa/affix rule."""
	tag = "p31-112"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_113(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.113 - vikaraNa/affix rule."""
	tag = "p31-113"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_114(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.114 - vikaraNa/affix rule."""
	tag = "p31-114"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_115(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.115 - vikaraNa/affix rule."""
	tag = "p31-115"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_116(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.116 - vikaraNa/affix rule."""
	tag = "p31-116"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_117(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.117 - vikaraNa/affix rule."""
	tag = "p31-117"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_118(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.118 - vikaraNa/affix rule."""
	tag = "p31-118"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_119(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.119 - vikaraNa/affix rule."""
	tag = "p31-119"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_120(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.120 - vikaraNa/affix rule."""
	tag = "p31-120"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_121(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.121 - vikaraNa/affix rule."""
	tag = "p31-121"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_122(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.122 - vikaraNa/affix rule."""
	tag = "p31-122"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_123(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.123 - vikaraNa/affix rule."""
	tag = "p31-123"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_124(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.124 - vikaraNa/affix rule."""
	tag = "p31-124"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_125(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.125 - vikaraNa/affix rule."""
	tag = "p31-125"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_126(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.126 - vikaraNa/affix rule."""
	tag = "p31-126"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_127(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.127 - vikaraNa/affix rule."""
	tag = "p31-127"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_128(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.128 - vikaraNa/affix rule."""
	tag = "p31-128"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_129(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.129 - vikaraNa/affix rule."""
	tag = "p31-129"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_130(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.130 - vikaraNa/affix rule."""
	tag = "p31-130"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_131(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.131 - vikaraNa/affix rule."""
	tag = "p31-131"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_132(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.132 - vikaraNa/affix rule."""
	tag = "p31-132"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_133(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.133 - vikaraNa/affix rule."""
	tag = "p31-133"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_134(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.134 - vikaraNa/affix rule."""
	tag = "p31-134"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_135(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.135 - vikaraNa/affix rule."""
	tag = "p31-135"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_136(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.136 - vikaraNa/affix rule."""
	tag = "p31-136"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_137(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.137 - vikaraNa/affix rule."""
	tag = "p31-137"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_138(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.138 - vikaraNa/affix rule."""
	tag = "p31-138"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_139(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.139 - vikaraNa/affix rule."""
	tag = "p31-139"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_140(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.140 - vikaraNa/affix rule."""
	tag = "p31-140"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_141(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.141 - vikaraNa/affix rule."""
	tag = "p31-141"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_142(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.142 - vikaraNa/affix rule."""
	tag = "p31-142"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_143(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.143 - vikaraNa/affix rule."""
	tag = "p31-143"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_144(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.144 - vikaraNa/affix rule."""
	tag = "p31-144"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_145(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.145 - vikaraNa/affix rule."""
	tag = "p31-145"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_146(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.146 - vikaraNa/affix rule."""
	tag = "p31-146"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_147(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.147 - vikaraNa/affix rule."""
	tag = "p31-147"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_148(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.148 - vikaraNa/affix rule."""
	tag = "p31-148"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_149(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.149 - vikaraNa/affix rule."""
	tag = "p31-149"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]

def apply_3_1_150(word, pos="", SUTRA_TOKEN=""):
	"""P.3.1.150 - vikaraNa/affix rule."""
	tag = "p31-150"
	return tag + ";input=" + (word or "") + ";rule=" + tag.split(":")[0]


# DISPATCH table
DISPATCH = {
	"प.3.1.1": apply_3_1_1,
	"प.3.1.2": apply_3_1_2,
	"प.3.1.3": apply_3_1_3,
	"प.3.1.4": apply_3_1_4,
	"प.3.1.5": apply_3_1_5,
	"प.3.1.6": apply_3_1_6,
	"प.3.1.7": apply_3_1_7,
	"प.3.1.8": apply_3_1_8,
	"प.3.1.9": apply_3_1_9,
	"प.3.1.10": apply_3_1_10,
	"प.3.1.11": apply_3_1_11,
	"प.3.1.12": apply_3_1_12,
	"प.3.1.13": apply_3_1_13,
	"प.3.1.14": apply_3_1_14,
	"प.3.1.15": apply_3_1_15,
	"प.3.1.16": apply_3_1_16,
	"प.3.1.17": apply_3_1_17,
	"प.3.1.18": apply_3_1_18,
	"प.3.1.19": apply_3_1_19,
	"प.3.1.20": apply_3_1_20,
	"प.3.1.21": apply_3_1_21,
	"प.3.1.22": apply_3_1_22,
	"प.3.1.23": apply_3_1_23,
	"प.3.1.24": apply_3_1_24,
	"प.3.1.25": apply_3_1_25,
	"प.3.1.26": apply_3_1_26,
	"प.3.1.27": apply_3_1_27,
	"प.3.1.28": apply_3_1_28,
	"प.3.1.29": apply_3_1_29,
	"प.3.1.30": apply_3_1_30,
	"प.3.1.31": apply_3_1_31,
	"प.3.1.32": apply_3_1_32,
	"प.3.1.33": apply_3_1_33,
	"प.3.1.34": apply_3_1_34,
	"प.3.1.35": apply_3_1_35,
	"प.3.1.36": apply_3_1_36,
	"प.3.1.37": apply_3_1_37,
	"प.3.1.38": apply_3_1_38,
	"प.3.1.39": apply_3_1_39,
	"प.3.1.40": apply_3_1_40,
	"प.3.1.41": apply_3_1_41,
	"प.3.1.42": apply_3_1_42,
	"प.3.1.43": apply_3_1_43,
	"प.3.1.44": apply_3_1_44,
	"प.3.1.45": apply_3_1_45,
	"प.3.1.46": apply_3_1_46,
	"प.3.1.47": apply_3_1_47,
	"प.3.1.48": apply_3_1_48,
	"प.3.1.49": apply_3_1_49,
	"प.3.1.50": apply_3_1_50,
	"प.3.1.51": apply_3_1_51,
	"प.3.1.52": apply_3_1_52,
	"प.3.1.53": apply_3_1_53,
	"प.3.1.54": apply_3_1_54,
	"प.3.1.55": apply_3_1_55,
	"प.3.1.56": apply_3_1_56,
	"प.3.1.57": apply_3_1_57,
	"प.3.1.58": apply_3_1_58,
	"प.3.1.59": apply_3_1_59,
	"प.3.1.60": apply_3_1_60,
	"प.3.1.61": apply_3_1_61,
	"प.3.1.62": apply_3_1_62,
	"प.3.1.63": apply_3_1_63,
	"प.3.1.64": apply_3_1_64,
	"प.3.1.65": apply_3_1_65,
	"प.3.1.66": apply_3_1_66,
	"प.3.1.67": apply_3_1_67,
	"प.3.1.68": apply_3_1_68,
	"प.3.1.69": apply_3_1_69,
	"प.3.1.70": apply_3_1_70,
	"प.3.1.71": apply_3_1_71,
	"प.3.1.72": apply_3_1_72,
	"प.3.1.73": apply_3_1_73,
	"प.3.1.74": apply_3_1_74,
	"प.3.1.75": apply_3_1_75,
	"प.3.1.76": apply_3_1_76,
	"प.3.1.77": apply_3_1_77,
	"प.3.1.78": apply_3_1_78,
	"प.3.1.79": apply_3_1_79,
	"प.3.1.80": apply_3_1_80,
	"प.3.1.81": apply_3_1_81,
	"प.3.1.82": apply_3_1_82,
	"प.3.1.83": apply_3_1_83,
	"प.3.1.84": apply_3_1_84,
	"प.3.1.85": apply_3_1_85,
	"प.3.1.86": apply_3_1_86,
	"प.3.1.87": apply_3_1_87,
	"प.3.1.88": apply_3_1_88,
	"प.3.1.89": apply_3_1_89,
	"प.3.1.90": apply_3_1_90,
	"प.3.1.91": apply_3_1_91,
	"प.3.1.92": apply_3_1_92,
	"प.3.1.93": apply_3_1_93,
	"प.3.1.94": apply_3_1_94,
	"प.3.1.95": apply_3_1_95,
	"प.3.1.96": apply_3_1_96,
	"प.3.1.97": apply_3_1_97,
	"प.3.1.98": apply_3_1_98,
	"प.3.1.99": apply_3_1_99,
	"प.3.1.100": apply_3_1_100,
	"प.3.1.101": apply_3_1_101,
	"प.3.1.102": apply_3_1_102,
	"प.3.1.103": apply_3_1_103,
	"प.3.1.104": apply_3_1_104,
	"प.3.1.105": apply_3_1_105,
	"प.3.1.106": apply_3_1_106,
	"प.3.1.107": apply_3_1_107,
	"प.3.1.108": apply_3_1_108,
	"प.3.1.109": apply_3_1_109,
	"प.3.1.110": apply_3_1_110,
	"प.3.1.111": apply_3_1_111,
	"प.3.1.112": apply_3_1_112,
	"प.3.1.113": apply_3_1_113,
	"प.3.1.114": apply_3_1_114,
	"प.3.1.115": apply_3_1_115,
	"प.3.1.116": apply_3_1_116,
	"प.3.1.117": apply_3_1_117,
	"प.3.1.118": apply_3_1_118,
	"प.3.1.119": apply_3_1_119,
	"प.3.1.120": apply_3_1_120,
	"प.3.1.121": apply_3_1_121,
	"प.3.1.122": apply_3_1_122,
	"प.3.1.123": apply_3_1_123,
	"प.3.1.124": apply_3_1_124,
	"प.3.1.125": apply_3_1_125,
	"प.3.1.126": apply_3_1_126,
	"प.3.1.127": apply_3_1_127,
	"प.3.1.128": apply_3_1_128,
	"प.3.1.129": apply_3_1_129,
	"प.3.1.130": apply_3_1_130,
	"प.3.1.131": apply_3_1_131,
	"प.3.1.132": apply_3_1_132,
	"प.3.1.133": apply_3_1_133,
	"प.3.1.134": apply_3_1_134,
	"प.3.1.135": apply_3_1_135,
	"प.3.1.136": apply_3_1_136,
	"प.3.1.137": apply_3_1_137,
	"प.3.1.138": apply_3_1_138,
	"प.3.1.139": apply_3_1_139,
	"प.3.1.140": apply_3_1_140,
	"प.3.1.141": apply_3_1_141,
	"प.3.1.142": apply_3_1_142,
	"प.3.1.143": apply_3_1_143,
	"प.3.1.144": apply_3_1_144,
	"प.3.1.145": apply_3_1_145,
	"प.3.1.146": apply_3_1_146,
	"प.3.1.147": apply_3_1_147,
	"प.3.1.148": apply_3_1_148,
	"प.3.1.149": apply_3_1_149,
	"प.3.1.150": apply_3_1_150,
}



def get_apply_31(num):
	code = "प.3.1." + str(num)
	return DISPATCH.get(code, lambda w, p="", s="": "stub:" + code + ":" + w)


def apply_any_31(code, word, pos=""):
	n = int(code.split(".")[-1])
	fn = get_apply_31(n)
	return fn(word, pos)
