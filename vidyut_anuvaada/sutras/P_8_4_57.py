# Sutra प.8.4.57: अणोऽप्रगृह्यस्यानुनासिकः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.57"
SUTRA_TEXT = "अणोऽप्रगृह्यस्यानुनासिकः"
SUTRA_DESC = "final transformations — continued"


class Sutra8457:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.57: अग्निः'),
		('रामः', '', 'प.8.4.57: रामः'),
		('सीता', '', 'प.8.4.57: सीता'),
	]

