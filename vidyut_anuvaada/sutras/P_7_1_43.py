# Sutra प.7.1.43: यजध्वैनमिति च
# (Taddhita (secondary derivations)) — yajaDvEnamiti ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.43"
SUTRA_TEXT = "यजध्वैनमिति च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yajaDvEnamiti ca"


class Sutra7143:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.43: अग्निः'),
		('रामः', '', 'प.7.1.43: रामः'),
		('सीता', '', 'प.7.1.43: सीता'),
	]

