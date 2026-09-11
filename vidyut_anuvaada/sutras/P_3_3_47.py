# Sutra प.3.3.47: परौ यज्ञे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — parO yajYe

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.47"
SUTRA_TEXT = "परौ यज्ञे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — parO yajYe"


class Sutra3347:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

