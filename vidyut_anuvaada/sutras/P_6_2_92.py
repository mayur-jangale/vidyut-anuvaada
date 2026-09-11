# Sutra प.6.2.92: अन्तः
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.92"
SUTRA_TEXT = "अन्तः"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6292:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.92: अग्निः'),
		('रामः', '', 'प.6.2.92: रामः'),
		('सीता', '', 'प.6.2.92: सीता'),
	]

