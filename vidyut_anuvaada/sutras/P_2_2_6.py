# Sutra प.2.2.6: नञ्
# (Samasa (compound formation)) — naY

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.6"
SUTRA_TEXT = "नञ्"
SUTRA_DESC = "(Samasa (compound formation)) — naY"


class Sutra226:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

