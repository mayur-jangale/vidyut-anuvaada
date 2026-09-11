# Sutra प.8.3.42: तिरसोऽन्यतरस्याम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.42"
SUTRA_TEXT = "तिरसोऽन्यतरस्याम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8342:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.42: अग्निः'),
		('रामः', '', 'प.8.3.42: रामः'),
		('सीता', '', 'प.8.3.42: सीता'),
	]

