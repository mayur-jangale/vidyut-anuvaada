# Sutra प.3.2.97: सप्तम्यां जनेर्डः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — saptamyAM janerqaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.97"
SUTRA_TEXT = "सप्तम्यां जनेर्डः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — saptamyAM janerqaH"


class Sutra3297:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

