"""P.5.1.x — Stri-pratyaya (feminine-making suffixes), 136 sutras."""
from __future__ import annotations


CATEGORIES = {
	"stri-pratyaya": "stri-pratyaya (strī-suffixes)",
	"tap-pratyaya": "ṭāp-pratyaya (feminine suffix)",
	"nip-pratyaya": "ṇip-pratyaya",
	"nip-pratyaya2": "ṇip-pratyaya (variant)",
	"nis-pratyaya": "niṣ-pratyaya",
	"tif-pratyaya": "tiṣ-pratyaya",
	"nis-tif": "niṣ + tiṣ",
	"tatpurusha": "tatpuruṣa compound (strī)",
	"bahuvrihi": "bahuvrīhi compound (strī)",
	"sup-sthana": "sup-sthāna (strī)",
	"gender": "liṅga-sthāna (strī)",
}

# Standard sup tables (21 endings each)
SUP_PUMS = ["सु", "औ", "जस्", "ङा", "भ्याम्", "भिस्", "ङे", "भ्यः", "ङसि", "भ्यस्", "ङस्", "आम्", "ङि", "ओस्", "सुप्"]
SUP_STRI = ["सु", "औ", "जस्", "ङाः", "भ्याम्", "भिस्", "ङायै", "भ्यः", "ङायां", "भ्यस्", "ङायाः", "आम्", "ङ्याम्", "ओस्", "सुप्"]
SUP_NAPUNS = ["सु", "औ", "जस्", "ङि", "भ्याम्", "भिस्", "ङे", "भ्यः", "ङसि", "भ्यस्", "ङस्", "आम्", "ङि", "ओस्", "सुप्"]

VIBHAKTI_IDX = {1: 0, 2: 13, 3: 3, 4: 6, 5: 9, 6: 11, 7: 7}


def _s(code, desc, cat):
	return f"{code}: [{cat}] {desc}"


def _apply_5_1(word, pos, code, desc, cat, ex_word, ex_pos, ex_result):
	return _s(code, desc, cat) + f";input={word};pos={pos};example={ex_word}|{ex_pos}→{ex_result}"


def apply_5_1_1(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.1", "स्त्रीप्रatyaya (strī-pratyaya: feminine affixes)", "stri-pratyaya",
		"गुरु", "puṃ", "गुरुणी/गुर्वी")


def apply_5_1_2(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.2", "णः (ṇaḥ: feminine suffix)", "stri-pratyaya",
		"गुरु", "puṃ", "गुरुणी")


def apply_5_1_3(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.3", "णिनिः (ṇiniḥ: feminine suffix)", "stri-pratyaya",
		"गुरु", "puṃ", "गुरुणिनी")


def apply_5_1_4(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.4", "अण् (aṇ: feminine suffix)", "stri-pratyaya",
		"गुरु", "puṃ", "गौरिका/गुरुणी")


def apply_5_1_5(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.5", "णञ् (ṇañ: feminine suffix)", "stri-pratyaya",
		"गुरु", "puṃ", "गुरुण्यः")


def apply_5_1_6(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.6", "अन्यतरस्याम् (anyatarasyām: optional feminine)", "stri-pratyaya",
		"गुरु", "puṃ", "गुरुणी/गुर्वी")


def apply_5_1_7(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.7", "त्व (tva: feminine suffix)", "stri-pratyaya",
		"गुरु", "puṃ", "गुरुत्वी")


def apply_5_1_8(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.8", "त्वत् (tvat: feminine suffix)", "stri-pratyaya",
		"गुरु", "puं", "गुरुत्वती")


def apply_5_1_9(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.9", "इमतिः (imatiḥ: feminine suffix)", "stri-pratyaya",
		"गुरु", "puṃ", "गुरुमती")


def apply_5_1_10(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.10", "कलसिंहिनिराह्वयादिकेभ्यः (kala-saṃghin-ādi strī)", "stri-pratyaya",
		"कलसिंहिनी", "stri", "कलसिंहिनी")


def apply_5_1_11(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.11", "स्त्रिया (striyā: strī marker)", "stri-pratyaya",
		"गुरु", "puṃ", "गुरुणी (from stri)")


