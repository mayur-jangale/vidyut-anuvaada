# Sutra प.8.4.41: ष्टुना ष्टुः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.41"
SUTRA_TEXT = "ष्टुना ष्टुः"
SUTRA_DESC = "final transformations — continued"


class Sutra8441:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.41: अग्निः'),
		('रामः', '', 'प.8.4.41: रामः'),
		('सीता', '', 'प.8.4.41: सीता'),
	]

