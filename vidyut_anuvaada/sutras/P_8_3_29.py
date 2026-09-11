# Sutra प.8.3.29: डः सि धुट्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.29"
SUTRA_TEXT = "डः सि धुट्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8329:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.29: अग्निः'),
		('रामः', '', 'प.8.3.29: रामः'),
		('सीता', '', 'प.8.3.29: सीता'),
	]

