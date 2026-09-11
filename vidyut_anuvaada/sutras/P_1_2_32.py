# Sutra प.1.2.32: तस्यादित उदात्तमर्धह्रस्वम्
# (Samjna (technical definitions)) — tasyAdita udAttamarDahrasvam

from P_1_2 import apply_1_2_32

SUTRA_CODE = "प.1.2.32"
SUTRA_TEXT = "तस्यादित उदात्तमर्धह्रस्वम्"
SUTRA_DESC = "(Samjna (technical definitions)) — tasyAdita udAttamarDahrasvam"


class Sutra1232:
	def apply(self, word, pos):
		return apply_1_2_32(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-svarita:अग्निः'),
		('रामः', '', 'non-svarita:रामः'),
		('सीता', '', 'non-svarita:सीता'),
	]

