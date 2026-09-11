# Sutra प.6.2.54: ईषदन्यतरस्याम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.54"
SUTRA_TEXT = "ईषदन्यतरस्याम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6254:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.54: अग्निः'),
		('रामः', '', 'प.6.2.54: रामः'),
		('सीता', '', 'प.6.2.54: सीता'),
	]

