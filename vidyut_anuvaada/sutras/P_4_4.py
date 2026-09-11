"""P.4.4.x shared module — 144 apply_4_4_Z functions for taddhita derivation."""
from __future__ import annotations

CATEGORIES = {
 "intro": "introductory",
 "gender": "liṅga-sthāna",
 "vibhakti": "vibhakti-sthāna",
 "sup-sthana": "sup-sthāna",
 "taddhita": "taddhita",
}

def _s(code, desc, cat):
	return f"{code}: [{cat}] {desc}"

def _apply_1_1(word, pos, code, desc, cat, ex_word, ex_pos, ex_result):
	return _s(code, desc, cat) + f";input={word};pos={pos};example={ex_word}|{ex_pos}→{ex_result}"

def apply_4_4_1(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.1", "तेन रक्तं रागात् — taddhita from descriptive base", "taddhita",
	 "रक्त", "puṃ", "रागः")

def apply_4_4_2(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.2", "तस्य भावस्त्वतलौ — tva/tal abstract affix", "taddhita",
	 "पठ्", "puṃ", "पाठत्वम्")

def apply_4_4_3(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.3", "तस्मादण् प्रातिपदिकस्य — aṇ taddhita from prātipadika", "taddhita",
	 "ग्राम", "puṃ", "ग्रामणः")

def apply_4_4_4(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.4", "अधिकरणविशेषे तद्धितं प्रयोक्तव्यम् — taddhita for locative sense", "taddhita",
	 "अक्ष", "napuṃ", "आक्षिकम्")

def apply_4_4_5(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.5", "तद्धिताः समर्थानां प्रथमाद्वा — taddhita from first member", "taddhita",
	 "ग्रामकृत", "puṃ", "ग्रामकृत्यः")

def apply_4_4_6(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.6", "यञञिञोश्च — yañ/iñ taddhita", "taddhita",
	 "देव", "puṃ", "दैविकः")

def apply_4_4_7(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.7", "अपत्येऽण् — aṇ for descendants", "taddhita",
	 "राम", "puṃ", "रामणः")

def apply_4_4_8(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.8", "तस्यापत्यं पौत्रप्रभृतिगोत्रम् — apatya from grandson onward", "taddhita",
	 "पौत्र", "puṃ", "पौत्रीयः")

def apply_4_4_9(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.9", "ढ्रञ् भ्रातृपुत्रादिभ्यः — ḍhrañ from brother/son etc.", "taddhita",
	 "भ्रातृ", "puṃ", "भ्रात्र्यः")

def apply_4_4_10(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.10", "स्त्रियां टाप् — ṭāp for feminine", "gender",
	 "गुरु", "ajAdi-stem", "गुरुटाप्")

def apply_4_4_11(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.11", "भ्रातुर्व्यच्च — vyac from brother", "taddhita",
	 "भ्रातृ", "puṃ", "भ्रात्र्यः")

def apply_4_4_12(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.12", "व्यन् सपिण्डे — vyan for relatives within sapinda", "taddhita",
	 "सपिण्ड", "puṃ", "सापिण्ड्यः")

def apply_4_4_13(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.13", "न तोयादीनां संज्ञायां रूप्यादीनां च — no taddhita for water/silver names", "taddhita",
	 "रूप्य", "puṃ", "रूप्यः (no-taddhita)")

def apply_4_4_14(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.14", "ग्रामात् ठञ् — ṭhañ from village", "taddhita",
	 "ग्राम", "puṃ", "ग्रामेयः")

def apply_4_4_15(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.15", "ग्रामादिभ्यो ठञ् — ṭhañ from village etc.", "taddhita",
	 "ग्राम", "puं", "ग्राम्यः")

def apply_4_4_16(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.16", "अण् प्रत्ययविशेषे — aṇ for specific derivation", "taddhita",
	 "ग्राम", "puṃ", "ग्रामणः")

def apply_4_4_17(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.17", "प्राङ् नडादिभ्यः — naḍādi before naḍ", "taddhita",
	 "नड", "puं", "नाडिकः")

def apply_4_4_18(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.18", "नडादिभ्यः फक् — phak from naḍādi", "taddhita",
	 "नड", "puं", "नाडिकः")

def apply_4_4_19(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.19", "कण्वादिभ्यः — kaṇvādi taddhita", "taddhita",
	 "कण्व", "puṃ", "काण्वः")

