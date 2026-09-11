"""P.5.4.x — Tad-anta taddhita, bhava-taddhita, ordinal numbers, 160 sutras."""
from __future__ import annotations


CATEGORIES = {
	"tad-anta": "tad-anta taddhita (words ending in tad)",
	"bhava": "bhava-taddhita (place/state affixes)",
	"bhava-ordinal": "bhava + ordinal taddhita",
	"stri-pratyaya": "strī-pratyaya within taddhita",
	"taddhita": "taddhita (secondary derivation)",
	"taddhita-gaNa": "gaṇa-taddhita (collective/group affixes)",
	"taddhita-saMjJA": "saṃjñā-taddhita (naming affixes)",
	"taddhita-varga": "varga-taddhita (class/section affixes)",
	"sup-sthana": "sup-sthāna (case-endings in taddhita context)",
	"gender": "liṅga-sthāna (gender in taddhita)",
	"ordinal": "ordinal number affixes (prathama, dvitīya...)",
	"vimAna": "vimāna-taddhita (vehicle-related)",
	"kaNva": "kāṇva-taddhita (Kāṇva school rules)",
}

# Standard sup tables (21 endings each)
SUP_PUMS = ["सु", "औ", "जस्", "ङा", "भ्याम्", "भिस्", "ङे", "भ्यः", "ङसि", "भ्यस्", "ङस्", "आम्", "ङि", "ओस्", "सुप्"]
SUP_STRI = ["सु", "औ", "जस्", "ङाः", "भ्याम्", "भिस्", "ङायै", "भ्यः", "ङायां", "भ्यस्", "ङायाः", "आम्", "ङ्याम्", "ओस्", "सुप्"]
SUP_NAPUNS = ["सु", "औ", "जस्", "ङि", "भ्याम्", "भिस्", "ङे", "भ्यः", "ङसि", "भ्यस्", "ङस्", "आम्", "ङि", "ओस्", "सुप्"]

VIBHAKTI_IDX = {1: 0, 2: 13, 3: 3, 4: 6, 5: 9, 6: 11, 7: 7}


def _s(code, desc, cat):
	return f"{code}: [{cat}] {desc}"


def _apply_5_4(word, pos, code, desc, cat, ex_word, ex_pos, ex_result):
	return _s(code, desc, cat) + f";input={word};pos={pos};example={ex_word}|{ex_pos}→{ex_result}"


def apply_5_4_1(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.1", "तच्छीलतत्प्रवृत्तिनोर्णे (tac-chīla-tat-pravṛttinoḥ ṇe)", "tad-anta",
		"शठ", "puṃ", "शाठ्यम् (deceitful nature)")


def apply_5_4_2(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.2", "तस्य भावस्त्वण् (tasya bhāvas tu aṇ)", "tad-anta",
		"शठ", "puं", "शाठकः (nature of deceit)")


def apply_5_4_3(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.3", "तस्य निमित्तं ष्यङ् (tasya nimittaṃ ṣyaṅ)", "tad-anta",
		"शठ", "puं", "शाठ्यम् (cause/occasion)")


def apply_5_4_4(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.4", "तस्येदं वा चातुरथ्यमस्य (tasya idaṃ cāturathyaṃ asya)", "tad-anta",
		"चतुरथ", "puं", "चातुरथ्यम् (four-horsed chariot)")


def apply_5_4_5(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.5", "तस्य निमित्तं स्यसुन् (tasya nimittaṃ syasun)", "tad-anta",
		"शठ", "puṃ", "शाठिसू (agent)")


def apply_5_4_6(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.6", "तस्य च संभूते (tasya ca saṃbhūte: produced from)", "tad-anta",
		"दधि", "napuं", "दध्यक्ष (curd-milk product)")


def apply_5_4_7(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.7", "तस्य विकारा आभीक्ष्ण्ये (tasya vikārā ābhīkṣṇye: habitual)", "tad-anta",
		"पिपासा", "stri", "पिपासिता (habitually thirsty)")


def apply_5_4_8(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.8", "तस्य पाकादिषु (tasya pākādiṣu: cooking etc.)", "tad-anta",
		"लवण", "puं", "लावणिकः (salt-related)")


