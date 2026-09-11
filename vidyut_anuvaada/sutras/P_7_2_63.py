# Sutra प.7.2.63: ऋतो भारद्वाजस्य
# (Taddhita (secondary derivations)) — fto BAradvAjasya

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.63"
SUTRA_TEXT = "ऋतो भारद्वाजस्य"
SUTRA_DESC = "(Taddhita (secondary derivations)) — fto BAradvAjasya"


class Sutra7263:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.63: अग्निः'),
		('रामः', '', 'प.7.2.63: रामः'),
		('सीता', '', 'प.7.2.63: सीता'),
	]

