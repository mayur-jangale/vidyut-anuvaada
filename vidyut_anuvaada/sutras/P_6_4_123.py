# Sutra प.6.4.123: राधो हिंसायाम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.123"
SUTRA_TEXT = "राधो हिंसायाम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.123: अग्निः'),
		('रामः', '', 'प.6.4.123: रामः'),
		('सीता', '', 'प.6.4.123: सीता'),
	]

