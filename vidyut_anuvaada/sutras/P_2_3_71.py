# Sutra प.2.3.71: कृत्यानां कर्तरि वा
# (Samasa (compound formation)) — kftyAnAM kartari vA

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.71"
SUTRA_TEXT = "कृत्यानां कर्तरि वा"
SUTRA_DESC = "(Samasa (compound formation)) — kftyAnAM kartari vA"


class Sutra2371:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

