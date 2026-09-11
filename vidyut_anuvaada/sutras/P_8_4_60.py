# Sutra प.8.4.60: तोर्लि
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.60"
SUTRA_TEXT = "तोर्लि"
SUTRA_DESC = "final transformations — continued"


class Sutra8460:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.60: अग्निः'),
		('रामः', '', 'प.8.4.60: रामः'),
		('सीता', '', 'प.8.4.60: सीता'),
	]

