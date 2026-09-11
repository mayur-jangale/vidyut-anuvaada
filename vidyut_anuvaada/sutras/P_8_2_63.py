# Sutra प.8.2.63: नशेर्वा
# (Final transformations (tripāḍī)) — naServA

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.63"
SUTRA_TEXT = "नशेर्वा"
SUTRA_DESC = "(Final transformations (tripāḍī)) — naServA"


class Sutra8263:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.63: अग्निः'),
		('रामः', '', 'प.8.2.63: रामः'),
		('सीता', '', 'प.8.2.63: सीता'),
	]

