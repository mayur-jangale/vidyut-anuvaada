# Sutra प.3.2.137: णेश्छन्दसि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ReSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.137"
SUTRA_TEXT = "णेश्छन्दसि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ReSCandasi"


class Sutra32137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

