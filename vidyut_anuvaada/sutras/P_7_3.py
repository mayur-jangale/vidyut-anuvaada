# -*- coding: utf-8 -*-
"""Shared apply_7_3_1..apply_7_3_120 functions for P.7.3.x."""

HAL = set("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")

A = chr(0x0905) # अ
I = chr(0x0907) # इ
U = chr(0x0909) # उ
RR = chr(0x090b) # ऋ
LL = chr(0x090c) # ऌ
E = chr(0x090f) # ए
O = chr(0x0913) # ओ
AI = chr(0x0910) # ऐ
AU = chr(0x0914) # औ
AA = chr(0x093e) # आ
I_ = chr(0x0908) # ई
U_ = chr(0x090a) # ऊ

VOWELS = {A, I, U, RR, LL, E, AI, O, AU, AA, I_, U_}
VRDDHI = {AI, AU}
GUNA = {E, O}
IK = {I, U, RR, LL}


def _analyse(word):
	if "+" not in word:
		return word, ""
	idx = word.index("+")
	return word[:idx], word[idx + 1:]


def apply_7_3_1(word, pos=""):
	"""devikaSimSapAdityavAddIrghasatraSreyasAmAt - long substitutes for
	specific compounds like devika, simsapa, aditya, vada, dirghasatra, sreyas
	before taddhita affixes; 'At' parses to A+t."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.1:input={word}"
	return f"7.3.1:special-at-lopa;{word}"


def apply_7_3_2(word, pos=""):
	"""kekayamitrayupralayanam yaaderiyaH - kekaya, mitra, yu, pralayana
	stems take iya taddhita instead of ya."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.2:input={word}"
	return f"7.3.2:kekayamitra-yadeH-iyaH;{word}"


def apply_7_3_3(word, pos=""):
	"""na yvabhyam padantabhyam purvau tu tabhyam aic - before final y/v
	at word boundary, the preceding member does NOT take aic (vrddhi) but
	the other member does."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.3:input={word}"
	return f"7.3.3:na-yvabhyam-aic;{word}"


def apply_7_3_4(word, pos=""):
	"""dvaradinam ca - dvara and related compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.4:input={word}"
	return f"7.3.4:dvaradinam;{word}"


def apply_7_3_5(word, pos=""):
	"""nyagrodhasya ca kevalasya - nyagrodha alone takes special taddhita."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.5:input={word}"
	return f"7.3.5:nyagrodha-kevalasya;{word}"


def apply_7_3_6(word, pos=""):
	"""na karmavyatihare - not in karmavyatihara (reciprocal compound)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.6:input={word}"
	return f"7.3.6:na-karmavyatihare;{word}"


def apply_7_3_7(word, pos=""):
	"""svagatadinam ca - svagata and similar compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.7:input={word}"
	return f"7.3.7:svagatadinam;{word}"


def apply_7_3_8(word, pos=""):
	"""SvAderiJi - svA-derived stems take in taddhita."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.8:input={word}"
	return f"7.3.8:SvAdeH-in;{word}"


def apply_7_3_9(word, pos=""):
	"""padAntasyAnyatarasyam - optional for padanta (word-final)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.9:input={word}"
	return f"7.3.9:padAnta-anyatarasyam;{word}"


def apply_7_3_10(word, pos=""):
	"""uttarapadasya - of the uttara pada (second member)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.10:input={word}"
	return f"7.3.10:uttarapadasya;{word}"


def apply_7_3_11(word, pos=""):
	"""avayavAdftoH - from avayava and fta stems."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.11:input={word}"
	return f"7.3.11:avayavAdftoH;{word}"


def apply_7_3_12(word, pos=""):
	"""susarvArDAjjanapadasya - from su, sarva, arDa before janapada."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.12:input={word}"
	return f"7.3.12:susarvArDAjjanapadasya;{word}"


def apply_7_3_13(word, pos=""):
	"""diSo'madrARAm - from dis (direction) but not madra names."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.13:input={word}"
	return f"7.3.13:diSo'madrARAm;{word}"


def apply_7_3_14(word, pos=""):
	"""prAcAM grAmanagarANAm - eastern grama-nagara compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.14:input={word}"
	return f"7.3.14:prAcAM-grAmanagarARAm;{word}"


