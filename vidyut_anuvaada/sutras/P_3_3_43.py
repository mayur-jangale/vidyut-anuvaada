# Sutra प.3.3.43: कर्मव्यतिहारे णच् स्त्रियाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmavyatihAre Rac striyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.43"
SUTRA_TEXT = "कर्मव्यतिहारे णच् स्त्रियाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmavyatihAre Rac striyAm"


class Sutra3343:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

