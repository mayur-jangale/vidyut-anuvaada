# Sutra प.2.4.48: इङश्च
# (Samasa (compound formation)) — iNaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.48"
SUTRA_TEXT = "इङश्च"
SUTRA_DESC = "(Samasa (compound formation)) — iNaSca"


class Sutra2448:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

