# Sutra प.8.3.66: सदिरप्रतेः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.66"
SUTRA_TEXT = "सदिरप्रतेः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8366:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.66: अग्निः'),
		('रामः', '', 'प.8.3.66: रामः'),
		('सीता', '', 'प.8.3.66: सीता'),
	]

