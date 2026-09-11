# Sutra प.4.4.25: मुद्गादण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — mudgAdaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.25"
SUTRA_TEXT = "मुद्गादण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — mudgAdaR"


class Sutra4425:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.25: अग्निः'),
		('रामः', '', 'प.4.4.25: रामः'),
		('सीता', '', 'प.4.4.25: सीता'),
	]

