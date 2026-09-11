# Sutra प.6.2.147: प्रवृद्धादीनां च
# (Sandhi (euphonic combination)) — pravfdDAdInAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.147"
SUTRA_TEXT = "प्रवृद्धादीनां च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — pravfdDAdInAM ca"


class Sutra62147:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.147: अग्निः'),
		('रामः', '', 'प.6.2.147: रामः'),
		('सीता', '', 'प.6.2.147: सीता'),
	]

