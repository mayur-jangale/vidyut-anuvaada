# Sutra प.8.3.32: ङमो ह्रस्वादचि ङमुण्नित्यम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.32"
SUTRA_TEXT = "ङमो ह्रस्वादचि ङमुण्नित्यम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8332:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.32: अग्निः'),
		('रामः', '', 'प.8.3.32: रामः'),
		('सीता', '', 'प.8.3.32: सीता'),
	]

