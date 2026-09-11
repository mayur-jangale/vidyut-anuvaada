# -*- coding: utf-8 -*-
"""Chapter 8 Pada 2 — 108 sutras (P_8_2_1 to P_8_2_108).

Tripadi section — imperative control flow, earlier rules win.
Special imperative paradigms, exceptions, overrides.

Each apply_8_2_Z(word, pos="", SUTRA_TOKEN="") returns a human-readable
string describing what that sutra does, mirroring the per-file SutraZ.apply()
pattern. The dispatcher apply_8_2(word, pos="", SUTRA_TOKEN="") selects the
correct sub-rule by number.
"""

from __future__ import annotations

from typing import Dict

# ──────────────────────────────────────────────────────────────────────────────
# Sutra registry
# ──────────────────────────────────────────────────────────────────────────────

_SUTRAS: Dict[int, Dict[str, str]] = {
	1: {
		"code": "प.8.2.1",
		"text": "पूर्वत्रासिद्धम्",
		"desc": "pūrvatrāsiddham — earlier rule has no effect here (asiddhatva)",
	},
	2: {
		"code": "प.8.2.2",
		"text": "नलोपः सुप्स्वरसंज्ञातुग्विधिषु कृति",
		"desc": "uttaratrāsiddham — later rule has no effect here",
	},
	3: {
		"code": "प.8.2.3",
		"text": "न मु ने",
		"desc": "paratvaṃ — priority of later rules",
	},
	4: {
		"code": "प.8.2.4",
		"text": "उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य",
		"desc": "aparatvaṃ — subordination of earlier rules",
	},
	5: {
		"code": "प.8.2.5",
		"text": "एकादेश उदात्तेनोदात्तः",
		"desc": "pūrvatrāsiddham — repeated",
	},
	6: {
		"code": "प.8.2.6",
		"text": "स्वरितो वाऽनुदात्ते पदादौ",
		"desc": "uttaratrāsiddham — repeated",
	},
	7: {
		"code": "प.8.2.7",
		"text": "नलोपः प्रातिपदिकान्तस्य",
		"desc": "padasya ca halantasya — word-final consonants are treated specially",
	},
	8: {
		"code": "प.8.2.8",
		"text": "न ङिसम्बुद्ध्योः",
		"desc": "saṃhitāyāṃ padāntasya — final element in saṃhitā",
	},
	9: {
		"code": "प.8.2.9",
		"text": "मादुपधायाश्च मतोर्वोऽयवादिभ्यः",
		"desc": "paraḥ paraṃ — each later rule applies to prior",
	},
	10: {
		"code": "प.8.2.10",
		"text": "झयः",
		"desc": "aparaḥ paraṃ — each earlier rule applies to later",
	},
	11: {
		"code": "प.8.2.11",
		"text": "संज्ञायाम्",
		"desc": "pūrvatrāsiddham — repeated",
	},
	12: {
		"code": "प.8.2.12",
		"text": "आसन्दीवदष्ठीवच्चक्रीवत्कक्षीवद्रुमण्वच्चर्मण्वती",
		"desc": "uttaratrāsiddham — repeated",
	},
	13: {
		"code": "प.8.2.13",
		"text": "उदन्वानुदधौ च",
		"desc": "paratvaṃ — repeated",
	},
	14: {
		"code": "प.8.2.14",
		"text": "राजन्वान् सौराज्ये",
		"desc": "aparatvaṃ — repeated",
	},
	15: {
		"code": "प.8.2.15",
		"text": "छन्दसीरः",
		"desc": "pūrvatrāsiddham — repeated",
	},
	16: {
		"code": "प.8.2.16",
		"text": "अनो नुट्",
		"desc": "uttaratrāsiddham — repeated",
	},
	17: {
		"code": "प.8.2.17",
		"text": "नाद्घस्य",
		"desc": "paraḥ paraṃ — repeated",
	},
	18: {
		"code": "प.8.2.18",
		"text": "कृपो रो लः",
		"desc": "aparaḥ paraṃ — repeated",
	},
	19: {
		"code": "प.8.2.19",
		"text": "उपसर्गस्यायतौ",
		"desc": "pūrvatrāsiddham — repeated",
	},
	20: {
		"code": "प.8.2.20",
		"text": "ग्रो यङि",
		"desc": "uttaratrāsiddham — repeated",
	},
	21: {
		"code": "प.8.2.21",
		"text": "अचि विभाषा",
		"desc": "paratvaṃ — repeated",
	},
	22: {
		"code": "प.8.2.22",
		"text": "परेश्च घाङ्कयोः",
		"desc": "aparatvaṃ — repeated",
	},
	23: {
		"code": "प.8.2.23",
		"text": "संयोगान्तस्य लोपः",
		"desc": "pūrvatrāsiddham — repeated",
	},
	24: {
		"code": "प.8.2.24",
		"text": "रात्सस्य",
		"desc": "uttaratrāsiddham — repeated",
	},
	25: {
		"code": "प.8.2.25",
		"text": "धि च",
		"desc": "paraḥ paraṃ — repeated",
	},
	26: {
		"code": "प.8.2.26",
		"text": "झलो झलि",
		"desc": "aparaḥ paraṃ — repeated",
	},
	27: {
		"code": "प.8.2.27",
		"text": "ह्रस्वादङ्गात्",
		"desc": "pūrvatrāsiddham — repeated",
	},
	28: {
		"code": "प.8.2.28",
		"text": "इट ईटि",
		"desc": "uttaratrāsiddham — repeated",
	},
	29: {
		"code": "प.8.2.29",
		"text": "स्कोः संयोगाद्योरन्ते च",
		"desc": "ṣaṇṇāṃ luk — elision of six suffixes (ṣaṇṇāṃ luk)",
	},
	30: {
		"code": "प.8.2.30",
		"text": "चोः कुः",
		"desc": "vibhāṣā senāsaṃyukteṣu — optional rules with army compounds",
	},
	31: {
		"code": "प.8.2.31",
		"text": "हो ढः",
		"desc": "samāse'nañpūrve ktvo lyap — lyap after ktvā in non-negative compounds",
	},
	32: {
		"code": "प.8.2.32",
		"text": "दादेर्धातोर्घः",
		"desc": "samāse'nañpūrve ktvo lyap — repeated",
	},
	33: {
		"code": "प.8.2.33",
		"text": "वा द्रुहमुहष्णुहष्णिहाम्",
		"desc": "pūrvatrāsiddham — repeated",
	},
	34: {
		"code": "प.8.2.34",
		"text": "नहो धः",
		"desc": "uttaratrāsiddham — repeated",
	},
	35: {
		"code": "प.8.2.35",
		"text": "आहस्थः",
		"desc": "paratvaṃ — repeated",
	},
	36: {
		"code": "प.8.2.36",
		"text": "व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः",
		"desc": "aparatvaṃ — repeated",
	},
	37: {
		"code": "प.8.2.37",
		"text": "एकाचो बशो भष् झषन्तस्य स्ध्वोः",
		"desc": "pūrvatrāsiddham — repeated",
	},
	38: {
		"code": "प.8.2.38",
		"text": "दधस्तथोश्च",
		"desc": "uttaratrāsiddham — repeated",
	},
	39: {
		"code": "प.8.2.39",
		"text": "झलां जशोऽन्ते",
		"desc": "samāptiḥ — end of section",
	},
	40: {
		"code": "प.8.2.40",
		"text": "झषस्तथोर्धोऽधः",
		"desc": "(Final transformations (tripāḍī)) — JazastaTorDo'DaH",
	},
	41: {
		"code": "प.8.2.41",
		"text": "षढोः कः सि",
		"desc": "(Final transformations (tripāḍī)) — zaQoH kaH si",
	},
	42: {
		"code": "प.8.2.42",
		"text": "रदाभ्यां निष्ठातो नः पूर्वस्य च दः",
		"desc": "(Final transformations (tripāḍī)) — radAByAM nizWAto naH pUrvasya ca daH",
	},
	43: {
		"code": "प.8.2.43",
		"text": "संयोगादेरातो धातोर्यण्वतः",
		"desc": "(Final transformations (tripāḍī)) — saMyogAderAto DAtoryaRvataH",
	},
	44: {
		"code": "प.8.2.44",
		"text": "ल्वादिभ्यः",
		"desc": "(Final transformations (tripāḍī)) — lvAdiByaH",
	},
	45: {
		"code": "प.8.2.45",
		"text": "ओदितश्च",
		"desc": "(Final transformations (tripāḍī)) — oditaSca",
	},
	46: {
		"code": "प.8.2.46",
		"text": "क्षियो दीर्घात्",
		"desc": "(Final transformations (tripāḍī)) — kziyo dIrGAt",
	},
	47: {
		"code": "प.8.2.47",
		"text": "श्योऽस्पर्शे",
		"desc": "(Final transformations (tripāḍī)) — Syo'sparSe",
	},
	48: {
		"code": "प.8.2.48",
		"text": "अञ्चोऽनपादाने",
		"desc": "(Final transformations (tripāḍī)) — aYco'napAdAne",
	},
	49: {
		"code": "प.8.2.49",
		"text": "दिवोऽविजिगीषायाम्",
		"desc": "(Final transformations (tripāḍī)) — divo'vijigIzAyAm",
	},
	50: {
		"code": "प.8.2.50",
		"text": "निर्वाणोऽवाते",
		"desc": "(Final transformations (tripāḍī)) — nirvARo'vAte",
	},
	51: {
		"code": "प.8.2.51",
		"text": "शुषः कः",
		"desc": "(Final transformations (tripāḍī)) — SuzaH kaH",
	},
	52: {
		"code": "प.8.2.52",
		"text": "पचो वः",
		"desc": "(Final transformations (tripāḍī)) — paco vaH",
	},
	53: {
		"code": "प.8.2.53",
		"text": "क्षायो मः",
		"desc": "(Final transformations (tripāḍī)) — kzAyo maH",
	},
	54: {
		"code": "प.8.2.54",
		"text": "प्रस्त्योऽन्यतरस्याम्",
		"desc": "(Final transformations (tripāḍī)) — prastyo'nyatarasyAm",
	},
	55: {
		"code": "प.8.2.55",
		"text": "अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः",
		"desc": "(Final transformations (tripāḍī)) — anupasargAt PullakzIbakfSollAGAH",
	},
	56: {
		"code": "प.8.2.56",
		"text": "नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्",
		"desc": "(Final transformations (tripāḍī)) — nudavidondatrAGrAhrIByo'nyatarasyAm",
	},
	57: {
		"code": "प.8.2.57",
		"text": "न ध्याख्यापॄमूर्छिमदाम्",
		"desc": "(Final transformations (tripāḍī)) — na DyAKyApFmUrCimadAm",
	},
	58: {
		"code": "प.8.2.58",
		"text": "वित्तो भोगप्रत्यययोः",
		"desc": "(Final transformations (tripāḍī)) — vitto BogapratyayayoH",
	},
	59: {
		"code": "प.8.2.59",
		"text": "भित्तं शकलम्",
		"desc": "(Final transformations (tripāḍī)) — BittaM Sakalam",
	},
	60: {
		"code": "प.8.2.60",
		"text": "ऋणमाधमर्ण्ये",
		"desc": "(Final transformations (tripāḍī)) — fRamADamarRye",
	},
	61: {
		"code": "प.8.2.61",
		"text": "नसत्तनिषत्तानुत्तप्रतूर्तसूर्तगूर्तानि छन्दसि",
		"desc": "(Final transformations (tripāḍī)) — nasattanizattAnuttapratUrtasUrtagUrtAni Candasi",
	},
	62: {
		"code": "प.8.2.62",
		"text": "क्विन्प्रत्ययस्य कुः",
		"desc": "(Final transformations (tripāḍī)) — kvinpratyayasya kuH",
	},
	63: {
		"code": "प.8.2.63",
		"text": "नशेर्वा",
		"desc": "(Final transformations (tripāḍī)) — naServA",
	},
	64: {
		"code": "प.8.2.64",
		"text": "मो नो धातोः",
		"desc": "(Final transformations (tripāḍī)) — mo no DAtoH",
	},
	65: {
		"code": "प.8.2.65",
		"text": "म्वोश्च",
		"desc": "(Final transformations (tripāḍī)) — mvoSca",
	},
	66: {
		"code": "प.8.2.66",
		"text": "ससजुषो रुः",
		"desc": "(Final transformations (tripāḍī)) — sasajuzo ruH",
	},
	67: {
		"code": "प.8.2.67",
		"text": "अवयाःश्वेतवाःपुरोडाश्च",
		"desc": "(Final transformations (tripāḍī)) — avayAHSvetavAHpuroqASca",
	},
	68: {
		"code": "प.8.2.68",
		"text": "अहन्",
		"desc": "(Final transformations (tripāḍी)) — ahan",
	},
	69: {
		"code": "प.8.2.69",
		"text": "रोऽसुपि",
		"desc": "(Final transformations (tripāḍī)) — ro'supi",
	},
	70: {
		"code": "प.8.2.70",
		"text": "अम्नरूधरवरित्युभयथा छन्दसि",
		"desc": "(Final transformations (tripāḍी)) — amnarUDaravarityuBayaTA Candasi",
	},
	71: {
		"code": "प.8.2.71",
		"text": "भुवश्च महाव्याहृतेः",
		"desc": "(Final transformations (tripāḍी)) — BuvaSca mahAvyAhfteH",
	},
	72: {
		"code": "प.8.2.72",
		"text": "वसुस्रंसुध्वंस्वनडुहां दः",
		"desc": "(Final transformations (tripāḍī)) — vasusraMsuDvaMsvanaquhAM daH",
	},
	73: {
		"code": "प.8.2.73",
		"text": "तिप्यनस्तेः",
		"desc": "(Final transformations (tripāḍी)) — tipyanasteH",
	},
	74: {
		"code": "प.8.2.74",
		"text": "सिपि धातो रुर्वा",
		"desc": "(Final transformations (tripāḍī)) — sipi DAto rurvA",
	},
	75: {
		"code": "प.8.2.75",
		"text": "दश्च",
		"desc": "(Final transformations (tripāḍी)) — daSca",
	},
	76: {
		"code": "प.8.2.76",
		"text": "र्वोरुपधाया दीर्घ इकः",
		"desc": "(Final transformations (tripāḍī)) — rvorupaDAyA dIrGa ikaH",
	},
	77: {
		"code": "प.8.2.77",
		"text": "हलि च",
		"desc": "(Final transformations (tripāḍī)) — hali ca",
	},
	78: {
		"code": "प.8.2.78",
		"text": "उपधायां च",
		"desc": "(Final transformations (tripāḍी)) — upaDAyAM ca",
	},
	79: {
		"code": "प.8.2.79",
		"text": "न भकुर्छुराम्",
		"desc": "(Final transformations (tripāḍī)) — na BakurCurAm",
	},
	80: {
		"code": "प.8.2.80",
		"text": "अदसोऽसेर्दादु दो मः",
		"desc": "(Final transformations (tripāḍी)) — adaso'serdAdu do maH",
	},
	81: {
		"code": "प.8.2.81",
		"text": "नाहो नाडः",
		"desc": "(Final transformations (tripāḍी)) — nAho nAqaH",
	},
	82: {
		"code": "प.8.2.82",
		"text": "असिद्धं वा कडारस्य",
		"desc": "(Final transformations (tripāḍī)) — asidDaM vA kqArasya",
	},
	83: {
		"code": "प.8.2.83",
		"text": "हेर्धः",
		"desc": "(Final transformations (tripāḍī)) — herDaH",
	},
	84: {
		"code": "प.8.2.84",
		"text": "श्र्यङ्गोश्छन्दसि बहुलम्",
		"desc": "(Final transformations (tripāḍī)) — SryaFgoSCandasi bahulam",
	},
	85: {
		"code": "प.8.2.85",
		"text": "हैहेप्रयोगे हैहयोः",
		"desc": "(Final transformations (tripāḍī)) — hEheprayoge hEhayoH",
	},
	86: {
		"code": "प.8.2.86",
		"text": "गवोऽश्वस्य चान्यतरस्याम्",
		"desc": "(Final transformations (tripāḍी)) — gavo'Svasya cAnyatarasyAm",
	},
	87: {
		"code": "प.8.2.87",
		"text": "वाहो वहतौ",
		"desc": "(Final transformations (tripāḍी)) — vAho vahatO",
	},
	88: {
		"code": "प.8.2.88",
		"text": "सन्ध्योः",
		"desc": "(Final transformations (tripāḍी)) — sanDyoH",
	},
	89: {
		"code": "प.8.2.89",
		"text": "नानाञोर्यतो लोपः",
		"desc": "(Final transformations (tripāḍī)) — nAnAQoH yato lopaH",
	},
	90: {
		"code": "प.8.2.90",
		"text": "याज्याऽन्तः",
		"desc": "(Final transformations (tripāḍी)) — yAjyA'ntaH",
	},
	91: {
		"code": "प.8.2.91",
		"text": "अर्धं भाजनम्",
		"desc": "(Final transformations (tripāḍī)) — arDaM BAjanam",
	},
	92: {
		"code": "प.8.2.92",
		"text": "आराद्द्व्यक्तिर्द्योरच्",
		"desc": "(Final transformations (tripāḍī)) — ArAddvyaktirdyo'c",
	},
	93: {
		"code": "प.8.2.93",
		"text": "गोत्रादीनि च",
		"desc": "(Final transformations (tripāḍī)) — gotrAdIni ca",
	},
	94: {
		"code": "प.8.2.94",
		"text": "स्वरितं चाद्युदात्तं छन्दसि बहुलम्",
		"desc": "(Final transformations (tripāḍī)) — svaritaM cAdyudAttaM Candasi bahulam",
	},
	95: {
		"code": "प.8.2.95",
		"text": "आम्रेडितं भर्त्सने",
		"desc": "(Final transformations (tripāḍी)) — AmreqitaM Bartsane",
	},
	96: {
		"code": "प.8.2.96",
		"text": "अङ्गयुक्तं तिङ् आकाङ्क्षम्",
		"desc": "(Final transformations (tripāḍी)) — aNgayuktaM tiN AkANkzam",
	},
	97: {
		"code": "प.8.2.97",
		"text": "प्रथमात्पुरुषात्परस्य",
		"desc": "(Final transformations (tripāḍī)) — praTamAtpuruSAtparasya",
	},
	98: {
		"code": "प.8.2.98",
		"text": "पूर्वं तु भाषायाम्",
		"desc": "(Final transformations (tripāḍी)) — pUrvaM tu BAzAyAm",
	},
	99: {
		"code": "प.8.2.99",
		"text": "प्रतिश्रवणे च",
		"desc": "(Final transformations (tripāḍī)) — pratiSravaRe ca",
	},
	100: {
		"code": "प.8.2.100",
		"text": "अनुदात्तं प्रश्नान्ताभिपूजितयोः",
		"desc": "(Final transformations (tripāḍī)) — anudAttaM praSnAntABipUjitayoH",
	},
	101: {
		"code": "प.8.2.101",
		"text": "चिदिति चोपमाऽर्थे प्रयुज्यमाने",
		"desc": "(Final transformations (tripāḍी)) — ciditi copamA'rTe prayujyamAne",
	},
	102: {
		"code": "प.8.2.102",
		"text": "स्वरितमगतिर्गतिकरणे",
		"desc": "(Final transformations (tripāḍī)) — svaritamagatiH gatikaraRe",
	},
	103: {
		"code": "प.8.2.103",
		"text": "स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु",
		"desc": "(Final transformations (tripāḍी)) — svaritamAmreqite'sUyAsammatikopakutsanezu",
	},
	104: {
		"code": "प.8.2.104",
		"text": "विहारस्वप्नयोः स्मोः",
		"desc": "(Final transformations (tripāḍी)) — vihArasvapnayoH smoH",
	},
	105: {
		"code": "प.8.2.105",
		"text": "निपातस्य पादाद्यादावन्यतरस्याम्",
		"desc": "(Final transformations (tripāḍī)) — nipAtasya pAdAdyAdAvanyatarasyAm",
	},
	106: {
		"code": "प.8.2.106",
		"text": "आद्युदात्तो द्वितीयस्य तृतीयस्य च",
		"desc": "(Final transformations (tripāḍī)) — AdyudAtto dvitIyasya tRtIyasya ca",
	},
	107: {
		"code": "प.8.2.107",
		"text": "एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ",
		"desc": "(Final transformations (tripāḍी)) — eco'pragfhyasyAdUrAdDUte pUrvasyArDasyAduttarasyedutO",
	},
	108: {
		"code": "प.8.2.108",
		"text": "तयोर्य्वावचि संहितायाम्",
		"desc": "(Final transformations (tripāḍī)) — tayoryvAvaci saMhitAyAm",
	},
}

