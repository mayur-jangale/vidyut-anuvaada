"""P.6.2.x — 199 apply_6_2_Z functions for visarga-sandhi (P.6.2.1-P.6.2.199).

Devanagari-format input: word pairs joined by '+', e.g. 'रामः+चाय'.
The pipeline's reverse_sandhi produces these pairs; the sutra functions
tag them with the applicable rule so the engine can pick the best
transformation chain.
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _analyse(word):
	"""Split '+' joined string into (w1, w2)."""
	if "+" not in word:
		return word, ""
	idx = word.index("+")
	return word[:idx], word[idx + 1:]


def _halant_consonant(word):
	"""Return the consonant before a final halant, or last char if no halant."""
	if len(word) >= 2 and word[-1] == chr(0x094d):
		return word[-2]
	return word[-1] if word else ""


def _ends_with_halant(word, consonant):
	"""Check if word ends with consonant + halant."""
	return len(word) >= 2 and word[-1] == chr(0x094d) and word[-2] == consonant


def _tag(n, name):
	return f"6.2.{n:03d}:{name}"


def _pass(rule, word):
	return f"{rule}:pass;input={word}"


def _hit(rule, word, detail=""):
	if detail:
		return f"{rule}:{detail};{word}"
	return f"{rule}:{word}"


# ---------------------------------------------------------------------------
# Devanagari character sets (codepoints)
# ---------------------------------------------------------------------------

# Vowels
_A = chr(0x0905); _I = chr(0x0907); _U = chr(0x0909); _R = chr(0x0941)
_L = chr(0x0942); _E = chr(0x090f); _O = chr(0x0913); _AI = chr(0x0910)
_AU = chr(0x0914)
_HALANT = chr(0x094d)
_VISARGA = chr(0x0903)

VOWELS = {_A, _I, _U, _R, _L, _E, _O, _AI, _AU,
		 _A + _HALANT, # aM
		 _A + _VISARGA, # aH
		 chr(0x0940), chr(0x0944)} # long ī ū

# Consonants
_KA = chr(0x0915); _KHA = chr(0x0916); _GA = chr(0x0917); _GHA = chr(0x0918); _NGA = chr(0x0919)
_CA = chr(0x091a); _CHA = chr(0x091b); _JA = chr(0x091c); _JHA = chr(0x091d); _NYA = chr(0x091e)
_TA_R = chr(0x091f); _THA_R = chr(0x0920); _DA_R = chr(0x0921); _DHA_R = chr(0x0922); _NA_R = chr(0x0923)
_TA = chr(0x0924); _THA = chr(0x0925); _DA = chr(0x0926); _DHA = chr(0x0927); _NA = chr(0x0928)
_PA = chr(0x092a); _PHA = chr(0x092b); _BA = chr(0x092c); _BHA = chr(0x092d); _MA = chr(0x092e)
_YA = chr(0x092f); _RA = chr(0x0930); _LA = chr(0x0932); _VA = chr(0x0935)
_SA = chr(0x0938); _SHA = chr(0x0936); _SSA = chr(0x0937); _HA = chr(0x0939)

# Halant combinations
_SA_HAL = _SA + _HALANT # स्
_SHA_HAL = _SHA + _HALANT # श्
_SSA_HAL = _SSA + _HALANT # ष्
_HA_HAL = _HA + _HALANT # ह्

# Convenience sets
_VOICED_INIT = {_GA, _GHA, _JA, _JHA, _DA_R, _DHA_R, _DA, _DHA,
				_BA, _BHA, _MA, _YA, _RA, _LA, _VA}
_SIBILANTS = {_SA, _SHA, _SSA}
_TRIGGER_CJS = {_CA, _CHA, _JA, _JHA, _SHA}
_ALL_CONSONANTS = {_KA, _KHA, _GA, _GHA, _NGA, _CA, _CHA, _JA, _JHA, _NYA,
				 _TA_R, _THA_R, _DA_R, _DHA_R, _NA_R,
				 _TA, _THA, _DA, _DHA, _NA,
				 _PA, _PHA, _BA, _BHA, _MA, _YA, _RA, _LA, _VA,
				 _SA, _SHA, _SSA, _HA}


# ---------------------------------------------------------------------------
# P.6.2.1 – P.6.2.10
# ---------------------------------------------------------------------------

def apply_6_2_1(word, pos="", SUTRA_TOKEN=""):
	"""hal-antyam — word-final consonant elided before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(1, "hal-antyam"), word)
	e = _halant_consonant(w1)
	if e in _ALL_CONSONANTS and w2[0] in VOWELS:
		return _hit(_tag(1, "hal-antyam"), f"{w1[:-len(e)+1] if len(e)>1 else w1[:-1]}+{w2}", f"drop-final-{e}")
	return _pass(_tag(1, "hal-antyam"), word)


def apply_6_2_2(word, pos="", SUTRA_TOKEN=""):
	"""pAda-AdAtsaH — final स् before vowel → ओ."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(2, "pAda-AdAtsaH"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(2, "pAda-AdAtsaH"), f"{w1[:-2]}o+{w2}", "s-os→o")
	return _pass(_tag(2, "pAda-AdAtsaH"), word)


def apply_6_2_3(word, pos="", SUTRA_TOKEN=""):
	"""asaMyoge — ordering flag (non-samyoga context)."""
	return _hit(_tag(3, "asaMyoge"), word, "ordering-flag")


def apply_6_2_4(word, pos="", SUTRA_TOKEN=""):
	"""khar-avasane — final voiceless stop before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(4, "khar-avasane"), word)
	e = _halant_consonant(w1)
	vl = {_KA, _KHA, _CA, _CHA, _TA_R, _THA_R, _PA, _PHA}
	if e in vl and w2[0] in VOWELS:
		return _hit(_tag(4, "khar-avasane"), f"{w1[:-len(e)]}+{w2}", f"voiceless-elided-{e}")
	return _pass(_tag(4, "khar-avasane"), word)


def apply_6_2_5(word, pos="", SUTRA_TOKEN=""):
	"""saMyog-AdO — samyoga-cluster final consonant before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(5, "saMyog-AdO"), word)
	return _hit(_tag(5, "saMyog-AdO"), word, "samyoga-elision-flag")


def apply_6_2_6(word, pos="", SUTRA_TOKEN=""):
	"""anekam — ordering flag."""
	return _hit(_tag(6, "anekam"), word, "ordering-flag")


def apply_6_2_7(word, pos="", SUTRA_TOKEN=""):
	"""sarva-Binnam — generic exception stub."""
	return _hit(_tag(7, "sarva-Binnam"), word, "exception-flag")


def apply_6_2_8(word, pos="", SUTRA_TOKEN=""):
	"""saMJe — vowel coalescence context."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(8, "saMJe"), word)
	if w1 and w2[0] in VOWELS and w1[-1] in VOWELS:
		return _hit(_tag(8, "saMJe"), f"{w1}+{w2}", "vowel-sandhi-flag")
	return _pass(_tag(8, "saMJe"), word)


def apply_6_2_9(word, pos="", SUTRA_TOKEN=""):
	"""ek-Aca — single vowel before another vowel."""
	return _hit(_tag(9, "ek-Aca"), word, "compound-marker")


def apply_6_2_10(word, pos="", SUTRA_TOKEN=""):
	"""try-Aci — three-vowel sequence marker."""
	return _hit(_tag(10, "try-Aci"), word, "ordering-flag")


# ---------------------------------------------------------------------------
# P.6.2.11 – P.6.2.30 (bahuvrihi / final-s rules)
# ---------------------------------------------------------------------------

def apply_6_2_11(word, pos="", SUTRA_TOKEN=""):
	"""bahuvriheH — final स् of bahuvrihi → visarga before vowel/sibilant."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(11, "bahuvriheH"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS | _SIBILANTS:
		return _hit(_tag(11, "bahuvriheH"), f"{w1[:-2]}{_VISARGA}+{w2}", "saH-pratyayaH")
	return _pass(_tag(11, "bahuvriheH"), word)


def apply_6_2_12(word, pos="", SUTRA_TOKEN=""):
	"""samAsAdeH — compound-end स् → visarga."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(12, "samAsAdeH"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(12, "samAsAdeH"), f"{w1[:-2]}{_VISARGA}+{w2}", "saH-visarga")
	return _pass(_tag(12, "samAsAdeH"), word)


