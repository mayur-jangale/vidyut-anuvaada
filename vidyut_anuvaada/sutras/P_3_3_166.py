# Sutra प.3.3.166: अधीष्टे च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — aDIzwe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.166"
SUTRA_TEXT = "अधीष्टे च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — aDIzwe ca"


class Sutra33166:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

