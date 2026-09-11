# Sutra प.6.4.34: शास इदङ्हलोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.34"
SUTRA_TEXT = "शास इदङ्हलोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6434:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.34: अग्निः'),
		('रामः', '', 'प.6.4.34: रामः'),
		('सीता', '', 'प.6.4.34: सीता'),
	]

