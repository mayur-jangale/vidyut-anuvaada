"""Shared logic for the 110 sutras of P.1.4.x - paribhasha, linga, sankhya,
karaka, and upasarga definitions.

Each P_1_4_X.py imports apply_* from here. Functions are small, pure,
operate on Devanagari strings (no SLP1).

Sections:
P.1.4.1-2 paribhasha | 3-9 linga | 10-12 laghu-guru
13-14 anga/pada | 15-20 misc | 21-22 sankhya | 23 karaka
24-51 karaka relations | 52-55 kartri | 56-108 upasarga/purusa/vibhakti
109-110 sandhi / virama
"""
from __future__ import annotations

# ------------------ Phoneme inventory (Devanagari only) ------------------
VRDDHI = {"ॎ", "ॏ", "॑"}
GUNA = {"े", "ो", "॒"}
IK = {"अ", "आ", "ि", "ी"}
IK_ALL = IK | {"इ", "ई", "उ", "ऊ"}
AC = VRDDHI | GUNA | IK_ALL
HAL = set("\u0915\u0916\u0917\u0918\u0919\u091a\u091b\u091c\u091d\u091e"
 "\u091f\u0920\u0921\u0922\u0923\u0924\u0925\u0926\u0927\u0928\u092a\u092b\u092c\u092d\u092e"
 "\u092f\u0930\u0932\u0933\u0934\u0935\u0936\u0937\u0938\u0939")


def saMjna(word, pos=""):
	"""Return (word, pos) as samanya/jnana tuple."""
	return (word, pos or "samanya")

# =====================================================================
# SECTION A P.1.4.1-2 paribhasha (meta-rules)
# =====================================================================


def apply_1_4_1(word, pos=""):
	"""P.1.4.1 A kaqAradekA saMjYA |
	Single technical definition from a cluster."""
	if not word:
		return "empty:no-samjna"
	known = {"puM", "strI", "napuMsakam", "sup", "tiG", "sambodhana"}
	for k in known:
		if k in word:
			return f"samjna={k};from=cluster;word={word}"
	return f"no-cluster-samjna:{word}"


def apply_1_4_2(word, pos=""):
	"""P.1.4.2 vipratiSedhe paraM kAryam |
	When two rules conflict, the later one wins."""
	prior = "P.1.1."
	later = "P.1.4."
	if pos == "conflict":
		return f"later-wins:{later}>{prior};word={word}"
	return f"no-conflict:{word}"

# =====================================================================
# SECTION B P.1.4.3-9 linga (gender)
# =====================================================================


def apply_1_4_3(word, pos=""):
	"""P.1.4.3 yU stryAKyO nadI |
	Feminine words ending in yU/y are called nadI."""
	if word.endswith(("\u092f\u0942", "\u092f\u0940")):
		return f"stri:nadI;ending=yU/y;word={word}"
	return f"not-nadI:{word}"


def apply_1_4_4(word, pos=""):
	"""P.1.4.4 neyaNuvaNsTAnAvastrI |
	n and Ng/u/Na are NOT feminine stems."""
	not_stri_stems = ("n", "\u1e45", "u", "\u1e4a")
	if word.startswith(not_stri_stems):
		return f"not-stri:stem={word}"
	return f"maybe-stri:{word}"


def apply_1_4_5(word, pos=""):
	"""P.1.4.5 vAmi - optionally i before ami (acc dual/plural)."""
	if pos in ("acc_dual", "acc_plural"):
		return f"opt-i:before=ami;word={word}"
	return f"no-opt-i:{word}"


def apply_1_4_6(word, pos=""):
	"""P.1.4.6 Niti hrasvaSca - also short vowel before Nit suffixes."""
	if pos.endswith("Nit") and word:
		return f"hrasva:Nit:before={word[-1]};ok"
	return f"no-Nit:{word}"


def apply_1_4_7(word, pos=""):
	"""P.1.4.7 Sezo GyasaKi - remaining is GyasaKi (genitive marker)."""
	if not word:
		return "empty:no-case"
	if word.endswith(("\u0938\u094d\u092f", "\u0918\u094d\u092f", "\u0938\u0916\u093f")):
		return f"case=genitive:GyasaKi;word={word}"
	return f"not-genitive:{word}"


def apply_1_4_8(word, pos=""):
	"""P.1.4.8 patiH samAsa eva - pati is only in compounds."""
	if word == "\u092a\u0924\u093f":
		if pos == "samAsa":
			return f"pati:in-samAsa;word={word}"
		return f"pati:not-in-samAsa:{word}"
	return f"not-pati:{word}"


def apply_1_4_9(word, pos=""):
	"""P.1.4.9 zazWIyuktaSCandasi vA - optionally in 6th case in Vedic."""
	if pos == "zazTi-Candasa":
		return f"opt-6th:Vedic;word={word}"
	return f"no-opt:{word}"

# =====================================================================
# SECTION C P.1.4.10-12 laghu-guru (syllable weight)
# =====================================================================


def apply_1_4_10(word, pos=""):
	"""P.1.4.10 hrasvaM laGu - short vowel = laghu (light)."""
	hrasva = set("\u0906\u0907\u0908\u0916\u0917\u0918\u091e\u091f\u0920\u0924\u0925\u0926\u092a\u092b\u0936\u0937\u0939")
	if word[-1] in hrasva:
		return f"weight=laghu;last={word[-1]}"
	return f"not-laghu:{word}"


