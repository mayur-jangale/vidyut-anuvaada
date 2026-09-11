# Sutra प.3.3.54: वृणोतेराच्छादने
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vfRoterAcCAdane

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.54"
SUTRA_TEXT = "वृणोतेराच्छादने"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vfRoterAcCAdane"


class Sutra3354:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

