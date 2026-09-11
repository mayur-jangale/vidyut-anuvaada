# Sutra प.4.2.110: प्रस्थोत्तरपदपलद्यादिकोपधादण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — prasTottarapadapaladyAdikopaDAdaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.110"
SUTRA_TEXT = "प्रस्थोत्तरपदपलद्यादिकोपधादण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — prasTottarapadapaladyAdikopaDAdaR"


class Sutra42110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.110: अग्निः'),
		('रामः', '', 'प.4.2.110: रामः'),
		('सीता', '', 'प.4.2.110: सीता'),
	]

