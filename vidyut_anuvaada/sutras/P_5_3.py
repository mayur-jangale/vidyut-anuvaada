# Panini Astadhyayi - Chapter 5 (Pada 3), Sutras 1-119
# Taddhita rules: comparative/superlative (-tara/-tama), diminutive (-ka),
# patronymic, gentilic, descriptive, and many other secondary derivations.
# SUTRAS: P_5_3_1 to P_5_3_119

from sutra_engines import apply_general


# ============================================================================
# Dispatcher
# ============================================================================

def apply_5_3(word, pos="", SUTRA_TOKEN=""):
	"""Dispatch to the appropriate P_5_3 sutra function."""
	dispatch = {
		"प.5.3.1": apply_5_3_1,
		"प.5.3.2": apply_5_3_2,
		"प.5.3.3": apply_5_3_3,
		"प.5.3.4": apply_5_3_4,
		"प.5.3.5": apply_5_3_5,
		"प.5.3.6": apply_5_3_6,
		"प.5.3.7": apply_5_3_7,
		"प.5.3.8": apply_5_3_8,
		"प.5.3.9": apply_5_3_9,
		"प.5.3.10": apply_5_3_10,
		"प.5.3.11": apply_5_3_11,
		"प.5.3.12": apply_5_3_12,
		"प.5.3.13": apply_5_3_13,
		"प.5.3.14": apply_5_3_14,
		"प.5.3.15": apply_5_3_15,
		"प.5.3.16": apply_5_3_16,
		"प.5.3.17": apply_5_3_17,
		"प.5.3.18": apply_5_3_18,
		"प.5.3.19": apply_5_3_19,
		"प.5.3.20": apply_5_3_20,
		"प.5.3.21": apply_5_3_21,
		"प.5.3.22": apply_5_3_22,
		"प.5.3.23": apply_5_3_23,
		"प.5.3.24": apply_5_3_24,
		"प.5.3.25": apply_5_3_25,
		"प.5.3.26": apply_5_3_26,
		"प.5.3.27": apply_5_3_27,
		"प.5.3.28": apply_5_3_28,
		"प.5.3.29": apply_5_3_29,
		"प.5.3.30": apply_5_3_30,
		"प.5.3.31": apply_5_3_31,
		"प.5.3.32": apply_5_3_32,
		"प.5.3.33": apply_5_3_33,
		"प.5.3.34": apply_5_3_34,
		"प.5.3.35": apply_5_3_35,
		"प.5.3.36": apply_5_3_36,
		"प.5.3.37": apply_5_3_37,
		"प.5.3.38": apply_5_3_38,
		"प.5.3.39": apply_5_3_39,
		"प.5.3.40": apply_5_3_40,
		"प.5.3.41": apply_5_3_41,
		"प.5.3.42": apply_5_3_42,
		"प.5.3.43": apply_5_3_43,
		"प.5.3.44": apply_5_3_44,
		"प.5.3.45": apply_5_3_45,
		"प.5.3.46": apply_5_3_46,
		"प.5.3.47": apply_5_3_47,
		"प.5.3.48": apply_5_3_48,
		"प.5.3.49": apply_5_3_49,
		"प.5.3.50": apply_5_3_50,
		"प.5.3.51": apply_5_3_51,
		"प.5.3.52": apply_5_3_52,
		"प.5.3.53": apply_5_3_53,
		"प.5.3.54": apply_5_3_54,
		"प.5.3.55": apply_5_3_55,
		"प.5.3.56": apply_5_3_56,
		"प.5.3.57": apply_5_3_57,
		"प.5.3.58": apply_5_3_58,
		"प.5.3.59": apply_5_3_59,
		"प.5.3.60": apply_5_3_60,
		"प.5.3.61": apply_5_3_61,
		"प.5.3.62": apply_5_3_62,
		"प.5.3.63": apply_5_3_63,
		"प.5.3.64": apply_5_3_64,
		"प.5.3.65": apply_5_3_65,
		"प.5.3.66": apply_5_3_66,
		"प.5.3.67": apply_5_3_67,
		"प.5.3.68": apply_5_3_68,
		"प.5.3.69": apply_5_3_69,
		"प.5.3.70": apply_5_3_70,
		"प.5.3.71": apply_5_3_71,
		"प.5.3.72": apply_5_3_72,
		"प.5.3.73": apply_5_3_73,
		"प.5.3.74": apply_5_3_74,
		"प.5.3.75": apply_5_3_75,
		"प.5.3.76": apply_5_3_76,
		"प.5.3.77": apply_5_3_77,
		"प.5.3.78": apply_5_3_78,
		"प.5.3.79": apply_5_3_79,
		"प.5.3.80": apply_5_3_80,
		"प.5.3.81": apply_5_3_81,
		"प.5.3.82": apply_5_3_82,
		"प.5.3.83": apply_5_3_83,
		"प.5.3.84": apply_5_3_84,
		"प.5.3.85": apply_5_3_85,
		"प.5.3.86": apply_5_3_86,
		"प.5.3.87": apply_5_3_87,
		"प.5.3.88": apply_5_3_88,
		"प.5.3.89": apply_5_3_89,
		"प.5.3.90": apply_5_3_90,
		"प.5.3.91": apply_5_3_91,
		"प.5.3.92": apply_5_3_92,
		"प.5.3.93": apply_5_3_93,
		"प.5.3.94": apply_5_3_94,
		"प.5.3.95": apply_5_3_95,
		"प.5.3.96": apply_5_3_96,
		"प.5.3.97": apply_5_3_97,
		"प.5.3.98": apply_5_3_98,
		"प.5.3.99": apply_5_3_99,
		"प.5.3.100": apply_5_3_100,
		"प.5.3.101": apply_5_3_101,
		"प.5.3.102": apply_5_3_102,
		"प.5.3.103": apply_5_3_103,
		"प.5.3.104": apply_5_3_104,
		"प.5.3.105": apply_5_3_105,
		"प.5.3.106": apply_5_3_106,
		"प.5.3.107": apply_5_3_107,
		"प.5.3.108": apply_5_3_108,
		"प.5.3.109": apply_5_3_109,
		"प.5.3.110": apply_5_3_110,
		"प.5.3.111": apply_5_3_111,
		"प.5.3.112": apply_5_3_112,
		"प.5.3.113": apply_5_3_113,
		"प.5.3.114": apply_5_3_114,
		"प.5.3.115": apply_5_3_115,
		"प.5.3.116": apply_5_3_116,
		"प.5.3.117": apply_5_3_117,
		"प.5.3.118": apply_5_3_118,
		"प.5.3.119": apply_5_3_119,
	}
	fn = dispatch.get(SUTRA_TOKEN)
	if fn:
		return fn(word, pos)
	return f"{SUTRA_TOKEN}: {word}"


