# Sutra प.3.3.11: भाववचनाश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BAvavacanASca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.11"
SUTRA_TEXT = "भाववचनाश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BAvavacanASca"


class Sutra3311:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

