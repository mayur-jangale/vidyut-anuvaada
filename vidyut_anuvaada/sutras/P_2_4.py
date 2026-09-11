"""Shared logic for the 85 sutras of P.2.4.x"""
from __future__ import annotations

# ── P.2.4: Avyaya (indeclinables) and Nipata rules ─────────────────────────
#
# Sutra layout (from the 85 individual P_2_4_N.py files):
# P.2.4.1 – P.2.4.30 : Avyaya definitions and samasa rules
# P.2.4.31 – P.2.4.85 : More avyaya / nipata / conjunction-particle rules
#
# Each apply_2_4_N function returns a marker string:
# "प.2.4.N:<short-label>;input=<word>;pos=<pos>"
# ─────────────────────────────────────────────────────────────────────────────


def apply_2_4_1(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.1:dvigurekavacanam;input=" + word + ";pos=" + pos

def apply_2_4_2(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.2:dvandvaSca-prARitUryasenANgAnAm;input=" + word + ";pos=" + pos

def apply_2_4_3(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.3:anuvAde-caraRAnAm;input=" + word + ";pos=" + pos

def apply_2_4_4(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.4:aDvaryukraturanapuMsakam;input=" + word + ";pos=" + pos

def apply_2_4_5(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.5:aDyayanato'viprakfzwAKyAnAm;input=" + word + ";pos=" + pos

def apply_2_4_6(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.6:jAtiraprARinAm;input=" + word + ";pos=" + pos

def apply_2_4_7(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.7:viSizwaliNgo-nadI-deSo'grAmAH;input=" + word + ";pos=" + pos

def apply_2_4_8(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.8:kzudrajantavaH;input=" + word + ";pos=" + pos

def apply_2_4_9(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.9:yezAM-ca-viroDaH-SASvatikaH;input=" + word + ";pos=" + pos

def apply_2_4_10(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.10:SUdrARamaniravasitAnAm;input=" + word + ";pos=" + pos

def apply_2_4_11(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.11:gavASvapraBftIni-ca;input=" + word + ";pos=" + pos

def apply_2_4_12(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.12:viBAzA-vfkzamfgatfRaDAnyavyaYjanapaSuSakunyaSvavaqavapUrvAparADarottarARAm;input=" + word + ";pos=" + pos

def apply_2_4_13(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.13:vipratizidDaM-cAnaDikaraRavAci;input=" + word + ";pos=" + pos

def apply_2_4_14(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.14:na-daDipayAdIni;input=" + word + ";pos=" + pos

def apply_2_4_15(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.15:aDikaraREtAvattve-ca;input=" + word + ";pos=" + pos

def apply_2_4_16(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.16:viBAzA-samIpe;input=" + word + ";pos=" + pos

def apply_2_4_17(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.17:sa-napuMsakam;input=" + word + ";pos=" + pos

def apply_2_4_18(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.18:avyayIBAvaSca;input=" + word + ";pos=" + pos

def apply_2_4_19(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.19:tatpuruzo'naY-karmaDArayaH;input=" + word + ";pos=" + pos

def apply_2_4_20(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.20:saMjYAyAM-kanToSInarezu;input=" + word + ";pos=" + pos

def apply_2_4_21(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.21:upajYopakramaM-tadAdyAciKyAsAyAm;input=" + word + ";pos=" + pos

def apply_2_4_22(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.22:CAyA-bAhulye;input=" + word + ";pos=" + pos

def apply_2_4_23(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.23:saBA-rAjAmanuzyapUrvA;input=" + word + ";pos=" + pos

def apply_2_4_24(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.24:aSAlA-ca;input=" + word + ";pos=" + pos

def apply_2_4_25(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.25:viBAzA-senAsurAcCAyASAlAniSAnAm;input=" + word + ";pos=" + pos

def apply_2_4_26(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.26:paravalliNgaM-dvandvatatpuruzayoH;input=" + word + ";pos=" + pos

def apply_2_4_27(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.27:pUrvavadaSvavaqavO;input=" + word + ";pos=" + pos

def apply_2_4_28(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.28:hemantaSiSirAvahorAtre-ca-cCandasi;input=" + word + ";pos=" + pos

def apply_2_4_29(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.29:rAtrAhnAhAH-puMsi;input=" + word + ";pos=" + pos

def apply_2_4_30(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.30:apaTaM-napuMsakam;input=" + word + ";pos=" + pos

def apply_2_4_31(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.31:arDarcAH-puMsi-ca;input=" + word + ";pos=" + pos

def apply_2_4_32(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.32:idamo'nvAdeSe'SanudAttastftIyAdO;input=" + word + ";pos=" + pos

def apply_2_4_33(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.33:etadastratasostratasO-cAnudAttO;input=" + word + ";pos=" + pos

def apply_2_4_34(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.34:dvitIyAwOssvenaH;input=" + word + ";pos=" + pos

def apply_2_4_35(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.35:ArDaDAtuke;input=" + word + ";pos=" + pos

def apply_2_4_36(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.36:ado-jagDirlyapti-kiti;input=" + word + ";pos=" + pos

def apply_2_4_37(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.37:luNsanorGasx;input=" + word + ";pos=" + pos

def apply_2_4_38(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.38:GaYapoSca;input=" + word + ";pos=" + pos

def apply_2_4_39(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.39:bahulaM-Candasi;input=" + word + ";pos=" + pos

def apply_2_4_40(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.40:liwyanyatarasyAm;input=" + word + ";pos=" + pos

def apply_2_4_41(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.41:veYo-vayiH;input=" + word + ";pos=" + pos

def apply_2_4_42(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.42:hano-vaDa-liNi;input=" + word + ";pos=" + pos

def apply_2_4_43(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.43:luNi-ca;input=" + word + ";pos=" + pos

def apply_2_4_44(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.44:AtmanepadezvanyatarasyAm;input=" + word + ";pos=" + pos

def apply_2_4_45(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.45:iRo-gA-luNi;input=" + word + ";pos=" + pos

def apply_2_4_46(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.46:RO-gamiraboDane;input=" + word + ";pos=" + pos

def apply_2_4_47(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.47:sani-ca;input=" + word + ";pos=" + pos

def apply_2_4_48(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.48:iNaSca;input=" + word + ";pos=" + pos

def apply_2_4_49(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.49:gAN-liwi;input=" + word + ";pos=" + pos

def apply_2_4_50(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.50:viBAzA-luNlfNoH;input=" + word + ";pos=" + pos

def apply_2_4_51(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.51:RO-ca-sa~ScaNoH;input=" + word + ";pos=" + pos

def apply_2_4_52(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.52:asterBUH;input=" + word + ";pos=" + pos

def apply_2_4_53(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.53:bruvo-vaciH;input=" + word + ";pos=" + pos

def apply_2_4_54(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.54:cakziNaH-KyAY;input=" + word + ";pos=" + pos

def apply_2_4_55(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.55:vA-liwi;input=" + word + ";pos=" + pos

def apply_2_4_56(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.56:ajervyaGaYapoH;input=" + word + ";pos=" + pos

def apply_2_4_57(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.57:vA-yO;input=" + word + ";pos=" + pos

def apply_2_4_58(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.58:RyakzatriyArzaYito-yUni-lugaRiYoH;input=" + word + ";pos=" + pos

def apply_2_4_59(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.59:pElAdiByaSca;input=" + word + ";pos=" + pos

def apply_2_4_60(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.60:iYaH-prAcAm;input=" + word + ";pos=" + pos

def apply_2_4_61(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.61:na-tOlvaliByaH;input=" + word + ";pos=" + pos

def apply_2_4_62(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.62:tadrAjasya-bahuzu-tenEvAstriyAm;input=" + word + ";pos=" + pos

def apply_2_4_63(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.63:yaskAdiByo-gotre;input=" + word + ";pos=" + pos

def apply_2_4_64(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.64:yaYaYoSca;input=" + word + ";pos=" + pos

def apply_2_4_65(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.65:atriBfgukutsavasizWagotamANgiroByaSca;input=" + word + ";pos=" + pos

def apply_2_4_66(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.66:bahvacaH-iYaH-prAcyaBaratezu;input=" + word + ";pos=" + pos

def apply_2_4_67(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.67:na-gopavanAdiByaH;input=" + word + ";pos=" + pos

def apply_2_4_68(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.68:tikakitavAdiByo-dvandve;input=" + word + ";pos=" + pos

def apply_2_4_69(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.69:upakAdiByo'nyatarasyAmadvandve;input=" + word + ";pos=" + pos

def apply_2_4_70(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.70:AgastyakORqinyayoragastikuRqinac;input=" + word + ";pos=" + pos

def apply_2_4_71(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.71:supo-DAtuprAtipadikayoH;input=" + word + ";pos=" + pos

def apply_2_4_72(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.72:adipraBftiByaH-SapaH;input=" + word + ";pos=" + pos

def apply_2_4_73(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.73:bahulaM-Candasi;input=" + word + ";pos=" + pos

def apply_2_4_74(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.74:yaNo'ci-ca;input=" + word + ";pos=" + pos

def apply_2_4_75(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.75:juhotyAdiByaH-SluH;input=" + word + ";pos=" + pos

def apply_2_4_76(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.76:bahulaM-Candasi;input=" + word + ";pos=" + pos

def apply_2_4_77(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.77:gAtisTAGupABUByaH-sicaH-parasmEpadezu;input=" + word + ";pos=" + pos

def apply_2_4_78(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.78:viBAzA-GrADewSAcCAsaH;input=" + word + ";pos=" + pos

def apply_2_4_79(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.79:tanAdiByastaTAsoH;input=" + word + ";pos=" + pos

def apply_2_4_80(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.80:mantre-GasahvaraRaSavfdahAdvfckfgamijaniByo-leH;input=" + word + ";pos=" + pos

def apply_2_4_81(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.81:AmaH;input=" + word + ";pos=" + pos

def apply_2_4_82(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.82:avyayAdApsupaH;input=" + word + ";pos=" + pos

def apply_2_4_83(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.83:nAvyayIBAvAdato'mtvapaYcamyAH;input=" + word + ";pos=" + pos

def apply_2_4_84(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.84:tftIyAsaptamyorbahulam;input=" + word + ";pos=" + pos

def apply_2_4_85(word, pos="", SUTRA_TOKEN=""):
	return "प.2.4.85:luwaH-praTamasya-qArOrasaH;input=" + word + ";pos=" + pos
