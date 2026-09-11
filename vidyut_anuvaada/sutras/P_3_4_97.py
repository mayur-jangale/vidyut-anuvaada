# Sutra प.3.4.97: इतश्च लोपः परस्मैपदेषु
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — itaSca lopaH parasmEpadezu

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.97"
SUTRA_TEXT = "इतश्च लोपः परस्मैपदेषु"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — itaSca lopaH parasmEpadezu"


class Sutra3497:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

