# Sutra प.8.3.28: ङ्णोः कुक्टुक् शरि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.28"
SUTRA_TEXT = "ङ्णोः कुक्टुक् शरि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8328:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.28: अग्निः'),
		('रामः', '', 'प.8.3.28: रामः'),
		('सीता', '', 'प.8.3.28: सीता'),
	]

