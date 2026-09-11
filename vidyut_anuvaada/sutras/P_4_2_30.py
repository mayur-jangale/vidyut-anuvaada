# Sutra प.4.2.30: सोमाट्ट्यण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — somAwwyaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.30"
SUTRA_TEXT = "सोमाट्ट्यण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — somAwwyaR"


class Sutra4230:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.30: अग्निः'),
		('रामः', '', 'प.4.2.30: रामः'),
		('सीता', '', 'प.4.2.30: सीता'),
	]

