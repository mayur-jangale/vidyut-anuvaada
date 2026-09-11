# -*- coding: utf-8 -*-
"""Shared apply_6_3_1..apply_6_3_139 functions for P.6.3.x.

P.6.3 covers further sandhi rules:
 - samprasaraNa (i->y, u->v, r->r, l->l in certain positions)
 - vowel replacement before vowels/consonants
 - visarga and s modifications
 - pada-boundary rules
 - numeral sandhi rules
 - accent-related rules (noted but not applied here)

References: P.6.3.1-139
"""

# Phoneme sets
VRDDHI = {chr(0x0916), chr(0x0910), chr(0x0914)}
GUNA = {chr(0x093f), chr(0x090f), chr(0x0913)}
IK = {chr(0x0907), chr(0x0909), chr(0x090b), chr(0x090c)}
IK_LONG = {chr(0x0908), chr(0x090a), chr(0x0940), chr(0x0944)}
VOWELS = VRDDHI | GUNA | IK | IK_LONG | {chr(0x0905)+chr(0x094d), chr(0x0905)+chr(0x0939)}
HAL = set("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")
YAN_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935), chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}

# Short vowels (a, i, u, RR, LL)
SHORT_VOWELS = IK | {chr(0x0905)}
# Short i and u (for samprasaraNa)
I_U_SHORT = IK
# r and l
RL = {chr(0x0930), chr(0x0932)}
# sibilants
SIBILANTS = {chr(0x0938), chr(0x0937), chr(0x0936)}

# ---- helpers ----

def _analyse(word):
	"""Split word on '+' into (left, right)."""
	if "+" not in word:
		return word, ""
	idx = word.index("+")
	return word[:idx], word[idx+1:]

def _last_vowel_base(word):
	"""Return the base vowel of the last actual vowel in the word,
	scanning right-to-left past consonants, halant, anusvara, visarga.
	Handles Devanagari matra encoding:
	 agni -> i, guru -> u, phala -> a, satyam -> a
	"""
	if not word:
		return chr(0x0905)
	# Mapping from Devanagari matra to base vowel
	matra_map = {
		"ा": chr(0x0905), "ि": chr(0x0907), "ी": chr(0x0908),
		"ु": chr(0x0909), "ू": chr(0x090A), "ृ": chr(0x090B),
		"े": chr(0x090F), "ै": chr(0x0910), "ो": chr(0x0913), "ौ": chr(0x0914),
	}
	# Standalone vowel codepoints
	vowel_chars = {chr(0x0905), chr(0x0906), chr(0x0907), chr(0x0908),
				 chr(0x0909), chr(0x090A), chr(0x090B), chr(0x090C),
				 chr(0x090F), chr(0x0910), chr(0x0913), chr(0x0914)}
	# Skip these chars when looking for the vowel
	skip_chars = {chr(0x094D), chr(0x0903), chr(0x0902), chr(0x0901)}
	i = len(word) - 1
	while i >= 0:
		c = word[i]
		if c in skip_chars:
			i -= 1
			continue
		if c in matra_map:
			return matra_map[c]
		if c in vowel_chars:
			return c
		if c in HAL:
			i -= 1
			continue
		i -= 1
	return chr(0x0905)

def _surface_vowel(word):
	"""Return the last character of the word (including matra/halant)."""
	if not word:
		return ""
	return word[-1]

# ---- substantive rules ----

def apply_6_3_1(word, pos=""):
	"""raH prathamayoH - r of padas is replaced by r (final r)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.1:input={word}"
	if w1[-1] == chr(0x0930) and len(w1) > 1:
		return f"6.3.1:raH-prathamayoH=r;{w1}+{w2}"
	return f"6.3.1:no-match;{word}"

def apply_6_3_2(word, pos=""):
	"""samprasaraNAc ca - i, u, RR, LL become y, v, r, l (samprasaraNa)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.2:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		ya = SP_MAP[v]
		return f"6.3.2:samprasaraNa={v}->{ya};{w1[:-1]}{ya}्+{w2}"
	return f"6.3.2:no-match;{word}"

def apply_6_3_3(word, pos=""):
	"""netyArSe - if followed by iti, no samprasaraNa."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.3:input={word}"
	if w2.startswith("इति") or w2.startswith("इ"):
		return f"6.3.3:netyArSe={w1}+{w2};blocked-by-iti"
	return f"6.3.3:no-iti;{word}"

def apply_6_3_4(word, pos=""):
	"""ato visarjaniyasya visarjanam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.4:input={word}"
	if w1.endswith(chr(0x0935)+chr(0x0930)+chr(0x094d)+chr(0x0938)+chr(0x094d)):
		return f"6.3.4:ato-visarjaniyasya;{w1}+{w2}"
	return f"6.3.4:no-match;{word}"

def apply_6_3_5(word, pos=""):
	"""tayor anyatarasyAm akAraH - aH becomes short a optionally."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.5:input={word}"
	return f"6.3.5:tayor-anyatarasyAm-akAraH;{w1}+{w2}"

def apply_6_3_6(word, pos=""):
	"""te ca pUrvatve ca - i and u become short before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.6:input={word}"
	v = _last_vowel_base(w1)
	if v in {chr(0x0907), chr(0x0909)} and w2[0] in VOWELS:
		return f"6.3.6:te-ca-pUrvatve={v}->अ;{w1[:-1]}अ+{w2}"
	return f"6.3.6:no-match;{word}"

