# Sutra प.3.2.62: भजो ण्विः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Bajo RviH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.62"
SUTRA_TEXT = "भजो ण्विः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Bajo RviH"


class Sutra3262:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

