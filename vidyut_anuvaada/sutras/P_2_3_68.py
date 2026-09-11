# Sutra प.2.3.68: अधिकरणवाचिनश्च
# (Samasa (compound formation)) — aDikaraRavAcinaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.68"
SUTRA_TEXT = "अधिकरणवाचिनश्च"
SUTRA_DESC = "(Samasa (compound formation)) — aDikaraRavAcinaSca"


class Sutra2368:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