def apply_7_3_15(word, pos=""):
	"""saMKyAyAH saMvatsarasaMKyasya ca - numeral compounds with year."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.15:input={word}"
	return f"7.3.15:saMKyAyAH-saMvatsarasaMKyasya;{word}"


def apply_7_3_16(word, pos=""):
	"""varzasyABavizyati - varsa when meaning future."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.16:input={word}"
	return f"7.3.16:varzasyABavizyati;{word}"


def apply_7_3_17(word, pos=""):
	"""parimARAntasyAsaMjYASARayoH - at end of measure terms, not proper names."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.17:input={word}"
	return f"7.3.17:parimARAntasyAsaMjYASARayoH;{word}"


def apply_7_3_18(word, pos=""):
	"""je prozWapadAnAm - je taddhita for prosThapada names."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.18:input={word}"
	return f"7.3.18:je-prozWapadAnAm;{word}"


def apply_7_3_19(word, pos=""):
	"""hfdBagasinDvante pUrvapadasya ca - hfd, Bag, sinDvanta compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.19:input={word}"
	return f"7.3.19:hfdBagasinDvante-pUrvapadasya;{word}"


def apply_7_3_20(word, pos=""):
	"""anuSatikAdInAM ca - anusatika and related."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.20:input={word}"
	return f"7.3.20:anuSatikAdInAM;{word}"


def apply_7_3_21(word, pos=""):
	"""devatAdvandve ca - in deity dvandva compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.21:input={word}"
	return f"7.3.21:devatAdvandve;{word}"


def apply_7_3_22(word, pos=""):
	"""nendrasya parasya - not indra's second member."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.22:input={word}"
	return f"7.3.22:nendrasya-parasya;{word}"


def apply_7_3_23(word, pos=""):
	"""dIrGAcca varuRasya - dirgha and varuna."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.23:input={word}"
	return f"7.3.23:dIrGAcca-varuRasya;{word}"


def apply_7_3_24(word, pos=""):
	"""prAcAM nagarAnte - eastern city-end compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.24:input={word}"
	return f"7.3.24:prAcAM-nagarAnte;{word}"


def apply_7_3_25(word, pos=""):
	"""jaNgalaDenuvalajAntasya viBAzitamuttaram - optional for jangala etc."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.25:input={word}"
	return f"7.3.25:jaNgalaDenuvalaja-viBAzA;{word}"


def apply_7_3_26(word, pos=""):
	"""arDAt parimARasya pUrvasya tu vA - from arDa measure, optionally."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.26:input={word}"
	return f"7.3.26:arDAt-parimARasya-tu-vA;{word}"


def apply_7_3_27(word, pos=""):
	"""nAtaH parasya - not after this."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.27:input={word}"
	return f"7.3.27:nAtaH-parasya;{word}"


def apply_7_3_28(word, pos=""):
	"""pravAhaRasya Qe - pravahana takes Qe."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.28:input={word}"
	return f"7.3.28:pravAhaRasya-Qe;{word}"


def apply_7_3_29(word, pos=""):
	"""tatpratyayasya ca - that pratyaya also."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.29:input={word}"
	return f"7.3.29:tatpratyayasya;{word}"


def apply_7_3_30(word, pos=""):
	"""naYaH SucISvarakzetrajYakuSalanipuRAnAm - naq prefix exceptions."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.30:input={word}"
	return f"7.3.30:naYaH-SucISvara-kzetrajYakuSala;{word}"


def apply_7_3_31(word, pos=""):
	"""yaTAtaTayaTApurayoH paryAyeRa - yatha, tatha, pur a paryaya."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.31:input={word}"
	return f"7.3.31:yaTAtaTayaTApurayoH;{word}"


def apply_7_3_32(word, pos=""):
	"""hanasto'ciRRaloH - from han roots, aci RR aloh."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.32:input={word}"
	return f"7.3.32:hanasto'ciRRaloH;{word}"


