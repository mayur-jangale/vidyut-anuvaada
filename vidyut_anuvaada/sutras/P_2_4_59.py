# Sutra प.2.4.59: पैलादिभ्यश्च
# (Samasa (compound formation)) — pElAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.59"
SUTRA_TEXT = "पैलादिभ्यश्च"
SUTRA_DESC = "(Samasa (compound formation)) — pElAdiByaSca"


class Sutra2459:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

