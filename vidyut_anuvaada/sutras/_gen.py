"""Build P_1_4.py - the consolidated sutra logic for P.1.4.1-110."""
import pathlib, ast

NL = "\n"
T = "\t"
OUT = pathlib.Path("P_1_4.py")

kara_specs = [
(24,'if pos=="apādāna": return f"kāraka=apādāna;dhruva;word={word}"','return f"not-apādāna:{word}"'),
(25,'if pos=="apādāna-bhayahetu": return f"kāraka=apādāna;bhayahetu;word={word}"','return f"not-bhayahetu:{word}"'),
(26,'if "पराजित" in word or "जित" in word: return f"kāraka=apādāna;parājita;word={word}"','return f"not-parājita:{word}"'),
(27,'if pos=="apādāna-vāraṇa" or word in ("अग्नि","शस्त्र","रक्ष"): return f"kāraka=apādāna;vāraṇa;word={word}"','return f"not-vāraṇa:{word}"'),
(28,'if pos=="apādāna-antarddhi": return f"kāraka=apādāna;antarddhi;word={word}"','return f"not-antarddhi-apādāna:{word}"'),
(29,'if pos=="kartṛ-ākhyāta": return f"kāraka=kartṛ;ākhyātopayoga;word={word}"','return f"not-ākhyāta-kartṛ:{word}"'),
(30,'if pos=="kartṛ-janikartṛ": return f"kartṛ=prakṛti;janikartṛ;word={word}"','return f"not-janikartṛ:{word}"'),
(31,'if pos=="apādāna-bhuvaḥ" or word in ("जन्म","उत्पत्ति","मूल"): return f"kāraka=apādāna;bhū-prabhava;word={word}"','return f"not-bhū-prabhava:{word}"'),
(32,'if pos=="sampradānam": return f"kāraka=sampradānam;abhiprēti;word={word}"','return f"not-sampradānam:{word}"'),
(33,'if pos=="sampradānam-ruci": return f"kāraka=sampradānam;ruci-artha;word={word}"','return f"not-ruci-sampradānam:{word}"'),
(34,'if pos in ("sampradānam-ślāghā","sampradānam-hnuṅ","sampradānam-sthāśap"): return f"kāraka=sampradānam;word={word}"','return f"not-ślāghā-sampradānam:{word}"'),
(35,'if pos=="sampradānam-dhāra": return f"kāraka=sampradānam;dhāra;uttamarṇa;word={word}"','return f"not-dhāra-sampradānam:{word}"'),
(36,'if pos=="sampradānam-spṛhā": return f"kāraka=sampradānam;spṛhā;word={word}"','return f"not-spṛhā-sampradānam:{word}"'),
(37,'if pos in ("sampradānam-krodha","sampradānam-droha","sampradānam-īrṣyā","sampradānam-asūyā"): return f"kāraka=sampradānam;word={word}"','return f"not-krodha-sampradānam:{word}"'),
(38,'if pos=="karman-krodha-upasṛṣṭa": return f"kāraka=karman;krodha-upasṛṣṭa;word={word}"','return f"not-krodha-upasṛṣṭa-karman:{word}"'),
(39,'if pos in ("kartṛ-rādhī","kartṛ-īkṣyā"): return f"kāraka=kartṛ;rādhī/īkṣyā;word={word}"','return f"not-rādhī-kartṛ:{word}"'),
(40,'if pos in ("kartṛ-śru-pratyaṅ","kartṛ-śru-āṅ"): return f"kāraka=kartṛ;śru;word={word}"','return f"not-pratyaṅ-kartṛ:{word}"'),
(41,'if pos in ("kartṛ-anu-gṛ","kartṛ-prati-gṛ","kartṛ-gṛ"): return f"kāraka=kartṛ;word={word}"','return f"not-anu-prati-gṛ-kartṛ:{word}"'),
(42,'if pos=="karaṇam": return f"kāraka=karaṇam;sādhakatama;word={word}"','return f"not-sādhakatama-karaṇam:{word}"'),
(43,'if pos=="karman-div" or word in ("दिव","दिव्य"): return f"kāraka=karman;div;word={word}"','return f"not-div-karman:{word}"'),
(44,'if pos in ("sampradānam-parikrayaṇa","sampradānam-parivikrayaṇa"): return f"kāraka=sampradānam;anyatara;word={word}"','return f"not-parikrayaṇa:{word}"'),
(45,'if pos=="adhikaraṇa": return f"kāraka=adhikaraṇa;ādhāra;word={word}"','return f"not-ādhāra-adhikaraṇa:{word}"'),
(46,'if pos in ("karman-adhi-śīṅ","karman-adhi-sthā","karman-adhi-āsā"): return f"kāraka=karman;word={word}"','return f"not-adhi-śīṅ-karman:{word}"'),
(47,'if pos=="karman-abhiniviś" or "अभिनिवेश" in word: return f"kāraka=karman;abhiniviś;word={word}"','return f"not-abhiniviś-karman:{word}"'),
(48,'if pos in ("karman-upa","karman-anva","karman-dhyāṅ","karman-vas"): return f"kāraka=karman;word={word}"','return f"not-upa-anva-karman:{word}"'),
(49,'if pos=="karman-īpsita": return f"kāraka=karman;īpsitatama;word={word}"','return f"not-īpsita-karman:{word}"'),
(50,'if pos=="not-karman-anīpsita": return f"not-karman;anīpsita;word={word}"','return f"possibly-karman:{word}"'),
(51,'if pos=="kāraka-akathita": return f"kāraka=akathita;word={word}"','return f"possibly-akathita:{word}"'),
]

