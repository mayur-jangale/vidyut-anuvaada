# Sutra प.7.2.55: जॄव्रश्च्योः क्त्वि
# (Taddhita (secondary derivations)) — jFvraScyoH ktvi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.55"
SUTRA_TEXT = "जॄव्रश्च्योः क्त्वि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — jFvraScyoH ktvi"


class Sutra7255:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.55: अग्निः'),
		('रामः', '', 'प.7.2.55: रामः'),
		('सीता', '', 'प.7.2.55: सीता'),
	]

