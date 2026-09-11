# Sutra प.7.3.77: इषुगमियमां छः
# (Taddhita (secondary derivations)) — izugamiyamAM CaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.77"
SUTRA_TEXT = "इषुगमियमां छः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — izugamiyamAM CaH"


class Sutra7377:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.77: अग्निः'),
		('रामः', '', 'प.7.3.77: रामः'),
		('सीता', '', 'प.7.3.77: सीता'),
	]

