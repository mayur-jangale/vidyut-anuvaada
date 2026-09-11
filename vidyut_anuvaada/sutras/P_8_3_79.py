# Sutra प.8.3.79: विभाषेटः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.79"
SUTRA_TEXT = "विभाषेटः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8379:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.79: अग्निः'),
		('रामः', '', 'प.8.3.79: रामः'),
		('सीता', '', 'प.8.3.79: सीता'),
	]