# ──────────────────────────────────────────────────────────────────────────────
# Individual apply_8_2_N functions (N = 1 .. 108)
# ──────────────────────────────────────────────────────────────────────────────

def apply_8_2_1(word="", pos="", SUTRA_TOKEN=""):
	"""पूर्वत्रासिद्धम् — earlier rule has no effect here (asiddhatva)."""
	rec = _SUTRAS[1]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_2(word="", pos="", SUTRA_TOKEN=""):
	"""नलोपः सुप्स्वरसंज्ञातुग्विधिषु कृति — later rule has no effect here."""
	rec = _SUTRAS[2]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_3(word="", pos="", SUTRA_TOKEN=""):
	"""न मु ने — priority of later rules."""
	rec = _SUTRAS[3]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_4(word="", pos="", SUTRA_TOKEN=""):
	"""उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य — subordination of earlier rules."""
	rec = _SUTRAS[4]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_5(word="", pos="", SUTRA_TOKEN=""):
	"""एकादेश उदात्तेनोदात्तः — pūrvatrāsiddham repeated."""
	rec = _SUTRAS[5]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_6(word="", pos="", SUTRA_TOKEN=""):
	"""स्वरितो वाऽनुदात्ते पदादौ — uttaratrāsiddham repeated."""
	rec = _SUTRAS[6]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_7(word="", pos="", SUTRA_TOKEN=""):
	"""नलोपः प्रातिपदिकान्तस्य — word-final consonants are treated specially."""
	rec = _SUTRAS[7]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_8(word="", pos="", SUTRA_TOKEN=""):
	"""न ङिसम्बुद्ध्योः — final element in saṃhitā."""
	rec = _SUTRAS[8]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_9(word="", pos="", SUTRA_TOKEN=""):
	"""मादुपधायाश्च मतोर्वोऽयवादिभ्यः — each later rule applies to prior."""
	rec = _SUTRAS[9]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_10(word="", pos="", SUTRA_TOKEN=""):
	"""झयः — each earlier rule applies to later."""
	rec = _SUTRAS[10]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_11(word="", pos="", SUTRA_TOKEN=""):
	"""संज्ञायाम् — pūrvatrāsiddham repeated."""
	rec = _SUTRAS[11]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_12(word="", pos="", SUTRA_TOKEN=""):
	"""आसन्दीवदष्ठीवच्चक्रीवत्कक्षीवद्रुमण्वच्चर्मण्वती — uttaratrāsiddham repeated."""
	rec = _SUTRAS[12]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_13(word="", pos="", SUTRA_TOKEN=""):
	"""उदन्वानुदधौ च — paratvaṃ repeated."""
	rec = _SUTRAS[13]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_14(word="", pos="", SUTRA_TOKEN=""):
	"""राजन्वान् सौराज्ये — aparatvaṃ repeated."""
	rec = _SUTRAS[14]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_15(word="", pos="", SUTRA_TOKEN=""):
	"""छन्दसीरः — pūrvatrāsiddham repeated."""
	rec = _SUTRAS[15]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_16(word="", pos="", SUTRA_TOKEN=""):
	"""अनो नुट् — uttaratrāsiddham repeated."""
	rec = _SUTRAS[16]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_17(word="", pos="", SUTRA_TOKEN=""):
	"""नाद्घस्य — paraḥ paraṃ repeated."""
	rec = _SUTRAS[17]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_18(word="", pos="", SUTRA_TOKEN=""):
	"""कृपो रो लः — aparaḥ paraṃ repeated."""
	rec = _SUTRAS[18]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_19(word="", pos="", SUTRA_TOKEN=""):
	"""उपसर्गस्यायतौ — pūrvatrāsiddham repeated."""
	rec = _SUTRAS[19]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_20(word="", pos="", SUTRA_TOKEN=""):
	"""ग्रो यङि — uttaratrāsiddham repeated."""
	rec = _SUTRAS[20]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_21(word="", pos="", SUTRA_TOKEN=""):
	"""अचि विभाषा — paratvaṃ repeated."""
	rec = _SUTRAS[21]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_22(word="", pos="", SUTRA_TOKEN=""):
	"""परेश्च घाङ्कयोः — aparatvaṃ repeated."""
	rec = _SUTRAS[22]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_23(word="", pos="", SUTRA_TOKEN=""):
	"""संयोगान्तस्य लोपः — pūrvatrāsiddham repeated."""
	rec = _SUTRAS[23]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_24(word="", pos="", SUTRA_TOKEN=""):
	"""रात्सस्य — uttaratrāsiddham repeated."""
	rec = _SUTRAS[24]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_25(word="", pos="", SUTRA_TOKEN=""):
	"""धि च — paraḥ paraṃ repeated."""
	rec = _SUTRAS[25]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_26(word="", pos="", SUTRA_TOKEN=""):
	"""झलो झलि — aparaḥ paraṃ repeated."""
	rec = _SUTRAS[26]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_27(word="", pos="", SUTRA_TOKEN=""):
	"""ह्रस्वादङ्गात् — pūrvatrāsiddham repeated."""
	rec = _SUTRAS[27]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_28(word="", pos="", SUTRA_TOKEN=""):
	"""इट ईटि — uttaratrāsiddham repeated."""
	rec = _SUTRAS[28]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_29(word="", pos="", SUTRA_TOKEN=""):
	"""स्कोः संयोगाद्योरन्ते च — ṣaṇṇāṃ luk elision."""
	rec = _SUTRAS[29]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_30(word="", pos="", SUTRA_TOKEN=""):
	"""चोः कुः — optional rules with army compounds."""
	rec = _SUTRAS[30]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_31(word="", pos="", SUTRA_TOKEN=""):
	"""हो ढः — lyap after ktvā in non-negative compounds."""
	rec = _SUTRAS[31]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_32(word="", pos="", SUTRA_TOKEN=""):
	"""दादेर्धातोर्घः — repeated."""
	rec = _SUTRAS[32]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_33(word="", pos="", SUTRA_TOKEN=""):
	"""वा द्रुहमुहष्णुहष्णिहाम् — pūrvatrāsiddham repeated."""
	rec = _SUTRAS[33]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_34(word="", pos="", SUTRA_TOKEN=""):
	"""नहो धः — uttaratrāsiddham repeated."""
	rec = _SUTRAS[34]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_35(word="", pos="", SUTRA_TOKEN=""):
	"""आहस्थः — paratvaṃ repeated."""
	rec = _SUTRAS[35]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_36(word="", pos="", SUTRA_TOKEN=""):
	"""व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः — aparatvaṃ repeated."""
	rec = _SUTRAS[36]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_37(word="", pos="", SUTRA_TOKEN=""):
	"""एकाचो बशो भष् झषन्तस्य स्ध्वोः — pūrvatrāsiddham repeated."""
	rec = _SUTRAS[37]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_38(word="", pos="", SUTRA_TOKEN=""):
	"""दधस्तथोश्च — uttaratrāsiddham repeated."""
	rec = _SUTRAS[38]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_39(word="", pos="", SUTRA_TOKEN=""):
	"""झलां जशोऽन्ते — samāptiḥ end of section."""
	rec = _SUTRAS[39]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_40(word="", pos="", SUTRA_TOKEN=""):
	"""झषस्तथोर्धोऽधः — tripāḍī: jhaṣa final dh→dh before a."""
	rec = _SUTRAS[40]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_41(word="", pos="", SUTRA_TOKEN=""):
	"""षढोः कः सि — tripāḍī: ṣaḍhaḥ ḍ→k in si."""
	rec = _SUTRAS[41]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_42(word="", pos="", SUTRA_TOKEN=""):
	"""रदाभ्यां निष्ठातो नः पूर्वस्य च दः — tripāḍī."""
	rec = _SUTRAS[42]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_43(word="", pos="", SUTRA_TOKEN=""):
	"""संयोगादेरातो धातोर्यण्वतः — tripāḍī."""
	rec = _SUTRAS[43]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_44(word="", pos="", SUTRA_TOKEN=""):
	"""ल्वादिभ्यः — tripāḍī: lvādi roots."""
	rec = _SUTRAS[44]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_45(word="", pos="", SUTRA_TOKEN=""):
	"""ओदितश्च — tripāḍī: o+dit roots."""
	rec = _SUTRAS[45]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_46(word="", pos="", SUTRA_TOKEN=""):
	"""क्षियो दीर्घात् — tripāḍī: kṣi from long vowel."""
	rec = _SUTRAS[46]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_47(word="", pos="", SUTRA_TOKEN=""):
	"""श्योऽस्पर्शे — tripāḍī: śyaḥ before sparśa consonants."""
	rec = _SUTRAS[47]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_48(word="", pos="", SUTRA_TOKEN=""):
	"""अञ्चोऽनपादाने — tripāḍī: añcaḥ when not apādāna."""
	rec = _SUTRAS[48]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_49(word="", pos="", SUTRA_TOKEN=""):
	"""दिवोऽविजिगीषायाम् — tripāḍī: divaḥ in desire to win."""
	rec = _SUTRAS[49]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_50(word="", pos="", SUTRA_TOKEN=""):
	"""निर्वाणोऽवाते — tripāḍī: nirvāṇaḥ before avāte."""
	rec = _SUTRAS[50]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_51(word="", pos="", SUTRA_TOKEN=""):
	"""शुषः कः — tripāḍī: śuṣaḥ ḍ→k."""
	rec = _SUTRAS[51]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_52(word="", pos="", SUTRA_TOKEN=""):
	"""पचो वः — tripāḍī: pacaḥ t→v."""
	rec = _SUTRAS[52]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_53(word="", pos="", SUTRA_TOKEN=""):
	"""क्षायो मः — tripāḍī: kṣāyaḥ ḍ→m."""
	rec = _SUTRAS[53]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_54(word="", pos="", SUTRA_TOKEN=""):
	"""प्रस्त्योऽन्यतरस्याम् — tripāḍī: prastyaḥ optionally."""
	rec = _SUTRAS[54]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_55(word="", pos="", SUTRA_TOKEN=""):
	"""अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः — tripāḍī."""
	rec = _SUTRAS[55]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_56(word="", pos="", SUTRA_TOKEN=""):
	"""नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम् — tripāḍī."""
	rec = _SUTRAS[56]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_57(word="", pos="", SUTRA_TOKEN=""):
	"""न ध्याख्यापॄमूर्छिमदाम् — tripāḍī: exceptions."""
	rec = _SUTRAS[57]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_58(word="", pos="", SUTRA_TOKEN=""):
	"""वित्तो भोगप्रत्यययोः — tripāḍī: vittaḥ before bhogapratyaya."""
	rec = _SUTRAS[58]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_59(word="", pos="", SUTRA_TOKEN=""):
	"""भित्तं शकलम् — tripāḍī: bhittaṃ śakalam."""
	rec = _SUTRAS[59]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_60(word="", pos="", SUTRA_TOKEN=""):
	"""ऋणमाधमर्ण्ये — tripāḍī: ṛṇamādhamaṇṇye."""
	rec = _SUTRAS[60]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_61(word="", pos="", SUTRA_TOKEN=""):
	"""नसत्तनिषत्तानुत्तप्रतूर्तसूर्तगूर्तानि छन्दसि — tripāḍī."""
	rec = _SUTRAS[61]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_62(word="", pos="", SUTRA_TOKEN=""):
	"""क्विन्प्रत्ययस्य कुः — tripāḍī: kvin-pratyaya kuḥ."""
	rec = _SUTRAS[62]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_63(word="", pos="", SUTRA_TOKEN=""):
	"""नशेर्वा — tripāḍī: naśeḥ optional."""
	rec = _SUTRAS[63]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_64(word="", pos="", SUTRA_TOKEN=""):
	"""मो नो धातोः — tripāḍī: mo→no in dhātu."""
	rec = _SUTRAS[64]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_65(word="", pos="", SUTRA_TOKEN=""):
	"""म्वोश्च — tripāḍī: mvośca."""
	rec = _SUTRAS[65]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_66(word="", pos="", SUTRA_TOKEN=""):
	"""ससजुषो रुः — tripāḍī: sa-sajuṣo ruḥ."""
	rec = _SUTRAS[66]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_67(word="", pos="", SUTRA_TOKEN=""):
	"""अवयाःश्वेतवाःपुरोडाश्च — tripāḍī: avayāḥ śvetavāḥ puroḍāśaḥ."""
	rec = _SUTRAS[67]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_68(word="", pos="", SUTRA_TOKEN=""):
	"""अहन् — tripāḍī: ahan."""
	rec = _SUTRAS[68]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_69(word="", pos="", SUTRA_TOKEN=""):
	"""रोऽसुपि — tripāḍī: raḥ before supi."""
	rec = _SUTRAS[69]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_70(word="", pos="", SUTRA_TOKEN=""):
	"""अम्नरूधरवरित्युभयथा छन्दसि — tripāḍī: amnaru-dhara-vara."""
	rec = _SUTRAS[70]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_71(word="", pos="", SUTRA_TOKEN=""):
	"""भुवश्च महाव्याहृतेः — tripāḍī: bhuvas ca mahāvyāhṛteḥ."""
	rec = _SUTRAS[71]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_72(word="", pos="", SUTRA_TOKEN=""):
	"""वसुस्रंसुध्वंस्वनडुहां दः — tripāḍī."""
	rec = _SUTRAS[72]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_73(word="", pos="", SUTRA_TOKEN=""):
	"""तिप्यनस्तेः — tripāḍī: tipyanasteḥ."""
	rec = _SUTRAS[73]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_74(word="", pos="", SUTRA_TOKEN=""):
	"""सिपि धातो रुर्वा — tripāḍī: sipi dhāto rurvā."""
	rec = _SUTRAS[74]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_75(word="", pos="", SUTRA_TOKEN=""):
	"""दश्च — tripāḍī: daśca."""
	rec = _SUTRAS[75]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_76(word="", pos="", SUTRA_TOKEN=""):
	"""र्वोरुपधाया दीर्घ इकः — tripāḍī: rvor upadhāyā dīrgha ikaḥ."""
	rec = _SUTRAS[76]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_77(word="", pos="", SUTRA_TOKEN=""):
	"""हलि च — tripāḍī: hali ca."""
	rec = _SUTRAS[77]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_78(word="", pos="", SUTRA_TOKEN=""):
	"""उपधायां च — tripāḍī: upadhāyāṃ ca."""
	rec = _SUTRAS[78]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_79(word="", pos="", SUTRA_TOKEN=""):
	"""न भकुर्छुराम् — tripāḍī: na bhakurchurām."""
	rec = _SUTRAS[79]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_80(word="", pos="", SUTRA_TOKEN=""):
	"""अदसोऽसेर्दादु दो मः — tripāḍī."""
	rec = _SUTRAS[80]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_81(word="", pos="", SUTRA_TOKEN=""):
	"""नाहो नाडः — tripāḍī: nāho nāḍaḥ."""
	rec = _SUTRAS[81]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_82(word="", pos="", SUTRA_TOKEN=""):
	"""असिद्धं वा कडारस्य — tripāḍī: asiddhaṃ vā kḍārasya."""
	rec = _SUTRAS[82]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_83(word="", pos="", SUTRA_TOKEN=""):
	"""हेर्धः — tripāḍī: herdhaḥ."""
	rec = _SUTRAS[83]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_84(word="", pos="", SUTRA_TOKEN=""):
	"""श्र्यङ्गोश्छन्दसि बहुलम् — tripāḍī."""
	rec = _SUTRAS[84]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_85(word="", pos="", SUTRA_TOKEN=""):
	"""हैहेप्रयोगे हैहयोः — tripāḍī."""
	rec = _SUTRAS[85]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_86(word="", pos="", SUTRA_TOKEN=""):
	"""गवोऽश्वस्य चान्यतरस्याम् — tripāḍī."""
	rec = _SUTRAS[86]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_87(word="", pos="", SUTRA_TOKEN=""):
	"""वाहो वहतौ — tripāḍī: vāho vahatau."""
	rec = _SUTRAS[87]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_88(word="", pos="", SUTRA_TOKEN=""):
	"""सन्ध्योः — tripāḍī: sandhyoḥ."""
	rec = _SUTRAS[88]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_89(word="", pos="", SUTRA_TOKEN=""):
	"""नानाञोर्यतो लोपः — tripāḍī."""
	rec = _SUTRAS[89]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_90(word="", pos="", SUTRA_TOKEN=""):
	"""याज्याऽन्तः — tripāḍī: yājyā'ntaḥ."""
	rec = _SUTRAS[90]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_91(word="", pos="", SUTRA_TOKEN=""):
	"""अर्धं भाजनम् — tripāḍī: arghaṃ bhājanam."""
	rec = _SUTRAS[91]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_92(word="", pos="", SUTRA_TOKEN=""):
	"""आराद्द्व्यक्तिर्द्योरच् — tripāḍī."""
	rec = _SUTRAS[92]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_93(word="", pos="", SUTRA_TOKEN=""):
	"""गोत्रादीनि च — tripāḍī: gotrādīni ca."""
	rec = _SUTRAS[93]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_94(word="", pos="", SUTRA_TOKEN=""):
	"""स्वरितं चाद्युदात्तं छन्दसि बहुलम् — tripāḍī."""
	rec = _SUTRAS[94]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_95(word="", pos="", SUTRA_TOKEN=""):
	"""आम्रेडितं भर्त्सने — tripāḍī: āmreḍitaṃ bhartṣane."""
	rec = _SUTRAS[95]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_96(word="", pos="", SUTRA_TOKEN=""):
	"""अङ्गयुक्तं तिङ् आकाङ्क्षम् — tripāḍī: aṅgayuktaṃ tiṅ ākāṅkṣam."""
	rec = _SUTRAS[96]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_97(word="", pos="", SUTRA_TOKEN=""):
	"""प्रथमात्पुरुषात्परस्य — tripāḍī."""
	rec = _SUTRAS[97]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_98(word="", pos="", SUTRA_TOKEN=""):
	"""पूर्वं तु भाषायाम् — tripāḍī: pūrvaṃ tu bhāṣāyām."""
	rec = _SUTRAS[98]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_99(word="", pos="", SUTRA_TOKEN=""):
	"""प्रतिश्रवणे च — tripāḍī: pratiśravaṇe ca."""
	rec = _SUTRAS[99]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_100(word="", pos="", SUTRA_TOKEN=""):
	"""अनुदात्तं प्रश्नान्ताभिपूजितयोः — tripāḍī."""
	rec = _SUTRAS[100]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_101(word="", pos="", SUTRA_TOKEN=""):
	"""चिदिति चोपमाऽर्थे प्रयुज्यमाने — tripāḍī."""
	rec = _SUTRAS[101]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_102(word="", pos="", SUTRA_TOKEN=""):
	"""स्वरितमगतिर्गतिकरणे — tripāḍī."""
	rec = _SUTRAS[102]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_103(word="", pos="", SUTRA_TOKEN=""):
	"""स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु — tripāḍī."""
	rec = _SUTRAS[103]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_104(word="", pos="", SUTRA_TOKEN=""):
	"""विहारस्वप्नयोः स्मोः — tripāḍī."""
	rec = _SUTRAS[104]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_105(word="", pos="", SUTRA_TOKEN=""):
	"""निपातस्य पादाद्यादावन्यतरस्याम् — tripāḍī."""
	rec = _SUTRAS[105]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_106(word="", pos="", SUTRA_TOKEN=""):
	"""आद्युदात्तो द्वितीयस्य तृतीयस्य च — tripāḍī."""
	rec = _SUTRAS[106]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_107(word="", pos="", SUTRA_TOKEN=""):
	"""एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ — tripāḍī."""
	rec = _SUTRAS[107]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


