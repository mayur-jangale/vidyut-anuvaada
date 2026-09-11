# Sutra प.3.2.76: क्विप् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kvip ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.76"
SUTRA_TEXT = "क्विप् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kvip ca"


class Sutra3276:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

