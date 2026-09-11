"""P.4.2.x shared module — 145 apply_4_2_Z functions for nominal derivation (kṛdanta)."""
from __future__ import annotations

CATEGORIES = {
	"intro": "introductory",
	"gender": "liṅga-sthāna",
	"vibhakti": "vibhakti-sthāna",
	"sup-sthana": "sup-sthāna",
	"taddhita": "taddhita",
	"krt": "kṛdanta",
	"samasa": "samāsa",
}

# Standard sup tables (21 endings each)
SUP_PUMS = ["सु","औ","जस्","ङा","भ्याम्","भिस्","ङे","भ्यः","ङसि","भ्यस्","ङस्","आम्","ङि","ओस्","सुप्"]
SUP_STRI = ["सु","औ","जस्","ङाः","भ्याम्","भिस्","ङायै","भ्यः","ङायां","भ्यस्","ङायाः","आम्","ङ्याम्","ओस्","सुप्"]
SUP_NAPUNS = ["सु","औ","जस्","ङि","भ्याम्","भिस्","ङे","भ्यः","ङसि","भ्यस्","ङस्","आम्","ङि","ओस्","सुप्"]

VIBHAKTI_IDX = {1: 0, 2: 13, 3: 3, 4: 6, 5: 9, 6: 11, 7: 7}

def _s(code, desc, cat):
	return f"{code}: [{cat}] {desc}"

def _apply_4_2(word, pos, code, desc, cat, ex_word, ex_pos, ex_result):
	"""Generic apply: returns category + sutra code + first example result."""
	return _s(code, desc, cat) + f";input={word};pos={pos};example={ex_word}|{ex_pos}->{ex_result}"

def apply_4_2_1(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.1", "तेन रक्तं रागात् (colored by — general kṛt)", "krt",
		"रक्त", "puं", "रक्तः")

def apply_4_2_2(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.2", "लाक्षारोचनाशकलकर्दमाट्ठक् (lākṣā-ādi → ṭhak)", "krt",
		"लाक्षा", "stri", "लाक्षाट्ठक्")

def apply_4_2_3(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.3", "नक्षत्रेण युक्तः कालः (nakṣatra-yukta kṛt)", "krt",
		"युक्त", "puं", "युक्तः")

def apply_4_2_4(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.4", "लुबविशेषे (luk viśeṣa for kṛdanta)", "krt",
		"दृष्ट", "puं", "दृष्टः (luk-viśeṣa)")

def apply_4_2_5(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.5", "संज्ञायां श्रवणाश्वत्थाभ्याम् (saṃjñā śravaṇa-ādi)", "krt",
		"श्रवण", "puं", "श्रवणः")

def apply_4_2_6(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.6", "द्वन्द्वाच्छः (dvandva → śaḥ kṛt)", "krt",
		"अश्वगो", "puं", "अश्वगोशः")

def apply_4_2_7(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.7", "दृष्टं साम (dṛṣṭa-sāma kṛt)", "krt",
		"दृष्ट", "puं", "दृष्टः")

def apply_4_2_8(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.8", "कलेर्ढक् (kaler ḍhak)", "krt",
		"कल", "stri", "कलाढक्")

def apply_4_2_9(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.9", "वामदेवाड्ड्यड्ड्यौ (vāmadevā ḍyaḍḍyau)", "krt",
		"वामदेवा", "stri", "वामदेवाड्ड्यौ")

def apply_4_2_10(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.10", "परिवृतो रथः (parivṛta-ratha kṛt)", "krt",
		"परिवृत", "puं", "परिवृतोरथः")

def apply_4_2_11(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.11", "पाण्डुकम्बलादिनिः (pāṇḍu-kambalādi → niḥ)", "krt",
		"पाण्डुकम्बल", "puं", "पाण्डुकम्बलनिः")

def apply_4_2_12(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.12", "द्वैपवैयाघ्रादञ् (dvaipa-vyāghrād añ)", "krt",
		"द्वैपवैयाघ्र", "puं", "द्वैपवैयाघ्रादञ्")

def apply_4_2_13(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.13", "कौमारापूर्ववचने (kaumārā-pūrva-vacane)", "krt",
		"कौमारा", "stri", "कौमारापूर्ववचने")

def apply_4_2_14(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.14", "तत्रोद्धृतममत्रेभ्यः (tatrod dhṛta-mamatrebhyaḥ)", "krt",
		"तत्रोद्धृत", "puं", "तत्रोद्धृतम्")

