# Sutra प.8.2.45: ओदितश्च
# (Final transformations (tripāḍī)) — oditaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.45"
SUTRA_TEXT = "ओदितश्च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — oditaSca"


class Sutra8245:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.45: अग्निः'),
		('रामः', '', 'प.8.2.45: रामः'),
		('सीता', '', 'प.8.2.45: सीता'),
	]

