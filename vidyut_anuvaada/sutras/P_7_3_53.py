# Sutra प.7.3.53: न्यङ्क्वादीनां च
# (Taddhita (secondary derivations)) — nyaNkvAdInAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.53"
SUTRA_TEXT = "न्यङ्क्वादीनां च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — nyaNkvAdInAM ca"


class Sutra7353:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.53: अग्निः'),
		('रामः', '', 'प.7.3.53: रामः'),
		('सीता', '', 'प.7.3.53: सीता'),
	]

