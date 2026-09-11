# Sutra प.3.2.144: अपे च लषः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ape ca lazaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.144"
SUTRA_TEXT = "अपे च लषः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ape ca lazaH"


class Sutra32144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