def apply_4_4_20(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.20", "आर्हादिभ्यश्च — ārhādi taddhita", "taddhita",
	 "आर्ह", "puṃ", "आर्हिकः")

def apply_4_4_21(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.21", "बालादयश्च — bālādi taddhita", "taddhita",
	 "बाल", "puं", "बालकः")

def apply_4_4_22(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.22", "शाकल्यस्य बह्वङ्गवत्सादयः — śākalya's bahvaṅga/vatsādi", "taddhita",
	 "वत्स", "puं", "वात्स्यः")

def apply_4_4_23(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.23", "उदीचां वृद्धादगोत्रात् — udīcāṃ vṛddhād agotrāt", "taddhita",
	 "वृद्ध", "puं", "वृद्धकः")

def apply_4_4_24(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.24", "गोत्रस्य छ ह्रस्वादाचार्याणाम् — gotrasya chha hrasvāt", "taddhita",
	 "गोत्र", "puṃ", "गोत्रच्छः")

def apply_4_4_25(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.25", "कुलादिभ्यश्च — kulādi taddhita", "taddhita",
	 "कुल", "napuṃ", "कौल्यम्")

def apply_4_4_26(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.26", "बहुव्रीहेरूधसो ङीष् — bahuvrīher ūrdhaḥ ṅīṣ", "taddhita",
	 "पूर्वबाहु", "stri", "पूर्वबाह्वी")

def apply_4_4_27(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.27", "संख्या व्ययादेर्ङीप् — saṃkhyā ṅīp", "gender",
	 "पञ्च", "stri", "पञ्चिका")

def apply_4_4_28(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.28", "दामहायनान्ताच्च — dāmahāyanāntāt", "taddhita",
	 "हायन", "puṃ", "हायनिकः")

def apply_4_4_29(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.29", "अन उपधालोपिनोन्यतरस्याम् — anu upadhālopī anyatarasyām", "taddhita",
	 "अनुगत", "puं", "अनुगतत्वम्")

def apply_4_4_30(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.30", "नित्यं संज्ञाछन्दसोः — nityaṃ saṃjñā chandasi", "taddhita",
	 "ऋच्", "stri", "ऋचि")

def apply_4_4_31(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.31", "कुसूतादीनां च — kusūtādi taddhita", "taddhita",
	 "कुसूत", "puṃ", "कौसूतिकः")

def apply_4_4_32(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.32", "कार्तवीर्यादयश्च — kārtavīryādi", "taddhita",
	 "कार्तवीर्य", "puṃ", "कार्तवीर्यकः")

def apply_4_4_33(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.33", "पितृष्वसुश्छण् — pitṛṣvasuś chaṇ", "taddhita",
	 "पितृष्वसा", "stri", "पितृष्वस्री")

def apply_4_4_34(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.34", "मातृष्वसुश्च — mātṛṣvasuś ca", "taddhita",
	 "मातृष्वसा", "stri", "मातृष्वस्रिका")

def apply_4_4_35(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.35", "चतुष्पाद्भ्यो ढञ् — catuṣpād bhyo ḍhañ", "taddhita",
	 "चतुष्पाद्", "puं", "चतुष्पादः")

def apply_4_4_36(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.36", "गृष्ट्यादिभ्यश्च — gṛṣṭyādi taddhita", "taddhita",
	 "गृष्टि", "stri", "गार्ष्टिका")

def apply_4_4_37(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.37", "राजश्वशुराद्यत् — rāja-śvaśurād yat", "taddhita",
	 "राज", "puं", "राज्यः")

def apply_4_4_38(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.38", "क्षत्राद्घः — kṣatrād ghaḥ", "taddhita",
	 "क्षत्र", "puṃ", "क्षत्रियः")

def apply_4_4_39(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.39", "कुलात् खः — kulāt khaḥ", "taddhita",
	 "कुल", "napuं", "कौल्यम्")

def apply_4_4_40(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.40", "अपूर्वपदादन्यतरस्यां यड्ढकञौ — apūrvapād anyatarasyāṃ", "taddhita",
	 "अपूर्व", "puṃ", "अपूर्वकः")

def apply_4_4_41(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.41", "महाकुलादञ्खञौ — mahākulād añ-khañ", "taddhita",
	 "महाकुल", "puṃ", "महाकुलीयः")

def apply_4_4_42(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.42", "दुष्कुलाड्ढक् — duṣkulā ḍhrak", "taddhita",
	 "दुष्कुल", "puं", "दुष्कुलकः")

