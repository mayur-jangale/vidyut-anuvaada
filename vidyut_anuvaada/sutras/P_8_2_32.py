# Sutra प.8.2.32: दादेर्धातोर्घः
# samāse'nañpūrve ktvo lyap — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.32"
SUTRA_TEXT = "दादेर्धातोर्घः"
SUTRA_DESC = "samāse'nañpūrve ktvo lyap — repeated"


class Sutra8232:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.32: अग्निः'),
		('रामः', '', 'प.8.2.32: रामः'),
		('सीता', '', 'प.8.2.32: सीता'),
	]

