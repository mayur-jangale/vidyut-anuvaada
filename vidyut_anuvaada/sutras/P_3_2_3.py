# Sutra प.3.2.3: आतोऽनुपसर्गे कः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Ato'nupasarge kaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.3"
SUTRA_TEXT = "आतोऽनुपसर्गे कः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Ato'nupasarge kaH"


class Sutra323:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

