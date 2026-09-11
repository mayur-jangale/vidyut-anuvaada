# Sutra प.4.2.132: कोपधादण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kopaDAdaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.132"
SUTRA_TEXT = "कोपधादण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kopaDAdaR"


class Sutra42132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.132: अग्निः'),
		('रामः', '', 'प.4.2.132: रामः'),
		('सीता', '', 'प.4.2.132: सीता'),
	]

