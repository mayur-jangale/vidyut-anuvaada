# Sutra प.8.2.87: ओमभ्यादाने
# (Final transformations (tripāḍī)) — omaByAdAne

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.87"
SUTRA_TEXT = "ओमभ्यादाने"
SUTRA_DESC = "(Final transformations (tripāḍī)) — omaByAdAne"


class Sutra8287:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.87: अग्निः'),
		('रामः', '', 'प.8.2.87: रामः'),
		('सीता', '', 'प.8.2.87: सीता'),
	]

