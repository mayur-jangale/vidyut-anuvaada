# Sutra प.6.1.84: एकः पूर्वपरयोः
# sandhi-sūtra प.6.1.84

from P_6_1 import apply_6_1_84

SUTRA_CODE = "प.6.1.84"
SUTRA_TEXT = "एकः पूर्वपरयोः"
SUTRA_DESC = "sandhi-sūtra प.6.1.84"


class Sutra6184:
	def apply(self, word, pos):
		return apply_6_1_84(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.84:input=अग्निः'),
		('रामः', '', '6.1.84:input=रामः'),
		('सीता', '', '6.1.84:input=सीता'),
	]
