# Sutra प.3.3.21: इङश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — iNaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.21"
SUTRA_TEXT = "इङश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — iNaSca"


class Sutra3321:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

