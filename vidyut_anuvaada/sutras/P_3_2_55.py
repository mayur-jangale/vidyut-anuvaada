# Sutra प.3.2.55: पाणिघताडघौ शिल्पिनि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pARiGatAqaGO Silpini

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.55"
SUTRA_TEXT = "पाणिघताडघौ शिल्पिनि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pARiGatAqaGO Silpini"


class Sutra3255:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

