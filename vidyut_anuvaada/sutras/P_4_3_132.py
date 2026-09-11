# Sutra प.4.3.132: कौपिञ्जलहास्तिपदादण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kOpiYjalahAstipadAdaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.132"
SUTRA_TEXT = "कौपिञ्जलहास्तिपदादण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kOpiYjalahAstipadAdaR"


class Sutra43132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.132: अग्निः'),
		('रामः', '', 'प.4.3.132: रामः'),
		('सीता', '', 'प.4.3.132: सीता'),
	]

