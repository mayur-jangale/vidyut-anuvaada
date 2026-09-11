# Sutra प.8.4.25: अयनं च
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.25"
SUTRA_TEXT = "अयनं च"
SUTRA_DESC = "final transformations — continued"


class Sutra8425:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.25: अग्निः'),
		('रामः', '', 'प.8.4.25: रामः'),
		('सीता', '', 'प.8.4.25: सीता'),
	]

