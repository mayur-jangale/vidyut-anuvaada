# Sutra प.4.4.4: कुलत्थकोपधादण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kulatTakopaDAdaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.4"
SUTRA_TEXT = "कुलत्थकोपधादण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kulatTakopaDAdaR"


class Sutra444:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.4: अग्निः'),
		('रामः', '', 'प.4.4.4: रामः'),
		('सीता', '', 'प.4.4.4: सीता'),
	]

