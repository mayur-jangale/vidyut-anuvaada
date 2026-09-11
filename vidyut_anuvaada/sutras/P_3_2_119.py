# Sutra प.3.2.119: अपरोक्षे च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — aparokze ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.119"
SUTRA_TEXT = "अपरोक्षे च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — aparokze ca"


class Sutra32119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

