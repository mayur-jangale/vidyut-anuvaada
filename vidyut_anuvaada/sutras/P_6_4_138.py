# Sutra प.6.4.138: अचः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.138"
SUTRA_TEXT = "अचः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.138: अग्निः'),
		('रामः', '', 'प.6.4.138: रामः'),
		('सीता', '', 'प.6.4.138: सीता'),
	]

