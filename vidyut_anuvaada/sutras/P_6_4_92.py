# Sutra प.6.4.92: मितां ह्रस्वः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.92"
SUTRA_TEXT = "मितां ह्रस्वः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6492:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.92: अग्निः'),
		('रामः', '', 'प.6.4.92: रामः'),
		('सीता', '', 'प.6.4.92: सीता'),
	]

