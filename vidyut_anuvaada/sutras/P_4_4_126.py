# Sutra प.4.4.126: अश्विमानण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aSvimAnaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.126"
SUTRA_TEXT = "अश्विमानण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aSvimAnaR"


class Sutra44126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.126: अग्निः'),
		('रामः', '', 'प.4.4.126: रामः'),
		('सीता', '', 'प.4.4.126: सीता'),
	]

