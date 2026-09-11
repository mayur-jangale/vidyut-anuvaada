# Sutra प.1.2.10: हलन्ताच्च
# (Samjna (technical definitions)) — halantAcca

from P_1_2 import apply_1_2_10

SUTRA_CODE = "प.1.2.10"
SUTRA_TEXT = "हलन्ताच्च"
SUTRA_DESC = "(Samjna (technical definitions)) — halantAcca"


class Sutra1210:
	def apply(self, word, pos):
		return apply_1_2_10(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-halanta:अग्निः'),
		('रामः', '', 'no-halanta:रामः'),
		('सीता', '', 'no-halanta:सीता'),
	]

