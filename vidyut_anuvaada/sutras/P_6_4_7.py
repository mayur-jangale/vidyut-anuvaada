# Sutra प.6.4.7: नोपधायाः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.7"
SUTRA_TEXT = "नोपधायाः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra647:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.7: अग्निः'),
		('रामः', '', 'प.6.4.7: रामः'),
		('सीता', '', 'प.6.4.7: सीता'),
	]

