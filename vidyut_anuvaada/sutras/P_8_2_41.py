# Sutra प.8.2.41: षढोः कः सि
# (Final transformations (tripāḍī)) — zaQoH kaH si

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.41"
SUTRA_TEXT = "षढोः कः सि"
SUTRA_DESC = "(Final transformations (tripāḍī)) — zaQoH kaH si"


class Sutra8241:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.41: अग्निः'),
		('रामः', '', 'प.8.2.41: रामः'),
		('सीता', '', 'प.8.2.41: सीता'),
	]