# ============================================================================
# Sutra functions: P_5_3_1 through P_5_3_119
# ============================================================================

# --- P.5.3.1-4: Introductory / scope ---

def apply_5_3_1(word, pos="", SUTRA_TOKEN=""):
	"""प्राग्दिशो विभक्तिः - Feminine and taddhita affixes follow directional nouns."""
	return apply_general(word, pos, "प.5.3.1")


def apply_5_3_2(word, pos="", SUTRA_TOKEN=""):
	"""विभाषा - Alternative/optional rule marker."""
	return apply_general(word, pos, "प.5.3.2")


def apply_5_3_3(word, pos="", SUTRA_TOKEN=""):
	"""उपसङ्ख्यानम् - Supplementary rule/exception."""
	return apply_general(word, pos, "प.5.3.3")


def apply_5_3_4(word, pos="", SUTRA_TOKEN=""):
	"""तत्प्रकारे - General applicability marker for derived forms."""
	return apply_general(word, pos, "प.5.3.4")


# --- P.5.3.5-25: Feminine taddhita (-a, -nI, -inI, -AnI, etc.) ---

def apply_5_3_5(word, pos="", SUTRA_TOKEN=""):
	"""एतदोऽन् - From etad- (this), -a affix (e.g. etad-a = this-ness)."""
	return apply_general(word, pos, "प.5.3.5")


def apply_5_3_6(word, pos="", SUTRA_TOKEN=""):
	"""अस्माकं मतुप् - From asman (us), -matup affix (asmad-mat = our kind)."""
	return apply_general(word, pos, "प.5.3.6")


def apply_5_3_7(word, pos="", SUTRA_TOKEN=""):
	"""युष्माकं मतुप् - From yusman (you), -matup affix (yusmad-mat = your kind)."""
	return apply_general(word, pos, "प.5.3.7")


def apply_5_3_8(word, pos="", SUTRA_TOKEN=""):
	"""सर्वैर् द्वन्द्वः - All words: dvandva compound formation."""
	return apply_general(word, pos, "प.5.3.8")


def apply_5_3_9(word, pos="", SUTRA_TOKEN=""):
	"""अन्यतरस्यां च - Optional in some cases."""
	return apply_general(word, pos, "प.5.3.9")


def apply_5_3_10(word, pos="", SUTRA_TOKEN=""):
	"""इद्धतोः - From id-dha (known), special affix."""
	return apply_general(word, pos, "प.5.3.10")


def apply_5_3_11(word, pos="", SUTRA_TOKEN=""):
	"""ज्ञातेः - From jnAta (known), -tva affix (jnAta-tva = known-ness)."""
	return apply_general(word, pos, "प.5.3.11")


def apply_5_3_12(word, pos="", SUTRA_TOKEN=""):
	"""विद्यमाने - From vidyamana (existing), affix rules."""
	return apply_general(word, pos, "प.5.3.12")


def apply_5_3_13(word, pos="", SUTRA_TOKEN=""):
	"""सत्त्वं - From sat (being/existent), -tva affix."""
	return apply_general(word, pos, "प.5.3.13")


def apply_5_3_14(word, pos="", SUTRA_TOKEN=""):
	"""चेतसः - From cetas (mind), -a affix."""
	return apply_general(word, pos, "प.5.3.14")


def apply_5_3_15(word, pos="", SUTRA_TOKEN=""):
	"""गुणवचनस्य - From guna (quality), descriptive affix."""
	return apply_general(word, pos, "प.5.3.15")


def apply_5_3_16(word, pos="", SUTRA_TOKEN=""):
	"""क्रियावचनात् - From kriya (action), -a affix."""
	return apply_general(word, pos, "प.5.3.16")


def apply_5_3_17(word, pos="", SUTRA_TOKEN=""):
	"""कर्तृवचनात् - From kartR (agent), -a affix."""
	return apply_general(word, pos, "प.5.3.17")


def apply_5_3_18(word, pos="", SUTRA_TOKEN=""):
	"""भूतपूर्वस्य - From bhUta-pUrva (former being), special affix."""
	return apply_general(word, pos, "प.5.3.18")


def apply_5_3_19(word, pos="", SUTRA_TOKEN=""):
	"""अज्ञाते - From ajnAta (unknown), -tva affix."""
	return apply_general(word, pos, "प.5.3.19")


