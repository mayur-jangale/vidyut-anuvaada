# Sutra प.3.2.84: भूते
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BUte

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.84"
SUTRA_TEXT = "भूते"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BUte"


class Sutra3284:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

