# Sutra प.1.2.51: लुपि युक्तवद्व्यक्तिवचने
# (Samjna (technical definitions)) — lupi yuktavadvyaktivacane

from P_1_2 import apply_1_2_51

SUTRA_CODE = "प.1.2.51"
SUTRA_TEXT = "लुपि युक्तवद्व्यक्तिवचने"
SUTRA_DESC = "(Samjna (technical definitions)) — lupi yuktavadvyaktivacane"


class Sutra1251:
	def apply(self, word, pos):
		return apply_1_2_51(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-lup:अग्निः'),
		('रामः', '', 'non-lup:रामः'),
		('सीता', '', 'non-lup:सीता'),
	]