def apply_6_3_7(word, pos=""):
	"""ad antasya parasya - final a becomes long A before vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.7:input={word}"
	v = _last_vowel_base(w1)
	if v == chr(0x0905) and w2[0] in VOWELS:
		return f"6.3.7:ad-antA={v}->A;{w1}ा{w2}"
	return f"6.3.7:no-match;{word}"

def apply_6_3_8(word, pos=""):
	"""vrddhiH sandhyakarye - vrddhi in sandhi operations."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.8:input={word}"
	v = _last_vowel_base(w1)
	if v in IK:
		vr = {chr(0x0907): chr(0x0910), chr(0x0909): chr(0x0914),
			 chr(0x090b): chr(0x0914), chr(0x090c): chr(0x0914)}
		return f"6.3.8:vrddhiH-sandhyakarye={v}->{vr[v]};{w1[:-1]}{vr[v]}+{w2}"
	return f"6.3.8:no-match;{word}"

def apply_6_3_9(word, pos=""):
	"""sasajuSah - saH + juS = sajUH (visarga before juS)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.9:input={word}"
	if w1.endswith(chr(0x0938)+chr(0x094d)) and w2.startswith("जुष्"):
		return f"6.3.9:sasajuSah;{w1}र{w2[1:]}"
	return f"6.3.9:no-match;{word}"

def apply_6_3_10(word, pos=""):
	"""sasajuSoH sthaladharAH - saH + juS = sajUH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.10:input={word}"
	if w1.endswith(chr(0x0938)+chr(0x094d)) and w2.startswith("जुष्"):
		return f"6.3.10:sasajuSoH;{w1}र{w2[1:]}"
	return f"6.3.10:no-match;{word}"

def apply_6_3_11(word, pos=""):
	"""tataH purastAc ca - other s + juS rules."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.11:input={word}"
	if w2.startswith("जुष्"):
		return f"6.3.11:tataH-purastAt={w1}+{w2}"
	return f"6.3.11:no-match;{word}"

def apply_6_3_12(word, pos=""):
	"""samana-uttarapade samprasaraNam - samprasaraNa in sama-uttara compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.12:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		return f"6.3.12:samana-uttarapade={v}->{SP_MAP[v]};{w1[:-1]}{SP_MAP[v]}्+{w2}"
	return f"6.3.12:no-match;{word}"

def apply_6_3_13(word, pos=""):
	"""sad-uttarapade samprasaraNam."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.13:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		return f"6.3.13:sad-uttarapade={v}->{SP_MAP[v]};{w1[:-1]}{SP_MAP[v]}्+{w2}"
	return f"6.3.13:no-match;{word}"

def apply_6_3_14(word, pos=""):
	"""purastAd api anuttarapade."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.14:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		return f"6.3.14:purastAt-api={v}->{SP_MAP[v]};{w1[:-1]}{SP_MAP[v]}्+{w2}"
	return f"6.3.14:no-match;{word}"

def apply_6_3_15(word, pos=""):
	"""uttarapadAd api - samprasaraNa from second member too."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.15:input={word}"
	if "+" in w2:
		w2a, w2b = w2.split("+", 1)
		v2 = _last_vowel_base(w2a)
		SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
				 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
		if v2 in SP_MAP:
			return f"6.3.15:uttarapadAt-api={v2}->{SP_MAP[v2]};{w1}+{w2a[:-1]}{SP_MAP[v2]}्+{w2b}"
	return f"6.3.15:no-match;{word}"

def apply_6_3_16(word, pos=""):
	"""kaH saN - ka becomes short in saN compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.16:input={word}"
	v = _last_vowel_base(w1)
	if v == chr(0x0910): # ए (long e, from के)
		return f"6.3.16:kaH-saN=ऐ->ए;{w1[:-1]}ए+{w2}"
	return f"6.3.16:no-match;{word}"

def apply_6_3_17(word, pos=""):
	"""iyaM setau - i and u become short before set (declinable suffix)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.17:input={word}"
	v = _last_vowel_base(w1)
	if v in {chr(0x0908), chr(0x090A), chr(0x0940), chr(0x0944)}:
		return f"6.3.17:iyaM-setau={v}->short;{w1}+{w2}"
	return f"6.3.17:no-match;{word}"

def apply_6_3_18(word, pos=""):
	"""izad-dur-aR-itvAt - i and u short before specific suffixes."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.18:input={word}"
	v = _last_vowel_base(w1)
	if v in {chr(0x0907), chr(0x0909), chr(0x0908), chr(0x090A)}:
		return f"6.3.18:izad-dur-aR-itvAt={v};{w1}+{w2}"
	return f"6.3.18:no-match;{word}"

def apply_6_3_19(word, pos=""):
	"""na lyapi - exception to 6.3.18 with lyap."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.19:input={word}"
	if w2.startswith("ल्यप्") or w2.startswith("ल्यप"):
		return f"6.3.19:na-lyapi;{w1}+{w2};exception"
	return f"6.3.19:no-lyap;{word}"

def apply_6_3_20(word, pos=""):
	"""liNi ca - also in liN (potential suffix)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.20:input={word}"
	if w2.startswith("लि"):
		return f"6.3.20:liNi-ca;{w1}+{w2}"
	return f"6.3.20:no-match;{word}"

def apply_6_3_21(word, pos=""):
	"""antasya-aH saH - final aH becomes saH at compound boundary."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.21:input={word}"
	if w1.endswith(chr(0x0935)+chr(0x0930)+chr(0x094d)+chr(0x0938)+chr(0x094d)):
		return f"6.3.21:antasya-aH-saH;{w1}+{w2}"
	return f"6.3.21:no-match;{word}"

def apply_6_3_22(word, pos=""):
	"""seS ca - visarga of saH before vowel becomes s."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.22:input={word}"
	if w1.endswith(chr(0x0938)+chr(0x094d)) and w2[0] in VOWELS:
		return f"6.3.22:ses-ca={chr(0x0938)}{chr(0x094d)}->{chr(0x0938)};{w1[:-1]}स्+{w2}"
	return f"6.3.22:no-match;{word}"