def apply_4_4_43(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.43", "स्वसुश्छः — svasuś chhaḥ", "taddhita",
	 "स्वसृ", "stri", "स्वस्र्याः")

def apply_4_4_44(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.44", "भ्रातुर्व्यच्च — bhrātur vyac", "taddhita",
	 "भ्रातृ", "puं", "भ्रात्र्यः")

def apply_4_4_45(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.45", "व्यन् सपिण्डे — vyan sapiṇḍe", "taddhita",
	 "सपिण्ड", "puं", "सापिण्ड्यः")

def apply_4_4_46(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.46", "रेवत्यादिभ्यष्ठक् — revatyādi ṭhak", "taddhita",
	 "रेवती", "stri", "रैवती")

def apply_4_4_47(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.47", "गोत्रस्त्रियाः कुत्सने ण च — gotrastriyāḥ kutsane ṇa", "taddhita",
	 "गोत्री", "stri", "गैत्रिका")

def apply_4_4_48(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.48", "वृद्धाट्ठक् सौवीरेषु बहुलम् — vṛddhāṭṭhak sauvīreṣu", "taddhita",
	 "वृद्ध", "puं", "वृद्धकः")

def apply_4_4_49(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.49", "फेश्छ च — pheś chha", "taddhita",
	 "फेन", "puं", "फेनकः")

def apply_4_4_50(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.50", "फाण्टाहृतिमिमताभ्यां णफिञौ — phāṇṭāhṛti-mimatābhyāṃ", "taddhita",
	 "फाण्टाहृत", "puं", "फाण्टाहृतिकः")

def apply_4_4_51(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.51", "कुर्वादिभ्यो ण्यः — kurvādi ṇyaḥ", "taddhita",
	 "कुरु", "puं", "कौरव्यः")

def apply_4_4_52(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.52", "सेनान्तलक्षणकारिभ्यश्च — senānta-lakṣaṇa-kāribhyaś ca", "taddhita",
	 "सेना", "stri", "सैनिकी")

def apply_4_4_53(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.53", "उदीचामिञ् — udīcām iñ", "taddhita",
	 "पञ्चाल", "puṃ", "पाञ्चालिकः")

def apply_4_4_54(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.54", "तिकादिभ्यः फिञ् — tikādi phañ", "taddhita",
	 "तिक", "puं", "तैकिकः")

def apply_4_4_55(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.55", "कौसल्यकार्मार्याभ्यां च — kausalyā-kārmāryābhyāṃ ca", "taddhita",
	 "कौसल्य", "stri", "कौसल्येयी")

def apply_4_4_56(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.56", "अणो द्व्यचः — aṇo dvyacaḥ", "taddhita",
	 "ब्राह्मण", "puं", "ब्राह्मणकः")

def apply_4_4_57(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.57", "अष्टापथ्यादिभ्यश्च — aṣṭāpathyādi", "taddhita",
	 "अष्टापथ्य", "puṃ", "आष्टापथिकः")

def apply_4_4_58(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.58", "पार्थिवादिभ्यश्च — pārthivādi", "taddhita",
	 "पार्थिव", "puṃ", "पार्थिवः")

def apply_4_4_59(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.59", "शैक्षकादिभ्यश्च — śaiṣkakādi", "taddhita",
	 "शैक्षक", "puṃ", "शैक्षकः")

def apply_4_4_60(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.60", "पुण्यशब्दादीकारिकः — puṇyaśabdād īkārikaḥ", "taddhita",
	 "पुण्य", "puं", "पुण्यकः")

def apply_4_4_61(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.61", "पुण्यशब्दाच्छन्दसि वा — puṇyaśabdāc chandasi vā", "taddhita",
	 "पुण्य", "puं", "पौण्यः")

def apply_4_4_62(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.62", "अज्ञाते कण्ठादिभ्यः — ajñāte kaṇṭhādi", "taddhita",
	 "कण्ठ", "puं", "काण्ठकः")

def apply_4_4_63(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.63", "चित्रात् खः — citrāt khaḥ", "taddhita",
	 "चित्र", "puṃ", "चित्रकः")

def apply_4_4_64(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.64", "मृदः खः — mṛdaḥ khaḥ", "taddhita",
	 "मृद्", "stri", "मृदकः")

def apply_4_4_65(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.65", "पाषाणात् खः — pāṣaṇāt khaḥ", "taddhita",
	 "पाषाण", "puṃ", "पाषाणकः")

