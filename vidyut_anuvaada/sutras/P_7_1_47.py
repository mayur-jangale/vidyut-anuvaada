# Sutra प.7.1.47: क्त्वो यक्
# (Taddhita (secondary derivations)) — ktvo yak

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.47"
SUTRA_TEXT = "क्त्वो यक्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ktvo yak"


class Sutra7147:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.47: अग्निः'),
		('रामः', '', 'प.7.1.47: रामः'),
		('सीता', '', 'प.7.1.47: सीता'),
	]