def apply_8_2_108(word="", pos="", SUTRA_TOKEN=""):
	"""तयोर्य्वावचि संहितायाम् — tripāḍī: tayor vyāvaci saṃhitāyām."""
	rec = _SUTRAS[108]
	return f"{rec['code']}:{rec['text']} → {rec['desc']} | word={word} pos={pos} token={SUTRA_TOKEN}"


# ──────────────────────────────────────────────────────────────────────────────
# Dispatcher — calls the right sub-rule by number
# ──────────────────────────────────────────────────────────────────────────────

def apply_8_2(n, word="", pos="", SUTRA_TOKEN=""):
	"""Dispatch to apply_8_2_N for n ∈ [1, 108].

	Returns the string produced by the matching sub-rule, or a 'not-found'
	message if n is out of range.
	"""
	if not (1 <= n <= 108):
		return f"प.8.2: sutra {n} out of range (1-108)"
	func = {
		1: apply_8_2_1,
		2: apply_8_2_2,
		3: apply_8_2_3,
		4: apply_8_2_4,
		5: apply_8_2_5,
		6: apply_8_2_6,
		7: apply_8_2_7,
		8: apply_8_2_8,
		9: apply_8_2_9,
		10: apply_8_2_10,
		11: apply_8_2_11,
		12: apply_8_2_12,
		13: apply_8_2_13,
		14: apply_8_2_14,
		15: apply_8_2_15,
		16: apply_8_2_16,
		17: apply_8_2_17,
		18: apply_8_2_18,
		19: apply_8_2_19,
		20: apply_8_2_20,
		21: apply_8_2_21,
		22: apply_8_2_22,
		23: apply_8_2_23,
		24: apply_8_2_24,
		25: apply_8_2_25,
		26: apply_8_2_26,
		27: apply_8_2_27,
		28: apply_8_2_28,
		29: apply_8_2_29,
		30: apply_8_2_30,
		31: apply_8_2_31,
		32: apply_8_2_32,
		33: apply_8_2_33,
		34: apply_8_2_34,
		35: apply_8_2_35,
		36: apply_8_2_36,
		37: apply_8_2_37,
		38: apply_8_2_38,
		39: apply_8_2_39,
		40: apply_8_2_40,
		41: apply_8_2_41,
		42: apply_8_2_42,
		43: apply_8_2_43,
		44: apply_8_2_44,
		45: apply_8_2_45,
		46: apply_8_2_46,
		47: apply_8_2_47,
		48: apply_8_2_48,
		49: apply_8_2_49,
		50: apply_8_2_50,
		51: apply_8_2_51,
		52: apply_8_2_52,
		53: apply_8_2_53,
		54: apply_8_2_54,
		55: apply_8_2_55,
		56: apply_8_2_56,
		57: apply_8_2_57,
		58: apply_8_2_58,
		59: apply_8_2_59,
		60: apply_8_2_60,
		61: apply_8_2_61,
		62: apply_8_2_62,
		63: apply_8_2_63,
		64: apply_8_2_64,
		65: apply_8_2_65,
		66: apply_8_2_66,
		67: apply_8_2_67,
		68: apply_8_2_68,
		69: apply_8_2_69,
		70: apply_8_2_70,
		71: apply_8_2_71,
		72: apply_8_2_72,
		73: apply_8_2_73,
		74: apply_8_2_74,
		75: apply_8_2_75,
		76: apply_8_2_76,
		77: apply_8_2_77,
		78: apply_8_2_78,
		79: apply_8_2_79,
		80: apply_8_2_80,
		81: apply_8_2_81,
		82: apply_8_2_82,
		83: apply_8_2_83,
		84: apply_8_2_84,
		85: apply_8_2_85,
		86: apply_8_2_86,
		87: apply_8_2_87,
		88: apply_8_2_88,
		89: apply_8_2_89,
		90: apply_8_2_90,
		91: apply_8_2_91,
		92: apply_8_2_92,
		93: apply_8_2_93,
		94: apply_8_2_94,
		95: apply_8_2_95,
		96: apply_8_2_96,
		97: apply_8_2_97,
		98: apply_8_2_98,
		99: apply_8_2_99,
		100: apply_8_2_100,
		101: apply_8_2_101,
		102: apply_8_2_102,
		103: apply_8_2_103,
		104: apply_8_2_104,
		105: apply_8_2_105,
		106: apply_8_2_106,
		107: apply_8_2_107,
		108: apply_8_2_108,
	}[n]
	return func(word, pos, SUTRA_TOKEN)


# ──────────────────────────────────────────────────────────────────────────────
# Convenience: list all sutra codes
# ──────────────────────────────────────────────────────────────────────────────

def all_sutras():
	"""Return a list of (number, code, text, desc) for all 108 sutras."""
	return [(n, _SUTRAS[n]["code"], _SUTRAS[n]["text"], _SUTRAS[n]["desc"])
			for n in range(1, 109)]
