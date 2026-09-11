# Sutra प.7.2.51: पूङश्च
# (Taddhita (secondary derivations)) — pUNaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.51"
SUTRA_TEXT = "पूङश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — pUNaSca"


class Sutra7251:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.51: अग्निः'),
		('रामः', '', 'प.7.2.51: रामः'),
		('सीता', '', 'प.7.2.51: सीता'),
	]

