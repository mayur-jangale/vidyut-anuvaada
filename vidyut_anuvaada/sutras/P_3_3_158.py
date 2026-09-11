# Sutra प.3.3.158: समानकर्तृकेषु तुमुन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — samAnakartfkezu tumun

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.158"
SUTRA_TEXT = "समानकर्तृकेषु तुमुन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — samAnakartfkezu tumun"


class Sutra33158:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

