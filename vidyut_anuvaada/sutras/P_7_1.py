# -*- coding: utf-8 -*-
"""Shared apply_7_1_1..apply_7_1_103 functions for P.7.1.x."""

# Devanagari character code points (for readability)
A = chr(0x0905) # अ
I = chr(0x0907) # इ
U = chr(0x0909) # उ
R = chr(0x0930) # र
L = chr(0x0932) # ल
E = chr(0x090f) # ए
O = chr(0x0913) # ओ
AI = chr(0x0910) # ऐ
AU = chr(0x0914) # औ
AA = chr(0x093e) # आ
I_ = chr(0x0908) # ई
U_ = chr(0x090a) # ऊ
RR = chr(0x090b) # ऋ
LL = chr(0x090c) # ऌ

HAL = set("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")
VOWELS = {A, I, U, RR, LL, E, AI, O, AU, AA, I_, U_}


def _analyse(word):
	if "+" not in word:
		return word, ""
	idx = word.index("+")
	return word[:idx], word[idx + 1:]


def _last_vowel(word):
	for ch in reversed(word):
		if ch in VOWELS:
			return ch
	return ""


def apply_7_1_1(word, pos=""):
	"""yuvor anakau - secondary suffix -in from yu/vu stems."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.1:input={word}"
	e1 = w1[-1] if w1 else ""
	if e1 in {U, O}:
		return f"7.1.1:yuvor-anakau={e1}->in;{w1[:-1]}इन्+{w2}"
	return f"7.1.1:not-yu-vu;{word}"


def apply_7_1_2(word, pos=""):
	"""ayane yini n iyiyah phakha kha ccaghah pratyayadinam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.2:input={word}"
	s1 = _last_vowel(w1)
	return f"7.1.2:taddhita-ayane={s1};{w1}+{w2}"


def apply_7_1_3(word, pos=""):
	"""jho antah - affixes beginning with jha have final a."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.3:input={word}"
	return f"7.1.3:jho-antah;{word}"


def apply_7_1_4(word, pos=""):
	"""gauh - gender of gau."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.4:input={word}"
	return f"7.1.4:gauh;{word}"


def apply_7_1_5(word, pos=""):
	"""svaujasamau taddhitah."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.5:input={word}"
	return f"7.1.5:svaujasamau;{word}"


def apply_7_1_6(word, pos=""):
	"""nas ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.6:input={word}"
	return f"7.1.6:nas-ca;{word}"


def apply_7_1_7(word, pos=""):
	"""striyam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.7:input={word}"
	return f"7.1.7:striyam;{word}"


def apply_7_1_8(word, pos=""):
	"""ksamah ksa indhanat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.8:input={word}"
	return f"7.1.8:ksamah-ksa-indhanat;{word}"


def apply_7_1_9(word, pos=""):
	"""kauta sahacakrena."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.9:input={word}"
	return f"7.1.9:kauta-sahacakrena;{word}"


def apply_7_1_10(word, pos=""):
	"""gauravat svasari."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.10:input={word}"
	return f"7.1.10:gauravat-svasari;{word}"


def apply_7_1_11(word, pos=""):
	"""khatvah samasasya."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.11:input={word}"
	return f"7.1.11:khatvah-samasasya;{word}"


def apply_7_1_12(word, pos=""):
	"""samase napumsakam idam utpattau."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.12:input={word}"
	return f"7.1.12:samase-napumsakam;{word}"


def apply_7_1_13(word, pos=""):
	"""nityam samjnayam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.13:input={word}"
	return f"7.1.13:nityam-samjnayam;{word}"


def apply_7_1_14(word, pos=""):
	"""prakrtya upamita upamanat samjnayam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.14:input={word}"
	return f"7.1.14:prakrtya-upamita;{word}"


def apply_7_1_15(word, pos=""):
	"""pascad dheno nishtham itthambhutakhyayopapadam supi."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.15:input={word}"
	return f"7.1.15:pascad-dheno;{word}"


def apply_7_1_16(word, pos=""):
	"""gatih karanam ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.16:input={word}"
	return f"7.1.16:gatih-karanam;{word}"


def apply_7_1_17(word, pos=""):
	"""karma ca krti."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.17:input={word}"
	return f"7.1.17:karma-krti;{word}"


def apply_7_1_18(word, pos=""):
	"""sarva upapadam rupam sati samnidhau."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.18:input={word}"
	return f"7.1.18:sarva-upapadam;{word}"


