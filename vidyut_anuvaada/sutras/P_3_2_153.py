# Sutra प.3.2.153: सूददीपदीक्षश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sUdadIpadIkzaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.153"
SUTRA_TEXT = "सूददीपदीक्षश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sUdadIpadIkzaSca"


class Sutra32153:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

