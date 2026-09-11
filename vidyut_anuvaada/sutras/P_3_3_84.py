# Sutra प.3.3.84: परौ घः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — parO GaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.84"
SUTRA_TEXT = "परौ घः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — parO GaH"


class Sutra3384:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