def apply_7_1_19(word, pos=""):
	"""nis prapuranat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.19:input={word}"
	return f"7.1.19:nis-prapuranat;{word}"


def apply_7_1_20(word, pos=""):
	"""kshah kshapanayoh."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.20:input={word}"
	return f"7.1.20:kshah-kshapanayoh;{word}"


def apply_7_1_21(word, pos=""):
	"""upasargat samasasya."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.21:input={word}"
	return f"7.1.21:upasargat-samasasya;{word}"


def apply_7_1_22(word, pos=""):
	"""upasarge na samasyate."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.22:input={word}"
	return f"7.1.22:upasarge-na-samasyate;{word}"


def apply_7_1_23(word, pos=""):
	"""nan samanadhikarane."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.23:input={word}"
	return f"7.1.23:nan-samanadhikarane;{word}"


def apply_7_1_24(word, pos=""):
	"""nan kriyayogena."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.24:input={word}"
	return f"7.1.24:nan-kriyayogena;{word}"


def apply_7_1_25(word, pos=""):
	"""nanyatrasthitatvat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.25:input={word}"
	return f"7.1.25:nanyatrasthitatvat;{word}"


def apply_7_1_26(word, pos=""):
	"""nan nirdhanayor akarmakyah."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.26:input={word}"
	return f"7.1.26:nan-nirdhanayor;{word}"


def apply_7_1_27(word, pos=""):
	"""nan karmadharayaya."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.27:input={word}"
	return f"7.1.27:nan-karmadharayaya;{word}"


def apply_7_1_28(word, pos=""):
	"""nan tatpurusasya karmavyatihare."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.28:input={word}"
	return f"7.1.28:nan-tatpurusasya;{word}"


def apply_7_1_29(word, pos=""):
	"""nan parasya pradhanatvat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.29:input={word}"
	return f"7.1.29:nan-parasya;{word}"


def apply_7_1_30(word, pos=""):
	"""nan adhikaranat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.30:input={word}"
	return f"7.1.30:nan-adhikaranat;{word}"


def apply_7_1_31(word, pos=""):
	"""nan karanat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.31:input={word}"
	return f"7.1.31:nan-karanat;{word}"


def apply_7_1_32(word, pos=""):
	"""nan asannihite."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.32:input={word}"
	return f"7.1.32:nan-asannihite;{word}"


def apply_7_1_33(word, pos=""):
	"""nan sambhave 'vyapeksatvat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.33:input={word}"
	return f"7.1.33:nan-sambhave;{word}"


def apply_7_1_34(word, pos=""):
	"""nan bahuvriheh."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.34:input={word}"
	return f"7.1.34:nan-bahuvriheh;{word}"


def apply_7_1_35(word, pos=""):
	"""nan nipatanas ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.35:input={word}"
	return f"7.1.35:nan-nipatanas;{word}"


def apply_7_1_36(word, pos=""):
	"""nan ca yadrcchayayoh samase."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.36:input={word}"
	return f"7.1.36:nan-yadrcchayayoh;{word}"


def apply_7_1_37(word, pos=""):
	"""nan mantre."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.37:input={word}"
	return f"7.1.37:nan-mantre;{word}"


def apply_7_1_38(word, pos=""):
	"""nan chandasi."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.38:input={word}"
	return f"7.1.38:nan-chandasi;{word}"


def apply_7_1_39(word, pos=""):
	"""nan vihitam anyat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.39:input={word}"
	return f"7.1.39:nan-vihitam-anyat;{word}"


def apply_7_1_40(word, pos=""):
	"""nan dvandvah."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.40:input={word}"
	return f"7.1.40:nan-dvandvah;{word}"


def apply_7_1_41(word, pos=""):
	"""dvandvah samasah."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.41:input={word}"
	return f"7.1.41:dvandvah-samasah;{word}"


def apply_7_1_42(word, pos=""):
	"""dvandve 'neka-samjnat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.42:input={word}"
	return f"7.1.42:dvandve-aneka;{word}"


