# Sutra प.5.2.48: तस्य पूरणे डट्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya pUraRe qaw

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.48"
SUTRA_TEXT = "तस्य पूरणे डट्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya pUraRe qaw"


class Sutra5248:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.48: अग्निः'),
		('रामः', '', 'प.5.2.48: रामः'),
		('सीता', '', 'प.5.2.48: सीता'),
	]