def apply_4_2_15(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.15", "स्थण्डिलाच्छयितरि व्रते (sthaṇḍilāt śayitari vrate)", "krt",
		"स्थण्डिल", "puं", "स्थण्डिलात्")

def apply_4_2_16(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.16", "संस्कृतं भक्षाः (saṃskṛta-bhakṣāḥ)", "krt",
		"संस्कृत", "puं", "संस्कृतभक्षाः")

def apply_4_2_17(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.17", "शूलोखाद्यत् (śūla-ukha-ādi → yat)", "krt",
		"शूल", "puं", "शूलयत्")

def apply_4_2_18(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.18", "दध्नष्ठक् (dadhnā ṣṭhak)", "krt",
		"दध्न", "puं", "दध्नष्ठक्")

def apply_4_2_19(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.19", "उदश्वितोऽन्यतरस्याम् (udaśvito 'nyatarasyām)", "krt",
		"उदश्वि", "puं", "उदश्वितः/उदश्विन्")

def apply_4_2_20(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.20", "क्षीराड्ढञ् (kṣīrā ḍhañ)", "krt",
		"क्षीर", "puं", "क्षीराढञ्")

def apply_4_2_21(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.21", "सास्मिन् पौर्णमासीति संज्ञायाम् (saṃjñā pūrṇamāsī)", "krt",
		"पौर्णमासी", "stri", "पौर्णमासी")

def apply_4_2_22(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.22", "आग्रहायण्यश्वत्थाट्ठक् (āgrahāyaṇyaśvattha ṭhak)", "krt",
		"आग्रहायण्यश्वत्थ", "puं", "आग्रहायण्यश्वत्थाट्ठक्")

def apply_4_2_23(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.23", "विभाषा फाल्गुनीश्रवणाकार्त्तिकीचैत्रीभ्यः (vibhāṣā)", "krt",
		"फाल्गुन", "stri", "फाल्गुन्याः")

def apply_4_2_24(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.24", "सास्य देवता (sā asya devatā)", "krt",
		"यज्ञ", "puं", "यज्ञदेवता")

def apply_4_2_25(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.25", "कस्येत् (kasyet kṛt)", "krt",
		"क", "puं", "कस्येत्")

def apply_4_2_26(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.26", "शुक्राद्घन् (śukrāc chan)", "krt",
		"शुक्र", "puं", "शुक्राघन्")

def apply_4_2_27(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.27", "अपोनप्त्रपान्नप्तृभ्यां घः (aponaptra-ādi ghaḥ)", "krt",
		"अपोनप्तृ", "puं", "अपोनप्त्रघः")

def apply_4_2_28(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.28", "छ च (cha ca kṛt)", "krt",
		"पाणि", "puं", "पाणिच्छः")

def apply_4_2_29(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.29", "महेन्द्राद्घाणौ च (mahendrāc chāṇau)", "krt",
		"महेन्द्र", "puं", "महेन्द्राघाणौ")

def apply_4_2_30(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.30", "सोमाट्ट्यण् (somā ṭyaṇ)", "krt",
		"सोम", "puं", "सोमाट्ट्यण्")

def apply_4_2_31(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.31", "वाय्वृतुपित्रुषसो यत् (vāyu-ṛtu-pitṛ-uṣas → yat)", "krt",
		"वायु", "puं", "वायुयत्")

def apply_4_2_32(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.32", "द्यावापृथिवीशुनासीरमरुत्वदग्नीषोमवास्तोष्पतिगृहमेधाच्छ ca (long list → śaḥ)", "krt",
		"द्यावापृथिवी", "puं", "द्यावापृथिवीशः")

def apply_4_2_33(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.33", "अग्नेर्ढक् (agneḥ ḍhak)", "krt",
		"अग्नि", "puं", "अग्नेरढक्")

def apply_4_2_34(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.34", "कालेभ्यो भववत् (kālebhyo bhavavat)", "krt",
		"काल", "puं", "कालभववत्")

def apply_4_2_35(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.35", "महाराजप्रोष्ठपदाट्ठञ् (mahārāja-puṣṭhapada ṭhañ)", "krt",
		"महाराजप्रोष्ठपद", "puं", "महाराजप्रोष्ठपदाट्ठञ्")

def apply_4_2_36(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.36", "पितृव्यमातुलमातामहपितामहाः (kṛdanta list)", "krt",
		"पितृव्य", "puं", "पितृव्यः")

def apply_4_2_37(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.37", "तस्य समूहः (tasya samūhaḥ kṛt)", "krt",
		"समूह", "puं", "समूहः")

def apply_4_2_38(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.38", "भिक्षादिभ्योऽण् (bhikṣādi → aṇ)", "krt",
		"भिक्षा", "stri", "भिक्षाङ्")

def apply_4_2_39(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.39", "गोत्रोक्षोष्ट्रोरभ्रराजराजन्यराजपुत्रवत्समनुष्याजाद्वुञ् (gotra-ādi → vuñ)", "krt",
		"गोत्र", "puं", "गोत्रवुञ्")

def apply_4_2_40(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.40", "केदाराद्यञ् च (kedārādi → yañ ca)", "krt",
		"केदार", "puं", "केदाराद्यञ्")

def apply_4_2_41(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.41", "ठञ् कवचिनश्च (kavacin → ṭhañ)", "krt",
		"कवचिन", "puं", "कवचिन्ठञ्")

def apply_4_2_42(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.42", "ब्राह्मणमाणववाडवाद्यन् (brāhmaṇa-ādi → yan)", "krt",
		"ब्राह्मण", "puं", "ब्राह्मणाद्यन्")

def apply_4_2_43(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.43", "ग्रामजनबन्धुसहायेभ्यः तल् (grāma-ādi → tal)", "krt",
		"ग्राम", "puं", "ग्रामतल्")

def apply_4_2_44(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.44", "अनुदात्तादेरञ् (anudāttād aṇ)", "krt",
		"अनुदात्त", "puं", "अनुदात्तादञ्")

def apply_4_2_45(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.45", "खण्डिकादिभ्यश्च (khaṇḍikādi → aṇ)", "krt",
		"खण्डिका", "stri", "खण्डिकाङ्")

def apply_4_2_46(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.46", "चरणेभ्यो धर्मवत् (caraṇebhyo dharmavat)", "krt",
		"चरण", "puं", "चरणधर्मवत्")

def apply_4_2_47(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.47", "अचित्तहस्तिधेनोष्ठक् (acitta-hasti-dhenu ṣṭhak)", "krt",
		"हस्ति", "puं", "हस्तिष्ठक्")

def apply_4_2_48(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.48", "केशाश्वाभ्यां यञ्छावन्यतरस्याम् (keśa-aśva → yañ-chau)", "krt",
		"केश", "puṃ", "केशयञ्/केशशः")

def apply_4_2_49(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.49", "पाशादिभ्यो यः (pāśādi → yaḥ)", "krt",
		"पाश", "puṃ", "पाशयः")

def apply_4_2_50(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.50", "खलगोरथात् (khala-goratha → kṛt)", "krt",
		"खलगोरथ", "puं", "खलगोरथः")

def apply_4_2_51(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.51", "इनित्रकट्यचश्च (ini-tra-kaṭyacaś ca)", "krt",
		"कटि", "stri", "कटिनित्रकट्यचः")

def apply_4_2_52(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.52", "विषयो देशे (viṣaya deśe kṛt)", "krt",
		"विषय", "puं", "विषयः")

def apply_4_2_53(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.53", "राजन्यादिभ्यो वुञ् (rājanyādi → vuñ)", "krt",
		"राजन्य", "puं", "राजन्यवुञ्")

def apply_4_2_54(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.54", "भौरिक्याद्यैषुकार्यादिभ्यो विधल्भक्तलौ (bhaurikādi → vidhalla-ktau)", "krt",
		"भौरिक", "puं", "भौरिकाद्यैषुकार्यविधल्भक्तलौ")

def apply_4_2_55(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.55", "सोऽस्यादिरिति च्छन्दसः प्रगाथेषु (chandasi pragātheṣu)", "krt",
		"आदि", "puं", "आदिः")

def apply_4_2_56(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.56", "संग्रामे प्रयोजनयोद्धृभ्यः (saṃgrāme prayojanayod dharibhyaḥ)", "krt",
		"संग्राम", "puं", "संग्रामः")

def apply_4_2_57(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.57", "तदस्यां प्रहरणमिति क्रीडायाम् णः (kṛīḍāyām ṇaḥ)", "krt",
		"प्रहरण", "puं", "प्रहरणणः")

def apply_4_2_58(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.58", "घञः साऽस्यां क्रियेति ञः (ghañ → ñaḥ kṛt)", "krt",
		"क्रिया", "stri", "क्रियाञः")

def apply_4_2_59(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.59", "तदधीते तद्वेद (tadadhīte tadveda kṛt)", "krt",
		"वेद", "puं", "वेदः")

def apply_4_2_60(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.60", "क्रतूक्थादिसूत्रान्ताट्ठक् (kratūktha-ādi sūtrānta ṭhak)", "krt",
		"क्रतूक्थ", "puं", "क्रतूक्थाट्ठक्")

def apply_4_2_61(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.61", "क्रमादिभ्यो वुन् (kramādi → vun)", "krt",
		"क्रम", "puं", "क्रमवुन्")

def apply_4_2_62(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.62", "अनुब्राह्मणादिनिः (anu-brāhmaṇādi → niḥ)", "krt",
		"अनुब्राह्मण", "puं", "अनुब्राह्मणनिः")

def apply_4_2_63(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.63", "वसन्तादिभ्यष्ठक् (vasantādi → ṣṭhak)", "krt",
		"वसन्त", "puं", "वसन्ताड्ठक्")

def apply_4_2_64(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.64", "प्रोक्ताल्लुक् (proktāl luk)", "krt",
		"प्रोक्त", "puं", "प्रोक्तः (luk)")

def apply_4_2_65(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.65", "सूत्राच्च कोपधात् (sūtrāc ca kopadhāt)", "krt",
		"सूत्र", "puं", "सूत्रात्")

def apply_4_2_66(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.66", "छन्दोब्राह्मणानि च तद्विषयाणि (chando-brāhmaṇāni)", "krt",
		"छन्दोब्राह्मण", "puं", "छन्दोब्राह्मणानि")

def apply_4_2_67(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.67", "तदस्मिन्नस्तीति देशे तन्नाम्नि (tad-deśa taddhita)", "krt",
		"देश", "puं", "देशः")

def apply_4_2_68(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.68", "तेन निर्वृत्तम् (tena nirvṛtta kṛt)", "krt",
		"निर्वृत्त", "puं", "निर्वृत्तम्")

def apply_4_2_69(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.69", "तस्य निवासः (tasya nivāsaḥ kṛt)", "krt",
		"निवास", "puं", "निवासः")

def apply_4_2_70(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.70", "अदूरभवश्च (adūrabhavaś ca kṛt)", "krt",
		"अदूरभव", "puं", "अदूरभवः")

def apply_4_2_71(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.71", "ओरञ् (oḥ añ)", "krt",
		"ओ", "puं", "ओरञ्")

def apply_4_2_72(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.72", "मतोश्च बह्वजङ्गात् (matoś ca bahvajaṅgāt)", "krt",
		"मतु", "puं", "मतोरञ्")

def apply_4_2_73(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.73", "बह्वचः कूपेषु (bahvacaḥ kūpeṣu kṛt)", "krt",
		"कूप", "puं", "कूपः")

def apply_4_2_74(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.74", "उदक् च विपाशः (udak ca vipāśaḥ)", "krt",
		"उदक्", "puं", "उदक्")

def apply_4_2_75(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.75", "संकलादिभ्यश्च (saṃkalādi → aṇ)", "krt",
		"संकल", "puं", "संकलाङ्")

def apply_4_2_76(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.76", "स्त्रीषु सौवीरसाल्वप्राक्षु (strīṣu sauvīra-sālva-prākṣu)", "gender",
		"स्त्री", "stri", "स्त्री")

def apply_4_2_77(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.77", "सुवास्त्वादिभ्योऽण् (suvāstvādi → aṇ)", "krt",
		"सुवास्तु", "puं", "सुवास्त्वाङ्")

def apply_4_2_78(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.78", "रोणी (roṇī strī)", "gender",
		"रोणी", "stri", "रोणी")

def apply_4_2_79(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.79", "कोपधाच्च (kopadhāc ca kṛt)", "krt",
		"कोपधा", "stri", "कोपधा")

def apply_4_2_80(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.80", "वुञ्छण्कठजिलशेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः (long kṛd-affix list)", "krt",
		"वुज्", "puं", "वुञ्छण्")

def apply_4_2_81(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.81", "जनपदे लुप् (janapade luk)", "krt",
		"जनपद", "puं", "जनपदः (luk)")

def apply_4_2_82(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.82", "वरणादिभ्यश्च (varaṇādi → aṇ)", "krt",
		"वरण", "puं", "वरणाङ्")

def apply_4_2_83(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.83", "शर्कराया वा (śarkarāyā vā kṛt)", "krt",
		"शर्करा", "stri", "शर्करा")

def apply_4_2_84(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.84", "ठक्छौ च (ṭhak-chau)", "krt",
		"स्थल", "puं", "स्थलठक्छौ")

def apply_4_2_85(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.85", "नद्यां मतुप् (nadyāṃ matup)", "krt",
		"नदी", "stri", "नदीमतुप्")

def apply_4_2_86(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.86", "मध्वादिभ्यश्च (madhvādi → aṇ)", "krt",
		"मधु", "puं", "मध्वङ्")

def apply_4_2_87(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.87", "कुमुदनडवेतसेभ्यो ड्मतुप् (kumuda-naḍa-vetasa → ḍmatup)", "krt",
		"कुमुद", "puं", "कुमुदड्मतुप्")

def apply_4_2_88(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.88", "नडशादाड्ड्वलच् (naḍa-śādā ḍvalac)", "krt",
		"नड", "puं", "नडड्ड्वलच्")

def apply_4_2_89(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.89", "शिखाया वलच् (śikhāyā valac)", "krt",
		"शिखा", "stri", "शिखावलच्")

def apply_4_2_90(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.90", "उत्करादिभ्यश्छः (utkarādi → śchaḥ)", "krt",
		"उत्कर", "puं", "उत्करश्छः")

def apply_4_2_91(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.91", "नडादीनां कुक् च (naḍādi kuk ca)", "krt",
		"नड", "puं", "नडकुक्")

def apply_4_2_92(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.92", "शेषे (śeṣe — general/default rule)", "krt",
		"शेष", "puं", "शेषः")

def apply_4_2_93(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.93", "राष्ट्रावारपाराद्घखौ (rāṣṭra-āvara-pārāc chakha)", "krt",
		"राष्ट्र", "puं", "राष्ट्रावारपाराघखौ")

def apply_4_2_94(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.94", "ग्रामाद्यखञौ (grāmād yakhañau)", "krt",
		"ग्राम", "puं", "ग्रामाद्यखञौ")

def apply_4_2_95(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.95", "कत्र्यादिभ्यो ढकञ् (katryādi → ḍhakañ)", "krt",
		"कत्रि", "puं", "कत्र्यादिभ्यो ढकञ्")

def apply_4_2_96(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.96", "कुलकुक्षिग्रीवाभ्यः श्वास्यलंकारेषु (kula-kukṣi-grīvā → śvāsyalaṃkāreṣu)", "krt",
		"कुल", "puं", "कुलकुक्षिग्रीवाः")

def apply_4_2_97(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.97", "नद्यादिभ्यो ढक् (nadyādi → ḍhak)", "krt",
		"नदी", "stri", "नद्याढक्")

def apply_4_2_98(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.98", "दक्षिणापश्चात्पुरसस्त्यक् (dakṣiṇā-paścāt-purasastyak)", "krt",
		"दक्षिण", "stri", "दक्षिणापश्चात्पुरसस्त्यक्")

def apply_4_2_99(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.99", "कापिश्याः ष्फक् (kāpiśyāḥ ṣphak)", "krt",
		"कापिशी", "stri", "कापिशीष्फक्")

def apply_4_2_100(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.100", "रंकोरमनुष्येऽण् च (raṅkoramanuṣye 'ṇ ca)", "krt",
		"रंकु", "puं", "रंकोरमनुष्येऽण्")

def apply_4_2_101(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.101", "द्युप्रागपागुदक्प्रतीचो यत् (dyu-prāg-apāg-udak-pratīco yat)", "krt",
		"द्यु", "puं", "द्युयत्")

def apply_4_2_102(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.102", "कन्थायाष्ठक् (kanthāyā ṣṭhak)", "krt",
		"कन्था", "stri", "कन्थाष्ठक्")

def apply_4_2_103(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.103", "वर्णौ वुक् (varṇau vuk)", "krt",
		"वर्ण", "puं", "वर्णवुक्")

def apply_4_2_104(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.104", "अव्ययात्त्यप् (avyayāt tyap)", "krt",
		"अव्यय", "puं", "अव्ययात्त्यप्")

def apply_4_2_105(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.105", "ऐषमोह्यःश्वसोऽन्यतरस्याम् (aiṣa-mohyaḥ-śvaso 'nyatarasyām)", "krt",
		"ऐषमोह्य", "puं", "ऐषमोह्यः")

def apply_4_2_106(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.106", "तीररूप्योत्तरपदादञ्ञौ (tīra-rūpyottarapād añ-ñau)", "krt",
		"तीर", "puं", "तीरादञ्ञौ")

def apply_4_2_107(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.107", "दिक्पूर्वपदादसंज्ञायां ञः (dik-pūrvapād asaṃjñāyāṃ ñaḥ)", "krt",
		"दिक्पूर्व", "puं", "दिक्पूर्वादञ्")

def apply_4_2_108(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.108", "मद्रेभ्योऽञ् (madrebhyo 'ñ)", "krt",
		"मद्र", "puं", "मद्रेभ्योऽञ्")

def apply_4_2_109(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.109", "उदीच्यग्रामाच्च बह्वचोऽन्तोदात्तात् (udīcya-grāmāc ca)", "krt",
		"उदीचग्राम", "puं", "उदीचग्रामाच्छः")

def apply_4_2_110(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.110", "प्रस्थोत्तरपदपलद्यादिकोपधादण् (prasthottarapada-palady-ādi aṇ)", "krt",
		"प्रस्थ", "puं", "प्रस्थोत्तरपदपलद्यादिकोपधादण्")

def apply_4_2_111(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.111", "कण्वादिभ्यो गोत्रे (kaṇvādi gotre kṛt)", "krt",
		"कण्व", "puं", "कण्वाङ्")

def apply_4_2_112(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.112", "इञश्च (iñaś ca)", "krt",
		"इञ्", "puं", "इञः")

def apply_4_2_113(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.113", "न द्व्यचः प्राच्यभरतेषु (na dvyacaḥ prācyabharateṣu)", "krt",
		"द्व्यच", "puं", "द्व्यचः (na-prācya)")

def apply_4_2_114(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.114", "वृद्धाच्छः (vṛddhāc śaḥ)", "krt",
		"वृद्ध", "puं", "वृद्धाच्छः")

def apply_4_2_115(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.115", "भवतष्ठक्छसौ (bhavata ṣṭhak-chasau)", "krt",
		"भवत्", "puं", "भवतष्ठक्छसौ")

def apply_4_2_116(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.116", "काश्यादिभ्यष्ठञ्ञिठौ (kāśyādi ṭhañ-ñiṭhau)", "krt",
		"काश्य", "puं", "काश्यादिभ्यष्ठञ्")

def apply_4_2_117(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.117", "वाहीकग्रामेभ्यश्च (vāhīka-grāmebhyaś ca)", "krt",
		"वाहीकग्राम", "puं", "वाहीकग्रामेभ्यश्च")

def apply_4_2_118(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.118", "विभाषोशीनरेषु (vibhāṣośīnar eṣu)", "krt",
		"उशीनर", "puं", "उशीनरेषु")

def apply_4_2_119(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.119", "ओर्देशे ठञ् (ordeśe ṭhañ)", "krt",
		"ओर्", "puं", "ओर्देशे ठञ्")

def apply_4_2_120(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.120", "वृद्धात् प्राचाम् (vṛddhāt prācām)", "krt",
		"वृद्ध", "puं", "वृद्धात् प्राचाम्")

def apply_4_2_121(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.121", "धन्वयोपधाद्वुञ् (dhanvayopadhād vuñ)", "krt",
		"धन्वय", "puं", "धन्वयोपधाद्वुञ्")

def apply_4_2_122(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.122", "प्रस्थपुरवहान्ताच्च (prastha-pura-vahāntāc ca)", "krt",
		"प्रस्थ", "puं", "प्रस्थपुरवहान्ताच्च")

def apply_4_2_123(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.123", "रोपधेतोः प्राचाम् (ropadhetoḥ prācām)", "krt",
		"रोप", "puं", "रोपधेतोः")

def apply_4_2_124(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.124", "जनपदतदवध्योश्च (janapada-tadavadhyoś ca)", "krt",
		"जनपद", "puं", "जनपदतदवध्योश्च")

def apply_4_2_125(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.125", "अवृद्धादपि बहुवचनविषयात् (avṛddhād api bahuvacana-viṣayāt)", "krt",
		"अवृद्ध", "puं", "अवृद्धादपि बहुवचनविषयात्")

def apply_4_2_126(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.126", "कच्छाग्निवक्त्रवर्त्तोत्तरपदात् (kaccha-agni-vaktra-vartta-uttarapadāt)", "krt",
		"कच्छाग्नि", "puं", "कच्छाग्निवक्त्रवर्त्तोत्तरपदात्")

def apply_4_2_127(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.127", "धूमादिभ्यश्च (dhūmādi → aṇ)", "krt",
		"धूम", "puं", "धूमाङ्")

def apply_4_2_128(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.128", "नगरात् कुत्सनप्रावीण्ययोः (nagarāt kutsana-prāvīṇyayoḥ)", "krt",
		"नगर", "puं", "नगरात् कुत्सनप्रावीण्ययोः")

def apply_4_2_129(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.129", "अरण्यान्मनुष्ये (araṇyān manuṣye)", "krt",
		"अरण्य", "puं", "अरण्यान्मनुष्ये")

def apply_4_2_130(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.130", "विभाषा कुरुयुगन्धराभ्याम् (vibhāṣā kuru-yugandharābhyām)", "krt",
		"कुरु", "puं", "कुरुविभाषा")

def apply_4_2_131(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.131", "मद्रवृज्योः कन् (madra-vṛjyoḥ kan)", "krt",
		"मद्र", "puं", "मद्रकन्")

def apply_4_2_132(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.132", "कोपधादण् (kopadhād aṇ)", "krt",
		"कोप", "puं", "कोपाङ्")

def apply_4_2_133(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.133", "कच्छादिभ्यश्च (kacchādi → aṇ)", "krt",
		"कच्छ", "puं", "कच्छाङ्")

def apply_4_2_134(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.134", "मनुष्यतत्स्थयोर्वुञ् (manuṣya-tats-thayor vuñ)", "krt",
		"मनुष्यतत्स्थ", "puं", "मनुष्यतत्स्थयोर्वुञ्")

def apply_4_2_135(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.135", "अपदातौ साल्वात् (apadātau sālvaḥ)", "krt",
		"साल्व", "puं", "साल्वात् अपदातौ")

def apply_4_2_136(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.136", "गोयवाग्वोश्च (go-yavāgvoś ca)", "krt",
		"गो", "puं", "गोयवाग्वोश्च")

def apply_4_2_137(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.137", "गर्तोत्तरपदाच्छः (gartottarapād śaḥ)", "krt",
		"गर्त", "puं", "गर्तोत्तरपदाच्छः")

def apply_4_2_138(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.138", "गहादिभ्यश्च (gahādi → aṇ)", "krt",
		"गह", "puं", "गहाङ्")

def apply_4_2_139(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.139", "प्राचां कटादेः (prācāṃ kaṭādeḥ)", "krt",
		"कट", "puं", "कटादेः")

def apply_4_2_140(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.140", "राज्ञः क च (rājñaḥ ka ca)", "krt",
		"राज", "puं", "राज्ञः क च")

def apply_4_2_141(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.141", "वृद्धादकेकान्तखोपधात् (vṛddhād ake-kānta-khopadhāt)", "krt",
		"वृद्ध", "puं", "वृद्धादकेकान्तखोपधात्")

def apply_4_2_142(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.142", "कन्थापलदनगरग्रामहृदोत्तरपदात् (kanthā-palada-nagara-grāma-hṛd uttarapadāt)", "krt",
		"कन्था", "stri", "कन्थापलदनगरग्रामहृदोत्तरपदात्")

def apply_4_2_143(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.143", "पर्वताच्च (parvatāc ca)", "krt",
		"पर्वत", "puं", "पर्वताच्च")

def apply_4_2_144(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.144", "विभाषाऽमनुष्ये (vibhāṣā amanuṣye)", "gender",
		"अमनुष्य", "apuṃ", "अमनुष्यविभाषा")

def apply_4_2_145(word, pos="", SUTRA_TOKEN=""):
	return _apply_4_2(word, pos, "प.4.2.145", "कृकणपर्णाद्भारद्वाजे (kṛkaṇa-parṇādbhāradvāje)", "krt",
		"कृकणपर्ण", "puं", "कृकणपर्णाद्भारद्वाजे")
