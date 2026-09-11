# Sutra प.3.2.130: इङ्धार्योः शत्रकृच्छ्रिणि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — iNDAryoH SatrakfcCriRi

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.130"
SUTRA_TEXT = "इङ्धार्योः शत्रकृच्छ्रिणि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — iNDAryoH SatrakfcCriRi"


class Sutra32130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

