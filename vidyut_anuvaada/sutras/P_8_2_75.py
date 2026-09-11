# Sutra प.8.2.75: दश्च
# (Final transformations (tripāḍī)) — daSca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.75"
SUTRA_TEXT = "दश्च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — daSca"


class Sutra8275:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.75: अग्निः'),
		('रामः', '', 'प.8.2.75: रामः'),
		('सीता', '', 'प.8.2.75: सीता'),
	]