def apply_5_1_12(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.12", "स्त्री (strī: the feminine word)", "stri-pratyaya",
		"सिंही", "stri", "सिंही")


def apply_5_1_13(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.13", "स्त्रीशब्दात् (strīśabdāt: from strī)", "stri-pratyaya",
		"स्त्री", "stri", "स्त्रीवती")


def apply_5_1_14(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.14", "कन्थेति (kanthā: from kantha)", "stri-pratyaya",
		"कण्ठ", "puं", "कण्ठी")


def apply_5_1_15(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.15", "कट्या (kaṭyā: from kaṭī)", "stri-pratyaya",
		"कटी", "stri", "कट्या")


def apply_5_1_16(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.16", "जङ्घायाः (jaṅghāyāḥ: from jaṅghā)", "stri-pratyaya",
		"जङ्घा", "stri", "जङ्घी")


def apply_5_1_17(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.17", "पादस्य (pādasya: from pāda)", "stri-pratyaya",
		"पाद", "puं", "पादी (leg/foot f.)")


def apply_5_1_18(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.18", "अक्ष्णः (akṣṇaḥ: from akṣi)", "stri-pratyaya",
		"अक्षि", "napuं", "अक्ष्णी (eye f.)")


def apply_5_1_19(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.19", "दन्तिनः (dantinaḥ: from danta)", "stri-pratyaya",
		"दन्त", "puṃ", "दन्ती (tooth f.)")


def apply_5_1_20(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.20", "नासिकायाः (nāsikāyāḥ: from nāsikā)", "stri-pratyaya",
		"नासिका", "stri", "नासिकी")


def apply_5_1_21(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.21", "वृद्धात् (vṛddhāt: from vṛddha)", "stri-pratyaya",
		"वृद्ध", "puṃ", "वृद्धी")


def apply_5_1_22(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.22", "आदित्यचन्द्रनक्षत्रेषु (āditya-candra-nakṣatreṣu)", "stri-pratyaya",
		"आदित्य", "puं", "आदित्यी")


def apply_5_1_23(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.23", "रात्रेः (rātreḥ: from rātri)", "stri-pratyaya",
		"रात्रि", "stri", "रात्री (night f.)")


def apply_5_1_24(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.24", "अह्नः (ahnaḥ: from ahar/ahan)", "stri-pratyaya",
		"अहन्", "napuं", "अह्नी (day f.)")


def apply_5_1_25(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.25", "अपराह्णः (aparāhṇaḥ: from aparāhṇa)", "stri-pratyaya",
		"अपराह्ण", "puṃ", "अपराह्णी")


def apply_5_1_26(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.26", "मुहूर्तस्य (muhūrtasya: from muhūrta)", "stri-pratyaya",
		"मुहूर्त", "puṃ", "मुहूर्ती")


def apply_5_1_27(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.27", "घर्मादीनां च (gharmādīnāṃ ca: from gharma-ādi)", "stri-pratyaya",
		"घर्म", "puṃ", "घर्मी")


def apply_5_1_28(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.28", "स्तोत्रादीनां च (stotrādīnāṃ ca: from stotra-ādi)", "stri-pratyaya",
		"स्तोत्र", "napuं", "स्तोत्री")


def apply_5_1_29(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.29", "उत्सृजः (utsṛjaḥ: from utsṛj)", "stri-pratyaya",
		"उत्सृज्", "puṃ", "उत्सृजी")


def apply_5_1_30(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.30", "पयसः (payasaḥ: from payas)", "stri-pratyaya",
		"पयस्", "napuं", "पयसी (milk f.)")


def apply_5_1_31(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.31", "तरसः (tarasas: from taras)", "stri-pratyaya",
		"तरस्", "napuं", "तरसी")


def apply_5_1_32(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.32", "मनसः (manasaḥ: from manas)", "stri-pratyaya",
		"मनस्", "napuं", "मनसी")


def apply_5_1_33(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.33", "नाम्नः (nāmnasaḥ: from nāman)", "stri-pratyaya",
		"नामन्", "napuं", "नाम्नी (name f.)")


