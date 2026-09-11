# Sutra प.8.3.84: मातृपितृभ्यां स्वसा
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.84"
SUTRA_TEXT = "मातृपितृभ्यां स्वसा"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8384:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.84: अग्निः'),
		('रामः', '', 'प.8.3.84: रामः'),
		('सीता', '', 'प.8.3.84: सीता'),
	]

