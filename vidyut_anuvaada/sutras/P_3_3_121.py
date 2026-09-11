# Sutra प.3.3.121: हलश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — halaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.121"
SUTRA_TEXT = "हलश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — halaSca"


class Sutra33121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

