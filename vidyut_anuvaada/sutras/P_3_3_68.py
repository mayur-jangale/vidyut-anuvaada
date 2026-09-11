# Sutra प.3.3.68: प्रमदसम्मदौ हर्षे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pramadasammadO harze

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.68"
SUTRA_TEXT = "प्रमदसम्मदौ हर्षे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pramadasammadO harze"


class Sutra3368:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

