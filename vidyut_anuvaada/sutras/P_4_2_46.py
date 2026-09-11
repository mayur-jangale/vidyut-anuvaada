# Sutra प.4.2.46: चरणेभ्यो धर्मवत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — caraReByo Darmavat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.46"
SUTRA_TEXT = "चरणेभ्यो धर्मवत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — caraReByo Darmavat"


class Sutra4246:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.46: अग्निः'),
		('रामः', '', 'प.4.2.46: रामः'),
		('सीता', '', 'प.4.2.46: सीता'),
	]

