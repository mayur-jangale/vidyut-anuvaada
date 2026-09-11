# Sutra प.8.2.84: दूराद्धूते च
# (Final transformations (tripāḍī)) — dUrAdDUte ca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.84"
SUTRA_TEXT = "दूराद्धूते च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — dUrAdDUte ca"


class Sutra8284:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.84: अग्निः'),
		('रामः', '', 'प.8.2.84: रामः'),
		('सीता', '', 'प.8.2.84: सीता'),
	]

