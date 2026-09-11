# Sutra प.3.2.133: अर्हः प्रशंसायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — arhaH praSaMsAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.133"
SUTRA_TEXT = "अर्हः प्रशंसायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — arhaH praSaMsAyAm"


class Sutra32133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

