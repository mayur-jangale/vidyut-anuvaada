# Sutra प.3.2.123: वर्तमाने लट्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vartamAne law

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.123"
SUTRA_TEXT = "वर्तमाने लट्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vartamAne law"


class Sutra32123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

