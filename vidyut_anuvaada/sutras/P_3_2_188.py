# Sutra प.3.2.188: मतिबुद्धिपूजार्थेभ्यश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — matibudDipUjArTeByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.188"
SUTRA_TEXT = "मतिबुद्धिपूजार्थेभ्यश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — matibudDipUjArTeByaSca"


class Sutra32188:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

