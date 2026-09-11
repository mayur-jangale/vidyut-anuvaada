# Sutra प.7.3.80: प्वादीनां ह्रस्वः
# (Taddhita (secondary derivations)) — pvAdInAM hrasvaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.80"
SUTRA_TEXT = "प्वादीनां ह्रस्वः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — pvAdInAM hrasvaH"


class Sutra7380:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.80: अग्निः'),
		('रामः', '', 'प.7.3.80: रामः'),
		('सीता', '', 'प.7.3.80: सीता'),
	]