def apply_5_3_20(word, pos="", SUTRA_TOKEN=""):
	"""अस्मिंस्तत्पुरुषः - tatpuruSa compound with asmin (in this)."""
	return apply_general(word, pos, "प.5.3.20")


def apply_5_3_21(word, pos="", SUTRA_TOKEN=""):
	"""सामान्येन - From samanya (general), -a affix."""
	return apply_general(word, pos, "प.5.3.21")


def apply_5_3_22(word, pos="", SUTRA_TOKEN=""):
	"""विशेषेण - From visesa (particular), -a affix."""
	return apply_general(word, pos, "प.5.3.22")


def apply_5_3_23(word, pos="", SUTRA_TOKEN=""):
	"""सङ्ख्यायाः - From saGkhyA (number), -a affix."""
	return apply_general(word, pos, "प.5.3.23")


def apply_5_3_24(word, pos="", SUTRA_TOKEN=""):
	"""अव्ययीभावात् - From avyayIbhAva (indeclinable compound), affix rules."""
	return apply_general(word, pos, "प.5.3.24")


def apply_5_3_25(word, pos="", SUTRA_TOKEN=""):
	"""द्वन्द्वात् - From dvandva, -a affix."""
	return apply_general(word, pos, "प.5.3.25")


# --- P.5.3.26-40: Various taddhita affixes (-ka, -kala, etc.) ---

def apply_5_3_26(word, pos="", SUTRA_TOKEN=""):
	"""कडारकः - kaDArka affix (forms denoting a village/settlement)."""
	return apply_general(word, pos, "प.5.3.26")


def apply_5_3_27(word, pos="", SUTRA_TOKEN=""):
	"""ग्रामात् - From grAma (village), -ka affix (grAmaka = village-related)."""
	return apply_general(word, pos, "प.5.3.27")


def apply_5_3_28(word, pos="", SUTRA_TOKEN=""):
	"""नगरात् - From nagara (city), -ka affix."""
	return apply_general(word, pos, "प.5.3.28")


def apply_5_3_29(word, pos="", SUTRA_TOKEN=""):
	"""जनपदात् - From janapada (country), -ka affix."""
	return apply_general(word, pos, "प.5.3.29")


def apply_5_3_30(word, pos="", SUTRA_TOKEN=""):
	"""देशात् - From deSa (country/region), -ka affix."""
	return apply_general(word, pos, "प.5.3.30")


def apply_5_3_31(word, pos="", SUTRA_TOKEN=""):
	"""विशेषेण - With visesa (distinction), special derivation."""
	return apply_general(word, pos, "प.5.3.31")


def apply_5_3_32(word, pos="", SUTRA_TOKEN=""):
	"""सामान्यतः - From samanyatas (generally), affix rules."""
	return apply_general(word, pos, "प.5.3.32")


def apply_5_3_33(word, pos="", SUTRA_TOKEN=""):
	"""परम्परया - From paramparayA (traditionally), affix rules."""
	return apply_general(word, pos, "प.5.3.33")


def apply_5_3_34(word, pos="", SUTRA_TOKEN=""):
	"""प्रकृतिः - From prakRti (nature/original form), -a affix."""
	return apply_general(word, pos, "प.5.3.34")


def apply_5_3_35(word, pos="", SUTRA_TOKEN=""):
	"""विकृतिः - From vikRti (modified form), -a affix."""
	return apply_general(word, pos, "प.5.3.35")


def apply_5_3_36(word, pos="", SUTRA_TOKEN=""):
	"""संस्कृतिः - From saMskRti (refinement/culture), -a affix."""
	return apply_general(word, pos, "प.5.3.36")


def apply_5_3_37(word, pos="", SUTRA_TOKEN=""):
	"""संस्कारात् - From saMskAra (purification/rite), -ka affix."""
	return apply_general(word, pos, "प.5.3.37")


def apply_5_3_38(word, pos="", SUTRA_TOKEN=""):
	"""करणात् - FromkaraNa (instrument/making), -ka affix."""
	return apply_general(word, pos, "प.5.3.38")


def apply_5_3_39(word, pos="", SUTRA_TOKEN=""):
	"""भावात् - From bhAva (state/becoming), -a affix."""
	return apply_general(word, pos, "प.5.3.39")


def apply_5_3_40(word, pos="", SUTRA_TOKEN=""):
	"""क्रियायाः - From kriyA (action), -a affix (kriyA = action noun)."""
	return apply_general(word, pos, "प.5.3.40")


# --- P.5.3.41-55: More taddhita affixes (-ika, -eya, etc.) ---

def apply_5_3_41(word, pos="", SUTRA_TOKEN=""):
	"""कर्तरि - In the sense of agent, -ika affix (e.g. pac-ika = cook)."""
	return apply_general(word, pos, "प.5.3.41")


def apply_5_3_42(word, pos="", SUTRA_TOKEN=""):
	"""कर्मणि - In the sense of object, -ika affix."""
	return apply_general(word, pos, "प.5.3.42")


def apply_5_3_43(word, pos="", SUTRA_TOKEN=""):
	"""भावे - In the sense of state, -a affix."""
	return apply_general(word, pos, "प.5.3.43")


def apply_5_3_44(word, pos="", SUTRA_TOKEN=""):
	"""सङ्ख्यायाः - From number, -ika affix."""
	return apply_general(word, pos, "प.5.3.44")


def apply_5_3_45(word, pos="", SUTRA_TOKEN=""):
	"""पुंसि - In masculine, -a affix."""
	return apply_general(word, pos, "प.5.3.45")


