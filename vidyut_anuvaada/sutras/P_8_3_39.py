# Sutra प.8.3.39: इणः षः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.39"
SUTRA_TEXT = "इणः षः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8339:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.39: अग्निः'),
		('रामः', '', 'प.8.3.39: रामः'),
		('सीता', '', 'प.8.3.39: सीता'),
	]