desc_H = {
24:'P.1.4.24 ध्रुवमपायेऽपादानम् — apādānam = fixed point of departure',
25:'P.1.4.25 भीत्रार्थानां भयहेतुः — fear-source = apādāna',
26:'P.1.4.26 पराजेरसोढः — defeated = apādāna',
27:'P.1.4.27 वारणार्थानामीप्सितः — in protection, desired = apādāna',
28:'P.1.4.28 अन्तर्द्धौ येनादर्शनमिच्छति — concealment = apādāna',
29:'P.1.4.29 आख्यातोपयोगे — with ākhyāta → kartṛ',
30:'P.1.4.30 जनिकर्तुः प्रकृतिः — prakṛti of janikartṛ',
31:'P.1.4.31 भुवः प्रभवः — bhū source = apādāna',
32:'P.1.4.32 कर्मणा यमभिप्रैति स सम्प्रदानम् — toward whom = sampradānam',
33:'P.1.4.33 रुच्यर्थानां प्रीयमाणः — in liking = sampradānam',
34:'P.1.4.34 श्लाघह्नुङ्स्थाशपां — praise/blame = sampradānam',
35:'P.1.4.35 धारेरुत्तमर्णः — in lending = sampradānam',
36:'P.1.4.36 स्पृहेरीप्सितः — in desiring = sampradānam',
37:'P.1.4.37 क्रुधद्रुहेर्ष्याऽसूयार्थानां — anger toward = sampradānam',
38:'P.1.4.38 क्रुधद्रुहोरुपसृष्टयोः कर्म — qualified = karman',
39:'P.1.4.39 राधीक्ष्योर्यस्य विप्रश्नः — enquiry = kartṛ',
40:'P.1.4.40 प्रत्याङ्भ्यां श्रुवः — hearer = kartṛ',
41:'P.1.4.41 अनुप्रतिगृणश्च — hearer = kartṛ',
42:'P.1.4.42 साधकतमं करणम् — most efficient = karaṇam',
43:'P.1.4.43 दिवः कर्म च — div also = karman',
44:'P.1.4.44 परिक्रयणे सम्प्रदानमन्यतरस्याम् — buying/selling = sampradānam',
45:'P.1.4.45 आधारोऽधिकरणम् — locus = adhikaraṇa',
46:'P.1.4.46 अधिशीङ्स्थाऽऽसां कर्म — adhi+śīṅ/sthā/āsā = karman',
47:'P.1.4.47 अभिनिविशश्च — abhiniviś = karman',
48:'P.1.4.48 उपान्वध्याङ्वसः — upa/anva = karman',
49:'P.1.4.49 कर्तुरीप्सिततमं कर्म — most desired = karman',
50:'P.1.4.50 तथायुक्तं चानीप्सितम् — connected but NOT desired ≠ karman',
51:'P.1.4.51 अकथितं च — unexpressed = kāraka',
}

