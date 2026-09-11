# Sutra प.8.4.53: झलां जश् झशि
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.53"
SUTRA_TEXT = "झलां जश् झशि"
SUTRA_DESC = "final transformations — continued"


class Sutra8453:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.53: अग्निः'),
		('रामः', '', 'प.8.4.53: रामः'),
		('सीता', '', 'प.8.4.53: सीता'),
	]