def apply_1_4_11(word, pos=""):
	"""P.1.4.11 saMyoge guru - consonant cluster = guru (heavy)."""
	consonants = "\u0915\u0916\u0917\u0918\u0919\u091a\u091b\u091c\u091d\u091e"
	for i in range(len(word) - 1):
		if word[i] in consonants and word[i+1] in consonants:
			return f"weight=guru:cluster={word[i:i+2]};word={word}"
	return f"no-cluster:{word}"


def apply_1_4_12(word, pos=""):
	"""P.1.4.12 dIrGaM ca - long vowel also guru."""
	dirgha = set("\u0906\u0908\u0910\u0914\u0948\u094c\u0950\u0951\u0952")
	if word[-1] in dirgha:
		return f"weight=guru:long-vowel={word[-1]}"
	return f"not-dirgha-guru:{word}"

# =====================================================================
# SECTION D P.1.4.13-14 anga / pada definitions
# =====================================================================


def apply_1_4_13(word, pos=""):
	"""P.1.4.13 yasmAt pratyayavidhista-dAdi pratyaye aNgam |
	Whatever the pratyaya vidhi targets, that is the anga."""
	pratyayas = ("\u0930\u094d\u0924\u094d\u092f\u092f", "\u090f\u0924\u093f", "\u0938\u0941\u092a\u094d")
	for s in pratyayas:
		if word.endswith(s):
			return f"anga:pratyaya-target={s};word={word}"
	return f"not-anga:{word}"


def apply_1_4_14(word, pos=""):
	"""P.1.4.14 suptiGantaM padam - word ending in sup or tiG is a pada."""
	sup_terms = ("\u0938\u0941\u092a\u094d",)
	tiG_terms = ("\u0924\u093f\u091f\u094d",)
	for s in sup_terms:
		if word.endswith(s):
			return f"pada:sup-ending;word={word}"
	for s in tiG_terms:
		if word.endswith(s):
			return f"pada:tiG-ending;word={word}"
	return f"not-pada:{word}"

# =====================================================================
# SECTION E P.1.4.15-20 misc
# =====================================================================


def apply_1_4_15(word, pos=""):
	"""P.1.4.15 naH kye - naH does not go before kye (acc pl)."""
	if word.endswith("\u0915\u094d\u092f\u0947"):
		return f"no-naH-prefix:kye;word={word}"
	return f"ok:{word}"


def apply_1_4_16(word, pos=""):
	"""P.1.4.16 siti ca - also before sit (siT)."""
	if pos == "siT":
		return f"apply-before-sit;word={word}"
	return f"no-apply:{word}"


def apply_1_4_17(word, pos=""):
	"""P.1.4.17 svAdizvasarvanAmasTAne - svAdi before asarvanamasthana."""
	svadi = ("\u0938\u094d\u0935\u093e\u0926\u093f",)
	if word.startswith(svadi):
		return f"svAdi:start;word={word}"
	return f"not-svAdi:{word}"


def apply_1_4_18(word, pos=""):
	"""P.1.4.18 yaSi BhawaH vacanasya - yac in the sense of sRJ."""
	if pos == "sRJ":
		return f"yac:sRJ-artha;word={word}"
	return f"not-sRJ:{word}"


def apply_1_4_19(word, pos=""):
	"""P.1.4.19 tasO matvarTe - tas in motion/opinion sense."""
	if pos in ("motion", "opinion"):
		return f"tas:mat-artha={pos};word={word}"
	return f"not-mat-artha:{word}"


def apply_1_4_20(word, pos=""):
	"""P.1.4.20 ayasmayAdIni cCandasi - ayasmaya etc. in Vedic."""
	vedic = ("\u090f\u092f\u0938\u094d\u092e\u092f", "\u0935\u0947\u0926\u093f\u0915\u093e")
	if word in vedic:
		return f"vedic:ayasmaya-adi;word={word}"
	return f"not-vedic-adi:{word}"

# =====================================================================
# SECTION F P.1.4.21-22 sankhya (number)
# =====================================================================


def apply_1_4_21(word, pos=""):
	"""P.1.4.21 bahuzu bahuvacanam - plural with bahu (many)."""
	if "\u092c\u0939\u0941" in word or pos == "bahuvacana":
		return f"number=bahuvacana;word={word}"
	return f"not-bahuvacana:{word}"


def apply_1_4_22(word, pos=""):
	"""P.1.4.22 dvya ekayor dvivacana ekavacane - dual of 2/1."""
	if pos in ("dvivacana", "ekavacana"):
		return f"number={pos}:dva-eka;word={word}"
	return f"not-dva-eka:{word}"

# =====================================================================
# SECTION G P.1.4.23 karaka definition
# =====================================================================


def apply_1_4_23(word, pos=""):
	"""P.1.4.23 kArake - karaka (case relations) definition."""
	karakas = {"kartA", "karman", "karaNam", "sampradAnam", "apAdAnam", "adhikaraNam"}
	if word in karakas or pos == "kAraka":
		return f"karaka:defined;role={word or pos}"
	return f"not-karaka:{word}"

# =====================================================================
# SECTION H P.1.4.24-28 apadana (source / fixed point)
# =====================================================================


