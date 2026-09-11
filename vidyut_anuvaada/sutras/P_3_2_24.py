# Sutra प.3.2.24: स्तम्बशकृतोरिन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — stambaSakftorin

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.24"
SUTRA_TEXT = "स्तम्बशकृतोरिन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — stambaSakftorin"


class Sutra3224:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

