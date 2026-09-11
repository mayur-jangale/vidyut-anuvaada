# Sutra प.3.3.14: लृटः सद् वा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — lfwaH sad vA

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.14"
SUTRA_TEXT = "लृटः सद् वा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — lfwaH sad vA"


class Sutra3314:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