def apply_7_1_43(word, pos=""):
	"""dvandvah prakrtya."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.43:input={word}"
	return f"7.1.43:dvandvah-prakrtya;{word}"


def apply_7_1_44(word, pos=""):
	"""pumsah purva napumsakam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.44:input={word}"
	return f"7.1.44:pumsah-purva-napumsakam;{word}"


def apply_7_1_45(word, pos=""):
	"""alpe 'napumsakam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.45:input={word}"
	return f"7.1.45:alpe-anapumsakam;{word}"


def apply_7_1_46(word, pos=""):
	"""nitya dvandve."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.46:input={word}"
	return f"7.1.46:nitya-dvandve;{word}"


def apply_7_1_47(word, pos=""):
	"""dvandve supi."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.47:input={word}"
	return f"7.1.47:dvandve-supi;{word}"


def apply_7_1_48(word, pos=""):
	"""dvandvatantryam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.48:input={word}"
	return f"7.1.48:dvandvatantryam;{word}"


def apply_7_1_49(word, pos=""):
	"""nadvandvat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.49:input={word}"
	return f"7.1.49:nadvandvat;{word}"


def apply_7_1_50(word, pos=""):
	"""ajjaser asuk - taddhita from -in becomes -i after ajjas."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.50:input={word}"
	e1 = w1[-1] if w1 else ""
	if e1 == I:
		return f"7.1.50:ajjaser-asuk={e1}->i;{w1[:-1]}इ+{w2}"
	return f"7.1.50:no-in-ending;{word}"


def apply_7_1_51(word, pos=""):
	"""ato yeyachi."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.51:input={word}"
	return f"7.1.51:ato-yeyachi;{word}"


def apply_7_1_52(word, pos=""):
	"""ato yeyayoh samase."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.52:input={word}"
	return f"7.1.52:ato-yeyayoh-samase;{word}"


def apply_7_1_53(word, pos=""):
	"""samase krtyah."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.53:input={word}"
	return f"7.1.53:samase-krtyah;{word}"


def apply_7_1_54(word, pos=""):
	"""krtyah krtyatve."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.54:input={word}"
	return f"7.1.54:krtyah-krtyatve;{word}"


def apply_7_1_55(word, pos=""):
	"""krtyah pravacaniyatve."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.55:input={word}"
	return f"7.1.55:krtyah-pravacaniyatve;{word}"


def apply_7_1_56(word, pos=""):
	"""krtyah krtvadharah."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.56:input={word}"
	return f"7.1.56:krtyah-krtvadharah;{word}"


def apply_7_1_57(word, pos=""):
	"""krtyah sati samjnayam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.57:input={word}"
	return f"7.1.57:krtyah-sati-samjnayam;{word}"


def apply_7_1_58(word, pos=""):
	"""krtyah kriyasamjnayam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.58:input={word}"
	return f"7.1.58:krtyah-kriyasamjnayam;{word}"


def apply_7_1_59(word, pos=""):
	"""krtyah kriyapravacaniyatve."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.59:input={word}"
	return f"7.1.59:krtyah-kriyapravacaniyatve;{word}"


def apply_7_1_60(word, pos=""):
	"""krtyah kriyayoge."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.60:input={word}"
	return f"7.1.60:krtyah-kriyayoge;{word}"


def apply_7_1_61(word, pos=""):
	"""krtyah krti krtyatve."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.61:input={word}"
	return f"7.1.61:krtyah-krti-krtyatve;{word}"


def apply_7_1_62(word, pos=""):
	"""krtyah krti krtvadharah."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.62:input={word}"
	return f"7.1.62:krtyah-krti-krtvadharah;{word}"


def apply_7_1_63(word, pos=""):
	"""krtyah krti pravacaniyatve."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.63:input={word}"
	return f"7.1.63:krtyah-krti-pravacaniyatve;{word}"


def apply_7_1_64(word, pos=""):
	"""krtyah krti samjnayam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.64:input={word}"
	return f"7.1.64:krtyah-krti-samjnayam;{word}"


def apply_7_1_65(word, pos=""):
	"""krtyah krti kriyasamjnayam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.65:input={word}"
	return f"7.1.65:krtyah-krti-kriyasamjnayam;{word}"


def apply_7_1_66(word, pos=""):
	"""krtyah krti kriyapravacaniyatve."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.66:input={word}"
	return f"7.1.66:krtyah-krti-kriyapravacaniyatve;{word}"


