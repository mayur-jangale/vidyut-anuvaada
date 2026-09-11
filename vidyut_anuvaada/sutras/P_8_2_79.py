# Sutra प.8.2.79: न भकुर्छुराम्
# (Final transformations (tripāḍī)) — na BakurCurAm

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.79"
SUTRA_TEXT = "न भकुर्छुराम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — na BakurCurAm"


class Sutra8279:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.79: अग्निः'),
		('रामः', '', 'प.8.2.79: रामः'),
		('सीता', '', 'प.8.2.79: सीता'),
	]

