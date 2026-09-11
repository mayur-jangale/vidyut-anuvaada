# Sutra प.8.3.96: विकुशमिपरिभ्यः स्थलम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.96"
SUTRA_TEXT = "विकुशमिपरिभ्यः स्थलम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8396:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.96: अग्निः'),
		('रामः', '', 'प.8.3.96: रामः'),
		('सीता', '', 'प.8.3.96: सीता'),
	]

