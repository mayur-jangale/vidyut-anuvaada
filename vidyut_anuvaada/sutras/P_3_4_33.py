# Sutra प.3.4.33: चेले क्नोपेः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — cele knopeH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.33"
SUTRA_TEXT = "चेले क्नोपेः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — cele knopeH"


class Sutra3433:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

