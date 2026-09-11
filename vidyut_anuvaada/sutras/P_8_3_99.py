# Sutra प.8.3.99: एति संज्ञायामगात्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.99"
SUTRA_TEXT = "एति संज्ञायामगात्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8399:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.99: अग्निः'),
		('रामः', '', 'प.8.3.99: रामः'),
		('सीता', '', 'प.8.3.99: सीता'),
	]

