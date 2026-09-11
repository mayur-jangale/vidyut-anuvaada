# Sutra प.8.3.60: शासिवसिघसीनां च
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.60"
SUTRA_TEXT = "शासिवसिघसीनां च"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8360:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.60: अग्निः'),
		('रामः', '', 'प.8.3.60: रामः'),
		('सीता', '', 'प.8.3.60: सीता'),
	]

