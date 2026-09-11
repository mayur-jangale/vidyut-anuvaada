# Sutra प.6.4.49: यस्य हलः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.49"
SUTRA_TEXT = "यस्य हलः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6449:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.49: अग्निः'),
		('रामः', '', 'प.6.4.49: रामः'),
		('सीता', '', 'प.6.4.49: सीता'),
	]

