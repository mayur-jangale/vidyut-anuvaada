# Sutra प.3.3.46: प्रे लिप्सायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre lipsAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.46"
SUTRA_TEXT = "प्रे लिप्सायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre lipsAyAm"


class Sutra3346:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

