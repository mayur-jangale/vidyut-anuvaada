# Sutra प.4.4.62: छत्रादिभ्यो णः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — CatrAdiByo RaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.62"
SUTRA_TEXT = "छत्रादिभ्यो णः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — CatrAdiByo RaH"


class Sutra4462:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.62: अग्निः'),
		('रामः', '', 'प.4.4.62: रामः'),
		('सीता', '', 'प.4.4.62: सीता'),
	]

