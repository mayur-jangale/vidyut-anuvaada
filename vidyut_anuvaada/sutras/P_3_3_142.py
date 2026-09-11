# Sutra प.3.3.142: गर्हायां लडपिजात्वोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — garhAyAM laqapijAtvoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.142"
SUTRA_TEXT = "गर्हायां लडपिजात्वोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — garhAyAM laqapijAtvoH"


class Sutra33142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

