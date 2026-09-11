# Sutra प.3.3.108: रोगाख्यायां ण्वुल् बहुलम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — rogAKyAyAM Rvul bahulam

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.108"
SUTRA_TEXT = "रोगाख्यायां ण्वुल् बहुलम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — rogAKyAyAM Rvul bahulam"


class Sutra33108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