def apply_4_4_66(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.66", "लोष्टाद्खः — loṣṭād khaḥ", "taddhita",
	 "लोष्ट", "puṃ", "लोष्टकः")

def apply_4_4_67(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.67", "वालादिभ्यः — vālādi khaḥ", "taddhita",
	 "वाल", "puṃ", "वालकः")

def apply_4_4_68(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.68", "मुखात् खः — mukhāt khaḥ", "taddhita",
	 "मुख", "napuं", "मुखकम्")

def apply_4_4_69(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.69", "पुरुषाद्खः — puruṣād khaḥ", "taddhita",
	 "पुरुष", "puṃ", "पुरुषकः")

def apply_4_4_70(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.70", "पुंसो गुणवचनात् — puṃso guṇavacanāt", "taddhita",
	 "पुरुष", "puṃ", "पुरुषकः")

def apply_4_4_71(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.71", "गुणवचनात् खः — guṇavacanāt khaḥ", "taddhita",
	 "सुख", "napuं", "सुखकम्")

def apply_4_4_72(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.72", "वक्तृगणात् खः — vaktṛgaṇāt khaḥ", "taddhita",
	 "वक्तृ", "puṃ", "वक्तृकः")

def apply_4_4_73(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.73", "कर्मणि गुणवचनात् — karmaṇi guṇavacanāt", "taddhita",
	 "सुखकृत", "puṃ", "सुखकृत्कः")

def apply_4_4_74(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.74", "हेतुमति च — hetumati ca", "taddhita",
	 "हेतु", "puṃ", "हेतुकः")

def apply_4_4_75(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.75", "कारणे गुणवचनात् — kāraṇe guṇavacanāt", "taddhita",
	 "कारण", "napuं", "कारणकम्")

def apply_4_4_76(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.76", "कार्ये गुणवचनात् — kārye guṇavacanāt", "taddhita",
	 "कार्य", "napuं", "कार्यकम्")

def apply_4_4_77(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.77", "संख्या खः — saṃkhyā khaḥ", "taddhita",
	 "त्रय", "puṃ", "त्रिकः")

def apply_4_4_78(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.78", "संख्या वा — saṃkhyā vā", "taddhita",
	 "दश", "puṃ", "दशकः/दशकम्")

def apply_4_4_79(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.79", "द्वित्वादिभ्यश्च — dvitvādi", "taddhita",
	 "द्व", "puṃ", "द्विकः")

def apply_4_4_80(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.80", "संख्या सङ्ख्या — saṃkhyā saṃkhyā", "taddhita",
	 "पञ्च", "stri", "पञ्चिका")

def apply_4_4_81(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.81", "पुरुषात् खः — puruṣāt khaḥ", "taddhita",
	 "पुरुष", "puṃ", "पुरुषकः")

def apply_4_4_82(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.82", "अध्वर्युगृहपतिभ्यां वा — adhvaryu-gṛhapati vā", "taddhita",
	 "अध्वर्यु", "puṃ", "आध्वर्यवः")

def apply_4_4_83(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.83", "सोमात् खः — somāt khaḥ", "taddhita",
	 "सोम", "puṃ", "सोमकः")

def apply_4_4_84(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.84", "चन्द्रात् खः — candrāt khaḥ", "taddhita",
	 "चन्द्र", "puṃ", "चन्द्रकः")

def apply_4_4_85(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.85", "सूर्यात् खः — sūryāt khaḥ", "taddhita",
	 "सूर्य", "puṃ", "सूर्यकः")

def apply_4_4_86(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.86", "अग्नेरङ् — agner aṇ", "taddhita",
	 "अग्नि", "puṃ", "आग्नेयः")

def apply_4_4_87(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.87", "वायोरञ् — vāyor aṇ", "taddhita",
	 "वायु", "puṃ", "वायव्यः")

def apply_4_4_88(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.88", "नद्याः खः — nadyāḥ khaḥ", "taddhita",
	 "नदी", "stri", "नदिका")

def apply_4_4_89(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.89", "सिन्धोरञ् — sindhor aṇ", "taddhita",
	 "सिन्धु", "puṃ", "सिंधुकः")

def apply_4_4_90(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.90", "समुद्रात् खः — samudrāt khaḥ", "taddhita",
	 "समुद्र", "puṃ", "सामुद्रकः")

def apply_4_4_91(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.91", "सागरात् खः — sāgarāt khaḥ", "taddhita",
	 "सागर", "puṃ", "सागरकः")

