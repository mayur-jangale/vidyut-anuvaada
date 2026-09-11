# Sutra प.6.1.78: एचोऽयवायावः
# sandhi-sūtra प.6.1.78

from P_6_1 import apply_6_1_78

SUTRA_CODE = "प.6.1.78"
SUTRA_TEXT = "एचोऽयवायावः"
SUTRA_DESC = "sandhi-sūtra प.6.1.78"


class Sutra6178:
	def apply(self, word, pos):
		return apply_6_1_78(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.78:input=अग्निः'),
		('रामः', '', '6.1.78:input=रामः'),
		('सीता', '', '6.1.78:input=सीता'),
	]
