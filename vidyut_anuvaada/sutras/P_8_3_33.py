# Sutra प.8.3.33: मय उञो वो वा
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.33"
SUTRA_TEXT = "मय उञो वो वा"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8333:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.33: अग्निः'),
		('रामः', '', 'प.8.3.33: रामः'),
		('सीता', '', 'प.8.3.33: सीता'),
	]

