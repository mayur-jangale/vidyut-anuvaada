# Sutra प.6.4.53: जनिता मन्त्रे
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.53"
SUTRA_TEXT = "जनिता मन्त्रे"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6453:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.53: अग्निः'),
		('रामः', '', 'प.6.4.53: रामः'),
		('सीता', '', 'प.6.4.53: सीता'),
	]

