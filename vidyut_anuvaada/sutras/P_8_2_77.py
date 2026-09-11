# Sutra प.8.2.77: हलि च
# (Final transformations (tripāḍī)) — hali ca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.77"
SUTRA_TEXT = "हलि च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — hali ca"


class Sutra8277:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.77: अग्निः'),
		('रामः', '', 'प.8.2.77: रामः'),
		('सीता', '', 'प.8.2.77: सीता'),
	]