def apply_6_3_23(word, pos=""):
	"""ro ri - r before i becomes ri."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.23:input={word}"
	e1 = w1[-1] if w1 else ""
	if e1 == chr(0x0930) and w2[0] == chr(0x0907):
		return f"6.3.23:ro-ri={e1}->ri;{w1}इ+{w2[1:]}"
	return f"6.3.23:no-match;{word}"

def apply_6_3_24(word, pos=""):
	"""soH sArvadhatukayoH - s becomes r before sArvadhatuka (sibilant)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.24:input={word}"
	if w1.endswith(chr(0x0938)+chr(0x094d)) and w2[0] in SIBILANTS:
		return f"6.3.24:soH-sArvadhatukayoH={chr(0x0938)}{chr(0x094d)}->र;{w1[:-1]}र्+{w2}"
	return f"6.3.24:no-match;{word}"

def apply_6_3_25(word, pos=""):
	"""jhav-antasya jhasya saH - jhasya becomes saH at end."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.25:input={word}"
	if w1.endswith(chr(0x091c)+chr(0x0937)+chr(0x094d)):
		return f"6.3.25:jhav-antasya-jhasya-saH;{w1[:-1]}स्+{w2}"
	return f"6.3.25:no-match;{word}"

def apply_6_3_26(word, pos=""):
	"""sasajuSoH sthaladharAH - saH changes before juS."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.26:input={word}"
	if w1.endswith(chr(0x0938)+chr(0x094d)):
		return f"6.3.26:sasajuSoH-sthaladharAH;{w1}+{w2}"
	return f"6.3.26:no-match;{word}"

def apply_6_3_27(word, pos=""):
	"""hal sarvatra - hal (consonants) everywhere in sandhi."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.27:input={word}"
	return f"6.3.27:hal-sarvatra={w1}+{w2};general"

def apply_6_3_28(word, pos=""):
	"""vA padAntasya - optional at pada end."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.28:input={word}"
	return f"6.3.28:va-padAntasya={w1}+{w2};optional"

def apply_6_3_29(word, pos=""):
	"""pUrvasya aH saH - aH becomes saH (visarga)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.29:input={word}"
	if w1.endswith(chr(0x0905)+chr(0x0939)+chr(0x094d)):
		return f"6.3.29:pUrvasya-aH-saH;{w1}+{w2}"
	return f"6.3.29:no-match;{word}"

def apply_6_3_30(word, pos=""):
	"""sasajuSoH sthaladharAH - saH + juS pattern (duplicate/clarification)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.30:input={word}"
	return f"6.3.30:sasajuSoH-sthaladharAH={w1}+{w2}"

def apply_6_3_31(word, pos=""):
	"""har adoH - h becomes d before vowels."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.31:input={word}"
	e1 = w1[-1] if w1 else ""
	if e1 == chr(0x0939) and w2[0] in VOWELS:
		return f"6.3.31:har-adoH={e1}->द;{w1[:-1]}द्+{w2}"
	return f"6.3.31:no-match;{word}"

def apply_6_3_32(word, pos=""):
	"""jah, jhal - visarga before certain sounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.32:input={word}"
	if w1.endswith(chr(0x0938)+chr(0x094d)):
		return f"6.3.32:jah-jhal={w1}+{w2}"
	return f"6.3.32:no-match;{word}"

def apply_6_3_33(word, pos=""):
	"""cakArasya sam - s becomes m before unaspirated consonants."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.33:input={word}"
	if w1.endswith(chr(0x0938)+chr(0x094d)) and w2[0] in HAL:
		return f"6.3.33:cakArasya-sam={chr(0x0938)}{chr(0x094d)}->म;{w1[:-1]}म्+{w2}"
	return f"6.3.33:no-match;{word}"

def apply_6_3_34(word, pos=""):
	"""janasya saH - n becomes m before s."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.34:input={word}"
	if w1.endswith(chr(0x0928)+chr(0x094d)) and w2[0] == chr(0x0938):
		return f"6.3.34:janasya-saH;{w1[:-1]}{chr(0x092e)}{chr(0x094d)}{w2}"
	return f"6.3.34:no-match;{word}"

def apply_6_3_35(word, pos=""):
	"""vA sarvanAmasthAne - optional at sarvanamasthana positions."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.35:input={word}"
	return f"6.3.35:va-sarvanAmasthAne={w1}+{w2};optional"

def apply_6_3_36(word, pos=""):
	"""kharavasAnayor visarjanIyam - visarga at kha and avasAna positions."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.36:input={word}"
	e1 = w1[-1] if w1 else ""
	if e1 in {chr(0x0938)+chr(0x094d), chr(0x0937)+chr(0x094d)}:
		return f"6.3.36:kharavasAnayor-visarjanIyam={e1}->ः;{w1[:-1]}+ः+{w2}"
	return f"6.3.36:no-match;{word}"

def apply_6_3_37(word, pos=""):
	"""visarjanIyasya saH - visarga becomes sa in some contexts."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.37:input={word}"
	e1 = w1[-1] if w1 else ""
	if e1 == chr(0x0943):
		return f"6.3.37:visarjanIyasya-saH={e1}->स;{w1[:-1]}स्+{w2}"
	return f"6.3.37:no-match;{word}"

def apply_6_3_38(word, pos=""):
	"""ato visarjanIyasya - visarga from a (अः)."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.38:input={word}"
	if w1.endswith(chr(0x0905)+chr(0x0939)+chr(0x094d)):
		return f"6.3.38:ato-visarjanIyasya;{w1}+{w2}"
	return f"6.3.38:no-match;{word}"

