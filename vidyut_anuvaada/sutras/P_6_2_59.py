# Sutra प.6.2.59: राजा च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.59"
SUTRA_TEXT = "राजा च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6259:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.59: अग्निः'),
		('रामः', '', 'प.6.2.59: रामः'),
		('सीता', '', 'प.6.2.59: सीता'),
	]

