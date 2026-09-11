# Sutra प.2.4.24: अशाला च
# (Samasa (compound formation)) — aSAlA ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.24"
SUTRA_TEXT = "अशाला च"
SUTRA_DESC = "(Samasa (compound formation)) — aSAlA ca"


class Sutra2424:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

