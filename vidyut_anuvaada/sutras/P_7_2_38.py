# Sutra प.7.2.38: वॄतो वा
# (Taddhita (secondary derivations)) — vFto vA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.38"
SUTRA_TEXT = "वॄतो वा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — vFto vA"


class Sutra7238:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.38: अग्निः'),
		('रामः', '', 'प.7.2.38: रामः'),
		('सीता', '', 'प.7.2.38: सीता'),
	]