def apply_7_3_33(word, pos=""):
	"""Ato yuk ciRkftoH - ato gives yuk before ciR kft affixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.33:input={word}"
	return f"7.3.33:Ato-yuk-ciRkftoH;{word}"


def apply_7_3_34(word, pos=""):
	"""nodAttopadeSasya mAntasyAnAcameH - not udatta-upadesa, final ma."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.34:input={word}"
	return f"7.3.34:nodAttopadeSasya-mAntasya;{word}"


def apply_7_3_35(word, pos=""):
	"""janivaDyoSca - jani and vadha."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.35:input={word}"
	return f"7.3.35:janivaDyoSca;{word}"


def apply_7_3_36(word, pos=""):
	"""artihrIvlIrIknUyIkzmAyyAtAM puNRO - arti, hrI, etc. in puN affix."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.36:input={word}"
	return f"7.3.36:artihrIvlIrIknUyIkzmAyyAtAM-puNRO;{word}"


def apply_7_3_37(word, pos=""):
	"""SAcCAsAhvAvyAvepAM yuk - SAc, CAc, sAhv, avyAvep take yuk."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.37:input={word}"
	return f"7.3.37:SAcCAsAhvAvyAvepAM-yuk;{word}"


def apply_7_3_38(word, pos=""):
	"""vo viDUnane juk - va takes juk in meaning of viDUnana."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.38:input={word}"
	return f"7.3.38:vo-viDUnane-juk;{word}"


def apply_7_3_39(word, pos=""):
	"""lIlornuglukAvanyatarasyAM snehavipAtane - lila takes nugluka optionally."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.39:input={word}"
	return f"7.3.39:lIlor-nuglukA-anyatarasyAM;{word}"


def apply_7_3_40(word, pos=""):
	"""Biyo hetuBaye zuk - Baya takes zuk in meaning of hetu (cause)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.40:input={word}"
	return f"7.3.40:Biyo-hetuBaye-zuk;{word}"


def apply_7_3_41(word, pos=""):
	"""sPAyo vaH - sPAya takes va."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.41:input={word}"
	return f"7.3.41:sPAyo-vaH;{word}"


def apply_7_3_42(word, pos=""):
	"""SaderagatO taH - Sad in sense of going takes ta."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.42:input={word}"
	return f"7.3.42:SaderagatO-taH;{word}"


def apply_7_3_43(word, pos=""):
	"""ruhaH po'nyatarasyAm - ruh optionally takes po."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.43:input={word}"
	return f"7.3.43:ruhaH-po-anyatarasyAm;{word}"


def apply_7_3_44(word, pos=""):
	"""pratyayasTAt kAt pUrvasyAta idApyasupaH - before pratyaya-stha k
	affix, preceding 'at' takes id, and api before sup."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.44:input={word}"
	return f"7.3.44:pratyayasTAt-kAt;{word}"


def apply_7_3_45(word, pos=""):
	"""na yAsayoH - ya and As do not apply."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.45:input={word}"
	return f"7.3.45:na-yAsayoH;{word}"


def apply_7_3_46(word, pos=""):
	"""udIcAmAtaH sTAne yakapUrvAyAH - udIcAM instead of at gives
	yakapUrvA (ya + kapurva)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.46:input={word}"
	return f"7.3.46:udIcAmAtaH-sTAne-yakapUrvAyAH;{word}"


def apply_7_3_47(word, pos=""):
	"""BastrEA'jAjYAdvAsvAnaYpUrvARAmapi - bastr, aja, ajna, vAsu, anaq also."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.47:input={word}"
	return f"7.3.47:BastrEA'jAjYAdvAsvAnaY;{word}"


def apply_7_3_48(word, pos=""):
	"""aBAzitapuMskAcca - from aBAzitapuMska."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.48:input={word}"
	return f"7.3.48:aBAzitapuMskAcca;{word}"


def apply_7_3_49(word, pos=""):
	"""AdAcAryARAm - Adi and acarya names."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.49:input={word}"
	return f"7.3.49:AdAcAryARAm;{word}"


def apply_7_3_50(word, pos=""):
	"""WasyekaH - the TH (ठ) of a suffix is replaced by eka."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.50:input={word}"
	return f"7.3.50:Was-ekaH;{word}"


