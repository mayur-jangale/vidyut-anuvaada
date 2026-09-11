"""Chapter 2, Pada 1 of Panini's Ashtadhyayi - the samAsapAda.
72 sutras (P_2_1_1 through P_2_1_72).
All functions use TAB indentation.
"""
from __future__ import annotations

from vidyut_anuvaada.sutras.P_1_2 import (
	_classify_samasa,
	AVYAYIBHAVA_HEADS,
	DVANDVA_SEP,
	DVI_GU_NUM,
	KARMADHARAYA_SUFFIXES,
	KARMADHARAYA_PATTERNS,
	BAHU_HEADS,
	AVYAYA,
	NO_COMPOUND,
)


def _split_members(word):
	"""Best-effort split of a compound into (head, tail)."""
	hd = sorted(AVYAYIBHAVA_HEADS, key=len, reverse=True)
	for head in hd:
		if word.startswith(head) and len(word) > len(head):
			return [head, word[len(head):]]
	ah = sorted(DVI_GU_NUM, key=len, reverse=True)
	for head in ah:
		if word.startswith(head) and len(word) > len(head):
			return [head, word[len(head):]]
	for sep in DVANDVA_SEP:
		i = word.find(sep)
		if 0 < i < len(word) - 1:
			parts = word.split(sep)
			return [p for p in parts if p]
	# fallback: split on first capital-ish boundary or last 2-3 chars
	if len(word) > 4:
		return [word[:-3], word[-3:]]
	return [word]


def samasa_detect(word):
	"""Detect samāsa (compound) type for a single Devanagari word.

	Returns:
		dict with keys:
			type – one of the SAMASA_TYPES or "unknown"
			members – list of constituent strings
			confidence – float 0..1
			tag – "valid" | "invalid" | "unknown"
	"""
	if not word:
		return {"type": "unknown", "members": [], "confidence": 0.0, "tag": "invalid"}
	if word in NO_COMPOUND:
		return {"type": "unknown", "members": [word], "confidence": 0.3, "tag": "unknown"}

	ctype = _classify_samasa(word)
	members = _split_members(word)

	# confidence heuristics
	conf = 0.85
	if ctype == "अव्ययीभाव":
		conf = 0.92 if any(word.startswith(h) for h in AVYAYIBHAVA_HEADS) else 0.75
	elif ctype == "द्वन्द्व":
		conf = 0.9 if any(sep in word for sep in DVANDVA_SEP) else 0.6
	elif ctype == "तत्पुरुष":
		conf = 0.7 # default fallback

	return {
		"type": ctype,
		"members": members,
		"confidence": round(conf, 2),
		"tag": "valid",
	}


# ============================================================
# P_2_1_1 samarthaH padavidhiH
# ============================================================
def apply_2_1_1(word, pos="", SUTRA_TOKEN=""):
	"""समर्थः पदविधिः — Eligible words form compounds."""
	return f"प.2.1.1:compound-eligible;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_2 subhAmantrite parAggavat svare
# ============================================================
def apply_2_1_2(word, pos="", SUTRA_TOKEN=""):
	"""सुबामन्त्रिते पराङ्गवत् स्वरे — Svarupa in samasa."""
	return f"प.2.1.2:svarupa;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_3 prAk kaqArAt samAsaH
# ============================================================
def apply_2_1_3(word, pos="", SUTRA_TOKEN=""):
	"""प्राक् कडारात् समासः — Samasa before kaDAra."""
	return f"प.2.1.3:before-kaDAra;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_4 saha supA
# ============================================================
def apply_2_1_4(word, pos="", SUTRA_TOKEN=""):
	"""सह सुपा — Sah + sup = samasa."""
	return f"प.2.1.4:saha-supA;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_5 nityaM samAso.avyayasya
# ============================================================
def apply_2_1_5(word, pos="", SUTRA_TOKEN=""):
	"""नित्यं समासोऽव्ययस्य — Avyaya always forms samasa."""
	return f"प.2.1.5:nitya-avyaya-samasa;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_6 avyayamaviprakRSTena...
