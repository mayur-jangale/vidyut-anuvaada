# Sutra प.3.3.57: ॠदोरप्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Fdorap

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.57"
SUTRA_TEXT = "ॠदोरप्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Fdorap"


class Sutra3357:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

