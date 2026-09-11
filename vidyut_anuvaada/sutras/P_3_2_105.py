# Sutra प.3.2.105: छन्दसि लिट्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Candasi liw

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.105"
SUTRA_TEXT = "छन्दसि लिट्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Candasi liw"


class Sutra32105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

