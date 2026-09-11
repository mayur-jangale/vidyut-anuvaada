# Sutra प.2.2.34: अल्पाच्तरम्
# (Samasa (compound formation)) — alpActaram

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.34"
SUTRA_TEXT = "अल्पाच्तरम्"
SUTRA_DESC = "(Samasa (compound formation)) — alpActaram"


class Sutra2234:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

