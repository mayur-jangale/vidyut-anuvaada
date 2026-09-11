"""Shared logic for P.1.3.x sutras."""
from __future__ import annotations

BHVA_DI = {"भू","अस्","कम्","कृ","गम्","दा","धा","नी","पा","भ्रम्"}
IT_ROOTS = {"कृष्","लिख्","वच्","वप्","पुष्"}

def apply_1_3_1(word, pos=""):
	if word in BHVA_DI: return "bhU-adi-dhAtu:" + word + ";in-list=yes"
	return "bhU-adi-dhAtu:" + word + ";in-list=no"

def apply_1_3_2(word, pos=""):
	if word in IT_ROOTS: return "it-vowel:" + word + ";it=yes"
	return "it-vowel:" + word + ";it=no"

def apply_1_3_3(word, pos=""):
	if not word: return "hal-ityam:empty"
	final = word[-2:] if word[-1] == '्' else word[-1]
	return "hal-ityam:" + word + ";final=" + final

def apply_1_3_4(word, pos=""):
	TU_SMA = {"त","स","म"}
	if pos in TU_SMA and word: return "vibhakti-no-tusmah:" + word + ";flag=yes"
	return "vibhakti-no-tusmah:" + word + ";flag=no"

def apply_1_3_5(word, pos=""):
	IT_FIRST = {"ञ","ट","ड"}
	if word[0] in IT_FIRST: return "adir-nitidudavah:" + word + ";first=" + word[0] + ";it=yes"
	return "adir-nitidudavah:" + word + ";it=no"

def apply_1_3_6(word, pos=""):
	if word.endswith("ष्") or word.endswith("ष"): return "sah-pratyayasya:" + word + ";sa-it=yes"
	return "sah-pratyayasya:" + word + ";sa-it=no"

def apply_1_3_7(word, pos=""):
	CT = {"च्","ट्","त्"}
	if word[-1] == "्" and len(word) >= 2:
		if word[-2:] in CT: return "cutU:" + word + ";ending=" + word[-2:]
	elif word[-1] in {"च","ट","त"}: return "cutU:" + word + ";ending=" + word[-1]
	return "cutU:" + word + ";not-cutU"

def apply_1_3_8(word, pos=""):
	if word.endswith("ल्") or word.endswith("श्") or word.endswith("क्"): return "laShakvataDDhite:" + word + ";yes"
	return "laShakvataDDhite:" + word + ";no"

def apply_1_3_9(word, pos=""):
	if not word: return "tasya-lopah:empty"
	stripped = word
	if word[-1] == "्":
		# Remove last consonant+virama (the "tasya" referred to)
		if len(word) >= 2: stripped = word[:-2]
		else: stripped = word
	else:
		IT_set = {"इ","उ","ऋ","ऌ","ञ","ट","ड","ल","श","क"}
		while stripped[-1] in IT_set: stripped = stripped[:-1]
	return "tasya-lopah:" + word + ";stripped=" + stripped

def apply_1_3_10(word, pos=""):
	return "prefix_10:" + word + ";flag=yes"

def apply_1_3_11(word, pos=""):
	return "prefix_11:" + word + ";flag=yes"

def apply_1_3_12(word, pos=""):
	if pos == "anudatta-nit": return "anudAttaiit-Atmanepadam:" + word + ";Atmanepada=yes"
	return "anudAttaiit-Atmanepadam:" + word + ";Atmanepada=no"

def apply_1_3_13(word, pos=""):
	if pos in ("bhAva","karman"): return "bhAvakarmaNoH:" + word + ";sense=" + pos + ";impersonal=yes"
	return "bhAvakarmaNoH:" + word + ";sense=other"

def apply_1_3_14(word, pos=""):
	if pos == "karmavyatihAra": return "kartari-karmavyatihAre:" + word + ";Atmanepada=yes"
	return "kartari-karmavyatihAre:" + word + ";Atmanepada=no"

def apply_1_3_15(word, pos=""):
	EXCLUDE = {"गम्","ई","हन्","स्पर्ध्"}
	if word in EXCLUDE: return "na-gati-hiMsArTeByaH:" + word + ";excluded=yes"
	return "na-gati-hiMsArTeByaH:" + word + ";depends"

def apply_1_3_16(word, pos=""):
	return "itaretarAnyonyopapadAcca:" + word + ";mutual=yes"

def apply_1_3_17(word, pos=""):
	if word == "ने": return "nerviShah:" + word + ";sense=viSh"
	return "nerviShah:" + word + ";n/a"

def apply_1_3_18(word, pos=""):
	PRE = {"परि","वि","अव"}
	for p in PRE:
		if word.startswith(p): return "parivyaveByaH-kriyaH:" + word + ";prefix=" + p
	return "parivyaveByaH-kriyaH:" + word + ";n/a"

