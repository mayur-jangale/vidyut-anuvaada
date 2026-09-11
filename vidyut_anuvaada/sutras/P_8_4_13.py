# Sutra प.8.4.13: कुमति च
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.13"
SUTRA_TEXT = "कुमति च"
SUTRA_DESC = "final transformations — continued"


class Sutra8413:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.13: अग्निः'),
		('रामः', '', 'प.8.4.13: रामः'),
		('सीता', '', 'प.8.4.13: सीता'),
	]

