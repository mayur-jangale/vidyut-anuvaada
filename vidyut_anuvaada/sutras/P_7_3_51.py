# Sutra प.7.3.51: इसुसुक्तान्तात् कः
# (Taddhita (secondary derivations)) — isusuktAntAt kaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.51"
SUTRA_TEXT = "इसुसुक्तान्तात् कः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — isusuktAntAt kaH"


class Sutra7351:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.51: अग्निः'),
		('रामः', '', 'प.7.3.51: रामः'),
		('सीता', '', 'प.7.3.51: सीता'),
	]