def apply_1_3_19(word, pos=""):
	if word == "जि": return "viparAByAM-jeH:" + word + ";yes"
	return "viparAByAM-jeH:" + word + ";n/a"

def apply_1_3_20(word, pos=""):
	if word == "दा" and pos == "anAsya-viharaNa": return "ANo-doAsyaviharaNe:" + word + ";Atmanepada=yes"
	return "ANo-doAsyaviharaNe:" + word + ";n/a"

def apply_1_3_21(word, pos=""):
	PRE = {"अनु","सम्परि"}
	for p in PRE:
		if word.startswith(p): return "krIqo-nusampariByaSca:" + word + ";prefix=" + p
	return "krIqo-nusampariByaSca:" + word + ";n/a"

def apply_1_3_22(word, pos=""):
	PRE = {"सम","व","प्र","वि"}
	if word == "स्था":
		for p in PRE:
			if pos == p: return "samavapraviByaH-sTaH:" + word + ";yes"
	return "samavapraviByaH-sTaH:" + word + ";n/a"

def apply_1_3_23(word, pos=""):
	if pos in ("prakASa","stheya","AKyA"): return "prakASanasTeyAKyayoSca:" + word + ";sense=" + pos
	return "prakASanasTeyAKyayoSca:" + word + ";n/a"

def apply_1_3_24(word, pos=""):
	if word == "उद्" and pos == "anUrDva-karman": return "udoUrDvakarmaNi:" + word + ";yes"
	return "udoUrDvakarmaNi:" + word + ";n/a"

def apply_1_3_25(word, pos=""):
	if word.startswith("उप") and pos == "mantra-karaNa": return "upAnmantrakaraNe:" + word + ";yes"
	return "upAnmantrakaraNe:" + word + ";n/a"

def apply_1_3_26(word, pos=""):
	AK = {"क्रम्","क्लप्","स्वप्","शी","दह्","द्रु","भ्रम्","लम्","ली"}
	if word in AK: return "akarmakAcca:" + word + ";akarmaka=yes"
	return "akarmakAcca:" + word + ";n/a"

def apply_1_3_27(word, pos=""):
	if word == "तप्" and pos in ("उद्","वि"): return "udviByAM-tapaH:" + word + ";yes"
	return "udviByAM-tapaH:" + word + ";n/a"

def apply_1_3_28(word, pos=""):
	if word in ("यम्","हन्") and pos == "AN": return "ANo-yamahanaH:" + word + ";yes"
	return "ANo-yamahanaH:" + word + ";n/a"

def apply_1_3_29(word, pos=""):
	PRE = {"गम्","ऋ","इच्छ्","प्रच्छ्","स्वरत्","श्रु","विद्"}
	if word in PRE and pos == "सम": return "samo-gamyfcChipracCisvaratyartiSruvidibhyaH:" + word + ";yes"
	return "samo-gamyfcChipracCisvaratyartiSruvidibhyaH:" + word + ";n/a"

def apply_1_3_30(word, pos=""):
	if word == "ह्वा" and pos in ("नि","सम","उप","वि"): return "nisamupavibhyo-hvaH:" + word + ";yes"
	return "nisamupavibhyo-hvaH:" + word + ";n/a"

def apply_1_3_31(word, pos=""):
	if pos == "spardhA" and word in ("ऋ","स्पर्ध्"): return "spardhAyAmANaH:" + word + ";yes"
	return "spardhAyAmANaH:" + word + ";n/a"

def apply_1_3_32(word, pos=""):
	CONTEXTS = ("gandhana","AkzepaNa","sevanA","sAhasikya","pratiyatna","prakaTana","upayoga")
	if word == "कृ" and pos in CONTEXTS: return "kandhanAvakzepaRasevanasAhasikyapratiyatnaprakaTanopayogeRu:" + word + ";yes"
	return "kandhanAvakzepaRasevanasAhasikyapratiyatnaprakaTanopayogeRu:" + word + ";n/a"

def apply_1_3_33(word, pos=""):
	return "sutra_33:" + word

def apply_1_3_34(word, pos=""):
	return "sutra_34:" + word

def apply_1_3_35(word, pos=""):
	return "sutra_35:" + word

def apply_1_3_36(word, pos=""):
	return "sutra_36:" + word

def apply_1_3_37(word, pos=""):
	return "sutra_37:" + word

def apply_1_3_38(word, pos=""):
	return "sutra_38:" + word

def apply_1_3_39(word, pos=""):
	return "sutra_39:" + word

def apply_1_3_40(word, pos=""):
	return "sutra_40:" + word

def apply_1_3_41(word, pos=""):
	return "sutra_41:" + word

