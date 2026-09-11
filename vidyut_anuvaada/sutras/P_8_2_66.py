# Sutra प.8.2.66: ससजुषो रुः
# (Final transformations (tripāḍī)) — sasajuzo ruH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.66"
SUTRA_TEXT = "ससजुषो रुः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — sasajuzo ruH"


class Sutra8266:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.66: अग्निः'),
		('रामः', '', 'प.8.2.66: रामः'),
		('सीता', '', 'प.8.2.66: सीता'),
	]

