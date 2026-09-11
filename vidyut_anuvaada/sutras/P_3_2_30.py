# Sutra प.3.2.30: नाडीमुष्ट्योश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nAqImuzwyoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.30"
SUTRA_TEXT = "नाडीमुष्ट्योश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nAqImuzwyoSca"


class Sutra3230:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

