# Sutra प.3.3.120: अवे तॄस्त्रोर्घञ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ave tFstrorGaY

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.120"
SUTRA_TEXT = "अवे तॄस्त्रोर्घञ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ave tFstrorGaY"


class Sutra33120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