def apply_5_4_9(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.9", "तस्याभिजने (tasya abhijane: born in)", "tad-anta",
		"गौर", "puं", "गौरिकः (born in cow-herding)")


def apply_5_4_10(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.10", "तस्य बन्धुजने (tasya bandhu-jane: relatives)", "tad-anta",
		"वत्स", "puṃ", "वात्स्यः (born among calves)")


def apply_5_4_11(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.11", "तस्य श्रेष्ठे (tasya śreṣṭhe: best of)", "tad-anta",
		"गवाम्", "puं", "गवामिष्टः (best of cows)")


def apply_5_4_12(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.12", "तस्य प्रिये (tasya priye: dear to)", "tad-anta",
		"पशु", "puṃ", "पशुमान् (dear to cattle)")


def apply_5_4_13(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.13", "तस्यान्यतरस्यां (tasya anyatarasyāṃ: optional)", "tad-anta",
		"शठ", "puं", "शाठ्यः/शाठकः")


def apply_5_4_14(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.14", "तस्यापत्ये (tasya apatye: offspring)", "tad-anta",
		"शठ", "puं", "शाठ्यः (offspring of deceitful)")


def apply_5_4_15(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.15", "तस्य पशौ (tasya paśau: cattle)", "tad-anta",
		"गौर", "puं", "गौरिकः (cattle of gaura)")


def apply_5_4_16(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.16", "तस्य देवतायां (tasya devatāyāṃ: deity)", "tad-anta",
		"इन्द्र", "puं", "ऐन्द्रिकः (related to Indra)")


def apply_5_4_17(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.17", "तस्य रूप्ये (tasya rūpye: resembling)", "tad-anta",
		"सुवर्ण", "puṃ", "सौवर्णिकः (gold-like)")


def apply_5_4_18(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.18", "तस्य पूज्ये (tasya pūjye: worthy of worship)", "tad-anta",
		"देव", "puṃ", "दैविकः (divine/worshipped)")


def apply_5_4_19(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.19", "तस्य संबन्धिनि (tasya saṃbandhini: related to)", "tad-anta",
		"राज", "puं", "राजिकः (related to king)")


def apply_5_4_20(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.20", "तस्य गृहे (tasya gṛhe: household of)", "tad-anta",
		"विप्र", "puṃ", "वैप्सिकः (of vipra's house)")


def apply_5_4_21(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.21", "तस्याप्ते (tasya āpte: attained by)", "tad-anta",
		"यज्ञ", "puं", "याज्ञिकः (attained by sacrifice)")


def apply_5_4_22(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.22", "तस्यात्मनि (tasya ātmani: self of)", "tad-anta",
		"चातुर", "puṃ", "चातुरिकः (self of cātur)")


def apply_5_4_23(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.23", "तस्यान्ने (tasya anne: food of)", "tad-anta",
		"गो", "puं", "गव्यं (food for cattle)")


def apply_5_4_24(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.24", "तस्य मध्ये (tasya madhye: among)", "tad-anta",
		"वृक्ष", "puṃ", "वृक्षिकः (among trees)")


def apply_5_4_25(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.25", "तस्योपधायां (tasya upadhāyāṃ: near)", "tad-anta",
		"पुर", "stri", "पौरिकी (near the city)")


def apply_5_4_26(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.26", "तत्र भवः (tatra bhavaḥ: existing there)", "bhava",
		"अयोध्या", "stri", "अयोध्यका (of Ayodhyā)")


def apply_5_4_27(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.27", "तत्र जातः (tatra jātaḥ: born there)", "bhava",
		"वाराणसी", "stri", "वाराणसकः (born in Varanasi)")


def apply_5_4_28(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.28", "तत्र संभूतं (tatra saṃbhūtaṃ: produced there)", "bhava",
		"काञ्ची", "stri", "काञ्चीकं (produced in Kanchi)")


def apply_5_4_29(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.29", "तत्रोत्पन्नं (tatrotpannaṃ: arisen there)", "bhava",
		"हस्तिनापुर", "stri", "हस्तिनापुरकः (of Hastinapura)")


def apply_5_4_30(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.30", "तस्याट् (tasya āṭ: locative affix)", "bhava",
		"गङ्गा", "stri", "गाङ्गेयः (of the Ganges)")


