# Sutra प.7.4.66: उरत्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.66"
SUTRA_TEXT = "उरत्"
SUTRA_DESC = "taddhita — continued"


class Sutra7466:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.66: अग्निः'),
		('रामः', '', 'प.7.4.66: रामः'),
		('सीता', '', 'प.7.4.66: सीता'),
	]

