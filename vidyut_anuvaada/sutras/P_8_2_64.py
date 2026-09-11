# Sutra प.8.2.64: मो नो धातोः
# (Final transformations (tripāḍī)) — mo no DAtoH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.64"
SUTRA_TEXT = "मो नो धातोः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — mo no DAtoH"


class Sutra8264:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.64: अग्निः'),
		('रामः', '', 'प.8.2.64: रामः'),
		('सीता', '', 'प.8.2.64: सीता'),
	]

