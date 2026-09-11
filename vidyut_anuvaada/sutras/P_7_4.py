"""P.7.4.x shared module — 97 apply_7_4_Z functions for derivation and tiG rules."""
from __future__ import annotations

CATEGORIES = {
	"intro": "introductory",
	"gender": "liṅga-sthāna",
	"vibhakti": "vibhakti-sthāna",
	"sup-sthana": "sup-sthāna",
	"taddhita": "taddhita",
	"tiG": "tiṇ-kit",
	"tripadi": "tripādi",
}

# Standard sup tables (21 endings each)
SUP_PUMS = ["सु","औ","जस्","गा","भ्याम्","भिस्","गी","भ्यहित्यही","भ्यसिं","सुप्"]
SUP_STRI = ["सु","औ","जस्","गाहि","भ्याम्","भिस्","गीयसि","भ्यहित्यही","गीयाम्","भ्यसिं","गीयाही","आम्","गीयाम्","औस्","सुप्"]
SUP_NAPUNS = ["सु","औ","जस्","गि","भ्याम्","भिस्","गी","भ्यहित्यही","भ्यसिं","भ्यस्","आम्","गी","औस्","सुप्"]

VIBHAKTI_IDX = {1: 0, 2: 13, 3: 3, 4: 6, 5: 9, 6: 11, 7: 7}

def _s(code, desc, cat):
	return f"{code}: [{cat}] {desc}"

def _apply_1_1(word, pos, code, desc, cat, ex_word, ex_pos, ex_result):
	"""Generic apply: returns category + sutra code + first example result."""
	return _s(code, desc, cat) + f";input={word};pos={pos};example={ex_word}|{ex_pos}→{ex_result}"

# P.7.4.1: ञौ चङ्युपधाया ह्रस्वः — taddhita (hrasva after cag-yaG)
def apply_7_4_1(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.1", "णौ चङ्युपधाया ह्रस्वः (hrasva for cag-yaG)", "taddhita",
	"अग्नि", "puṃ", "अग्नेः")

# P.7.4.2: नाग्लोपिशास्वृदिताम् — taddhita (no luk/anaG)
def apply_7_4_2(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.2", "नाग्लोपिशास्वृदिताम् (no luk/anaG for listed)", "taddhita",
	"देव", "puṃ", "दैव")

# P.7.4.3: भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम् — taddhita
def apply_7_4_3(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.3", "भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम् (viśeṣa-taddhita)", "taddhita",
	"भ्राज", "puṃ", "भ्राट/भ्राज")

# P.7.4.4: लोपः पिबतेरीच्चाभ्यासस्य — tiG (lop for piba + icca)
def apply_7_4_4(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.4", "लोपः पिबतेरीच्चाभ्यासस्य (lopa of abhyasa)", "tiG",
	"पिब", "lat", "पिबति")

# P.7.4.5: तिष्ठतेरित् — tiG (it after tiSThat)
def apply_7_4_5(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.5", "तिष्ठतेरित् (it affix for tiSThat)", "tiG",
	"तिष्ठ", "lat", "तिष्ठतेः")

# P.7.4.6: जिघ्रतेर्वा — tiG (optional rule for jiGhrat)
def apply_7_4_6(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.6", "जिघ्रतेर्वा (optional for jiGhrat)", "tiG",
	"जिघ्र", "lat", "जिघ्रति/जिघ्रते")

# P.7.4.7: उरृत् — tiG (u + Rt for listed roots)
def apply_7_4_7(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.7", "उरृत् (u-Rt affix)", "tiG",
	"शी", "lat", "शेते")

# P.7.4.8: नित्यं छन्दसि — tiG (always in Vedic)
def apply_7_4_8(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.8", "नित्यं छन्दसि (nitya in chandasi)", "tiG",
	"कृ", "lot-ch", "करोतु")

# P.7.4.9: दयतेर्दिगि लिटि — tiG (day + digi in lit)
def apply_7_4_9(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.9", "दयतेर्दिगि लिटि (day-digi in lit)", "tiG",
	"दय", "lit", "दिद्ये")

# P.7.4.10: ऋतश्च संयोगादेर्गुणः — tiG (guna after samyoga)
def apply_7_4_10(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.10", "ऋतश्च संयोगादेर्गुणः (guna after samyoga)", "tiG",
	"कृष्", "lat", "कर्षति")

