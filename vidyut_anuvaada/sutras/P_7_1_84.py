# Sutra प.7.1.84: दिव औत्
# (Taddhita (secondary derivations)) — diva Ot

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.84"
SUTRA_TEXT = "दिव औत्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — diva Ot"


class Sutra7184:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.84: अग्निः'),
		('रामः', '', 'प.7.1.84: रामः'),
		('सीता', '', 'प.7.1.84: सीता'),
	]