def apply_7_3_51(word, pos=""):
	"""isusuktAntAt kaH - from isu suktanta gives ka."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.51:input={word}"
	return f"7.3.51:isusuktAntAt-kaH;{word}"


def apply_7_3_52(word, pos=""):
	"""cajoH ku GiRRyatoH - ca and ja become ku/G before RR affixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.52:input={word}"
	return f"7.3.52:cajoH-ku-GiRRyatoH;{word}"


def apply_7_3_53(word, pos=""):
	"""nyaNkvAdInAM ca - nyaNku and related."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.53:input={word}"
	return f"7.3.53:nyaNkvAdInAM;{word}"


def apply_7_3_54(word, pos=""):
	"""ho hanterYRinnezu - han roots ho in YR inn affixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.54:input={word}"
	return f"7.3.54:ho-hanterYRinnezu;{word}"


def apply_7_3_55(word, pos=""):
	"""aByAsAcca - from abhyasa also."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.55:input={word}"
	return f"7.3.55:aByAsAcca;{word}"


def apply_7_3_56(word, pos=""):
	"""heracaNi - her in ac affix."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.56:input={word}"
	return f"7.3.56:heracaNi;{word}"


def apply_7_3_57(word, pos=""):
	"""sanliwoH jeH - san, lit, je affixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.57:input={word}"
	return f"7.3.57:sanliwoH-jeH;{word}"


def apply_7_3_58(word, pos=""):
	"""viBAzA ceH - optional for ci."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.58:input={word}"
	return f"7.3.58:viBAzA-ceH;{word}"


def apply_7_3_59(word, pos=""):
	"""na kvAdeH - not for kva."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.59:input={word}"
	return f"7.3.59:na-kvAdeH;{word}"


def apply_7_3_60(word, pos=""):
	"""ajivrajyoSca - aji, vraj."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.60:input={word}"
	return f"7.3.60:ajivrajyoSca;{word}"


def apply_7_3_61(word, pos=""):
	"""BujanyubjO pARyupatApayoH - bhuj, nyubj with pain."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.61:input={word}"
	return f"7.3.61:BujanyubjO-pARyupatApayoH;{word}"


def apply_7_3_62(word, pos=""):
	"""prayAjAnuyAjO yajYANge - prayaja, anuyaja in yajna-anga."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.62:input={word}"
	return f"7.3.62:prayAjAnuyAjO-yajYANge;{word}"


def apply_7_3_63(word, pos=""):
	"""vaYcergatO - vanc in sense of going."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.63:input={word}"
	return f"7.3.63:vaYcergatO;{word}"


def apply_7_3_64(word, pos=""):
	"""oka ucaH ke - uka takes ke."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.64:input={word}"
	return f"7.3.64:oka-ucaH-ke;{word}"


def apply_7_3_65(word, pos=""):
	"""Rya AvaSyake - nya in avasyaka."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.65:input={word}"
	return f"7.3.65:Rya-AvaSyake;{word}"


def apply_7_3_66(word, pos=""):
	"""yajayAcarucapravacarcaSca - yaja, yaca, ruca, p avac, arc."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.66:input={word}"
	return f"7.3.66:yajayAcarucapravacarcaSca;{word}"


def apply_7_3_67(word, pos=""):
	"""vaco'SabdasaMjYAyAm - vac as a word-denoting name."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.67:input={word}"
	return f"7.3.67:vaco-SabdasaMjYAyAm;{word}"


def apply_7_3_68(word, pos=""):
	"""prayojyaniyojyO SakyArTe - prayojya, niyojya in sense of capable."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.68:input={word}"
	return f"7.3.68:prayojyaniyojyO-SakyArTe;{word}"


def apply_7_3_69(word, pos=""):
	"""BojyaM Bakzye - bhojya in sense of food."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.69:input={word}"
	return f"7.3.69:BojyaM-Bakzye;{word}"


def apply_7_3_70(word, pos=""):
	"""Gorlopo leTi vA - Gh root, lopa optionally in lit."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.70:input={word}"
	return f"7.3.70:Gorlopo-leTi-vA;{word}"


