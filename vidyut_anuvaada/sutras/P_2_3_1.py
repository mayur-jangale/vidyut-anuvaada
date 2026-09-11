# Sutra प.2.3.1: अनभिहिते
# (Samasa (compound formation)) — anaBihite

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.1"
SUTRA_TEXT = "अनभिहिते"
SUTRA_DESC = "(Samasa (compound formation)) — anaBihite"


class Sutra231:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

