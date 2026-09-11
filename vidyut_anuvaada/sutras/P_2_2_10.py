# Sutra प.2.2.10: न निर्धारणे
# (Samasa (compound formation)) — na nirDAraRe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.10"
SUTRA_TEXT = "न निर्धारणे"
SUTRA_DESC = "(Samasa (compound formation)) — na nirDAraRe"


class Sutra2210:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