# ============================================================
def apply_2_1_6(word, pos="", SUTRA_TOKEN=""):
	"""अव्ययमविप्रकृष्टेन — Avyayibhava samasa."""
	return f"प.2.1.6:avyayibhava;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_7 yathAsAdRzyaM saMjJAyAM pUrvasya
# ============================================================
def apply_2_1_7(word, pos="", SUTRA_TOKEN=""):
	"""यथासादृश्यं संज्ञायां पूर्वस्य — yathA-sAdRzya in saMjJA."""
	return f"प.2.1.7:yathA-sAdRzya;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_8 yAvadavadhAraNe
# ============================================================
def apply_2_1_8(word, pos="", SUTRA_TOKEN=""):
	"""यावतवधारणे — yAvat boundary marker."""
	return f"प.2.1.8:yAvat-avadhAraNe;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_9 suH saMjJAyAm
# ============================================================
def apply_2_1_9(word, pos="", SUTRA_TOKEN=""):
	"""सुः संज्ञायाम् — su- marker in saMjJA."""
	return f"प.2.1.9:su-samjJAyAm;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_10 akSAzalAkAsaMjJAyAM puMsi saMjJAyAM
# ============================================================
def apply_2_1_10(word, pos="", SUTRA_TOKEN=""):
	"""अक्षशलाकासंज्ञायां पुंसि संज्ञायां — aksha-shAlakA saMjJA."""
	return f"प.2.1.10:aksha-shAlakA;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_11 vibhASehaH supeH
# ============================================================
def apply_2_1_11(word, pos="", SUTRA_TOKEN=""):
	"""विभाषेहः सुपेः — vibhASe haH supeH."""
	return f"प.2.1.11:vibhASe-haH-supeH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_12 apapAribahirAGgavat paJcamI
# ============================================================
def apply_2_1_12(word, pos="", SUTRA_TOKEN=""):
	"""अपपारिबहिराङ्गवत् पञ्चमी — apa-pari-bahir-aGgavat paJcamI."""
	return f"प.2.1.12:apa-pari-bahir-aGgavat;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_13 aGgmaryAdAbhividhau
# ============================================================
def apply_2_1_13(word, pos="", SUTRA_TOKEN=""):
	"""आङ्मर्यादाभिविधौ — aGg-maryAdA-abhividhi."""
	return f"प.2.1.13:aGg-maryAdA-abhividhi;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_14 lakSaNenAbhipratyAbhImukhyaH
# ============================================================
def apply_2_1_14(word, pos="", SUTRA_TOKEN=""):
	"""लक्षणेनाभिप्रतीत्याभीमुख्यः — lakSaNena-abhipratyAbhImukhyaH."""
	return f"प.2.1.14:lakSaNena-abhipratI;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_15 anuryat-samayA
# ============================================================
def apply_2_1_15(word, pos="", SUTRA_TOKEN=""):
	"""अनुर्यत्समया — anuryat-samayA."""
	return f"प.2.1.15:anuryat-samayA;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_16 yasyA cAyAmaH
# ============================================================
def apply_2_1_16(word, pos="", SUTRA_TOKEN=""):
	"""यस्य चायामः — yasyA cAyAmaH."""
	return f"प.2.1.16:yasyA-cAyAmaH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_17 tiSThadgu-prabhRtIni ca
# ============================================================
def apply_2_1_17(word, pos="", SUTRA_TOKEN=""):
	"""तिष्ठद्गुप्रभृतीनि च — tiSThadgu-prabhRtIni ca."""
	return f"प.2.1.17:tiSThadgu-prabhRtIni;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_18 pAre madhye SaSThyA vA
# ============================================================
def apply_2_1_18(word, pos="", SUTRA_TOKEN=""):
	"""पारे मध्ये षष्ठ्या वा — pAre-madhye-SaSThyA-vA."""
	return f"प.2.1.18:pAre-madhye;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_19 saMkhyA vaMSyena
# ============================================================
def apply_2_1_19(word, pos="", SUTRA_TOKEN=""):
	"""संख्या वंश्येन — saMkhyA vaMSyena."""
	return f"प.2.1.19:saMkhyA-vaMSyena;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_20 nadIbhiSca
