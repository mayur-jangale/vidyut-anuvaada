# Sutra प.7.3.58: विभाषा चेः
# (Taddhita (secondary derivations)) — viBAzA ceH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.58"
SUTRA_TEXT = "विभाषा चेः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — viBAzA ceH"


class Sutra7358:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.58: अग्निः'),
		('रामः', '', 'प.7.3.58: रामः'),
		('सीता', '', 'प.7.3.58: सीता'),
	]