def apply_7_3_71(word, pos=""):
	"""otaH Syani - ota before Syan affix."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.71:input={word}"
	return f"7.3.71:otaH-Syani;{word}"


def apply_7_3_72(word, pos=""):
	"""ksasyAci - ksa before ac affix."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.72:input={word}"
	return f"7.3.72:ksasyAci;{word}"


def apply_7_3_73(word, pos=""):
	"""lugvA duhadihalihaguhAmAtmanepade dantye - optionally lug for
	duh, dih, lih, guh in atmanepada dantyA."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.73:input={word}"
	return f"7.3.73:lugvA-duhadihalihaguhAmAtmanepade-dantye;{word}"


def apply_7_3_74(word, pos=""):
	"""SamAmazwAnAM dIrGaH Syani - sama, astha take dirgha in Syan."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.74:input={word}"
	return f"7.3.74:SamAmazwAnAM-dIrGaH-Syani;{word}"


def apply_7_3_75(word, pos=""):
	"""zWivuklamucamAM Siti - sTivu, klam, muc in sit affix."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.75:input={word}"
	return f"7.3.75:zWivuklamucamAM-Siti;{word}"


def apply_7_3_76(word, pos=""):
	"""kramaH parasmEpadezu - kram in parasmaipada."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.76:input={word}"
	return f"7.3.76:kramaH-parasmEpadezu;{word}"


def apply_7_3_77(word, pos=""):
	"""izugamiyamAM CaH - izu, gam, iya in Ca affix."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.77:input={word}"
	return f"7.3.77:izugamiyamAM-CaH;{word}"


def apply_7_3_78(word, pos=""):
	"""pAGrADmAsTAmnAdARdfSyarttisarttiSadasadAM pibajiGraDamatizWamanayacCapa
	SyarcCaDOSIyasIdAH - roots like pA, ghra, dhma, etc. specific affixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.78:input={word}"
	return f"7.3.78:pAGrADmAsTAmnAdARdfSyarttisarttiSadasadAM;{word}"


def apply_7_3_79(word, pos=""):
	"""jYAjanorjA - jna and jana take ja."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.79:input={word}"
	return f"7.3.79:jYAjanorjA;{word}"


def apply_7_3_80(word, pos=""):
	"""pvAdInAM hrasvaH - pva and related take hrasva (short vowel)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.80:input={word}"
	return f"7.3.80:pvAdInAM-hrasvaH;{word}"


def apply_7_3_81(word, pos=""):
	"""mInAternigame - minat in nigama context."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.81:input={word}"
	return f"7.3.81:mInAternigame;{word}"


def apply_7_3_82(word, pos=""):
	"""miderguRaH - mid gives guNa."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.82:input={word}"
	return f"7.3.82:miderguRaH;{word}"


def apply_7_3_83(word, pos=""):
	"""jusi ca - in jus affix also."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.83:input={word}"
	return f"7.3.83:jusi-ca;{word}"


def apply_7_3_84(word, pos=""):
	"""sArvaDAtukArDaDAtukayoH - sarva-dhatuka and ardha-dhatuka."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.84:input={word}"
	return f"7.3.84:sArvaDAtukArDaDAtukayoH;{word}"


def apply_7_3_85(word, pos=""):
	"""jAgro'viciRRalNitsu - jagr in avic, iRR, alN, its affixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.85:input={word}"
	return f"7.3.85:jAgro'viciRRalNitsu;{word}"


def apply_7_3_86(word, pos=""):
	"""pugantalaGUpaDasya ca - pu-ganta-laghu-upadha."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.86:input={word}"
	return f"7.3.86:pugantalaGUpaDasya;{word}"


def apply_7_3_87(word, pos=""):
	"""nAByastasyAci piti sArvaDAtuke - not abhyasta before ac, pi
	in sarva-dhatuka."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.87:input={word}"
	return f"7.3.87:nAByastasyAci-piti-sArvaDAtuke;{word}"


def apply_7_3_88(word, pos=""):
	"""BUsuvostiNi - BU, su, vu in tiG affixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.88:input={word}"
	return f"7.3.88:BUsuvostiNi;{word}"