# ============================================================
def apply_2_1_20(word, pos="", SUTRA_TOKEN=""):
	"""नदीभिश्च — nadIbhiSca. Tatpurusha samasa."""
	return f"प.2.1.20:nadIbhishca;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_21 anyapadArthe ca saMjJAyAm
# ============================================================
def apply_2_1_21(word, pos="", SUTRA_TOKEN=""):
	"""अन्यपदार्थे च संज्ञायाम् — anyapadArthe-ca-saMjJAyAm."""
	return f"प.2.1.21:anyapadArthe-ca-saMjJA;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_22 tatpuruSaH
# ============================================================
def apply_2_1_22(word, pos="", SUTRA_TOKEN=""):
	"""तत्पुरुषः — Tatpurusha samasa."""
	return f"प.2.1.22:tatpuruSaH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_23 dviguSca
# ============================================================
def apply_2_1_23(word, pos="", SUTRA_TOKEN=""):
	"""द्विगुश्च — dviguSca (number + noun = dvigu)."""
	return f"प.2.1.23:dviguSca;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_24 dvitIyAzritAtItapatitagatAtyastaprAptApannaiH
# ============================================================
def apply_2_1_24(word, pos="", SUTRA_TOKEN=""):
	"""द्वितीयाश्रितातीतपतितगतात्यस्तप्राप्तापन्नैः — dvitIyAzritAtIta... tatpuruSa."""
	return f"प.2.1.24:dvitIyAzritAtIta;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_25 svayaMktena
# ============================================================
def apply_2_1_25(word, pos="", SUTRA_TOKEN=""):
	"""स्वयंक्तेन — svayaMktena (self-declared)."""
	return f"प.2.1.25:svayaMktena;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_26 khaTvAkSepe
# ============================================================
def apply_2_1_26(word, pos="", SUTRA_TOKEN=""):
	"""खट्वाक्षेपे — khaTvAkSepe (khatvA kSepa)."""
	return f"प.2.1.26:khaTvAkSepe;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_27 sAmi
# ============================================================
def apply_2_1_27(word, pos="", SUTRA_TOKEN=""):
	"""सामि — sAmi (equality marker)."""
	return f"प.2.1.27:sAmi;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_28 kAla-tatpuruSa
# ============================================================
def apply_2_1_28(word, pos="", SUTRA_TOKEN=""):
	"""कालतत्पुरुषः — kAla-tatpuruSa (time compound)."""
	return f"प.2.1.28:kAla-tatpuruSa;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_29 dvandvaH
# ============================================================
def apply_2_1_29(word, pos="", SUTRA_TOKEN=""):
	"""द्वन्द्वः — Dvandva samasa."""
	return f"प.2.1.29:dvandvaH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_30 tRtIyAtatkRtArthena guNavacanena
# ============================================================
def apply_2_1_30(word, pos="", SUTRA_TOKEN=""):
	"""तृतीयातत्कृतार्थेन गुणवचनेन — tRtIyA-tatkRtArthena-guNavacanena."""
	return f"प.2.1.30:tRtIyA-tatkRtArthena;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_31 pUrvasadRza-sama-artha-kalAha-nipuNa-miSra-zlakSaNaiH
# ============================================================
def apply_2_1_31(word, pos="", SUTRA_TOKEN=""):
	"""पूर्वसदृशसमार्थकलाहनिपूणमिश्रश्लक्ष्णैः — pUrva-sadRza-sama-artha-kalAha-nipuNa-miSra-zlakSaNaiH."""
	return f"प.2.1.31:pUrva-sadRza-sama;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_32 kartRkaraNe kRtA bahulam
# ============================================================
def apply_2_1_32(word, pos="", SUTRA_TOKEN=""):
	"""कर्तृकरणे कृता बहुलम् — kartRkaraNe kRtA bahulam."""
	return f"प.2.1.32:kartRkaraNe-kRtA;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_33 kRtyair-adhikArtha-vacane
# ============================================================
def apply_2_1_33(word, pos="", SUTRA_TOKEN=""):
	"""कृत्यैरधिकार्थवचने — kRtyair-adhikArtha-vacane."""
	return f"प.2.1.33:kRtyair-adhikArtha;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_34 anna-vyaJjanam