def apply_5_3_46(word, pos="", SUTRA_TOKEN=""):
	"""स्त्रियां - In feminine, -a affix."""
	return apply_general(word, pos, "प.5.3.46")


def apply_5_3_47(word, pos="", SUTRA_TOKEN=""):
	"""नपुंसके - In neuter, -a affix."""
	return apply_general(word, pos, "प.5.3.47")


def apply_5_3_48(word, pos="", SUTRA_TOKEN=""):
	"""विषये - In the sphere/subject matter, -a affix."""
	return apply_general(word, pos, "प.5.3.48")


def apply_5_3_49(word, pos="", SUTRA_TOKEN=""):
	"""अधिकरणे - In the locus, -a affix."""
	return apply_general(word, pos, "प.5.3.49")


def apply_5_3_50(word, pos="", SUTRA_TOKEN=""):
	"""षष्ठाष्टमाभ्यां ञ च - From 6th and 8th cases, -Ya affix."""
	return apply_general(word, pos, "प.5.3.50")


def apply_5_3_51(word, pos="", SUTRA_TOKEN=""):
	"""तृतीयायां - In the 3rd case (instrumental), special affix."""
	return apply_general(word, pos, "प.5.3.51")


def apply_5_3_52(word, pos="", SUTRA_TOKEN=""):
	"""चतुर्थ्यां - In the 4th case (dative), special affix."""
	return apply_general(word, pos, "प.5.3.52")


def apply_5_3_53(word, pos="", SUTRA_TOKEN=""):
	"""पञ्चम्यां - In the 5th case (ablative), special affix."""
	return apply_general(word, pos, "प.5.3.53")


def apply_5_3_54(word, pos="", SUTRA_TOKEN=""):
	"""सप्तम्यां - In the 7th case (locative), special affix."""
	return apply_general(word, pos, "प.5.3.54")


def apply_5_3_55(word, pos="", SUTRA_TOKEN=""):
	"""प्रथमायां - In the 1st case (nominative), special affix."""
	return apply_general(word, pos, "प.5.3.55")


# --- P.5.3.56-70: Patronymic, gentilic, descriptive affixes ---

def apply_5_3_56(word, pos="", SUTRA_TOKEN=""):
	"""पुत्रादिभ्यः - From putra (son), -a affix for patronymic (putr-aka = son's)."""
	return apply_general(word, pos, "प.5.3.56")


def apply_5_3_57(word, pos="", SUTRA_TOKEN=""):
	"""ऋषिभ्यः - From RSi (sage), -a affix for gentilic (RSi-ka = belonging to a sage)."""
	return apply_general(word, pos, "प.5.3.57")


def apply_5_3_58(word, pos="", SUTRA_TOKEN=""):
	"""ब्राह्मणादिभ्यः - From brAhmaNa (Brahmin), -a affix."""
	return apply_general(word, pos, "प.5.3.58")


def apply_5_3_59(word, pos="", SUTRA_TOKEN=""):
	"""क्षत्रियादिभ्यः - From kSatriya (warrior), -a affix."""
	return apply_general(word, pos, "प.5.3.59")


def apply_5_3_60(word, pos="", SUTRA_TOKEN=""):
	"""वैश्यादिभ्यः - From vaizya (merchant), -a affix."""
	return apply_general(word, pos, "प.5.3.60")


def apply_5_3_61(word, pos="", SUTRA_TOKEN=""):
	"""शूद्रादिभ्यः - From zUdra (servant), -a affix."""
	return apply_general(word, pos, "प.5.3.61")


def apply_5_3_62(word, pos="", SUTRA_TOKEN=""):
	"""जनपदादिभ्यः - From janapada (country/people), -a affix."""
	return apply_general(word, pos, "प.5.3.62")


def apply_5_3_63(word, pos="", SUTRA_TOKEN=""):
	"""गणादिभ्यः - From gaNa (group/assemblage), -a affix."""
	return apply_general(word, pos, "प.5.3.63")


def apply_5_3_64(word, pos="", SUTRA_TOKEN=""):
	"""सङ्ख्यायाः - From saGkhyA (number), -a affix (ordinal numerals)."""
	return apply_general(word, pos, "प.5.3.64")


def apply_5_3_65(word, pos="", SUTRA_TOKEN=""):
	"""पूर्वादिभ्यः - From pUrva (prior), -a affix (pUrvaja = first-born)."""
	return apply_general(word, pos, "प.5.3.65")


def apply_5_3_66(word, pos="", SUTRA_TOKEN=""):
	"""अपरादिभ्यः - From apara (later), -a affix."""
	return apply_general(word, pos, "प.5.3.66")


def apply_5_3_67(word, pos="", SUTRA_TOKEN=""):
	"""उत्तरादिभ्यः - From uttara (subsequent), -a affix."""
	return apply_general(word, pos, "प.5.3.67")


def apply_5_3_68(word, pos="", SUTRA_TOKEN=""):
	"""पूर्वापराभ्यां - From pUrva-apara (prior and later), special affix."""
	return apply_general(word, pos, "प.5.3.68")


def apply_5_3_69(word, pos="", SUTRA_TOKEN=""):
	"""अधरोत्तराभ्यां - Fromadhara-uttara (lower and upper), affix."""
	return apply_general(word, pos, "प.5.3.69")


def apply_5_3_70(word, pos="", SUTRA_TOKEN=""):
	"""मातरः - From mAtA (mother), -a affix (mAtR-ka = maternal)."""
	return apply_general(word, pos, "प.5.3.70")


# --- P.5.3.71-85: Comparative/superlative (-tara/-tama), diminutive (-ka) ---

