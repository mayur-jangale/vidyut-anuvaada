# Sutra प.6.2.5: दायाद्यं दायादे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.5"
SUTRA_TEXT = "दायाद्यं दायादे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra625:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.5: अग्निः'),
		('रामः', '', 'प.6.2.5: रामः'),
		('सीता', '', 'प.6.2.5: सीता'),
	]

