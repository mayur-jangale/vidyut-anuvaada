# Sutra प.4.3.72: द्व्यजृद्ब्राह्मणर्क्प्रथमाध्वरपुरश्चरणनामाख्याताट्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dvyajfdbrAhmaRarkpraTamADvarapuraScaraRanAmAKyAtAwWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.72"
SUTRA_TEXT = "द्व्यजृद्ब्राह्मणर्क्प्रथमाध्वरपुरश्चरणनामाख्याताट्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dvyajfdbrAhmaRarkpraTamADvarapuraScaraRanAmAKyAtAwWak"


class Sutra4372:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.72: अग्निः'),
		('रामः', '', 'प.4.3.72: रामः'),
		('सीता', '', 'प.4.3.72: सीता'),
	]

