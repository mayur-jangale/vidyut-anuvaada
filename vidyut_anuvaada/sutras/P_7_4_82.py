# Sutra प.7.4.82: गुणो यङ्लुकोः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.82"
SUTRA_TEXT = "गुणो यङ्लुकोः"
SUTRA_DESC = "taddhita — continued"


class Sutra7482:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.82: अग्निः'),
		('रामः', '', 'प.7.4.82: रामः'),
		('सीता', '', 'प.7.4.82: सीता'),
	]

