# Sutra प.8.2.94: निगृह्यानुयोगे च
# (Final transformations (tripāḍī)) — nigfhyAnuyoge ca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.94"
SUTRA_TEXT = "निगृह्यानुयोगे च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — nigfhyAnuyoge ca"


class Sutra8294:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.94: अग्निः'),
		('रामः', '', 'प.8.2.94: रामः'),
		('सीता', '', 'प.8.2.94: सीता'),
	]

