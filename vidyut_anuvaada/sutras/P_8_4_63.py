# Sutra प.8.4.63: शश्छोऽटि
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.63"
SUTRA_TEXT = "शश्छोऽटि"
SUTRA_DESC = "final transformations — continued"


class Sutra8463:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.63: अग्निः'),
		('रामः', '', 'प.8.4.63: रामः'),
		('सीता', '', 'प.8.4.63: सीता'),
	]

