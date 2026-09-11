# Sutra प.3.2.77: स्थः क च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sTaH ka ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.77"
SUTRA_TEXT = "स्थः क च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sTaH ka ca"


class Sutra3277:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

