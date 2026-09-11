# Sutra प.8.3.25: मो राजि समः क्वौ
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.25"
SUTRA_TEXT = "मो राजि समः क्वौ"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8325:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.25: अग्निः'),
		('रामः', '', 'प.8.3.25: रामः'),
		('सीता', '', 'प.8.3.25: सीता'),
	]

