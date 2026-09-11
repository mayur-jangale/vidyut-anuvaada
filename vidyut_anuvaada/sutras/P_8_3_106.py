# Sutra प.8.3.106: पूर्वपदात्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.106"
SUTRA_TEXT = "पूर्वपदात्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.106: अग्निः'),
		('रामः', '', 'प.8.3.106: रामः'),
		('सीता', '', 'प.8.3.106: सीता'),
	]

