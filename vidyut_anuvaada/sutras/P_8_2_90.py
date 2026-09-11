# Sutra प.8.2.90: याज्याऽन्तः
# (Final transformations (tripāḍī)) — yAjyA'ntaH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.90"
SUTRA_TEXT = "याज्याऽन्तः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — yAjyA'ntaH"


class Sutra8290:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.90: अग्निः'),
		('रामः', '', 'प.8.2.90: रामः'),
		('सीता', '', 'प.8.2.90: सीता'),
	]

