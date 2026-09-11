# Sutra प.6.2.125: आदिश्चिहणादीनाम्
# (Sandhi (euphonic combination)) — AdiScihaRAdInAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.125"
SUTRA_TEXT = "आदिश्चिहणादीनाम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — AdiScihaRAdInAm"


class Sutra62125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.125: अग्निः'),
		('रामः', '', 'प.6.2.125: रामः'),
		('सीता', '', 'प.6.2.125: सीता'),
	]