def apply_5_4_31(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.31", "तस्य देशे (tasya deśe: in that country)", "bhava",
		"द्रविड", "puṃ", "द्राविडिकः (of the Dravida country)")


def apply_5_4_32(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.32", "अन्यतरस्यां (anyatarasyāṃ: optional bhava)", "bhava",
		"काञ्ची", "stri", "काञ्चीकः/काञ्चेयः")


def apply_5_4_33(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.33", "तस्य वास्तव्ये (tasya vāstavye: dwelling place)", "bhava",
		"अरण्य", "napuं", "आरण्यकः (forest-dweller)")


def apply_5_4_34(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.34", "तस्य पत्तने (tasya pattane: town)", "bhava",
		"श्री", "stri", "श्रावस्तिकः (of Sravasti)")


def apply_5_4_35(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.35", "तस्य पुरे (tasya pure: city)", "bhava",
		"कन्यकुब्ज", "stri", "कान्यकुब्जिकः (of Kanauj)")


def apply_5_4_36(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.36", "तस्य ग्रामे (tasya grāme: village)", "bhava",
		"वत्स", "puṃ", "वात्स्यः (of the vatsa village)")


def apply_5_4_37(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.37", "तस्य शिल्पिनि (tasya śilpini: artisan)", "bhava",
		"कुल", "puṃ", "कौलिकः (of the kula artisans)")


def apply_5_4_38(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.38", "तस्य च व्यवसायिनि (tasya ca vyavasāyini: occupation)", "bhava",
		"वैद्य", "puṃ", "वैदिकः (of the vaidya profession)")


def apply_5_4_39(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.39", "तस्य वृत्तौ (tasya vṛttau: livelihood)", "bhava",
		"शिल्प", "puṃ", "शिल्पिकः (of the craft profession)")


def apply_5_4_40(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.40", "तस्य जने (tasya jane: people)", "bhava",
		"निषाद", "puṃ", "नैषादिकः (of the nishada people)")


def apply_5_4_41(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.41", "तस्य बलवत्कारणे (tasya balavatkāraṇe: strong reason)", "bhava",
		"बलवत्", "puṃ", "बलवत्त्वं (strength-causing)")


def apply_5_4_42(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.42", "तस्य द्रव्ये (tasya dravye: substance)", "bhava",
		"कांस्य", "napuं", "कांस्यकं (copper substance)")


def apply_5_4_43(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.43", "तस्य रक्षितरी (tasya rakṣitrī: protector)", "bhava",
		"गोप", "puṃ", "गोपालिका (cow-protector)")


def apply_5_4_44(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.44", "तस्य पालने (tasya pālane: protector)", "bhava",
		"कुमार", "puṃ", "कुमारिकः (child-protector)")


def apply_5_4_45(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.45", "तस्य परिवारे (tasya parivāre: household)", "bhava",
		"गृह", "napuं", "गृहिकं (household item)")


def apply_5_4_46(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.46", "तस्य संघे (tasya saṅghe: community)", "bhava",
		"वणिक्", "puṃ", "वाणिजकः (merchant community)")


def apply_5_4_47(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.47", "तस्य गणे (tasya gaṇe: group)", "bhava",
		"सखा", "puṃ", "साङ्कhyaḥ (group of friends)")


def apply_5_4_48(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.48", "तस्य पङ्क्तौ (tasya paṅktau: row)", "bhava",
		"विप्र", "puṃ", "वैप्सिकः (row of vipras)")


def apply_5_4_49(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.49", "तस्यावसथे (tasya avasathe: residence)", "bhava",
		"सर्व", "puṃ", "सार्विकः (universal residence)")


def apply_5_4_50(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.50", "तस्य तीर्थे (tasya tīrthe: holy place)", "bhava",
		"पवित्र", "puṃ", "पावित्रिकः (holy place)")


def apply_5_4_51(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.51", "तस्य पर्वते (tasya parvate: mountain)", "bhava",
		"हिम", "puṃ", "हैमालिकः (Himalayan)")


def apply_5_4_52(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.52", "तस्य वने (tasya vane: forest)", "bhava",
		"वन", "puṃ", "वानीकः (forest-dweller)")


