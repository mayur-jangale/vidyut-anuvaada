# Sutra प.3.3.112: आक्रोशे नञ्यनिः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AkroSe naYyaniH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.112"
SUTRA_TEXT = "आक्रोशे नञ्यनिः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AkroSe naYyaniH"


class Sutra33112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

