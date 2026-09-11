# Sutra प.3.2.70: दुहः कब् घश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — duhaH kab GaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.70"
SUTRA_TEXT = "दुहः कब् घश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — duhaH kab GaSca"


class Sutra3270:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

