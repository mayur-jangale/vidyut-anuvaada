# Sutra प.7.2.56: उदितो वा
# (Taddhita (secondary derivations)) — udito vA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.56"
SUTRA_TEXT = "उदितो वा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — udito vA"


class Sutra7256:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.56: अग्निः'),
		('रामः', '', 'प.7.2.56: रामः'),
		('सीता', '', 'प.7.2.56: सीता'),
	]