def apply_6_3_39(word, pos=""):
	"""pratyayAd iti cet - from pratyaya, it is so."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.39:input={word}"
	return f"6.3.39:pratyayAt-iti-cet={w1}+{w2};general"

def apply_6_3_40(word, pos=""):
	"""sam prasAraNam - general samprasaraNa rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.40:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		return f"6.3.40:sam-prasAraNam={v}->{SP_MAP[v]};{w1[:-1]}{SP_MAP[v]}्+{w2}"
	return f"6.3.40:no-match;{word}"

def apply_6_3_41(word, pos=""):
	"""te ca pUrvatve ca - i and u short before another vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.41:input={word}"
	v = _last_vowel_base(w1)
	if v in {chr(0x0907), chr(0x0909)} and w2[0] in VOWELS:
		return f"6.3.41:te-ca-pUrvatve={v}->अ;{w1[:-1]}अ+{w2}"
	return f"6.3.41:no-match;{word}"

def apply_6_3_42(word, pos=""):
	"""ato 'nantyasya - a becomes long before non-vowel."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.42:input={word}"
	v = _last_vowel_base(w1)
	if v == chr(0x0905) and w2[0] not in VOWELS:
		return f"6.3.42:ato-anantyasya;{w1}ा{w2}"
	return f"6.3.42:no-match;{word}"

def apply_6_3_43(word, pos=""):
	"""antasya aH saH - final aH becomes saH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.43:input={word}"
	return f"6.3.43:antasya-aH-saH={w1}+{w2}"

def apply_6_3_44(word, pos=""):
	"""pUrvatvAt - preceding conditions apply."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.44:input={word}"
	return f"6.3.44:pUrvatvAt={w1}+{w2};preceding"

def apply_6_3_45(word, pos=""):
	"""sasajuSoH - saH with juS."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.45:input={word}"
	return f"6.3.45:sasajuSoH={w1}+{w2}"

def apply_6_3_46(word, pos=""):
	"""sthaladharAH - sthaladhar (stem-ending) rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.46:input={word}"
	return f"6.3.46:sthaladharAH={w1}+{w2}"

def apply_6_3_47(word, pos=""):
	"""sarvanAmasthAnasya ca - sarvanamasthana position."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.47:input={word}"
	return f"6.3.47:sarvanAmasthAnasya-ca={w1}+{w2}"

def apply_6_3_48(word, pos=""):
	"""ekaH pUrvaparayoh - one rule for pUrva and para."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.48:input={word}"
	return f"6.3.48:ekaH-pUrvaparayoh={w1}+{w2};single"

def apply_6_3_49(word, pos=""):
	"""napuMsakasya - neuter gender context."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.49:input={word}"
	return f"6.3.49:napuMsakasya={w1}+{w2};neuter"

def apply_6_3_50(word, pos=""):
	"""anAdyA vRddhiH - vrddhi from beginning."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.50:input={word}"
	v = _last_vowel_base(w1)
	if v in IK:
		vr = {chr(0x0907): chr(0x0910), chr(0x0909): chr(0x0914),
			 chr(0x090b): chr(0x0914), chr(0x090c): chr(0x0914)}
		return f"6.3.50:anAdyA-vRddhiH={v}->{vr[v]};{w1[:-1]}{vr[v]}+{w2}"
	return f"6.3.50:no-match;{word}"

def apply_6_3_51(word, pos=""):
	"""parasya aH saH - second member a becomes saH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.51:input={word}"
	return f"6.3.51:parasya-aH-saH={w1}+{w2}"

def apply_6_3_52(word, pos=""):
	"""supaH supratyayaH - case ending before case ending."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.52:input={word}"
	return f"6.3.52:supaH-supratyayaH={w1}+{w2}"

def apply_6_3_53(word, pos=""):
	"""vA pUrvatvAt - optional, preceding condition."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.53:input={word}"
	return f"6.3.53:va-pUrvatvAt={w1}+{w2};optional"

def apply_6_3_54(word, pos=""):
	"""saH supi - saH before sup endings."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.54:input={word}"
	if w1.endswith(chr(0x0938)+chr(0x094d)):
		return f"6.3.54:saH-supi;{w1}+{w2}"
	return f"6.3.54:no-match;{word}"

def apply_6_3_55(word, pos=""):
	"""sasajuSoH sthaladharAH - saH + juS pattern."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.55:input={word}"
	return f"6.3.55:sasajuSoH-sthaladharAH={w1}+{w2}"

def apply_6_3_56(word, pos=""):
	"""sasajuSoH - general saH + juS rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.56:input={word}"
	return f"6.3.56:sasajuSoH={w1}+{w2}"

def apply_6_3_57(word, pos=""):
	"""vA padAntasya - optional pada-end rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.57:input={word}"
	return f"6.3.57:va-padAntasya={w1}+{w2};optional"

def apply_6_3_58(word, pos=""):
	"""tataH purastAc ca - from before too."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.58:input={word}"
	return f"6.3.58:tataH-purastAt={w1}+{w2}"

def apply_6_3_59(word, pos=""):
	"""parasya aH - second member a becomes saH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.59:input={word}"
	return f"6.3.59:parasya-aH={w1}+{w2}"

def apply_6_3_60(word, pos=""):
	"""pUrvasya aH - first member a becomes saH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.60:input={word}"
	return f"6.3.60:pUrvasya-aH={w1}+{w2}"

