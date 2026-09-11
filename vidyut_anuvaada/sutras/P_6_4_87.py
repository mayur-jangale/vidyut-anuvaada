# Sutra प.6.4.87: हुश्नुवोः सार्वधातुके
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.87"
SUTRA_TEXT = "हुश्नुवोः सार्वधातुके"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6487:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.87: अग्निः'),
		('रामः', '', 'प.6.4.87: रामः'),
		('सीता', '', 'प.6.4.87: सीता'),
	]

