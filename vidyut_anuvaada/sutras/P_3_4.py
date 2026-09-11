# -*- coding: utf-8 -*-
from __future__ import annotations

import re

PA = chr(0x092A)

TIP = "ति"
TAS = "तः"
JHI = "न्ति"
SIP = "सि"
VAS = "वः"
MAS = "मः"
TA = "त"
ATAM = "ताम्"
JA = "इ"
JAS = "इव"
THA = "थ"
ATHAM = "थाम्"
DVAM = "ध्वम्"
MI = "मि"
VAS_P = "व"
MAH_P = "म"
TI_NAMES = [TIP, TAS, JHI, SIP, VAS, MAS, TA, ATAM, JA, JAS, THA, ATHAM, DVAM, MI, VAS_P, MAH_P]

ROOT_GAM = "गम्"
ROOT_KRI = "कृ"
ROOT_BHU = "भू"
ROOT_STHA = "स्था"
ROOT_PATH = "पठ्"
ROOT_DRU = "द्रु"
ROOT_VAD = "वद्"
ROOT_AS = "अस्"

def _verb_stem(word):
	if not word:
		return word
	for ln in (3, 2, 1):
		if len(word) >= ln and word[-ln:] in (JHI, ATHAM, ATAM, SIP, "तु", "त्"):
			return word[:-ln]
	return word

def _last_char(word):
	return word[-1] if word else ""

def _has_it(word):
	return word.endswith("इ") or word.endswith("इत्")

def _has_at(word):
	return "त्" in word