def apply_1_4_24(word, pos=""):
	"""P.1.4.24 DruvamapAye apAdAnam.
	apAdAnam = fixed point from which something moves away."""
	apadana_words = ("\u0917\u0941\u0930\u0941", "\u092d\u0941\u0935\u0928", "\u092e\u0942\u0932")
	if word in apadana_words or pos == "dhruva":
		return f"kAraka=apAdAnam:dhruva;word={word}"
	return f"not-apadana:{word}"


def apply_1_4_25(word, pos=""):
	"""P.1.4.25 BItrArTAnAM BayahetuH - source of fear = apAdāna."""
	bhayahetu = ("\u0915\u0930\u094d\u0923", "\u092d\u094d\u0930\u092f\u0902", "\u0936\u093f\u0915\u093e\u0930\u093e")
	if word in bhayahetu or pos == "bhayahetu":
		return f"kAraka=apAdAnam:BI-bhayahetu;word={word}"
	return f"not-apadana-bhayahetu:{word}"


def apply_1_4_26(word, pos=""):
	"""P.1.4.26 parAjerasoQaH - conquered = apādāna."""
	if "\u092a\u0930\u093e\u091c\u093f\u0924" in word or pos == "parAjita":
		return f"kAraka=apAdAnam:parAjita;word={word}"
	return f"not-parAjita:{word}"


def apply_1_4_27(word, pos=""):
	"""P.1.4.27 vAraNArTAnAmIpsitaH - protection, desired object."""
	varana = ("\u0905\u0917\u094d\u0928\u093f", "\u0936\u0938\u094d\u0924\u094d\u0930", "\u0930\u0915\u094d\u0937")
	if word in varana or pos == "vAraNa":
		return f"kAraka=apAdAnam:vAraNa;word={word}"
	return f"not-apadana-vAraNa:{word}"


def apply_1_4_28(word, pos=""):
	"""P.1.4.28 antardDO yenAdarSanamicCati - concealment context."""
	if "\u0905\u0928\u094d\u0924\u0930" in word or pos == "antarddhi":
		return f"kAraka=apAdAnam:antarddhi;word={word}"
	return f"not-antarddhi-apadana:{word}"

# =====================================================================
# SECTION I P.1.4.29-31 kartA (agent)
# =====================================================================


def apply_1_4_29(word, pos=""):
	"""P.1.4.29 AKyAtopayoge - when verb is used with the noun."""
	if pos == "akhyAta" or "kriyA" in pos:
		return f"kAraka=kartA:akhyAtopayoga;word={word}"
	return f"not-akhyAta-kartA:{word}"


def apply_1_4_30(word, pos=""):
	"""P.1.4.30 janikartuH prakftiH - prakrti of the generator."""
	if pos == "janikartA":
		return f"kAraka=kartA:janikartA-prakfti;word={word}"
	return f"not-janikartA:{word}"


def apply_1_4_31(word, pos=""):
	"""P.1.4.31 BuvaH praBavaH - bhU (be) as source = apādāna."""
	bhava = ("\u091c\u0928\u094d\u092e", "\u0909\u0924\u094d\u092a\u0924\u094d\u0924\u093f", "\u092e\u0942\u0932")
	if word in bhava or pos == "bhU-prabhava":
		return f"kAraka=apAdAnam:bhU-prabhava;word={word}"
	return f"not-bhU-apadana:{word}"

# =====================================================================
# SECTION J P.1.4.32-36 sampradanam (recipient)
# =====================================================================


def apply_1_4_32(word, pos=""):
	"""P.1.4.32 karmaRA yamaBiprEti sa sampradAnam.
	sampradAnam = recipient of what is intended."""
	recipients = ("\u0926\u093e\u0924\u093e", "\u092c\u094d\u0930\u093e\u0924\u093e", "\u0906\u0924\u094d\u092e\u0947")
	if word in recipients or pos == "sampradAnam":
		return f"kAraka=sampradAnam:abhiprEti;word={word}"
	return f"not-sampradAnam:{word}"


def apply_1_4_33(word, pos=""):
	"""P.1.4.33 rucyarTAnAM prIyamARaH - for liking, the pleased one."""
	if pos == "ruci" or "\u092a\u094d\u0930\u0940\u0924\u093f" in word:
		return f"kAraka=sampradAnam:ruci;word={word}"
	return f"not-ruci-sampradAnam:{word}"


def apply_1_4_34(word, pos=""):
	"""P.1.4.34 SlAGahnuNsTASapAM jYIpsyamAnaH - for praise/blame."""
	if pos in ("SlAGhA", "hnuG", "sthASap"):
		return f"kAraka=sampradAnam:{pos};word={word}"
	return f"not-SlAGhA-sampradAnam:{word}"


def apply_1_4_35(word, pos=""):
	"""P.1.4.35 DAreruttamarRaH - of lending, upper creditor."""
	if pos == "dhAra" or "\u0909\u0924\u094d\u0924\u092e\u0930\u094d\u0923" in word:
		return f"kAraka=sampradAnam:dhAra;uttamarRa;word={word}"
	return f"not-dhAra-sampradAnam:{word}"


