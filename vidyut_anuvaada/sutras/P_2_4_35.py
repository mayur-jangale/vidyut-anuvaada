# Sutra प.2.4.35: आर्धधातुके
# (Samasa (compound formation)) — ArDaDAtuke

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.35"
SUTRA_TEXT = "आर्धधातुके"
SUTRA_DESC = "(Samasa (compound formation)) — ArDaDAtuke"


class Sutra2435:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

