# Sutra प.6.4.63: दीङो युडचि क्ङिति
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.63"
SUTRA_TEXT = "दीङो युडचि क्ङिति"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6463:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.63: अग्निः'),
		('रामः', '', 'प.6.4.63: रामः'),
		('सीता', '', 'प.6.4.63: सीता'),
	]

