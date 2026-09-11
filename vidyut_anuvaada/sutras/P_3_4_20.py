# Sutra प.3.4.20: परावरयोगे च
# kvasu — absolutive alternative suffix

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.20"
SUTRA_TEXT = "परावरयोगे च"
SUTRA_DESC = "kvasu — absolutive alternative suffix"


class Sutra3420:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

