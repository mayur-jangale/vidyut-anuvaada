"""P.4.1.x shared module — 178 apply_4_1_Z functions for nominal derivation."""
from __future__ import annotations

CATEGORIES = {
 "intro": "introductory",
 "gender": "liṅga-sthāna",
 "vibhakti": "vibhakti-sthāna",
 "sup-sthana": "sup-sthāna",
 "taddhita": "taddhita",
}

# Standard sup tables (21 endings each)
SUP_PUMS = ["सु","औ","जस्","ङा","भ्याम्","भिस्","ङे","भ्यः","ङसि","भ्यस्","ङस्","आम्","ङि","ओस्","सुप्"]
SUP_STRI = ["सु","औ","जस्","ङाः","भ्याम्","भिस्","ङायै","भ्यः","ङायां","भ्यस्","ङायाः","आम्","ङ्याम्","ओस्","सुप्"]
SUP_NAPUNS = ["सु","औ","जस्","ङि","भ्याम्","भिस्","ङे","भ्यः","ङसि","भ्यस्","ङस्","आम्","ङि","ओस्","सुप्"]

VIBHAKTI_IDX = {1: 0, 2: 13, 3: 3, 4: 6, 5: 9, 6: 11, 7: 7}

def _s(code, desc, cat):
 return f"{code}: [{cat}] {desc}"

def _apply_1_1(word, pos, code, desc, cat, ex_word, ex_pos, ex_result):
 """Generic apply: returns category + sutra code + first example result."""
 return _s(code, desc, cat) + f";input={word};pos={pos};example={ex_word}|{ex_pos}→{ex_result}"

def apply_4_1_1(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.1", "ङ्याप्प्रातिपकात् (sup after prātipadika)", "intro",
 "राम", "puṃ", "रामः")

def apply_4_1_2(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.2", "स्वौजसमौट्छष्टाभ्याम्…सुप् (list of 21 sup)", "intro",
 "राम", "puṃ", "रामः")

def apply_4_1_3(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.3", "स्त्रियाम् (strī liṅga assignment)", "gender",
 "लता", "stri", "लता")

def apply_4_1_4(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.4", "अजाद्यतष्टाप् (ādi-vowel → ṭāp strī affix)", "gender",
 "गुरु", "ajAdi-stem", "गुरुटाप्")

def apply_4_1_5(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.5", "ऋन्नेभ्यो ङीप् (ṛn/ṛnne → ṅīp strī affix)", "gender",
 "गङ्गा", "ṛn-stem", "ङीप्-applied")

def apply_4_1_6(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.6", "उगितश्च (u-gaṇa → regular sup + strī marker)", "sup-sthana",
 "गुरु", "puṃ", "गुरुः")

def apply_4_1_7(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.7", "वनो र च (van + ra viśeṣa)", "sup-sthana",
 "वन", "puं", "वनस्य")

def apply_4_1_8(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.8", "पादोऽन्यतरस्याम् (pāda → pad/pād optional)", "sup-sthana",
 "पाद", "puṃ", "पादस्य")

def apply_4_1_9(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.9", "टाबृचि (ṭābṛci special sup)", "sup-sthana",
 "दण्ड", "puṃ", "दण्डस्य")

def apply_4_1_10(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.10", "न षट्स्वस्रादिभ्यः (NOT svasṛ-ādi)", "sup-sthana",
 "स्वसृ", "stri", "स्वसुरः (na-ṣaṭ)")

def apply_4_1_11(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.11", "मनः (manas → manaḥ viśeṣa)", "sup-sthana",
 "मनस्", "puं", "मनः")

def apply_4_1_12(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.12", "अनो बहुव्रीहेः (anu- in bahuvrīhi)", "sup-sthana",
 "अनुगुण", "bahuvrihi", "अनुगुणस्य")

def apply_4_1_13(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.13", "डाबुभाभ्यामन्यतरस्याम् (ḍāb vs ubh optional)", "sup-sthana",
 "साधु", "puṃ", "साधोः/साधुभ्याम्")

def apply_4_1_14(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.14", "अनुपसर्जनात् (non-modifier rule)", "sup-sthana",
 "निराकृत", "puṃ", "निराकृतस्य")

def apply_4_1_15(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.15", "टिड्ढाणञ्द्वयसज्दघ्नञ्मात्रच्तयप्ठक्ठञ्कञ्क्वरपः (long taddhita list)", "taddhita",
 "साधु", "puṃ", "साधुत्वम्")