def apply_3_4_1(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-001:dhAtu-pratyaya sambandha"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_2(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-002:kriya-samuccaya low"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_3(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-003:samuccaye anyatarasyAm"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_4(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-004:yaTA-vid-anuprayogaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_5(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-005:samuccaye sAmAnya"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_6(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-006:Candasi luN laN liT"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_7(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-007:liN-arTe leT"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_8(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-008:upasamvAda ASaNka"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_9(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-009:tum-arTe sesenase"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_10(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-010:prayE rohiSye avyaTiSye"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_11(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-011:dfSe viKye ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_12(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-012:Saki Ramul kamulO"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_13(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-013:ISvare tosun kasunO"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_14(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-014:kfty-arTe tavya"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_15(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-015:avacakze ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_16(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-016:BAva-lakzaRe tosun"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_17(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-017:sfpi tfdoH kasun"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_18(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-018:alaNKalvoH prAcAM ktvA"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_19(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-019:udIcAM mANo vyatIhAre"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_20(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-020:parAvara-yoge ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_21(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-021:samAna-kartfkoH pUrvakAle lyap"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_22(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-022:ABIkzRye Ramul ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_23(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-023:na yadi anAkANkze"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_24(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-024:viBAzA gre prathama pUrve"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_25(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-025:karmaRi AkroSe kfYaH khamuY"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_26(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-026:svAdumi Ramul"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_27(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-027:anyaTA evaM kaTam itTaMsu"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_28(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-028:yaTA taTA asUyAprativacane"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_29(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-029:karmaRi dfSividoH sAkalye"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_30(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-030:yAvati vindajIvoH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_31(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-031:carmodarayoH pUraH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_32(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-032:varza-pramARa Ulopa ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_33(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-033:cele knopeH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_34(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-034:nimUla samUla kaSaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_35(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-035:Suzka cUrNa rUkzezu pizaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_36(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-036:samUlA Akfta jIvezu"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_37(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-037:karaRe hanaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_38(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-038:snehane pizaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_39(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-039:haste vartti grahoH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_40(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-040:sve puzaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_41(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-041:aDikaraRe banDaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_42(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-042:saMjYAyAm"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_43(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-043:kartror jIva puruZayoH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_44(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-044:UrDve Suzi pUraH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_45(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-045:upamAne karmaRi ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_46(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-046:kazAdizu anuprayogaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_47(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-047:upadaMSa tfIyAyAm"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_48(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-048:hiMsArTAnAM ca samAnakarmakARAm"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_49(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-049:saptamyAM ca upapIqa ruDa kfza"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_50(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-050:samAsattO"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_51(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-051:pramARe ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_52(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-052:apAdAne parIpsAyAm"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_53(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-053:dvitIyAyAM ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_54(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-054:svANge aDruve"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_55(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-055:parikliSyamAne ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_56(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-056:viSi pati padi skandAM vyApya"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_57(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-057:asyati tfzaH kriyA'ntare kAlezu"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_58(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-058:nAmnyAdi Si grahoH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_59(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-059:avyaye'yaTABipretAKyAne kfYaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_60(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-060:tiryacyapavarge"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_61(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-061:svANge taspratyaye kfBvoH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_62(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-062:na ADA'rTa pratyaye cvyarTe"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_63(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-063:tuSNImi BuvuH ktin"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_64(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-064:anvacyAnulomye"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_65(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-065:Saka tRz etc. arTezu tumun"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_66(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-066:paryApte vacanezu alaM arTezu"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_67(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-067:kartari kft"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_68(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-068:Bavya geya etc. vA"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_69(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-069:laH karmaRi ca BAve cAkarmakeByaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_70(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-070:tayoH eva kftya-kta-Kal-arthaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_71(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-071:AdikarmaRi ktaH kartari ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_72(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-072:gatyarTAkarmaka SliSa SIga"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_73(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-073:dASa goGnO sampradAne"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_74(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-074:BImAdayo'apAdAne"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_75(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-075:tAByAm anyatroNAdayaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_76(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-076:kto'DikaraRe ca DROvya"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_77(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-077:lasya"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_78(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-078:tiptas-jhi-sip-thas-mip-vas-mas"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_79(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-079:Tit AtmanepadAnAM TeRe"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_80(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-080:TAsas se"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_81(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-081:liwas taYjor eSirec"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_82(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-082:parasmaipadAnAM Ralatusu"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_83(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-083:vido lawo vA leT"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_84(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-084:BruvaH paYcAnAm Adit Aho"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_85(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-085:loTo laNvat"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_86(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-086:vidhiliN eruH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_87(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-087:ASIrliN ser hyap icca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_88(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-088:vA Candasi luG"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_89(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-089:mer niH lRG"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_90(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-090:AmetaH sArvadhAtuka"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_91(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-091:savAByAM vAmO"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_92(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-092:AD uttamasya picca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_93(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-093:eta ai liT"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_94(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-094:leTo aDAwO liG-ASiSi"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_95(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-095:Ata ai ekAj liG"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_96(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-096:vEto'nyatra"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_97(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-097:itaSca lopaH parasmEpadeSu"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_98(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-098:sa uttamasya"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_99(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-099:nityaM NitaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_100(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-100:itaSca tNi lopaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_101(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-101:tasthastha mipAM tAMta tAmaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_102(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-102:liNas sI yuT"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_103(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-103:yAsuT parasmEpadeSu udAtta"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_104(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-104:kid AsiSi"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_105(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-105:Yasya ran"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_106(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-106:iTo at Snasor"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_107(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-107:suT TitoH svAsryAH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_108(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-108:Yer jus svAsRNAm"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_109(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-109:sij aByasta vidiByaSca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_110(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-110:AtaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_111(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-111:laNaH SAkATAyanasyaiva"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_112(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-112:dviSaz ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_113(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-113:tiN Sit sArvadhAtukam"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_114(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-114:ArDadhAtukaM SezaH"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_115(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-115:liT ca"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_116(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-116:liN AsiSi"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos

def apply_3_4_117(word, pos="", SUTRA_TOKEN=""):
	tag = "p34-117:CandasyuBayatTA"
	stem = _verb_stem(word)
	ending = word[len(stem):] if word else ""
	matched = ending or "-"
	return tag + ";input=" + word + ";stem=" + stem + ";ending=" + matched + ";pos=" + pos