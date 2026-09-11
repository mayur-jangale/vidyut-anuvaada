# Sutra प.3.3.66: नित्यं पणः परिमाणे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nityaM paRaH parimARe

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.66"
SUTRA_TEXT = "नित्यं पणः परिमाणे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nityaM paRaH parimARe"


class Sutra3366:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

