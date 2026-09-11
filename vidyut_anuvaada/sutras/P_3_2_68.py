# Sutra प.3.2.68: अदोऽनन्ने
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ado'nanne

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.68"
SUTRA_TEXT = "अदोऽनन्ने"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ado'nanne"


class Sutra3268:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