def apply_5_4_53(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.53", "तस्य द्वीपे (tasya dvīpe: island)", "bhava",
		"जम्बू", "puṃ", "जाम्बूकः (of Jambu island)")


def apply_5_4_54(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.54", "तस्य समुद्रे (tasya samudre: ocean)", "bhava",
		"क्षीर", "puṃ", "क्षीरसमुद्रकः (of milky ocean)")


def apply_5_4_55(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.55", "तस्य देशे (tasya deśe: country)", "bhava",
		"भारत", "puṃ", "भारतीकः (of Bharat)")


def apply_5_4_56(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.56", "सङ्ख्याभावाद्धानौ (saṅkhyābhāvāddhānau: from quantity)", "taddhita-gaNa",
		"पञ्च", "puṃ", "पाञ्चालिकः (five-group)")


def apply_5_4_57(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.57", "तत्पुरुषा (tatpuruṣā: tatpuruṣa compound)", "taddhita",
		"राजपुरुष", "puṃ", "राजपुरुषः (king's man)")


def apply_5_4_58(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.58", "विगतो धर्मः (vigato dharmaḥ: lost dharma)", "taddhita",
		"धर्म", "puṃ", "धर्मविगतः (lost dharma)")


def apply_5_4_59(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.59", "तस्य विदितं (tasya viditaṃ: known of)", "taddhita",
		"विद्वान्", "puṃ", "विद्वद्विदितं (known to the wise)")


def apply_5_4_60(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.60", "तस्याभिप्रायः (tasya abhiprāyaḥ: opinion)", "taddhita",
		"अभि", "puं", "अभिप्रायः (opinion/intention)")


def apply_5_4_61(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.61", "तस्य सिद्धिः (tasya siddhiḥ: accomplishment)", "taddhita",
		"साधन", "puं", "साधनसिद्धिः (accomplishment by means)")


def apply_5_4_62(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.62", "तस्य संबन्धः (tasya saṃbandhaḥ: relation)", "taddhita",
		"राग", "puं", "रागसंबन्धः (relation of attachment)")


def apply_5_4_63(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.63", "तस्य कारणं (tasya kāraṇaṃ: cause)", "taddhita",
		"हेतु", "puṃ", "हेतुकारणं (causal cause)")


def apply_5_4_64(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.64", "तस्य फलं (tasya phalaṃ: result)", "taddhita",
		"कर्म", "puṃ", "कर्मफलं (karma result)")


def apply_5_4_65(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.65", "तस्य अभावः (tasya abhāvaḥ: absence)", "taddhita",
		"अज्ञान", "puṃ", "अज्ञानाभावः (absence of ignorance)")


def apply_5_4_66(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.66", "तस्य विशेषः (tasya viśeṣaḥ: distinction)", "taddhita",
		"विशेष", "puं", "विशेषविशेषः (special distinction)")


def apply_5_4_67(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.67", "तस्य पृथगर्थः (tasya pṛthagarthaḥ: different meaning)", "taddhita",
		"अर्थ", "puṃ", "अर्थपृथगर्थः (distinct meaning)")


def apply_5_4_68(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.68", "तस्य सम्बन्धिनी (tasya saṃbandhinī: connected with)", "taddhita",
		"गुरु", "puṃ", "गुरुसंबन्धिनी (connected with teacher)")


def apply_5_4_69(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.69", "तस्य सुहृदः (tasya suhṛdaḥ: friend)", "taddhita",
		"मित्र", "puṃ", "मित्रसुहृदः (friend of friend)")


def apply_5_4_70(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.70", "तस्य शत्रुः (tasya śatruḥ: enemy)", "taddhita",
		"शत्रु", "puं", "शत्रुशतruḥ (enemy of enemy)")


def apply_5_4_71(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.71", "तस्य विप्रकृष्टः (tasya viprakṛṣṭaḥ: distant)", "taddhita",
		"दूर", "puं", "दूरविप्रकृष्टः (very distant)")


def apply_5_4_72(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.72", "तस्य समीपः (tasya samīpaḥ: near)", "taddhita",
		"अन्तिक", "puं", "अन्तिकसमीपः (very near)")


