# Sutra प.3.3.45: आक्रोशेऽवन्योर्ग्रहः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AkroSe'vanyorgrahaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.45"
SUTRA_TEXT = "आक्रोशेऽवन्योर्ग्रहः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AkroSe'vanyorgrahaH"


class Sutra3345:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