# P.7.4.11: ऋच्छत्यॄताम् — tiG (RcChat-grama)
def apply_7_4_11(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.11", "ऋच्छत्यॄताम् (RcChat-tAm)", "tiG",
	"इष्", "lat", "इर्ष्यति")

# P.7.4.12: शॄदॄप्रां ह्रस्वो वा — tiG (hrasva option)
def apply_7_4_12(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.12", "शॄदॄप्रां ह्रस्वो वा (hrasva option)", "tiG",
	"शॄ", "lat", "शरति/श्राति")

# P.7.4.13: केऽणः — tiG (ke-No)
def apply_7_4_13(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.13", "केऽणः (ke-No)", "tiG",
	"कै", "lat", "कैयाति")

# P.7.4.14: न कपि — tiG (na kapi)
def apply_7_4_14(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.14", "न कपि (na kapi)", "tiG",
	"कप्", "lat", "कपति")

# P.7.4.15: आपोऽन्यतरस्याम् — tiG (apo-anyatarasyam)
def apply_7_4_15(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.15", "आपोऽन्यतरस्याम् (apo-anyatarasyam)", "tiG",
	"आप्", "lat", "आप्नोति/आप्नाति")

# P.7.4.16: ऋदृशोऽङि गुणः — tiG (guna for f-drz)
def apply_7_4_16(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.16", "ऋदृशोऽङि गुणः (guna for f-drz)", "tiG",
	"दृश्", "lot", "दर्शतु")

# P.7.4.17: अस्यतेस्थुक् — tiG (asya-t-sthuk)
def apply_7_4_17(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.17", "अस्यतेस्थुक् (asya-t-sthuk)", "tiG",
	"अस्", "lat", "अस्ति")

# P.7.4.18: श्वयतेरः — tiG (Svayater-R)
def apply_7_4_18(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.18", "श्वयतेरः (Svayater-R)", "tiG",
	"श्वय", "lat", "श्वयते")

# P.7.4.19: पतः पुम् — tiG (pater-pum)
def apply_7_4_19(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.19", "पतः पुम् (pater-pum)", "tiG",
	"पा", "lat", "पिबति (pum-viśeṣa)")

# P.7.4.20: वच उम् — tiG (vac-Um)
def apply_7_4_20(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.20", "वच उम् (vac-Um)", "tiG",
	"वच्", "lat", "वक्ति/वचति")

# P.7.4.21: शीङः सार्वधातुके गुणः — tiG (SIG-sarvadhAtuke-guna)
def apply_7_4_21(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.21", "शीङः सार्वधातुके गुणः (SIG-guna)", "tiG",
	"शी", "lat", "शिनāti")

# P.7.4.22: अयङ् यि क्ङिति — tiG (ayaG-yi-kNiti)
def apply_7_4_22(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.22", "अयङ् यि क्ङिति (ayaG-yi-kNiti)", "tiG",
	"कृ", "lat-k", "करोति")

# P.7.4.23: उपसर्गाद्ध्रस्व ऊहतेः — tiG (hrasva after upasarga for Uh)
def apply_7_4_23(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.23", "उपसर्गाद्ध्रस्व ऊहतेः (hrasva after upasarga)", "tiG",
	"प्र-ऊह", "lat", "प्रोहति")

# P.7.4.24: एतेर्लिङि — tiG (eteH-liG)
def apply_7_4_24(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.24", "एतेर्लिङि (eteH-liG)", "tiG",
	"ए", "liG", "एतु")

# P.7.4.25: अकृत्सार्वधातुकयोर्दीर्घः — tiG (dIrgha for akRt-sarvadhAtukayoh)
def apply_7_4_25(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.25", "अकृत्सार्वधातुकयोर्दीर्घः (dIrgha akRt)", "tiG",
	"दृञ्", "lat", "दीर्घयति")

# P.7.4.26: च्वौ च — tiG (cvo)
def apply_7_4_26(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.26", "च्वौ च (cvau)", "tiG",
	"बुध्", "cvau", "बुबोधिषते")

# P.7.4.27: रीङ् ऋतः — tiG (rIG-RtaH)
def apply_7_4_27(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.27", "रीङ् ऋतः (rIG-RtaH)", "tiG",
	"सृज्", "lat", "सृजति")

