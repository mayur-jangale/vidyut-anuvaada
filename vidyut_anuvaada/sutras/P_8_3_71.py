# Sutra प.8.3.71: सिवादीनां वाऽड्व्यवायेऽपि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.71"
SUTRA_TEXT = "सिवादीनां वाऽड्व्यवायेऽपि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8371:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.71: अग्निः'),
		('रामः', '', 'प.8.3.71: रामः'),
		('सीता', '', 'प.8.3.71: सीता'),
	]

