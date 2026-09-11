# Sutra प.3.3.91: स्वपो नन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — svapo nan

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.91"
SUTRA_TEXT = "स्वपो नन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — svapo nan"


class Sutra3391:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

