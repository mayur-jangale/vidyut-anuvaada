# Sutra प.7.1.53: त्रेस्त्रयः
# (Taddhita (secondary derivations)) — trestrayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.53"
SUTRA_TEXT = "त्रेस्त्रयः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — trestrayaH"


class Sutra7153:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.53: अग्निः'),
		('रामः', '', 'प.7.1.53: रामः'),
		('सीता', '', 'प.7.1.53: सीता'),
	]

