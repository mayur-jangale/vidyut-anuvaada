# Sutra प.2.4.69: उपकादिभ्योऽन्यतरस्यामद्वन्द्वे
# (Samasa (compound formation)) — upakAdiByo'nyatarasyAmadvandve

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.69"
SUTRA_TEXT = "उपकादिभ्योऽन्यतरस्यामद्वन्द्वे"
SUTRA_DESC = "(Samasa (compound formation)) — upakAdiByo'nyatarasyAmadvandve"


class Sutra2469:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

