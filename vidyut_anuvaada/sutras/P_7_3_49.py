# Sutra प.7.3.49: आदाचार्याणाम्
# (Taddhita (secondary derivations)) — AdAcAryARAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.49"
SUTRA_TEXT = "आदाचार्याणाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — AdAcAryARAm"


class Sutra7349:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.49: अग्निः'),
		('रामः', '', 'प.7.3.49: रामः'),
		('सीता', '', 'प.7.3.49: सीता'),
	]

