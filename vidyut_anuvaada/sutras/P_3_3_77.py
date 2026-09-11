# Sutra प.3.3.77: मूर्तौ घनः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — mUrtO GanaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.77"
SUTRA_TEXT = "मूर्तौ घनः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — mUrtO GanaH"


class Sutra3377:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

