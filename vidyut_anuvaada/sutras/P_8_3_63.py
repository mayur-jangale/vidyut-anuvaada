# Sutra प.8.3.63: प्राक्सितादड्व्यवायेऽपि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.63"
SUTRA_TEXT = "प्राक्सितादड्व्यवायेऽपि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8363:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.63: अग्निः'),
		('रामः', '', 'प.8.3.63: रामः'),
		('सीता', '', 'प.8.3.63: सीता'),
	]

