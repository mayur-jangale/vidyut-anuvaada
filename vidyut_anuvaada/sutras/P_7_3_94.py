# Sutra प.7.3.94: यङो वा
# (Taddhita (secondary derivations)) — yaNo vA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.94"
SUTRA_TEXT = "यङो वा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yaNo vA"


class Sutra7394:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.94: अग्निः'),
		('रामः', '', 'प.7.3.94: रामः'),
		('सीता', '', 'प.7.3.94: सीता'),
	]

