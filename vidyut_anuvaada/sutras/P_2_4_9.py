# Sutra प.2.4.9: येषां च विरोधः शाश्वतिकः
# (Samasa (compound formation)) — yezAM ca viroDaH SASvatikaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.9"
SUTRA_TEXT = "येषां च विरोधः शाश्वतिकः"
SUTRA_DESC = "(Samasa (compound formation)) — yezAM ca viroDaH SASvatikaH"


class Sutra249:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

