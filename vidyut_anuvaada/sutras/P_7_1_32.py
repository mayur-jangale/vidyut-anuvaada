# Sutra प.7.1.32: एकवचनस्य च
# (Taddhita (secondary derivations)) — ekavacanasya ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.32"
SUTRA_TEXT = "एकवचनस्य च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ekavacanasya ca"


class Sutra7132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.32: अग्निः'),
		('रामः', '', 'प.7.1.32: रामः'),
		('सीता', '', 'प.7.1.32: सीता'),
	]

