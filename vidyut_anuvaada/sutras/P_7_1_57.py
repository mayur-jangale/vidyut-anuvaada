# Sutra प.7.1.57: गोः पादान्ते
# (Taddhita (secondary derivations)) — goH pAdAnte

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.57"
SUTRA_TEXT = "गोः पादान्ते"
SUTRA_DESC = "(Taddhita (secondary derivations)) — goH pAdAnte"


class Sutra7157:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.57: अग्निः'),
		('रामः', '', 'प.7.1.57: रामः'),
		('सीता', '', 'प.7.1.57: सीता'),
	]