# P.7.4.28: रिङ् शयग्लिङ्क्षु — tiG (riG-Saya-gl-iG-kSu)
def apply_7_4_28(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.28", "रिङ् शयग्लिङ्क्षु (riG-Saya-gl)", "tiG",
	"शी", "lat", "शेते")

# P.7.4.29: गुणोऽर्तिसंयोगाद्योः — tiG (guna for arti-samyoga-adi)
def apply_7_4_29(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.29", "गुणोऽर्तिसंयोगाद्योः (guna arti-samyoga)", "tiG",
	"पत्", "lat", "पतति")

# P.7.4.30: यङि च — tiG (yaGi)
def apply_7_4_30(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.30", "यङि च (yaGi)", "tiG",
	"क्रीड्", "yaG", "क्रीडायते")

# P.7.4.31: ई घ्राध्मोः — tiG (I-ghrA-Dhmoh)
def apply_7_4_31(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.31", "ई घ्राध्मोः (I-ghrA-Dhmoh)", "tiG",
	"घ्रा", "lat", "जिघ्रेति")

# P.7.4.32: अस्य च्वौ — tiG (asya-cvo)
def apply_7_4_32(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.32", "अस्य च्वौ (asya-cvo)", "tiG",
	"अस्", "cvau", "असिष्यते")

# P.7.4.33: क्यचि च — tiG (kyaci)
def apply_7_4_33(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.33", "क्यचि च (kyaci)", "tripadi",
	"पूज्", "lat", "पूजयति")

# P.7.4.34: अशनायोदन्यधनाया बुभुक्षापिपासागर्द्धेषु — tiG
def apply_7_4_34(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.34", "अशनायोदन्यधनाया बुभुक्षापिपासागर्द्धेषु", "tiG",
	"बुभुक्ष", "lat", "बुभुक्षति")

# P.7.4.35: न च्छन्दस्यपुत्रस्य — tiG
def apply_7_4_35(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.35", "न च्छन्दस्यपुत्रस्य (na chandasyaputrasya)", "tiG",
	"अपुत्र", "lat", "अपुत्रकृत्")

# P.7.4.36: दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति — tiG
def apply_7_4_36(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.36", "दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति", "tiG",
	"दुरस्", "lat", "दुरस्यति")

# P.7.4.37: अश्वाघस्यात् — tiG
def apply_7_4_37(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.37", "अश्वाघस्यात् (aSvAGhasya)", "tiG",
	"अश्वाघ", "lat", "अश्वाघति")

# P.7.4.38: देवसुम्नयोर्यजुषि काठके — tiG
def apply_7_4_38(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.38", "देवसुम्नयोर्यजुषि काठके", "tiG",
	"देवसुम्न", "lat", "देवसुम्नयति")

# P.7.4.39: कव्यध्वरपृतनस्यर्चि लोपः — tiG
def apply_7_4_39(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.39", "कव्यध्वरपृतनस्यर्चि लोपः", "tiG",
	"कव्यध्वर", "lat", "कव्यध्वरति")

# P.7.4.40: द्यतिस्यतिमास्थामित्ति किति — tiG
def apply_7_4_40(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.40", "द्यतिस्यतिमास्थामित्ति किति", "tiG",
	"आस्", "lat", "आस्ते")

# P.7.4.41: शाच्छोरन्यतरस्याम् — tiG
def apply_7_4_41(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.41", "शाच्छोरन्यतरस्याम्", "tiG",
	"शाच्छ", "lat", "शाच्छति")

# P.7.4.42: दधातेर्हिः — tiG
def apply_7_4_42(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.42", "दधातेर्हिः (dadhAter-hiH)", "tiG",
	"दध्", "lat", "दधाति")

# P.7.4.43: जहातेश्च क्त्वि — tiG
def apply_7_4_43(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.43", "जहातेश्च क्त्वि (jahAteH-ktvi)", "tiG",
	"हा", "ktv", "जहित्वा")

# P.7.4.44: विभाषा छन्दसि — tiG
def apply_7_4_44(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.44", "विभाषा छन्दसि (vibhASA chandasi)", "tiG",
	"कृ", "lot-ch", "करोतु/करोताम्")

# P.7.4.45: सुधितवसुधितनेमधितधिष्वधिषीय च — tiG
def apply_7_4_45(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.45", "सुधितवसुधितनेमधितधिष्वधिषीय च", "tiG",
	"सु", "lat", "सुनोति")

