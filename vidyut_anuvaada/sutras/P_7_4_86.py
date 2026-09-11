# Sutra प.7.4.86: जपजभदहदशभञ्जपशां च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.86"
SUTRA_TEXT = "जपजभदहदशभञ्जपशां च"
SUTRA_DESC = "taddhita — continued"


class Sutra7486:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.86: अग्निः'),
		('रामः', '', 'प.7.4.86: रामः'),
		('सीता', '', 'प.7.4.86: सीता'),
	]

