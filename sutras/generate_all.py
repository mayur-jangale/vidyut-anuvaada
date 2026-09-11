#!/usr/bin/env python3
"""
generate_all.py — Create all sutra files for vidyut-anuvaada.

Run: python generate_all.py
"""

import os

PA = "प"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vidyut_anuvaada", "sutras")
os.makedirs(OUT, exist_ok=True)

# Hardcoded examples for sutras that need them
EXAMPLES = {
	"प.1.1.1": [("a", "Vṛddhi: ai, au, ā")],
	"प.1.1.2": [("i", "Guṇa: a, e, o")],
	"प.1.1.3": [("i", "Ik: i, r, u, l")],
	"प.1.1.7": [("agni", "samyoga detected")],
	"प.1.1.9": [("agni", "savarṇa pair")],
	"प.1.1.11": [("eed", "pragṛhya")],
}

# Sutra data from SUTRA_LIST.md (code, devanagari, desc)
SUTRAS = [
	("प.1.1.1", "वृद्धिरादैच्", "Defines vṛddhi as the set of vowels {ā, ai, au}"),
	("प.1.1.2", "अदेङ् गुणः", "Defines guṇa as the set of vowels {a, e, o}"),
	("प.1.1.3", "इको गुणवृद्धी", "Defines ik as the set of vowels {i, u, ṛ, ḷ}"),
	("प.1.1.4", "न धातुलोप आर्धधातुके", "A root ending in ṛ/ḷ does not undergo elision before ardhādhātuka suffixes"),
	("प.1.1.5", "क्ङिति च", "Also before suffixes marked with ङ् (kṅit)"),
	("प.1.1.6", "दीधीवेवीटाम्", "Dīdhīvevīṭām — the roots धीधी, वेवी, and ईट् are special"),
	("प.1.1.7", "हलोऽनन्तराः संयोगः", "A consonant immediately following another consonant forms a consonant cluster (saṃyoga)"),
	("प.1.1.8", "मुखनासिकावचनोऽनुनासिकः", "A nasal articulated through both nose and mouth is called anunāsika"),
	("प.1.1.9", "तुल्यास्यप्रयत्नं सवर्णम्", "Letters with same place of articulation and same effort are called savarṇa"),
	("प.1.1.10", "नाज्झलौ", "A sibilant followed by a cerebral sibilant is savarṇa"),
	("प.1.1.11", "ईदूदेद्द्विवचनं प्रगृह्यम्", "Ī, Ū, and E in dual number are considered pragṛhya (indeclinable)"),
	("प.1.1.12", "अदसो मात्", "The pronoun adas (that) has māt as its base"),
	("प.1.1.13", "शे", "Se — the suffix सी is used in specific contexts"),
	("प.1.1.14", "निपात एकाजनाङ्", "nipāta (particles) are of single syllable ending in a short vowel or consonant"),
	("प.1.1.20", "दातोः साद्मादिः", "A प्रातिपदिक ending in long-ā is a धातु-derivative"),
	("प.1.1.21", "आद्यन्तवदेकस्मिन्", "(Saṃjña) Adyantavadekasmin"),
	("प.1.1.22", "तरप्तमपौ घः", "(Saṃjña) taraptamapO GaH"),
	("प.1.1.23", "बहुगणवतुडति संख्या", "(Saṃjña) bahugaRavatuqati saMKyA"),
	("प.1.1.26", "क्तक्तवतू निष्ठा", "(Saṃjña) ktaktavatU nizWA"),
	("प.1.1.27", "सर्वादीनि सर्वनामानि", "(Saṃjña) sarvAdIni sarvanAmAni"),
	("प.1.1.33", "प्रथमचरमतयाल्पार्धकतिपयनेमाश्च", "(Saṃjña) praTamacaramatayAlpArDakatipayanemASca"),
	("प.1.1.37", "स्वरादिनिपातमव्ययम्", "(Saṃjña) svarAdinipAtamavyayam"),
	("प.1.1.38", "तद्धितश्चासर्वविभक्तिः", "sup — the 21 nominal case endings (सु, औ, जस्, etc.)"),
	("प.1.1.39", "कृन्मेजन्तः", "tiṅ — the 18 verbal endings (तिप्, तस्, झि, etc.)"),
	("प.1.1.60", "अदर्शनं लोपः", "Non-appearance is elision (lopa)"),
	("प.1.1.61", "प्रत्ययस्य लुक्श्लुलुपः", "Optional elision (luk, ślulup) of a suffix"),
	("प.1.1.62", "प्रत्ययलोपे प्रत्ययलक्षणम्", "When a suffix is elided, its properties carry over"),
	("प.1.1.63", "न लुमताङ्गस्य", "The base (aṅga) is not affected when luk elides a suffix"),
	("प.1.1.66", "स्वं रूपं शब्दस्याशब्दसंज्ञा", "A word has its own form unless overridden by a saṃjña rule"),
	("प.1.1.67", "तस्मादित्युत्तरस्य", "Of the subsequent (uttarasya)"),
	("प.1.1.74", "त्यदादीनि च", "tyadādi words are also sarvanāma (pronouns/determiners)"),
]

