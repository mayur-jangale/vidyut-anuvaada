# Sutra प.2.4.81: आमः
# (Samasa (compound formation)) — AmaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.81"
SUTRA_TEXT = "आमः"
SUTRA_DESC = "(Samasa (compound formation)) — AmaH"


class Sutra2481:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

