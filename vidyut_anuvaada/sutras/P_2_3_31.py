# Sutra प.2.3.31: एनपा द्वितीया
# (Samasa (compound formation)) — enapA dvitIyA

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.31"
SUTRA_TEXT = "एनपा द्वितीया"
SUTRA_DESC = "(Samasa (compound formation)) — enapA dvitIyA"


class Sutra2331:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

