# Sutra प.3.2.44: क्षेमप्रियमद्रेऽण् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kzemapriyamadre'R ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.44"
SUTRA_TEXT = "क्षेमप्रियमद्रेऽण् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kzemapriyamadre'R ca"


class Sutra3244:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