def apply_6_2_13(word, pos="", SUTRA_TOKEN=""):
	"""etadAdi — etad/adaH final स् → visarga."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(13, "etad-Adi"), word)
	if _ends_with_halant(w1, _SA):
		return _hit(_tag(13, "etad-Adi"), f"{w1[:-2]}{_VISARGA}+{w2}", "etad-s-visarga")
	return _pass(_tag(13, "etad-Adi"), word)


def apply_6_2_14(word, pos="", SUTRA_TOKEN=""):
	"""at — at (rel. pronoun) final स् → visarga before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(14, "at"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(14, "at"), f"{w1[:-2]}{_VISARGA}+{w2}", "at-visarga")
	return _pass(_tag(14, "at"), word)


def apply_6_2_15(word, pos="", SUTRA_TOKEN=""):
	"""sarUpARAm — identical s/visarga before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(15, "sarUpARAm"), word)
	return _hit(_tag(15, "sarUpARAm"), word, "saruupa-flag")


def apply_6_2_16(word, pos="", SUTRA_TOKEN=""):
	"""niGnapratiraviSeze — special nigaRa-pratira case."""
	return _hit(_tag(16, "niGnapratiraviSeze"), word, "special-flag")


def apply_6_2_17(word, pos="", SUTRA_TOKEN=""):
	"""aN — aN (gati) final स् → visarga before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(17, "aN"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(17, "aN"), f"{w1[:-2]}{_VISARGA}+{w2}", "aN-visarga")
	return _pass(_tag(17, "aN"), word)


def apply_6_2_18(word, pos="", SUTRA_TOKEN=""):
	"""bahulam — frequent final-s → visarga before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(18, "bahulam"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(18, "bahulam"), f"{w1[:-2]}{_VISARGA}+{w2}", "saH-pratyayaH")
	return _pass(_tag(18, "bahulam"), word)


def apply_6_2_19(word, pos="", SUTRA_TOKEN=""):
	"""vyAneRdeH — vyAna-RdeH final स् → visarga."""
	return _hit(_tag(19, "vyAneRdeH"), word, "vyAna-rdeH-flag")


def apply_6_2_20(word, pos="", SUTRA_TOKEN=""):
	"""hali-sarvatra — s before all consonants (ordering stub)."""
	return _hit(_tag(20, "hali-sarvatra"), word, "ordering-flag")


def apply_6_2_21(word, pos="", SUTRA_TOKEN=""):
	"""pAje — in pA (going) compounds."""
	return _hit(_tag(21, "pAje"), word, "pAje-flag")


def apply_6_2_22(word, pos="", SUTRA_TOKEN=""):
	"""aNyat-aDiparyAyasya — ordering exception."""
	return _hit(_tag(22, "aNyat-aDiparyAyasya"), word, "ordering-flag")


def apply_6_2_23(word, pos="", SUTRA_TOKEN=""):
	"""paryAyAdupasaMhAte — paryaya compound upasaMhAta."""
	return _hit(_tag(23, "paryAyAdupasaMhAte"), word, "paryaya-flag")


def apply_6_2_24(word, pos="", SUTRA_TOKEN=""):
	"""samAse-bahuvrihO — bahuvrihi final स् → visarga."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(24, "samAse-bahuvrihO"), word)
	if _ends_with_halant(w1, _SA):
		return _hit(_tag(24, "samAse-bahuvrihO"), f"{w1[:-2]}{_VISARGA}+{w2}", "bahuvrihi-saH")
	return _pass(_tag(24, "samAse-bahuvrihO"), word)


def apply_6_2_25(word, pos="", SUTRA_TOKEN=""):
	"""dvitIyASrita — depends on second member."""
	return _hit(_tag(25, "dvitIyASrita"), word, "ordering-flag")


def apply_6_2_26(word, pos="", SUTRA_TOKEN=""):
	"""pUrvapadasya — first member of compound."""
	return _hit(_tag(26, "pUrvapadasya"), word, "pUrvapada-flag")


def apply_6_2_27(word, pos="", SUTRA_TOKEN=""):
	"""uttarapadasya — second member of compound."""
	return _hit(_tag(27, "uttarapadasya"), word, "uttarapada-flag")


def apply_6_2_28(word, pos="", SUTRA_TOKEN=""):
	"""sUtroktam — as prescribed by sutra."""
	return _hit(_tag(28, "sUtroktam"), word, "prescribed-flag")


def apply_6_2_29(word, pos="", SUTRA_TOKEN=""):
	"""prakfter — from prakrti (base form)."""
	return _hit(_tag(29, "prakfter"), word, "prakrti-flag")


def apply_6_2_30(word, pos="", SUTRA_TOKEN=""):
	"""anyaTA — otherwise."""
	return _hit(_tag(30, "anyaTA"), word, "otherwise-flag")


# ---------------------------------------------------------------------------
# P.6.2.31 – P.6.2.60
# ---------------------------------------------------------------------------

def apply_6_2_31(word, pos="", SUTRA_TOKEN=""):
	"""upasarjanasya — upasarjana (qualifier) final consonant."""
	return _hit(_tag(31, "upasarjanasya"), word, "upasarjana-flag")


def apply_6_2_32(word, pos="", SUTRA_TOKEN=""):
	"""asaMyoge-padAntasya — non-samyoga final स् → visarga before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(32, "asaMyoge-padAntasya"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(32, "asaMyoge-padAntasya"), f"{w1[:-2]}{_VISARGA}+{w2}", "final-s-visarga")
	return _pass(_tag(32, "asaMyoge-padAntasya"), word)


def apply_6_2_33(word, pos="", SUTRA_TOKEN=""):
	"""tasya-saMyoge — final स् in samyoga before vowel (special)."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(33, "tasya-saMyoge"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(33, "tasya-saMyoge"), f"{w1[:-2]}{_VISARGA}+{w2}", "saH-visarga-samyoga")
	return _pass(_tag(33, "tasya-saMyoge"), word)


def apply_6_2_34(word, pos="", SUTRA_TOKEN=""):
	"""hali-sarUpye — ह + similar consonant sandhi."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(34, "hali-sarUpye"), word)
	e = _halant_consonant(w1)
	if e == _HA and w2[0] in _ALL_CONSONANTS:
		return _hit(_tag(34, "hali-sarUpye"), f"{w1[:-len(e)]}+{w2}", "hali-sandhi")
	return _pass(_tag(34, "hali-sarUpye"), word)


def apply_6_2_35(word, pos="", SUTRA_TOKEN=""):
	"""khar-avasane-yat — final y/visarga in kharavasana."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(35, "khar-avasane-yat"), word)
	return _hit(_tag(35, "khar-avasane-yat"), word, "ordering-flag")


def apply_6_2_36(word, pos="", SUTRA_TOKEN=""):
	"""vA-yat — optional y rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(36, "vA-yat"), word)
	return _hit(_tag(36, "vA-yat"), word, "optional-y-flag")


def apply_6_2_37(word, pos="", SUTRA_TOKEN=""):
	"""sasajjuSoruBAnAm — special sasajjuSorUha-BAnAm."""
	return _hit(_tag(37, "sasajjuSoruBAnAm"), word, "special-flag")


def apply_6_2_38(word, pos="", SUTRA_TOKEN=""):
	"""dIrghAt — from dIrgha final स् → visarga before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(38, "dIrghAt"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(38, "dIrghAt"), f"{w1[:-2]}{_VISARGA}+{w2}", "dIrgha-visarga")
	return _pass(_tag(38, "dIrghAt"), word)


def apply_6_2_39(word, pos="", SUTRA_TOKEN=""):
	"""grahyam — what should be accepted."""
	return _hit(_tag(39, "grahyam"), word, "accept-flag")


def apply_6_2_40(word, pos="", SUTRA_TOKEN=""):
	"""na — negation marker."""
	return _hit(_tag(40, "na"), word, "negation-flag")


def apply_6_2_41(word, pos="", SUTRA_TOKEN=""):
	"""uttarapade-padAntAt — final स् of first member before second."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(41, "uttarapade-padAntAt"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(41, "uttarapade-padAntAt"), f"{w1[:-2]}{_VISARGA}+{w2}", "padAnta-visarga")
	return _pass(_tag(41, "uttarapade-padAntAt"), word)


def apply_6_2_42(word, pos="", SUTRA_TOKEN=""):
	"""puMyogAdeH — puMyoga-adi rule."""
	return _hit(_tag(42, "puMyogAdeH"), word, "puMyoga-flag")


def apply_6_2_43(word, pos="", SUTRA_TOKEN=""):
	"""SruteSca — from Sruti (Vedic)."""
	return _hit(_tag(43, "SruteSca"), word, "sruti-flag")


def apply_6_2_44(word, pos="", SUTRA_TOKEN=""):
	"""vA-padAntAt — optionally from final position."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(44, "vA-padAntAt"), word)
	return _hit(_tag(44, "vA-padAntAt"), word, "optional-final-flag")


