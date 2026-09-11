# Sutra प.8.2.51: शुषः कः
# (Final transformations (tripāḍī)) — SuzaH kaH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.51"
SUTRA_TEXT = "शुषः कः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — SuzaH kaH"


class Sutra8251:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.51: अग्निः'),
		('रामः', '', 'प.8.2.51: रामः'),
		('सीता', '', 'प.8.2.51: सीता'),
	]