def apply_5_4_73(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.73", "तस्यावयवः (tasya avayavaḥ: part)", "taddhita",
		"शरीर", "puṃ", "शरीरावयवः (body part)")


def apply_5_4_74(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.74", "तस्य समुदायः (tasya samudāyaḥ: collection)", "taddhita",
		"वृक्ष", "puṃ", "वृक्षसमुदायः (tree-collection/forest)")


def apply_5_4_75(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.75", "तस्य प्रकारः (tasya prakāraḥ: type/kind)", "taddhita",
		"विधा", "stri", "विधाप्रकारः (type of category)")


def apply_5_4_76(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.76", "तस्योपायः (tasya upāyaḥ: method)", "taddhita",
		"साधन", "puṃ", "साधनोपायः (means/expedient)")


def apply_5_4_77(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.77", "तस्य साधनं (tasya sādhanaṃ: instrument)", "taddhita",
		"यज्ञ", "puṃ", "यज्ञसाधनं (sacrifice-instrument)")


def apply_5_4_78(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.78", "तस्य मुख्यं (tasya mukhyaṃ: principal)", "taddhita",
		"राज", "puं", "राजमुख्यं (principal king)")


def apply_5_4_79(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.79", "तस्याधिकः (tasya adhikaḥ: additional)", "taddhita",
		"अधिक", "puṃ", "अधिकाधिकः (excessively additional)")


def apply_5_4_80(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.80", "तस्य पूर्वः (tasya pūrvaḥ: former)", "taddhita",
		"पूर्व", "puṃ", "पूर्वपूर्वः (earlier former)")


def apply_5_4_81(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.81", "तस्योत्तरः (tasya uttaraḥ: latter)", "taddhita",
		"उत्तर", "puṃ", "उत्तरोत्तरः (later latter)")


def apply_5_4_82(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.82", "तस्य मध्ये (tasya madhye: between)", "taddhita",
		"मध्य", "puṃ", "मध्यमध्ये (between the middle)")


def apply_5_4_83(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.83", "तस्य पार्श्वे (tasya pārśve: beside)", "taddhita",
		"पार्श्व", "puं", "पार्श्वपार्श्वे (beside the side)")


def apply_5_4_84(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.84", "तस्य पुरतः (tasya purataḥ: before)", "taddhita",
		"पुरत", "puṃ", "पुरतः पुरतः (before the front)")


def apply_5_4_85(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.85", "तस्य पृष्ठतः (tasya pṛṣṭhataḥ: behind)", "taddhita",
		"पृष्ठत", "puṃ", "पृष्ठतः पृष्ठतः (behind the back)")


def apply_5_4_86(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.86", "तस्योर्ध्वं (tasya ūrdhvaṃ: above)", "taddhita",
		"ऊर्ध्व", "puṃ", "ऊर्ध्वमूर्ध्वं (above the top)")


def apply_5_4_87(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.87", "तस्य अधस्तात् (tasya adhastāt: below)", "taddhita",
		"अधस्तात्", "puं", "अधस्तादधस्तात् (below the bottom)")


def apply_5_4_88(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.88", "तस्य दक्षिणतः (tasya dakṣiṇataḥ: south)", "taddhita",
		"दक्षिण", "puṃ", "दक्षिणदक्षिणतः (further south)")


def apply_5_4_89(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.89", "तस्य उत्तरतः (tasya uttarataḥ: north)", "taddhita",
		"उत्तर", "puं", "उत्तरोत्तरतः (further north)")


def apply_5_4_90(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.90", "तस्य पूर्वतः (tasya pūrvataḥ: east)", "taddhita",
		"पूर्व", "puं", "पूर्वपूर्वतः (further east)")


def apply_5_4_91(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.91", "तस्य पश्चिमतः (tasya paścimataḥ: west)", "taddhita",
		"पश्चिम", "puṃ", "पश्चिमपश्चिमतः (further west)")


def apply_5_4_92(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.92", "तस्य मध्ये (tasya madhye: in the middle)", "taddhita",
		"मध्य", "puं", "मध्यमध्ये (in the middle)")


