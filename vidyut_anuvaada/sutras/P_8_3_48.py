# Sutra प.8.3.48: कस्कादिषु च
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.48"
SUTRA_TEXT = "कस्कादिषु च"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8348:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.48: अग्निः'),
		('रामः', '', 'प.8.3.48: रामः'),
		('सीता', '', 'प.8.3.48: सीता'),
	]