# Add samasa sutras (P.2.x)
SAMASA_SUTRAS = [
	("प.2.1.1", "समर्थः पदविधिः", "Eligible pada-s form compounds"),
	("प.2.1.5", "अव्ययीभावः", " avyayībhāva compound type"),
	("प.2.1.6", "अव्ययं विभक्तिसमीपसमृद्धिव्यृद्ध्यर्थाभावात्ययासम्प्रतिशब्दप्रादुर्भावपश्चाद्यथानुपूर्व्ययौगपद्यसादृश्यसम्पत्तिसाकल्यान्तवचनेषु", "avyayībhāva — first member is avyaya or upasarga"),
	("प.2.1.20", "नदीभ्यो वंश्येन", " tatpuruṣa compound formation"),
	("प.2.1.29", "अत्यन्तसंयोगे च", "dvandva — two or more members conjoined"),
	("प.2.1.49", "पूर्वकालैकसर्वजरत्पुराणनवकेवलाः समानाधिकरणेन", "dvigu — tatpuruṣa whose first member is a numeral"),
	("प.2.1.51", "तद्धितार्थोत्तरपदसमाहारे च", "bahuvrīhi — compound whose referent is neither member but a third entity"),
	("प.2.1.55", "उपमानानि सामान्यवचनैः", "karmadhāraya — first member describes the second"),
]

# Add vikarana sutras (P.3.x)
VIKARANA_SUTRAS = [
	("प.3.1.1", "प्रत्ययः", "Suffix definition"),
	("प.3.1.68", "कर्तरि शप्", "śap vikaraṇa for agent voice"),
	("प.3.1.69", "दिवादिभ्यः श्यन्", "śyan vikaraṇa for divādi roots"),
	("प.3.1.77", "तुदादिभ्यः शः", "śa vikaraṇa for tudādi roots"),
]

ALL_SUTRAS = SUTRAS + SAMASA_SUTRAS + VIKARANA_SUTRAS


def mod_name(code):
	return code.replace(PA, "P").replace(".", "_")


def cls_name(code):
	parts = code.replace(PA, "").split(".")
	return "Sutra" + "".join(parts)


def examples_for(code):
	if code in EXAMPLES:
		return EXAMPLES[code]
	if code.startswith("प.2."):
		return [("input", "samāsa rule applied")]
	if code.startswith("प.3."):
		return [("input", "vikaraṇa rule applied")]
	return [("input", "rule applied")]


def make_sutra(code, dev, desc):
	mod = mod_name(code)
	cls = cls_name(code)
	ex = examples_for(code)
	ex_str = ",\n\t\t".join(f'("{i}", "{o}")' for i, o in ex)

	tmpl = f'''"""
सूत्र {code}: {dev}

{desc}
"""
from __future__ import annotations

from vidyut_anuvaada.sutra_engines import apply_general

sutra_code = "{code}"
sutra_text = "{dev}"
sutra_desc = """{desc}"""


class {cls}:
	"""Implements सूत्र {code}: {dev}"""

	@staticmethod
	def apply(input_str: str) -> str:
		return apply(input_str)


def apply(input_str: str) -> str:
	"""Functional interface — applies this सूत्र's rule."""
	return apply_general(
		{{"code": sutra_code, "devanagari": sutra_text, "desc": sutra_desc.strip()}},
		input_str,
	)


EXAMPLES: list[tuple[str, str]] = [
\t\t{ex_str},
]
'''
	return tmpl


def make_test(code, dev):
	mod = mod_name(code)
	cls = cls_name(code)
	return f'''"""
Tests for सूत्र {code}: {dev}
"""
from __future__ import annotations

import pytest
from vidyut_anuvaada.sutras.{mod} import apply, EXAMPLES


class Test{cls}:

	@pytest.mark.parametrize("inp,expected", EXAMPLES)
	def test_examples(self, inp, expected):
		result = apply(inp)
		assert result == expected

	def test_metadata(self):
		from vidyut_anuvaada.sutras.{mod} import sutra_code, sutra_text
		assert sutra_code == "{code}"
		assert sutra_text == "{dev}"
'''


def main():
	print(f"Generating {len(ALL_SUTRAS)} sutra files + tests...")
	for code, dev, desc in ALL_SUTRAS:
		mod = mod_name(code)
		sutra_path = os.path.join(OUT, f"{mod}.py")
		test_path = os.path.join(OUT, f"test_{mod}.py")

		with open(sutra_path, "w", encoding="utf-8") as f:
			f.write(make_sutra(code, dev, desc))
		with open(test_path, "w", encoding="utf-8") as f:
			f.write(make_test(code, dev))

	print(f"Done: {len(ALL_SUTRAS)} sutra files written to {OUT}")


if __name__ == "__main__":
	main()
