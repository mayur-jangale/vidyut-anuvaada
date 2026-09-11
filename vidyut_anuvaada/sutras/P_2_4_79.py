# Sutra प.2.4.79: तनादिभ्यस्तथासोः
# (Samasa (compound formation)) — tanAdiByastaTAsoH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.79"
SUTRA_TEXT = "तनादिभ्यस्तथासोः"
SUTRA_DESC = "(Samasa (compound formation)) — tanAdiByastaTAsoH"


class Sutra2479:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

