# Sutra प.6.2.57: कतरकतमौ कर्मधारये
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.57"
SUTRA_TEXT = "कतरकतमौ कर्मधारये"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6257:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.57: अग्निः'),
		('रामः', '', 'प.6.2.57: रामः'),
		('सीता', '', 'प.6.2.57: सीता'),
	]

