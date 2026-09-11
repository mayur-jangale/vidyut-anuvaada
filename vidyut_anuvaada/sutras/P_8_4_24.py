# Sutra प.8.4.24: अन्तरदेशे
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.24"
SUTRA_TEXT = "अन्तरदेशे"
SUTRA_DESC = "final transformations — continued"


class Sutra8424:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.24: अग्निः'),
		('रामः', '', 'प.8.4.24: रामः'),
		('सीता', '', 'प.8.4.24: सीता'),
	]

