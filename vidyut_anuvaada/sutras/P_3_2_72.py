# Sutra प.3.2.72: अवे यजः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ave yajaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.72"
SUTRA_TEXT = "अवे यजः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ave yajaH"


class Sutra3272:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

