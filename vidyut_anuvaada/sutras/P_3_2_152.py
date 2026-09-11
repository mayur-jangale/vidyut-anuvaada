# Sutra प.3.2.152: न यः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — na yaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.152"
SUTRA_TEXT = "न यः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — na yaH"


class Sutra32152:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