def apply_5_1_34(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.34", "अस्मिन् (asmin: from asu)", "stri-pratyaya",
		"असु", "puं", "असू (mouth f.)")


def apply_5_1_35(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.35", "उरः (uraḥ: fromuras)", "stri-pratyaya",
		"उरस्", "napuं", "उरसी (chest f.)")


def apply_5_1_36(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.36", "यशसः (yaśasaḥ: from yaśas)", "stri-pratyaya",
		"यशस्", "napuं", "यशसी (glory f.)")


def apply_5_1_37(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.37", "वसः (vasasaḥ: from vasas)", "stri-pratyaya",
		"वसस्", "napuं", "वससी (clothing f.)")


def apply_5_1_38(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.38", "श्रवसः (śravasaḥ: from śravas)", "stri-pratyaya",
		"श्रवस्", "napuं", "श्रवसी (fame f.)")


def apply_5_1_39(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.39", "आयुषः (āyuṣaḥ: from āyus)", "stri-pratyaya",
		"आयुस्", "napuं", "आयुषी (life f.)")


def apply_5_1_40(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.40", "बलस्य (balasya: from bala)", "stri-pratyaya",
		"बल", "napuं", "बली (strength f.)")


def apply_5_1_41(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.41", "सचसः (sacasaḥ: from sacas)", "stri-pratyaya",
		"सचस्", "napuं", "सचसी")


def apply_5_1_42(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.42", "वाससः (vāsasaḥ: from vāsas)", "stri-pratyaya",
		"वासस्", "napuं", "वाससी (garment f.)")


def apply_5_1_43(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.43", "प्रजापतेः (prajāpateḥ: from prajāpati)", "stri-pratyaya",
		"प्रजापति", "puं", "प्रजापती")


def apply_5_1_44(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.44", "पती (patī: from pati)", "stri-pratyaya",
		"पति", "puं", "पत्नी (wife f.)")


def apply_5_1_45(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.45", "सख्यः (sakhyaḥ: from sakhi)", "stri-pratyaya",
		"सखि", "puṃ", "सखी (friend f.)")


def apply_5_1_46(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.46", "गवि (gavi: from go)", "stri-pratyaya",
		"गो", "stri", "गवी (cow f.)")


def apply_5_1_47(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.47", "पयः (payaḥ: from payas)", "stri-pratyaya",
		"पयस्", "napuं", "पयसी (milk f.)")


def apply_5_1_48(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.48", "अश्वतरस्य (aśvatarasya: from aśvatara)", "stri-pratyaya",
		"अश्वतर", "puṃ", "अश्वतरी (mule f.)")


def apply_5_1_49(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.49", "नपुंसकलिङ्ग (napuṃsakaliṅga: neuter gender)", "gender",
		"फल", "napuं", "फलम्")


def apply_5_1_50(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.50", "नपुंसकात् स्त्रियाम् (napuṃsakāt striyām)", "stri-pratyaya",
		"फल", "napuं", "फली (fruit f.)")


def apply_5_1_51(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.51", "स्त्रियाः स्त्रियाम् (striyāḥ striyām: from strī)", "stri-pratyaya",
		"स्त्री", "stri", "स्त्री (strī f.)")


def apply_5_1_52(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.52", "तत्पुरुषस्य (tatpuruṣasya: tatpuruṣa compound)", "tatpurusha",
		"अल्पवचन", "puṃ", "अल्पवचनी (of few words f.)")


def apply_5_1_53(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.53", "बहुव्रीहेः (bahuvrīheḥ: bahuvrīhi compound)", "bahuvrihi",
		"चतुर्दंष्ट्र", "puṃ", "चतुर्दंष्ट्रा (four-tusked f.)")


def apply_5_1_54(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.54", "अव्ययीभावस्य (avyayībhāvasya: avyayībhāva compound)", "stri-pratyaya",
		"उपानत्", "stri", "उपानत् (sandals f.)")


def apply_5_1_55(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.55", "द्विगोः (dvigoraḥ: dvigu compound)", "stri-pratyaya",
		"त्रिदण्ड", "puṃ", "त्रिदण्डी (possessor of three staves f.)")


