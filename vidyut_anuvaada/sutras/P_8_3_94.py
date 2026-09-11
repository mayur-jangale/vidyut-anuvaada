# Sutra प.8.3.94: छन्दोनाम्नि च
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.94"
SUTRA_TEXT = "छन्दोनाम्नि च"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8394:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.94: अग्निः'),
		('रामः', '', 'प.8.3.94: रामः'),
		('सीता', '', 'प.8.3.94: सीता'),
	]

