# Sutra प.3.2.17: भिक्षासेनादायेषु च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BikzAsenAdAyezu ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.17"
SUTRA_TEXT = "भिक्षासेनादायेषु च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BikzAsenAdAyezu ca"


class Sutra3217:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