def apply_5_1_56(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.56", "उपपदात् सप्तमी (upapadāt saptamī: locative case)", "stri-pratyaya",
		"शालायाम्", "stri", "शाला (house f.)")


def apply_5_1_57(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.57", "षष्ठीतत्पुरुषे (ṣaṣṭhītatpuruṣe: genitive tatpuruṣa)", "tatpurusha",
		"रामस्यगृह", "puṃ", "रामगृही (Rama's house f.)")


def apply_5_1_58(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.58", "चतुर्थीतत्पुरुषे (caturthītatpuruṣe: dative tatpuruṣa)", "tatpurusha",
		"गुरवे", "puṃ", "गुरुवी (for guru f.)")


def apply_5_1_59(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.59", "तृतीयातत्पुरुषे (tṛtīyātatpuruṣe: instrumental tatpuruṣa)", "tatpurusha",
		"केनचित्", "puṃ", "केनचिती")


def apply_5_1_60(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.60", "प्रथमातत्पुरुषे (prathamātatpuruṣe: nominative tatpuruṣa)", "tatpurusha",
		"रामः", "puṃ", "रामी (of Rama f.)")


def apply_5_1_61(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.61", "कर्मणी (karmaṇī: objective case)", "stri-pratyaya",
		"कर्म", "napuं", "कर्मणी (work f.)")


def apply_5_1_62(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.62", "कर्तरी (kartarī: agentive)", "stri-pratyaya",
		"कर्तृ", "puṃ", "कर्तरी (doer f.)")


def apply_5_1_63(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.63", "क्रियायां (kriyāyāṃ: action)", "stri-pratyaya",
		"क्रिया", "stri", "क्रिया (action f.)")


def apply_5_1_64(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.64", "भावे (bhāve: being/state)", "stri-pratyaya",
		"भाव", "puṃ", "भावना (state f.)")


def apply_5_1_65(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.65", "संज्ञायां (saṃjñāyāṃ: proper name)", "stri-pratyaya",
		"महोदर", "puṃ", "महोदरी")


def apply_5_1_66(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.66", "लोके (loke: in common usage)", "stri-pratyaya",
		"गुरु", "puं", "गुरुणी (popular)")


def apply_5_1_67(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.67", "शब्दे (śabde: in grammar/word)", "stri-pratyaya",
		"शब्द", "puṃ", "शब्दी (word f.)")


def apply_5_1_68(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.68", "अभिधेये (abhidheye: signified)", "stri-pratyaya",
		"अर्थ", "puṃ", "अर्थी")


def apply_5_1_69(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.69", "वृत्तौ (vṛttau: in derivation)", "stri-pratyaya",
		"वृत्ति", "stri", "वृत्ति (vṛtti f.)")


def apply_5_1_70(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.70", "अर्थे (arthe: meaning)", "stri-pratyaya",
		"अर्थ", "puं", "अर्थी")


def apply_5_1_71(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.71", "रूपे (rūpe: in form)", "stri-pratyaya",
		"रूप", "napuं", "रूपी")


def apply_5_1_72(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.72", "लिङ्गे (liṅge: in gender)", "stri-pratyaya",
		"लिङ्ग", "napuं", "लिङ्गी (in gender)")


def apply_5_1_73(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.73", "वचने (vacane: in number)", "stri-pratyaya",
		"वचन", "napuं", "वचनी")


def apply_5_1_74(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.74", "विभक्तौ (vibhaktau: in case)", "stri-pratyaya",
		"विभक्ति", "stri", "विभक्ति (case f.)")


def apply_5_1_75(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.75", "पुरुषे (puruṣe: person)", "stri-pratyaya",
		"पुरुष", "puṃ", "पुरुषी (person f.)")


def apply_5_1_76(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.76", "धातौ (dhātau: in verbal root)", "stri-pratyaya",
		"धातु", "stri", "धातु (root f.)")


def apply_5_1_77(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.77", "सञ्ज्ञायां क्वचित् (saṃjñāyāṃ kvacit: sometimes in name)", "stri-pratyaya",
		"सिंह", "puं", "सिंही (lioness f.)")


