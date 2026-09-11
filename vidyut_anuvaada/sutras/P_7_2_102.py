# Sutra प.7.2.102: त्यदादीनामः
# (Taddhita (secondary derivations)) — tyadAdInAmaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.102"
SUTRA_TEXT = "त्यदादीनामः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tyadAdInAmaH"


class Sutra72102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.102: अग्निः'),
		('रामः', '', 'प.7.2.102: रामः'),
		('सीता', '', 'प.7.2.102: सीता'),
	]

