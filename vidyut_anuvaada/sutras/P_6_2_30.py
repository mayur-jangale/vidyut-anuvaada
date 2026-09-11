# Sutra प.6.2.30: बह्वन्यतरस्याम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.30"
SUTRA_TEXT = "बह्वन्यतरस्याम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6230:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.30: अग्निः'),
		('रामः', '', 'प.6.2.30: रामः'),
		('सीता', '', 'प.6.2.30: सीता'),
	]

