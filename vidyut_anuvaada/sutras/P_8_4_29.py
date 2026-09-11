# Sutra प.8.4.29: कृत्यचः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.29"
SUTRA_TEXT = "कृत्यचः"
SUTRA_DESC = "final transformations — continued"


class Sutra8429:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.29: अग्निः'),
		('रामः', '', 'प.8.4.29: रामः'),
		('सीता', '', 'प.8.4.29: सीता'),
	]

