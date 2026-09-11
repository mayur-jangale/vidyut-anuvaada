# Sutra प.3.3.56: एरच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — erac

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.56"
SUTRA_TEXT = "एरच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — erac"


class Sutra3356:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

