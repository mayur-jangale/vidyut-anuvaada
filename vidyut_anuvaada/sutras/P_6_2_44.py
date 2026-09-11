# Sutra प.6.2.44: अर्थे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.44"
SUTRA_TEXT = "अर्थे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6244:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.44: अग्निः'),
		('रामः', '', 'प.6.2.44: रामः'),
		('सीता', '', 'प.6.2.44: सीता'),
	]

