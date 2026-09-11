# Sutra प.7.1.65: आङो यि
# (Taddhita (secondary derivations)) — ANo yi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.65"
SUTRA_TEXT = "आङो यि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ANo yi"


class Sutra7165:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.65: अग्निः'),
		('रामः', '', 'प.7.1.65: रामः'),
		('सीता', '', 'प.7.1.65: सीता'),
	]

