# Sutra प.3.3.81: अपघनोऽङ्गम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — apaGano'Ngam

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.81"
SUTRA_TEXT = "अपघनोऽङ्गम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — apaGano'Ngam"


class Sutra3381:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

