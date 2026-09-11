# Sutra प.3.2.41: पूःसर्वयोर्दारिसहोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pUHsarvayordArisahoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.41"
SUTRA_TEXT = "पूःसर्वयोर्दारिसहोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pUHsarvayordArisahoH"


class Sutra3241:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

