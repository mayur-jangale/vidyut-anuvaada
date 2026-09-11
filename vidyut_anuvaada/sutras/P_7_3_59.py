# Sutra प.7.3.59: न क्वादेः
# (Taddhita (secondary derivations)) — na kvAdeH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.59"
SUTRA_TEXT = "न क्वादेः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — na kvAdeH"


class Sutra7359:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.59: अग्निः'),
		('रामः', '', 'प.7.3.59: रामः'),
		('सीता', '', 'प.7.3.59: सीता'),
	]

