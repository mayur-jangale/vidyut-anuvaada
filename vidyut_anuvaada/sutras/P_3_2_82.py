# Sutra प.3.2.82: मनः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — manaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.82"
SUTRA_TEXT = "मनः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — manaH"


class Sutra3282:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

