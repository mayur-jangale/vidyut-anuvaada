# Sutra प.2.3.21: इत्थंभूतलक्षणे
# (Samasa (compound formation)) — itTaMBUtalakzaRe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.21"
SUTRA_TEXT = "इत्थंभूतलक्षणे"
SUTRA_DESC = "(Samasa (compound formation)) — itTaMBUtalakzaRe"


class Sutra2321:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

