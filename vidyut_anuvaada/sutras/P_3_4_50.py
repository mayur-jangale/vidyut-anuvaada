# Sutra प.3.4.50: समासत्तौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — samAsattO

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.50"
SUTRA_TEXT = "समासत्तौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — samAsattO"


class Sutra3450:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

