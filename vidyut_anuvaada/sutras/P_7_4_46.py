# Sutra प.7.4.46: दो दद् घोः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.46"
SUTRA_TEXT = "दो दद् घोः"
SUTRA_DESC = "taddhita — continued"


class Sutra7446:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.46: अग्निः'),
		('रामः', '', 'प.7.4.46: रामः'),
		('सीता', '', 'प.7.4.46: सीता'),
	]

