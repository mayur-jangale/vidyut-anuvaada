# Sutra प.7.2.90: शेषे लोपः
# (Taddhita (secondary derivations)) — Seze lopaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.90"
SUTRA_TEXT = "शेषे लोपः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Seze lopaH"


class Sutra7290:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.90: अग्निः'),
		('रामः', '', 'प.7.2.90: रामः'),
		('सीता', '', 'प.7.2.90: सीता'),
	]