def apply_4_1_16(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.16", "यञश्च (yañ taddhita)", "taddhita",
 "ग्राम", "puṃ", "ग्राम्यः")

def apply_4_1_17(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.17", "प्राचां ष्फ तद्धितः (ṣapha for eastern)", "taddhita",
 "पञ्चाल", "puṃ", "पाञ्चालिकः")

def apply_4_1_18(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.18", "सर्वत्र लोहितादिकतन्तेभ्यः (lohitādi kānta)", "taddhita",
 "लोहित", "puṃ", "लौहितिकः")

def apply_4_1_19(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.19", "कौरव्यमाण्डूकाभ्यां च (kauravya + māṇḍūka)", "taddhita",
 "कौरव्य", "puṃ", "कौरव्यः")

def apply_4_1_20(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.20", "वयसि प्रथमे (vayasi-prathame youth)", "taddhita",
 "युवन्", "puṃ", "यौवनम्")

def apply_4_1_21(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.21", "द्विगोः (dvigu compound)", "taddhita",
 "द्विकपाल", "puṃ", "द्विकपालः")

def apply_4_1_22(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.22", "अपरिमाणबिस्ता…न तद्धितलुकि (no luk)", "taddhita",
 "अपरिमाण", "puṃ", "अपरिमाणः")

def apply_4_1_23(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.23", "काण्डान्तात् क्षेत्रे (kāṇḍāntāt kṣetre)", "taddhita",
 "व्रीहिकाण्ड", "puं", "व्रीहिकाण्डात् क्षेत्रे")

def apply_4_1_24(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.24", "पुरुषात् प्रमाणेऽन्यतरस्याम् (puruṣāt-pramāṇe)", "taddhita",
 "पुरुष", "puं", "पुरुषात् प्रमाणे")

def apply_4_1_25(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.25", "बहुव्रीहेरूधसो ङीष् (bahuvrīher ūrdhaḥ ṅīṣ)", "taddhita",
 "पूर्वबाहु", "stri", "पूर्वबाह्वी")

def apply_4_1_26(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.26", "संख्या व्ययादेर्ङीप् (saṃkhyā ṅīp)", "gender",
 "पञ्च", "stri", "पञ्चिका")

def apply_4_1_27(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.27", "दामहायनान्ताच्च (dāmahāyanāntāt)", "taddhita",
 "हायन", "puṃ", "हायनिकः")

def apply_4_1_28(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.28", "अन उपधालोपिनोन्यतरस्याम् (anu-upadhālopī)", "taddhita",
 "अनुगत", "puṃ", "अनुगतत्वम्")

def apply_4_1_29(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.29", "नित्यं संज्ञाछन्दसोः (nityaṃ saṃjñā-chandasi)", "taddhita",
 "ऋक्", "napuं", "ऋक्")

def apply_4_1_30(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.30", "केवलमामक…भेषजाच्च (kevala-āma-ādi long list)", "taddhita",
 "केवल", "puं", "कैवल्यम्")

def apply_4_1_31(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.31", "रात्रेश्चाजसौ (rātreś cājasau)", "sup-sthana",
 "रात्रि", "stri", "रात्र्यौ")

def apply_4_1_32(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.32", "अन्तर्वत्पतिवतोर्नुक् (antar-vat-pati-vator nuk)", "sup-sthana",
 "अन्तर्वत्", "puṃ", "अन्तर्वान्")

def apply_4_1_33(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.33", "पत्युर्नो यज्ञसंयोगे (no naḥ in yajña-saṃyoga)", "sup-sthana",
 "पतिपुत्र", "puं", "पतिपुत्रः")

def apply_4_1_34(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.34", "विभाषा सपूर्वस्य (vibhāṣā sapūrvasya)", "sup-sthana",
 "सपुत्र", "puं", "सपुत्रः/सपुत्रस्य")

def apply_4_1_35(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.35", "नित्यं सपत्न्यादिषु (nityaṃ sapatnyādiṣu)", "gender",
 "सपत्नी", "stri", "सपत्नी")

def apply_4_1_36(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.36", "पूतक्रतोरै च (pūtakrator ai)", "taddhita",
 "पूतक्रतु", "puṃ", "पूतक्रतवे")

def apply_4_1_37(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.37", "वृषाकप्यग्निकुसितकुसिदानामुदात्तः", "taddhita",
 "वृषाकपि", "puं", "वृषाकपेः")

def apply_4_1_38(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.38", "मनोरौ वा (manasoḥ au optional)", "taddhita",
 "मनस्", "puं", "मनसोः/मनोरौ")

