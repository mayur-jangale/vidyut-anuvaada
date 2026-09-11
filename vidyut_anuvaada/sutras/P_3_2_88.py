# Sutra प.3.2.88: बहुलं छन्दसि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — bahulaM Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.88"
SUTRA_TEXT = "बहुलं छन्दसि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — bahulaM Candasi"


class Sutra3288:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

