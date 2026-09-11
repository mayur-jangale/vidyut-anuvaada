# Sutra प.3.2.11: आङि ताच्छील्ये
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ANi tAcCIlye

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.11"
SUTRA_TEXT = "आङि ताच्छील्ये"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ANi tAcCIlye"


class Sutra3211:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

