# Sutra प.7.4.33: क्यचि च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.33"
SUTRA_TEXT = "क्यचि च"
SUTRA_DESC = "taddhita — continued"


class Sutra7433:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.33: अग्निः'),
		('रामः', '', 'प.7.4.33: रामः'),
		('सीता', '', 'प.7.4.33: सीता'),
	]

