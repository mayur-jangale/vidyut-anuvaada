# Sutra प.3.3.42: संघे चानौत्तराधर्ये
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMGe cAnOttarADarye

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.42"
SUTRA_TEXT = "संघे चानौत्तराधर्ये"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMGe cAnOttarADarye"


class Sutra3342:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

