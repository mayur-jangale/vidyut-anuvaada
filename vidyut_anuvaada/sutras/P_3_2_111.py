# Sutra प.3.2.111: अनद्यतने लङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — anadyatane laN

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.111"
SUTRA_TEXT = "अनद्यतने लङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — anadyatane laN"


class Sutra32111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

