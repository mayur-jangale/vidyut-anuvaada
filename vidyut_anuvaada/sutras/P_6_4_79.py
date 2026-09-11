# Sutra प.6.4.79: स्त्रियाः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.79"
SUTRA_TEXT = "स्त्रियाः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6479:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.79: अग्निः'),
		('रामः', '', 'प.6.4.79: रामः'),
		('सीता', '', 'प.6.4.79: सीता'),
	]

