# Sutra प.6.4.85: न भूसुधियोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.85"
SUTRA_TEXT = "न भूसुधियोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6485:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.85: अग्निः'),
		('रामः', '', 'प.6.4.85: रामः'),
		('सीता', '', 'प.6.4.85: सीता'),
	]

