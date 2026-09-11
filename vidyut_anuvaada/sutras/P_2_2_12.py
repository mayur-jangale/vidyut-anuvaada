# Sutra प.2.2.12: क्तेन च पूजायाम्
# (Samasa (compound formation)) — ktena ca pUjAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.12"
SUTRA_TEXT = "क्तेन च पूजायाम्"
SUTRA_DESC = "(Samasa (compound formation)) — ktena ca pUjAyAm"


class Sutra2212:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

