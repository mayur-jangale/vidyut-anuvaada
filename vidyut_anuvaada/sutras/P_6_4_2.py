# Sutra प.6.4.2: हलः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.2"
SUTRA_TEXT = "हलः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra642:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.2: अग्निः'),
		('रामः', '', 'प.6.4.2: रामः'),
		('सीता', '', 'प.6.4.2: सीता'),
	]

