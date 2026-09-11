# Sutra प.8.2.73: तिप्यनस्तेः
# (Final transformations (tripāḍī)) — tipyanasteH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.73"
SUTRA_TEXT = "तिप्यनस्तेः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — tipyanasteH"


class Sutra8273:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.73: अग्निः'),
		('रामः', '', 'प.8.2.73: रामः'),
		('सीता', '', 'प.8.2.73: सीता'),
	]

