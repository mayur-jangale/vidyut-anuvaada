# Sutra प.2.4.8: क्षुद्रजन्तवः
# (Samasa (compound formation)) — kzudrajantavaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.8"
SUTRA_TEXT = "क्षुद्रजन्तवः"
SUTRA_DESC = "(Samasa (compound formation)) — kzudrajantavaH"


class Sutra248:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

