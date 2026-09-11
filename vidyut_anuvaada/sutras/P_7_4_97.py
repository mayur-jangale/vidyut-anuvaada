# Sutra प.7.4.97: ई च गणः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.97"
SUTRA_TEXT = "ई च गणः"
SUTRA_DESC = "taddhita — continued"


class Sutra7497:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.97: अग्निः'),
		('रामः', '', 'प.7.4.97: रामः'),
		('सीता', '', 'प.7.4.97: सीता'),
	]

