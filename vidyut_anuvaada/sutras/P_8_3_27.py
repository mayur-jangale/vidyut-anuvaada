# Sutra प.8.3.27: नपरे नः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.27"
SUTRA_TEXT = "नपरे नः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8327:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.27: अग्निः'),
		('रामः', '', 'प.8.3.27: रामः'),
		('सीता', '', 'प.8.3.27: सीता'),
	]

