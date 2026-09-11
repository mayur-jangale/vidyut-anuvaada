# Sutra प.5.3.43: अधिकरणविचाले च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aDikaraRavicAle ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.43"
SUTRA_TEXT = "अधिकरणविचाले च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aDikaraRavicAle ca"


class Sutra5343:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.43: अग्निः'),
		('रामः', '', 'प.5.3.43: रामः'),
		('सीता', '', 'प.5.3.43: सीता'),
	]

