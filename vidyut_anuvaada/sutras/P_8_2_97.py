# Sutra प.8.2.97: विचार्यमाणानाम्
# (Final transformations (tripāḍī)) — vicAryamARAnAm

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.97"
SUTRA_TEXT = "विचार्यमाणानाम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — vicAryamARAnAm"


class Sutra8297:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.97: अग्निः'),
		('रामः', '', 'प.8.2.97: रामः'),
		('सीता', '', 'प.8.2.97: सीता'),
	]

