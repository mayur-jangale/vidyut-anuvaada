# Sutra प.3.4.51: प्रमाणे च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pramARe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.51"
SUTRA_TEXT = "प्रमाणे च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pramARe ca"


class Sutra3451:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

