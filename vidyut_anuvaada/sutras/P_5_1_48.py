# Sutra प.5.1.48: पूरणार्धाट्ठन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUraRArDAwWan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.48"
SUTRA_TEXT = "पूरणार्धाट्ठन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUraRArDAwWan"


class Sutra5148:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.48: अग्निः'),
		('रामः', '', 'प.5.1.48: रामः'),
		('सीता', '', 'प.5.1.48: सीता'),
	]

