# Sutra प.2.2.29: चार्थे द्वन्द्वः
# (Samasa (compound formation)) — cArTe dvandvaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.29"
SUTRA_TEXT = "चार्थे द्वन्द्वः"
SUTRA_DESC = "(Samasa (compound formation)) — cArTe dvandvaH"


class Sutra2229:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

