# Sutra प.3.3.70: अक्षेषु ग्लहः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — akzezu glahaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.70"
SUTRA_TEXT = "अक्षेषु ग्लहः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — akzezu glahaH"


class Sutra3370:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

