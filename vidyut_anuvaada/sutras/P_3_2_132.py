# Sutra प.3.2.132: सुञो यज्ञसंयोगे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — suYo yajYasaMyoge

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.132"
SUTRA_TEXT = "सुञो यज्ञसंयोगे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — suYo yajYasaMyoge"


class Sutra32132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

