# Sutra प.8.3.61: स्तौतिण्योरेव षण्यभ्यासात्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.61"
SUTRA_TEXT = "स्तौतिण्योरेव षण्यभ्यासात्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8361:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.61: अग्निः'),
		('रामः', '', 'प.8.3.61: रामः'),
		('सीता', '', 'प.8.3.61: सीता'),
	]

