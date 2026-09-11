# Sutra प.8.3.81: भीरोः स्थानम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.81"
SUTRA_TEXT = "भीरोः स्थानम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8381:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.81: अग्निः'),
		('रामः', '', 'प.8.3.81: रामः'),
		('सीता', '', 'प.8.3.81: सीता'),
	]

