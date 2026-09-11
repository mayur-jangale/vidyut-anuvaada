# Sutra प.2.2.36: निष्ठा
# (Samasa (compound formation)) — nizWA

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.36"
SUTRA_TEXT = "निष्ठा"
SUTRA_DESC = "(Samasa (compound formation)) — nizWA"


class Sutra2236:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

