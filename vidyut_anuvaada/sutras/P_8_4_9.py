# Sutra प.8.4.9: पानं देशे
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.9"
SUTRA_TEXT = "पानं देशे"
SUTRA_DESC = "final transformations — continued"


class Sutra849:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.9: अग्निः'),
		('रामः', '', 'प.8.4.9: रामः'),
		('सीता', '', 'प.8.4.9: सीता'),
	]

