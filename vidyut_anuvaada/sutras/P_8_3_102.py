# Sutra प.8.3.102: निसस्तपतावनासेवने
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.102"
SUTRA_TEXT = "निसस्तपतावनासेवने"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.102: अग्निः'),
		('रामः', '', 'प.8.3.102: रामः'),
		('सीता', '', 'प.8.3.102: सीता'),
	]

