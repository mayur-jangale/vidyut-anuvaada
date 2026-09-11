# Sutra प.3.2.49: आशिषि हनः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ASizi hanaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.49"
SUTRA_TEXT = "आशिषि हनः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ASizi hanaH"


class Sutra3249:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

