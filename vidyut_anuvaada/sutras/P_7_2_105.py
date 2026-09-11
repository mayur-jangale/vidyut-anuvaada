# Sutra प.7.2.105: क्वाति
# (Taddhita (secondary derivations)) — kvAti

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.105"
SUTRA_TEXT = "क्वाति"
SUTRA_DESC = "(Taddhita (secondary derivations)) — kvAti"


class Sutra72105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.105: अग्निः'),
		('रामः', '', 'प.7.2.105: रामः'),
		('सीता', '', 'प.7.2.105: सीता'),
	]