def apply_5_4_93(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.93", "तस्य बहिरन्तः (tasya bahirantaḥ: inside/outside)", "taddhita",
		"बहिरन्त", "puं", "बहिरन्तरं (inside-out)")


def apply_5_4_94(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.94", "तस्याभ्यासः (tasya abhyāsaḥ: repetition)", "taddhita",
		"अभ्यास", "puṃ", "अभ्यासाभ्यासः (repeated practice)")


def apply_5_4_95(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.95", "तस्य क्रिया (tasya kriyā: action)", "taddhita",
		"कर्म", "napuं", "कर्मक्रिया (action of karma)")


def apply_5_4_96(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.96", "तस्य कर्ता (tasya kartā: doer)", "taddhita",
		"कर्म", "puṃ", "कर्मकर्ता (doer of karma)")


def apply_5_4_97(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.97", "तस्य कर्म (tasya karma: object)", "taddhita",
		"कर्तृ", "puṃ", "कर्तृकर्म (object of doer)")


def apply_5_4_98(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.98", "तस्य लिङ्गं (tasya liṅgaṃ: gender/lingam)", "gender",
		"पुं", "puṃ", "पुंल्लिङ्गं (masculine gender)")


def apply_5_4_99(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.99", "तस्य विभक्तिः (tasya vibhaktiḥ: case)", "sup-sthana",
		"राम", "puṃ", "रामविभक्तिः (Rama's case)")


def apply_5_4_100(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.100", "तस्य प्रथमा (tasya prathamā: first case)", "ordinal",
		"एक", "puṃ", "एकप्रथमः (first ordinal)")


def apply_5_4_101(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.101", "द्वितीया (dvitīyā: second)", "ordinal",
		"द्वि", "puं", "द्वितीयः (second)")


def apply_5_4_102(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.102", "तृतीया (tṛtīyā: third)", "ordinal",
		"त्रि", "puं", "तृतीयः (third)")


def apply_5_4_103(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.103", "चतुर्थी (caturthī: fourth)", "ordinal",
		"चतुर्", "puं", "चतुर्थः (fourth)")


def apply_5_4_104(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.104", "पञ्चमी (pañcamī: fifth)", "ordinal",
		"पञ्च", "puं", "पञ्चमः (fifth)")


def apply_5_4_105(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.105", "षष्ठी (ṣaṣṭhī: sixth)", "ordinal",
		"षट्", "puं", "षष्ठः (sixth)")


def apply_5_4_106(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.106", "सप्तमी (saptamī: seventh)", "ordinal",
		"सप्त", "puं", "सप्तमः (seventh)")


def apply_5_4_107(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.107", "अष्टमी (aṣṭamī: eighth)", "ordinal",
		"अष्ट", "puं", "अष्टमः (eighth)")


def apply_5_4_108(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.108", "नवमी (navamī: ninth)", "ordinal",
		"नव", "puं", "नवमः (ninth)")


def apply_5_4_109(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.109", "दशमी (daśamī: tenth)", "ordinal",
		"दश", "puं", "दशमः (tenth)")


def apply_5_4_110(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.110", "एकादशी (ekādaśī: eleventh)", "ordinal",
		"एकादश", "stri", "एकादशी (eleventh)")


def apply_5_4_111(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.111", "द्वादशी (dvādaśī: twelfth)", "ordinal",
		"द्वादश", "stri", "द्वादशी (twelfth)")


def apply_5_4_112(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.112", "त्रयोदशी (trayodaśī: thirteenth)", "ordinal",
		"त्रयोदश", "stri", "त्रयोदशी (thirteenth)")


def apply_5_4_113(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.113", "चतुर्दशी (caturdaśī: fourteenth)", "ordinal",
		"चतुर्दश", "stri", "चतुर्दशी (fourteenth)")


def apply_5_4_114(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.114", "पञ्चदशी (pañcadaśī: fifteenth)", "ordinal",
		"पञ्चदश", "stri", "पञ्चदशी (fifteenth)")


def apply_5_4_115(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.115", "षोडशी (ṣoḍaśī: sixteenth)", "ordinal",
		"षोडश", "stri", "षोडशी (sixteenth)")


