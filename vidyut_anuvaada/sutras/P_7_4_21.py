# Sutra प.7.4.21: शीङः सार्वधातुके गुणः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.21"
SUTRA_TEXT = "शीङः सार्वधातुके गुणः"
SUTRA_DESC = "taddhita — continued"


class Sutra7421:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.21: अग्निः'),
		('रामः', '', 'प.7.4.21: रामः'),
		('सीता', '', 'प.7.4.21: सीता'),
	]

