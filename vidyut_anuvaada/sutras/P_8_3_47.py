# Sutra प.8.3.47: अधःशिरसी पदे
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.47"
SUTRA_TEXT = "अधःशिरसी पदे"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8347:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.47: अग्निः'),
		('रामः', '', 'प.8.3.47: रामः'),
		('सीता', '', 'प.8.3.47: सीता'),
	]