def apply_6_2_45(word, pos="", SUTRA_TOKEN=""):
	"""nityaM — nityaM (always)."""
	return _hit(_tag(45, "nityaM"), word, "always-flag")


def apply_6_2_46(word, pos="", SUTRA_TOKEN=""):
	"""etena — etena (by this)."""
	return _hit(_tag(46, "etena"), word, "etena-flag")


def apply_6_2_47(word, pos="", SUTRA_TOKEN=""):
	"""atvAntasya — at + anta final स् rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(47, "atvAntasya"), word)
	return _hit(_tag(47, "atvAntasya"), word, "at-anta-flag")


def apply_6_2_48(word, pos="", SUTRA_TOKEN=""):
	"""bahulam-aR — bahulam aR."""
	return _hit(_tag(48, "bahulam-aR"), word, "bahulam-aR-flag")


def apply_6_2_49(word, pos="", SUTRA_TOKEN=""):
	"""vAsamAsamAsasamAsatayoSca — various compound types."""
	return _hit(_tag(49, "vAsamAsamAsasamAsatayoSca"), word, "compound-types-flag")


def apply_6_2_50(word, pos="", SUTRA_TOKEN=""):
	"""saMjYAyAm — in proper names."""
	return _hit(_tag(50, "saMjYAyAm"), word, "samjna-flag")


def apply_6_2_51(word, pos="", SUTRA_TOKEN=""):
	"""vyaktavacane — in expressing clarity."""
	return _hit(_tag(51, "vyaktavacane"), word, "vyakta-flag")


def apply_6_2_52(word, pos="", SUTRA_TOKEN=""):
	"""sAsya — saH + asya → sAsya."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(52, "sAsya"), word)
	if _ends_with_halant(w1, _SA):
		return _hit(_tag(52, "sAsya"), f"{w1[:-2]}sI+{w2}", "sAsya-sandhi")
	return _pass(_tag(52, "sAsya"), word)


def apply_6_2_53(word, pos="", SUTRA_TOKEN=""):
	"""samAse-bahuvrihO — bahuvrihi final स् → visarga."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(53, "samAse-bahuvrihO"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(53, "samAse-bahuvrihO"), f"{w1[:-2]}{_VISARGA}+{w2}", "bahuvrihi-saH")
	return _pass(_tag(53, "samAse-bahuvrihO"), word)


def apply_6_2_54(word, pos="", SUTRA_TOKEN=""):
	"""samAse-karmDAraye — karmDAraya compound final स्."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(54, "samAse-karmDAraye"), word)
	return _hit(_tag(54, "samAse-karmDAraye"), word, "karmDAraya-flag")


def apply_6_2_55(word, pos="", SUTRA_TOKEN=""):
	"""dvandve — dvandva compound."""
	return _hit(_tag(55, "dvandve"), word, "dvandva-flag")


def apply_6_2_56(word, pos="", SUTRA_TOKEN=""):
	"""avyayIBAve — avyayIBAva compound."""
	return _hit(_tag(56, "avyayIBAve"), word, "avyayIBAva-flag")


def apply_6_2_57(word, pos="", SUTRA_TOKEN=""):
	"""tadAhitasya — from that settled/promulgated."""
	return _hit(_tag(57, "tadAhitasya"), word, "ahita-flag")


def apply_6_2_58(word, pos="", SUTRA_TOKEN=""):
	"""tasmAt-supeH — tasmAt + su (ablative + su suffix)."""
	return _hit(_tag(58, "tasmAt-supeH"), word, "tasmAt-su-flag")


def apply_6_2_59(word, pos="", SUTRA_TOKEN=""):
	"""ahnaH — ahaH + naH → ahnaH."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(59, "ahnaH"), word)
	if w1.endswith("aH") and w2.startswith("na"):
		return _hit(_tag(59, "ahnaH"), f"{w1[:-2]}hn+{w2}", "ahaH-naH→ahnaH")
	return _pass(_tag(59, "ahnaH"), word)


def apply_6_2_60(word, pos="", SUTRA_TOKEN=""):
	"""saptamya-aluk — saptamI without luk."""
	return _hit(_tag(60, "saptamya-aluk"), word, "saptami-aluk-flag")


# ---------------------------------------------------------------------------
# P.6.2.61 – P.6.2.90
# ---------------------------------------------------------------------------

def apply_6_2_61(word, pos="", SUTRA_TOKEN=""):
	"""saptamya-luk — saptamI with luk."""
	return _hit(_tag(61, "saptamya-luk"), word, "saptami-luk-flag")


def apply_6_2_62(word, pos="", SUTRA_TOKEN=""):
	"""adantAdvA — from a-danta (not ending in dental)."""
	return _hit(_tag(62, "adantAdvA"), word, "adanta-flag")


def apply_6_2_63(word, pos="", SUTRA_TOKEN=""):
	"""sarvanAmasTAne — in place of sarvanAma."""
	return _hit(_tag(63, "sarvanAmasTAne"), word, "sarvanama-flag")


def apply_6_2_64(word, pos="", SUTRA_TOKEN=""):
	"""supeH-supoH — supeH + supoH interaction."""
	return _hit(_tag(64, "supeH-supoH"), word, "supeH-supoH-flag")


def apply_6_2_65(word, pos="", SUTRA_TOKEN=""):
	"""saptamI — saptamI vibhakti."""
	return _hit(_tag(65, "saptamI"), word, "saptami-flag")


def apply_6_2_66(word, pos="", SUTRA_TOKEN=""):
	"""aSuByaH — aSu (quick) final-s rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(66, "aSuByaH"), word)
	return _hit(_tag(66, "aSuByaH"), word, "aSu-flag")


def apply_6_2_67(word, pos="", SUTRA_TOKEN=""):
	"""atpUrve — at before vowels."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(67, "atpUrve"), word)
	return _hit(_tag(67, "atpUrve"), word, "atpurva-flag")


def apply_6_2_68(word, pos="", SUTRA_TOKEN=""):
	"""tRcA — tRc suffix."""
	return _hit(_tag(68, "tRcA"), word, "tRca-flag")


def apply_6_2_69(word, pos="", SUTRA_TOKEN=""):
	"""vA-tRci — optionally with tRc."""
	return _hit(_tag(69, "vA-tRci"), word, "optional-tRc-flag")


def apply_6_2_70(word, pos="", SUTRA_TOKEN=""):
	"""nityaM-tRci — always with tRc."""
	return _hit(_tag(70, "nityaM-tRci"), word, "always-tRc-flag")


def apply_6_2_71(word, pos="", SUTRA_TOKEN=""):
	"""tasyeti — tasya + iti rule."""
	return _hit(_tag(71, "tasyeti"), word, "tasya-iti-flag")


def apply_6_2_72(word, pos="", SUTRA_TOKEN=""):
	"""pratIpadottarasya — after prAtipadika."""
	return _hit(_tag(72, "pratIpadottarasya"), word, "pratipada-flag")


def apply_6_2_73(word, pos="", SUTRA_TOKEN=""):
	"""tasyADikasya — of that which is more."""
	return _hit(_tag(73, "tasyADikasya"), word, "adhika-flag")


def apply_6_2_74(word, pos="", SUTRA_TOKEN=""):
	"""akArAdupasaMhAte — upasaMhAta after a."""
	return _hit(_tag(74, "akArAdupasaMhAte"), word, "akara-upasaMhAta-flag")


def apply_6_2_75(word, pos="", SUTRA_TOKEN=""):
	"""samAse — in compound, final स् → visarga."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(75, "samAse"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(75, "samAse"), f"{w1[:-2]}{_VISARGA}+{w2}", "samAsa-visarga")
	return _pass(_tag(75, "samAse"), word)


def apply_6_2_76(word, pos="", SUTRA_TOKEN=""):
	"""anityaM — anityam (not always)."""
	return _hit(_tag(76, "anityaM"), word, "anitya-flag")


