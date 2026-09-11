# Sutra प.3.2.118: लट् स्मे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — law sme

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.118"
SUTRA_TEXT = "लट् स्मे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — law sme"


class Sutra32118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

