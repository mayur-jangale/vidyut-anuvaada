# Sutra प.2.4.61: न तौल्वलिभ्यः
# (Samasa (compound formation)) — na tOlvaliByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.61"
SUTRA_TEXT = "न तौल्वलिभ्यः"
SUTRA_DESC = "(Samasa (compound formation)) — na tOlvaliByaH"


class Sutra2461:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

