# Sutra प.7.4.52: ह एति
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.52"
SUTRA_TEXT = "ह एति"
SUTRA_DESC = "taddhita — continued"


class Sutra7452:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.52: अग्निः'),
		('रामः', '', 'प.7.4.52: रामः'),
		('सीता', '', 'प.7.4.52: सीता'),
	]

