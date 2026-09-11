# Sutra प.3.2.106: लिटः कानज्वा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — liwaH kAnajvA

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.106"
SUTRA_TEXT = "लिटः कानज्वा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — liwaH kAnajvA"


class Sutra32106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