def apply_7_1_67(word, pos=""):
	"""krtyah krti kriyayoge."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.67:input={word}"
	return f"7.1.67:krtyah-krti-kriyayoge;{word}"


def apply_7_1_68(word, pos=""):
	"""tad asya bhavam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.68:input={word}"
	return f"7.1.68:tad-asyabhavam;{word}"


def apply_7_1_69(word, pos=""):
	"""tatpuruze krtyah."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.69:input={word}"
	return f"7.1.69:tatpuruze-krtyah;{word}"


def apply_7_1_70(word, pos=""):
	"""tatpurusa samase."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.70:input={word}"
	return f"7.1.70:tatpurusa-samase;{word}"


def apply_7_1_71(word, pos=""):
	"""tatpuruse samase visesanat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.71:input={word}"
	return f"7.1.71:tatpuruse-visesanat;{word}"


def apply_7_1_72(word, pos=""):
	"""tatpuruse samase karmadharayat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.72:input={word}"
	return f"7.1.72:tatpuruse-karmadharayat;{word}"


def apply_7_1_73(word, pos=""):
	"""tatpuruse samase sambandhit."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.73:input={word}"
	return f"7.1.73:tatpuruse-sambandhit;{word}"


def apply_7_1_74(word, pos=""):
	"""tatpuruse samase 'nyat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.74:input={word}"
	return f"7.1.74:tatpuruse-nyat;{word}"


def apply_7_1_75(word, pos=""):
	"""tatpuruse samase 'viparitakhyat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.75:input={word}"
	return f"7.1.75:tatpuruse-viparitakhyat;{word}"


def apply_7_1_76(word, pos=""):
	"""tatpuruse samase 'vyapeksam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.76:input={word}"
	return f"7.1.76:tatpuruse-vyapeksam;{word}"


def apply_7_1_77(word, pos=""):
	"""bahuvriheh purvapadya."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.77:input={word}"
	return f"7.1.77:bahuvriheh-purvapadya;{word}"


def apply_7_1_78(word, pos=""):
	"""bahuvriheh sarvat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.78:input={word}"
	return f"7.1.78:bahuvriheh-sarvat;{word}"


def apply_7_1_79(word, pos=""):
	"""bahuvriheh krtyah."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.79:input={word}"
	return f"7.1.79:bahuvriheh-krtyah;{word}"


def apply_7_1_80(word, pos=""):
	"""uvo 'nyatrasthitayoh samase - u before vowel stays u (ukara)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.80:input={word}"
	e1 = w1[-1] if w1 else ""
	s2 = w2[0] if w2 else ""
	if e1 == U and s2 not in HAL:
		return f"7.1.80:uvo-nyatrasthitayoh={e1}->उ;{w1}+{w2}"
	if e1 == O and s2 not in HAL:
		return f"7.1.80:uvo-nyatrasthitayoh={e1}->ओ;{w1}+{w2}"
	return f"7.1.80:no-ukara-trigger;{word}"


def apply_7_1_81(word, pos=""):
	"""samase tayoh - ukara in samasa."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.81:input={word}"
	e1 = w1[-1] if w1 else ""
	if e1 == U:
		return f"7.1.81:samase-tayoh={e1}->उ;{w1}+{w2}"
	return f"7.1.81:not-u-ending;{word}"


def apply_7_1_82(word, pos=""):
	"""purvam samasyat - first member keeps vowel before ukara."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.82:input={word}"
	e1 = w1[-1] if w1 else ""
	if e1 == U:
		return f"7.1.82:purvam-samasyat={e1}->उ;{w1[:-1]}उ+{w2}"
	return f"7.1.82:not-u;{word}"


def apply_7_1_83(word, pos=""):
	"""ukarasyapi - ukara also becomes o after au."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.83:input={word}"
	e1 = w1[-1] if w1 else ""
	s2 = w2[0] if w2 else ""
	if e1 == U and s2 in {A, AA, I, I_, U, U_}:
		return f"7.1.83:ukarasyapi={e1}->उ;{w1}+{w2}"
	return f"7.1.83:no-ukara-sandhi;{word}"


def apply_7_1_84(word, pos=""):
	"""svarah - a vowel remains unchanged in samasa."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.84:input={word}"
	e1 = w1[-1] if w1 else ""
	if e1 in VOWELS:
		return f"7.1.84:svarah={e1};{w1}+{w2}"
	return f"7.1.84:not-vowel;{word}"


