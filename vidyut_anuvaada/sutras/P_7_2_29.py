# Sutra प.7.2.29: हृषेर्लोमसु
# (Taddhita (secondary derivations)) — hfzerlomasu

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.29"
SUTRA_TEXT = "हृषेर्लोमसु"
SUTRA_DESC = "(Taddhita (secondary derivations)) — hfzerlomasu"


class Sutra7229:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.29: अग्निः'),
		('रामः', '', 'प.7.2.29: रामः'),
		('सीता', '', 'प.7.2.29: सीता'),
	]

