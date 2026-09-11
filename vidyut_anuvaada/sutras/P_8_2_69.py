# Sutra प.8.2.69: रोऽसुपि
# (Final transformations (tripāḍī)) — ro'supi

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.69"
SUTRA_TEXT = "रोऽसुपि"
SUTRA_DESC = "(Final transformations (tripāḍī)) — ro'supi"


class Sutra8269:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.69: अग्निः'),
		('रामः', '', 'प.8.2.69: रामः'),
		('सीता', '', 'प.8.2.69: सीता'),
	]