def apply_1_4_36(word, pos=""):
	"""P.1.4.36 spfherIpsitaH - of spRh (desire), the desired one."""
	if pos == "spRhA" or "\u0906\u0924\u094d\u092e\u0938\u094d\u092f" in word:
		return f"kAraka=sampradAnam:spRhA;ipsita;word={word}"
	return f"not-spRhA-sampradAnam:{word}"


def apply_1_4_37(word, pos=""):
	"""P.1.4.37 kruDadruherzyAsUyArTAnAM yaM prati kopaH.
	anger/hatred/jealousy/envy toward someone."""
	if pos in ("krodha", "droha", "IrzyA", "asUyA"):
		return f"kAraka=sampradAnam:{pos};word={word}"
	return f"not-emotion-sampradAnam:{word}"


def apply_1_4_38(word, pos=""):
	"""P.1.4.38 kruDadruhorupasfzwayoH karma - karma when qualified."""
	if pos in ("krodha-upasfzwa", "droha-upasfzwa"):
		return f"kAraka=karman:krodha-droha-upasfzwa;word={word}"
	return f"not-upasfzwa-karman:{word}"


def apply_1_4_39(word, pos=""):
	"""P.1.4.39 rADIkzyoryasya vipraSnaH - enquiry target."""
	if pos in ("rAdhi", "IkzyA"):
		return f"kAraka=sampradAnam:vipraSna;word={word}"
	return f"not-vipraSna-sampradAnam:{word}"

# =====================================================================
# SECTION K P.1.4.40-42 kartA from hearing
# =====================================================================


def apply_1_4_40(word, pos=""):
	"""P.1.4.40 pratyANByAM SruvaH pUrvasya kartA - hearer as agent."""
	if pos in ("pratyaG", "AG") or word.startswith(("\u092a\u094d\u0930", "\u0906")):
		return f"kAraka=kartA:SruvaH-hearer;word={word}"
	return f"not-SruvaH-kartA:{word}"


def apply_1_4_41(word, pos=""):
	"""P.1.4.41 anupratigfRaSca - anu/prati/gR as kartā."""
	if word.startswith(("\u0905\u0928\u0941", "\u092a\u094d\u0930\u0924\u093f", "\u0917\u0943")):
		return f"kAraka=kartA:anupratigR;word={word}"
	return f"not-anupratigR-kartA:{word}"


def apply_1_4_42(word, pos=""):
	"""P.1.4.42 sADakatamaM karaNam - most efficient = karaNam."""
	if pos == "sADakatama":
		return f"kAraka=karaNam:sADakatama;word={word}"
	return f"not-sADakatama-karaNam:{word}"

# =====================================================================
# SECTION L P.1.4.43-48 karman (object)
# =====================================================================


def apply_1_4_43(word, pos=""):
	"""P.1.4.43 divaH karma ca - div (dig) also = karman."""
	if word in ("\u0926\u093f\u0935", "\u0926\u093f\u0935\u094d") or pos == "div":
		return f"kAraka=karman:div;word={word}"
	return f"not-div-karman:{word}"


def apply_1_4_44(word, pos=""):
	"""P.1.4.44 parikrayaRe sampradAnamanyatarasyAm - optional."""
	if pos in ("parikrayaNa", "vikrayaNa"):
		return f"kAraka=sampradAnam:optional;word={word}"
	return f"not-optional-sampradAnam:{word}"


def apply_1_4_45(word, pos=""):
	"""P.1.4.45 ADaroaDikaraRam - adhara = adhikaraNam."""
	if word in ("\u0905\u0927\u0930", "\u092d\u0942\u092e\u093f", "\u091b\u093e\u092f\u093e") or pos == "adhara":
		return f"kAraka=adhikaraNam:adhara;word={word}"
	return f"not-adhar-adhikaraNam:{word}"


def apply_1_4_46(word, pos=""):
	"""P.1.4.46 aDiSINsTAsAM karma - adhi+SIG/sthA/AsA = karman."""
	if pos.startswith("aDi") and pos in ("aDiSIG", "aDisthA", "aDiAsA"):
		return f"kAraka=karman:aDi-SIG-sthA-AsA;word={word}"
	return f"not-aDi-karman:{word}"


def apply_1_4_47(word, pos=""):
	"""P.1.4.47 aBiniviSaSca - abhiniviS also = karman."""
	if pos == "abhiniviS":
		return f"kAraka=karman:abhiniviS;word={word}"
	return f"not-abhiniviS-karman:{word}"


def apply_1_4_48(word, pos=""):
	"""P.1.4.48 upAnvaDyANvasaH - upa/anva/dhyAG/vas = karman."""
	if pos in ("upa", "anva", "dhyAG", "vas"):
		return f"kAraka=karman:upa-anva-dhyAG-vas;word={word}"
	return f"not-upAnva-karman:{word}"


def apply_1_4_49(word, pos=""):
	"""P.1.4.49 karturIpsitatamaM karma - most desired = karman."""
	if pos == "karturIpsita":
		return f"kAraka=karman:ipsitatama;word={word}"
	return f"not-ipsitatama-karman:{word}"


def apply_1_4_50(word, pos=""):
	"""P.1.4.50 taTAyuktaM cAnIpsitam - similarly connected but not desired."""
	if pos == "taTAyukta-anIpsita":
		return f"not-karman:anIpsita;taTAyukta;word={word}"
	return f"maybe-karman:{word}"