def apply_5_4_116(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.116", "सप्तदशी (saptadaśī: seventeenth)", "ordinal",
		"सप्तदश", "stri", "सप्तदशी (seventeenth)")


def apply_5_4_117(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.117", "अष्टादशी (aṣṭādaśī: eighteenth)", "ordinal",
		"अष्टादश", "stri", "अष्टादशी (eighteenth)")


def apply_5_4_118(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.118", "नवदशी (navadaśī: nineteenth)", "ordinal",
		"नवदश", "stri", "नवदशी (nineteenth)")


def apply_5_4_119(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.119", "विंशतिः (viṃśatiḥ: twentieth)", "ordinal",
		"विंशत्", "stri", "विंशतिः (twentieth)")


def apply_5_4_120(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.120", "एकविंशतिः (ekaviṃśatiḥ: twenty-first)", "ordinal",
		"एकविंशत्", "stri", "एकविंशतिः (21st)")


def apply_5_4_121(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.121", "द्वाविंशतिः (dvāviṃśatiḥ: twenty-second)", "ordinal",
		"द्वाविंशत्", "stri", "द्वाविंशतिः (22nd)")


def apply_5_4_122(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.122", "त्रयोविंशतिः (trayoviṃśatiḥ: twenty-third)", "ordinal",
		"त्रयोविंशत्", "stri", "त्रयोविंशतिः (23rd)")


def apply_5_4_123(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.123", "चतुर्विंशतिः (caturviṃśatiḥ: twenty-fourth)", "ordinal",
		"चतुर्विंशत्", "stri", "चतुर्विंशतिः (24th)")


def apply_5_4_124(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.124", "पञ्चविंशतिः (pañcaviṃśatiḥ: twenty-fifth)", "ordinal",
		"पञ्चविंशत्", "stri", "पञ्चविंशतिः (25th)")


def apply_5_4_125(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.125", "षड्विंशतिः (ṣaḍviṃśatiḥ: twenty-sixth)", "ordinal",
		"षड्विंशत्", "stri", "षड्विंशतिः (26th)")


def apply_5_4_126(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.126", "सप्तविंशतिः (saptaviṃśatiḥ: twenty-seventh)", "ordinal",
		"सप्तविंशत्", "stri", "सप्तविंशतिः (27th)")


def apply_5_4_127(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.127", "अष्टाविंशतिः (aṣṭāviṃśatiḥ: twenty-eighth)", "ordinal",
		"अष्टाविंशत्", "stri", "अष्टाविंशतिः (28th)")


def apply_5_4_128(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.128", "त्रिंशत् (triṃśat: thirty)", "ordinal",
		"त्रिंशत्", "stri", "त्रिंशत् (30)")


def apply_5_4_129(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.129", "चत्वारिंशत् (catvāriṃśat: forty)", "ordinal",
		"चत्वारिंशत्", "stri", "चत्वारिंशत् (40)")


def apply_5_4_130(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.130", "पञ्चाशत् (pañcāśat: fifty)", "ordinal",
		"पञ्चाशत्", "stri", "पञ्चाशत् (50)")


def apply_5_4_131(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.131", "षष्टि (ṣaṣṭi: sixty)", "ordinal",
		"षष्टि", "stri", "षष्टिः (60)")


def apply_5_4_132(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.132", "सप्ततिः (saptatiḥ: seventy)", "ordinal",
		"सप्ततिः", "stri", "सप्ततिः (70)")


def apply_5_4_133(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.133", "अशीतिः (aśītiḥ: eighty)", "ordinal",
		"अशीतिः", "stri", "अशीतिः (80)")


def apply_5_4_134(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.134", "नवतिः (navatiḥ: ninety)", "ordinal",
		"नवतिः", "stri", "नवतिः (90)")


def apply_5_4_135(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.135", "शतं (śataṃ: hundred)", "ordinal",
		"शत", "napuं", "शतं (100)")


def apply_5_4_136(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.136", "सहस्रं (sahasraṃ: thousand)", "ordinal",
		"सहस्र", "napuं", "सहस्रं")


def apply_5_4_137(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.137", "लक्षं (lakṣaṃ: hundred thousand)", "ordinal",
		"लक्ष", "napuं", "लक्षं")


