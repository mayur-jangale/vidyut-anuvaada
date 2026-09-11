# Sutra प.3.2.96: सहे च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sahe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.96"
SUTRA_TEXT = "सहे च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sahe ca"


class Sutra3296:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

