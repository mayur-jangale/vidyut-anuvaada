# Sutra प.7.3.20: अनुशतिकादीनां च
# (Taddhita (secondary derivations)) — anuSatikAdInAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.20"
SUTRA_TEXT = "अनुशतिकादीनां च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — anuSatikAdInAM ca"


class Sutra7320:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.20: अग्निः'),
		('रामः', '', 'प.7.3.20: रामः'),
		('सीता', '', 'प.7.3.20: सीता'),
	]

