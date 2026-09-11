# Sutra प.6.2.88: मालादीनां च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.88"
SUTRA_TEXT = "मालादीनां च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6288:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.88: अग्निः'),
		('रामः', '', 'प.6.2.88: रामः'),
		('सीता', '', 'प.6.2.88: सीता'),
	]

