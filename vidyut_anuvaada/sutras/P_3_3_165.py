# Sutra प.3.3.165: स्मे लोट्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sme low

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.165"
SUTRA_TEXT = "स्मे लोट्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sme low"


class Sutra33165:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