# ============================================================
def apply_2_1_34(word, pos="", SUTRA_TOKEN=""):
	"""अन्नव्यञ्जनम् — anna-vyaJjanam."""
	return f"प.2.1.34:anna-vyaJjanam;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_35 bhakSya-miSrIkaraNam
# ============================================================
def apply_2_1_35(word, pos="", SUTRA_TOKEN=""):
	"""भक्ष्यमिश्रीकरणम् — bhakSya-miSrIkaraNam."""
	return f"प.2.1.35:bhakSya-miSrIkaraNam;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_36 caturthI tadarthArtha-bali-hita-sukha-rakSitaiH
# ============================================================
def apply_2_1_36(word, pos="", SUTRA_TOKEN=""):
	"""चतुर्थी तदर्थार्थबलिहितसुखरक्षितैः — caturthI-tadarthArtha-bali-hita-sukha-rakSitaiH."""
	return f"प.2.1.36:caturthI-tadarthArtha;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_37 paJcamI-bhaya
# ============================================================
def apply_2_1_37(word, pos="", SUTRA_TOKEN=""):
	"""पञ्चमी भय — paJcamI-bhaya."""
	return f"प.2.1.37:paJcamI-bhaya;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_38 apetA-poSTha-mukta-patitApatra-stair-alpaSaH
# ============================================================
def apply_2_1_38(word, pos="", SUTRA_TOKEN=""):
	"""अपेतापोढमुक्तपतितापत्रस्थैरल्पशः — apetA-poSTha-mukta-patitApatra-stair-alpaSaH."""
	return f"प.2.1.38:apetA-poSTha-mukta;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_39 stoka-antika-dUra-ktA
# ============================================================
def apply_2_1_39(word, pos="", SUTRA_TOKEN=""):
	"""स्तोकान्तिकदूरक्ताः — stoka-antika-dUra-ktA."""
	return f"प.2.1.39:stoka-antika-dUra;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_40 saptamI-zauNDaiH
# ============================================================
def apply_2_1_40(word, pos="", SUTRA_TOKEN=""):
	"""सप्तम्यौण्डैः — saptamI-zauNDaiH."""
	return f"प.2.1.40:saptamI-zauNDaiH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_41 siddha-zUkha-pakva-bandhaiSca
# ============================================================
def apply_2_1_41(word, pos="", SUTRA_TOKEN=""):
	"""सिद्धशुष्कपक्वबन्धैश्च — siddha-zUkha-pakva-bandhaiSca."""
	return f"प.2.1.41:siddha-zUkha-pakva;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_42 dhvAGkSeNa-kSepe
# ============================================================
def apply_2_1_42(word, pos="", SUTRA_TOKEN=""):
	"""ध्वाङ्क्षेण क्षेपे — dhvAGkSeNa-kSepe."""
	return f"प.2.1.42:dhvAGkSeNa-kSepe;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_43 kRtyai-rRe
# ============================================================
def apply_2_1_43(word, pos="", SUTRA_TOKEN=""):
	"""कृत्यैर्ऋणे — kRtyai-rRe."""
	return f"प.2.1.43:kRtyai-rRe;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_44 saMjJAyAm
# ============================================================
def apply_2_1_44(word, pos="", SUTRA_TOKEN=""):
	"""संज्ञायाम् — saMjJAyAm (in technical designation)."""
	return f"प.2.1.44:saMjJAyAm;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_45 ktena-ahorAtra
# ============================================================
def apply_2_1_45(word, pos="", SUTRA_TOKEN=""):
	"""क्तेनाहोरात्र — ktena-ahorAtra."""
	return f"प.2.1.45:ktena-ahorAtra;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_46 tatra-tatpuruSa
# ============================================================
def apply_2_1_46(word, pos="", SUTRA_TOKEN=""):
	"""तत्र तत्पुरुषः — tatra-tatpuruSa."""
	return f"प.2.1.46:tatra-tatpuruSa;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_47 kSepa-tatpuruSa