up_specs = [
(56, 'if pos=="nipāta-īśvara": return f"nipāta:before-īśvara;word={word}"', 'return f"not-nipāta-īśvara:{word}"'),
(57, 'NIPATA_CA={"च","चैव","तु","अपि","हि","किल","स्म","वै","एव"}\nif word in NIPATA_CA: return f"nipāta:ca-ādi;word={word}"', 'return f"not-ca-ādi:{word}"'),
(58, 'PRADI={"प्र","परा","अप","अनु","अव","सम्","दुस्","निर्","दुर्","अति","अधि","उत्","अभि","उप","निस्","पुनः"}\nif word in PRADI: return f"upasarga:prādi;word={word}"', 'return f"not-prādi:{word}"'),
(59, 'UPASARGA={"प्र","अप","अनु","उप","पुनः","अति","अधि","सम्"}\nif word in UPASARGA or pos=="upasarga-kriyāyoge": return f"upasarga;kriyāyoge;word={word}"', 'return f"not-upasarga-kriyā:{word}"'),
(60, 'GATI={"परा","अप","अनु","अव","सम्","दुर्","निर्","अति","अधि","उप","निस्","पुनः"}\nif word in GATI: return f"upasarga:gati;word={word}"', 'return f"not-gati-upasarga:{word}"'),
(61, 'URYADI=("ऊरी","क्रुध्","द्रुह्","कुह")\nif word[:4] in URYADI: return f"upasarga:ūryādi;word={word}"', 'return f"not-ūryādi:{word}"'),
(62, 'ANUKARANA={"चटचटा","ठठा","फफा"}\nif word in ANUKARANA or pos=="anukaraṇa": return f"upasarga:anukaraṇa;word={word}"', 'return f"not-anukaraṇa:{word}"'),
(63, 'if word in {"सत्","सद्","असत्"} or pos=="abhiniveśa": return f"sadasatī:abhiniveśa;word={word}"', 'return f"not-sadasatī:{word}"'),
(64, 'if word=="अलम्" or pos=="upasarga-alam": return f"upasarga:alam;word={word}"', 'return f"not-alam:{word}"'),
(65, 'if word=="अन्तर" or pos=="upasarga-antara": return f"upasarga:antara;word={word}"', 'return f"not-antara:{word}"'),
(66, 'if word in ("कण","मनस्") or pos in ("śraddhā","apratighāta"): return f"kaṇa-manas;word={word}"', 'return f"not-kaṇa-manas:{word}"'),
(67, 'if word=="पुरा" or word.startswith("पुरो"): return f"avyaya:purā;word={word}"', 'return f"not-purā:{word}"'),
(68, 'if word=="अस्तम्" or word.startswith("अस्त"): return f"avyaya:astam;word={word}"', 'return f"not-astam:{word}"'),
(69, 'if word.startswith("अच्छ") or pos=="upasarga-accha": return f"upasarga:accha;word={word}"', 'return f"not-accha:{word}"'),
(70, 'if word.startswith("अदस") or word in {"अदस्","अदसो"}: return f"adas:anupadeśe;word={word}"', 'return f"not-adas:{word}"'),
(71, 'if word.startswith("तिर") or pos=="upasarga-tiras": return f"upasarga:tiras;word={word}"', 'return f"not-tiras:{word}"'),
(72, 'if pos in ("kṛñ","kṛñ-optional"): return f"viBhāṣā:kṛñ;word={word}"', 'return f"not-kṛñ:{word}"'),
(73, 'if word.startswith("उपाज") or word.startswith("अन्वाज"): return f"upāja/anvāja;word={word}"', 'return f"not-upāja:{word}"'),
(74, 'SAKSHAT={"साक्षात्","साक्षाद्","साक्षाच्"}\nif word in SAKSHAT: return f"upasarga:sākṣāt;word={word}"', 'return f"not-sākṣāt:{word}"'),
(75, 'if word in ("उरस्","उरः","मनस्","मनः") or pos=="anityādhāna": return f"anityādhāna;word={word}"', 'return f"not-anityādhāna:{word}"'),
(76, 'if pos in ("madhyam-pada","nivacana"): return f"madhyam-pada;word={word}"', 'return f"not-madhyam:{word}"'),
(77, 'if word in ("हस्त","हस्ते","पाणि","पाणौ") or pos=="upayamana": return f"hasta-pāṇi;word={word}"', 'return f"not-hasta-pāṇi:{word}"'),
(78, 'if word.startswith("प्राधु") or pos=="bandhana": return f"prādhu;word={word}"', 'return f"not-prādhu:{word}"'),
(79, 'if word in ("जीविका","उपनिषद्","उपनिषाद्") or pos=="aupamya": return f"jīvikā-upaniṣad;word={word}"', 'return f"not-jīvikā-upaniṣad:{word}"'),
(80, 'if word=="ते" or word.startswith("ते"): return f"te-dhātu;word={word}"', 'return f"not-te:{word}"'),
(81, 'if pos=="chandas": return f"vedic:chandas;word={word}"', 'return f"not-chandas-pare:{word}"'),
(82, 'if pos=="vyavahita": return f"vyavahita;word={word}"', 'return f"not-vyavahita:{word}"'),
(83, 'if pos=="karmapravacanīya": return f"karmapravacanīya;word={word}"', 'return f"not-karmapravacanīya:{word}"'),
(84, 'if word.startswith("अनु") or pos=="anu-lakṣaṇa": return f"upasarga:anu;word={word}"', 'return f"not-anu-lakṣaṇa:{word}"'),
(85, 'if pos=="tṛtīyārtha": return f"tṛtīyā;word={word}"', 'return f"not-tṛtīyā:{word}"'),
(86, 'if pos=="hīna" or "हीन" in word: return f"hīna;word={word}"', 'return f"not-hīna:{word}"'),
(87, 'if word.startswith("उप") or pos=="upa-adhika": return f"upasarga:upa;word={word}"', 'return f"not-upa-adhika:{word}"'),
(88, 'if word.startswith("अप") or word.startswith("परि") or pos=="apa-parī-varjana": return f"upasarga:apa/parī;word={word}"', 'return f"not-apa-parī:{word}"'),
(89, 'if word.startswith("आ") or pos=="āṅ-maryādā": return f"upasarga:āṅ;word={word}"', 'return f"not-āṅ-maryādā:{word}"'),
(90, 'if word.startswith("प्रतिपर") or pos.startswith("pratipar"): return f"upasarga:pratipar;word={word}"', 'return f"not-pratipar:{word}"'),
(91, 'if word.startswith("अभि") or pos=="abhi-bhāga": return f"upasarga:abhi;word={word}"', 'return f"not-abhi-bhāga:{word}"'),
(92, 'if word.startswith("प्रति") or pos=="prati-pratinidhi": return f"upasarga:prati;word={word}"', 'return f"not-prati-pratinidhi:{word}"'),
(93, 'if word.startswith("अधि") or word.startswith("परि"): return f"upasarga:adhi/parī;word={word}"', 'return f"not-adhi-parī:{word}"'),
(94, 'if word.startswith("सु") or pos=="su-pūjā": return f"upasarga:su;word={word}"', 'return f"not-su-pūjā:{word}"'),
(95, 'if word.startswith("अति") or pos=="ati-atikramaṇa": return f"upasarga:ati;word={word}"', 'return f"not-ati-atikramaṇa:{word}"'),
(96, 'if word=="अपि" or pos.startswith("api"): return f"nipāta:api;word={word}"', 'return f"not-api:{word}"'),
(97, 'if word.startswith("अधि") or pos=="adhi-īśvara": return f"upasarga:adhi;īśvara;word={word}"', 'return f"not-adhi-īśvara:{word}"'),
(98, 'if pos in ("kṛñ","kṛñ-optional"): return f"viBhāṣā:kṛñ;word={word}"', 'return f"not-kṛñ:{word}"'),
(99, 'if pos in ("parasmaipada","la"): return f"parasmaipada;word={word}"', 'return f"not-parasmaipada:{word}"'),
(100, 'if pos in ("ātmanepada","taṅ","ānāu"): return f"ātmanepada;word={word}"', 'return f"not-ātmanepada:{word}"'),
(101, 'if pos in ("prathama","madhyama","uttama","tiṅ"): return f"tiṅ:purusha;pos={pos};word={word}"', 'return f"not-tiṅ:{word}"'),
(102, 'if pos in ("ekavacana","dvivacana","bahuvacana"): return f"tiṅ:number;pos={pos};word={word}"', 'return f"not-tiṅ-number:{word}"'),
(103, 'if pos=="sup": return f"sup;word={word}"', 'return f"not-sup:{word}"'),
(104, 'if pos in ("vibhakti","sup"): return f"vibhakthi;word={word}"', 'return f"not-vibhakthi:{word}"'),
(105, 'if pos in ("yusmad","madhyama") or word=="युष्मद्": return f"purusha:madhyama;word={word}"', 'return f"not-madhyama-yusmad:{word}"'),
(106, 'if pos in ("prahāsa-manyā","uttama-ekavacana"): return f"purusha:uttama;manyā;word={word}"', 'return f"not-prahāsa-manyā:{word}"'),
(107, 'if pos in ("asmad","uttama") or word=="अस्मद्": return f"purusha:uttama;asmad;word={word}"', 'return f"not-uttama-asmad:{word}"'),
(108, 'if pos in ("prathama","śeṣa"): return f"purusha:prathama;word={word}"', 'return f"not-prathama:{word}"'),
]