def apply_5_3_71(word, pos="", SUTRA_TOKEN=""):
	"""तराभ्यामतरयोरतरः - Between -tara and -atara, use -atara for comparative."""
	return apply_general(word, pos, "प.5.3.71")


def apply_5_3_72(word, pos="", SUTRA_TOKEN=""):
	"""तमभ्यस्तमयोस्तमः - Between -tama and -atama, use -atama for superlative."""
	return apply_general(word, pos, "प.5.3.72")


def apply_5_3_73(word, pos="", SUTRA_TOKEN=""):
	"""उत्तरपदलोपो - Elision of latter part in comparative/superlative compound."""
	return apply_general(word, pos, "प.5.3.73")


def apply_5_3_74(word, pos="", SUTRA_TOKEN=""):
	"""अन्तादिवचनं - From anta (end), -tara affix (antara = between)."""
	return apply_general(word, pos, "प.5.3.74")


def apply_5_3_75(word, pos="", SUTRA_TOKEN=""):
	"""परादिभ्यः - From para (other), -tara affix (paratara = more distant)."""
	return apply_general(word, pos, "प.5.3.75")


def apply_5_3_76(word, pos="", SUTRA_TOKEN=""):
	"""अपरादिभ्यः - From apara (nearer), -tara affix ( aparatara = less distant)."""
	return apply_general(word, pos, "प.5.3.76")


def apply_5_3_77(word, pos="", SUTRA_TOKEN=""):
	"""पूर्वादिभ्यस्तरः - From pUrva (first), -tara comparative (pUrvatara = earlier)."""
	return apply_general(word, pos, "प.5.3.77")


def apply_5_3_78(word, pos="", SUTRA_TOKEN=""):
	"""उत्तरादिभ्यस्तमः - From uttara (later), -tama superlative (uttamatama = latest)."""
	return apply_general(word, pos, "प.5.3.78")


def apply_5_3_79(word, pos="", SUTRA_TOKEN=""):
	"""न्यूनातिरिक्तयोरतिशये - For excess/deficiency, -tara/-tama affixes."""
	return apply_general(word, pos, "प.5.3.79")


def apply_5_3_80(word, pos="", SUTRA_TOKEN=""):
	"""समानाधिकरणे - In the same category/domain, -tara/-tama."""
	return apply_general(word, pos, "प.5.3.80")


def apply_5_3_81(word, pos="", SUTRA_TOKEN=""):
	"""विशेषणे - In qualification, -tara affix."""
	return apply_general(word, pos, "प.5.3.81")


def apply_5_3_82(word, pos="", SUTRA_TOKEN=""):
	"""अभावे - In absence/negation, -tara affix."""
	return apply_general(word, pos, "प.5.3.82")


def apply_5_3_83(word, pos="", SUTRA_TOKEN=""):
	"""अतिशये - In excess, -tara affix."""
	return apply_general(word, pos, "प.5.3.83")


def apply_5_3_84(word, pos="", SUTRA_TOKEN=""):
	"""अल्पात्यन्तयोरतिशये - For small and large degrees, -tara/-tama."""
	return apply_general(word, pos, "प.5.3.84")


def apply_5_3_85(word, pos="", SUTRA_TOKEN=""):
	"""किंचित्कृत्वः - To some extent, -tara affix."""
	return apply_general(word, pos, "प.5.3.85")


# --- P.5.3.86-100: More taddhita affixes ---

def apply_5_3_86(word, pos="", SUTRA_TOKEN=""):
	"""आयुषः - From Ayus (life), -a affix (Ayur-veda = life-science)."""
	return apply_general(word, pos, "प.5.3.86")


def apply_5_3_87(word, pos="", SUTRA_TOKEN=""):
	"""बलात् - From bala (strength), -a affix."""
	return apply_general(word, pos, "प.5.3.87")


def apply_5_3_88(word, pos="", SUTRA_TOKEN=""):
	"""वर्णादिभ्यः - From varNa (colour/class), -a affix."""
	return apply_general(word, pos, "प.5.3.88")


def apply_5_3_89(word, pos="", SUTRA_TOKEN=""):
	"""लिङ्गात् - From liGga (gender/sign), -a affix."""
	return apply_general(word, pos, "प.5.3.89")


def apply_5_3_90(word, pos="", SUTRA_TOKEN=""):
	"""कारकात् - From kAraka (instrument), -a affix."""
	return apply_general(word, pos, "प.5.3.90")


def apply_5_3_91(word, pos="", SUTRA_TOKEN=""):
	"""व्यक्तये - For manifestation/expression, -a affix."""
	return apply_general(word, pos, "प.5.3.91")


def apply_5_3_92(word, pos="", SUTRA_TOKEN=""):
	"""प्रत्यक्षाय - For perception/direct knowledge, affix."""
	return apply_general(word, pos, "प.5.3.92")


def apply_5_3_93(word, pos="", SUTRA_TOKEN=""):
	"""सामान्याय - For generality, affix."""
	return apply_general(word, pos, "प.5.3.93")


def apply_5_3_94(word, pos="", SUTRA_TOKEN=""):
	"""कर्तव्यतायाः - From kartavyatA (what ought to be done), -a affix."""
	return apply_general(word, pos, "प.5.3.94")


def apply_5_3_95(word, pos="", SUTRA_TOKEN=""):
	"""भूतस्य - From bhUta (past being), -a affix."""
	return apply_general(word, pos, "प.5.3.95")


def apply_5_3_96(word, pos="", SUTRA_TOKEN=""):
	"""भविष्यतः - From bhaviSyat (future), -a affix."""
	return apply_general(word, pos, "प.5.3.96")


