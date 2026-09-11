# Sutra प.7.2.91: मपर्यन्तस्य
# (Taddhita (secondary derivations)) — maparyantasya

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.91"
SUTRA_TEXT = "मपर्यन्तस्य"
SUTRA_DESC = "(Taddhita (secondary derivations)) — maparyantasya"


class Sutra7291:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.91: अग्निः'),
		('रामः', '', 'प.7.2.91: रामः'),
		('सीता', '', 'प.7.2.91: सीता'),
	]

