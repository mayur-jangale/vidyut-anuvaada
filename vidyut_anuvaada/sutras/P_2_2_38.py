# Sutra प.2.2.38: कडाराः कर्मधारये
# (Samasa (compound formation)) — kaqArAH karmaDAraye

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.38"
SUTRA_TEXT = "कडाराः कर्मधारये"
SUTRA_DESC = "(Samasa (compound formation)) — kaqArAH karmaDAraye"


class Sutra2238:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

