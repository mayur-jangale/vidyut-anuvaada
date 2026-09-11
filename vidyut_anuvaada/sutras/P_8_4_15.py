# Sutra प.8.4.15: हिनुमीना
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.15"
SUTRA_TEXT = "हिनुमीना"
SUTRA_DESC = "final transformations — continued"


class Sutra8415:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.15: अग्निः'),
		('रामः', '', 'प.8.4.15: रामः'),
		('सीता', '', 'प.8.4.15: सीता'),
	]