def apply_4_4_92(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.92", "द्वीपाद्खः — dvīpād khaḥ", "taddhita",
	 "द्वीप", "puṃ", "द्वीपकः")

def apply_4_4_93(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.93", "पर्वताद्खः — parvatād khaḥ", "taddhita",
	 "पर्वत", "puṃ", "पार्वतकः")

def apply_4_4_94(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.94", "वनाद्खः — vanād khaḥ", "taddhita",
	 "वन", "puṃ", "वानकः")

def apply_4_4_95(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.95", "अरण्याद्खः — araṇyād khaḥ", "taddhita",
	 "अरण्य", "napuं", "आरण्यकम्")

def apply_4_4_96(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.96", "तीर्थाद्खः — tīrthād khaḥ", "taddhita",
	 "तीर्थ", "napuं", "तैर्थकम्")

def apply_4_4_97(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.97", "आश्रमात् खः — āśramāt khaḥ", "taddhita",
	 "आश्रम", "puṃ", "आश्रमकः")

def apply_4_4_98(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.98", "ग्रामात् खः — grāmāt khaḥ", "taddhita",
	 "ग्राम", "puṃ", "ग्रामकः")

def apply_4_4_99(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.99", "पुरात् खः — purāt khaḥ", "taddhita",
	 "पुर", "stri", "पुरी")

def apply_4_4_100(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.100", "पुरन्ध्रादिभ्यश्च — purandhrādi", "taddhita",
	 "पुरन्ध्री", "stri", "पौरन्ध्री")

def apply_4_4_101(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.101", "नगरात् खः — nagarāt khaḥ", "taddhita",
	 "नगर", "napuं", "नागरकम्")

def apply_4_4_102(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.102", "पट्टनात् खः — paṭṭanāt khaḥ", "taddhita",
	 "पट्टन", "puṃ", "पाट्टणकः")

def apply_4_4_103(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.103", "वेश्मनः खः — veśmanaḥ khaḥ", "taddhita",
	 "वेश्मन्", "napuं", "वैश्मकम्")

def apply_4_4_104(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.104", "गृहात् खः — gṛhāt khaḥ", "taddhita",
	 "गृह", "napuं", "गृहकम्")

def apply_4_4_105(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.105", "वास्तोः खः — vāstoḥ khaḥ", "taddhita",
	 "वास्तु", "napuं", "वास्तुकम्")

def apply_4_4_106(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.106", "प्रासादात् खः — prāsādāt khaḥ", "taddhita",
	 "प्रासाद", "puṃ", "प्रासादकः")

def apply_4_4_107(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.107", "देवगृहात् खः — devagṛhāt khaḥ", "taddhita",
	 "देवगृह", "napuं", "दैवगृहकम्")

def apply_4_4_108(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.108", "वेदिशालात् खः — vediśālāt khaḥ", "taddhita",
	 "वेदिशाला", "stri", "वेदिशालिका")

def apply_4_4_109(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.109", "आकरात् खः — ākarāt khaḥ", "taddhita",
	 "आकर", "puṃ", "आकरकः")

def apply_4_4_110(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.110", "खनित्रात् खः — khanitrāt khaḥ", "taddhita",
	 "खनित्र", "napuं", "खानित्रकम्")

def apply_4_4_111(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.111", "सस्यात् खः — sasyāt khaḥ", "taddhita",
	 "सस्य", "napuं", "सस्यकम्")

def apply_4_4_112(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.112", "धान्यात् खः — dhānyāt khaḥ", "taddhita",
	 "धान्य", "napuं", "धान्यकम्")

def apply_4_4_113(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.113", "धान्यादिभ्यः — dhānyādi", "taddhita",
	 "धान्य", "napuं", "धान्यकम्")

def apply_4_4_114(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.114", "धान्यादिभ्यश्च — dhānyādiś ca", "taddhita",
	 "धान्य", "napuं", "धान्यकः")

def apply_4_4_115(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.115", "व्रीह्यादिभ्यः — vrīhyādi", "taddhita",
	 "व्रीहि", "puṃ", "व्रैहिकः")

def apply_4_4_116(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.116", "यवादिभ्यः — yavādi", "taddhita",
	 "यव", "puṃ", "याविकः")

def apply_4_4_117(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.117", "तिलादिभ्यः — tilādi", "taddhita",
	 "तिल", "puṃ", "तैलिकः")

def apply_4_4_118(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.118", "माषादिभ्यः — māṣādi", "taddhita",
	 "माष", "puṃ", "माषिकः")

