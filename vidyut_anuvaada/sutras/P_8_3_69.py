# Sutra प.8.3.69: वेश्च स्वनो भोजने
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.69"
SUTRA_TEXT = "वेश्च स्वनो भोजने"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8369:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.69: अग्निः'),
		('रामः', '', 'प.8.3.69: रामः'),
		('सीता', '', 'प.8.3.69: सीता'),
	]

