# Sutra प.2.3.42: पञ्चमी विभक्ते
# (Samasa (compound formation)) — paYcamI viBakte

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.42"
SUTRA_TEXT = "पञ्चमी विभक्ते"
SUTRA_DESC = "(Samasa (compound formation)) — paYcamI viBakte"


class Sutra2342:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