# P.7.4.46: दो दद् घोः — tiG
def apply_7_4_46(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.46", "दो दद् घोः (dah-ghoh)", "tiG",
	"दह्", "lat", "ददाहि")

# P.7.4.47: अच उपसर्गात्तः — tiG
def apply_7_4_47(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.47", "अच उपसर्गात्तः (aca-upasargAttaH)", "tiG",
	"प्र-क्रम्", "lat", "प्रक्रमते")

# P.7.4.48: अपो भि — tiG
def apply_7_4_48(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.48", "अपो भि (apo-Bi)", "tiG",
	"आप्", "lat", "आप्नोति")

# P.7.4.49: सः स्यार्द्धधातुके — tiG (saH-sya)
def apply_7_4_49(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.49", "सः स्यार्द्धधातुके (saH-sya)", "tiG",
	"सह्", "lat", "सहति")

# P.7.4.50: तासस्त्योर्लोपः — tiG (tAsas-tyor-lopa)
def apply_7_4_50(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.50", "तासस्त्योर्लोपः (tAsas-tyor-lopa)", "tiG",
	"दम्", "lat", "दत्ते")

# P.7.4.51: रि च — tiG (ri-ca)
def apply_7_4_51(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.51", "रि च (ri-ca)", "tiG",
	"कृ", "lat", "करोति")

# P.7.4.52: ह एति — tiG (ha-eti)
def apply_7_4_52(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.52", "ह एति (ha-eti)", "tiG",
	"हा", "lat", "हिनाति")

# P.7.4.53: यीवर्णयोर्दीधीवेव्योः — tiG
def apply_7_4_53(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.53", "यीवर्णयोर्दीधीवेव्योः (yIvarnayor-dIdhIvevyoh)", "tiG",
	"दीधी", "lat", "दीद्धीयति")

# P.7.4.54: सनि मीमाघुरभलभशकपतपदामच इस् — tiG
def apply_7_4_54(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.54", "सनि मीमाघुरभलभशकपतपदामच इस्", "tiG",
	"मीमा", "san", "मीमायिषति")

# P.7.4.55: आप्ज्ञप्यृधामीत् — tiG
def apply_7_4_55(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.55", "आप्ज्ञप्यृधामीत्", "tiG",
	"ज्ञा", "lat", "जानाति")

# P.7.4.56: दम्भ इच्च — tiG
def apply_7_4_56(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.56", "दम्भ इच्च (damB-icca)", "tiG",
	"दम्भ्", "lat", "दम्भति")

# P.7.4.57: मुचोऽकर्मकस्य गुणो वा — tiG
def apply_7_4_57(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.57", "मुचोऽकर्मकस्य गुणो वा (muca-akarma-guna-va)", "tiG",
	"मुच्", "lat", "मुञ्चति/मोचयति")

# P.7.4.58: अत्र लोपोऽभ्यासस्य — tiG
def apply_7_4_58(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.58", "अत्र लोपोऽभ्यासस्य (atra-lopaH-abhyAsasya)", "tiG",
	"दिव्", "lat", "दिनatti")

# P.7.4.59: ह्रस्वः — tiG
def apply_7_4_59(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.59", "ह्रस्वः (hrasvaH)", "tiG",
	"मन्", "lat", "मन्यते")

# P.7.4.60: हलादिः शेषः — tiG
def apply_7_4_60(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.60", "हलादिः शेषः (halAdiH-seSaH)", "tiG",
	"सृज्", "lat", "सर्जति")

# P.7.4.61: शर्पूर्वाः खयः — tiG (SarpurvAH-KhayaH)
def apply_7_4_61(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.61", "शर्पूर्वाः खयः (SarpurvAH-KhayaH)", "tiG",
	"सर्प्", "lat", "सर्पति")

# P.7.4.62: कुहोश्चुः — tiG
def apply_7_4_62(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.62", "कुहोश्चुः (kuhoh-cuH)", "tiG",
	"कुह्", "lat", "कुचति")

# P.7.4.63: न कवतेर्यङि — tiG
def apply_7_4_63(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.63", "न कवतेर्यङि (na kavater-yaGi)", "tiG",
	"कव्", "yaG", "कावयते")