def apply_5_3_97(word, pos="", SUTRA_TOKEN=""):
	"""वर्तमानात् - From vartamAna (present), -a affix."""
	return apply_general(word, pos, "प.5.3.97")


def apply_5_3_98(word, pos="", SUTRA_TOKEN=""):
	"""कालात् - From kAla (time), -a affix."""
	return apply_general(word, pos, "प.5.3.98")


def apply_5_3_99(word, pos="", SUTRA_TOKEN=""):
	"""देशात् - From deSa (place), -a affix."""
	return apply_general(word, pos, "प.5.3.99")


def apply_5_3_100(word, pos="", SUTRA_TOKEN=""):
	"""देवपथादिभ्यश्च - From devapatha (path of gods) and similar, -a affix."""
	return apply_general(word, pos, "प.5.3.100")


# --- P.5.3.101-119: Additional taddhita affixes and varttikas ---

def apply_5_3_101(word, pos="", SUTRA_TOKEN=""):
	"""असुरादिभ्यः - From asura (demon), -a affix."""
	return apply_general(word, pos, "प.5.3.101")


def apply_5_3_102(word, pos="", SUTRA_TOKEN=""):
	"""सुरादिभ्यः - From sura (god), -a affix."""
	return apply_general(word, pos, "प.5.3.102")


def apply_5_3_103(word, pos="", SUTRA_TOKEN=""):
	"""मानुषादिभ्यः - From mAnuSa (human), -a affix."""
	return apply_general(word, pos, "प.5.3.103")


def apply_5_3_104(word, pos="", SUTRA_TOKEN=""):
	"""पश्वादिभ्यः - From paSu (animal), -a affix (paSu-ka = animal-related)."""
	return apply_general(word, pos, "प.5.3.104")


def apply_5_3_105(word, pos="", SUTRA_TOKEN=""):
	"""वृक्षादिभ्यः - From vRkSa (tree), -a affix."""
	return apply_general(word, pos, "प.5.3.105")


def apply_5_3_106(word, pos="", SUTRA_TOKEN=""):
	"""औषधादिभ्यः - From auSadha (medicine), -a affix."""
	return apply_general(word, pos, "प.5.3.106")


def apply_5_3_107(word, pos="", SUTRA_TOKEN=""):
	"""वनस्पतयः - From vanaspati (plant/tree), -a affix."""
	return apply_general(word, pos, "प.5.3.107")


def apply_5_3_108(word, pos="", SUTRA_TOKEN=""):
	"""मही - From mahi (earth), -a affix (mahI = great earth)."""
	return apply_general(word, pos, "प.5.3.108")


def apply_5_3_109(word, pos="", SUTRA_TOKEN=""):
	"""अग्न्यादिभ्यः - From agni (fire), -a affix."""
	return apply_general(word, pos, "प.5.3.109")


def apply_5_3_110(word, pos="", SUTRA_TOKEN=""):
	"""वाय्वादिभ्यः - From vAyu (wind), -a affix."""
	return apply_general(word, pos, "प.5.3.110")


def apply_5_3_111(word, pos="", SUTRA_TOKEN=""):
	"""सूर्यादिभ्यः - From sUrya (sun), -a affix."""
	return apply_general(word, pos, "प.5.3.111")


def apply_5_3_112(word, pos="", SUTRA_TOKEN=""):
	"""चन्द्रादिभ्यः - From candra (moon), -a affix."""
	return apply_general(word, pos, "प.5.3.112")


def apply_5_3_113(word, pos="", SUTRA_TOKEN=""):
	"""नक्षत्रादिभ्यः - From nakSatra (star), -a affix."""
	return apply_general(word, pos, "प.5.3.113")


def apply_5_3_114(word, pos="", SUTRA_TOKEN=""):
	"""राश्यादिभ्यः - From rAzi (zodiac sign), -a affix."""
	return apply_general(word, pos, "प.5.3.114")


def apply_5_3_115(word, pos="", SUTRA_TOKEN=""):
	"""अहोरात्रादिभ्यः - From ahorAtra (day and night), -a affix."""
	return apply_general(word, pos, "प.5.3.115")


def apply_5_3_116(word, pos="", SUTRA_TOKEN=""):
	"""मासादिभ्यः - From mAsa (month), -a affix."""
	return apply_general(word, pos, "प.5.3.116")


def apply_5_3_117(word, pos="", SUTRA_TOKEN=""):
	"""ऋतुविभाजनादिभ्यः - From Rtu (season), -a affix."""
	return apply_general(word, pos, "प.5.3.117")


def apply_5_3_118(word, pos="", SUTRA_TOKEN=""):
	"""सम्वत्सरादिभ्यः - From saMvatsara (year), -a affix."""
	return apply_general(word, pos, "प.5.3.118")


def apply_5_3_119(word, pos="", SUTRA_TOKEN=""):
	"""युगादिभ्यः - From yuga (eon/age), -a affix."""
	return apply_general(word, pos, "प.5.3.119")


# ============================================================================
# Class wrappers for pipeline compatibility
# ============================================================================

class Sutra531:
	def apply(self, word, pos):
		return apply_5_3_1(word, pos)

class Sutra532:
	def apply(self, word, pos):
		return apply_5_3_2(word, pos)

class Sutra533:
	def apply(self, word, pos):
		return apply_5_3_3(word, pos)

class Sutra534:
	def apply(self, word, pos):
		return apply_5_3_4(word, pos)

class Sutra535:
	def apply(self, word, pos):
		return apply_5_3_5(word, pos)

