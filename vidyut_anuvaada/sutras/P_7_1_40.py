# Sutra प.7.1.40: अमो मश्
# (Taddhita (secondary derivations)) — amo maS

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.40"
SUTRA_TEXT = "अमो मश्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — amo maS"


class Sutra7140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.40: अग्निः'),
		('रामः', '', 'प.7.1.40: रामः'),
		('सीता', '', 'प.7.1.40: सीता'),
	]

