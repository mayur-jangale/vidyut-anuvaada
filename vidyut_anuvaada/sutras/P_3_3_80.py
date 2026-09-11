# Sutra प.3.3.80: उद्घनोऽत्याधानम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — udGano'tyADAnam

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.80"
SUTRA_TEXT = "उद्घनोऽत्याधानम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — udGano'tyADAnam"


class Sutra3380:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

