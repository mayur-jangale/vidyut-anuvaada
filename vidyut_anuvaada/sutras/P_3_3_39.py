# Sutra प.3.3.39: व्युपयोः शेतेः पर्याये
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vyupayoH SeteH paryAye

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.39"
SUTRA_TEXT = "व्युपयोः शेतेः पर्याये"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vyupayoH SeteH paryAye"


class Sutra3339:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

