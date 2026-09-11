# Sutra प.8.4.54: अभ्यासे चर्च
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.54"
SUTRA_TEXT = "अभ्यासे चर्च"
SUTRA_DESC = "final transformations — continued"


class Sutra8454:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.54: अग्निः'),
		('रामः', '', 'प.8.4.54: रामः'),
		('सीता', '', 'प.8.4.54: सीता'),
	]

