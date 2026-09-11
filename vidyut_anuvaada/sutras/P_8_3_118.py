# Sutra प.8.3.118: सदेः परस्य लिटि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.118"
SUTRA_TEXT = "सदेः परस्य लिटि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.118: अग्निः'),
		('रामः', '', 'प.8.3.118: रामः'),
		('सीता', '', 'प.8.3.118: सीता'),
	]