def apply_7_3_89(word, pos=""):
	"""uto vfdDirluki hali - uto vrddhi when luki (elision) and hali."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.89:input={word}"
	return f"7.3.89:uto-vfdDirluki-hali;{word}"


def apply_7_3_90(word, pos=""):
	"""UrRoterviBAzA - UrR and uter optionally."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.90:input={word}"
	return f"7.3.90:UrRoterviBAzA;{word}"


def apply_7_3_91(word, pos=""):
	"""guRo'pfkte - guNa when not apRkta (not contracted)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.91:input={word}"
	return f"7.3.91:guRo'pfkte;{word}"


def apply_7_3_92(word, pos=""):
	"""tfRaha im - tfRa ha takes im."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.92:input={word}"
	return f"7.3.92:tfRaha-im;{word}"


def apply_7_3_93(word, pos=""):
	"""bruva Iw - bru takes It."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.93:input={word}"
	return f"7.3.93:bruva-Iw;{word}"


def apply_7_3_94(word, pos=""):
	"""yaNo vA - yaN optionally."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.94:input={word}"
	return f"7.3.94:yaNo-vA;{word}"


def apply_7_3_95(word, pos=""):
	"""turustuSamyamaH sArvaDAtuke - turu, stu, Samya in sarvadhatuka."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.95:input={word}"
	return f"7.3.95:turustuSamyamaH-sArvaDAtuke;{word}"


def apply_7_3_96(word, pos=""):
	"""astisico'pfkte - asti, sic when not apRkta."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.96:input={word}"
	return f"7.3.96:astisico'pfkte;{word}"


def apply_7_3_97(word, pos=""):
	"""bahulaM Candasi - freely in Vedic usage."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.97:input={word}"
	return f"7.3.97:bahulaM-Candasi;{word}"


def apply_7_3_98(word, pos=""):
	"""rudaSca paYcaByaH - rud and five others."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.98:input={word}"
	return f"7.3.98:rudaSca-paYcaByaH;{word}"


def apply_7_3_99(word, pos=""):
	"""aqgArgyagAlavayoH - argya, galava names."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.99:input={word}"
	return f"7.3.99:aqgArgyagAlavayoH;{word}"


def apply_7_3_100(word, pos=""):
	"""adaH sarvezAm - adaH before all affixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.100:input={word}"
	return f"7.3.100:adaH-sarvezAm;{word}"


def apply_7_3_101(word, pos=""):
	"""ato dIrGo yaYi - at gives dirgha before yaN affix."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.101:input={word}"
	return f"7.3.101:ato-dIrGo-yaYi;{word}"


def apply_7_3_102(word, pos=""):
	"""supi ca - in sup affixes also."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.102:input={word}"
	return f"7.3.102:supi-ca;{word}"


def apply_7_3_103(word, pos=""):
	"""bahuvacane Jalyet - in plural, Jat instead of et."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.103:input={word}"
	return f"7.3.103:bahuvacane-Jalyet;{word}"


def apply_7_3_104(word, pos=""):
	"""osi ca - in os affix also."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.104:input={word}"
	return f"7.3.104:osi-ca;{word}"


def apply_7_3_105(word, pos=""):
	"""ANi cApaH - AN before apa."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.105:input={word}"
	return f"7.3.105:ANi-cApaH;{word}"


def apply_7_3_106(word, pos=""):
	"""sambudDO ca - in sambuddhi (vocative)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.106:input={word}"
	return f"7.3.106:sambudDO-ca;{word}"


def apply_7_3_107(word, pos=""):
	"""ambA'rTanadyorhrasvaH - amba, arTa, nada take hrasva."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.107:input={word}"
	return f"7.3.107:ambA'rTanadyorhrasvaH;{word}"


def apply_7_3_108(word, pos=""):
	"""hrasvasya guRaH - hrasva gets guNa."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.108:input={word}"
	return f"7.3.108:hrasvasya-guRaH;{word}"


