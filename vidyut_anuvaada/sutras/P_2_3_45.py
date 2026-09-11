# Sutra प.2.3.45: नक्षत्रे च लुपि
# (Samasa (compound formation)) — nakzatre ca lupi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.45"
SUTRA_TEXT = "नक्षत्रे च लुपि"
SUTRA_DESC = "(Samasa (compound formation)) — nakzatre ca lupi"


class Sutra2345:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

