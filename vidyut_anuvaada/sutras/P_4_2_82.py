# Sutra प.4.2.82: वरणादिभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — varaRAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.82"
SUTRA_TEXT = "वरणादिभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — varaRAdiByaSca"


class Sutra4282:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.82: अग्निः'),
		('रामः', '', 'प.4.2.82: रामः'),
		('सीता', '', 'प.4.2.82: सीता'),
	]

