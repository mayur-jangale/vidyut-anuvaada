# Sutra प.3.3.67: मदोऽनुपसर्गे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — mado'nupasarge

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.67"
SUTRA_TEXT = "मदोऽनुपसर्गे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — mado'nupasarge"


class Sutra3367:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