desc_L = {
56:'P.1.4.56 प्राग्रीश्वरान्निपाताः — nipāta before īśvara',
57:'P.1.4.57 चादयोऽसत्त्वे — ca-ādi in asattva',
58:'P.1.4.58 प्रादयः — prādi = upasarga',
59:'P.1.4.59 उपसर्गाः क्रियायोगे — upasarga with action',
60:'P.1.4.60 गतिश्च — gati also = upasarga',
61:'P.1.4.61 ऊर्यादिच्विडाचश्च — ūryādi/cviḍāca',
62:'P.1.4.62 अनुकरणं चानितिपरम् — imitation = upasarga',
63:'P.1.4.63 आदरानादरयोः सदसती — sad/asat = abhiniveśa',
64:'P.1.4.64 भूषणेऽलम् — alam = upasarga',
65:'P.1.4.65 अन्तरपरिग्रहे — antara = upasarga',
66:'P.1.4.66 कणेमनसी श्रद्धाप्रतीघाते — kaṇa/manas in śraddhā',
67:'P.1.4.67 पुरोऽव्ययम् — purā = avyaya',
68:'P.1.4.68 अस्तं च — astam = avyaya',
69:'P.1.4.69 अच्छ गत्यर्थवदेषु — accha + gati = upasarga',
70:'P.1.4.70 अदोऽनुपदेशे — adas in non-teaching',
71:'P.1.4.71 तिरोऽन्तर्द्धौ — tiras in antarddhi',
72:'P.1.4.72 विभाषा कृञि — optional in kṛñ',
73:'P.1.4.73 उपाजेऽन्वाजे — upāja and anvāja',
74:'P.1.4.74 साक्षात्प्रभृतीनि च — sākṣāt and following',
75:'P.1.4.75 अनत्याधान उरसिमनसी — uraḥ/manas',
76:'P.1.4.76 मध्ये पदे निवचने च — middle of pada / nivacana',
77:'P.1.4.77 नित्यं हस्ते पाणावुपयमने — hasta/pāṇi',
78:'P.1.4.78 प्राध्वं बन्धने — prādhu in binding',
79:'P.1.4.79 जीविकोपनिषदावौपम्ये — jīvikā/upaniṣad',
80:'P.1.4.80 ते प्राग्धातोः — te before dhātu',
81:'P.1.4.81 छन्दसि परेऽपि — also in Vedic when following',
82:'P.1.4.82 व्यवहिताश्च — also when separated',
83:'P.1.4.83 कर्मप्रवचनीयाः — karmapravacanīya definition',
84:'P.1.4.84 अनुर्लक्षणे — anu in lakṣaṇa',
85:'P.1.4.85 तृतीयार्थे — in third case sense',
86:'P.1.4.86 हीने — in deficiency',
87:'P.1.4.87 उपोऽधिके च — upa in excess',
88:'P.1.4.88 अपपरी वर्जने — apa/parī in abandonment',
89:'P.1.4.89 आङ् मर्यादावचने — āṅ in limit sense',
90:'P.1.4.90 लक्षणेत्थम्भूताख्यानभागवीप्सासु — pratipar',
91:'P.1.4.91 अभिरभागे — abhi in part sense',
92:'P.1.4.92 प्रतिः प्रतिनिधिप्रतिदानयोः — prati',
93:'P.1.4.93 अधिपरी अनर्थकौ — adhi/parī meaningless',
94:'P.1.4.94 सुः पूजायाम् — su in worship',
95:'P.1.4.95 अतिरतिक्रमणे च — ati in transgression',
96:'P.1.4.96 अपिः पदार्थसम्भावनान्ववसर्गगर्हासमुच्चयेषु — api',
97:'P.1.4.97 अधिरीश्वरे — adhi in lordship',
98:'P.1.4.98 विभाषा कृञि — optional in kṛñ',
99:'P.1.4.99 लः परस्मैपदम् — lakārāḥ = parasmaipada',
100:'P.1.4.100 तङानावात्मनेपदम् — taṅ+ānāu = ātmanepada',
101:'P.1.4.101 तिङस्त्रीणि त्रीणि प्रथममध्यमोत्तमाः — tiṅ person',
102:'P.1.4.102 तान्येकवचनद्विवचनबहुवचनान्येकशः — tiṅ number',
103:'P.1.4.103 सुपः — sup',
104:'P.1.4.104 विभक्तिश्च — vibhakti = sup',
105:'P.1.4.105 युष्मद्युपपदे मध्यमः — madhyama with yusmad',
106:'P.1.4.106 प्रहासे च मन्योपपदे — uttama with manyā',
107:'P.1.4.107 अस्मद्युत्तमः — asmad → uttama',
108:'P.1.4.108 शेषे प्रथमः — śeṣa → prathama',
}

