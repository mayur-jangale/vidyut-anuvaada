# Sutra प.3.2.67: जनसनखनक्रमगमो विट्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — janasanaKanakramagamo viw

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.67"
SUTRA_TEXT = "जनसनखनक्रमगमो विट्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — janasanaKanakramagamo viw"


class Sutra3267:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

