# Sutra प.8.4.55: खरि च
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.55"
SUTRA_TEXT = "खरि च"
SUTRA_DESC = "final transformations — continued"


class Sutra8455:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.55: अग्निः'),
		('रामः', '', 'प.8.4.55: रामः'),
		('सीता', '', 'प.8.4.55: सीता'),
	]