# Build content using f-strings
lines = []
A = lines.append
def AL(s):
 lines.append(s.lstrip())
AL('"""Shared logic for the 110 sutras of P.1.4.x — paribhāṣā, liṅga, saṅkhyā,')
AL('kāraka, and upasarga definitions.')
AL('')
AL('Each P_1_4_X.py imports apply_* from here. Functions are small, pure,')
AL('operate on Devanagari strings (no SLP1).')
AL('')
AL(' Sections:')
AL(' P.1.4.1-2 paribhāṣā | 3-9 liṅga | 10-12 laghu-guru')
AL(' 13-14 aṅga/pada | 15-20 misc | 21-22 saṅkhyā | 23 kāraka')
AL(' 24-51 kāraka relations | 52-55 kartṛ | 56-108 upasarga/puruṣa/vibhakti')
AL(' 109-110 sandhi / virāma')
AL('"""')
AL('from __future__ import annotations')
AL('')
AL('# ------------------ Phoneme inventory (Devanagari only) ------------------')
AL('VRDDHI = {"आ","ऐ","औ"}')
AL('GUNA = {"अ","ए","ओ"}')
AL('IK = {"इ","उ","ऋ","ऌ"}')
AL('IK_ALL = IK | {"ई","ऊ","ॠ","ॡ"}')
AL('AC = VRDDHI | GUNA | IK_ALL')
AL('HAL = set("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")')
AL('')
AL(T + 'def saMjna(word, pos=""):')
AL(T*2 + '"""Return (word, pos) as saṃjñā tuple."""')
AL(T*2 + 'return (word, pos or "saṃjñā")')
AL('')
AL('# =====================================================================')
AL('# SECTION A – P.1.4.1-2 paribhāṣā (meta-rules)')
AL('# =====================================================================')
AL('')
AL(T + 'def apply_1_4_1(word, pos=""):')
AL(T*2 + '"""P.1.4.1 आ कडारादेका संज्ञा — cluster gets ONE saṃjñā label."""')
AL(T*2 + 'clusters = []; i = 0')
AL(T*2 + 'while i < len(word) - 1:')
AL(T*3 + 'if word[i] in HAL and word[i+1] in HAL:')
AL(T*4 + 'j = i + 2')
AL(T*4 + 'while j < len(word) and word[j] in HAL:')
AL(T*5 + 'j += 1')
AL(T*4 + 'clusters.append(word[i:j]); i = j')
AL(T*3 + 'else:')
AL(T*4 + 'i += 1')
AL(T*2 + 'if clusters:')
AL(T*3 + 'sep = ","')
AL(T*3 + 'return f"saṃjñā=single;cluster={sep.join(clusters)};word={word}"')
AL(T*2 + 'return f"no-kaḍāra:{word}"')
AL('')
AL(T + 'def apply_1_4_2(word, pos=""):')
AL(T*2 + '"""P.1.4.2 विप्रतिषेधे परं कार्यम् — later rule wins on conflict."""')
AL(T*2 + 'if pos == "conflict":')
AL(T*3 + 'if "|" in word:')
AL(T*4 + 'p = word.split("|", 1)')
AL(T*4 + 'return f"conflict:{p[0]}+{p[1]};winner={p[1]};para"')
AL(T*3 + 'return f"conflict:{word};winner=later-rule"')
AL(T*2 + 'return f"no-conflict:{word}"')
AL('')
AL('# =====================================================================')
AL('# SECTION B – P.1.4.3-9 liṅga (grammatical gender / stem class)')
AL('# =====================================================================')
AL('')
AL(T+'def apply_1_4_3(word, pos=""):')
AL(T*2+'"""P.1.4.3 यू स्त्र्याख्यौ नदी — यू/य ending = नदी (feminine) stem."""')
AL(T*2+'if word.endswith("यू") or word.endswith("य"):')
AL(T*3+'if pos in ("stri","feminine","nadee") or "स्त्री" in pos:')
AL(T*4+'end = "यू" if word.endswith("यू") else "य"')
AL(T*4+'return f"liṅga=nadī-stem;ending={end};word={word}"')
AL(T*3+'return f"nadee-candidate:{word}"')
AL(T*2+'return f"not-nadee:{word}"')
AL('')
AL(T+'def apply_1_4_4(word, pos=""):')
AL(T*2+'"""P.1.4.4 नेयङुवङ्स्थानावस्त्री — stems in न/ण/ङ/ञ/न/म are NOT feminine."""')
AL(T*2+'if word.endswith("न") or word.endswith("ण") or word[-1:] in {"ङ","ञ","ण","न","म"}:')
AL(T*3+'return f"not-nadee:stems-na-or-N/U/NG;word={word}"')
AL(T*2+'return f"not-exempt:{word}"')
AL('')
AL(T+'def apply_1_4_5(word, pos=""):')
AL(T*2+'"""P.1.4.5 वाऽऽमि — optionally इ before अमि (acc dual/pl ending)."""')
AL(T*2+'if word.endswith("इमि") or word.endswith("मि") or word.endswith("अमि"):')
AL(T*3+'return f"vā-mī:context;form={word}"')
AL(T*2+'return f"no-amī-ending:{word}"')
AL('')
AL(T+'def apply_1_4_6(word, pos=""):')
AL(T*2+'"""P.1.4.6 ङिति ह्रस्वश्च — short vowel also = ङित marker."""')
AL(T*2+'last = word[-1] if word else ""')
AL(T*2+'if last in IK: return f"hrasva=short;last={last};ṅit={word}"')
AL(T*2+'if last in HAL:')
AL(T*3+'for ch in reversed(word):')
AL(T*4+'if ch in IK_ALL and ch not in VRDDHI | GUNA:')
AL(T*5+'return f"hrasva=short;preceding={ch};ṅit={word}"')
AL(T*4+'if ch in GUNA | VRDDHI: return f"hrasva=long;preceding={ch};word={word}"')
AL(T*4+'if ch in HAL: continue')
AL(T*4+'break')
AL(T*2+'return f"no-vowel:{word}"')
AL('')
AL(T+'def apply_1_4_7(word, pos=""):')
AL(T*2+'"""P.1.4.7 शेषो घ्यसखि — remaining cases use घ्यसखि genitive."""')
AL(T*2+'if word.endswith("स्य") or word.endswith("यः") or word.endswith("ष"):')
AL(T*3+'return f"ṣeṣa:ghyasakhi;form={word}"')
AL(T*2+'return f"ṣeṣa-candidate:{word}"')
AL('')
AL(T+'def apply_1_4_8(word, pos=""):')
AL(T*2+'"""P.1.4.8 पतिः समास एव — पति valid ONLY in compounds."""')
AL(T*2+'if word == "पति" or word.startswith("पति"):')
AL(T*3+'if pos == "samāsa": return f"pati:compound-valid;word={word}"')
AL(T*3+'return f"pati:compound-only;rejected={word}"')
AL(T*2+'return f"not-pati:{word}"')
AL('')
AL(T+'def apply_1_4_9(word, pos=""):')
AL(T*2+'"""P.1.4.9 षष्ठीयुक्तश्छन्दसि वा — optionally in Vedic with 6th case."""')
AL(T*2+'if pos == "chandas" or "वेद" in pos: return f"ṣaṣṭhī-vedic;word={word}"')
AL(T*2+'return f"ṣaṣṭhī-standard:{word}"')
AL('')
AL('# =====================================================================')
AL('# SECTION C – P.1.4.10-12 laghu / guru (syllable weight)')
AL('# =====================================================================')
AL('')
AL(T+'def apply_1_4_10(word, pos=""):')
AL(T*2+'"""P.1.4.10 ह्रस्वं लघु — short vowel = laghu syllable."""')
AL(T*2+'sv = {"अ","इ","उ","ऋ","ऌ"}; lv = {"ई","ऊ","ए","ओ","ऐ","औ","ॠ","ॡ"}')
AL(T*2+'laghu = sum(1 for c in word if c in sv); guru = sum(1 for c in word if c in lv)')
AL(T*2+'return f"syllable-weight:laghu={laghu};guru={guru};word={word}"')
AL('')
AL(T+'def apply_1_4_11(word, pos=""):')
AL(T*2+'"""P.1.4.11 संयोगे गुरु — consonant cluster = guru syllable."""')
AL(T*2+'pairs = [a+b for a,b in zip(word, word[1:]) if a in HAL and b in HAL]')
AL(T*2+'sep = ","')
AL(T*2+'if pairs: return f"saṃyoga:guru;clusters={sep.join(pairs)};word={word}"')
AL(T*2+'return f"no-saṃyoga:laghu;word={word}"')
AL('')
AL(T+'def apply_1_4_12(word, pos=""):')
AL(T*2+'"""P.1.4.12 दीर्घं च — long vowel also makes syllable heavy."""')
AL(T*2+'lv = {"ई","ऊ","ए","ओ","ऐ","औ","ॠ","ॡ"}')
AL(T*2+'found = [c for c in word if c in lv]')
AL(T*2+'sep = ","')
AL(T*2+'if found: return f"dīrgha=guru;vowels={sep.join(found)};word={word}"')
AL(T*2+'return f"no-dīrgha:{word}"')
AL('')
AL('# =====================================================================')
AL('# SECTION D – P.1.4.13-14 aṅga, pada')
AL('# =====================================================================')
AL('')
AL(T+'def apply_1_4_13(word, pos=""):')
AL(T*2+'"""P.1.4.13 यस्मात् प्रत्ययविधिस्तदादि — pratyaya target = aṅga."""')
AL(T*2+'SUFFIXES = ("तिप्","तस्","झि","सिप्","थ","मिप्","वस्","मस्",')
AL(T*3+'"सु","औ","जस्","ङा","भ्याम्","भिस्","ङे","भ्यः",')
AL(T*3+'"ङसि","भ्यस्","ङस्","आम्","ङि","ओस्","सुप्")')
AL(T*2+'for sfx in SUFFIXES:')
AL(T*3+'if word.endswith(sfx):')
AL(T*4+'aṅga = word[:-len(sfx)]')
AL(T*4+'return f"aṅga={aṅga};pratyaya={sfx};word={word}"')
AL(T*2+'return f"no-pratyaya:aṅga=full={word}"')
AL('')
AL(T+'def apply_1_4_14(word, pos=""):')
AL(T*2+'"""P.1.4.14 सुप्तिङन्तं पदम् — ending in sup or tiṅ = pada."""')
AL(T*2+'SUP_LIST = {"सु","औ","जस्","ङा","भ्याम्","भिस्","ङे","भ्यः",')
AL(T*3+'"ङसि","भ्यस्","ङस्","आम्","ङि","ओस्","सुप्"}')
AL(T*2+'TIṄ_LIST = {"तिप्","तस्","झि","सिप्","थ","मिप्","वस्","मस्",')
AL(T*3+'"त","आताम्","झ","थास्","आथाम्","ध्वम्","इट्","वहि","महिङ्"}')
AL(T*2+'for sfx in SUP_LIST:')
AL(T*3+'if word.endswith(sfx): return f"pada:sup={sfx};{word}"')
AL(T*2+'for sfx in TIṄ_LIST:')
AL(T*3+'if word.endswith(sfx): return f"pada:tiṅ={sfx};{word}"')
AL(T*2+'return f"not-pada:{word}"')
AL('')
AL('# =====================================================================')
AL('# SECTION E – P.1.4.15-20 miscellaneous')
AL('# =====================================================================')
AL('')
AL(T+'def apply_1_4_15(word, pos=""):')
AL(T*2+'"""P.1.4.15 नः क्ये — न does NOT go before क्य (acc pl marker)."""')
AL(T*2+'if word.endswith("नक्य") or word.endswith("न्क्य"):')
AL(T*3+'return f"n→∅-before-kya:form={word};blocked"')
AL(T*2+'return f"no-na-kya:{word}"')
AL('')
AL(T+'def apply_1_4_16(word, pos=""):')
AL(T*2+'"""P.1.4.16 सिति च — न-block also before सित् (siT marker)."""')
AL(T*2+'if word.endswith("सित्") or word.endswith("सित"):')
AL(T*3+'return f"na-blocked:before-sit;form={word}"')
AL(T*2+'return f"not-sit-context:{word}"')
AL('')
AL(T+'def apply_1_4_17(word, pos=""):')
AL(T*2+'"""P.1.4.17 स्वादिष्वसर्वनामस्थाने — स्वादि + असर्वनामस्थान."""')
AL(T*2+'SVADI = ("स्व","वस","हु","धू","ध्व","रुष","रु","लुष","ल","व","स्तो","स्थ","स्थू","स्क")')
AL(T*2+'for ini in SVADI:')
AL(T*3+'if word.startswith(ini): return f"svādi:as-sarvanāmasthāna;prefix={ini};{word}"')
AL(T*2+'return f"not-svādi:{word}"')
AL('')
AL(T+'def apply_1_4_18(word, pos=""):')
AL(T*2+'"""P.1.4.18 यचि भम् — यच् in sense of sṛj (causative)."""')
AL(T*2+'if word.endswith("यच्") or word.endswith("यच"):')
AL(T*3+'return f"yañ:sṛj-sense;causative={word}"')
AL(T*2+'return f"not-yañ-sṛj:{word}"')
AL('')
AL(T+'def apply_1_4_19(word, pos=""):')
AL(T*2+'"""P.1.4.19 तसौ मत्वर्थे — तस् in motion/opinion (matvartha) sense."""')
AL(T*2+'if word.endswith("तस्") or word.endswith("तस"):')
AL(T*3+'if pos in ("motion","opinion","matvartha"): return f"tas:matvartha;{word}"')
AL(T*3+'return f"tas:possibly-matvartha;{word}"')
AL(T*2+'return f"no-tas:{word}"')
AL('')
AL(T+'def apply_1_4_20(word, pos=""):')
AL(T*2+'"""P.1.4.20 अयस्मयादीनि च्छन्दसि — ayasmaya etc. in Vedic."""')
AL(T*2+'if word in {"अयस्मय","अग्निष्ठ","पृश्निगर्भ","वाजिन"} or pos=="chandas":')
AL(T*3+'return f"ayasmaya-ādi:vedic;word={word}"')
AL(T*2+'return f"not-ayasmaya:{word}"')
AL('')
AL('# =====================================================================')
AL('# SECTION F – P.1.4.21-22 saṅkhyā (number)')
AL('# =====================================================================')
AL('')
AL(T+'def apply_1_4_21(word, pos=""):')
AL(T*2+'"""P.1.4.21 बहुषु बहुवचनम् — plural (bahuvacana) with "many"."""')
AL(T*2+'if pos in ("bahuvacana","bahu"): return f"saṅkhyā=bahuvacana;word={word}"')
AL(T*2+'for m in ("भ्यः","भिस्","भ्यस्"):')
AL(T*3+'if word.endswith(m): return f"saṅkhyā=bahuvacana;marker={m};word={word}"')
AL(T*2+'return f"not-bahuvacana:{word}"')
AL('')
AL(T+'def apply_1_4_22(word, pos=""):')
AL(T*2+'"""P.1.4.22 द्व्येकयोर्द्विवचनैकवचने — dual for 2, singular for 1."""')
AL(T*2+'for m in ("औ","यौ","भ्याम्","ओस्"):')
AL(T*3+'if word.endswith(m): return f"saṅkhyā=dvivacana;dual;word={word}"')
AL(T*2+'for m in ("आम्","सु"):')
AL(T*3+'if word.endswith(m): return f"saṅkhyā=ekavacana;singular;word={word}"')
AL(T*2+'if pos in ("dvivacana","ekavacana"): return f"saṅkhyā={pos};word={word}"')
AL(T*2+'return f"no-number-marker:{word}"')
AL('')
AL('# =====================================================================')
AL('# SECTION G – P.1.4.23 kāraka definition')
AL('# =====================================================================')
AL('')
AL(T+'def apply_1_4_23(word, pos=""):')
AL(T*2+'"""P.1.4.23 कारके — definition of kāraka (6 case-relations)."""')
AL(T*2+'KT = ("apādāna","sampradānam","karaṇam","karman","kartṛ","hetu")')
AL(T*2+'if pos in KT: return f"kāraka={pos};word={word}"')
AL(T*2+'return f"kāraka-candidate:{word}"')
AL('')
AL('# =====================================================================')
AL('# SECTION H – P.1.4.24-51 kāraka relations')
AL('# =====================================================================')
AL('')

