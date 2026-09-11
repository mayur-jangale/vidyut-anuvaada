# Sutra प.3.4.86: एरुः
# vidhiliṅ — optative endings

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.86"
SUTRA_TEXT = "एरुः"
SUTRA_DESC = "vidhiliṅ — optative endings"


class Sutra3486:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