def apply_1_3_42(word, pos=""):
	return "sutra_42:" + word

def apply_1_3_43(word, pos=""):
	return "sutra_43:" + word

def apply_1_3_44(word, pos=""):
	return "sutra_44:" + word

def apply_1_3_45(word, pos=""):
	return "sutra_45:" + word

def apply_1_3_46(word, pos=""):
	return "sutra_46:" + word

def apply_1_3_47(word, pos=""):
	return "sutra_47:" + word

def apply_1_3_48(word, pos=""):
	return "sutra_48:" + word

def apply_1_3_49(word, pos=""):
	return "sutra_49:" + word

def apply_1_3_50(word, pos=""):
	if pos == "vipralApe": return "viBAzA-vipralApe:" + word + ";optional=yes;sense=vipralApa"
	return "viBAzA-vipralApe:" + word + ";optional=no"

def apply_1_3_51(word, pos=""):
	return "sutra_51:" + word

def apply_1_3_52(word, pos=""):
	return "sutra_52:" + word

def apply_1_3_53(word, pos=""):
	return "sutra_53:" + word

def apply_1_3_54(word, pos=""):
	return "sutra_54:" + word

def apply_1_3_55(word, pos=""):
	return "sutra_55:" + word

def apply_1_3_56(word, pos=""):
	return "sutra_56:" + word

def apply_1_3_57(word, pos=""):
	return "sutra_57:" + word

def apply_1_3_58(word, pos=""):
	return "sutra_58:" + word

def apply_1_3_59(word, pos=""):
	return "sutra_59:" + word

def apply_1_3_60(word, pos=""):
	return "sutra_60:" + word

def apply_1_3_61(word, pos=""):
	return "sutra_61:" + word

def apply_1_3_62(word, pos=""):
	return "sutra_62:" + word

def apply_1_3_63(word, pos=""):
	return "sutra_63:" + word

def apply_1_3_64(word, pos=""):
	return "sutra_64:" + word

def apply_1_3_65(word, pos=""):
	return "sutra_65:" + word

def apply_1_3_66(word, pos=""):
	return "sutra_66:" + word

def apply_1_3_67(word, pos=""):
	return "sutra_67:" + word

def apply_1_3_68(word, pos=""):
	return "sutra_68:" + word

def apply_1_3_69(word, pos=""):
	return "sutra_69:" + word

def apply_1_3_70(word, pos=""):
	return "sutra_70:" + word

def apply_1_3_71(word, pos=""):
	return "sutra_71:" + word

def apply_1_3_72(word, pos=""):
	if pos == "kartf-aBiprAye": return "svaritaYitaH-kartraBiprAye-kriyAPale:" + word + ";Atmanepada=yes"
	return "svaritaYitaH-kartraBiprAye-kriyAPale:" + word + ";not-applicable"

def apply_1_3_73(word, pos=""):
	return "sutra_73:" + word

def apply_1_3_74(word, pos=""):
	return "sutra_74:" + word

def apply_1_3_75(word, pos=""):
	return "sutra_75:" + word

def apply_1_3_76(word, pos=""):
	return "sutra_76:" + word

def apply_1_3_77(word, pos=""):
	return "sutra_77:" + word

def apply_1_3_78(word, pos=""):
	if pos in ("","kartf"): return "SezAt-kartari-parasmEpadam:" + word + ";parasmaipada=yes;default"
	return "SezAt-kartari-parasmEpadam:" + word + ";Atmanepada=yes"

def apply_1_3_79(word, pos=""):
	return "sutra_79:" + word

def apply_1_3_80(word, pos=""):
	return "sutra_80:" + word

def apply_1_3_81(word, pos=""):
	return "sutra_81:" + word

def apply_1_3_82(word, pos=""):
	return "sutra_82:" + word

def apply_1_3_83(word, pos=""):
	return "sutra_83:" + word

def apply_1_3_84(word, pos=""):
	return "sutra_84:" + word

def apply_1_3_85(word, pos=""):
	return "sutra_85:" + word

def apply_1_3_86(word, pos=""):
	return "sutra_86:" + word

def apply_1_3_87(word, pos=""):
	return "sutra_87:" + word

def apply_1_3_88(word, pos=""):
	return "sutra_88:" + word

def apply_1_3_89(word, pos=""):
	return "sutra_89:" + word

def apply_1_3_90(word, pos=""):
	if word.endswith("ष्") or word.endswith("क्ष्"): return "vA-kyzaH:" + word + ";optional=yes"
	return "vA-kyzaH:" + word + ";optional=no"

def apply_1_3_91(word, pos=""):
	return "sutra_91:" + word

def apply_1_3_92(word, pos=""):
	return "sutra_92:" + word

def apply_1_3_93(word, pos=""):
	return "sutra_93:" + word