# ============================================================
def apply_2_1_47(word, pos="", SUTRA_TOKEN=""):
	"""क्षेप तत्पुरुषः — kSepa-tatpuruSa."""
	return f"प.2.1.47:kSepa-tatpuruSa;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_48 pAtra-samita
# ============================================================
def apply_2_1_48(word, pos="", SUTRA_TOKEN=""):
	"""पात्रसमितः — pAtra-samita."""
	return f"प.2.1.48:pAtra-samita;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_49 pUrvakAla-eka-sarva-jaraT-purANa-nava-kevalaH
# ============================================================
def apply_2_1_49(word, pos="", SUTRA_TOKEN=""):
	"""पूर्वकालैकसर्वजरल्पुराणनवकेवलाः — pUrvakAla-eka-sarva-jaraT-purANa-nava-kevalaH. Dvigu samasa (number + noun)."""
	return f"प.2.1.49:pUrvakAla-dvigu;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_50 dik-saMkhyA-saMjJA
# ============================================================
def apply_2_1_50(word, pos="", SUTRA_TOKEN=""):
	"""दिक्संख्याsaंज्ञाः — dik-saMkhyA-saMjJA (direction, number, designation)."""
	return f"प.2.1.50:dik-saMkhyA-saMjJA;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_51 bahuvrIhiH
# ============================================================
def apply_2_1_51(word, pos="", SUTRA_TOKEN=""):
	"""बहुव्रीहिः — Bahuvrihi samasa."""
	return f"प.2.1.51:bahuvrIhiH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_52 saMkhyA pUrvo dviguH
# ============================================================
def apply_2_1_52(word, pos="", SUTRA_TOKEN=""):
	"""संख्या पूर्वो द्विगुः — saMkhyA pUrvo dviguH."""
	return f"प.2.1.52:saMkhyA-pUrvo-dviguH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_53 kutsitAni kutsanaiH
# ============================================================
def apply_2_1_53(word, pos="", SUTRA_TOKEN=""):
	"""कुत्सितानि कुत्सनैः — kutsitAni kutsanaiH."""
	return f"प.2.1.53:kutsitAni-kutsanaiH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_54 pApANake kutsitaiH
# ============================================================
def apply_2_1_54(word, pos="", SUTRA_TOKEN=""):
	"""पापाणके कुत्सितैः — pApANake kutsitaiH."""
	return f"प.2.1.54:pApANake-kutsitaiH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_55 upamAnAni sAmAnyavacanaiH
# ============================================================
def apply_2_1_55(word, pos="", SUTRA_TOKEN=""):
	"""उपमानानि सामान्यवचनैः — upamAnAni sAmAnyavacanaiH. Karmadharaya samasa."""
	return f"प.2.1.55:upamAnAni-sAmAnyavacanaiH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_56 upamitaM vyAghrAdibhiH
# ============================================================
def apply_2_1_56(word, pos="", SUTRA_TOKEN=""):
	"""उपमितं व्याघ्रादिभिः — upamitaM vyAghrAdibhiH (simile compound)."""
	return f"प.2.1.56:upamitaM-vyAghrAdibhiH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_57 viSesaNaM-viSeyeNa bahulam
# ============================================================
def apply_2_1_57(word, pos="", SUTRA_TOKEN=""):
	"""विशेषणंविशेषेण बहुलम् — viSesaNaM-viSeyeNa bahulam."""
	return f"प.2.1.57:viSesaNaM-viSeyeNa;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_58 pUrvApara-prathama-carama-jaghanya-samAna-madhya-madhyavIrAzca
# ============================================================
def apply_2_1_58(word, pos="", SUTRA_TOKEN=""):
	"""पूर्वापरप्रथमचरमजघन्यसमानमध्यमध्यवीराश्च — pUrvApara-prathama-carama-jaghanya-samAna-madhya-madhyavIrAzca."""
	return f"प.2.1.58:pUrvApara-prathama;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_59 zreNyAdayaH kRtAdibhiH
# ============================================================
def apply_2_1_59(word, pos="", SUTRA_TOKEN=""):
	"""श्रेण्यादयः कृतादिभिः — zreNyAdayaH kRtAdibhiH."""
	return f"प.2.1.59:zreNyAdayaH-kRtAdibhiH;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_60 ktena-naJ-viSiSTenAnaJ
