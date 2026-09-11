# Sutra प.3.2.90: सोमे सुञः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — some suYaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.90"
SUTRA_TEXT = "सोमे सुञः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — some suYaH"


class Sutra3290:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

