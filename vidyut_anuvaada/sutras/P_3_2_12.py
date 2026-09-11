# Sutra प.3.2.12: अर्हः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — arhaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.12"
SUTRA_TEXT = "अर्हः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — arhaH"


class Sutra3212:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

