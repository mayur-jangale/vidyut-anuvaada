# Sutra प.7.1.17: जसः शी
# (Taddhita (secondary derivations)) — jasaH SI

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.17"
SUTRA_TEXT = "जसः शी"
SUTRA_DESC = "(Taddhita (secondary derivations)) — jasaH SI"


class Sutra7117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.17: अग्निः'),
		('रामः', '', 'प.7.1.17: रामः'),
		('सीता', '', 'प.7.1.17: सीता'),
	]

