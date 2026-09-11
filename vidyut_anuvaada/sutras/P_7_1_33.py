# Sutra प.7.1.33: साम आकम्
# (Taddhita (secondary derivations)) — sAma Akam

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.33"
SUTRA_TEXT = "साम आकम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sAma Akam"


class Sutra7133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.33: अग्निः'),
		('रामः', '', 'प.7.1.33: रामः'),
		('सीता', '', 'प.7.1.33: सीता'),
	]

