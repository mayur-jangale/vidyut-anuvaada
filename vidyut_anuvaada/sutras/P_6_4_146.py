# Sutra प.6.4.146: ओर्गुणः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.146"
SUTRA_TEXT = "ओर्गुणः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.146: अग्निः'),
		('रामः', '', 'प.6.4.146: रामः'),
		('सीता', '', 'प.6.4.146: सीता'),
	]

