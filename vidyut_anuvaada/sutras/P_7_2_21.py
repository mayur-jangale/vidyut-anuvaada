# Sutra प.7.2.21: प्रभौ परिवृढः
# (Taddhita (secondary derivations)) — praBO parivfQaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.21"
SUTRA_TEXT = "प्रभौ परिवृढः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — praBO parivfQaH"


class Sutra7221:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.21: अग्निः'),
		('रामः', '', 'प.7.2.21: रामः'),
		('सीता', '', 'प.7.2.21: सीता'),
	]

