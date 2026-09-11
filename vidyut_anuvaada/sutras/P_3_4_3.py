# Sutra प.3.4.3: समुच्चयेऽन्यतरस्याम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — samuccaye'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.3"
SUTRA_TEXT = "समुच्चयेऽन्यतरस्याम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — samuccaye'nyatarasyAm"


class Sutra343:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

