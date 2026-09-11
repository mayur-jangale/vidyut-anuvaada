# Sutra प.3.2.1: कर्मण्यण्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRyaR

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.1"
SUTRA_TEXT = "कर्मण्यण्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRyaR"


class Sutra321:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

