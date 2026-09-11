# Sutra प.2.2.22: क्त्वा च
# (Samasa (compound formation)) — ktvA ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.22"
SUTRA_TEXT = "क्त्वा च"
SUTRA_DESC = "(Samasa (compound formation)) — ktvA ca"


class Sutra2222:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