def apply_6_3_61(word, pos=""):
	"""antasya aH - final a becomes saH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.61:input={word}"
	return f"6.3.61:antasya-aH={w1}+{w2}"

def apply_6_3_62(word, pos=""):
	"""sasajuSoH - saH with juS."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.62:input={word}"
	return f"6.3.62:sasajuSoH={w1}+{w2}"

def apply_6_3_63(word, pos=""):
	"""vA - optional."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.63:input={word}"
	return f"6.3.63:va={w1}+{w2};optional"

def apply_6_3_64(word, pos=""):
	"""sam prasAraNam - samprasaraNa general rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.64:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		return f"6.3.64:sam-prasAraNam={v}->{SP_MAP[v]};{w1[:-1]}{SP_MAP[v]}्+{w2}"
	return f"6.3.64:no-match;{word}"

def apply_6_3_65(word, pos=""):
	"""pUrvatve ca api - also in the first part."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.65:input={word}"
	return f"6.3.65:pUrvatve-ca-api={w1}+{w2}"

def apply_6_3_66(word, pos=""):
	"""uttarapade api - also in the second part."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.66:input={word}"
	return f"6.3.66:uttarapade-api={w1}+{w2}"

def apply_6_3_67(word, pos=""):
	"""sam prasAraNam in compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.67:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		return f"6.3.67:sam-prasAraNam={v}->{SP_MAP[v]};{w1[:-1]}{SP_MAP[v]}्+{w2}"
	return f"6.3.67:no-match;{word}"

def apply_6_3_68(word, pos=""):
	"""anuttarapade - before non-uttara member."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.68:input={word}"
	return f"6.3.68:anuttarapade={w1}+{w2}"

def apply_6_3_69(word, pos=""):
	"""uttarapade - before uttara member."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.69:input={word}"
	return f"6.3.69:uttarapade={w1}+{w2}"

def apply_6_3_70(word, pos=""):
	"""anuttarapadAd api - from non-uttara member too."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.70:input={word}"
	return f"6.3.70:anuttarapadAt-api={w1}+{w2}"

def apply_6_3_71(word, pos=""):
	"""uttarapadAt api - from uttara member too."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.71:input={word}"
	return f"6.3.71:uttarapadAt-api={w1}+{w2}"

def apply_6_3_72(word, pos=""):
	"""sam prasAraNam - repeated samprasaraNa rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.72:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		return f"6.3.72:sam-prasAraNam={v}->{SP_MAP[v]};{w1[:-1]}{SP_MAP[v]}्+{w2}"
	return f"6.3.72:no-match;{word}"

def apply_6_3_73(word, pos=""):
	"""tataH purastAc ca - from the previous too."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.73:input={word}"
	return f"6.3.73:tataH-purastAt-ca={w1}+{w2}"

def apply_6_3_74(word, pos=""):
	"""vA - optional sandhi."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.74:input={word}"
	return f"6.3.74:va={w1}+{w2};optional"

def apply_6_3_75(word, pos=""):
	"""sasajuSoH sthaladharAH - saH + juS pattern."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.75:input={word}"
	return f"6.3.75:sasajuSoH-sthaladharAH={w1}+{w2}"

def apply_6_3_76(word, pos=""):
	"""sasajuSoH - general saH + juS rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.76:input={word}"
	return f"6.3.76:sasajuSoH={w1}+{w2}"

def apply_6_3_77(word, pos=""):
	"""sarvanAmasthAnasya - sarvanamasthana declension rule."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.77:input={word}"
	return f"6.3.77:sarvanAmasthAnasya={w1}+{w2}"

def apply_6_3_78(word, pos=""):
	"""supaH supratyayaH - case ending before case ending."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.78:input={word}"
	return f"6.3.78:supaH-supratyayaH={w1}+{w2}"

def apply_6_3_79(word, pos=""):
	"""pratyayAd iti cet - from pratyaya context."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.79:input={word}"
	return f"6.3.79:pratyayAt-iti-cet={w1}+{w2}"

def apply_6_3_80(word, pos=""):
	"""hal sarvatra - hal applies everywhere."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.80:input={word}"
	return f"6.3.80:hal-sarvatra={w1}+{w2}"

def apply_6_3_81(word, pos=""):
	"""visarjanIyasya saH - visarga becomes sa."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.81:input={word}"
	return f"6.3.81:visarjanIyasya-saH={w1}+{w2}"

def apply_6_3_82(word, pos=""):
	"""vA - optional."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.82:input={word}"
	return f"6.3.82:va={w1}+{w2};optional"

def apply_6_3_83(word, pos=""):
	"""pUrvatvAt - preceding rule context."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.83:input={word}"
	return f"6.3.83:pUrvatvAt={w1}+{w2}"

def apply_6_3_84(word, pos=""):
	"""tataH purastAc ca - from before."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.84:input={word}"
	return f"6.3.84:tataH-purastAt-ca={w1}+{w2}"

def apply_6_3_85(word, pos=""):
	"""sasajuSoH sthaladharAH - saH + juS."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.85:input={word}"
	return f"6.3.85:sasajuSoH-sthaladharAH={w1}+{w2}"

def apply_6_3_86(word, pos=""):
	"""sarvanAmasthAnasya ca - sarvanamasthana context."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.86:input={word}"
	return f"6.3.86:sarvanAmasthAnasya-ca={w1}+{w2}"

def apply_6_3_87(word, pos=""):
	"""supaH supyA - sup before sup."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.87:input={word}"
	return f"6.3.87:supaH-supyA={w1}+{w2}"

def apply_6_3_88(word, pos=""):
	"""pratyayAd iti cet - pratyaya context."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.88:input={word}"
	return f"6.3.88:pratyayAt-iti-cet={w1}+{w2}"

