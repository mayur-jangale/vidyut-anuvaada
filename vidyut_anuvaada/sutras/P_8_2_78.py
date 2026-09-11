# Sutra प.8.2.78: उपधायां च
# (Final transformations (tripāḍī)) — upaDAyAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.78"
SUTRA_TEXT = "उपधायां च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — upaDAyAM ca"


class Sutra8278:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.78: अग्निः'),
		('रामः', '', 'प.8.2.78: रामः'),
		('सीता', '', 'प.8.2.78: सीता'),
	]

