# Sutra प.7.1.91: णलुत्तमो वा
# (Taddhita (secondary derivations)) — Raluttamo vA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.91"
SUTRA_TEXT = "णलुत्तमो वा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Raluttamo vA"


class Sutra7191:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.91: अग्निः'),
		('रामः', '', 'प.7.1.91: रामः'),
		('सीता', '', 'प.7.1.91: सीता'),
	]

