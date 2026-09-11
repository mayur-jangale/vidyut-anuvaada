# Sutra प.7.4.56: दम्भ इच्च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.56"
SUTRA_TEXT = "दम्भ इच्च"
SUTRA_DESC = "taddhita — continued"


class Sutra7456:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.56: अग्निः'),
		('रामः', '', 'प.7.4.56: रामः'),
		('सीता', '', 'प.7.4.56: सीता'),
	]

