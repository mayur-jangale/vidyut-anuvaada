# Sutra प.3.2.170: क्याच्छन्दसि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kyAcCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.170"
SUTRA_TEXT = "क्याच्छन्दसि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kyAcCandasi"


class Sutra32170:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

