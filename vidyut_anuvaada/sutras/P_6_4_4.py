# Sutra प.6.4.4: न तिसृचतसृ
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.4"
SUTRA_TEXT = "न तिसृचतसृ"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra644:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.4: अग्निः'),
		('रामः', '', 'प.6.4.4: रामः'),
		('सीता', '', 'प.6.4.4: सीता'),
	]

