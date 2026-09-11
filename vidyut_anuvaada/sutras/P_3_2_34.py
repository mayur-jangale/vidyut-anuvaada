# Sutra प.3.2.34: मितनखे च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — mitanaKe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.34"
SUTRA_TEXT = "मितनखे च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — mitanaKe ca"


class Sutra3234:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