# P.7.4.64: कृषेश्छन्दसि — tiG
def apply_7_4_64(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.64", "कृषेश्छन्दसि (kRSeH-chandasi)", "tiG",
	"कृष्", "lat-ch", "कर्षति")

# P.7.4.65: दाधर्तिदर्धर्तिदर्धर्षिबोभूतुतेतिक्तेऽलर्ष्यापनीफणत्संसनिष्यदत्करिक्रत्कनिक्रदद्भरिभ्रद्दविध्वतोदविद्युतत्तरित्रतःसरीसृपतंवरीवृजन्मर्मृज्यागनीगन्तीति च — tiG
def apply_7_4_65(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.65", "दाधर्तिदर्धर्तिदर्धर्षिबोभूतुतेतिक्तेऽलर्ष्यापनीफणत्संसनिष्यदत्करिक्रत्कनिक्रदद्भरिभ्रद्दविध्वतोदविद्युतत्तरित्रतःसरीसृपतंवरीवृजन्मर्मृज्यागनीगन्तीति च (long vedic list)", "tiG",
	"दाधृ", "lat", "दाधर्ति")

# P.7.4.66: उरत् — tiG (urat)
def apply_7_4_66(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.66", "उरत् (urat)", "tiG",
	"शी", "lat", "शेते")

# P.7.4.67: द्युतिस्वाप्योः सम्प्रसारणम् — tiG
def apply_7_4_67(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.67", "द्युतिस्वाप्योः सम्प्रसारणम्", "tiG",
	"द्युत्", "lat", "द्योतयति")

# P.7.4.68: व्यथो लिटि — tiG
def apply_7_4_68(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.68", "व्यथो लिटि (vyaTo-liTi)", "tiG",
	"व्यथ्", "lit", "व्यथिता")

# P.7.4.69: दीर्घ इणः किति — tiG
def apply_7_4_69(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.69", "दीर्घ इणः किति (dIrgha iNaH-kiti)", "tiG",
	"ई", "lat-k", "ईयति")

# P.7.4.70: अत आदेः — tiG (ata-AdeH)
def apply_7_4_70(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.70", "अत आदेः (ata-AdeH)", "tiG",
	"अत्", "lat", "अत्ति")

# P.7.4.71: तस्मान्नुड् द्विहलः — tiG
def apply_7_4_71(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.71", "तस्मान्नुड् द्विहलः (tasmAn-nuD-dvihalaH)", "tiG",
	"अग्नि", "lat", "अग्निनā")

# P.7.4.72: अश्नोतेश्च — tiG
def apply_7_4_72(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.72", "अश्नोतेश्च (aSnoteH-ca)", "tiG",
	"अश्नु", "lat", "अश्नोति")

# P.7.4.73: भवतेरः — tiG
def apply_7_4_73(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.73", "भवतेरः (Bavater-aH)", "tiG",
	"भू", "lat", "भवति")

# P.7.4.74: ससूवेति निगमे — tiG
def apply_7_4_74(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.74", "ससूवेति निगमे (sasUveti-nigame)", "tiG",
	"सु", "lit-ch", "ससूवे")

# P.7.4.75: निजां त्रयाणां गुणः श्लौ — tiG
def apply_7_4_75(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.75", "निजां त्रयाणां गुणः श्लौ (nijAM-trayANAM-gunaH-Slau)", "tiG",
	"निज", "slu", "निजयते")

# P.7.4.76: भृञामित् — tiG
def apply_7_4_76(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.76", "भृञामित् (BhRJAM-it)", "tiG",
	"भृ", "lat", "भरति")

# P.7.4.77: अर्तिपिपर्त्योश्च — tiG
def apply_7_4_77(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.77", "अर्तिपिपर्त्योश्च (arti-pipartyoH-ca)", "tiG",
	"पृ", "lat", "पिपर्ति")

# P.7.4.78: बहुलं छन्दसि — tiG
def apply_7_4_78(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.78", "बहुलं छन्दसि (bahulaM-chandasi)", "tiG",
	"अस्", "lat-ch", "अस्ति/अस्ताम्")

# P.7.4.79: सन्यतः — tiG
def apply_7_4_79(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.79", "सन्यतः (sanyataH)", "tiG",
	"सम्-कृ", "san", "सङ्करिषति")