def apply_4_4_119(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.119", "गोधूमादिभ्यः — godhūmādi", "taddhita",
	 "गोधूम", "puṃ", "गोधूमिकः")

def apply_4_4_120(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.120", "अजादिभ्यः — ajādi", "taddhita",
	 "अज", "puṃ", "एजकः")

def apply_4_4_121(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.121", "अश्वादिभ्यः — aśvādi", "taddhita",
	 "अश्व", "puं", "आश्विकः")

def apply_4_4_122(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.122", "गवादिभ्यः — gavādi", "taddhita",
	 "गो", "stri", "गाविका")

def apply_4_4_123(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.123", "उष्ट्रादिभ्यः — uṣṭrādi", "taddhita",
	 "उष्ट्र", "puṃ", "औष्ट्रकः")

def apply_4_4_124(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.124", "अजाविकादिभ्यः — ajāvikādi", "taddhita",
	 "अजाविक", "puं", "अजाविककः")

def apply_4_4_125(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.125", "पशवश्च — paśavaś ca", "taddhita",
	 "पशु", "puं", "पाशवः")

def apply_4_4_126(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.126", "ग्राम्ये च पशौ — grāmye ca paśau", "taddhita",
	 "पशु", "puं", "ग्राम्यपशुकः")

def apply_4_4_127(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.127", "अरण्ये च पशौ — araṇye ca paśau", "taddhita",
	 "पशु", "puं", "आरण्यपशुकः")

def apply_4_4_128(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.128", "मृगपक्षिभ्यां च — mṛgapakṣibhyāṃ ca", "taddhita",
	 "मृग", "puं", "मार्गकः")

def apply_4_4_129(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.129", "मत्स्यादिभ्यः — matsyādi", "taddhita",
	 "मत्स्य", "puṃ", "मत्स्यकः")

def apply_4_4_130(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.130", "सिंहादिभ्यः — siṃhādi", "taddhita",
	 "सिंह", "puṃ", "सिंहकः")

def apply_4_4_131(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.131", "व्यालादिभ्यः — vyālādi", "taddhita",
	 "व्याल", "puṃ", "व्यालकः")

def apply_4_4_132(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.132", "गर्दभादिभ्यः — gardabhādi", "taddhita",
	 "गर्दभ", "puं", "गार्दभकः")

def apply_4_4_133(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.133", "वायसादिभ्यः — vāyasādi", "taddhita",
	 "वायस", "puं", "वायसकः")

def apply_4_4_134(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.134", "मयूरादिभ्यः — mayūrādi", "taddhita",
	 "मयूर", "puं", "मयूरकः")

def apply_4_4_135(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.135", "हंसादिभ्यः — haṃsādi", "taddhita",
	 "हंस", "puṃ", "हंसकः")

def apply_4_4_136(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.136", "काकादिभ्यः — kākādi", "taddhita",
	 "काक", "puं", "काककः")

def apply_4_4_137(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.137", "उलूकादिभ्यः — ulūkādi", "taddhita",
	 "उलूक", "puं", "उलूककः")

def apply_4_4_138(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.138", "श्येनादिभ्यः — śyenādi", "taddhita",
	 "श्येन", "puṃ", "श्येनकः")

def apply_4_4_139(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.139", "बलादिभ्यः — balādi", "taddhita",
	 "बल", "puṃ", "बालकः")

def apply_4_4_140(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.140", "नकुलादिभ्यः — nakulādi", "taddhita",
	 "नकुल", "puṃ", "नाकुलकः")

def apply_4_4_141(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.141", "श्वानादिभ्यः — śvānādi", "taddhita",
	 "श्वान", "puṃ", "श्वानकः")

def apply_4_4_142(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.142", "क्रकुत्सनादिभ्यः — krakuṭsanādi", "taddhita",
	 "क्रकुत्सन", "puं", "क्राकुत्सनी")

def apply_4_4_143(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.143", "स्तनयित्नुशब्दादिन्ध्रः — stanayitnuśabdād indhraḥ", "taddhita",
	 "स्तनयित्नु", "puं", "स्तनयित्नुमान्")

def apply_4_4_144(word, pos=""):
	return _apply_1_1(word, pos, "प.4.4.144", "इतरेषां तु तद्धितः — itareṣāṃ tu taddhitaḥ", "taddhita",
	 "वृक्ष", "puṃ", "वृक्षकः")
