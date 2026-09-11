# Sutra प.6.4.105: अतो हेः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.105"
SUTRA_TEXT = "अतो हेः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.105: अग्निः'),
		('रामः', '', 'प.6.4.105: रामः'),
		('सीता', '', 'प.6.4.105: सीता'),
	]

