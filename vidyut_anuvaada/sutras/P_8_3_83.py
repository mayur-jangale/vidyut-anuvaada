# Sutra प.8.3.83: ज्योतिरायुषः स्तोमः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.83"
SUTRA_TEXT = "ज्योतिरायुषः स्तोमः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8383:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.83: अग्निः'),
		('रामः', '', 'प.8.3.83: रामः'),
		('सीता', '', 'प.8.3.83: सीता'),
	]