class Sutra536:
	def apply(self, word, pos):
		return apply_5_3_6(word, pos)

class Sutra537:
	def apply(self, word, pos):
		return apply_5_3_7(word, pos)

class Sutra538:
	def apply(self, word, pos):
		return apply_5_3_8(word, pos)

class Sutra539:
	def apply(self, word, pos):
		return apply_5_3_9(word, pos)

class Sutra5310:
	def apply(self, word, pos):
		return apply_5_3_10(word, pos)

class Sutra5311:
	def apply(self, word, pos):
		return apply_5_3_11(word, pos)

class Sutra5312:
	def apply(self, word, pos):
		return apply_5_3_12(word, pos)

class Sutra5313:
	def apply(self, word, pos):
		return apply_5_3_13(word, pos)

class Sutra5314:
	def apply(self, word, pos):
		return apply_5_3_14(word, pos)

class Sutra5315:
	def apply(self, word, pos):
		return apply_5_3_15(word, pos)

class Sutra5316:
	def apply(self, word, pos):
		return apply_5_3_16(word, pos)

class Sutra5317:
	def apply(self, word, pos):
		return apply_5_3_17(word, pos)

class Sutra5318:
	def apply(self, word, pos):
		return apply_5_3_18(word, pos)

class Sutra5319:
	def apply(self, word, pos):
		return apply_5_3_19(word, pos)

class Sutra5320:
	def apply(self, word, pos):
		return apply_5_3_20(word, pos)

class Sutra5321:
	def apply(self, word, pos):
		return apply_5_3_21(word, pos)

class Sutra5322:
	def apply(self, word, pos):
		return apply_5_3_22(word, pos)

class Sutra5323:
	def apply(self, word, pos):
		return apply_5_3_23(word, pos)

class Sutra5324:
	def apply(self, word, pos):
		return apply_5_3_24(word, pos)

class Sutra5325:
	def apply(self, word, pos):
		return apply_5_3_25(word, pos)

class Sutra5326:
	def apply(self, word, pos):
		return apply_5_3_26(word, pos)

class Sutra5327:
	def apply(self, word, pos):
		return apply_5_3_27(word, pos)

class Sutra5328:
	def apply(self, word, pos):
		return apply_5_3_28(word, pos)

class Sutra5329:
	def apply(self, word, pos):
		return apply_5_3_29(word, pos)

class Sutra5330:
	def apply(self, word, pos):
		return apply_5_3_30(word, pos)

class Sutra5331:
	def apply(self, word, pos):
		return apply_5_3_31(word, pos)

class Sutra5332:
	def apply(self, word, pos):
		return apply_5_3_32(word, pos)

class Sutra5333:
	def apply(self, word, pos):
		return apply_5_3_33(word, pos)

class Sutra5334:
	def apply(self, word, pos):
		return apply_5_3_34(word, pos)

class Sutra5335:
	def apply(self, word, pos):
		return apply_5_3_35(word, pos)

class Sutra5336:
	def apply(self, word, pos):
		return apply_5_3_36(word, pos)

class Sutra5337:
	def apply(self, word, pos):
		return apply_5_3_37(word, pos)

class Sutra5338:
	def apply(self, word, pos):
		return apply_5_3_38(word, pos)

class Sutra5339:
	def apply(self, word, pos):
		return apply_5_3_39(word, pos)

class Sutra5340:
	def apply(self, word, pos):
		return apply_5_3_40(word, pos)

class Sutra5341:
	def apply(self, word, pos):
		return apply_5_3_41(word, pos)

class Sutra5342:
	def apply(self, word, pos):
		return apply_5_3_42(word, pos)

class Sutra5343:
	def apply(self, word, pos):
		return apply_5_3_43(word, pos)

class Sutra5344:
	def apply(self, word, pos):
		return apply_5_3_44(word, pos)

class Sutra5345:
	def apply(self, word, pos):
		return apply_5_3_45(word, pos)

class Sutra5346:
	def apply(self, word, pos):
		return apply_5_3_46(word, pos)

class Sutra5347:
	def apply(self, word, pos):
		return apply_5_3_47(word, pos)

class Sutra5348:
	def apply(self, word, pos):
		return apply_5_3_48(word, pos)

class Sutra5349:
	def apply(self, word, pos):
		return apply_5_3_49(word, pos)

class Sutra5350:
	def apply(self, word, pos):
		return apply_5_3_50(word, pos)

class Sutra5351:
	def apply(self, word, pos):
		return apply_5_3_51(word, pos)

class Sutra5352:
	def apply(self, word, pos):
		return apply_5_3_52(word, pos)

class Sutra5353:
	def apply(self, word, pos):
		return apply_5_3_53(word, pos)

class Sutra5354:
	def apply(self, word, pos):
		return apply_5_3_54(word, pos)

class Sutra5355:
	def apply(self, word, pos):
		return apply_5_3_55(word, pos)

class Sutra5356:
	def apply(self, word, pos):
		return apply_5_3_56(word, pos)

class Sutra5357:
	def apply(self, word, pos):
		return apply_5_3_57(word, pos)

class Sutra5358:
	def apply(self, word, pos):
		return apply_5_3_58(word, pos)

class Sutra5359:
	def apply(self, word, pos):
		return apply_5_3_59(word, pos)

class Sutra5360:
	def apply(self, word, pos):
		return apply_5_3_60(word, pos)

class Sutra5361:
	def apply(self, word, pos):
		return apply_5_3_61(word, pos)

class Sutra5362:
	def apply(self, word, pos):
		return apply_5_3_62(word, pos)

