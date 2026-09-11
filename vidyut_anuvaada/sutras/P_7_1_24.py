# Sutra प.7.1.24: अतोऽम्
# (Taddhita (secondary derivations)) — ato'm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.24"
SUTRA_TEXT = "अतोऽम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ato'm"


class Sutra7124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.24: अग्निः'),
		('रामः', '', 'प.7.1.24: रामः'),
		('सीता', '', 'प.7.1.24: सीता'),
	]

