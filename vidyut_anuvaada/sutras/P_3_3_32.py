# Sutra प.3.3.32: प्रे स्त्रोऽयज्ञे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre stro'yajYe

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.32"
SUTRA_TEXT = "प्रे स्त्रोऽयज्ञे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre stro'yajYe"


class Sutra3332:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

