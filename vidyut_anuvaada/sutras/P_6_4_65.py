# Sutra प.6.4.65: ईद्यति
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.65"
SUTRA_TEXT = "ईद्यति"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6465:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.65: अग्निः'),
		('रामः', '', 'प.6.4.65: रामः'),
		('सीता', '', 'प.6.4.65: सीता'),
	]

