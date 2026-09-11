# Sutra प.3.3.3: भविष्यति गम्यादयः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Bavizyati gamyAdayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.3"
SUTRA_TEXT = "भविष्यति गम्यादयः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Bavizyati gamyAdayaH"


class Sutra333:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