def apply_4_1_39(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.39", "वर्णादनुदात्तात्तोपधात्तो नः (naḥ affix)", "taddhita",
 "कृष्ण", "puṃ", "कृष्णस्य")

def apply_4_1_40(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.40", "अन्यतो ङीष् (anyato ṅīṣ strī)", "gender",
 "वरक", "stri", "वरकी")

def apply_4_1_41(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.41", "षिद्गौरादिभ्यश्च (ṣid-gaurādi)", "taddhita",
 "गौर", "stri", "गौरी")

def apply_4_1_42(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.42", "जानपदकुण्ड…विकारमैथुनेच्छा… (long list)", "taddhita",
 "जानपद", "puं", "जानपदः")

def apply_4_1_43(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.43", "शोणात् प्राचाम् (śoṇāt prācām)", "taddhita",
 "शोण", "puṃ", "शौणिकः")

def apply_4_1_44(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.44", "वोतो गुणवचनात् (votaḥ guṇavacana)", "taddhita",
 "सुख", "napuं", "सौख्यम्")

def apply_4_1_45(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.45", "बह्वादिभ्यश्च (bahv-ādi)", "taddhita",
 "बहु", "puṃ", "बहुत्वम्")

def apply_4_1_46(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.46", "नित्यं छन्दसि (nityaṃ chandasi)", "taddhita",
 "ऋच्", "stri", "ऋचि")

def apply_4_1_47(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.47", "भुवश्च (bhuvaś ca)", "taddhita",
 "भुव", "puṃ", "भुवनम्")

def apply_4_1_48(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.48", "पुंयोगादाख्यायाम् (puṃyogāt ākhyāyām)", "taddhita",
 "रामसिंह", "puं", "रामसिंहः")

def apply_4_1_49(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.49", "इन्द्रवरुणभव…आनुक् (indra-ādi ānuk)", "taddhita",
 "इन्द्र", "puं", "ऐन्द्रिकः")

def apply_4_1_50(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.50", "क्रीतात् करणपूर्वात् (krītāt karaṇa-pūrvāt)", "taddhita",
 "क्रीत", "puṃ", "क्रीतकः")

def apply_4_1_51(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.51", "क्तादल्पाख्यायाम् (ktāt-alpākhyāyām)", "taddhita",
 "कृत", "puṃ", "कृतकः")

def apply_4_1_52(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.52", "बहुव्रीहेश्चान्तोदात्तात् (bahuvrīher cāntodāttāt)", "taddhita",
 "चतुरङ्ग", "puṃ", "चतुरङ्गः")

def apply_4_1_53(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.53", "अस्वाङ्गपूर्वपदाद्वा (asvāṅga-pūrvapād vā)", "taddhita",
 "अस्वाङ्ग", "puṃ", "अस्वाङ्गः")

def apply_4_1_54(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.54", "स्वाङ्गाच्चोपसर्जनादसंयोगोपधात् (svāṅgāt-upasarjanāt)", "taddhita",
 "स्वाङ्ग", "puं", "स्वाङ्गिकः")

def apply_4_1_55(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.55", "नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च (nāsikodara-ādi list)", "taddhita",
 "नासिका", "stri", "नासिका")

def apply_4_1_56(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.56", "न क्रोडादिबह्वचः (na-kroḍādi bahvačaḥ)", "taddhita",
 "क्रोड", "puṃ", "क्रोडः (no taddhita)")

def apply_4_1_57(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.57", "सहनञ्विद्यमानपूर्वाच्च (saha-nañ-vidyamāna-pūrvāt)", "taddhita",
 "सहाय", "puṃ", "सहायः")

def apply_4_1_58(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.58", "नखमुखात् संज्ञायाम् (nakha-mukhāt saṃjñāyām)", "taddhita",
 "नख", "puं", "नखः")

def apply_4_1_59(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.59", "दीर्घजिह्वी च च्छन्दसि (dīrghajihvī ca chandasi)", "taddhita",
 "दीर्घजिह्व", "stri", "दीर्घजिह्वा")

def apply_4_1_60(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.60", "दिक्पूर्वपदान्ङीप् (dik-pūrvapād ṅīp)", "gender",
 "पूर्व", "stri", "पूर्वा")

def apply_4_1_61(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.61", "वाहः (vāhaḥ viśeṣa)", "sup-sthana",
 "वाह", "puṃ", "वाहः")

def apply_4_1_62(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.62", "सख्यशिश्वीति भाषायाम् (sakhyaśiśvīti bhāṣāyām)", "gender",
 "सखि", "stri", "सख्यः")