def apply_7_3_109(word, pos=""):
	"""jasi ca - in jas affix also."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.109:input={word}"
	return f"7.3.109:jasi-ca;{word}"


def apply_7_3_110(word, pos=""):
	"""fto NisarvanAmasTAnayoH - R before Ni and sarvanamasthana."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.110:input={word}"
	return f"7.3.110:fto-NisarvanAmasTAnayoH;{word}"


def apply_7_3_111(word, pos=""):
	"""GerNiti - Gh before Ni."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.111:input={word}"
	return f"7.3.111:GerNiti;{word}"


def apply_7_3_112(word, pos=""):
	"""ARnadyAH - AN before nadi (river names)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.112:input={word}"
	return f"7.3.112:ARnadyAH;{word}"


def apply_7_3_113(word, pos=""):
	"""yAqApaH - yAq before apa."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.113:input={word}"
	return f"7.3.113:yAqApaH;{word}"


def apply_7_3_114(word, pos=""):
	"""sarvanAmnaH syAqQrasvaSca - sarvanama takes syAq, hrasva."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.114:input={word}"
	return f"7.3.114:sarvanAmnaH-syAqQrasvaSca;{word}"


def apply_7_3_115(word, pos=""):
	"""viBAzA dvitIyAtftIyAByAm - optionally from 2nd and 3rd cases."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.115:input={word}"
	return f"7.3.115:viBAzA-dvitIyAtftIyAByAm;{word}"


def apply_7_3_116(word, pos=""):
	"""NerAmnadyAmnIByaH - Ni from amnady, amni."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.116:input={word}"
	return f"7.3.116:NgAmnadyAmnIByaH;{word}"


def apply_7_3_117(word, pos=""):
	"""idudByAm - id, ud before sup."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.117:input={word}"
	return f"7.3.117:idudByAm;{word}"


def apply_7_3_118(word, pos=""):
	"""Ot - O before t."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.118:input={word}"
	return f"7.3.118:Ot;{word}"


def apply_7_3_119(word, pos=""):
	"""acca GeH - ca before Gh affix."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.119:input={word}"
	return f"7.3.119:acca-GeH;{word}"


def apply_7_3_120(word, pos=""):
	"""ANo nA'striyAm - AN, but not in feminine."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.3.120:input={word}"
	return f"7.3.120:ANo-nA'striyAm;{word}"