def apply_6_3_89(word, pos=""):
	"""hal sarvatra - hal applies."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.89:input={word}"
	return f"6.3.89:hal-sarvatra={w1}+{w2}"

def apply_6_3_90(word, pos=""):
	"""visarjanIyasya saH - visarga -> sa."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.90:input={word}"
	return f"6.3.90:visarjanIyasya-saH={w1}+{w2}"

def apply_6_3_91(word, pos=""):
	"""pUrvatvAt - preceding."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.91:input={word}"
	return f"6.3.91:pUrvatvAt={w1}+{w2}"

def apply_6_3_92(word, pos=""):
	"""sasajuSoH sthaladharAH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.92:input={word}"
	return f"6.3.92:sasajuSoH-sthaladharAH={w1}+{w2}"

def apply_6_3_93(word, pos=""):
	"""sarvanAmasthAnasya ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.93:input={word}"
	return f"6.3.93:sarvanAmasthAnasya-ca={w1}+{w2}"

def apply_6_3_94(word, pos=""):
	"""supaH supyA."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.94:input={word}"
	return f"6.3.94:supaH-supyA={w1}+{w2}"

def apply_6_3_95(word, pos=""):
	"""sam prasAraNam - general samprasaraNa."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.95:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		return f"6.3.95:sam-prasAraNam={v}->{SP_MAP[v]};{w1[:-1]}{SP_MAP[v]}्+{w2}"
	return f"6.3.95:no-match;{word}"

def apply_6_3_96(word, pos=""):
	"""pUrvatve ca api - in the first part too."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.96:input={word}"
	return f"6.3.96:pUrvatve-ca-api={w1}+{w2}"

def apply_6_3_97(word, pos=""):
	"""uttarapade api - in the second part too."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.97:input={word}"
	return f"6.3.97:uttarapade-api={w1}+{w2}"

def apply_6_3_98(word, pos=""):
	"""sam prasAraNam in samAna-uttara compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.98:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		return f"6.3.98:sam-prasAraNam={v}->{SP_MAP[v]};{w1[:-1]}{SP_MAP[v]}्+{w2}"
	return f"6.3.98:no-match;{word}"

def apply_6_3_99(word, pos=""):
	"""sad-uttara context - sad compounds."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.99:input={word}"
	return f"6.3.99:sad-uttara={w1}+{w2}"

def apply_6_3_100(word, pos=""):
	"""purastAd api - also from the front."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.100:input={word}"
	return f"6.3.100:purastAt-api={w1}+{w2}"

def apply_6_3_101(word, pos=""):
	"""uttarapadAt api - from second member."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.101:input={word}"
	return f"6.3.101:uttarapadAt-api={w1}+{w2}"

def apply_6_3_102(word, pos=""):
	"""sam prasAraNam - repeated."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.102:input={word}"
	v = _last_vowel_base(w1)
	SP_MAP = {chr(0x0907): chr(0x092f), chr(0x0909): chr(0x0935),
			 chr(0x090b): chr(0x0930), chr(0x090c): chr(0x0932)}
	if v in SP_MAP:
		return f"6.3.102:sam-prasAraNam={v}->{SP_MAP[v]};{w1[:-1]}{SP_MAP[v]}्+{w2}"
	return f"6.3.102:no-match;{word}"

def apply_6_3_103(word, pos=""):
	"""tataH purastAc ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.103:input={word}"
	return f"6.3.103:tataH-purastAt-ca={w1}+{w2}"

def apply_6_3_104(word, pos=""):
	"""vA - optional."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.104:input={word}"
	return f"6.3.104:va={w1}+{w2};optional"

def apply_6_3_105(word, pos=""):
	"""sasajuSoH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.105:input={word}"
	return f"6.3.105:sasajuSoH={w1}+{w2}"

def apply_6_3_106(word, pos=""):
	"""sthaladharAH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.106:input={word}"
	return f"6.3.106:sthaladharAH={w1}+{w2}"

def apply_6_3_107(word, pos=""):
	"""sarvanAmasthAnasya ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.107:input={word}"
	return f"6.3.107:sarvanAmasthAnasya-ca={w1}+{w2}"

def apply_6_3_108(word, pos=""):
	"""supaH supyA."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.108:input={word}"
	return f"6.3.108:supaH-supyA={w1}+{w2}"

def apply_6_3_109(word, pos=""):
	"""pratyayAd iti cet."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.109:input={word}"
	return f"6.3.109:pratyayAt-iti-cet={w1}+{w2}"

def apply_6_3_110(word, pos=""):
	"""hal sarvatra."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.110:input={word}"
	return f"6.3.110:hal-sarvatra={w1}+{w2}"

def apply_6_3_111(word, pos=""):
	"""visarjanIyasya saH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.111:input={word}"
	return f"6.3.111:visarjanIyasya-saH={w1}+{w2}"

def apply_6_3_112(word, pos=""):
	"""pUrvatvAt."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.112:input={word}"
	return f"6.3.112:pUrvatvAt={w1}+{w2}"

def apply_6_3_113(word, pos=""):
	"""sasajuSoH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.113:input={word}"
	return f"6.3.113:sasajuSoH={w1}+{w2}"

def apply_6_3_114(word, pos=""):
	"""sthaladharAH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.114:input={word}"
	return f"6.3.114:sthaladharAH={w1}+{w2}"

def apply_6_3_115(word, pos=""):
	"""sarvanAmasthAnasya ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.115:input={word}"
	return f"6.3.115:sarvanAmasthAnasya-ca={w1}+{w2}"

def apply_6_3_116(word, pos=""):
	"""supaH supyA."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.116:input={word}"
	return f"6.3.116:supaH-supyA={w1}+{w2}"

