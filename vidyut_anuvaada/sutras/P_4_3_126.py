# Sutra प.4.3.126: गोत्रचरणाद्वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gotracaraRAdvuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.126"
SUTRA_TEXT = "गोत्रचरणाद्वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gotracaraRAdvuY"


class Sutra43126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.126: अग्निः'),
		('रामः', '', 'प.4.3.126: रामः'),
		('सीता', '', 'प.4.3.126: सीता'),
	]

