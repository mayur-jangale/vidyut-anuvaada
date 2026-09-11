# Sutra प.2.3.36: सप्तम्यधिकरणे च
# (Samasa (compound formation)) — saptamyaDikaraRe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.36"
SUTRA_TEXT = "सप्तम्यधिकरणे च"
SUTRA_DESC = "(Samasa (compound formation)) — saptamyaDikaraRe ca"


class Sutra2336:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

