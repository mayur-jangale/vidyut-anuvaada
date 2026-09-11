# Sutra प.2.2.26: दिङ्नामान्यन्तराले
# (Samasa (compound formation)) — diNnAmAnyantarAle

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.26"
SUTRA_TEXT = "दिङ्नामान्यन्तराले"
SUTRA_DESC = "(Samasa (compound formation)) — diNnAmAnyantarAle"


class Sutra2226:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

