# Sutra प.3.2.108: भाषायां सदवसश्रुवः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BAzAyAM sadavasaSruvaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.108"
SUTRA_TEXT = "भाषायां सदवसश्रुवः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BAzAyAM sadavasaSruvaH"


class Sutra32108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