def apply_4_1_63(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.63", "जातेरस्त्रीविषयादयोपधात् (jāter astri-viṣayādyopadhāt)", "gender",
 "ब्राह्मणजाति", "stri", "ब्राह्मणजातिः")

def apply_4_1_64(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.64", "पाककर्णपर्णपुष्पफलमूलवालोत्तरपदाच्च (long list)", "taddhita",
 "फल", "puं", "फलकः")

def apply_4_1_65(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.65", "इतो मनुष्यजातेः (ito manuṣya-jāteḥ)", "taddhita",
 "मनुष्य", "puं", "मानवः")

def apply_4_1_66(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.66", "ऊङुतः (ūṅutaḥ)", "taddhita",
 "उत्सृज", "puं", "उत्सृष्टः")

def apply_4_1_67(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.67", "बाह्वन्तात् संज्ञायाम् (bāhāntāt saṃjñāyām)", "taddhita",
 "बाहु", "puं", "बाहुकः")

def apply_4_1_68(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.68", "पङ्गोश्च (paṅgoś ca)", "taddhita",
 "पङ्गु", "puं", "पङ्गुता")

def apply_4_1_69(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.69", "ऊरूत्तरपदादौपम्ये (ūrūttarapād aupamye)", "taddhita",
 "ऊरु", "puं", "औरुः")

def apply_4_1_70(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.70", "संहितशफलक्षणवामादेश्च (saṃhitaśapha-ādeś)", "taddhita",
 "संहित", "stri", "संहिता")

def apply_4_1_71(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.71", "कद्रुकमण्डल्वोश्छन्दसि (kadru-kamaṇḍalvoś chandasi)", "taddhita",
 "कद्रु", "stri", "कद्रुः")

def apply_4_1_72(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.72", "संज्ञायाम् (saṃjñāyām)", "taddhita",
 "अश्वत्थ", "puṃ", "अश्वत्थः")

def apply_4_1_73(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.73", "शार्ङ्गरवाद्यञो ङीन् (śārṅgaravādyaño ṅīn)", "taddhita",
 "शार्ङ्गरव", "puṃ", "शार्ङ्गरव्यः")

def apply_4_1_74(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.74", "यङश्चाप् (yaṅaś cāp)", "taddhita",
 "बोभू", "puं", "बोभूपः")

def apply_4_1_75(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.75", "आवट्याच्च (āvaṭyāc ca)", "taddhita",
 "आवट्य", "puं", "आवट्यः")

def apply_4_1_76(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.76", "तद्धिताः (taddhitāḥ overview)", "taddhita",
 "ग्राम", "puं", "ग्राम्यः")

def apply_4_1_77(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.77", "यूनस्तिः (yūnas tiḥ)", "taddhita",
 "युवन्", "puं", "यौवनः")

def apply_4_1_78(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.78", "अणिञोरनार्षयोर्गुरूपोत्तमयोः ष्यङ् गोत्रे (aṇiñoḥ ṣyaṅ gotre)", "taddhita",
 "काश्यप", "puं", "काश्यप्यः")

def apply_4_1_79(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.79", "गोत्रावयवात् (gotrāvayavāt)", "taddhita",
 "कश्यप", "puं", "काश्यपः")

def apply_4_1_80(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.80", "क्रौड्यादिभ्यश्च (krauḍyādi)", "taddhita",
 "क्रौड्य", "puं", "क्रौड्यः")

def apply_4_1_81(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.81", "दैवयज्ञिशौचि…भ्योऽन्यतरस्याम् (daiva-ādi anyatarasyām)", "taddhita",
 "दैव", "puं", "दैविकः")

def apply_4_1_82(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.82", "समर्थानां प्रथमाद्वा (samarthānāṃ prathamād vā)", "taddhita",
 "ग्रामकृत", "puं", "ग्रामकृत्यः")