# Add kara_specs functions
for n, line1, line2 in kara_specs:
 blk = [T+f'def apply_1_4_{n}(word, pos=""):', T*2+f'"""{desc_H[n]}"""']
 for sub in line1.split(NL): blk.append(T*2+sub)
 blk.append(T*2+line2)
 blk.append('')
 AL(NL.join(blk))

AL('# =====================================================================')
AL('# SECTION K – P.1.4.52-55 kartṛ, ṇi, hetu')
AL('# =====================================================================')
AL('')
AL(T+'def apply_1_4_52(word, pos=""):')
AL(T*2+'"""P.1.4.52 …णि कर्ता — ṇi marks agent for gati/buddhi roots."""')
AL(T*2+'if pos=="kartṛ-ṇi": return f"kāraka=kartṛ;ṇi-marked;word={word}"')
AL(T*2+'return f"not-ṇi-kartṛ:{word}"')
AL('')
AL(T+'def apply_1_4_53(word, pos=""):')
AL(T*2+'"""P.1.4.53 हृक्रोरन्यतरस्याम् — optional for hṛ/kṛ."""')
AL(T*2+'if pos in ("kartṛ-hṛ","kartṛ-kṛ","kartṛ-hṛkṛ"): return f"kāraka=kartṛ;hṛ/kṛ;optional;word={word}"')
AL(T*2+'return f"not-hṛ-kṛ:{word}"')
AL('')
AL(T+'def apply_1_4_54(word, pos=""):')
AL(T*2+'"""P.1.4.54 स्वतन्त्रः कर्ता — kartṛ = svatantra (independent)."""')
AL(T*2+'if pos=="kartṛ": return f"kāraka=kartṛ;svatantra;word={word}"')
AL(T*2+'return f"possibly-kartṛ:{word}"')
AL('')
AL(T+'def apply_1_4_55(word, pos=""):')
AL(T*2+'"""P.1.4.55 तत्प्रयोजको हेतुश्च — instigator = hetu."""')
AL(T*2+'if pos=="hetu-prayojaka": return f"kāraka=hetu;prayojaka;word={word}"')
AL(T*2+'return f"not-prayojaka-hetu:{word}"')
AL('')
AL('# =====================================================================')
AL('# SECTION L – P.1.4.56-108 upasarga / avyaya / puruṣa / vibhakti')
AL('# =====================================================================')
AL('')