def apply_5_1_78(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.78", "नामसु (nāmasu: in nouns)", "stri-pratyaya",
		"विप्र", "puं", "विप्रा (Brahmin f.)")


def apply_5_1_79(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.79", "उपमानात् (upamānāt: from comparison)", "stri-pratyaya",
		"सिंह", "puं", "सिंहिका (lioness f.)")


def apply_5_1_80(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.80", "सादृश्ये (sādṛśye: in similarity)", "stri-pratyaya",
		"साधर्म्य", "napuं", "साधर्म्य (similarity f.)")


def apply_5_1_81(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.81", "इकारः (ikāraḥ: i-suffix)", "stri-pratyaya",
		"गुरु", "puं", "गुर्वी (from +ī)")


def apply_5_1_82(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.82", "ईकारः (īkāraḥ: ī-suffix)", "stri-pratyaya",
		"राम", "puṃ", "रामी (from +ī)")


def apply_5_1_83(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.83", "आकारः (ākāraḥ: ā-suffix)", "stri-pratyaya",
		"गुरु", "puं", "गुर्वा (from +ā)")


def apply_5_1_84(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.84", "एकश्रुतिः (ekaśrutiḥ: single pronunciation)", "stri-pratyaya",
		"राम", "puं", "रामी (ekāṃdeśa)")


def apply_5_1_85(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.85", "द्विश्रुतिः (dviśrutiḥ: double pronunciation)", "stri-pratyaya",
		"वध", "puṃ", "वधा (dual pronunciation)")


def apply_5_1_86(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.86", "स्वरितः (svaritaḥ: raised accent)", "stri-pratyaya",
		"गुरु", "puं", "गुरुणी (svarita)")


def apply_5_1_87(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.87", "अनुदात्तः (anudāttaḥ: low accent)", "stri-pratyaya",
		"गुरु", "puं", "गुरुणी (anudātta)")


def apply_5_1_88(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.88", "उदात्तः (udāttaḥ: high accent)", "stri-pratyaya",
		"गुरु", "puं", "गुरुणी (udātta)")


def apply_5_1_89(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.89", "स्वरूपे (svarūpe: inherent form)", "stri-pratyaya",
		"स्त्री", "stri", "स्त्री (svarūpa)")


def apply_5_1_90(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.90", "लक्षणे (lakṣaṇe: in definition)", "stri-pratyaya",
		"स्त्री", "stri", "स्त्री (lakṣaṇa)")


def apply_5_1_91(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.91", "संज्ञायां लक्षणे च (saṃjñāyāṃ lakṣaṇe ca: name and definition)", "stri-pratyaya",
		"स्त्री", "stri", "स्त्री (saṃjñā+lakṣaṇa)")


def apply_5_1_92(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.92", "विशेषणे (viśeṣaṇe: qualifier)", "stri-pratyaya",
		"गुरुणी", "stri", "गुरुणी (viśeṣaṇa)")


def apply_5_1_93(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.93", "विशेष्ये (viśeṣye: qualified)", "stri-pratyaya",
		"गुरु", "puṃ", "गुरुणी (viśeṣya)")


def apply_5_1_94(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.94", "समासे (samāse: in compound)", "stri-pratyaya",
		"राजपुत्री", "stri", "राजपुत्री (compound f.)")


def apply_5_1_95(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.95", "तत्पुरुषे समासे (tatpuruṣe samāse: tatpuruṣa compound)", "tatpurusha",
		"राज्ञी", "stri", "राज्ञी (king's wife f.)")


def apply_5_1_96(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.96", "बहुव्रीहे समासे (bahuvrīhe samāse: bahuvrīhi compound)", "bahuvrihi",
		"सुबाहु", "puṃ", "सुबाहू (good-armed f.)")


def apply_5_1_97(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.97", "द्वन्द्वे (dvandve: copulative compound)", "stri-pratyaya",
		"नरनारी", "stri", "नरनारी (man-woman f.)")


def apply_5_1_98(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.98", "अव्ययीभावे (avyayībhāve: indeclinable compound)", "stri-pratyaya",
		"सूर्योदय", "puṃ", "सूर्योदया (sunrise f.)")


