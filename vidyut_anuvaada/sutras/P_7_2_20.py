# Sutra प.7.2.20: दृढः स्थूलबलयोः
# (Taddhita (secondary derivations)) — dfQaH sTUlabalayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.20"
SUTRA_TEXT = "दृढः स्थूलबलयोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — dfQaH sTUlabalayoH"


class Sutra7220:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.20: अग्निः'),
		('रामः', '', 'प.7.2.20: रामः'),
		('सीता', '', 'प.7.2.20: सीता'),
	]

