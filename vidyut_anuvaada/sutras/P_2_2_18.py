# Sutra प.2.2.18: कुगतिप्रादयः
# (Samasa (compound formation)) — kugatiprAdayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.18"
SUTRA_TEXT = "कुगतिप्रादयः"
SUTRA_DESC = "(Samasa (compound formation)) — kugatiprAdayaH"


class Sutra2218:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

