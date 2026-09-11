# Sutra प.7.3.50: ठस्येकः
# (Taddhita (secondary derivations)) — WasyekaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.50"
SUTRA_TEXT = "ठस्येकः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — WasyekaH"


class Sutra7350:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.50: अग्निः'),
		('रामः', '', 'प.7.3.50: रामः'),
		('सीता', '', 'प.7.3.50: सीता'),
	]

