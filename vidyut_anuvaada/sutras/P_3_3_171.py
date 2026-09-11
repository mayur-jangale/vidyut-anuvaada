# Sutra प.3.3.171: कृत्याश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kftyASca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.171"
SUTRA_TEXT = "कृत्याश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kftyASca"


class Sutra33171:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