# ============================================================
def apply_2_1_60(word, pos="", SUTRA_TOKEN=""):
	"""क्तेनाञ्विशिष्टेनाञः — ktena-naJ-viSiSTenAnaJ."""
	return f"प.2.1.60:ktena-naJ-viSiSTena;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_61 san-mahat-parama-uttama-utkRSTA
# ============================================================
def apply_2_1_61(word, pos="", SUTRA_TOKEN=""):
	"""सन्महत्परमोत्तमोत्कृष्टाः — san-mahat-parama-uttama-utkRSTA."""
	return f"प.2.1.61:san-mahat-parama;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_62 vRndAraka-nAga-kuJjaraiH
# ============================================================
def apply_2_1_62(word, pos="", SUTRA_TOKEN=""):
	"""वृन्दारकनागकुञ्जरैः — vRndAraka-nAga-kuJjaraiH."""
	return f"प.2.1.62:vRndAraka-nAga-kuJjara;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_63 katara-katamau
# ============================================================
def apply_2_1_63(word, pos="", SUTRA_TOKEN=""):
	"""कतरकतमौ — katara-katamau."""
	return f"प.2.1.63:katara-katamau;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_64 kiM-kSepe
# ============================================================
def apply_2_1_64(word, pos="", SUTRA_TOKEN=""):
	"""किं क्षेपे — kiM-kSepe."""
	return f"प.2.1.64:kiM-kSepe;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_65 poTA-yuvati
# ============================================================
def apply_2_1_65(word, pos="", SUTRA_TOKEN=""):
	"""पोटा युवति — poTA-yuvati."""
	return f"प.2.1.65:poTA-yuvati;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_66 prazaMsA-vacanaiSca
# ============================================================
def apply_2_1_66(word, pos="", SUTRA_TOKEN=""):
	"""प्रशंसावचनैश्च — prazaMsA-vacanaiSca."""
	return f"प.2.1.66:prazaMsA-vacanaiSca;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_67 yuvA-khalati-palita-valina-jaratIbhyaH
# ============================================================
def apply_2_1_67(word, pos="", SUTRA_TOKEN=""):
	"""युवाक्हलतिपलितवलिनजरतीभ्यः — yuvA-khalati-palita-valina-jaratIbhyaH."""
	return f"प.2.1.67:yuvA-khalati-palita;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_68 kRtya-tulyAhyA-ajAtyA
# ============================================================
def apply_2_1_68(word, pos="", SUTRA_TOKEN=""):
	"""कृत्यतुल्याख्याजात्या — kRtya-tulyAhyA-ajAtyA."""
	return f"प.2.1.68:kRtya-tulyAhyA-ajAtyA;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_69 varNo-varNena
# ============================================================
def apply_2_1_69(word, pos="", SUTRA_TOKEN=""):
	"""वर्णो वर्णेन — varNo-varNena."""
	return f"प.2.1.69:varNo-varNena;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_70 kumAraH-zramaNAdibhiH
# ============================================================
def apply_2_1_70(word, pos="", SUTRA_TOKEN=""):
	"""कुमारः श्रमणादिभिः — kumAraH-zramaNAdibhiH."""
	return f"प.2.1.70:kumAraH-zramaNAdi;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_71 catuSpAdo-garbhiNyA
# ============================================================
def apply_2_1_71(word, pos="", SUTRA_TOKEN=""):
	"""चतुष्पादो गर्भिण्या — catuSpAdo-garbhiNyA."""
	return f"प.2.1.71:catuSpAdo-garbhiNyA;input={word};pos={pos};token={SUTRA_TOKEN}"

# ============================================================
# P_2_1_72 mayUra-vyaMsakAdayaHca
# ============================================================
def apply_2_1_72(word, pos="", SUTRA_TOKEN=""):
	"""मयूरव्यंसकादयश्च — mayUra-vyaMsakAdayaHca."""
	return f"प.2.1.72:mayUra-vyaMsakAdayaH;input={word};pos={pos};token={SUTRA_TOKEN}"