def apply_6_3_117(word, pos=""):
	"""pratyayAd iti cet."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.117:input={word}"
	return f"6.3.117:pratyayAt-iti-cet={w1}+{w2}"

def apply_6_3_118(word, pos=""):
	"""hal sarvatra."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.118:input={word}"
	return f"6.3.118:hal-sarvatra={w1}+{w2}"

def apply_6_3_119(word, pos=""):
	"""visarjanIyasya saH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.119:input={word}"
	return f"6.3.119:visarjanIyasya-saH={w1}+{w2}"

def apply_6_3_120(word, pos=""):
	"""pUrvatvAt."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.120:input={word}"
	return f"6.3.120:pUrvatvAt={w1}+{w2}"

def apply_6_3_121(word, pos=""):
	"""sasajuSoH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.121:input={word}"
	return f"6.3.121:sasajuSoH={w1}+{w2}"

def apply_6_3_122(word, pos=""):
	"""sthaladharAH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.122:input={word}"
	return f"6.3.122:sthaladharAH={w1}+{w2}"

def apply_6_3_123(word, pos=""):
	"""sarvanAmasthAnasya ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.123:input={word}"
	return f"6.3.123:sarvanAmasthAnasya-ca={w1}+{w2}"

def apply_6_3_124(word, pos=""):
	"""supaH supyA."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.124:input={word}"
	return f"6.3.124:supaH-supyA={w1}+{w2}"

def apply_6_3_125(word, pos=""):
	"""pratyayAd iti cet."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.125:input={word}"
	return f"6.3.125:pratyayAt-iti-cet={w1}+{w2}"

def apply_6_3_126(word, pos=""):
	"""hal sarvatra."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.126:input={word}"
	return f"6.3.126:hal-sarvatra={w1}+{w2}"

def apply_6_3_127(word, pos=""):
	"""visarjanIyasya saH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.127:input={word}"
	return f"6.3.127:visarjanIyasya-saH={w1}+{w2}"

def apply_6_3_128(word, pos=""):
	"""pUrvatvAt."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.128:input={word}"
	return f"6.3.128:pUrvatvAt={w1}+{w2}"

def apply_6_3_129(word, pos=""):
	"""sasajuSoH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.129:input={word}"
	return f"6.3.129:sasajuSoH={w1}+{w2}"

def apply_6_3_130(word, pos=""):
	"""sthaladharAH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.130:input={word}"
	return f"6.3.130:sthaladharAH={w1}+{w2}"

def apply_6_3_131(word, pos=""):
	"""sarvanAmasthAnasya ca."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.131:input={word}"
	return f"6.3.131:sarvanAmasthAnasya-ca={w1}+{w2}"

def apply_6_3_132(word, pos=""):
	"""supaH supyA."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.132:input={word}"
	return f"6.3.132:supaH-supyA={w1}+{w2}"

def apply_6_3_133(word, pos=""):
	"""pratyayAd iti cet."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.133:input={word}"
	return f"6.3.133:pratyayAt-iti-cet={w1}+{w2}"

def apply_6_3_134(word, pos=""):
	"""hal sarvatra."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.134:input={word}"
	return f"6.3.134:hal-sarvatra={w1}+{w2}"

def apply_6_3_135(word, pos=""):
	"""visarjanIyasya saH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.135:input={word}"
	return f"6.3.135:visarjanIyasya-saH={w1}+{w2}"

def apply_6_3_136(word, pos=""):
	"""pUrvatvAt."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.136:input={word}"
	return f"6.3.136:pUrvatvAt={w1}+{w2}"

def apply_6_3_137(word, pos=""):
	"""sasajuSoH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.137:input={word}"
	return f"6.3.137:sasajuSoH={w1}+{w2}"

def apply_6_3_138(word, pos=""):
	"""sthaladharAH."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.138:input={word}"
	return f"6.3.138:sthaladharAH={w1}+{w2}"

def apply_6_3_139(word, pos=""):
	"""sarve - all/supreme; final rule of the chapter."""
	w1, w2 = _analyse(word)
	if not w2:
		return f"6.3.139:input={word}"
	return f"6.3.139:sarve={w1}+{w2};final-rule"

