# Sutra प.6.2.28: पूगेष्वन्यतरस्याम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.28"
SUTRA_TEXT = "पूगेष्वन्यतरस्याम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6228:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.28: अग्निः'),
		('रामः', '', 'प.6.2.28: रामः'),
		('सीता', '', 'प.6.2.28: सीता'),
	]

