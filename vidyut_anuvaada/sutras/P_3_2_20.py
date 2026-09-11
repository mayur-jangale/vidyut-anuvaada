# Sutra प.3.2.20: कृञो हेतुताच्छील्यानुलोम्येषु
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kfYo hetutAcCIlyAnulomyezu

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.20"
SUTRA_TEXT = "कृञो हेतुताच्छील्यानुलोम्येषु"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kfYo hetutAcCIlyAnulomyezu"


class Sutra3220:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

