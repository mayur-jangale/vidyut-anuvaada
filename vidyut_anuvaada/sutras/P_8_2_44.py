# Sutra प.8.2.44: ल्वादिभ्यः
# (Final transformations (tripāḍī)) — lvAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.44"
SUTRA_TEXT = "ल्वादिभ्यः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — lvAdiByaH"


class Sutra8244:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.44: अग्निः'),
		('रामः', '', 'प.8.2.44: रामः'),
		('सीता', '', 'प.8.2.44: सीता'),
	]