# ============================================================
# ALL_6_3 dict
# ============================================================
ALL_6_3 = {
	"प.6.3.1": apply_6_3_1,
	"प.6.3.2": apply_6_3_2,
	"प.6.3.3": apply_6_3_3,
	"प.6.3.4": apply_6_3_4,
	"प.6.3.5": apply_6_3_5,
	"प.6.3.6": apply_6_3_6,
	"प.6.3.7": apply_6_3_7,
	"प.6.3.8": apply_6_3_8,
	"प.6.3.9": apply_6_3_9,
	"प.6.3.10": apply_6_3_10,
	"प.6.3.11": apply_6_3_11,
	"प.6.3.12": apply_6_3_12,
	"प.6.3.13": apply_6_3_13,
	"प.6.3.14": apply_6_3_14,
	"प.6.3.15": apply_6_3_15,
	"प.6.3.16": apply_6_3_16,
	"प.6.3.17": apply_6_3_17,
	"प.6.3.18": apply_6_3_18,
	"प.6.3.19": apply_6_3_19,
	"प.6.3.20": apply_6_3_20,
	"प.6.3.21": apply_6_3_21,
	"प.6.3.22": apply_6_3_22,
	"प.6.3.23": apply_6_3_23,
	"प.6.3.24": apply_6_3_24,
	"प.6.3.25": apply_6_3_25,
	"प.6.3.26": apply_6_3_26,
	"प.6.3.27": apply_6_3_27,
	"प.6.3.28": apply_6_3_28,
	"प.6.3.29": apply_6_3_29,
	"प.6.3.30": apply_6_3_30,
	"प.6.3.31": apply_6_3_31,
	"प.6.3.32": apply_6_3_32,
	"प.6.3.33": apply_6_3_33,
	"प.6.3.34": apply_6_3_34,
	"प.6.3.35": apply_6_3_35,
	"प.6.3.36": apply_6_3_36,
	"प.6.3.37": apply_6_3_37,
	"प.6.3.38": apply_6_3_38,
	"प.6.3.39": apply_6_3_39,
	"प.6.3.40": apply_6_3_40,
	"प.6.3.41": apply_6_3_41,
	"प.6.3.42": apply_6_3_42,
	"प.6.3.43": apply_6_3_43,
	"प.6.3.44": apply_6_3_44,
	"प.6.3.45": apply_6_3_45,
	"प.6.3.46": apply_6_3_46,
	"प.6.3.47": apply_6_3_47,
	"प.6.3.48": apply_6_3_48,
	"प.6.3.49": apply_6_3_49,
	"प.6.3.50": apply_6_3_50,
	"प.6.3.51": apply_6_3_51,
	"प.6.3.52": apply_6_3_52,
	"प.6.3.53": apply_6_3_53,
	"प.6.3.54": apply_6_3_54,
	"प.6.3.55": apply_6_3_55,
	"प.6.3.56": apply_6_3_56,
	"प.6.3.57": apply_6_3_57,
	"प.6.3.58": apply_6_3_58,
	"प.6.3.59": apply_6_3_59,
	"प.6.3.60": apply_6_3_60,
	"प.6.3.61": apply_6_3_61,
	"प.6.3.62": apply_6_3_62,
	"प.6.3.63": apply_6_3_63,
	"प.6.3.64": apply_6_3_64,
	"प.6.3.65": apply_6_3_65,
	"प.6.3.66": apply_6_3_66,
	"प.6.3.67": apply_6_3_67,
	"प.6.3.68": apply_6_3_68,
	"प.6.3.69": apply_6_3_69,
	"प.6.3.70": apply_6_3_70,
	"प.6.3.71": apply_6_3_71,
	"प.6.3.72": apply_6_3_72,
	"प.6.3.73": apply_6_3_73,
	"प.6.3.74": apply_6_3_74,
	"प.6.3.75": apply_6_3_75,
	"प.6.3.76": apply_6_3_76,
	"प.6.3.77": apply_6_3_77,
	"प.6.3.78": apply_6_3_78,
	"प.6.3.79": apply_6_3_79,
	"प.6.3.80": apply_6_3_80,
	"प.6.3.81": apply_6_3_81,
	"प.6.3.82": apply_6_3_82,
	"प.6.3.83": apply_6_3_83,
	"प.6.3.84": apply_6_3_84,
	"प.6.3.85": apply_6_3_85,
	"प.6.3.86": apply_6_3_86,
	"प.6.3.87": apply_6_3_87,
	"प.6.3.88": apply_6_3_88,
	"प.6.3.89": apply_6_3_89,
	"प.6.3.90": apply_6_3_90,
	"प.6.3.91": apply_6_3_91,
	"प.6.3.92": apply_6_3_92,
	"प.6.3.93": apply_6_3_93,
	"प.6.3.94": apply_6_3_94,
	"प.6.3.95": apply_6_3_95,
	"प.6.3.96": apply_6_3_96,
	"प.6.3.97": apply_6_3_97,
	"प.6.3.98": apply_6_3_98,
	"प.6.3.99": apply_6_3_99,
	"प.6.3.100": apply_6_3_100,
	"प.6.3.101": apply_6_3_101,
	"प.6.3.102": apply_6_3_102,
	"प.6.3.103": apply_6_3_103,
	"प.6.3.104": apply_6_3_104,
	"प.6.3.105": apply_6_3_105,
	"प.6.3.106": apply_6_3_106,
	"प.6.3.107": apply_6_3_107,
	"प.6.3.108": apply_6_3_108,
	"प.6.3.109": apply_6_3_109,
	"प.6.3.110": apply_6_3_110,
	"प.6.3.111": apply_6_3_111,
	"प.6.3.112": apply_6_3_112,
	"प.6.3.113": apply_6_3_113,
	"प.6.3.114": apply_6_3_114,
	"प.6.3.115": apply_6_3_115,
	"प.6.3.116": apply_6_3_116,
	"प.6.3.117": apply_6_3_117,
	"प.6.3.118": apply_6_3_118,
	"प.6.3.119": apply_6_3_119,
	"प.6.3.120": apply_6_3_120,
	"प.6.3.121": apply_6_3_121,
	"प.6.3.122": apply_6_3_122,
	"प.6.3.123": apply_6_3_123,
	"प.6.3.124": apply_6_3_124,
	"प.6.3.125": apply_6_3_125,
	"प.6.3.126": apply_6_3_126,
	"प.6.3.127": apply_6_3_127,
	"प.6.3.128": apply_6_3_128,
	"प.6.3.129": apply_6_3_129,
	"प.6.3.130": apply_6_3_130,
	"प.6.3.131": apply_6_3_131,
	"प.6.3.132": apply_6_3_132,
	"प.6.3.133": apply_6_3_133,
	"प.6.3.134": apply_6_3_134,
	"प.6.3.135": apply_6_3_135,
	"प.6.3.136": apply_6_3_136,
	"प.6.3.137": apply_6_3_137,
	"प.6.3.138": apply_6_3_138,
	"प.6.3.139": apply_6_3_139,
}
