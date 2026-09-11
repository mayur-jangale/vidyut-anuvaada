# Sutra प.3.2.138: भुवश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BuvaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.138"
SUTRA_TEXT = "भुवश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BuvaSca"


class Sutra32138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

