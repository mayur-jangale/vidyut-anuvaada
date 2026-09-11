# Sutra प.8.3.58: नुम्विसर्जनीयशर्व्यवायेऽपि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.58"
SUTRA_TEXT = "नुम्विसर्जनीयशर्व्यवायेऽपि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8358:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.58: अग्निः'),
		('रामः', '', 'प.8.3.58: रामः'),
		('सीता', '', 'प.8.3.58: सीता'),
	]

