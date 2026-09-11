# Sutra प.3.3.104: षिद्भिदादिभ्योऽङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — zidBidAdiByo'N

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.104"
SUTRA_TEXT = "षिद्भिदादिभ्योऽङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — zidBidAdiByo'N"


class Sutra33104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

