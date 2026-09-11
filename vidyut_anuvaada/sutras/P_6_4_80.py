# Sutra प.6.4.80: वाऽम्शसोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.80"
SUTRA_TEXT = "वाऽम्शसोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6480:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.80: अग्निः'),
		('रामः', '', 'प.6.4.80: रामः'),
		('सीता', '', 'प.6.4.80: सीता'),
	]