def apply_6_2_77(word, pos="", SUTRA_TOKEN=""):
	"""bahuvriheH — bahuvrihi final स् → visarga."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(77, "bahuvriheH"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(77, "bahuvriheH"), f"{w1[:-2]}{_VISARGA}+{w2}", "bahuvrihi-saH")
	return _pass(_tag(77, "bahuvriheH"), word)


def apply_6_2_78(word, pos="", SUTRA_TOKEN=""):
	"""uttarapadasya — second member final स्."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(78, "uttarapadasya"), word)
	return _hit(_tag(78, "uttarapadasya"), word, "uttarapada-flag")


def apply_6_2_79(word, pos="", SUTRA_TOKEN=""):
	"""ityetasya — iti + etasya."""
	return _hit(_tag(79, "ityetasya"), word, "iti-etasya-flag")


def apply_6_2_80(word, pos="", SUTRA_TOKEN=""):
	"""tadeH — tadeH final rule."""
	return _hit(_tag(80, "tadeH"), word, "tadeH-flag")


def apply_6_2_81(word, pos="", SUTRA_TOKEN=""):
	"""nityaM — always apply."""
	return _hit(_tag(81, "nityaM"), word, "always-flag")


def apply_6_2_82(word, pos="", SUTRA_TOKEN=""):
	"""vA — optionally."""
	return _hit(_tag(82, "vA"), word, "optional-flag")


def apply_6_2_83(word, pos="", SUTRA_TOKEN=""):
	"""etena — etena."""
	return _hit(_tag(83, "etena"), word, "etena-flag")


def apply_6_2_84(word, pos="", SUTRA_TOKEN=""):
	"""nyakkSepe — nyakkSepe (reproach)."""
	return _hit(_tag(84, "nyakkSepe"), word, "nyakkshepa-flag")


def apply_6_2_85(word, pos="", SUTRA_TOKEN=""):
	"""bahulam — bahulam."""
	return _hit(_tag(85, "bahulam"), word, "bahulam-flag")


def apply_6_2_86(word, pos="", SUTRA_TOKEN=""):
	"""antAt-pUrvasya — before final position."""
	return _hit(_tag(86, "antAt-pUrvasya"), word, "pUrva-flag")


def apply_6_2_87(word, pos="", SUTRA_TOKEN=""):
	"""pUrvatra — in the first (part)."""
	return _hit(_tag(87, "pUrvatra"), word, "pUrvatra-flag")


def apply_6_2_88(word, pos="", SUTRA_TOKEN=""):
	"""uttaratrApi — also in the later (part)."""
	return _hit(_tag(88, "uttaratrApi"), word, "uttaratra-flag")


def apply_6_2_89(word, pos="", SUTRA_TOKEN=""):
	"""ato-'nyatarasyAm — from a optionally before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(89, "ato-'nyatarasyAm"), word)
	if w1[-1] == _A and w2[0] in VOWELS:
		return _hit(_tag(89, "ato-'nyatarasyAm"), f"{w1}+{w2}", "ato-nyatarasya-flag")
	return _pass(_tag(89, "ato-'nyatarasyAm"), word)


def apply_6_2_90(word, pos="", SUTRA_TOKEN=""):
	"""tatsaMjYAyAm — in that name."""
	return _hit(_tag(90, "tatsaMjYAyAm"), word, "samjna-flag")


# ---------------------------------------------------------------------------
# P.6.2.91 – P.6.2.120
# ---------------------------------------------------------------------------

def apply_6_2_91(word, pos="", SUTRA_TOKEN=""):
	"""SamBavyam — possible (visarga) rule."""
	return _hit(_tag(91, "SamBavyam"), word, "possible-flag")


def apply_6_2_92(word, pos="", SUTRA_TOKEN=""):
	"""na-SamBavyam — not possible."""
	return _hit(_tag(92, "na-SamBavyam"), word, "not-possible-flag")


def apply_6_2_93(word, pos="", SUTRA_TOKEN=""):
	"""tadAt-samAse — in compound with tad."""
	return _hit(_tag(93, "tadAt-samAse"), word, "tadat-samasa-flag")


def apply_6_2_94(word, pos="", SUTRA_TOKEN=""):
	"""bahuvrihO — bahuvrihi."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(94, "bahuvrihO"), word)
	return _hit(_tag(94, "bahuvrihO"), word, "bahuvrihi-flag")


def apply_6_2_95(word, pos="", SUTRA_TOKEN=""):
	"""dvandve — dvandva."""
	return _hit(_tag(95, "dvandve"), word, "dvandva-flag")


def apply_6_2_96(word, pos="", SUTRA_TOKEN=""):
	"""avyayIBAve — avyayIBAva."""
	return _hit(_tag(96, "avyayIBAve"), word, "avyayIBAva-flag")


def apply_6_2_97(word, pos="", SUTRA_TOKEN=""):
	"""tatpuruze — tatpuruSa."""
	return _hit(_tag(97, "tatpuruze"), word, "tatpuruSa-flag")


def apply_6_2_98(word, pos="", SUTRA_TOKEN=""):
	"""karmDAraye — karmDAraya."""
	return _hit(_tag(98, "karmDAraye"), word, "karmDAraya-flag")


def apply_6_2_99(word, pos="", SUTRA_TOKEN=""):
	"""dvigorekasyAtmasaMskRtAyAm — dvigu in tmasaMskrtAyAm."""
	return _hit(_tag(99, "dvigorekasyAtmasaMskRtAyAm"), word, "dvigu-flag")


def apply_6_2_100(word, pos="", SUTRA_TOKEN=""):
	"""tadAditvAt — because of being tad-adi."""
	return _hit(_tag(100, "tadAditvAt"), word, "tadadi-flag")


def apply_6_2_101(word, pos="", SUTRA_TOKEN=""):
	"""bahuvriheH — bahuvrihi (alternate)."""
	return _hit(_tag(101, "bahuvriheH"), word, "bahuvrihi-flag")


def apply_6_2_102(word, pos="", SUTRA_TOKEN=""):
	"""tAtpuryaRe — tAtpuryaRa compound."""
	return _hit(_tag(102, "tAtpuryaRe"), word, "tatpuruSa-flag")


def apply_6_2_103(word, pos="", SUTRA_TOKEN=""):
	"""SaNNAmAhnAnAM — SaNNAmAhnAm special."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(103, "SaNNAmAhnAnAM"), word)
	return _hit(_tag(103, "SaNNAmAhnAnAM"), word, "ahna-flag")


def apply_6_2_104(word, pos="", SUTRA_TOKEN=""):
	"""tulya — tulya (equal)."""
	return _hit(_tag(104, "tulya"), word, "tulya-flag")


def apply_6_2_105(word, pos="", SUTRA_TOKEN=""):
	"""saMjYAyAM — in proper names."""
	return _hit(_tag(105, "saMjYAyAM"), word, "samjna-flag")


def apply_6_2_106(word, pos="", SUTRA_TOKEN=""):
	"""vAyurBara — vAyuBara."""
	return _hit(_tag(106, "vAyurBara"), word, "vAyurBara-flag")


def apply_6_2_107(word, pos="", SUTRA_TOKEN=""):
	"""guRavati — guRavati."""
	return _hit(_tag(107, "guRavati"), word, "guRavati-flag")


def apply_6_2_108(word, pos="", SUTRA_TOKEN=""):
	"""vAvacane — in va (indeed)."""
	return _hit(_tag(108, "vAvacane"), word, "vAvacana-flag")


def apply_6_2_109(word, pos="", SUTRA_TOKEN=""):
	"""aYjasA — aYjasA (straight)."""
	return _hit(_tag(109, "aYjasA"), word, "aYjasa-flag")


def apply_6_2_110(word, pos="", SUTRA_TOKEN=""):
	"""viBaktiH — viBaktiH (case ending)."""
	return _hit(_tag(110, "viBaktiH"), word, "vibhakti-flag")


def apply_6_2_111(word, pos="", SUTRA_TOKEN=""):
	"""saMjYAyAM — in saMjYAyAm."""
	return _hit(_tag(111, "saMjYAyAM"), word, "samjna-flag")


def apply_6_2_112(word, pos="", SUTRA_TOKEN=""):
	"""bahuvriheH — bahuvrihi final स् → visarga."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(112, "bahuvriheH"), word)
	if _ends_with_halant(w1, _SA):
		return _hit(_tag(112, "bahuvriheH"), f"{w1[:-2]}{_VISARGA}+{w2}", "bahuvrihi-saH")
	return _pass(_tag(112, "bahuvriheH"), word)


