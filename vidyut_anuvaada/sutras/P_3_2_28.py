# Sutra प.3.2.28: एजेः खश्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ejeH KaS

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.28"
SUTRA_TEXT = "एजेः खश्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ejeH KaS"


class Sutra3228:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