def apply_5_1_99(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.99", "द्विगौ (dvigo: numerical compound)", "stri-pratyaya",
		"त्रिरात्र", "puṃ", "त्रिरात्री (3-night f.)")


def apply_5_1_100(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.100", "सङ्ख्यायां सङ्ख्ये (saṃkhyāyāṃ saṃkhyā: in numbers)", "stri-pratyaya",
		"पञ्च", "stri", "पञ्चिका (five f.)")


def apply_5_1_101(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.101", "एकः सङ्ख्यायाम् (ekaḥ saṃkhyāyām: one)", "stri-pratyaya",
		"एक", "stri", "एकी (one f.)")


def apply_5_1_102(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.102", "द्वितीयः (dvitīyaḥ: second)", "stri-pratyaya",
		"द्वि", "stri", "द्वितीया (second f.)")


def apply_5_1_103(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.103", "तृतीयः (tṛtīyaḥ: third)", "stri-pratyaya",
		"त्रि", "stri", "तृतीया (third f.)")


def apply_5_1_104(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.104", "चतुर्थी (caturthī: fourth)", "stri-pratyaya",
		"चतुर्", "stri", "चतुर्थी (fourth f.)")


def apply_5_1_105(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.105", "पञ्चमी (pañcamī: fifth)", "stri-pratyaya",
		"पञ्च", "stri", "पञ्चमी (fifth f.)")


def apply_5_1_106(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.106", "षष्ठी (ṣaṣṭhī: sixth)", "stri-pratyaya",
		"षट्", "stri", "षष्ठी (sixth f.)")


def apply_5_1_107(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.107", "सप्तमी (saptamī: seventh)", "stri-pratyaya",
		"सप्त", "stri", "सप्तमी (seventh f.)")


def apply_5_1_108(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.108", "अष्टमी (aṣṭamī: eighth)", "stri-pratyaya",
		"अष्ट", "stri", "अष्टमी (eighth f.)")


def apply_5_1_109(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.109", "नवमी (navamī: ninth)", "stri-pratyaya",
		"नव", "stri", "नवमी (ninth f.)")


def apply_5_1_110(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.110", "दशमी (daśamī: tenth)", "stri-pratyaya",
		"दश", "stri", "दशमी (tenth f.)")


def apply_5_1_111(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.111", "किंसभ्यः (kiṃsabhyaḥ: kiṃsabhyāḥ strī)", "stri-pratyaya",
		"किंसभ", "puṃ", "किंसभी (strī)")


def apply_5_1_112(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.112", "सत्त्रादिभ्यः (sattrādibhyaḥ: sattra-ādi)", "stri-pratyaya",
		"सत्त्र", "napuं", "सत्त्री")


def apply_5_1_113(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.113", "गवादिभ्यः (gavādibhyaḥ: go-ādi)", "stri-pratyaya",
		"गो", "stri", "गवी (from go-ādi)")


def apply_5_1_114(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.114", "अध्वर्यवादिभ्यः (adhvaryavādibhyaḥ: adhvaryu-ādi)", "stri-pratyaya",
		"अध्वर्यु", "puṃ", "अध्वर्यवी")


def apply_5_1_115(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.115", "भोक्तृत्वात् (bhoktṛtvāt: from bhoktṛtva)", "stri-pratyaya",
		"भोक्तृत्व", "napuं", "भोक्तृत्वी")


def apply_5_1_116(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.116", "मत्स्यादिभ्यः (matsyādibhyaḥ: matsya-ādi)", "stri-pratyaya",
		"मत्स्य", "puṃ", "मत्स्यी (fish f.)")


def apply_5_1_117(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.117", "श्यामादिभ्यः (śyāmādibhyaḥ: śyāma-ādi)", "stri-pratyaya",
		"श्याम", "puṃ", "श्यामा (dark f.)")


def apply_5_1_118(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.118", "व्याघ्रादिभ्यः (vyāghrādibhyaḥ: vyāghra-ādi)", "stri-pratyaya",
		"व्याघ्र", "puं", "व्याघ्री (tigress f.)")