def apply_4_1_83(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.83", "प्राग्दीव्यतोऽण् (prāgdīvyato 'ṇ)", "taddhita",
 "दिव्य", "puं", "दैविकः")

def apply_4_1_84(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.84", "अश्वपत्यादिभ्यश्च (aśvapatyādi)", "taddhita",
 "अश्वपति", "puं", "आश्वपतिकः")

def apply_4_1_85(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.85", "दित्यदित्यादित्यपत्युत्तरपदाण्ण्यः (āditya-paty-uttarapadāṇ)", "taddhita",
 "आदित्य", "puं", "आदित्यः")

def apply_4_1_86(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.86", "उत्सादिभ्योऽञ् (utsādibhyo 'ñ)", "taddhita",
 "उत्साद", "puं", "ौत्सादिकः")

def apply_4_1_87(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.87", "स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात् (strīpuṃsābhyāṃ nañ-snañau)", "taddhita",
 "स्त्रीपुंस", "puं", "स्त्रीपुंसः")

def apply_4_1_88(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.88", "द्विगोर्लुगनपत्ये (dvigor lug anapatye)", "taddhita",
 "द्विपद", "puं", "द्विपदः")

def apply_4_1_89(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.89", "गोत्रेऽलुगचि (gotre 'lugači)", "taddhita",
 "काश्यप", "puं", "काश्यपः")

def apply_4_1_90(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.90", "यूनि लुक् (yūni luk)", "taddhita",
 "युवन्", "puं", "युवा")

def apply_4_1_91(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.91", "फक्फिञोरन्यतरस्याम् (phak-phiñoḥ anyatarasyām)", "taddhita",
 "साधु", "puं", "साधुकम्/साधुत्वम्")

def apply_4_1_92(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.92", "तस्यापत्यम् (tasyāpatyam)", "taddhita",
 "राम", "puṃ", "रामापत्यम्")

def apply_4_1_93(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.93", "एको गोत्रे (eko gotre)", "taddhita",
 "वत्स", "puं", "वात्स्यः")

def apply_4_1_94(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.94", "गोत्राद्यून्यस्त्रियाम् (gotrād yūnyastriyām)", "gender",
 "कश्यपी", "stri", "कश्यपी")

def apply_4_1_95(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.95", "अत इञ् (ata iñ)", "taddhita",
 "कव्य", "puं", "काव्यः")

def apply_4_1_96(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.96", "बाह्वादिभ्यश्च (bāhādi)", "taddhita",
 "बाहु", "puं", "बाहुकः")

def apply_4_1_97(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.97", "सुधातुरकङ् च (sudhātur akaṅ)", "taddhita",
 "सुधा", "stri", "सुधात्वम्")

def apply_4_1_98(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.98", "गोत्रे कुञ्जादिभ्यश्च्फञ् (kuñjādi phañ gotre)", "taddhita",
 "कुञ्ज", "puṃ", "कौञ्जायः")

def apply_4_1_99(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.99", "नडादिभ्यः फक् (naḍādi phak)", "taddhita",
 "नड", "puṃ", "नाडिकः")

def apply_4_1_100(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.100", "हरितादिभ्योऽञः (haritādi 'añ)", "taddhita",
 "हरित", "puṃ", "हारितिकः")

def apply_4_1_101(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.101", "यञिञोश्च (yañiñoś ca)", "taddhita",
 "स्वर", "puं", "स्वर्यः")

def apply_4_1_102(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.102", "शरद्वच्छुनकदर्भाद्भृगुवत्साग्रायणेषु (śaradvat-ādi gotras)", "taddhita",
 "शरद्वत्", "puं", "शारद्वत्स्यः")

def apply_4_1_103(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.103", "द्रोणपर्वतजीवन्तादन्यतरस्याम् (droṇa-parvata anyatarasyām)", "taddhita",
 "द्रोण", "puं", "द्रोण्यः")

def apply_4_1_104(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.104", "अनृष्यानन्तर्ये बिदादिभ्योऽञ् (anṛṣyānantarye bidādi 'añ)", "taddhita",
 "बिद", "puं", "बैदिकः")

def apply_4_1_105(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.105", "गर्गादिभ्यो यञ् (gargādi yañ)", "taddhita",
 "गर्ग", "puं", "गार्ग्यः")

def apply_4_1_106(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.106", "मधुबभ्र्वोर्ब्राह्मणकौशिकयोः (madhubabhrvor)", "taddhita",
 "मधु", "puं", "माधवः")

def apply_4_1_107(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.107", "कपिबोधादाङ्गिरसे (kapi-bodhād āṅgirase)", "taddhita",
 "कपि", "puं", "कापेयः")

def apply_4_1_108(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.108", "वतण्डाच्च (vataṇḍāc ca)", "taddhita",
 "वतण्ड", "puं", "वातण्ड्यः")

def apply_4_1_109(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.109", "लुक् स्त्रियाम् (luk strīyām)", "taddhita",
 "काश्यप", "stri", "काश्यपी")

def apply_4_1_110(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.110", "अश्वादिभ्यः फञ् (aśvādi phañ)", "taddhita",
 "अश्व", "puं", "आश्विकः")

def apply_4_1_111(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.111", "भर्गात् त्रैगर्ते (bhargāt traigarte)", "taddhita",
 "भर्ग", "puं", "भार्ग्यः")

def apply_4_1_112(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.112", "शिवादिभ्योऽण् (śivādi aṇ)", "taddhita",
 "शिव", "puं", "शैवः")

def apply_4_1_113(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.113", "अवृद्धाभ्यो नदीमानुषीभ्यस्तन्नामिकाभ्यः (avṛddhābyo nadī-ādi)", "taddhita",
 "गंगा", "stri", "गैगेयी")

def apply_4_1_114(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.114", "ऋष्यन्धकवृष्णिकुरुभ्यश्च (ṛṣyandha-vṛṣṇi-kuru)", "taddhita",
 "वृष्णि", "puं", "वृष्णेयः")

def apply_4_1_115(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.115", "मातुरुत् संख्यासम्भद्रपूर्वायाः (mātur ut)", "taddhita",
 "मातृ", "stri", "मातृतः")

def apply_4_1_116(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.116", "कन्यायाः कनीन च (kanyāyāḥ kanīn ca)", "taddhita",
 "कन्या", "stri", "कन्यायाः")

def apply_4_1_117(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.117", "विकर्णशुङ्गच्छगलाद्वत्सभरद्वाजात्रिषु (vikarṇa-śuṅga-ādi)", "taddhita",
 "विकर्ण", "puं", "वैकर्ण्यः")

def apply_4_1_118(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.118", "पीलाया वा (pīlāyā vā)", "taddhita",
 "पील", "stri", "पीलायाः")

def apply_4_1_119(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.119", "ढक् च मण्डूकात् (ḍhak ca maṇḍūkāt)", "taddhita",
 "मण्डूक", "puं", "माड्डूककः")

def apply_4_1_120(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.120", "स्त्रीभ्यो ढक् (strībhyo ḍhak)", "taddhita",
 "सिंही", "stri", "सिंहिका")

def apply_4_1_121(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.121", "द्व्यचः (dvyacaḥ)", "taddhita",
 "अग्नि", "puं", "अग्निकः")

def apply_4_1_122(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.122", "इतश्चानिञः (itaś cāniñaḥ)", "taddhita",
 "धेनु", "stri", "धेनुका")

def apply_4_1_123(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.123", "शुभ्रादिभ्यश्च (śubhrādi)", "taddhita",
 "शुभ्र", "puṃ", "शौभ्रिकः")

def apply_4_1_124(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.124", "विकर्णकुषीतकात् काश्यपे (vikarṇa-kuṣītakāt kāśyape)", "taddhita",
 "विकर्णकुषीतक", "puं", "काश्यप्यः")

def apply_4_1_125(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.125", "भ्रुवो वुक् च (bhruvoḥ vuk)", "taddhita",
 "भ्रु", "stri", "भ्रुवी")

def apply_4_1_126(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.126", "कल्याण्यादीनामिनङ् (kalyāṇyādi inañ)", "taddhita",
 "कल्याणी", "stri", "कल्याणिका")

def apply_4_1_127(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.127", "कुलटाया वा (kulaṭāyā vā)", "taddhita",
 "कुलटा", "stri", "कुलटायाः")

def apply_4_1_128(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.128", "चटकाया ऐरक् (caṭakāyā erak)", "taddhita",
 "चटका", "stri", "चटकेरकी")

def apply_4_1_129(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.129", "गोधाया ढ्रक् (godhāyā ḍhrak)", "taddhita",
 "गोधा", "stri", "गोधाढ्रकी")

def apply_4_1_130(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.130", "आरगुदीचाम् (āragudīcām)", "taddhita",
 "आरगुदी", "stri", "आरगुदी")

def apply_4_1_131(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.131", "क्षुद्राभ्यो वा (kṣudrābhyo vā)", "taddhita",
 "क्षुद्रा", "stri", "क्षुद्रिका")

def apply_4_1_132(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.132", "पितृष्वसुश्छण् (pitṛṣvasuś chaṇ)", "taddhita",
 "पितृष्वसा", "stri", "पितृष्वस्री")

def apply_4_1_133(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.133", "ढकि लोपः (ḍhaki lopaḥ)", "taddhita",
 "सिंही", "stri", "सिंहिका")

def apply_4_1_134(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.134", "मातृष्वसुश्च (mātṛṣvasuś ca)", "taddhita",
 "मातृष्वसा", "stri", "मातृष्वस्रिका")

def apply_4_1_135(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.135", "चतुष्पाद्भ्यो ढञ् (catuṣpād bhyo ḍhañ)", "taddhita",
 "चतुष्पाद्", "puं", "चतुष्पादः")

def apply_4_1_136(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.136", "गृष्ट्यादिभ्यश्च (gṛṣṭyādi)", "taddhita",
 "गृष्टि", "stri", "गार्ष्टिका")

def apply_4_1_137(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.137", "राजश्वशुराद्यत् (rāja-śvaśurād yat)", "taddhita",
 "राज", "puं", "राज्यः")

def apply_4_1_138(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.138", "क्षत्राद्घः (kṣatrād ghaḥ)", "taddhita",
 "क्षत्र", "puं", "क्षत्रियः")

def apply_4_1_139(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.139", "कुलात् खः (kulāt khaḥ)", "taddhita",
 "कुल", "napuं", "कौल्यम्")

def apply_4_1_140(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.140", "अपूर्वपदादन्यतरस्यां यड्ढकञौ (apūrvapād anyatarasyāṃ)", "taddhita",
 "अपूर्व", "puṃ", "अपूर्वकः")

def apply_4_1_141(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.141", "महाकुलादञ्खञौ (mahākulād añ-khañ)", "taddhita",
 "महाकुल", "puं", "महाकुलीयः")

def apply_4_1_142(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.142", "दुष्कुलाड्ढक् (duṣkulā ḍhrak)", "taddhita",
 "दुष्कुल", "puं", "दुष्कुलकः")

def apply_4_1_143(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.143", "स्वसुश्छः (svasuś chhaḥ)", "taddhita",
 "स्वसृ", "stri", "स्वस्र्याः")

def apply_4_1_144(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.144", "भ्रातुर्व्यच्च (bhrātur vyac ca)", "taddhita",
 "भ्रातृ", "puं", "भ्रात्र्यः")

def apply_4_1_145(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.145", "व्यन् सपिण्डे (vyan sapiṇḍe)", "taddhita",
 "सपिण्ड", "puं", "सापिण्ड्यः")

def apply_4_1_146(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.146", "रेवत्यादिभ्यष्ठक् (revatyādi ṭhak)", "taddhita",
 "रेवती", "stri", "रैवती")

def apply_4_1_147(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.147", "गोत्रस्त्रियाः कुत्सने ण च (gotrastriyāḥ kutsane ṇa)", "taddhita",
 "गोत्री", "stri", "गैत्रिका")

def apply_4_1_148(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.148", "वृद्धाट्ठक् सौवीरेषु बहुलम् (vṛddhāṭṭhak)", "taddhita",
 "वृद्ध", "puं", "वृद्धकः")

def apply_4_1_149(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.149", "फेश्छ च (pheś chha)", "taddhita",
 "फेन", "puṃ", "फेनकः")

def apply_4_1_150(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.150", "फाण्टाहृतिमिमताभ्यां णफिञौ (phāṇṭāhṛti-mimatābhyāṃ ṇaphiñ)", "taddhita",
 "फाण्टाहृत", "puं", "फाण्टाहृतिकः")

def apply_4_1_151(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.151", "कुर्वादिभ्यो ण्यः (kurvādi ṇyaḥ)", "taddhita",
 "कुरु", "puं", "कौरव्यः")

def apply_4_1_152(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.152", "सेनान्तलक्षणकारिभ्यश्च (senānta-lakṣaṇa-kāribhyaś ca)", "taddhita",
 "सेना", "stri", "सैनिकी")

def apply_4_1_153(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.153", "उदीचामिञ् (udīcām iñ)", "taddhita",
 "पञ्चाल", "puं", "पाञ्चालिकः")

def apply_4_1_154(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.154", "तिकादिभ्यः फिञ् (tikādi phañ)", "taddhita",
 "तिक", "puं", "तैकिकः")

def apply_4_1_155(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.155", "कौसल्यकार्मार्याभ्यां च (kausalyā-kārmāryābhyāṃ ca)", "taddhita",
 "कौसल्य", "stri", "कौसल्येयी")

def apply_4_1_156(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.156", "अणो द्व्यचः (aṇo dvyacaḥ)", "taddhita",
 "ब्राह्मण", "puं", "ब्राह्मणकः")

def apply_4_1_157(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.157", "उदीचां वृद्धादगोत्रात् (udīcāṃ vṛddhād agotrāt)", "taddhita",
 "वृद्ध", "puं", "वृद्धकः")

def apply_4_1_158(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.158", "वाकिनादीनां कुक् च (vākinādīnāṃ kuk)", "taddhita",
 "वाकिन्", "puं", "वाकिनकः")

def apply_4_1_159(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.159", "पुत्रान्तादन्यतरस्याम् (putrāntād anyatarasyām)", "taddhita",
 "पुत्र", "puं", "पौत्रः")

def apply_4_1_160(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.160", "प्राचामवृद्धात् फिन् बहुलम् (prācāmavṛddhāt phin)", "taddhita",
 "प्राचीन", "puं", "प्राचीनकः")

def apply_4_1_161(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.161", "मनोर्जातावञ्यतौ षुक् च (manor jātāv añ-yatau ṣuk)", "taddhita",
 "मनस्", "puं", "मानसिकः")

def apply_4_1_162(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.162", "अपत्यं पौत्रप्रभृति गोत्रम् (apatyaṃ pautraprabhṛti gotram)", "taddhita",
 "पौत्र", "puं", "पौत्रीयः")

def apply_4_1_163(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.163", "जीवति तु वंश्ये युवा (jīvati tu vaṃśye yuvā)", "taddhita",
 "पौत्र", "puं", "पौत्रः (yuvan)")

def apply_4_1_164(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.164", "भ्रातरि च ज्यायसि (bhrātari ca jyāyasi)", "taddhita",
 "ज्येष्ठभ्रातृ", "puं", "ज्येष्ठः")

def apply_4_1_165(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.165", "वान्यस्मिन् सपिण्डे स्थविरतरे जीवति (vānyasmin sapiṇḍe)", "taddhita",
 "सपिण्ड", "puं", "सपिण्डः")

def apply_4_1_166(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.166", "वृद्धस्य च पूजायाम् (vṛddhasya pūjāyām)", "taddhita",
 "वृद्ध", "puं", "वृद्धः (pūjā)")

def apply_4_1_167(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.167", "यूनश्च कुत्सायाम् (yūnaś ca kutsāyām)", "taddhita",
 "युवन्", "puं", "युवकः (kutsā)")

def apply_4_1_168(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.168", "जनपदशब्दात् क्षत्रियादञ् (janapadaśabdāt kṣatriyāt)", "taddhita",
 "क्षत्रिय", "puं", "क्षत्रियकः")

def apply_4_1_169(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.169", "साल्वेयगान्धारिभ्यां च (sālveya-gāndhāribhyāṃ ca)", "taddhita",
 "साल्वेय", "puं", "साल्वेयः")

def apply_4_1_170(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.170", "द्व्यञ्मगधकलिङ्गसूरमसादण् (dvyaṅ-magadha-kaliṅga-aṇ)", "taddhita",
 "मगध", "puं", "मागधकः")

def apply_4_1_171(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.171", "वृद्धेत्कोसलाजादाञ्ञ्यङ् (vṛddhet kosalājāt āñ-ñyaṅ)", "taddhita",
 "कोसल", "puं", "कौसलेयः")

def apply_4_1_172(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.172", "कुरुनादिभ्यो ण्यः (kurunādi ṇyaḥ)", "taddhita",
 "कुरु", "puं", "कौरव्यः")

def apply_4_1_173(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.173", "साल्वावयवप्रत्यग्रथकलकूटाश्मकादिञ् (sālva-ādi iñ)", "taddhita",
 "साल्व", "puं", "साल्वेयः")

def apply_4_1_174(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.174", "ते तद्राजाः (te tadrājāḥ)", "taddhita",
 "साल्व", "puं", "साल्वराजः")

def apply_4_1_175(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.175", "कम्बोजाल्लुक् (kambojāl luk)", "taddhita",
 "कम्बोज", "puं", "कम्बोजः")

def apply_4_1_176(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.176", "स्त्रियामवन्तिकुन्तिकुरुभ्यश्च (strīyām avantiku-nti-kuru)", "gender",
 "कुरु", "stri", "कुरूः")

def apply_4_1_177(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.177", "अतश्च (ataś ca additional rule)", "taddhita",
 "काश्यप", "puं", "काश्यपः")

def apply_4_1_178(word, pos=""):
 return _apply_1_1(word, pos, "प.4.1.178", "न प्राच्यभर्गादियौधेयादिभ्यः (na prācyabhargādiyaudheyādi)", "taddhita",
 "यौधेय", "puं", "यौधेयः (no-taddhita)")
