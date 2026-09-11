# Sutra प.6.4.95: ह्लादो निष्ठायाम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.95"
SUTRA_TEXT = "ह्लादो निष्ठायाम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6495:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.95: अग्निः'),
		('रामः', '', 'प.6.4.95: रामः'),
		('सीता', '', 'प.6.4.95: सीता'),
	]

