# Sutra प.6.4.48: अतो लोपः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.48"
SUTRA_TEXT = "अतो लोपः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6448:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.48: अग्निः'),
		('रामः', '', 'प.6.4.48: रामः'),
		('सीता', '', 'प.6.4.48: सीता'),
	]

