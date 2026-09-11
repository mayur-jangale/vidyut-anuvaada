# Sutra प.8.2.59: भित्तं शकलम्
# (Final transformations (tripāḍī)) — BittaM Sakalam

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.59"
SUTRA_TEXT = "भित्तं शकलम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — BittaM Sakalam"


class Sutra8259:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.59: अग्निः'),
		('रामः', '', 'प.8.2.59: रामः'),
		('सीता', '', 'प.8.2.59: सीता'),
	]

