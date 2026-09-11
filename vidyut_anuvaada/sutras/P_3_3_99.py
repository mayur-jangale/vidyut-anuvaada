# Sutra प.3.3.99: संज्ञायां समजनिषदनिपतमनविदषुञ्शीङ्भृञिणः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMjYAyAM samajanizadanipatamanavidazuYSINBfYiRaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.99"
SUTRA_TEXT = "संज्ञायां समजनिषदनिपतमनविदषुञ्शीङ्भृञिणः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMjYAyAM samajanizadanipatamanavidazuYSINBfYiRaH"


class Sutra3399:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