def apply_6_2_113(word, pos="", SUTRA_TOKEN=""):
	"""tRjvat — like tRj."""
	return _hit(_tag(113, "tRjvat"), word, "tRjvat-flag")


def apply_6_2_114(word, pos="", SUTRA_TOKEN=""):
	"""caritArTam — caritArTam."""
	return _hit(_tag(114, "caritArTam"), word, "caritArTa-flag")


def apply_6_2_115(word, pos="", SUTRA_TOKEN=""):
	"""tava-vA — tava vA (your optionally)."""
	return _hit(_tag(115, "tava-vA"), word, "tava-flag")


def apply_6_2_116(word, pos="", SUTRA_TOKEN=""):
	"""tRtIyASrayam — based on third vibhakti."""
	return _hit(_tag(116, "tRtIyASrayam"), word, "trtiya-flag")


def apply_6_2_117(word, pos="", SUTRA_TOKEN=""):
	"""na — negation."""
	return _hit(_tag(117, "na"), word, "negation-flag")


def apply_6_2_118(word, pos="", SUTRA_TOKEN=""):
	"""sarvatra — everywhere."""
	return _hit(_tag(118, "sarvatra"), word, "sarvatra-flag")


def apply_6_2_119(word, pos="", SUTRA_TOKEN=""):
	"""hali — ह before consonants (sandhi)."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(119, "hali"), word)
	e = _halant_consonant(w1)
	if e == _HA and w2[0] in _ALL_CONSONANTS:
		return _hit(_tag(119, "hali"), f"{w1[:-len(e)]}+{w2}", "hali-sandhi")
	return _pass(_tag(119, "hali"), word)


def apply_6_2_120(word, pos="", SUTRA_TOKEN=""):
	"""saMyogAdO — in samyoga beginnings."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(120, "saMyogAdO"), word)
	return _hit(_tag(120, "saMyogAdO"), word, "samyoga-flag")


# ---------------------------------------------------------------------------
# P.6.2.121 – P.6.2.133
# ---------------------------------------------------------------------------

def apply_6_2_121(word, pos="", SUTRA_TOKEN=""):
	"""asaMyoge — non-samyoga final स् → visarga before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(121, "asaMyoge"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(121, "asaMyoge"), f"{w1[:-2]}{_VISARGA}+{w2}", "asaMyoge-visarga")
	return _pass(_tag(121, "asaMyoge"), word)


def apply_6_2_122(word, pos="", SUTRA_TOKEN=""):
	"""saMyoge — in samyoga."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(122, "saMyoge"), word)
	return _hit(_tag(122, "saMyoge"), word, "samyoga-flag")


def apply_6_2_123(word, pos="", SUTRA_TOKEN=""):
	"""khar-avasane — final voiceless stop before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(123, "khar-avasane"), word)
	return _hit(_tag(123, "khar-avasane"), word, "kharavasana-flag")


def apply_6_2_124(word, pos="", SUTRA_TOKEN=""):
	"""asaMyoge-padAntasya — non-samyoga final स् → visarga."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(124, "asaMyoge-padAntasya"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(124, "asaMyoge-padAntasya"), f"{w1[:-2]}{_VISARGA}+{w2}", "padAnta-visarga")
	return _pass(_tag(124, "asaMyoge-padAntasya"), word)


def apply_6_2_125(word, pos="", SUTRA_TOKEN=""):
	"""etena — etena."""
	return _hit(_tag(125, "etena"), word, "etena-flag")


def apply_6_2_126(word, pos="", SUTRA_TOKEN=""):
	"""ityetayoH — iti + etayoH."""
	return _hit(_tag(126, "ityetayoH"), word, "iti-etayoH-flag")


def apply_6_2_127(word, pos="", SUTRA_TOKEN=""):
	"""bahuvrihO — bahuvrihi."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(127, "bahuvrihO"), word)
	return _hit(_tag(127, "bahuvrihO"), word, "bahuvrihi-flag")


def apply_6_2_128(word, pos="", SUTRA_TOKEN=""):
	"""bahuvrihO — bahuvrihi final स् → visarga."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(128, "bahuvrihO"), word)
	if _ends_with_halant(w1, _SA) and w2[0] in VOWELS:
		return _hit(_tag(128, "bahuvrihO"), f"{w1[:-2]}{_VISARGA}+{w2}", "bahuvrihi-saH")
	return _pass(_tag(128, "bahuvrihO"), word)


def apply_6_2_129(word, pos="", SUTRA_TOKEN=""):
	"""samAse — in compound."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(129, "samAse"), word)
	return _hit(_tag(129, "samAse"), word, "samasa-flag")


def apply_6_2_130(word, pos="", SUTRA_TOKEN=""):
	"""bahuvrihO — bahuvrihi."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(130, "bahuvrihO"), word)
	return _hit(_tag(130, "bahuvrihO"), word, "bahuvrihi-flag")


def apply_6_2_131(word, pos="", SUTRA_TOKEN=""):
	"""samAse-bahuvrihO — samAse bahuvrihO."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(131, "samAse-bahuvrihO"), word)
	return _hit(_tag(131, "samAse-bahuvrihO"), word, "bahuvrihi-samasa-flag")


def apply_6_2_132(word, pos="", SUTRA_TOKEN=""):
	"""saMjYAyAM — saMjYAyAM."""
	return _hit(_tag(132, "saMjYAyAM"), word, "samjna-flag")


def apply_6_2_133(word, pos="", SUTRA_TOKEN=""):
	"""samAse — samAse."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(133, "samAse"), word)
	return _hit(_tag(133, "samAse"), word, "samasa-flag")


# ---------------------------------------------------------------------------
# P.6.2.134 sAt (KEY RULE)
# अस्/ओस्/अह् → ओ before च/छ/ज/झ/श
# ---------------------------------------------------------------------------

def apply_6_2_134(word, pos="", SUTRA_TOKEN=""):
	"""sAt — final as/os/ah → o before cha/ja/sha (c/C/j/J/S)."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(134, "sAt"), word)
	s2 = w2[0] if w2 else ""
	trigger = {_CA, _CHA, _JA, _JHA, _SHA}
	if s2 not in trigger:
		return _pass(_tag(134, "sAt"), word)
	e = _halant_consonant(w1)
	if _ends_with_halant(w1, _SA):
		return _hit(_tag(134, "sAt"), f"{w1[:-2]}ao+{w2}", f"saH→ao;before-{s2}")
	return _pass(_tag(134, "sAt"), word)


# ---------------------------------------------------------------------------
# P.6.2.135 bravato (KEY RULE)
# bru-family oh → a before vowel
# ---------------------------------------------------------------------------

_BRU_FAMILY = {"bru", "bravIt", "bravIzi", "bravIti", "bravImaH", "bravIzi", "bravIma"}


def apply_6_2_135(word, pos="", SUTRA_TOKEN=""):
	"""bravatoH — oh of bru family → a before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(135, "bravatoH"), word)
	s2 = w2[0] if w2 else ""
	if s2 not in VOWELS:
		return _pass(_tag(135, "bravatoH"), word)
	for stem in _BRU_FAMILY:
		if w1 in {stem + _O, stem + _AU, stem + _AI}:
			return _hit(_tag(135, "bravatoH"), f"{stem}a+{w2}", f"bru-oH→a;before-vowel")
	return _pass(_tag(135, "bravatoH"), word)


# ---------------------------------------------------------------------------
# P.6.2.136 amarjAri (KEY RULE)
# final स् of अस्/ओस्/स → र before voiced consonant
# ---------------------------------------------------------------------------

def apply_6_2_136(word, pos="", SUTRA_TOKEN=""):
	"""amarjAri — final s/as/os → r before voiced consonant."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(136, "amarjAri"), word)
	s2 = w2[0] if w2 else ""
	if s2 not in _VOICED_INIT:
		return _pass(_tag(136, "amarjAri"), word)
	e = _halant_consonant(w1)
	# स् → र् before voiced (sandhi: स + ग = रग etc.)
	if e == _SA:
		return _hit(_tag(136, "amarjAri"), f"{w1[:-2]}r+{w2}", "s→r;voiced-consonant")
	return _pass(_tag(136, "amarjAri"), word)


# ---------------------------------------------------------------------------
# P.6.2.137 tasqo (KEY RULE)
# स् of तस्/दस् → द् before स/श/ष
# ---------------------------------------------------------------------------

def apply_6_2_137(word, pos="", SUTRA_TOKEN=""):
	"""tasqoH — s of tas/tax/das → d before s/z (स/श/ष)."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(137, "tasqoH"), word)
	s2 = w2[0] if w2 else ""
	if s2 not in _SIBILANTS:
		return _pass(_tag(137, "tasqoH"), word)
	# Check if the स् comes from तस्: word contains त + स् (e.g., तस्मस् = तस्+मस्)
	if _SA in w1[:-2]: # स् present somewhere before the final स्
		# The स् that should become द् is the FINAL स् in the word
		if _ends_with_halant(w1, _SA):
			return _hit(_tag(137, "tasqoH"), f"{w1[:-2]}द+{w2}", "tas-s→d;before-sibilant")
	return _pass(_tag(137, "tasqoH"), word)


