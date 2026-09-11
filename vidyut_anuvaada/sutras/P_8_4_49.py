# Sutra प.8.4.49: शरोऽचि
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.49"
SUTRA_TEXT = "शरोऽचि"
SUTRA_DESC = "final transformations — continued"


class Sutra8449:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.49: अग्निः'),
		('रामः', '', 'प.8.4.49: रामः'),
		('सीता', '', 'प.8.4.49: सीता'),
	]