def apply_1_4_51(word, pos=""):
	"""P.1.4.51 akaTitaM ca - unexpressed = also a karaka."""
	if pos == "akathitam":
		return f"karaka:unexpressed;word={word}"
	return f"expressed-or-other:{word}"

# =====================================================================
# SECTION P.1.4.52-55 kartā (agent, continued)
# =====================================================================


def apply_1_4_52(word, pos=""):
	"""P.1.4.52 gatibudDipratyavasAnArTaSabdakarmAkarmakARAmaNi kartā sa RO.
	Agent marked by Ni in certain roots with specific meanings."""
	if pos in ("Ni-kartA", "RO-kartA"):
		return f"kAraka=kartA:Ni-pratyaya;word={word}"
	return f"not-Ni-kartA:{word}"


def apply_1_4_53(word, pos=""):
	"""P.1.4.53 hfkroranyatarasyAm - optionally for hR and kR."""
	if word.startswith(("\u0939\u0943", "\u0915\u0943")) or pos in ("hR", "kR"):
		return f"opt-rule:hR-kR;word={word}"
	return f"not-hR-kR:{word}"


def apply_1_4_54(word, pos=""):
	"""P.1.4.54 svatantraH kartA - kartā = independent agent."""
	if pos == "kartA":
		return f"kAraka=kartA:svatantra;word={word}"
	return f"not-kartA:{word}"


def apply_1_4_55(word, pos=""):
	"""P.1.4.55 tatprayojako hetuSca - instigator is also hetu."""
	if pos == "hetu":
		return f"kAraka=hetu:tatprayojaka;word={word}"
	return f"not-hetu:{word}"

# =====================================================================
# SECTION M P.1.4.56-108 upasarga / avyaya / purusa / vibhakti
# =====================================================================


def apply_1_4_56(word, pos=""):
	"""P.1.4.56 prAgrISvarAnnipAtAH - nipAta before ISvara."""
	if pos.startswith("prAg") or word.startswith("\u092a\u094d\u0930\u093e\u0917"):
		return f"nipAta:prAg:ISvara;word={word}"
	return f"not-prAg:{word}"


def apply_1_4_57(word, pos=""):
	"""P.1.4.57 cAdayosattve - ca etc. in non-entity context."""
	cadi = ("\u091a", "\u091a\u093e", "\u0935\u093e", "\u0924\u0941", "\u0905\u092a\u093f")
	if word in cadi or pos == "cAdi":
		return f"avyaya:cAdi:sattve;word={word}"
	return f"not-cAdi:{word}"


def apply_1_4_58(word, pos=""):
	"""P.1.4.58 prAdayaH - pre etc. (prepositions/prefixes)."""
	pre = ("\u092a\u094d\u0930", "\u092a\u0930", "\u0938\u092e", "\u0935\u093f")
	if word in pre or word.startswith(pre):
		return f"upasarga:prAdi;word={word}"
	return f"not-prAdi:{word}"


def apply_1_4_59(word, pos=""):
	"""P.1.4.59 upasargAH kriyAyoge - upasarga when connected to action."""
	if pos == "upasarga" or word.startswith(("\u0909\u092a", "\u092a\u094d\u0930", "\u0935\u093f")):
		return f"upasarga:kriyAyoga;word={word}"
	return f"not-upasarga:{word}"


def apply_1_4_60(word, pos=""):
	"""P.1.4.60 gatiSca - gati (movement) also = upasarga."""
	gati = ("\u0905\u092c\u094d\u092f\u093e\u0938", "\u092a\u0930\u093e", "\u0906\u0926\u093f", "\u0939\u093f")
	if word in gati or pos == "gati":
		return f"upasarga:gati;word={word}"
	return f"not-gati-upasarga:{word}"


def apply_1_4_61(word, pos=""):
	"""P.1.4.61 UryAdicviqAcaSca - UryAdi and cviqAca also."""
	if word.startswith(("\u0942\u0930\u094d\u092f", "\u091a\u094d\u0935\u093f")) or pos == "UryAdi":
		return f"upasarga:UryAdi-cviqAca;word={word}"
	return f"not-UryAdi:{word}"


def apply_1_4_62(word, pos=""):
	"""P.1.4.62 anukaraRaM cAnitiparam - imitation (not imperative)."""
	if word == "\u0905\u0928\u0941\u0915\u0930" or pos == "anukaraRa":
		return f"avyaya:anukaraRa:not-imperative;word={word}"
	return f"not-anukaraNa:{word}"


def apply_1_4_63(word, pos=""):
	"""P.1.4.63 AdarAnAdarayoH sadasatI - sad/asat = abhinivesha."""
	if word in ("\u0938\u0926\u094d", "\u0905\u0938\u0926\u094d") or pos == "Adara":
		return f"abhinivesha:sadasatI;word={word}"
	return f"not-sadasatI:{word}"


def apply_1_4_64(word, pos=""):
	"""P.1.4.64 BUzaNealam - alam in embellishment = upasarga."""
	if word == "\u0905\u0932\u092e\u094d":
		if pos in ("BUzaRa", "alam"):
			return f"upasarga:BUzaRa:alam;word={word}"
		return f"alam:not-emphasis:{word}"
	return f"not-alam:{word}"


