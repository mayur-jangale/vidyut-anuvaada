# Sutra प.8.2.89: प्रणवष्टेः
# (Final transformations (tripāḍī)) — praRavazweH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.89"
SUTRA_TEXT = "प्रणवष्टेः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — praRavazweH"


class Sutra8289:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.89: अग्निः'),
		('रामः', '', 'प.8.2.89: रामः'),
		('सीता', '', 'प.8.2.89: सीता'),
	]