# P.7.4.80: ओः पुयण्ज्यपरे — tiG
def apply_7_4_80(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.80", "ओः पुयण्ज्यपरे (oH-pu-yaJ-ja-apare)", "tiG",
	"पु", "lat", "पवति")

# P.7.4.81: स्रवतिशृणोतिद्रवतिप्रवतिप्लवतिच्यवतीनां वा — tiG
def apply_7_4_81(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.81", "स्रवतिशृणोतिद्रवतिप्रवतिप्लवतिच्यवतीनां वा (long vedic list)", "tiG",
	"स्रव्", "lat", "स्रवति")

# P.7.4.82: गुणो यङ्लुकोः — tiG
def apply_7_4_82(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.82", "गुणो यङ्लुकोः (gunaH-yaGlukoH)", "tiG",
	"क्रीड्", "yaG", "क्रीडायते")

# P.7.4.83: दीर्घोऽकितः — tiG
def apply_7_4_83(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.83", "दीर्घोऽकितः (dIrgho-akitaH)", "tiG",
	"अक्", "lat", "अकति")

# P.7.4.84: नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम् — tiG
def apply_7_4_84(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.84", "नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम् (long list)", "tiG",
	"नैग्", "lat", "नैगति")

# P.7.4.85: नुगतोऽनुनासिकान्तस्य — tiG
def apply_7_4_85(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.85", "नुगतोऽनुनासिकान्तस्य (nugato-nunAsikAntasya)", "tiG",
	"सृज्", "lat", "सृजति")

# P.7.4.86: जपजभदहदशभञ्जपशां च — tiG
def apply_7_4_86(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.86", "जपजभदहदशभञ्जपशां च (long list)", "tiG",
	"जप्", "lat", "जपति")

# P.7.4.87: चरफलोश्च — tiG
def apply_7_4_87(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.87", "चरफलोश्च (cara-phaloH-ca)", "tiG",
	"चर्", "lat", "चरति")

# P.7.4.88: उत् परस्यातः — tiG
def apply_7_4_88(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.88", "उत् परस्यातः (ut-parasyAtaH)", "tiG",
	"आत्", "lat", "आत्ते")

# P.7.4.89: ति च — tiG
def apply_7_4_89(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.89", "ति च (ti-ca)", "tiG",
	"कृ", "lat", "करोति")

# P.7.4.90: रीगृदुपधस्य च — tiG
def apply_7_4_90(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.90", "रीगृदुपधस्य च (rIg-Rd-upadhasya-ca)", "tiG",
	"सृज्", "lat", "सर्जति")

# P.7.4.91: रुग्रिकौ च लुकि — tiG
def apply_7_4_91(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.91", "रुग्रिकौ च लुकि (rug-rikau-ca-luki)", "tiG",
	"सृज्", "lat-luk", "सृजतु")

# P.7.4.92: ऋतश्च — tiG
def apply_7_4_92(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.92", "ऋतश्च (RtaH-ca)", "tiG",
	"ऋ", "lat", "ऋणोति")

# P.7.4.93: सन्वल्लघुनि चङ्परेऽनग्लोपे — tiG
def apply_7_4_93(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.93", "सन्वल्लघुनि चङ्परेऽनग्लोपे", "tripadi",
	"सन्वल्", "lat", "सन्वल्लति")

# P.7.4.94: दीर्घो लघोः — tiG
def apply_7_4_94(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.94", "दीर्घो लघोः (dIrgho-laghoH)", "tiG",
	"अल्", "lat", "आलति")

# P.7.4.95: अत् स्मृदॄत्वरप्रथम्रदस्तॄस्पशाम् — tiG
def apply_7_4_95(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.95", "अत् स्मृदॄत्वरप्रथम्रदस्तॄस्पशाम् (long list)", "tiG",
	"स्मृ", "lat", "स्मरति")

# P.7.4.96: विभाषा वेष्टिचेष्ट्योः — tiG
def apply_7_4_96(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.96", "विभाषा वेष्टिचेष्ट्योः (vibhASA-veSTiceSTyoH)", "tiG",
	"वेष्ट्", "lat", "वेष्टयति")

# P.7.4.97: ई च गणः — tiG/taddhita continued
def apply_7_4_97(word, pos=""):
	return _apply_1_1(word, pos, "प.7.4.97", "ई च गणः (I-ca-gaNaH)", "tripadi",
	"ई", "lat", "ईयति")
