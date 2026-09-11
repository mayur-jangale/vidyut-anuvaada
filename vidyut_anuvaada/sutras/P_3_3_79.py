# Sutra प.3.3.79: अगारैकदेशे प्रघणः प्रघाणश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — agArEkadeSe praGaRaH praGARaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.79"
SUTRA_TEXT = "अगारैकदेशे प्रघणः प्रघाणश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — agArEkadeSe praGaRaH praGARaSca"


class Sutra3379:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

