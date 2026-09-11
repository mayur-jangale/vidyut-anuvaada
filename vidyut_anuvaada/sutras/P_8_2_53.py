# Sutra प.8.2.53: क्षायो मः
# (Final transformations (tripāḍī)) — kzAyo maH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.53"
SUTRA_TEXT = "क्षायो मः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — kzAyo maH"


class Sutra8253:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.53: अग्निः'),
		('रामः', '', 'प.8.2.53: रामः'),
		('सीता', '', 'प.8.2.53: सीता'),
	]

