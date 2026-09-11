# Sutra प.3.4.12: शकि णमुल्कमुलौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Saki RamulkamulO

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.12"
SUTRA_TEXT = "शकि णमुल्कमुलौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Saki RamulkamulO"


class Sutra3412:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

