# Sutra प.3.3.48: नौ वृ धान्ये
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nO vf DAnye

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.48"
SUTRA_TEXT = "नौ वृ धान्ये"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nO vf DAnye"


class Sutra3348:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

