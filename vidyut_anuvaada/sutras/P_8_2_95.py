# Sutra प.8.2.95: आम्रेडितं भर्त्सने
# (Final transformations (tripāḍī)) — AmreqitaM Bartsane

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.95"
SUTRA_TEXT = "आम्रेडितं भर्त्सने"
SUTRA_DESC = "(Final transformations (tripāḍī)) — AmreqitaM Bartsane"


class Sutra8295:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.95: अग्निः'),
		('रामः', '', 'प.8.2.95: रामः'),
		('सीता', '', 'प.8.2.95: सीता'),
	]

