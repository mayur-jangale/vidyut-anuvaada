# Sutra प.5.3.48: पूरणाद्भागे तीयादन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUraRAdBAge tIyAdan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.48"
SUTRA_TEXT = "पूरणाद्भागे तीयादन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUraRAdBAge tIyAdan"


class Sutra5348:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.48: अग्निः'),
		('रामः', '', 'प.5.3.48: रामः'),
		('सीता', '', 'प.5.3.48: सीता'),
	]

