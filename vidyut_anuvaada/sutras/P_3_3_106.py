# Sutra प.3.3.106: आतश्चोपसर्गे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AtaScopasarge

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.106"
SUTRA_TEXT = "आतश्चोपसर्गे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AtaScopasarge"


class Sutra33106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

