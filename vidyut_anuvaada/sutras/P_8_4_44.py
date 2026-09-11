# Sutra प.8.4.44: शात्
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.44"
SUTRA_TEXT = "शात्"
SUTRA_DESC = "final transformations — continued"


class Sutra8444:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.44: अग्निः'),
		('रामः', '', 'प.8.4.44: रामः'),
		('सीता', '', 'प.8.4.44: सीता'),
	]

