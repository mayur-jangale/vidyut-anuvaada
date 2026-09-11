# Sutra प.2.2.9: याजकादिभिश्च
# (Samasa (compound formation)) — yAjakAdiBiSca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.9"
SUTRA_TEXT = "याजकादिभिश्च"
SUTRA_DESC = "(Samasa (compound formation)) — yAjakAdiBiSca"


class Sutra229:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

