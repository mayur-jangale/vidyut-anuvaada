# Sutra प.2.4.15: अधिकरणैतावत्त्वे च
# (Samasa (compound formation)) — aDikaraREtAvattve ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.15"
SUTRA_TEXT = "अधिकरणैतावत्त्वे च"
SUTRA_DESC = "(Samasa (compound formation)) — aDikaraREtAvattve ca"


class Sutra2415:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

