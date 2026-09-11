# Sutra प.8.2.83: प्रत्यभिवादेऽशूद्रे
# (Final transformations (tripāḍī)) — pratyaBivAde'SUdre

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.83"
SUTRA_TEXT = "प्रत्यभिवादेऽशूद्रे"
SUTRA_DESC = "(Final transformations (tripāḍī)) — pratyaBivAde'SUdre"


class Sutra8283:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.83: अग्निः'),
		('रामः', '', 'प.8.2.83: रामः'),
		('सीता', '', 'प.8.2.83: सीता'),
	]

