# Sutra प.7.4.49: सः स्यार्द्धधातुके
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.49"
SUTRA_TEXT = "सः स्यार्द्धधातुके"
SUTRA_DESC = "taddhita — continued"


class Sutra7449:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.49: अग्निः'),
		('रामः', '', 'प.7.4.49: रामः'),
		('सीता', '', 'प.7.4.49: सीता'),
	]

