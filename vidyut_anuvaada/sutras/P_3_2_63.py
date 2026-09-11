# Sutra प.3.2.63: छन्दसि सहः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Candasi sahaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.63"
SUTRA_TEXT = "छन्दसि सहः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Candasi sahaH"


class Sutra3263:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

