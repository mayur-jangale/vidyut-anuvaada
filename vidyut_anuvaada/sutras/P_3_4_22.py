# Sutra प.3.4.22: आभीक्ष्ण्ये णमुल् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ABIkzRye Ramul ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.22"
SUTRA_TEXT = "आभीक्ष्ण्ये णमुल् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ABIkzRye Ramul ca"


class Sutra3422:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