ALL_7_3 = {
	"प.7.3.1": apply_7_3_1,
	"प.7.3.2": apply_7_3_2,
	"प.7.3.3": apply_7_3_3,
	"प.7.3.4": apply_7_3_4,
	"प.7.3.5": apply_7_3_5,
	"प.7.3.6": apply_7_3_6,
	"प.7.3.7": apply_7_3_7,
	"प.7.3.8": apply_7_3_8,
	"प.7.3.9": apply_7_3_9,
	"प.7.3.10": apply_7_3_10,
	"प.7.3.11": apply_7_3_11,
	"प.7.3.12": apply_7_3_12,
	"प.7.3.13": apply_7_3_13,
	"प.7.3.14": apply_7_3_14,
	"प.7.3.15": apply_7_3_15,
	"प.7.3.16": apply_7_3_16,
	"प.7.3.17": apply_7_3_17,
	"प.7.3.18": apply_7_3_18,
	"प.7.3.19": apply_7_3_19,
	"प.7.3.20": apply_7_3_20,
	"प.7.3.21": apply_7_3_21,
	"प.7.3.22": apply_7_3_22,
	"प.7.3.23": apply_7_3_23,
	"प.7.3.24": apply_7_3_24,
	"प.7.3.25": apply_7_3_25,
	"प.7.3.26": apply_7_3_26,
	"प.7.3.27": apply_7_3_27,
	"प.7.3.28": apply_7_3_28,
	"प.7.3.29": apply_7_3_29,
	"प.7.3.30": apply_7_3_30,
	"प.7.3.31": apply_7_3_31,
	"प.7.3.32": apply_7_3_32,
	"प.7.3.33": apply_7_3_33,
	"प.7.3.34": apply_7_3_34,
	"प.7.3.35": apply_7_3_35,
	"प.7.3.36": apply_7_3_36,
	"प.7.3.37": apply_7_3_37,
	"प.7.3.38": apply_7_3_38,
	"प.7.3.39": apply_7_3_39,
	"प.7.3.40": apply_7_3_40,
	"प.7.3.41": apply_7_3_41,
	"प.7.3.42": apply_7_3_42,
	"प.7.3.43": apply_7_3_43,
	"प.7.3.44": apply_7_3_44,
	"प.7.3.45": apply_7_3_45,
	"प.7.3.46": apply_7_3_46,
	"प.7.3.47": apply_7_3_47,
	"प.7.3.48": apply_7_3_48,
	"प.7.3.49": apply_7_3_49,
	"प.7.3.50": apply_7_3_50,
	"प.7.3.51": apply_7_3_51,
	"प.7.3.52": apply_7_3_52,
	"प.7.3.53": apply_7_3_53,
	"प.7.3.54": apply_7_3_54,
	"प.7.3.55": apply_7_3_55,
	"प.7.3.56": apply_7_3_56,
	"प.7.3.57": apply_7_3_57,
	"प.7.3.58": apply_7_3_58,
	"प.7.3.59": apply_7_3_59,
	"प.7.3.60": apply_7_3_60,
	"प.7.3.61": apply_7_3_61,
	"प.7.3.62": apply_7_3_62,
	"प.7.3.63": apply_7_3_63,
	"प.7.3.64": apply_7_3_64,
	"प.7.3.65": apply_7_3_65,
	"प.7.3.66": apply_7_3_66,
	"प.7.3.67": apply_7_3_67,
	"प.7.3.68": apply_7_3_68,
	"प.7.3.69": apply_7_3_69,
	"प.7.3.70": apply_7_3_70,
	"प.7.3.71": apply_7_3_71,
	"प.7.3.72": apply_7_3_72,
	"प.7.3.73": apply_7_3_73,
	"प.7.3.74": apply_7_3_74,
	"प.7.3.75": apply_7_3_75,
	"प.7.3.76": apply_7_3_76,
	"प.7.3.77": apply_7_3_77,
	"प.7.3.78": apply_7_3_78,
	"प.7.3.79": apply_7_3_79,
	"प.7.3.80": apply_7_3_80,
	"प.7.3.81": apply_7_3_81,
	"प.7.3.82": apply_7_3_82,
	"प.7.3.83": apply_7_3_83,
	"प.7.3.84": apply_7_3_84,
	"प.7.3.85": apply_7_3_85,
	"प.7.3.86": apply_7_3_86,
	"प.7.3.87": apply_7_3_87,
	"प.7.3.88": apply_7_3_88,
	"प.7.3.89": apply_7_3_89,
	"प.7.3.90": apply_7_3_90,
	"प.7.3.91": apply_7_3_91,
	"प.7.3.92": apply_7_3_92,
	"प.7.3.93": apply_7_3_93,
	"प.7.3.94": apply_7_3_94,
	"प.7.3.95": apply_7_3_95,
	"प.7.3.96": apply_7_3_96,
	"प.7.3.97": apply_7_3_97,
	"प.7.3.98": apply_7_3_98,
	"प.7.3.99": apply_7_3_99,
	"प.7.3.100": apply_7_3_100,
	"प.7.3.101": apply_7_3_101,
	"प.7.3.102": apply_7_3_102,
	"प.7.3.103": apply_7_3_103,
	"प.7.3.104": apply_7_3_104,
	"प.7.3.105": apply_7_3_105,
	"प.7.3.106": apply_7_3_106,
	"प.7.3.107": apply_7_3_107,
	"प.7.3.108": apply_7_3_108,
	"प.7.3.109": apply_7_3_109,
	"प.7.3.110": apply_7_3_110,
	"प.7.3.111": apply_7_3_111,
	"प.7.3.112": apply_7_3_112,
	"प.7.3.113": apply_7_3_113,
	"प.7.3.114": apply_7_3_114,
	"प.7.3.115": apply_7_3_115,
	"प.7.3.116": apply_7_3_116,
	"प.7.3.117": apply_7_3_117,
	"प.7.3.118": apply_7_3_118,
	"प.7.3.119": apply_7_3_119,
	"प.7.3.120": apply_7_3_120,
}
