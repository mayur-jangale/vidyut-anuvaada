# Sutra प.3.4.14: कृत्यार्थे तवैकेन्केन्यत्वनः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kftyArTe tavEkenkenyatvanaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.14"
SUTRA_TEXT = "कृत्यार्थे तवैकेन्केन्यत्वनः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kftyArTe tavEkenkenyatvanaH"


class Sutra3414:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

