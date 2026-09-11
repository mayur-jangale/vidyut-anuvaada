# Sutra प.8.4.34: न भाभूपूकमिगमिप्यायीवेपाम्
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.34"
SUTRA_TEXT = "न भाभूपूकमिगमिप्यायीवेपाम्"
SUTRA_DESC = "final transformations — continued"


class Sutra8434:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.34: अग्निः'),
		('रामः', '', 'प.8.4.34: रामः'),
		('सीता', '', 'प.8.4.34: सीता'),
	]

