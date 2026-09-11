# Sutra प.8.4.23: वमोर्वा
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.23"
SUTRA_TEXT = "वमोर्वा"
SUTRA_DESC = "final transformations — continued"


class Sutra8423:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.23: अग्निः'),
		('रामः', '', 'प.8.4.23: रामः'),
		('सीता', '', 'प.8.4.23: सीता'),
	]

