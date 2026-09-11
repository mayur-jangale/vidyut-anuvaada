# Sutra प.7.2.67: वस्वेकाजाद्घसाम्
# (Taddhita (secondary derivations)) — vasvekAjAdGasAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.67"
SUTRA_TEXT = "वस्वेकाजाद्घसाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — vasvekAjAdGasAm"


class Sutra7267:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.67: अग्निः'),
		('रामः', '', 'प.7.2.67: रामः'),
		('सीता', '', 'प.7.2.67: सीता'),
	]

