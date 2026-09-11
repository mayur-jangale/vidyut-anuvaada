# Sutra प.3.3.125: खनो घ च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Kano Ga ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.125"
SUTRA_TEXT = "खनो घ च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Kano Ga ca"


class Sutra33125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

