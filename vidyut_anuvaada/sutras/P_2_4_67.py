# Sutra प.2.4.67: न गोपवनादिभ्यः
# (Samasa (compound formation)) — na gopavanAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.67"
SUTRA_TEXT = "न गोपवनादिभ्यः"
SUTRA_DESC = "(Samasa (compound formation)) — na gopavanAdiByaH"


class Sutra2467:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

