# Sutra प.2.2.31: राजदन्तादिषु परम्
# (Samasa (compound formation)) — rAjadantAdizu param

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.31"
SUTRA_TEXT = "राजदन्तादिषु परम्"
SUTRA_DESC = "(Samasa (compound formation)) — rAjadantAdizu param"


class Sutra2231:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

