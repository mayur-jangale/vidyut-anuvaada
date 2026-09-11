# Sutra प.7.4.22: अयङ् यि क्ङिति
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.22"
SUTRA_TEXT = "अयङ् यि क्ङिति"
SUTRA_DESC = "taddhita — continued"


class Sutra7422:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.22: अग्निः'),
		('रामः', '', 'प.7.4.22: रामः'),
		('सीता', '', 'प.7.4.22: सीता'),
	]

