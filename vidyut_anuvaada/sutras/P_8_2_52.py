# Sutra प.8.2.52: पचो वः
# (Final transformations (tripāḍī)) — paco vaH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.52"
SUTRA_TEXT = "पचो वः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — paco vaH"


class Sutra8252:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.52: अग्निः'),
		('रामः', '', 'प.8.2.52: रामः'),
		('सीता', '', 'प.8.2.52: सीता'),
	]

