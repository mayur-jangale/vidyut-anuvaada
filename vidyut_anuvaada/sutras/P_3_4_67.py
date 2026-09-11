# Sutra प.3.4.67: कर्तरि कृत्
# aṇ — action noun suffix (gamana-type)

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.67"
SUTRA_TEXT = "कर्तरि कृत्"
SUTRA_DESC = "aṇ — action noun suffix (gamana-type)"


class Sutra3467:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

