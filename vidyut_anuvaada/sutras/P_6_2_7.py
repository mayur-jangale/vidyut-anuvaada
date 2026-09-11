# Sutra प.6.2.7: पदेऽपदेशे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.7"
SUTRA_TEXT = "पदेऽपदेशे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra627:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.7: अग्निः'),
		('रामः', '', 'प.6.2.7: रामः'),
		('सीता', '', 'प.6.2.7: सीता'),
	]

