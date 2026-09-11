"""P.5.2.x shared module — 140 apply_5_2_Z functions for taddhita derivations."""
from __future__ import annotations

CATEGORIES = {
	"intro": "taddhita-intro",
	"taddhita": "taddhita",
	"mat": "mat-vat-in",
	"vat": "mat-vat-in",
	"in": "mat-vat-in",
}


def _s(code, desc, cat):
	return f"{code}: [{cat}] {desc}"


def _apply(word, pos, code, desc, cat, ex_word, ex_pos, ex_result):
	return _s(code, desc, cat) + f";input={word};pos={pos};example={ex_word}|{ex_pos}->{ex_result}"


def apply_5_2_1(word, pos=""):
	return _apply(word, pos, "प.5.2.1", "धान्यानां भवने क्षेत्रे खञ्", "intro",
	"धान्य", "puं", "धान्यक्षेत्रं")


def apply_5_2_2(word, pos=""):
	return _apply(word, pos, "प.5.2.2", "व्रीहिशाल्योर्ढक्", "intro",
	"धान्य", "puं", "धान्यक्षेत्रं")


def apply_5_2_3(word, pos=""):
	return _apply(word, pos, "प.5.2.3", "यवयवकषष्टिकाद्यत्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_4(word, pos=""):
	return _apply(word, pos, "प.5.2.4", "विभाषा तिलमाषोमाभङ्गाऽणुभ्यः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_5(word, pos=""):
	return _apply(word, pos, "प.5.2.5", "सर्वचर्मणः कृतः खखञौ", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_6(word, pos=""):
	return _apply(word, pos, "प.5.2.6", "यथामुखसंमुखस्य दर्शनः खः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_7(word, pos=""):
	return _apply(word, pos, "प.5.2.7", "तत्सर्वादेः पथ्यङ्गकर्मपत्रपात्रं व्याप्नोति", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_8(word, pos=""):
	return _apply(word, pos, "प.5.2.8", "आप्रपदं प्राप्नोति", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_9(word, pos=""):
	return _apply(word, pos, "प.5.2.9", "अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_10(word, pos=""):
	return _apply(word, pos, "प.5.2.10", "परोवरपरम्परपुत्रपौत्रमनुभवति", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_11(word, pos=""):
	return _apply(word, pos, "प.5.2.11", "अवारपारात्यन्तानुकामं गामी", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_12(word, pos=""):
	return _apply(word, pos, "प.5.2.12", "समांसमां विजायते", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_13(word, pos=""):
	return _apply(word, pos, "प.5.2.13", "अद्यश्वीनाऽवष्टब्धे", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_14(word, pos=""):
	return _apply(word, pos, "प.5.2.14", "आगवीनः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_15(word, pos=""):
	return _apply(word, pos, "प.5.2.15", "अनुग्वलंगामी", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_16(word, pos=""):
	return _apply(word, pos, "प.5.2.16", "अध्वनो यत्खौ", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_17(word, pos=""):
	return _apply(word, pos, "प.5.2.17", "अभ्यमित्राच्छ च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_18(word, pos=""):
	return _apply(word, pos, "प.5.2.18", "गोष्ठात् खञ् भूतपूर्वे", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_19(word, pos=""):
	return _apply(word, pos, "प.5.2.19", "अश्वस्यैकाहगमः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_20(word, pos=""):
	return _apply(word, pos, "प.5.2.20", "शालीनकौपीने अधृष्टाकार्ययोः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_21(word, pos=""):
	return _apply(word, pos, "प.5.2.21", "व्रातेन जीवति", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_22(word, pos=""):
	return _apply(word, pos, "प.5.2.22", "साप्तपदीनं सख्यम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_23(word, pos=""):
	return _apply(word, pos, "प.5.2.23", "हैयंगवीनं संज्ञायाम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_24(word, pos=""):
	return _apply(word, pos, "प.5.2.24", "तस्य पाकमूले पील्वादिकर्णादिभ्यः कुणब्जाहचौ", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_25(word, pos=""):
	return _apply(word, pos, "प.5.2.25", "पक्षात्तिः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_26(word, pos=""):
	return _apply(word, pos, "प.5.2.26", "तेन वित्तश्चुञ्चुप्चणपौ", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_27(word, pos=""):
	return _apply(word, pos, "प.5.2.27", "विनञ्भ्यां नानाञौ नसह", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_28(word, pos=""):
	return _apply(word, pos, "प.5.2.28", "वेः शालच्छङ्कटचौ", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_29(word, pos=""):
	return _apply(word, pos, "प.5.2.29", "सम्प्रोदश्च कटच्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_30(word, pos=""):
	return _apply(word, pos, "प.5.2.30", "अवात् कुटारच्च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_31(word, pos=""):
	return _apply(word, pos, "प.5.2.31", "नते नासिकायाः संज्ञायां टीटञ्नाटज्भ्रटचः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_32(word, pos=""):
	return _apply(word, pos, "प.5.2.32", "नेर्बिडज्बिरीसचौ", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_33(word, pos=""):
	return _apply(word, pos, "प.5.2.33", "इनच्पिटच्चिकचि च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_34(word, pos=""):
	return _apply(word, pos, "प.5.2.34", "उपाधिभ्यां त्यकन्नासन्नारूढयोः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_35(word, pos=""):
	return _apply(word, pos, "प.5.2.35", "कर्मणि घटोऽठच्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_36(word, pos=""):
	return _apply(word, pos, "प.5.2.36", "तदस्य संजातं तारकादिभ्य इतच्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_37(word, pos=""):
	return _apply(word, pos, "प.5.2.37", "प्रमाणे द्वयसज्दघ्नञ्मात्रचः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_38(word, pos=""):
	return _apply(word, pos, "प.5.2.38", "पुरुषहस्तिभ्यामण् च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_39(word, pos=""):
	return _apply(word, pos, "प.5.2.39", "यद्तदेतेभ्यः परिमाणे वतुप्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_40(word, pos=""):
	return _apply(word, pos, "प.5.2.40", "किमिदंभ्यां वो घः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_41(word, pos=""):
	return _apply(word, pos, "प.5.2.41", "किमः संख्यापरिमाणे डति च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_42(word, pos=""):
	return _apply(word, pos, "प.5.2.42", "संख्याया अवयवे तयप्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_43(word, pos=""):
	return _apply(word, pos, "प.5.2.43", "द्वित्रिभ्यां तयस्यायज्वा", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_44(word, pos=""):
	return _apply(word, pos, "प.5.2.44", "उभादुदात्तो नित्यम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_45(word, pos=""):
	return _apply(word, pos, "प.5.2.45", "तदस्मिन्नधिकमिति दशान्ताड्डः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_46(word, pos=""):
	return _apply(word, pos, "प.5.2.46", "शदन्तविंशतेश्च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_47(word, pos=""):
	return _apply(word, pos, "प.5.2.47", "संख्याया गुणस्य निमाने मयट्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_48(word, pos=""):
	return _apply(word, pos, "प.5.2.48", "तस्य पूरणे डट्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_49(word, pos=""):
	return _apply(word, pos, "प.5.2.49", "नान्तादसंख्यादेर्मट्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_50(word, pos=""):
	return _apply(word, pos, "प.5.2.50", "थट् चच्छन्दसि", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_51(word, pos=""):
	return _apply(word, pos, "प.5.2.51", "षट्कतिकतिपयचतुरां थुक्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_52(word, pos=""):
	return _apply(word, pos, "प.5.2.52", "बहुपूगगणसंघस्य तिथुक्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_53(word, pos=""):
	return _apply(word, pos, "प.5.2.53", "वतोरिथुक्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_54(word, pos=""):
	return _apply(word, pos, "प.5.2.54", "द्वेस्तीयः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_55(word, pos=""):
	return _apply(word, pos, "प.5.2.55", "त्रेः सम्प्रसारणम् च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_56(word, pos=""):
	return _apply(word, pos, "प.5.2.56", "विंशत्यादिभ्यस्तमडन्यतरस्याम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_57(word, pos=""):
	return _apply(word, pos, "प.5.2.57", "नित्यं शतादिमासार्धमाससंवत्सराच्च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_58(word, pos=""):
	return _apply(word, pos, "प.5.2.58", "षष्ट्यादेश्चासंख्यादेः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_59(word, pos=""):
	return _apply(word, pos, "प.5.2.59", "मतौ छः सूक्तसाम्नोः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_60(word, pos=""):
	return _apply(word, pos, "प.5.2.60", "अध्यायानुवाकयोर्लुक्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_61(word, pos=""):
	return _apply(word, pos, "प.5.2.61", "विमुक्तादिभ्योऽण्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_62(word, pos=""):
	return _apply(word, pos, "प.5.2.62", "गोषदादिभ्यो वुन्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_63(word, pos=""):
	return _apply(word, pos, "प.5.2.63", "तत्र कुशलः पथः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_64(word, pos=""):
	return _apply(word, pos, "प.5.2.64", "आकर्षादिभ्यः कन्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_65(word, pos=""):
	return _apply(word, pos, "प.5.2.65", "धनहिरण्यात् कामे", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_66(word, pos=""):
	return _apply(word, pos, "प.5.2.66", "स्वाङ्गेभ्यः प्रसिते", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_67(word, pos=""):
	return _apply(word, pos, "प.5.2.67", "उदराट्ठगाद्यूने", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_68(word, pos=""):
	return _apply(word, pos, "प.5.2.68", "सस्येन परिजातः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_69(word, pos=""):
	return _apply(word, pos, "प.5.2.69", "अंशं हारी", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_70(word, pos=""):
	return _apply(word, pos, "प.5.2.70", "तन्त्रादचिरापहृते", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_71(word, pos=""):
	return _apply(word, pos, "प.5.2.71", "ब्राह्मणकोष्णिके संज्ञायाम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_72(word, pos=""):
	return _apply(word, pos, "प.5.2.72", "शीतोष्णाभ्यां कारिणि", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_73(word, pos=""):
	return _apply(word, pos, "प.5.2.73", "अधिकम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_74(word, pos=""):
	return _apply(word, pos, "प.5.2.74", "अनुकाभिकाभीकः कमिता", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_75(word, pos=""):
	return _apply(word, pos, "प.5.2.75", "पार्श्वेनान्विच्छति", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_76(word, pos=""):
	return _apply(word, pos, "प.5.2.76", "अयःशूलदण्डाजिनाभ्यां ठक्ठञौ", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_77(word, pos=""):
	return _apply(word, pos, "प.5.2.77", "तावतिथं ग्रहणमिति लुग्वा", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_78(word, pos=""):
	return _apply(word, pos, "प.5.2.78", "स एषां ग्रामणीः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_79(word, pos=""):
	return _apply(word, pos, "प.5.2.79", "शृङ्खलमस्य बन्धनं करभे", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_80(word, pos=""):
	return _apply(word, pos, "प.5.2.80", "उत्क उन्मनाः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_81(word, pos=""):
	return _apply(word, pos, "प.5.2.81", "कालप्रयोजनाद्रोगे", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_82(word, pos=""):
	return _apply(word, pos, "प.5.2.82", "तदस्मिन्नन्नं प्राये संज्ञायाम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_83(word, pos=""):
	return _apply(word, pos, "प.5.2.83", "कुल्माषादञ्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_84(word, pos=""):
	return _apply(word, pos, "प.5.2.84", "श्रोत्रियंश्छन्दोऽधीते", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_85(word, pos=""):
	return _apply(word, pos, "प.5.2.85", "श्राद्धमनेन भुक्तमिनिठनौ", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_86(word, pos=""):
	return _apply(word, pos, "प.5.2.86", "पूर्वादिनिः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_87(word, pos=""):
	return _apply(word, pos, "प.5.2.87", "सपूर्वाच्च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_88(word, pos=""):
	return _apply(word, pos, "प.5.2.88", "इष्टादिभ्यश्च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_89(word, pos=""):
	return _apply(word, pos, "प.5.2.89", "छन्दसि परिपन्थिपरिपरिणौ पर्यवस्थातरि", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_90(word, pos=""):
	return _apply(word, pos, "प.5.2.90", "अनुपद्यन्वेष्टा", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_91(word, pos=""):
	return _apply(word, pos, "प.5.2.91", "साक्षाद्द्रष्टरि संज्ञायाम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_92(word, pos=""):
	return _apply(word, pos, "प.5.2.92", "क्षेत्रियच् परक्षेत्रे चिकित्स्यः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_93(word, pos=""):
	return _apply(word, pos, "प.5.2.93", "इन्द्रियमिन्द्रलिंगमिन्द्रदृष्टमिन्द्रसृष्टमिन्द्रजुष्टमिन्द्रदत्तमिति वा", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_94(word, pos=""):
	return _apply(word, pos, "प.5.2.94", "तदस्यास्त्यस्मिन्निति मतुप्", "mat",
	"धन", "puं", "धनवान्")


def apply_5_2_95(word, pos=""):
	return _apply(word, pos, "प.5.2.95", "रसादिभ्यश्च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_96(word, pos=""):
	return _apply(word, pos, "प.5.2.96", "प्राणिस्थादातो लजन्यतरस्याम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_97(word, pos=""):
	return _apply(word, pos, "प.5.2.97", "सिध्मादिभ्यश्च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_98(word, pos=""):
	return _apply(word, pos, "प.5.2.98", "वत्सांसाभ्यां कामबले", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_99(word, pos=""):
	return _apply(word, pos, "प.5.2.99", "फेनादिलच् च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_100(word, pos=""):
	return _apply(word, pos, "प.5.2.100", "लोमादिपामादिपिच्छादिभ्यः शनेलचः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_101(word, pos=""):
	return _apply(word, pos, "प.5.2.101", "प्रज्ञाश्रद्धार्चाभ्यो णः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_102(word, pos=""):
	return _apply(word, pos, "प.5.2.102", "तपःसहस्राभ्यां विनीनी", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_103(word, pos=""):
	return _apply(word, pos, "प.5.2.103", "अण् च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_104(word, pos=""):
	return _apply(word, pos, "प.5.2.104", "सिकताशर्कराभ्यां च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_105(word, pos=""):
	return _apply(word, pos, "प.5.2.105", "देशे लुबिलचौ च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_106(word, pos=""):
	return _apply(word, pos, "प.5.2.106", "दन्त उन्नत उरच्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_107(word, pos=""):
	return _apply(word, pos, "प.5.2.107", "ऊषसुषिमुष्कमधो रः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_108(word, pos=""):
	return _apply(word, pos, "प.5.2.108", "द्युद्रुभ्यां मः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_109(word, pos=""):
	return _apply(word, pos, "प.5.2.109", "केशाद्वोऽन्यतरस्याम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_110(word, pos=""):
	return _apply(word, pos, "प.5.2.110", "गाण्ड्यजगात् संज्ञायाम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_111(word, pos=""):
	return _apply(word, pos, "प.5.2.111", "काण्डाण्डादीरन्नीरचौ", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_112(word, pos=""):
	return _apply(word, pos, "प.5.2.112", "रजःकृष्यासुतिपरिषदो वलच्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_113(word, pos=""):
	return _apply(word, pos, "प.5.2.113", "दन्तशिखात् संज्ञायाम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_114(word, pos=""):
	return _apply(word, pos, "प.5.2.114", "ज्योत्स्नातमिस्राशृङ्गिणोर्जस्विन्नूर्जस्वलगोमिन्मलिनमलीमसाः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_115(word, pos=""):
	return _apply(word, pos, "प.5.2.115", "अत इनिठनौ", "in",
	"राम", "puं", "रामिन्")


def apply_5_2_116(word, pos=""):
	return _apply(word, pos, "प.5.2.116", "व्रीह्यादिभ्यश्च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_117(word, pos=""):
	return _apply(word, pos, "प.5.2.117", "तुन्दादिभ्य इलच् च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_118(word, pos=""):
	return _apply(word, pos, "प.5.2.118", "एकगोपूर्वाट्ठञ् नित्यम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_119(word, pos=""):
	return _apply(word, pos, "प.5.2.119", "शतसहस्रान्ताच्च निष्कात्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_120(word, pos=""):
	return _apply(word, pos, "प.5.2.120", "रूपादाहतप्रशंसयोर्यप्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_121(word, pos=""):
	return _apply(word, pos, "प.5.2.121", "अस्मायामेधास्रजो विनिः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_122(word, pos=""):
	return _apply(word, pos, "प.5.2.122", "बहुलं छन्दसि", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_123(word, pos=""):
	return _apply(word, pos, "प.5.2.123", "ऊर्णाया युस्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_124(word, pos=""):
	return _apply(word, pos, "प.5.2.124", "वाचो ग्मिनिः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_125(word, pos=""):
	return _apply(word, pos, "प.5.2.125", "आलजाटचौ बहुभाषिणि", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_126(word, pos=""):
	return _apply(word, pos, "प.5.2.126", "स्वामिन्नैश्वर्ये", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_127(word, pos=""):
	return _apply(word, pos, "प.5.2.127", "अर्शआदिभ्योऽच्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_128(word, pos=""):
	return _apply(word, pos, "प.5.2.128", "द्वन्द्वोपतापगर्ह्यात् प्राणिस्थादिनिः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_129(word, pos=""):
	return _apply(word, pos, "प.5.2.129", "वातातिसाराभ्यां कुक् च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_130(word, pos=""):
	return _apply(word, pos, "प.5.2.130", "वयसि पूरणात्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_131(word, pos=""):
	return _apply(word, pos, "प.5.2.131", "सुखादिभ्यश्च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_132(word, pos=""):
	return _apply(word, pos, "प.5.2.132", "धर्मशीलवर्णान्ताच्च", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_133(word, pos=""):
	return _apply(word, pos, "प.5.2.133", "हस्ताज्जातौ", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_134(word, pos=""):
	return _apply(word, pos, "प.5.2.134", "वर्णाद्ब्रह्मचारिणि", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_135(word, pos=""):
	return _apply(word, pos, "प.5.2.135", "पुष्करादिभ्यो देशे", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_136(word, pos=""):
	return _apply(word, pos, "प.5.2.136", "बलादिभ्यो मतुबन्यतरस्याम्", "vat",
	"बल", "puं", "बलवान्")


def apply_5_2_137(word, pos=""):
	return _apply(word, pos, "प.5.2.137", "संज्ञायां मन्माभ्याम्", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_138(word, pos=""):
	return _apply(word, pos, "प.5.2.138", "कंशंभ्यां बभयुस्तितुतयसः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_139(word, pos=""):
	return _apply(word, pos, "प.5.2.139", "तुन्दिवलिवटेर्भः", "taddhita",
	"राम", "puं", "रामिकः")


def apply_5_2_140(word, pos=""):
	return _apply(word, pos, "प.5.2.140", "अहंशुभमोर्युस्", "taddhita",
	"राम", "puं", "रामिकः")
