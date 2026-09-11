# Sutra प.2.4.68: तिककितवादिभ्यो द्वन्द्वे
# (Samasa (compound formation)) — tikakitavAdiByo dvandve

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.68"
SUTRA_TEXT = "तिककितवादिभ्यो द्वन्द्वे"
SUTRA_DESC = "(Samasa (compound formation)) — tikakitavAdiByo dvandve"


class Sutra2468:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

