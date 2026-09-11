# Sutra प.3.2.127: तौ सत्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — tO sat

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.127"
SUTRA_TEXT = "तौ सत्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — tO sat"


class Sutra32127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