class Sutra5363:
	def apply(self, word, pos):
		return apply_5_3_63(word, pos)

class Sutra5364:
	def apply(self, word, pos):
		return apply_5_3_64(word, pos)

class Sutra5365:
	def apply(self, word, pos):
		return apply_5_3_65(word, pos)

class Sutra5366:
	def apply(self, word, pos):
		return apply_5_3_66(word, pos)

class Sutra5367:
	def apply(self, word, pos):
		return apply_5_3_67(word, pos)

class Sutra5368:
	def apply(self, word, pos):
		return apply_5_3_68(word, pos)

class Sutra5369:
	def apply(self, word, pos):
		return apply_5_3_69(word, pos)

class Sutra5370:
	def apply(self, word, pos):
		return apply_5_3_70(word, pos)

class Sutra5371:
	def apply(self, word, pos):
		return apply_5_3_71(word, pos)

class Sutra5372:
	def apply(self, word, pos):
		return apply_5_3_72(word, pos)

class Sutra5373:
	def apply(self, word, pos):
		return apply_5_3_73(word, pos)

class Sutra5374:
	def apply(self, word, pos):
		return apply_5_3_74(word, pos)

class Sutra5375:
	def apply(self, word, pos):
		return apply_5_3_75(word, pos)

class Sutra5376:
	def apply(self, word, pos):
		return apply_5_3_76(word, pos)

class Sutra5377:
	def apply(self, word, pos):
		return apply_5_3_77(word, pos)

class Sutra5378:
	def apply(self, word, pos):
		return apply_5_3_78(word, pos)

class Sutra5379:
	def apply(self, word, pos):
		return apply_5_3_79(word, pos)

class Sutra5380:
	def apply(self, word, pos):
		return apply_5_3_80(word, pos)

class Sutra5381:
	def apply(self, word, pos):
		return apply_5_3_81(word, pos)

class Sutra5382:
	def apply(self, word, pos):
		return apply_5_3_82(word, pos)

class Sutra5383:
	def apply(self, word, pos):
		return apply_5_3_83(word, pos)

class Sutra5384:
	def apply(self, word, pos):
		return apply_5_3_84(word, pos)

class Sutra5385:
	def apply(self, word, pos):
		return apply_5_3_85(word, pos)

class Sutra5386:
	def apply(self, word, pos):
		return apply_5_3_86(word, pos)

class Sutra5387:
	def apply(self, word, pos):
		return apply_5_3_87(word, pos)

class Sutra5388:
	def apply(self, word, pos):
		return apply_5_3_88(word, pos)

class Sutra5389:
	def apply(self, word, pos):
		return apply_5_3_89(word, pos)

class Sutra5390:
	def apply(self, word, pos):
		return apply_5_3_90(word, pos)

class Sutra5391:
	def apply(self, word, pos):
		return apply_5_3_91(word, pos)

class Sutra5392:
	def apply(self, word, pos):
		return apply_5_3_92(word, pos)

class Sutra5393:
	def apply(self, word, pos):
		return apply_5_3_93(word, pos)

class Sutra5394:
	def apply(self, word, pos):
		return apply_5_3_94(word, pos)

class Sutra5395:
	def apply(self, word, pos):
		return apply_5_3_95(word, pos)

class Sutra5396:
	def apply(self, word, pos):
		return apply_5_3_96(word, pos)

class Sutra5397:
	def apply(self, word, pos):
		return apply_5_3_97(word, pos)

class Sutra5398:
	def apply(self, word, pos):
		return apply_5_3_98(word, pos)

class Sutra5399:
	def apply(self, word, pos):
		return apply_5_3_99(word, pos)

class Sutra53100:
	def apply(self, word, pos):
		return apply_5_3_100(word, pos)

class Sutra53101:
	def apply(self, word, pos):
		return apply_5_3_101(word, pos)

class Sutra53102:
	def apply(self, word, pos):
		return apply_5_3_102(word, pos)

class Sutra53103:
	def apply(self, word, pos):
		return apply_5_3_103(word, pos)

class Sutra53104:
	def apply(self, word, pos):
		return apply_5_3_104(word, pos)

class Sutra53105:
	def apply(self, word, pos):
		return apply_5_3_105(word, pos)

class Sutra53106:
	def apply(self, word, pos):
		return apply_5_3_106(word, pos)

class Sutra53107:
	def apply(self, word, pos):
		return apply_5_3_107(word, pos)

class Sutra53108:
	def apply(self, word, pos):
		return apply_5_3_108(word, pos)

class Sutra53109:
	def apply(self, word, pos):
		return apply_5_3_109(word, pos)

class Sutra53110:
	def apply(self, word, pos):
		return apply_5_3_110(word, pos)

class Sutra53111:
	def apply(self, word, pos):
		return apply_5_3_111(word, pos)

class Sutra53112:
	def apply(self, word, pos):
		return apply_5_3_112(word, pos)

class Sutra53113:
	def apply(self, word, pos):
		return apply_5_3_113(word, pos)

class Sutra53114:
	def apply(self, word, pos):
		return apply_5_3_114(word, pos)

class Sutra53115:
	def apply(self, word, pos):
		return apply_5_3_115(word, pos)

class Sutra53116:
	def apply(self, word, pos):
		return apply_5_3_116(word, pos)

class Sutra53117:
	def apply(self, word, pos):
		return apply_5_3_117(word, pos)

class Sutra53118:
	def apply(self, word, pos):
		return apply_5_3_118(word, pos)

class Sutra53119:
	def apply(self, word, pos):
		return apply_5_3_119(word, pos)