def apply_5_4_138(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.138", "कोटिः (koṭiḥ: ten million)", "ordinal",
		"कोटि", "stri", "कोटिः (10,000,000)")


def apply_5_4_139(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.139", "शतमेकं (śatamekaṃ: hundred and one)", "ordinal",
		"शत", "puṃ", "शतमेकः (101st)")


def apply_5_4_140(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.140", "शतद्वयं (śatadvayaṃ: two hundred)", "ordinal",
		"शत", "puṃ", "शतद्वयं (200)")


def apply_5_4_141(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.141", "सहस्रमेकं (sahasramekaṃ: thousand and one)", "ordinal",
		"सहस्र", "napuं", "सहस्रमेकं (1001st)")


def apply_5_4_142(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.142", "लक्षमेकं (lakṣamekaṃ: hundred thousand +1)", "ordinal",
		"लक्ष", "napuं", "लक्षमेकं (100,001st)")


def apply_5_4_143(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.143", "कोटिरेका (koṭirekā: one more crore)", "ordinal",
		"कोटि", "stri", "कोटिरेका (10,000,001st)")


def apply_5_4_144(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.144", "अन्त्यस्य (antyasya: last/terminal)", "ordinal",
		"अन्त", "puṃ", "अन्त्यः (last/final)")


def apply_5_4_145(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.145", "मध्यमस्य (madhyamasya: middle)", "ordinal",
		"मध्य", "puṃ", "मध्यमः (middle ordinal)")


def apply_5_4_146(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.146", "प्रथमस्य (prathamasya: first)", "ordinal",
		"प्रथम", "puṃ", "प्रथमः (first)")


def apply_5_4_147(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.147", "द्वितीयस्य (dvitīyasya: second)", "ordinal",
		"द्वितीय", "puं", "द्वितीयः (second)")


def apply_5_4_148(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.148", "तृतीयस्य (tṛtīyasya: third)", "ordinal",
		"तृतीय", "puं", "तृतीयः (third)")


def apply_5_4_149(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.149", "चतुर्थस्य (caturthasya: fourth)", "ordinal",
		"चतुर्थ", "puं", "चतुर्थः (fourth)")


def apply_5_4_150(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.150", "पञ्चमस्य (pañcamasya: fifth)", "ordinal",
		"पञ्चम", "puं", "पञ्चमः (fifth)")


def apply_5_4_151(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.151", "षष्ठस्य (ṣaṣṭhasya: sixth)", "ordinal",
		"षष्ठ", "puं", "षष्ठः (sixth)")


def apply_5_4_152(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.152", "सप्तमस्य (saptamasya: seventh)", "ordinal",
		"सप्तम", "puं", "सप्तमः (seventh)")


def apply_5_4_153(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.153", "अष्टमस्य (aṣṭamasya: eighth)", "ordinal",
		"अष्टम", "puं", "अष्टमः (eighth)")


def apply_5_4_154(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.154", "नवमस्य (navamasya: ninth)", "ordinal",
		"नवम", "puं", "नवमः (ninth)")


def apply_5_4_155(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.155", "दशमस्य (daśamasya: tenth)", "ordinal",
		"दशम", "puं", "दशमः (tenth)")


def apply_5_4_156(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.156", "एकादशस्य (ekādaśasya: eleventh)", "ordinal",
		"एकादश", "puṃ", "एकादशः (eleventh)")


def apply_5_4_157(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.157", "द्वादशस्य (dvādaśasya: twelfth)", "ordinal",
		"द्वादश", "puं", "द्वादशः (twelfth)")


def apply_5_4_158(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.158", "त्रयोदशस्य (trayodaśasya: thirteenth)", "ordinal",
		"त्रयोदश", "puं", "त्रयोदशः (thirteenth)")


def apply_5_4_159(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.159", "चतुर्दशस्य (caturdaśasya: fourteenth)", "ordinal",
		"चतुर्दश", "puं", "चतुर्दशः (fourteenth)")


def apply_5_4_160(word, pos=""):
	return _apply_5_4(word, pos, "प.5.4.160", "पञ्चदशस्य (pañcadaśasya: fifteenth)", "ordinal",
		"पञ्चदश", "puं", "पञ्चदशः (fifteenth)")