# Sutra प.3.3.20: परिमाणाख्यायां सर्वेभ्यः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — parimARAKyAyAM sarveByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.20"
SUTRA_TEXT = "परिमाणाख्यायां सर्वेभ्यः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — parimARAKyAyAM sarveByaH"


class Sutra3320:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

