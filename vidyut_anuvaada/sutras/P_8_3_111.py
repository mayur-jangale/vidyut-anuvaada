# Sutra प.8.3.111: सात्पदाद्योः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.111"
SUTRA_TEXT = "सात्पदाद्योः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.111: अग्निः'),
		('रामः', '', 'प.8.3.111: रामः'),
		('सीता', '', 'प.8.3.111: सीता'),
	]

