# Sutra प.3.2.135: तृन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — tfn

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.135"
SUTRA_TEXT = "तृन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — tfn"


class Sutra32135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

