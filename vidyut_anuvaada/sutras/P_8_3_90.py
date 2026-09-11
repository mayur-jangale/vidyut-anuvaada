# Sutra प.8.3.90: सूत्रं प्रतिष्णातम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.90"
SUTRA_TEXT = "सूत्रं प्रतिष्णातम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8390:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.90: अग्निः'),
		('रामः', '', 'प.8.3.90: रामः'),
		('सीता', '', 'प.8.3.90: सीता'),
	]

