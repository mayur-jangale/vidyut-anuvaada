# Sutra प.3.3.133: क्षिप्रवचने लृट्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kzipravacane lfw

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.133"
SUTRA_TEXT = "क्षिप्रवचने लृट्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kzipravacane lfw"


class Sutra33133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