def apply_1_4_65(word, pos=""):
	"""P.1.4.65 antaraparigrahe - antara in acceptance."""
	if word == "\u0905\u0928\u094d\u0924\u0930" or pos == "antaraparigraha":
		return f"upasarga:antara:parigraha;word={word}"
	return f"not-antara:{word}"


def apply_1_4_66(word, pos=""):
	"""P.1.4.66 kaRemanasI SradDApratIGAte - kaRa and manas."""
	if word in ("\u0915\u0923", "\u092e\u0928\u0938\u0940"):
		return f"artha:SradDA:apratighAta;word={word}"
	return f"not-kaRa-manas:{word}"


def apply_1_4_67(word, pos=""):
	"""P.1.4.67 purovyayam - purA (before) = avyaya."""
	if word in ("\u092a\u0941\u0930\u093e", "\u092a\u0942\u0930\u094d"):
		return f"avyaya:purA;word={word}"
	return f"not-purA:{word}"


def apply_1_4_68(word, pos=""):
	"""P.1.4.68 astaM ca - astam (down) also = avyaya."""
	if word in ("\u0905\u0938\u094d\u0924", "\u0905\u0938\u094d\u0924\u0902", "\u0905\u0938\u094d\u0924\u093e"):
		return f"avyaya:astaM;word={word}"
	return f"not-astaM:{word}"


def apply_1_4_69(word, pos=""):
	"""P.1.4.69 acCa gatyarTavadezu - accha + gati-artha."""
	if word.startswith("\u0905\u091a"):
		return f"upasarga:acCa:gati;word={word}"
	return f"not-acCa:{word}"


def apply_1_4_70(word, pos=""):
	"""P.1.4.70 adonupadeSe - adas in non-teaching context."""
	if word.startswith("\u0905\u0926"):
		return f"avyaya:adas:anupadeSe;word={word}"
	return f"not-adas:{word}"


def apply_1_4_71(word, pos=""):
	"""P.1.4.71 tiroantardDO - tiras (concealed) in antarddhi."""
	if word in ("\u0924\u093f\u0930\u093e\u0938\u094d", "\u0924\u093f\u0930\u094b") or pos == "antarddhi":
		return f"avyaya:tiras:antarddhi;word={word}"
	return f"not-tiras:{word}"


def apply_1_4_72(word, pos=""):
	"""P.1.4.72 viBAzA kfYi - optionally in kRJ."""
	if word.startswith("\u0915\u0943") or pos == "kRJ":
		return f"optional:viBAzA:kRJ;word={word}"
	return f"no-optional:{word}"


def apply_1_4_73(word, pos=""):
	"""P.1.4.73 upAjenvAje - upAja and anvAja."""
	if word in ("\u0909\u092a\u093e\u091c", "\u0905\u0928\u094d\u0935\u093e\u091c") or pos == "upAja":
		return f"upasarga:upAja-anvAja;word={word}"
	return f"not-upAja:{word}"


def apply_1_4_74(word, pos=""):
	"""P.1.4.74 sAkzAtpraBftIni ca - sAkzAt and following."""
	sAkzAdi = ("\u0938\u093e\u0915\u094d\u0937\u093e\u0924\u094d", "\u092a\u0941\u0930\u0930\u094d", "\u0939\u093f")
	if word in sAkzAdi or word.startswith("\u0938\u093e\u0915\u094d"):
		return f"upasarga:sAkzAt-praBfti;word={word}"
	return f"not-sAkzAt:{word}"


def apply_1_4_75(word, pos=""):
	"""P.1.4.75 anatyADAna urasimanasI - uraH/manas context."""
	if word in ("\u0909\u0930\u0938\u093f", "\u092e\u0928\u0938\u0940"):
		return f"artha:anatyADAna:uraH-manas;word={word}"
	return f"not-uraH-manas:{word}"


def apply_1_4_76(word, pos=""):
	"""P.1.4.76 maDye pade nivacane ca - middle of pada, enumeration."""
	if pos in ("pada-maDya", "nivacana"):
		return f"artha:maDya:nivacana;word={word}"
	return f"not-maDya-nivacana:{word}"


def apply_1_4_77(word, pos=""):
	"""P.1.4.77 nityaM haste pANAvupayamane - always in hand."""
	if word in ("\u0939\u0938\u094d\u0924\u0947", "\u092a\u093e\u0923") or pos == "upayamana":
		return f"artha:nityaM:hasta:pANi;word={word}"
	return f"not-hasta:{word}"


def apply_1_4_78(word, pos=""):
	"""P.1.4.78 prADvaM banDane - prAGhu in binding."""
	if word in ("\u092a\u094d\u0930\u093e\u0927\u094d\u0935", "\u092c\u0928\u094d\u0927\u0928") or pos == "banDana":
		return f"artha:prAGhu:banDana;word={word}"
	return f"not-prAGhu:{word}"


def apply_1_4_79(word, pos=""):
	"""P.1.4.79 jIvikopanizadAvOpamye - jIvikA and upaniSad."""
	if word in ("\u091c\u0940\u0935\u093f\u0915\u093e", "\u0909\u092a\u0928\u093f\u0937\u0926\u094d") or pos == "Opamya":
		return f"artha:jIvikA-upaniSad:Opamya;word={word}"
	return f"not-Opamya:{word}"


