# Sutra प.7.3.89: उतो वृद्धिर्लुकि हलि
# (Taddhita (secondary derivations)) — uto vfdDirluki hali

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.89"
SUTRA_TEXT = "उतो वृद्धिर्लुकि हलि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — uto vfdDirluki hali"


class Sutra7389:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.89: अग्निः'),
		('रामः', '', 'प.7.3.89: रामः'),
		('सीता', '', 'प.7.3.89: सीता'),
	]