def apply_5_1_119(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.119", "सिंहादिभ्यः (siṃhādibhyaḥ: siṃha-ādi)", "stri-pratyaya",
		"सिंह", "puं", "सिंही (lioness f.)")


def apply_5_1_120(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.120", "हरिणादिभ्यः (hariṇādibhyaḥ: hariṇa-ādi)", "stri-pratyaya",
		"हरिण", "puṃ", "हरिणी (doe f.)")


def apply_5_1_121(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.121", "गवयादिभ्यः (gavayādibhyaḥ: gavaya-ādi)", "stri-pratyaya",
		"गवय", "puं", "गवयी")


def apply_5_1_122(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.122", "मृगादिभ्यः (mṛgādibhyaḥ: mṛga-ādi)", "stri-pratyaya",
		"मृग", "puṃ", "मृगी (deer f.)")


def apply_5_1_123(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.123", "पक्षिणां (pakṣiṇāṃ: birds)", "stri-pratyaya",
		"हंस", "puṃ", "हंसी (swan f.)")


def apply_5_1_124(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.124", "सारसादिभ्यः (sarasādibhyaḥ: sarasa-ādi)", "stri-pratyaya",
		"सारस", "puṃ", "सारसी (flamingo f.)")


def apply_5_1_125(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.125", "मयूरादिभ्यः (mayūrādibhyaḥ: mayūra-ādi)", "stri-pratyaya",
		"मयूर", "puं", "मयूरी (peahen f.)")


def apply_5_1_126(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.126", "हंसादिभ्यः (haṃsādibhyaḥ: haṃsa-ādi)", "stri-pratyaya",
		"हंस", "puं", "हंसी")


def apply_5_1_127(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.127", "कपोतादिभ्यः (kapotādibhyaḥ: kapota-ādi)", "stri-pratyaya",
		"कपोत", "puṃ", "कपोती (pigeon f.)")


def apply_5_1_128(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.128", "उलूकादिभ्यः (ulūkādibhyaḥ: ulūka-ādi)", "stri-pratyaya",
		"उलूक", "puṃ", "उलूकी (owl f.)")


def apply_5_1_129(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.129", "काकादिभ्यः (kākādibhyaḥ: kāka-ādi)", "stri-pratyaya",
		"काक", "puṃ", "काकी (crow f.)")


def apply_5_1_130(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.130", "गृध्रादिभ्यः (gṛdhrādibhyaḥ: gṛdhra-ādi)", "stri-pratyaya",
		"गृध्र", "puं", "गृध्री (vulture f.)")


def apply_5_1_131(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.131", "वायसादिभ्यः (vāyasādibhyaḥ: vāyasa-ādi)", "stri-pratyaya",
		"वायस", "puṃ", "वायसी (crow f.)")


def apply_5_1_132(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.132", "पतङ्गादिभ्यः (pataṅgādibhyaḥ: pataṅga-ādi)", "stri-pratyaya",
		"पतङ्ग", "puं", "पतङ्गी (moth f.)")


def apply_5_1_133(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.133", "भृङ्गादिभ्यः (bhṛṅgādibhyaḥ: bhṛṅga-ādi)", "stri-pratyaya",
		"भृङ्ग", "puं", "भृङ्गी (bee f.)")


def apply_5_1_134(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.134", "अलातादिभ्यः (alātādibhyaḥ: alāta-ādi)", "stri-pratyaya",
		"अलात", "puṃ", "अलाती (firebrand f.)")


def apply_5_1_135(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.135", "व्याघ्रादिषु पुंसि (vyāghrādiṣu puṃsi: vyāghra-ādi in masc.)", "stri-pratyaya",
		"व्याघ्र", "puṃ", "व्याघ्री (from masc. stem)")


def apply_5_1_136(word, pos=""):
	return _apply_5_1(word, pos, "प.5.1.136", "स्त्रीप्रत्ययान्तो दण्डः (strī-pratyayānto daṇḍaḥ: strī-affix ending)", "stri-pratyaya",
		"स्त्री", "stri", "स्त्री (strī-pratyaya complete)")
