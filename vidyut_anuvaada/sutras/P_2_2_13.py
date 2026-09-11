# Sutra प.2.2.13: अधिकरणवाचिना च
# (Samasa (compound formation)) — aDikaraRavAcinA ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.13"
SUTRA_TEXT = "अधिकरणवाचिना च"
SUTRA_DESC = "(Samasa (compound formation)) — aDikaraRavAcinA ca"


class Sutra2213:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