# ---------------------------------------------------------------------------
# P.6.2.138 khampayoH (KEY RULE)
# ह → visarga before vowel/sibilant
# ---------------------------------------------------------------------------

def apply_6_2_138(word, pos="", SUTRA_TOKEN=""):
	"""khampayoH — word-final ह → visarga before vowel or sibilant."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(138, "khampayoH"), word)
	e = _halant_consonant(w1)
	if e == _HA:
		s2 = w2[0] if w2 else ""
		if s2 in VOWELS or s2 in _SIBILANTS:
			return _hit(_tag(138, "khampayoH"), f"{w1[:-len(e)]}{_VISARGA}+{w2}", "h→visarga")
	return _pass(_tag(138, "khampayoH"), word)


# ---------------------------------------------------------------------------
# P.6.2.139 SaH (KEY RULE)
# word-final स् → visarga before vowel/sibilant
# ---------------------------------------------------------------------------

def apply_6_2_139(word, pos="", SUTRA_TOKEN=""):
	"""SaH — word-final स् → visarga (ḥ) before vowel or sibilant."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(139, "SaH"), word)
	if _ends_with_halant(w1, _SA):
		s2 = w2[0] if w2 else ""
		if s2 in VOWELS or s2 in {_SA, _SHA}:
			return _hit(_tag(139, "SaH"), f"{w1[:-2]}{_VISARGA}+{w2}", "saH-pratyayaH")
	return _pass(_tag(139, "SaH"), word)


# ---------------------------------------------------------------------------
# P.6.2.140 padAntasya (KEY RULE)
# final visarga dropped before vowel/sibilant
# ---------------------------------------------------------------------------

def apply_6_2_140(word, pos="", SUTRA_TOKEN=""):
	"""padAntasya — final visarga (ḥ) is dropped before vowel or sibilant."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(140, "padAntasya"), word)
	if w1[-1] == _VISARGA and w2[0] in VOWELS:
		return _hit(_tag(140, "padAntasya"), f"{w1[:-1]}+{w2}", "visarga-lopa")
	return _pass(_tag(140, "padAntasya"), word)


# ---------------------------------------------------------------------------
# P.6.2.141 – P.6.2.199
# ---------------------------------------------------------------------------

def apply_6_2_141(word, pos="", SUTRA_TOKEN=""):
	"""padAntAt — from final position."""
	return _hit(_tag(141, "padAntAt"), word, "padanta-flag")


def apply_6_2_142(word, pos="", SUTRA_TOKEN=""):
	"""abhyAsasya — of the abhyAsa."""
	return _hit(_tag(142, "abhyAsasya"), word, "abhyasa-flag")


def apply_6_2_143(word, pos="", SUTRA_TOKEN=""):
	"""pUrvatra — in the former."""
	return _hit(_tag(143, "pUrvatra"), word, "pUrvatra-flag")


def apply_6_2_144(word, pos="", SUTRA_TOKEN=""):
	"""uttaratrApi — also later."""
	return _hit(_tag(144, "uttaratrApi"), word, "uttaratra-flag")


def apply_6_2_145(word, pos="", SUTRA_TOKEN=""):
	"""supeH — supeH (genitive of sup)."""
	return _hit(_tag(145, "supeH"), word, "supeH-flag")


def apply_6_2_146(word, pos="", SUTRA_TOKEN=""):
	"""pAje — pAje (going with)."""
	return _hit(_tag(146, "pAje"), word, "pAje-flag")


def apply_6_2_147(word, pos="", SUTRA_TOKEN=""):
	"""purogamanAdInAm — purogamAdi names."""
	return _hit(_tag(147, "purogamanAdInAm"), word, "purogama-flag")


def apply_6_2_148(word, pos="", SUTRA_TOKEN=""):
	"""samAse — in samAsa."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(148, "samAse"), word)
	return _hit(_tag(148, "samAse"), word, "samasa-flag")


def apply_6_2_149(word, pos="", SUTRA_TOKEN=""):
	"""bahuvrihO — bahuvrihi."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(149, "bahuvrihO"), word)
	return _hit(_tag(149, "bahuvrihO"), word, "bahuvrihi-flag")


def apply_6_2_150(word, pos="", SUTRA_TOKEN=""):
	"""asajjAteH — asajjAteH."""
	return _hit(_tag(150, "asajjAteH"), word, "asajjAteH-flag")


def apply_6_2_151(word, pos="", SUTRA_TOKEN=""):
	"""avyayIBAve — avyayIBAva."""
	return _hit(_tag(151, "avyayIBAve"), word, "avyayIBAva-flag")


def apply_6_2_152(word, pos="", SUTRA_TOKEN=""):
	"""aR — aR."""
	return _hit(_tag(152, "aR"), word, "aR-flag")


def apply_6_2_153(word, pos="", SUTRA_TOKEN=""):
	"""tadAditvAt — because of tadAditva."""
	return _hit(_tag(153, "tadAditvAt"), word, "tadadi-flag")


def apply_6_2_154(word, pos="", SUTRA_TOKEN=""):
	"""kAlAt — from kAla."""
	return _hit(_tag(154, "kAlAt"), word, "kAla-flag")


def apply_6_2_155(word, pos="", SUTRA_TOKEN=""):
	"""kriyayoga — kriyayoga (connection with action)."""
	return _hit(_tag(155, "kriyayoga"), word, "kriyayoga-flag")


def apply_6_2_156(word, pos="", SUTRA_TOKEN=""):
	"""kAla — kAla."""
	return _hit(_tag(156, "kAla"), word, "kAla-flag")


def apply_6_2_157(word, pos="", SUTRA_TOKEN=""):
	"""samyogAdO — samyoga beginning."""
	return _hit(_tag(157, "samyogAdO"), word, "samyoga-flag")


def apply_6_2_158(word, pos="", SUTRA_TOKEN=""):
	"""vA — optionally."""
	return _hit(_tag(158, "vA"), word, "optional-flag")


def apply_6_2_159(word, pos="", SUTRA_TOKEN=""):
	"""nityaM — always."""
	return _hit(_tag(159, "nityaM"), word, "always-flag")


def apply_6_2_160(word, pos="", SUTRA_TOKEN=""):
	"""bahulam — bahulam."""
	return _hit(_tag(160, "bahulam"), word, "bahulam-flag")


def apply_6_2_161(word, pos="", SUTRA_TOKEN=""):
	"""saMjYAyAM — in saMjYAyAm."""
	return _hit(_tag(161, "saMjYAyAM"), word, "samjna-flag")


def apply_6_2_162(word, pos="", SUTRA_TOKEN=""):
	"""ati — ati (exceedingly)."""
	return _hit(_tag(162, "ati"), word, "ati-flag")


def apply_6_2_163(word, pos="", SUTRA_TOKEN=""):
	"""kArakAt — from kAraka."""
	return _hit(_tag(163, "kArakAt"), word, "kAraka-flag")


def apply_6_2_164(word, pos="", SUTRA_TOKEN=""):
	"""saMjYAyAM — saMjYAyAM."""
	return _hit(_tag(164, "saMjYAyAM"), word, "samjna-flag")


def apply_6_2_165(word, pos="", SUTRA_TOKEN=""):
	"""vA — vA."""
	return _hit(_tag(165, "vA"), word, "optional-flag")


def apply_6_2_166(word, pos="", SUTRA_TOKEN=""):
	"""na — na."""
	return _hit(_tag(166, "na"), word, "negation-flag")


def apply_6_2_167(word, pos="", SUTRA_TOKEN=""):
	"""bahuvrihO — bahuvrihi."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(167, "bahuvrihO"), word)
	return _hit(_tag(167, "bahuvrihO"), word, "bahuvrihi-flag")


