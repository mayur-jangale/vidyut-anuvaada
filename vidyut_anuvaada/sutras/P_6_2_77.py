# Sutra प.6.2.77: संज्ञायां च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.77"
SUTRA_TEXT = "संज्ञायां च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6277:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.77: अग्निः'),
		('रामः', '', 'प.6.2.77: रामः'),
		('सीता', '', 'प.6.2.77: सीता'),
	]