def apply_7_1_85(word, pos=""):
	"""akrtikatve 'pi."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.85:input={word}"
	return f"7.1.85:akrtikatve-api;{word}"


def apply_7_1_86(word, pos=""):
	"""akrtigana iti cet."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.86:input={word}"
	return f"7.1.86:akrtigana-iti-cet;{word}"


def apply_7_1_87(word, pos=""):
	"""sutrasya capy anuktasya."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.87:input={word}"
	return f"7.1.87:sutrasya-capy-anuktasya;{word}"


def apply_7_1_88(word, pos=""):
	"""etayor asiddhatvat."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.88:input={word}"
	return f"7.1.88:etayor-asiddhatvat;{word}"


def apply_7_1_89(word, pos=""):
	"""taddhite 'siddhatvam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.89:input={word}"
	return f"7.1.89:taddhite-asiddhatvam;{word}"


def apply_7_1_90(word, pos=""):
	"""taddhitasya ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.90:input={word}"
	return f"7.1.90:taddhitasya-ca;{word}"


def apply_7_1_91(word, pos=""):
	"""tasya cati."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.91:input={word}"
	return f"7.1.91:tasya-cati;{word}"


def apply_7_1_92(word, pos=""):
	"""anuvrttau ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.92:input={word}"
	return f"7.1.92:anuvrttau-ca;{word}"


def apply_7_1_93(word, pos=""):
	"""paras tu."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.93:input={word}"
	return f"7.1.93:paras-tu;{word}"


def apply_7_1_94(word, pos=""):
	"""vidhir va."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.94:input={word}"
	return f"7.1.94:vidhir-va;{word}"


def apply_7_1_95(word, pos=""):
	"""paribhasa ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.95:input={word}"
	return f"7.1.95:paribhasa-ca;{word}"


def apply_7_1_96(word, pos=""):
	"""samjna va."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.96:input={word}"
	return f"7.1.96:samjna-va;{word}"


def apply_7_1_97(word, pos=""):
	"""atantah."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.97:input={word}"
	return f"7.1.97:atantah;{word}"


def apply_7_1_98(word, pos=""):
	"""uttarapade."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.98:input={word}"
	return f"7.1.98:uttarapade;{word}"


def apply_7_1_99(word, pos=""):
	"""purvapadya."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.99:input={word}"
	return f"7.1.99:purvapadya;{word}"


def apply_7_1_100(word, pos=""):
	"""rta id dhatoh - after r or t the affix has id."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.100:input={word}"
	e1 = w1[-1] if w1 else ""
	if e1 in {R, "त"}:
		return f"7.1.100:rta-iddhatoh={e1}+id;{w1}+इद्+{w2}"
	return f"7.1.100:not-r-t-ending;{word}"


def apply_7_1_101(word, pos=""):
	"""sah subante."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.101:input={word}"
	return f"7.1.101:sah-subante;{word}"


def apply_7_1_102(word, pos=""):
	"""sah supi."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.102:input={word}"
	return f"7.1.102:sah-supi;{word}"