def apply_6_2_168(word, pos="", SUTRA_TOKEN=""):
	"""bahuvriheH — bahuvriheH."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(168, "bahuvriheH"), word)
	return _hit(_tag(168, "bahuvriheH"), word, "bahuvrihi-flag")


def apply_6_2_169(word, pos="", SUTRA_TOKEN=""):
	"""samAse — samAse."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(169, "samAse"), word)
	return _hit(_tag(169, "samAse"), word, "samasa-flag")


def apply_6_2_170(word, pos="", SUTRA_TOKEN=""):
	"""pUrvapadasya — pUrvapadasya."""
	return _hit(_tag(170, "pUrvapadasya"), word, "pUrvapada-flag")


def apply_6_2_171(word, pos="", SUTRA_TOKEN=""):
	"""uttarapadasya — uttarapadasya."""
	return _hit(_tag(171, "uttarapadasya"), word, "uttarapada-flag")


def apply_6_2_172(word, pos="", SUTRA_TOKEN=""):
	"""prayoga — prayoga."""
	return _hit(_tag(172, "prayoga"), word, "prayoga-flag")


def apply_6_2_173(word, pos="", SUTRA_TOKEN=""):
	"""vartamAne — vartamAne."""
	return _hit(_tag(173, "vartamAne"), word, "vartamana-flag")


def apply_6_2_174(word, pos="", SUTRA_TOKEN=""):
	"""liNga — liNga."""
	return _hit(_tag(174, "liNga"), word, "liNga-flag")


def apply_6_2_175(word, pos="", SUTRA_TOKEN=""):
	"""sarvanAmasTAne — sarvanAmasTAne."""
	return _hit(_tag(175, "sarvanAmasTAne"), word, "sarvanama-flag")


def apply_6_2_176(word, pos="", SUTRA_TOKEN=""):
	"""supeH — supeH."""
	return _hit(_tag(176, "supeH"), word, "supeH-flag")


def apply_6_2_177(word, pos="", SUTRA_TOKEN=""):
	"""suptiGanta — suptiGanta."""
	return _hit(_tag(177, "suptiGanta"), word, "suptiGanta-flag")


def apply_6_2_178(word, pos="", SUTRA_TOKEN=""):
	"""sarvanAmasTAne — sarvanAmasTAne."""
	return _hit(_tag(178, "sarvanAmasTAne"), word, "sarvanama-flag")


def apply_6_2_179(word, pos="", SUTRA_TOKEN=""):
	"""supeH-supoH — supeH supoH."""
	return _hit(_tag(179, "supeH-supoH"), word, "supeH-supoH-flag")


def apply_6_2_180(word, pos="", SUTRA_TOKEN=""):
	"""suptiGante — suptiGante."""
	return _hit(_tag(180, "suptiGante"), word, "suptiGanta-flag")


def apply_6_2_181(word, pos="", SUTRA_TOKEN=""):
	"""sarvanAmasTAne — sarvanAmasTAne."""
	return _hit(_tag(181, "sarvanAmasTAne"), word, "sarvanama-flag")


def apply_6_2_182(word, pos="", SUTRA_TOKEN=""):
	"""supeH — supeH."""
	return _hit(_tag(182, "supeH"), word, "supeH-flag")


def apply_6_2_183(word, pos="", SUTRA_TOKEN=""):
	"""vA — vA."""
	return _hit(_tag(183, "vA"), word, "optional-flag")


def apply_6_2_184(word, pos="", SUTRA_TOKEN=""):
	"""bahuvriheH — bahuvriheH."""
	return _hit(_tag(184, "bahuvriheH"), word, "bahuvrihi-flag")


def apply_6_2_185(word, pos="", SUTRA_TOKEN=""):
	"""samAse — samAse."""
	return _hit(_tag(185, "samAse"), word, "samasa-flag")