def apply_1_4_80(word, pos=""):
	"""P.1.4.80 te prAgDAtoH - te before the dhAtu."""
	if word in ("\u0924\u0947", "\u0924\u0935\u0924\u094d") or pos.startswith("prAg-"):
		return f"prAg:te:DAtoH;word={word}"
	return f"not-te-prag:{word}"


def apply_1_4_81(word, pos=""):
	"""P.1.4.81 Candasi parepi - also in Vedic when following."""
	if pos in ("Candasa", "vedic-pare"):
		return f"vedic:Candasa:pare;word={word}"
	return f"not-vedic-pare:{word}"


def apply_1_4_82(word, pos=""):
	"""P.1.4.82 vyavahitASca - also when separated."""
	if pos == "vyavahita":
		return f"avyaya:vyavahita;word={word}"
	return f"not-vyavahita:{word}"


def apply_1_4_83(word, pos=""):
	"""P.1.4.83 karmapravacanIyAH - karmapravacanIya definition."""
	karma = ("\u0905\u0924\u093f", "\u0905\u0915\u094d", "\u092a\u0930\u093f", "\u0935\u0943\u0924\u094d")
	if word in karma or pos == "karmapravacanIya":
		return f"upasarga:karmapravacanIya;word={word}"
	return f"not-karmapravacanIya:{word}"


def apply_1_4_84(word, pos=""):
	"""P.1.4.84 anurlakzaRe - anu in the sense of lakshaNa."""
	if word == "\u0905\u0928\u0941" or pos == "anurlakshaRa":
		return f"karmapravacanIya:anu:lakshaRa;word={word}"
	return f"not-anu-lakshaRa:{word}"


def apply_1_4_85(word, pos=""):
	"""P.1.4.85 tftIyArTe - in the third case sense."""
	if pos == "tftIyArtha":
		return f"artha:tftIyArtha:3rd;word={word}"
	return f"not-3rd-case:{word}"


def apply_1_4_86(word, pos=""):
	"""P.1.4.86 hIne - in deficiency."""
	if pos == "hIna" or "\u0939\u0940\u0928\u0947" in word:
		return f"artha:hIna:hIne;word={word}"
	return f"not-hIna:{word}"


def apply_1_4_87(word, pos=""):
	"""P.1.4.87 upoaDike ca - upa in excess."""
	if word.startswith("\u0909\u092a") or pos == "upa-adhika":
		return f"artha:upa:adhike;word={word}"
	return f"not-upa-adhika:{word}"


def apply_1_4_88(word, pos=""):
	"""P.1.4.88 apaparI varjane - apa and parI in abandonment."""
	if word.startswith(("\u0905\u092a", "\u092a\u0930\u0940")) or pos == "varjana":
		return f"karmapravacanIya:apa-parI:varjane;word={word}"
	return f"not-apa-parI:{word}"


def apply_1_4_89(word, pos=""):
	"""P.1.4.89 ANg maryAdAvacane - AG in the sense of limit."""
	if word.startswith("\u0906\u091f\u094d") or pos == "maryAdA":
		return f"karmapravacanIya:AN:maryAdA;word={word}"
	return f"not-AN-maryAdA:{word}"


def apply_1_4_90(word, pos=""):
	"""P.1.4.90 lakzaRetTamBUtAKyAnaBAgavIpsAsu pratiparyanavaH.
	pratipar in these senses."""
	if pos in ("lakshaRa", "itTamBUta", "AKyAna", "BAga", "vIpsA"):
		return f"karmapravacanIya:pratipar;artha={pos};word={word}"
	return f"not-pratipar-context:{word}"


def apply_1_4_91(word, pos=""):
	"""P.1.4.91 aBiraBAge - abhi in the sense of part."""
	if word.startswith("\u0905\u092d\u093f") or pos == "BAga":
		return f"karmapravacanIya:abhi:BAge;word={word}"
	return f"not-abhi-BAga:{word}"


def apply_1_4_92(word, pos=""):
	"""P.1.4.92 pratiH pratiniDipratidAnayoH - substitute/repayment."""
	if word == "\u092a\u094d\u0930\u0924\u093f\u0939\u094d" or pos in ("pratiniDi", "pratidAna"):
		return f"karmapravacanIya:prati:pratiniDi-pratidAna;word={word}"
	return f"not-prati-substitute:{word}"


def apply_1_4_93(word, pos=""):
	"""P.1.4.93 aDiparI anarTakO - adhi and parI meaningless."""
	if word in ("\u0905\u0927\u093f", "\u092a\u0930\u0940"):
		return f"upasarga:adhi-parI:anartha;word={word}"
	return f"not-adhi-parI:{word}"


def apply_1_4_94(word, pos=""):
	"""P.1.4.94 suH pUjAyAm - su in the sense of worship."""
	if word.startswith("\u0938\u0941") or pos == "pUjA":
		return f"upasarga:su:pUjA;word={word}"
	return f"not-su-pUjA:{word}"


def apply_1_4_95(word, pos=""):
	"""P.1.4.95 atiratikramaRe ca - ati in transgression."""
	if word.startswith("\u0905\u0924\u093f\u0930") or pos == "atikramaRa":
		return f"upasarga:ati:atikramaRa;word={word}"
	return f"not-ati-atikramaRa:{word}"