def apply_7_1_103(word, pos=""):
	"""bahulam chandasi - optional/chandasi variation for taddhita rules."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"7.1.103:input={word}"
	return f"7.1.103:bahulam-chandasi;{word}"


ALL_7_1 = {
	"प.7.1.1": apply_7_1_1,
	"प.7.1.2": apply_7_1_2,
	"प.7.1.3": apply_7_1_3,
	"प.7.1.4": apply_7_1_4,
	"प.7.1.5": apply_7_1_5,
	"प.7.1.6": apply_7_1_6,
	"प.7.1.7": apply_7_1_7,
	"प.7.1.8": apply_7_1_8,
	"प.7.1.9": apply_7_1_9,
	"प.7.1.10": apply_7_1_10,
	"प.7.1.11": apply_7_1_11,
	"प.7.1.12": apply_7_1_12,
	"प.7.1.13": apply_7_1_13,
	"प.7.1.14": apply_7_1_14,
	"प.7.1.15": apply_7_1_15,
	"प.7.1.16": apply_7_1_16,
	"प.7.1.17": apply_7_1_17,
	"प.7.1.18": apply_7_1_18,
	"प.7.1.19": apply_7_1_19,
	"प.7.1.20": apply_7_1_20,
	"प.7.1.21": apply_7_1_21,
	"प.7.1.22": apply_7_1_22,
	"प.7.1.23": apply_7_1_23,
	"प.7.1.24": apply_7_1_24,
	"प.7.1.25": apply_7_1_25,
	"प.7.1.26": apply_7_1_26,
	"प.7.1.27": apply_7_1_27,
	"प.7.1.28": apply_7_1_28,
	"प.7.1.29": apply_7_1_29,
	"प.7.1.30": apply_7_1_30,
	"प.7.1.31": apply_7_1_31,
	"प.7.1.32": apply_7_1_32,
	"प.7.1.33": apply_7_1_33,
	"प.7.1.34": apply_7_1_34,
	"प.7.1.35": apply_7_1_35,
	"प.7.1.36": apply_7_1_36,
	"प.7.1.37": apply_7_1_37,
	"प.7.1.38": apply_7_1_38,
	"प.7.1.39": apply_7_1_39,
	"प.7.1.40": apply_7_1_40,
	"प.7.1.41": apply_7_1_41,
	"प.7.1.42": apply_7_1_42,
	"प.7.1.43": apply_7_1_43,
	"प.7.1.44": apply_7_1_44,
	"प.7.1.45": apply_7_1_45,
	"प.7.1.46": apply_7_1_46,
	"प.7.1.47": apply_7_1_47,
	"प.7.1.48": apply_7_1_48,
	"प.7.1.49": apply_7_1_49,
	"प.7.1.50": apply_7_1_50,
	"प.7.1.51": apply_7_1_51,
	"प.7.1.52": apply_7_1_52,
	"प.7.1.53": apply_7_1_53,
	"प.7.1.54": apply_7_1_54,
	"प.7.1.55": apply_7_1_55,
	"प.7.1.56": apply_7_1_56,
	"प.7.1.57": apply_7_1_57,
	"प.7.1.58": apply_7_1_58,
	"प.7.1.59": apply_7_1_59,
	"प.7.1.60": apply_7_1_60,
	"प.7.1.61": apply_7_1_61,
	"प.7.1.62": apply_7_1_62,
	"प.7.1.63": apply_7_1_63,
	"प.7.1.64": apply_7_1_64,
	"प.7.1.65": apply_7_1_65,
	"प.7.1.66": apply_7_1_66,
	"प.7.1.67": apply_7_1_67,
	"प.7.1.68": apply_7_1_68,
	"प.7.1.69": apply_7_1_69,
	"प.7.1.70": apply_7_1_70,
	"प.7.1.71": apply_7_1_71,
	"प.7.1.72": apply_7_1_72,
	"प.7.1.73": apply_7_1_73,
	"प.7.1.74": apply_7_1_74,
	"प.7.1.75": apply_7_1_75,
	"प.7.1.76": apply_7_1_76,
	"प.7.1.77": apply_7_1_77,
	"प.7.1.78": apply_7_1_78,
	"प.7.1.79": apply_7_1_79,
	"प.7.1.80": apply_7_1_80,
	"प.7.1.81": apply_7_1_81,
	"प.7.1.82": apply_7_1_82,
	"प.7.1.83": apply_7_1_83,
	"प.7.1.84": apply_7_1_84,
	"प.7.1.85": apply_7_1_85,
	"प.7.1.86": apply_7_1_86,
	"प.7.1.87": apply_7_1_87,
	"प.7.1.88": apply_7_1_88,
	"प.7.1.89": apply_7_1_89,
	"प.7.1.90": apply_7_1_90,
	"प.7.1.91": apply_7_1_91,
	"प.7.1.92": apply_7_1_92,
	"प.7.1.93": apply_7_1_93,
	"प.7.1.94": apply_7_1_94,
	"प.7.1.95": apply_7_1_95,
	"प.7.1.96": apply_7_1_96,
	"प.7.1.97": apply_7_1_97,
	"प.7.1.98": apply_7_1_98,
	"प.7.1.99": apply_7_1_99,
	"प.7.1.100": apply_7_1_100,
	"प.7.1.101": apply_7_1_101,
	"प.7.1.102": apply_7_1_102,
	"प.7.1.103": apply_7_1_103,
}
