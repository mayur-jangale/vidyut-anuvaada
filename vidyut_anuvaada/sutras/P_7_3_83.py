# Sutra प.7.3.83: जुसि च
# (Taddhita (secondary derivations)) — jusi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.83"
SUTRA_TEXT = "जुसि च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — jusi ca"


class Sutra7383:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.83: अग्निः'),
		('रामः', '', 'प.7.3.83: रामः'),
		('सीता', '', 'प.7.3.83: सीता'),
	]

