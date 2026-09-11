# Sutra प.3.2.4: सुपि स्थः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — supi sTaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.4"
SUTRA_TEXT = "सुपि स्थः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — supi sTaH"


class Sutra324:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