def apply_1_4_96(word, pos=""):
	"""P.1.4.96 apiH padArTasamBAvanAnvavasargagarhAsamuccayezu.
	api in these senses."""
	if word == "\u0905\u092a\u093f" or pos in ("samBAvanA", "anvavasarga", "garhA", "samuccaya"):
		return f"upasarga:api:multi-artha;word={word}"
	return f"not-api-multi:{word}"


def apply_1_4_97(word, pos=""):
	"""P.1.4.97 aDirISvare - adhi in lordship."""
	if word.startswith("\u0905\u0927\u093f") or pos == "ISvara":
		return f"upasarga:adhi:ISvare;word={word}"
	return f"not-adhi-ISvara:{word}"


def apply_1_4_98(word, pos=""):
	"""P.1.4.98 viBAzA kfYi - optionally in kRJ."""
	if word.startswith("\u0915\u0943") or pos == "kRJ":
		return f"optional:viBAzA:kRJ;word={word}"
	return f"no-optional:{word}"

# =====================================================================
# SECTION N P.1.4.99-102 puruSa (person)
# =====================================================================


def apply_1_4_99(word, pos=""):
	"""P.1.4.99 laH parasmEpadam - lArAH = parasmai padam."""
	if pos == "parasmaipada":
		return f"pada:parasmaipada:laH;word={word}"
	return f"not-parasmaipada:{word}"


def apply_1_4_100(word, pos=""):
	"""P.1.4.100 taNAnAvAtmanepadam - taG and AnAu = Atmane padam."""
	if word.startswith("\u0924\u091f\u094d") or pos == "Atmanepada":
		return f"pada:Atmanepada:taNAna;word={word}"
	return f"not-Atmanepada:{word}"


def apply_1_4_101(word, pos=""):
	"""P.1.4.101 tiNastrINi trINi praTamamaDyamottamAH.
	tiG in 3 groups: 1st, 2nd, 3rd person."""
	if pos in ("prathama", "maDyama", "uttama"):
		return f"pada:tiG:{pos}:person;word={word}"
	return f"no-person:{word}"


def apply_1_4_102(word, pos=""):
	"""P.1.4.102 tAnyekavacanadvivacanabahuvacanAnyekaSaH.
	each in singular/dual/plural."""
	if pos in ("ekavacana", "dvivacana", "bahuvacana"):
		return f"saMkhyA:{pos}:tiG;word={word}"
	return f"no-saMkhyA:{word}"

# =====================================================================
# SECTION O P.1.4.103-108 sup / vibhakti (case endings)
# =====================================================================


def apply_1_4_103(word, pos=""):
	"""P.1.4.103 supaH - sup (case endings) definition."""
	if pos == "sup" or word.endswith(("\u0938\u0941\u092a\u094d",)):
		return f"vibhakti:sup;word={word}"
	return f"not-sup:{word}"


def apply_1_4_104(word, pos=""):
	"""P.1.4.104 viBaktiSca - vibhakti also."""
	vibhakti_suffixes = (
		"\u0938\u0941\u092a\u094d", # sup
		"\u0906", "\u0907", "\u0908", "\u090f", "\u0940", "\u0941", "\u0942",
		"\u0948", "\u094b", "\u094c", "\u094d", "\u0902", "\u0901"
	)
	for s in vibhakti_suffixes:
		if word.endswith(s):
			return f"vibhakti:{s};word={word}"
	return f"no-vibhakti:{word}"


def apply_1_4_105(word, pos=""):
	"""P.1.4.105 yuzmadyupapade samAnADikaraRe sTAninyapi maDyamaH.
	with yusmad, madhyama even when sthanin is present."""
	if "\u092f\u0941\u0937\u094d\u092e\u0924\u094d" in word or pos.startswith("yusmad"):
		return f"pada:maDyama:yusmad;word={word}"
	return f"not-yusmad-maDyama:{word}"


def apply_1_4_106(word, pos=""):
	"""P.1.4.106 prahAse ca manyopapade manyateruttama ekavacca.
	in ridicule with manyA, uttama singular."""
	if word.startswith("\u092e\u0928\u094d\u092f") or pos == "manyA-prahAsa":
		return f"pada:uttama:ekavacana:manyA;prahAsa;word={word}"
	return f"not-uttama-manyA:{word}"


def apply_1_4_107(word, pos=""):
	"""P.1.4.107 asmadyuttamaH - with asmad = uttama."""
	if "\u0905\u0938\u094d\u092e\u0924\u094d" in word or pos.startswith("asmad"):
		return f"pada:uttama:asmad;word={word}"
	return f"not-asmad-uttama:{word}"


def apply_1_4_108(word, pos=""):
	"""P.1.4.108 Seze praTamaH - prathama (1st) in all other contexts."""
	return f"pada:prathama:default;word={word}"

# =====================================================================
# SECTION P P.1.4.109-110 sandhi / virama
# =====================================================================


def apply_1_4_109(word, pos=""):
	"""P.1.4.109 paraH sannikarzaH saMhitA - close proximity = sandhi."""
	if pos == "sannikarSa" or len(word) > 1:
		return f"sandhi:saMhitA:para-sannikarSa;word={word}"
	return f"no-sandhi:{word}"


def apply_1_4_110(word, pos=""):
	"""P.1.4.110 virAmoavasAnam - virama (pause) = end."""
	if pos == "virama" or word == "":
		return f"virama:avasAna:end;word={word}"
	return f"normal:{word}"

# EOF