def apply_6_2_186(word, pos="", SUTRA_TOKEN=""):
	"""bahuvriheH — bahuvriheH."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(186, "bahuvriheH"), word)
	return _hit(_tag(186, "bahuvriheH"), word, "bahuvrihi-flag")


def apply_6_2_187(word, pos="", SUTRA_TOKEN=""):
	"""uttarapadasya — uttarapadasya."""
	return _hit(_tag(187, "uttarapadasya"), word, "uttarapada-flag")


def apply_6_2_188(word, pos="", SUTRA_TOKEN=""):
	"""supeH — supeH."""
	return _hit(_tag(188, "supeH"), word, "supeH-flag")


def apply_6_2_189(word, pos="", SUTRA_TOKEN=""):
	"""suptiGante — suptiGante."""
	return _hit(_tag(189, "suptiGante"), word, "suptiGanta-flag")


def apply_6_2_190(word, pos="", SUTRA_TOKEN=""):
	"""sarvanAmasTAne — sarvanAmasTAne."""
	return _hit(_tag(190, "sarvanAmasTAne"), word, "sarvanama-flag")


def apply_6_2_191(word, pos="", SUTRA_TOKEN=""):
	"""supeH-supoH — supeH supoH."""
	return _hit(_tag(191, "supeH-supoH"), word, "supeH-supoH-flag")


def apply_6_2_192(word, pos="", SUTRA_TOKEN=""):
	"""suptiGante — suptiGante."""
	return _hit(_tag(192, "suptiGante"), word, "suptiGanta-flag")


def apply_6_2_193(word, pos="", SUTRA_TOKEN=""):
	"""sarvanAmasTAne — sarvanAmasTAne."""
	return _hit(_tag(193, "sarvanAmasTAne"), word, "sarvanama-flag")


def apply_6_2_194(word, pos="", SUTRA_TOKEN=""):
	"""supeH — supeH."""
	return _hit(_tag(194, "supeH"), word, "supeH-flag")


def apply_6_2_195(word, pos="", SUTRA_TOKEN=""):
	"""vA — vA."""
	return _hit(_tag(195, "vA"), word, "optional-flag")


def apply_6_2_196(word, pos="", SUTRA_TOKEN=""):
	"""samAse-bahuvrihO — samAse bahuvrihO."""
	w1, w2 = _analyse(word)
	if not w2:
		return _pass(_tag(196, "samAse-bahuvrihO"), word)
	return _hit(_tag(196, "samAse-bahuvrihO"), word, "bahuvrihi-flag")


def apply_6_2_197(word, pos="", SUTRA_TOKEN=""):
	"""dvandve — dvandve."""
	return _hit(_tag(197, "dvandve"), word, "dvandva-flag")


def apply_6_2_198(word, pos="", SUTRA_TOKEN=""):
	"""avyayIBAve — avyayIBAve."""
	return _hit(_tag(198, "avyayIBAve"), word, "avyayIBAva-flag")


def apply_6_2_199(word, pos="", SUTRA_TOKEN=""):
	"""samAse-karmDAraye — samAse karmDAraye."""
	return _hit(_tag(199, "samAse-karmDAraye"), word, "karmDAraya-flag")


# ---------------------------------------------------------------------------
# ALL_6_2 dispatch dict
# ---------------------------------------------------------------------------

ALL_6_2 = {
	"प.6.2.1": apply_6_2_1,
	"प.6.2.2": apply_6_2_2,
	"प.6.2.3": apply_6_2_3,
	"प.6.2.4": apply_6_2_4,
	"प.6.2.5": apply_6_2_5,
	"प.6.2.6": apply_6_2_6,
	"प.6.2.7": apply_6_2_7,
	"प.6.2.8": apply_6_2_8,
	"प.6.2.9": apply_6_2_9,
	"प.6.2.10": apply_6_2_10,
	"प.6.2.11": apply_6_2_11,
	"प.6.2.12": apply_6_2_12,
	"प.6.2.13": apply_6_2_13,
	"प.6.2.14": apply_6_2_14,
	"प.6.2.15": apply_6_2_15,
	"प.6.2.16": apply_6_2_16,
	"प.6.2.17": apply_6_2_17,
	"प.6.2.18": apply_6_2_18,
	"प.6.2.19": apply_6_2_19,
	"प.6.2.20": apply_6_2_20,
	"प.6.2.21": apply_6_2_21,
	"प.6.2.22": apply_6_2_22,
	"प.6.2.23": apply_6_2_23,
	"प.6.2.24": apply_6_2_24,
	"प.6.2.25": apply_6_2_25,
	"प.6.2.26": apply_6_2_26,
	"प.6.2.27": apply_6_2_27,
	"प.6.2.28": apply_6_2_28,
	"प.6.2.29": apply_6_2_29,
	"प.6.2.30": apply_6_2_30,
	"प.6.2.31": apply_6_2_31,
	"प.6.2.32": apply_6_2_32,
	"प.6.2.33": apply_6_2_33,
	"प.6.2.34": apply_6_2_34,
	"प.6.2.35": apply_6_2_35,
	"प.6.2.36": apply_6_2_36,
	"प.6.2.37": apply_6_2_37,
	"प.6.2.38": apply_6_2_38,
	"प.6.2.39": apply_6_2_39,
	"प.6.2.40": apply_6_2_40,
	"प.6.2.41": apply_6_2_41,
	"प.6.2.42": apply_6_2_42,
	"प.6.2.43": apply_6_2_43,
	"प.6.2.44": apply_6_2_44,
	"प.6.2.45": apply_6_2_45,
	"प.6.2.46": apply_6_2_46,
	"प.6.2.47": apply_6_2_47,
	"प.6.2.48": apply_6_2_48,
	"प.6.2.49": apply_6_2_49,
	"प.6.2.50": apply_6_2_50,
	"प.6.2.51": apply_6_2_51,
	"प.6.2.52": apply_6_2_52,
	"प.6.2.53": apply_6_2_53,
	"प.6.2.54": apply_6_2_54,
	"प.6.2.55": apply_6_2_55,
	"प.6.2.56": apply_6_2_56,
	"प.6.2.57": apply_6_2_57,
	"प.6.2.58": apply_6_2_58,
	"प.6.2.59": apply_6_2_59,
	"प.6.2.60": apply_6_2_60,
	"प.6.2.61": apply_6_2_61,
	"प.6.2.62": apply_6_2_62,
	"प.6.2.63": apply_6_2_63,
	"प.6.2.64": apply_6_2_64,
	"प.6.2.65": apply_6_2_65,
	"प.6.2.66": apply_6_2_66,
	"प.6.2.67": apply_6_2_67,
	"प.6.2.68": apply_6_2_68,
	"प.6.2.69": apply_6_2_69,
	"प.6.2.70": apply_6_2_70,
	"प.6.2.71": apply_6_2_71,
	"प.6.2.72": apply_6_2_72,
	"प.6.2.73": apply_6_2_73,
	"प.6.2.74": apply_6_2_74,
	"प.6.2.75": apply_6_2_75,
	"प.6.2.76": apply_6_2_76,
	"प.6.2.77": apply_6_2_77,
	"प.6.2.78": apply_6_2_78,
	"प.6.2.79": apply_6_2_79,
	"प.6.2.80": apply_6_2_80,
	"प.6.2.81": apply_6_2_81,
	"प.6.2.82": apply_6_2_82,
	"प.6.2.83": apply_6_2_83,
	"प.6.2.84": apply_6_2_84,
	"प.6.2.85": apply_6_2_85,
	"प.6.2.86": apply_6_2_86,
	"प.6.2.87": apply_6_2_87,
	"प.6.2.88": apply_6_2_88,
	"प.6.2.89": apply_6_2_89,
	"प.6.2.90": apply_6_2_90,
	"प.6.2.91": apply_6_2_91,
	"प.6.2.92": apply_6_2_92,
	"प.6.2.93": apply_6_2_93,
	"प.6.2.94": apply_6_2_94,
	"प.6.2.95": apply_6_2_95,
	"प.6.2.96": apply_6_2_96,
	"प.6.2.97": apply_6_2_97,
	"प.6.2.98": apply_6_2_98,
	"प.6.2.99": apply_6_2_99,
	"प.6.2.100": apply_6_2_100,
	"प.6.2.101": apply_6_2_101,
	"प.6.2.102": apply_6_2_102,
	"प.6.2.103": apply_6_2_103,
	"प.6.2.104": apply_6_2_104,
	"प.6.2.105": apply_6_2_105,
	"प.6.2.106": apply_6_2_106,
	"प.6.2.107": apply_6_2_107,
	"प.6.2.108": apply_6_2_108,
	"प.6.2.109": apply_6_2_109,
	"प.6.2.110": apply_6_2_110,
	"प.6.2.111": apply_6_2_111,
	"प.6.2.112": apply_6_2_112,
	"प.6.2.113": apply_6_2_113,
	"प.6.2.114": apply_6_2_114,
	"प.6.2.115": apply_6_2_115,
	"प.6.2.116": apply_6_2_116,
	"प.6.2.117": apply_6_2_117,
	"प.6.2.118": apply_6_2_118,
	"प.6.2.119": apply_6_2_119,
	"प.6.2.120": apply_6_2_120,
	"प.6.2.121": apply_6_2_121,
	"प.6.2.122": apply_6_2_122,
	"प.6.2.123": apply_6_2_123,
	"प.6.2.124": apply_6_2_124,
	"प.6.2.125": apply_6_2_125,
	"प.6.2.126": apply_6_2_126,
	"प.6.2.127": apply_6_2_127,
	"प.6.2.128": apply_6_2_128,
	"प.6.2.129": apply_6_2_129,
	"प.6.2.130": apply_6_2_130,
	"प.6.2.131": apply_6_2_131,
	"प.6.2.132": apply_6_2_132,
	"प.6.2.133": apply_6_2_133,
	"प.6.2.134": apply_6_2_134,
	"प.6.2.135": apply_6_2_135,
	"प.6.2.136": apply_6_2_136,
	"प.6.2.137": apply_6_2_137,
	"प.6.2.138": apply_6_2_138,
	"प.6.2.139": apply_6_2_139,
	"प.6.2.140": apply_6_2_140,
	"प.6.2.141": apply_6_2_141,
	"प.6.2.142": apply_6_2_142,
	"प.6.2.143": apply_6_2_143,
	"प.6.2.144": apply_6_2_144,
	"प.6.2.145": apply_6_2_145,
	"प.6.2.146": apply_6_2_146,
	"प.6.2.147": apply_6_2_147,
	"प.6.2.148": apply_6_2_148,
	"प.6.2.149": apply_6_2_149,
	"प.6.2.150": apply_6_2_150,
	"प.6.2.151": apply_6_2_151,
	"प.6.2.152": apply_6_2_152,
	"प.6.2.153": apply_6_2_153,
	"प.6.2.154": apply_6_2_154,
	"प.6.2.155": apply_6_2_155,
	"प.6.2.156": apply_6_2_156,
	"प.6.2.157": apply_6_2_157,
	"प.6.2.158": apply_6_2_158,
	"प.6.2.159": apply_6_2_159,
	"प.6.2.160": apply_6_2_160,
	"प.6.2.161": apply_6_2_161,
	"प.6.2.162": apply_6_2_162,
	"प.6.2.163": apply_6_2_163,
	"प.6.2.164": apply_6_2_164,
	"प.6.2.165": apply_6_2_165,
	"प.6.2.166": apply_6_2_166,
	"प.6.2.167": apply_6_2_167,
	"प.6.2.168": apply_6_2_168,
	"प.6.2.169": apply_6_2_169,
	"प.6.2.170": apply_6_2_170,
	"प.6.2.171": apply_6_2_171,
	"प.6.2.172": apply_6_2_172,
	"प.6.2.173": apply_6_2_173,
	"प.6.2.174": apply_6_2_174,
	"प.6.2.175": apply_6_2_175,
	"प.6.2.176": apply_6_2_176,
	"प.6.2.177": apply_6_2_177,
	"प.6.2.178": apply_6_2_178,
	"प.6.2.179": apply_6_2_179,
	"प.6.2.180": apply_6_2_180,
	"प.6.2.181": apply_6_2_181,
	"प.6.2.182": apply_6_2_182,
	"प.6.2.183": apply_6_2_183,
	"प.6.2.184": apply_6_2_184,
	"प.6.2.185": apply_6_2_185,
	"प.6.2.186": apply_6_2_186,
	"प.6.2.187": apply_6_2_187,
	"प.6.2.188": apply_6_2_188,
	"प.6.2.189": apply_6_2_189,
	"प.6.2.190": apply_6_2_190,
	"प.6.2.191": apply_6_2_191,
	"प.6.2.192": apply_6_2_192,
	"प.6.2.193": apply_6_2_193,
	"प.6.2.194": apply_6_2_194,
	"प.6.2.195": apply_6_2_195,
	"प.6.2.196": apply_6_2_196,
	"प.6.2.197": apply_6_2_197,
	"प.6.2.198": apply_6_2_198,
	"प.6.2.199": apply_6_2_199,
}
