# Sutra प.3.3.101: इच्छा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — icCA

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.101"
SUTRA_TEXT = "इच्छा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — icCA"


class Sutra33101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

