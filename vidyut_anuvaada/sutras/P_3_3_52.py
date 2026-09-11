# Sutra प.3.3.52: प्रे वणिजाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre vaRijAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.52"
SUTRA_TEXT = "प्रे वणिजाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre vaRijAm"


class Sutra3352:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

