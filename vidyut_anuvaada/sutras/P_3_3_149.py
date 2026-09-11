# Sutra प.3.3.149: गर्हायां च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — garhAyAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.149"
SUTRA_TEXT = "गर्हायां च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — garhAyAM ca"


class Sutra33149:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

