# Sutra प.3.3.123: उदङ्कोऽनुदके
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — udaNko'nudake

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.123"
SUTRA_TEXT = "उदङ्कोऽनुदके"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — udaNko'nudake"


class Sutra33123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

