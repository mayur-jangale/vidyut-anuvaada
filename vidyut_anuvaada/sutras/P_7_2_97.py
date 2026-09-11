# Sutra प.7.2.97: त्वमावेकवचने
# (Taddhita (secondary derivations)) — tvamAvekavacane

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.97"
SUTRA_TEXT = "त्वमावेकवचने"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tvamAvekavacane"


class Sutra7297:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.97: अग्निः'),
		('रामः', '', 'प.7.2.97: रामः'),
		('सीता', '', 'प.7.2.97: सीता'),
	]

