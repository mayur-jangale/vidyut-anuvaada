# Sutra प.3.2.66: हव्येऽनन्तः पादम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — havye'nantaH pAdam

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.66"
SUTRA_TEXT = "हव्येऽनन्तः पादम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — havye'nantaH pAdam"


class Sutra3266:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

