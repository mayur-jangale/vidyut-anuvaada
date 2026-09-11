# Sutra प.3.3.94: स्त्रियां क्तिन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — striyAM ktin

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.94"
SUTRA_TEXT = "स्त्रियां क्तिन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — striyAM ktin"


class Sutra3394:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

