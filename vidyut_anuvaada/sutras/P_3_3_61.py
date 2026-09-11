# Sutra प.3.3.61: व्यधजपोरनुपसर्गे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vyaDajaporanupasarge

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.61"
SUTRA_TEXT = "व्यधजपोरनुपसर्गे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vyaDajaporanupasarge"


class Sutra3361:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

