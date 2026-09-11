# Sutra प.7.2.83: ईदासः
# (Taddhita (secondary derivations)) — IdAsaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.83"
SUTRA_TEXT = "ईदासः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — IdAsaH"


class Sutra7283:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.83: अग्निः'),
		('रामः', '', 'प.7.2.83: रामः'),
		('सीता', '', 'प.7.2.83: सीता'),
	]

