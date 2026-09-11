# Sutra प.7.2.89: योऽचि
# (Taddhita (secondary derivations)) — yo'ci

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.89"
SUTRA_TEXT = "योऽचि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yo'ci"


class Sutra7289:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.89: अग्निः'),
		('रामः', '', 'प.7.2.89: रामः'),
		('सीता', '', 'प.7.2.89: सीता'),
	]

