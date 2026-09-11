# Sutra प.7.4.90: रीगृदुपधस्य च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.90"
SUTRA_TEXT = "रीगृदुपधस्य च"
SUTRA_DESC = "taddhita — continued"


class Sutra7490:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.90: अग्निः'),
		('रामः', '', 'प.7.4.90: रामः'),
		('सीता', '', 'प.7.4.90: सीता'),
	]

