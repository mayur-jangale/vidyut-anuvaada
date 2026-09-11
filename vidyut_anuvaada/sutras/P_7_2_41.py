# Sutra प.7.2.41: इट् सनि वा
# (Taddhita (secondary derivations)) — iw sani vA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.41"
SUTRA_TEXT = "इट् सनि वा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — iw sani vA"


class Sutra7241:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.41: अग्निः'),
		('रामः', '', 'प.7.2.41: रामः'),
		('सीता', '', 'प.7.2.41: सीता'),
	]