ALL = {
 "प.1.3.1": apply_1_3_1,
 "प.1.3.2": apply_1_3_2,
 "प.1.3.3": apply_1_3_3,
 "प.1.3.4": apply_1_3_4,
 "प.1.3.5": apply_1_3_5,
 "प.1.3.6": apply_1_3_6,
 "प.1.3.7": apply_1_3_7,
 "प.1.3.8": apply_1_3_8,
 "प.1.3.9": apply_1_3_9,
 "प.1.3.10": apply_1_3_10,
 "प.1.3.11": apply_1_3_11,
 "प.1.3.12": apply_1_3_12,
 "प.1.3.13": apply_1_3_13,
 "प.1.3.14": apply_1_3_14,
 "प.1.3.15": apply_1_3_15,
 "प.1.3.16": apply_1_3_16,
 "प.1.3.17": apply_1_3_17,
 "प.1.3.18": apply_1_3_18,
 "प.1.3.19": apply_1_3_19,
 "प.1.3.20": apply_1_3_20,
 "प.1.3.21": apply_1_3_21,
 "प.1.3.22": apply_1_3_22,
 "प.1.3.23": apply_1_3_23,
 "प.1.3.24": apply_1_3_24,
 "प.1.3.25": apply_1_3_25,
 "प.1.3.26": apply_1_3_26,
 "प.1.3.27": apply_1_3_27,
 "प.1.3.28": apply_1_3_28,
 "प.1.3.29": apply_1_3_29,
 "प.1.3.30": apply_1_3_30,
 "प.1.3.31": apply_1_3_31,
 "प.1.3.32": apply_1_3_32,
 "प.1.3.33": apply_1_3_33,
 "प.1.3.34": apply_1_3_34,
 "प.1.3.35": apply_1_3_35,
 "प.1.3.36": apply_1_3_36,
 "प.1.3.37": apply_1_3_37,
 "प.1.3.38": apply_1_3_38,
 "प.1.3.39": apply_1_3_39,
 "प.1.3.40": apply_1_3_40,
 "प.1.3.41": apply_1_3_41,
 "प.1.3.42": apply_1_3_42,
 "प.1.3.43": apply_1_3_43,
 "प.1.3.44": apply_1_3_44,
 "प.1.3.45": apply_1_3_45,
 "प.1.3.46": apply_1_3_46,
 "प.1.3.47": apply_1_3_47,
 "प.1.3.48": apply_1_3_48,
 "प.1.3.49": apply_1_3_49,
 "प.1.3.50": apply_1_3_50,
 "प.1.3.51": apply_1_3_51,
 "प.1.3.52": apply_1_3_52,
 "प.1.3.53": apply_1_3_53,
 "प.1.3.54": apply_1_3_54,
 "प.1.3.55": apply_1_3_55,
 "प.1.3.56": apply_1_3_56,
 "प.1.3.57": apply_1_3_57,
 "प.1.3.58": apply_1_3_58,
 "प.1.3.59": apply_1_3_59,
 "प.1.3.60": apply_1_3_60,
 "प.1.3.61": apply_1_3_61,
 "प.1.3.62": apply_1_3_62,
 "प.1.3.63": apply_1_3_63,
 "प.1.3.64": apply_1_3_64,
 "प.1.3.65": apply_1_3_65,
 "प.1.3.66": apply_1_3_66,
 "प.1.3.67": apply_1_3_67,
 "प.1.3.68": apply_1_3_68,
 "प.1.3.69": apply_1_3_69,
 "प.1.3.70": apply_1_3_70,
 "प.1.3.71": apply_1_3_71,
 "प.1.3.72": apply_1_3_72,
 "प.1.3.73": apply_1_3_73,
 "प.1.3.74": apply_1_3_74,
 "प.1.3.75": apply_1_3_75,
 "प.1.3.76": apply_1_3_76,
 "प.1.3.77": apply_1_3_77,
 "प.1.3.78": apply_1_3_78,
 "प.1.3.79": apply_1_3_79,
 "प.1.3.80": apply_1_3_80,
 "प.1.3.81": apply_1_3_81,
 "प.1.3.82": apply_1_3_82,
 "प.1.3.83": apply_1_3_83,
 "प.1.3.84": apply_1_3_84,
 "प.1.3.85": apply_1_3_85,
 "प.1.3.86": apply_1_3_86,
 "प.1.3.87": apply_1_3_87,
 "प.1.3.88": apply_1_3_88,
 "प.1.3.89": apply_1_3_89,
 "प.1.3.90": apply_1_3_90,
 "प.1.3.91": apply_1_3_91,
 "प.1.3.92": apply_1_3_92,
 "प.1.3.93": apply_1_3_93,
}

