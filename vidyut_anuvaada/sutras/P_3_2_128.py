# Sutra प.3.2.128: पूङ्यजोः शानन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pUNyajoH SAnan

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.128"
SUTRA_TEXT = "पूङ्यजोः शानन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pUNyajoH SAnan"


class Sutra32128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

