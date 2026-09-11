# Sutra प.6.2.64: आदिरुदात्तः
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.64"
SUTRA_TEXT = "आदिरुदात्तः"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6264:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.64: अग्निः'),
		('रामः', '', 'प.6.2.64: रामः'),
		('सीता', '', 'प.6.2.64: सीता'),
	]

