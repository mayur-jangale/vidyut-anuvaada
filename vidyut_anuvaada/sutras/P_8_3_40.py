# Sutra प.8.3.40: नमस्पुरसोर्गत्योः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.40"
SUTRA_TEXT = "नमस्पुरसोर्गत्योः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8340:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.40: अग्निः'),
		('रामः', '', 'प.8.3.40: रामः'),
		('सीता', '', 'प.8.3.40: सीता'),
	]