for n, line1, line2 in up_specs:
 blk = [T+f'def apply_1_4_{n}(word, pos=""):', T*2+f'"""{desc_L[n]}"""']
 for sub in line1.split(NL): blk.append(T*2+sub)
 blk.append(T*2+line2)
 blk.append('')
 AL(NL.join(blk))

AL('# =====================================================================')
AL('# SECTION M – P.1.4.109-110 sandhi and end-of-utterance')
AL('# =====================================================================')
AL('')
AL(T+'def apply_1_4_109(word, pos=""):')
AL(T*2+'"""P.1.4.109 परः सन्निकर्षः संहिता — close proximity = sandhi."""')
AL(T*2+'if pos=="sandhi": return f"sandhi:parah-sannikarṣaḥ;word={word}"')
AL(T*2+'return f"not-sandhi:{word}"')
AL('')
AL(T+'def apply_1_4_110(word, pos=""):')
AL(T*2+'"""P.1.4.110 विरामोऽवसानम् — virāma (pause) = avasānam (end)."""')
AL(T*2+'if pos in ("virāma","avasānam"): return f"virāma=avasānam;end;word={word}"')
AL(T*2+'return f"not-virāma:{word}"')
AL('')

content = NL.join(lines)
OUT.write_text(content, encoding='utf-8')

print(f"Wrote {OUT}")
print(f"Lines: {content.count(NL)}, Bytes: {len(content)}")

import ast
tree = ast.parse(content)
funcs = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith('apply_1_4_')]
print(f"Functions: {len(funcs)}")
nums = sorted(int(n.split('_')[-1]) for n in funcs)
print(f"Range: {nums[0]}-{nums[-1]}")
missing = sorted(set(range(1,111))-set(nums))
print(f"Missing: {missing if missing else 'none'}")
