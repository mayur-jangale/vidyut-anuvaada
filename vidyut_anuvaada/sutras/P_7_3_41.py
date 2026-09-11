# Sutra प.7.3.41: स्फायो वः
# (Taddhita (secondary derivations)) — sPAyo vaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.41"
SUTRA_TEXT = "स्फायो वः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sPAyo vaH"


class Sutra7341:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.41: अग्निः'),
		('रामः', '', 'प.7.3.41: रामः'),
		('सीता', '', 'प.7.3.41: सीता'),
	]

