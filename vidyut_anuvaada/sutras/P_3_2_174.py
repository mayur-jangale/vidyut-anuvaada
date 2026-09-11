# Sutra प.3.2.174: भियः क्रुक्लुकनौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BiyaH kruklukanO

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.174"
SUTRA_TEXT = "भियः क्रुक्लुकनौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BiyaH kruklukanO"


class Sutra32174:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

